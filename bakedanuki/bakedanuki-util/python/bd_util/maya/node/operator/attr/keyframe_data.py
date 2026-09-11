"""Sceneから独立したキー情報。値と接線Yはdegree / cmへ換算する。"""

from __future__ import annotations

import math
from collections.abc import Mapping
from dataclasses import asdict, dataclass, fields, replace
from typing import Literal, cast

CurveTypeName = Literal["animCurveTA", "animCurveTL", "animCurveTU"]
KeyTangentTypeName = Literal[
    "fixed",
    "auto",
    "clamped",
    "fast",
    "flat",
    "linear",
    "plateau",
    "slow",
    "spline",
    "step",
    "stepnext",
    "autocustom",
    "autoease",
    "automix",
]
InfinityTypeName = Literal[
    "constant", "linear", "cycle", "cycleRelative", "oscillate"
]

_CURVE_TYPES = ("animCurveTA", "animCurveTL", "animCurveTU")
_TANGENT_TYPES = (
    "fixed",
    "auto",
    "clamped",
    "fast",
    "flat",
    "linear",
    "plateau",
    "slow",
    "spline",
    "step",
    "stepnext",
    "autocustom",
    "autoease",
    "automix",
)
_INFINITY_TYPES = ("constant", "linear", "cycle", "cycleRelative", "oscillate")


def _number(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number.")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"{name} must be finite.")
    return result


def _boolean(value: object, name: str) -> bool:
    if not isinstance(value, bool):
        raise TypeError(f"{name} must be a bool.")
    return value


def _choice(value: object, choices: tuple[str, ...], name: str) -> str:
    if not isinstance(value, str) or value not in choices:
        raise ValueError(f"Unsupported {name}: {value!r}.")
    return value


def _xy(value: object, name: str) -> tuple[float, float]:
    if not isinstance(value, (list, tuple)):
        raise TypeError(f"{name} must contain two numbers.")
    items = cast(list[object] | tuple[object, ...], value)
    if len(items) != 2:
        raise TypeError(f"{name} must contain two numbers.")
    result = (_number(items[0], name), _number(items[1], name))
    if result[0] < 0:
        raise ValueError(f"{name} X must be nonnegative.")
    return result


def _mapping(
    value: object, cls: type[KeyData] | type[AnimCurveData]
) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise TypeError(f"{cls.__name__} data must be a mapping.")
    data = cast(Mapping[str, object], value)
    if set(data) != {field.name for field in fields(cls)}:
        raise ValueError(f"Unexpected or missing {cls.__name__} fields.")
    return data


def _key_data(value: object) -> KeyData:
    if not isinstance(value, KeyData):
        raise TypeError("keys must contain KeyData objects.")
    return replace(value)


def weighted_tangent_xy(
    xy: tuple[float, float], span_seconds: float | None
) -> tuple[float, float]:
    """nonweightedの方向をMayaのweighted tangent vectorへ換算する。"""
    if span_seconds is None or xy[0] == 0.0:
        return xy
    return span_seconds, span_seconds * (xy[1] / xy[0])


def copy_curve_data(value: object) -> AnimCurveData:
    """予約境界で再検証し、変更可能なKeyDataも独立して保持する。"""
    if not isinstance(value, AnimCurveData):
        raise TypeError("data must be AnimCurveData.")
    return replace(value)


@dataclass(slots=True, kw_only=True)
class KeyData:
    """編集可能な1キーのデータ。接線XYはweighted相当、frameは取得時のUI単位。"""

    frame: float
    value: float
    in_tangent_type: KeyTangentTypeName
    out_tangent_type: KeyTangentTypeName
    in_tangent_xy: tuple[float, float]
    out_tangent_xy: tuple[float, float]
    tangents_locked: bool
    weights_locked: bool
    breakdown: bool

    def __post_init__(self) -> None:
        for name in ("frame", "value"):
            setattr(self, name, _number(getattr(self, name), name))
        for name in ("in_tangent_type", "out_tangent_type"):
            _choice(getattr(self, name), _TANGENT_TYPES, name)
        for name in ("in_tangent_xy", "out_tangent_xy"):
            setattr(self, name, _xy(getattr(self, name), name))
        for name in ("tangents_locked", "weights_locked", "breakdown"):
            _boolean(getattr(self, name), name)

    def to_dict(self) -> dict[str, object]:
        """json.dumpsへ渡せる独立した辞書を返す。"""
        return asdict(replace(self))

    @classmethod
    def from_dict(cls, value: object) -> KeyData:
        data = _mapping(value, cls)
        return cls(
            frame=_number(data["frame"], "frame"),
            value=_number(data["value"], "value"),
            in_tangent_type=cast(
                KeyTangentTypeName,
                _choice(
                    data["in_tangent_type"], _TANGENT_TYPES, "in_tangent_type"
                ),
            ),
            out_tangent_type=cast(
                KeyTangentTypeName,
                _choice(
                    data["out_tangent_type"],
                    _TANGENT_TYPES,
                    "out_tangent_type",
                ),
            ),
            in_tangent_xy=_xy(data["in_tangent_xy"], "in_tangent_xy"),
            out_tangent_xy=_xy(data["out_tangent_xy"], "out_tangent_xy"),
            tangents_locked=_boolean(
                data["tangents_locked"], "tangents_locked"
            ),
            weights_locked=_boolean(data["weights_locked"], "weights_locked"),
            breakdown=_boolean(data["breakdown"], "breakdown"),
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class AnimCurveData:
    """カーブ全体のデータ。共通設定は不変、keysの各KeyDataは編集可能。"""

    curve_type: CurveTypeName
    seconds_per_frame: float
    weighted: bool
    pre_infinity: InfinityTypeName
    post_infinity: InfinityTypeName
    keys: tuple[KeyData, ...]
    schema_version: Literal[2] = 2

    def __post_init__(self) -> None:
        if type(self.schema_version) is not int or self.schema_version != 2:
            raise ValueError("Unsupported AnimCurveData schema_version.")
        _choice(self.curve_type, _CURVE_TYPES, "curve_type")
        rate = _number(self.seconds_per_frame, "seconds_per_frame")
        if rate <= 0:
            raise ValueError("seconds_per_frame must be positive.")
        object.__setattr__(self, "seconds_per_frame", rate)
        _boolean(self.weighted, "weighted")
        _choice(self.pre_infinity, _INFINITY_TYPES, "pre_infinity")
        _choice(self.post_infinity, _INFINITY_TYPES, "post_infinity")
        keys = tuple(_key_data(key) for key in self.keys)
        if any(a.frame >= b.frame for a, b in zip(keys, keys[1:])):
            raise ValueError("KeyData frames must be strictly increasing.")
        for key in keys:
            _number(key.frame * rate, "key time in seconds")
        object.__setattr__(self, "keys", keys)

    def to_dict(self) -> dict[str, object]:
        return asdict(copy_curve_data(self))

    @classmethod
    def from_dict(cls, value: object) -> AnimCurveData:
        data = _mapping(value, cls)
        if (
            type(data["schema_version"]) is not int
            or data["schema_version"] != 2
        ):
            raise ValueError("Unsupported AnimCurveData schema_version.")
        keys = data["keys"]
        if not isinstance(keys, (list, tuple)):
            raise TypeError("keys must be a list or tuple.")
        return cls(
            curve_type=cast(
                CurveTypeName,
                _choice(data["curve_type"], _CURVE_TYPES, "curve_type"),
            ),
            seconds_per_frame=_number(
                data["seconds_per_frame"], "seconds_per_frame"
            ),
            weighted=_boolean(data["weighted"], "weighted"),
            pre_infinity=cast(
                InfinityTypeName,
                _choice(data["pre_infinity"], _INFINITY_TYPES, "pre_infinity"),
            ),
            post_infinity=cast(
                InfinityTypeName,
                _choice(
                    data["post_infinity"], _INFINITY_TYPES, "post_infinity"
                ),
            ),
            keys=tuple(
                KeyData.from_dict(key)
                for key in cast(list[object] | tuple[object, ...], keys)
            ),
        )
