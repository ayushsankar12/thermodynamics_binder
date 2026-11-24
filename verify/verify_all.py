#!/usr/bin/env python3
"""Master Independent Numerical Verification Runner (verify/verify_all.py).

Auto-discovers and executes every verification module matching:
  - verify/checks/check_*.py
  - verify/checks/sec*.py

Supported module conventions (either or both):
  1. CHECKS: list of tuples
       - (check_id, fn, method_str) where fn() -> (passed: bool, detail: str)
       - or (check_id, section, description, fn, method_str)
  2. run_checks() -> list[dict] or list[tuple]
       where each dict has keys: id, section (optional), description (optional),
       passed (bool), expected (optional), computed (optional), rel_error (optional),
       tolerance (optional), detail (optional), method (optional).

Outputs:
  - verify/verification_report.json
  - verify/verification_summary.md
  - build/verification-report.md (mirror for QA scripts)
Exits 0 iff 100% of discovered checks pass.
"""
import importlib.util, json, sys, time, traceback
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

VERIFY_DIR = Path(__file__).resolve().parent
ROOT = VERIFY_DIR.parent
CHECKS_DIR = VERIFY_DIR / "checks"
JSON_OUT = VERIFY_DIR / "verification_report.json"
MD_OUT = VERIFY_DIR / "verification_summary.md"
BUILD_MD_OUT = ROOT / "build" / "verification-report.md"

sys.path.insert(0, str(VERIFY_DIR))

def normalize_record(module_name: str, item) -> dict:
    if isinstance(item, dict):
        if "passed" in item:
            passed = bool(item["passed"])
        elif "ok" in item:
            passed = bool(item["ok"])
        elif "status" in item:
            passed = str(item["status"]).strip().upper() in ("PASS", "PASSED", "OK", "TRUE")
        else:
            passed = False
        cid = str(item.get("id", item.get("check_id", "CHECK")))
        sec = str(item.get("section", module_name))
        desc = str(item.get("description", item.get("title", "")))
        detail = str(item.get("detail", ""))
        if not detail and ("expected" in item or "computed" in item):
            detail = f"expected={item.get('expected')} computed={item.get('computed')} rel_err={item.get('rel_error', 0.0)}"
        method = str(item.get("method", "Independent Python numerical check"))
        return {
            "module": module_name,
            "id": cid,
            "section": sec,
            "description": desc,
            "passed": passed,
            "expected": item.get("expected"),
            "computed": item.get("computed"),
            "rel_error": item.get("rel_error"),
            "tolerance": item.get("tolerance"),
            "detail": detail,
            "method": method,
        }
    if isinstance(item, (tuple, list)):
        if len(item) == 3:
            cid, fn_or_ok, method = item
            if callable(fn_or_ok):
                ok, detail = fn_or_ok()
            else:
                ok, detail = bool(fn_or_ok), str(method)
            return {
                "module": module_name,
                "id": str(cid),
                "section": module_name,
                "description": "",
                "passed": bool(ok),
                "expected": None,
                "computed": None,
                "rel_error": None,
                "tolerance": None,
                "detail": str(detail),
                "method": str(method),
            }
        elif len(item) >= 5:
            cid, sec, desc, fn_or_ok, method = item[:5]
            if callable(fn_or_ok):
                ok, detail = fn_or_ok()
            else:
                ok, detail = bool(fn_or_ok), ""
            return {
                "module": module_name,
                "id": str(cid),
                "section": str(sec),
                "description": str(desc),
                "passed": bool(ok),
                "expected": None,
                "computed": None,
                "rel_error": None,
                "tolerance": None,
                "detail": str(detail),
                "method": str(method),
            }
    raise ValueError(f"Unsupported check item format in {module_name}: {item!r}")

def discover_check_files() -> list[Path]:
    CHECKS_DIR.mkdir(parents=True, exist_ok=True)
    found = {}
    for pat in ("check_*.py", "sec*.py"):
        for f in sorted(CHECKS_DIR.glob(pat)):
            if f.name != "__init__.py":
                found[f.resolve()] = f
    return [found[k] for k in sorted(found)]

def main():
    t0 = time.time()
    files = discover_check_files()
    records = []
    for f in files:
        mod_name = f.stem
        spec = importlib.util.spec_from_file_location(mod_name, f)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
        except Exception:
            tb = traceback.format_exc(limit=2).strip().splitlines()[-1]
            records.append({
                "module": mod_name,
                "id": f"{mod_name}:IMPORT",
                "section": mod_name,
                "description": "Module import",
                "passed": False,
                "expected": "clean import",
                "computed": tb,
                "rel_error": None,
                "tolerance": None,
                "detail": tb,
                "method": "Python module loader",
            })
            continue

        ran_module = False
        if hasattr(mod, "run_checks") and callable(mod.run_checks):
            ran_module = True
            try:
                out = mod.run_checks()
                for item in out:
                    records.append(normalize_record(mod_name, item))
            except Exception as e:
                records.append({
                    "module": mod_name,
                    "id": f"{mod_name}:RUN_CHECKS",
                    "section": mod_name,
                    "description": "run_checks() execution",
                    "passed": False,
                    "expected": None,
                    "computed": repr(e),
                    "rel_error": None,
                    "tolerance": None,
                    "detail": f"exception: {e!r}",
                    "method": "run_checks()",
                })

        if hasattr(mod, "CHECKS") and not ran_module:
            ran_module = True
            for item in getattr(mod, "CHECKS", []):
                try:
                    records.append(normalize_record(mod_name, item))
                except Exception as e:
                    cid = item[0] if isinstance(item, (tuple, list)) and item else "CHECK"
                    records.append({
                        "module": mod_name,
                        "id": str(cid),
                        "section": mod_name,
                        "description": "",
                        "passed": False,
                        "expected": None,
                        "computed": repr(e),
                        "rel_error": None,
                        "tolerance": None,
                        "detail": f"exception: {e!r}",
                        "method": "CHECKS tuple",
                    })

    dt = time.time() - t0
    n_total = len(records)
    n_pass = sum(1 for r in records if r["passed"])
    n_fail = n_total - n_pass

    report_obj = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "python_version": sys.version.split()[0],
        "modules_discovered": [f.name for f in files],
        "total_checks": n_total,
        "passed_checks": n_pass,
        "failed_checks": n_fail,
        "elapsed_seconds": round(dt, 3),
        "all_passed": (n_fail == 0),
        "checks": records,
    }
    JSON_OUT.write_text(json.dumps(report_obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    md_lines = [
        "# Independent Numerical Verification Summary (`verify/verify_all.py`)",
        "",
        f"- **Date:** `{report_obj['timestamp']}`",
        f"- **Python Interpreter:** `{sys.executable}` (`{report_obj['python_version']}`)",
        f"- **Modules Executed:** `{len(files)}`",
        f"- **Total Checks Run:** **`{n_total}`** | **Passed:** **`{n_pass}`** | **Failed:** **`{n_fail}`** | **Elapsed:** `{dt:.2f} s`",
        "",
        "| Module | Check ID | Section | Result | Detail | Verification Method |",
        "|---|---|---|---|---|---|",
    ]
    for r in records:
        res_str = "PASS" if r["passed"] else "**FAIL**"
        det = str(r["detail"]).replace("|", "\\|")
        meth = str(r["method"]).replace("|", "\\|")
        md_lines.append(f"| `{r['module']}` | `{r['id']}` | `{r['section']}` | {res_str} | {det} | {meth} |")

    md_text = "\n".join(md_lines) + "\n"
    MD_OUT.write_text(md_text, encoding="utf-8")
    BUILD_MD_OUT.parent.mkdir(parents=True, exist_ok=True)
    BUILD_MD_OUT.write_text(md_text, encoding="utf-8")

    print(f"verify_all: modules={len(files)} checks={n_total} passed={n_pass} failed={n_fail} time={dt:.2f}s")
    for r in records:
        if not r["passed"]:
            print(f"  FAIL [{r['module']}] {r['id']}: {r['detail']}")
    return 1 if n_fail > 0 else 0

if __name__ == "__main__":
    sys.exit(main())
