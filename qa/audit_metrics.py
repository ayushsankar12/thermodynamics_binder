#!/usr/bin/env python3
"""Readability & structure audit for the binder PDFs (qa/audit_metrics.py).

Per page:   word count, smallest font size, share of characters under 8 pt
            (all text, and excluding sub/superscripts), flag if < 250 words.
Whole PDF:  literal "**" (markdown leaking into LaTeX), empty section headings
            (a heading followed directly by another heading or by the page end),
            figure captions with no "How to read" line, summary statistics.

Font sizes are PDF points (1/72 in). TeX's 8 pt (1/72.27 in) prints as 7.97 pt,
so "under 8 pt" means size < 7.9 pt here; true 8 pt TeX text is not flagged.

Sub/superscripts: a small span (< 7.9 pt) is treated as a script when it touches
(<= 1.6 pt gap) a larger span on an overlapping baseline band in the same block.
Running header/footer bands and rotated thumb-tab text are excluded from counts.

Usage:
  python qa/audit_metrics.py                          # all PDFs in output/
  python qa/audit_metrics.py output/X.pdf --label baseline
Writes qa/metrics/<label>_<pdfstem>.json and qa/metrics/<label>_summary.md.
"""
import argparse, json, re, statistics, sys
from pathlib import Path

try:
    import pymupdf as fitz
except ImportError:  # older PyMuPDF
    import fitz

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

QA_DIR = Path(__file__).resolve().parent
ROOT = QA_DIR.parent
OUT = ROOT / "output"
METRICS = QA_DIR / "metrics"

SMALL_PT = 7.9          # "under 8 pt" (see module docstring)
TINY_PT = 7.5           # legacy baseline statistic
LOW_WORDS = 250
HEADER_Y = 62.0         # spans ending above this are the running head
FOOTER_Y = 738.0        # spans starting below this are the running foot
SCRIPT_GAP = 1.6        # pt, horizontal adjacency for sub/superscript detection

HEADING_RE = re.compile(r"^(§\s?\d+(\.\d+)*|App\.\s?[A-H](\.\d+)?)\s*[A-Z(]")
FIG_RE = re.compile(r"^Fig\.\s?(\d+|[A-H])\.\d+[a-z]?\.")
HOWTO_RE = re.compile(r"how to read", re.I)


def is_bold_sans(font: str) -> bool:
    f = font.lower()
    sans = any(k in f for k in ("helvet", "nimbussan", "uhv", "sans", "arial"))
    bold = any(k in f for k in ("bold", "-b", "bd", "black", "heavy"))
    return sans and bold


def page_spans(page):
    """Yield (block_no, span dict) for horizontal body text."""
    d = page.get_text("dict")
    for bno, b in enumerate(d["blocks"]):
        for ln in b.get("lines", []):
            dx, dy = ln.get("dir", (1, 0))
            if abs(dy) > 0.01 or dx < 0.99:
                continue  # rotated thumb-tab labels etc.
            for sp in ln["spans"]:
                t = sp["text"]
                if not t.strip():
                    continue
                x0, y0, x1, y1 = sp["bbox"]
                if y1 < HEADER_Y or y0 > FOOTER_Y:
                    continue
                yield bno, sp


def classify_scripts(spans):
    """Return set of indices of small spans that look like sub/superscripts."""
    by_block = {}
    for i, (bno, sp) in enumerate(spans):
        by_block.setdefault(bno, []).append(i)
    scripts = set()
    for idxs in by_block.values():
        bigs = [i for i in idxs if spans[i][1]["size"] >= SMALL_PT]
        for i in idxs:
            sp = spans[i][1]
            if sp["size"] >= SMALL_PT:
                continue
            x0, y0, x1, y1 = sp["bbox"]
            for j in bigs:
                bx0, by0, bx1, by1 = spans[j][1]["bbox"]
                hgap = max(bx0 - x1, x0 - bx1, 0.0)
                vover = min(y1, by1) - max(y0, by0)
                if hgap <= SCRIPT_GAP and vover > -2.0:
                    scripts.add(i)
                    break
            else:
                # small span sandwiched between other small spans that are scripts of a big one
                # (e.g. multi-character subscripts split into several spans) — check neighbours
                for j in idxs:
                    if j in scripts and j != i:
                        bx0, by0, bx1, by1 = spans[j][1]["bbox"]
                        hgap = max(bx0 - x1, x0 - bx1, 0.0)
                        vover = min(y1, by1) - max(y0, by0)
                        if hgap <= 0.6 and vover > 0:
                            scripts.add(i)
                            break
    return scripts


def heading_lines(page):
    """Return list of (y0, text, is_heading) for text lines in reading order (body only)."""
    d = page.get_text("dict")
    out = []
    for b in d["blocks"]:
        for ln in b.get("lines", []):
            dx, dy = ln.get("dir", (1, 0))
            if abs(dy) > 0.01 or dx < 0.99:
                continue
            spans = [s for s in ln["spans"] if s["text"].strip()]
            if not spans:
                continue
            x0, y0, x1, y1 = ln["bbox"]
            if y1 < HEADER_Y or y0 > FOOTER_Y:
                continue
            text = "".join(s["text"] for s in spans).strip()
            size = max(s["size"] for s in spans)
            bold = all(is_bold_sans(s["font"]) for s in spans)
            big_bold = bold and size >= 10.4
            is_head = big_bold and bool(HEADING_RE.match(text))
            out.append((y0, x0, text, is_head, big_bold))
    out.sort(key=lambda r: (round(r[0], 0), r[1]))
    # merge wrapped heading continuation lines (large bold sans, no leading section number)
    merged = []
    for row in out:
        if merged and merged[-1][3] and row[4] and not row[3]:
            y0, x0, text, is_head, big = merged[-1]
            merged[-1] = (y0, x0, text + " " + row[2], is_head, big)
            continue
        merged.append(row)
    return [r[:4] for r in merged]


def audit_pdf(pdf: Path):
    doc = fitz.open(pdf)
    pages = []
    star_hits, empty_heads, fig_no_howto = [], [], []
    tot_chars = tot_small = tot_small_noscript = tot_tiny = 0
    min_font_all = 99.0
    for i, page in enumerate(doc):
        pno = i + 1
        spans = list(page_spans(page))
        scripts = classify_scripts(spans)
        chars = small = small_ns = tiny = 0
        min_font = 99.0
        min_font_ns = 99.0
        words = len(page.get_text("words"))  # same definition as the stated baseline (whole page)
        for k, (_, sp) in enumerate(spans):
            t = sp["text"]
            n = len(re.sub(r"\s", "", t))
            sz = sp["size"]
            chars += n
            min_font = min(min_font, sz)
            if sz < SMALL_PT:
                small += n
                if k not in scripts:
                    small_ns += n
                    min_font_ns = min(min_font_ns, sz)
            else:
                min_font_ns = min(min_font_ns, sz)
            if sz < TINY_PT:
                tiny += n
        txt = page.get_text("text")
        if "**" in txt:
            star_hits.append(pno)
        # empty headings
        lines = heading_lines(page)
        for j, (y0, x0, text, is_head) in enumerate(lines):
            if not is_head:
                continue
            nxt = lines[j + 1] if j + 1 < len(lines) else None
            if nxt is None or nxt[3]:
                empty_heads.append({"page": pno, "heading": text[:80],
                                    "reason": "page end" if nxt is None else f"followed by heading '{nxt[2][:50]}'"})
        # figure captions without a How-to-read line
        blocks = page.get_text("blocks")
        for bi, blk in enumerate(blocks):
            btxt = blk[4].strip()
            m = FIG_RE.match(btxt)
            if not m:
                continue
            tail = btxt + " " + " ".join(b[4] for b in blocks[bi + 1:bi + 3])
            if not HOWTO_RE.search(tail):
                fig_no_howto.append({"page": pno, "caption": re.sub(r"\s+", " ", btxt)[:90]})
        pages.append({
            "page": pno, "words": words, "chars": chars,
            "min_font": round(min_font, 2) if chars else None,
            "min_font_nonscript": round(min_font_ns, 2) if chars else None,
            "share_under_8pt": round(small / chars, 4) if chars else 0.0,
            "share_under_8pt_nonscript": round(small_ns / chars, 4) if chars else 0.0,
            "share_under_7p5pt": round(tiny / chars, 4) if chars else 0.0,
            "low_words": words < LOW_WORDS,
        })
        tot_chars += chars
        tot_small += small
        tot_small_noscript += small_ns
        tot_tiny += tiny
        if chars:
            min_font_all = min(min_font_all, min_font)
    doc.close()
    words = [p["words"] for p in pages]
    summary = {
        "pdf": pdf.name,
        "pages": len(pages),
        "median_words_per_page": statistics.median(words) if words else 0,
        "mean_words_per_page": round(statistics.mean(words), 1) if words else 0,
        "total_chars": tot_chars,
        "share_chars_under_8pt": round(tot_small / tot_chars, 4) if tot_chars else 0,
        "share_chars_under_8pt_nonscript": round(tot_small_noscript / tot_chars, 4) if tot_chars else 0,
        "chars_under_8pt_nonscript": tot_small_noscript,
        "share_chars_under_7p5pt": round(tot_tiny / tot_chars, 4) if tot_chars else 0,
        "pages_mostly_under_8pt": [p["page"] for p in pages if p["share_under_8pt"] > 0.5],
        "pages_under_250_words": [p["page"] for p in pages if p["low_words"]],
        "min_font_pt": round(min_font_all, 2),
        "literal_double_star_pages": star_hits,
        "empty_headings": empty_heads,
        "figure_captions_without_how_to_read": fig_no_howto,
    }
    return summary, pages


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("pdfs", nargs="*")
    ap.add_argument("--label", default="current")
    args = ap.parse_args()
    pdfs = [Path(p).resolve() for p in args.pdfs] if args.pdfs else sorted(OUT.glob("*.pdf"))
    METRICS.mkdir(parents=True, exist_ok=True)
    md = [f"# Audit metrics — `{args.label}`", "",
          "| PDF | Pages | Median words/pg | Chars < 8 pt | < 8 pt excl. scripts | Chars < 7.5 pt | Pages mostly < 8 pt | Pages < 250 words | Min font | `**` pages | Empty headings | Figs w/o How-to-read |",
          "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    detail = []
    for pdf in pdfs:
        s, pages = audit_pdf(pdf)
        (METRICS / f"{args.label}_{pdf.stem}.json").write_text(
            json.dumps({"summary": s, "pages": pages}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        md.append(f"| `{s['pdf']}` | {s['pages']} | {s['median_words_per_page']} | "
                  f"{100*s['share_chars_under_8pt']:.1f}% | {100*s['share_chars_under_8pt_nonscript']:.1f}% | "
                  f"{100*s['share_chars_under_7p5pt']:.1f}% | {len(s['pages_mostly_under_8pt'])} | "
                  f"{len(s['pages_under_250_words'])} | {s['min_font_pt']} | {len(s['literal_double_star_pages'])} | "
                  f"{len(s['empty_headings'])} | {len(s['figure_captions_without_how_to_read'])} |")
        detail += ["", f"## `{s['pdf']}`", "",
                   f"- Pages mostly under 8 pt: {s['pages_mostly_under_8pt']}",
                   f"- Pages under 250 words: {s['pages_under_250_words']}",
                   f"- Literal `**` on pages: {s['literal_double_star_pages']}",
                   f"- Empty headings: " + ("; ".join(f"p{e['page']} {e['heading']!r} ({e['reason']})" for e in s['empty_headings']) or "none"),
                   f"- Figure captions without a How-to-read line: {len(s['figure_captions_without_how_to_read'])} "
                   + (f"(first: p{s['figure_captions_without_how_to_read'][0]['page']})" if s['figure_captions_without_how_to_read'] else "")]
        print(f"{s['pdf']}: pages={s['pages']} median_words={s['median_words_per_page']} "
              f"under8={100*s['share_chars_under_8pt']:.1f}% under8_nonscript={100*s['share_chars_under_8pt_nonscript']:.1f}% "
              f"under7.5={100*s['share_chars_under_7p5pt']:.1f}% mostly<8pt={len(s['pages_mostly_under_8pt'])} "
              f"<250w={len(s['pages_under_250_words'])} min_font={s['min_font_pt']} **={len(s['literal_double_star_pages'])} "
              f"empty_heads={len(s['empty_headings'])} figs_no_howto={len(s['figure_captions_without_how_to_read'])}")
    (METRICS / f"{args.label}_summary.md").write_text("\n".join(md + detail) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
