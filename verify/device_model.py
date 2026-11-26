#!/usr/bin/env python3
"""Single source of truth for the REFERENCE COLLECTOR model (modeled, not your device).

Every §16 lookup table, the Fig. 16.2 nomogram and the worked examples that read from
them are generated from (and checked against) the numbers in this file:

  * TG125_10MIN  - 10-minute top-layer gain [C] under a 125 W lamp at the 5-cm anchor
                   heights, T_start = T_room = 22.0 C (the calibration base);
  * piecewise-linear 1-cm interpolation between anchors (the calculator program in §16
    uses the same slopes);
  * TAU_EFF      - effective top-layer time constant [s] (fitted, see Ex 13.2 / 16.2b);
  * ETA_100      - 100 W / 125 W absorbed-power ratio;
  * M_t, k_start, k_room - time scaling from 10 min to 11-15 min.

Replace these with your own measured runs; they describe the reference design only.

Run `python verify/device_model.py` to print every derived table.
"""
import math

TAU_EFF = 903.0            # s
ETA_100 = 0.800            # 100 W relative to 125 W
T_REF_START = 22.0         # C, T_start = T_room for the table runs
TG125_10MIN = {40: 24.8, 45: 27.7, 50: 21.3, 55: 17.5, 60: 13.6, 65: 10.6}
ANCHORS = sorted(TG125_10MIN)


def tg125_10(h_cm: float) -> float:
    """10-min, 125 W gain at any height 40-65 cm (linear between 5-cm anchors)."""
    if not 40 <= h_cm <= 65:
        raise ValueError("height outside 40-65 cm")
    for lo, hi in zip(ANCHORS, ANCHORS[1:]):
        if lo <= h_cm <= hi:
            f = (h_cm - lo) / (hi - lo)
            return TG125_10MIN[lo] + f * (TG125_10MIN[hi] - TG125_10MIN[lo])
    return TG125_10MIN[65]


def m_t(t_min: float) -> float:
    """Time multiplier relative to 10 min."""
    return (1 - math.exp(-60 * t_min / TAU_EFF)) / (1 - math.exp(-600 / TAU_EFF))


def k_start(t_min: float) -> float:
    return math.exp(-60 * t_min / TAU_EFF)


def k_room(t_min: float) -> float:
    return 1 - k_start(t_min)


def tg_table(h_cm: float, watts: int, t_min: float) -> float:
    """TG_table(h, P, t) [C] for T_start = T_room."""
    eta = 1.0 if watts == 125 else ETA_100
    return tg125_10(h_cm) * eta * m_t(t_min)


def dT_ss(h_cm: float, watts: int = 125) -> float:
    """Asymptotic gain implied by the 10-min value and tau."""
    eta = 1.0 if watts == 125 else ETA_100
    return tg125_10(h_cm) * eta / (1 - math.exp(-600 / TAU_EFF))


def t_pred(h_cm, watts, t_min, T_start, T_room, dT_cool):
    """The binder's single prediction formula (all in C)."""
    return T_start + tg_table(h_cm, watts, t_min) + k_room(t_min) * (T_room - T_start) - dT_cool


def r1(x: float) -> str:
    """Round half up to 0.1 for printing (avoids banker's rounding of x.x5)."""
    return f"{math.floor(x * 10 + 0.5 + 1e-9) / 10:.1f}"


if __name__ == "__main__":
    print("t  M_t     k_start k_room")
    for t in range(10, 16):
        print(f"{t}  {m_t(t):.4f}  {k_start(t):.3f}   {k_room(t):.3f}")
    print("\nh   125W: 10   11   12   13   14   15  | 100W: 10   11   12   13   14   15 | dTss125")
    for h in ANCHORS:
        a = [r1(tg_table(h, 125, t)) for t in range(10, 16)]
        b = [r1(tg_table(h, 100, t)) for t in range(10, 16)]
        print(h, " ".join(a), "|", " ".join(b), "|", r1(dT_ss(h)))
    print("\n1-cm table: h TG125 TG100")
    for h in range(40, 66):
        print(h, r1(tg125_10(h)), r1(ETA_100 * tg125_10(h)))
