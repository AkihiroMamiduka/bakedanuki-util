"""Bezier区間の誤差上界。判定できない区間は削減を許可しない。"""

from __future__ import annotations

import math
from dataclasses import dataclass

_Four = tuple[float, float, float, float]


def _split(values: _Four, u: float) -> tuple[_Four, _Four]:
    a, b, c, d = values
    ab, bc, cd = a + (b - a) * u, b + (c - b) * u, c + (d - c) * u
    abc, bcd = ab + (bc - ab) * u, bc + (cd - bc) * u
    middle = abc + (bcd - abc) * u
    return (a, ab, abc, middle), (middle, bcd, cd, d)


@dataclass(frozen=True, slots=True)
class Bezier:
    x: _Four
    y: _Four
    supported: bool = True
    linear_x: bool = False

    def split(self, time: float) -> tuple[Bezier, Bezier]:
        start, end = self.x[0], self.x[-1]
        span = end - start
        linear = (start, start + span / 3, end - span / 3, end)
        linear_x = self.linear_x or self.x == linear
        if linear_x:
            u = (time - start) / span
        else:
            low, high = 0.0, 1.0
            for _ in range(52):
                u = (low + high) / 2
                if _split(self.x, u)[0][-1] < time:
                    low = u
                else:
                    high = u
            u = (low + high) / 2
        if linear_x:
            left_span, right_span = time - start, end - time
            left_x = (start, start + left_span / 3, time - left_span / 3, time)
            right_x = (time, time + right_span / 3, end - right_span / 3, end)
        else:
            left_x, right_x = _split(self.x, u)
        left_y, right_y = _split(self.y, u)
        return (
            Bezier(left_x, left_y, self.supported, linear_x),
            Bezier(right_x, right_y, self.supported, linear_x),
        )

    def clip(self, start: float, end: float) -> Bezier:
        result = self
        if start > result.x[0]:
            result = result.split(start)[1]
        if end < result.x[-1]:
            result = result.split(end)[0]
        return result


def rounding_slack(*values: float) -> float:
    return max(1e-12, 32 * math.ulp(max(map(abs, values), default=0.0)))


def within_error(source: Bezier, result: Bezier, tolerance: float) -> bool:
    if source == result:
        return True
    if not source.supported or not result.supported:
        return False
    pending = [(source, result, 0)]
    budget = 2048
    while pending:
        a, b, depth = pending.pop()
        budget -= 1
        slack = rounding_slack(*a.y, *b.y)
        limit = tolerance + slack
        if abs(a.y[0] - b.y[0]) > limit or abs(a.y[-1] - b.y[-1]) > limit:
            return False
        if a.x == b.x:
            # 同じ時間パラメーターなら差もBezier曲線になる。
            bound = max(abs(y - z) for y, z in zip(a.y, b.y))
        else:
            # 共通の直線成分を引くと、傾斜したカーブでも狭い上界を得られる。
            start, end = a.x[0], a.x[-1]
            slope = (a.y[-1] - a.y[0]) / (end - start)
            ra = [y - a.y[0] - slope * (x - start) for x, y in zip(a.x, a.y)]
            rb = [y - a.y[0] - slope * (x - start) for x, y in zip(b.x, b.y)]
            bound = max(abs(max(ra) - min(rb)), abs(max(rb) - min(ra)))
        if bound <= limit:
            continue
        middle = (a.x[0] + a.x[-1]) / 2
        if depth >= 24 or budget <= 0 or not a.x[0] < middle < a.x[-1]:
            return False
        al, ar = a.split(middle)
        bl, br = b.split(middle)
        pending.extend(((al, bl, depth + 1), (ar, br, depth + 1)))
    return True
