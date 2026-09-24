from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from maya.api import OpenMaya as om


@dataclass(frozen=True)
class Influence:
    start: om.MTime | None
    end: om.MTime | None
    fade_start: om.MTime | None
    fade_end: om.MTime | None
    interpolation: Literal["linear", "smoothstep"]

    def __post_init__(self) -> None:
        if self.interpolation not in ("linear", "smoothstep"):
            raise ValueError("interpolation must be 'linear' or 'smoothstep'.")
        if (
            self.start is not None
            and self.end is not None
            and self.start > self.end
        ):
            raise ValueError(
                "start_frame must be less than or equal to end_frame."
            )
        if self.fade_start is not None and (
            self.start is None or self.fade_start >= self.start
        ):
            raise ValueError(
                "interpolate_start requires an explicit, later start_frame."
            )
        if self.fade_end is not None and (
            self.end is None or self.fade_end <= self.end
        ):
            raise ValueError(
                "interpolate_end requires an explicit, earlier end_frame."
            )

    @property
    def low(self) -> om.MTime | None:
        return self.start if self.fade_start is None else self.fade_start

    @property
    def high(self) -> om.MTime | None:
        return self.end if self.fade_end is None else self.fade_end

    @property
    def boundaries(self) -> tuple[om.MTime | None, ...]:
        return self.fade_start, self.start, self.end, self.fade_end

    def weight(self, time: om.MTime) -> float:
        u = 1.0
        if self.start is not None and time < self.start:
            assert self.fade_start is not None
            u = (time - self.fade_start).asUnits(om.MTime.kSeconds) / (
                self.start - self.fade_start
            ).asUnits(om.MTime.kSeconds)
        elif self.end is not None and time > self.end:
            assert self.fade_end is not None
            u = (self.fade_end - time).asUnits(om.MTime.kSeconds) / (
                self.fade_end - self.end
            ).asUnits(om.MTime.kSeconds)
        u = max(0.0, min(1.0, u))
        return u if self.interpolation == "linear" else u * u * (3 - 2 * u)
