# coding: utf-8
"""Maya の数値属性に共通する十進の四捨五入。"""

from decimal import Decimal, ROUND_HALF_UP, localcontext
from math import isfinite
from typing import Literal

from maya.api import OpenMaya as om

__all__ = [
    "MayaScalarKind",
    "RoundingUnit",
    "round_decimal_half_up",
    "round_maya_scalar",
]

MayaScalarKind = Literal["distance", "angle"]
RoundingUnit = Literal["canonical", "display"]


def round_decimal_half_up(value: float, ndigits: int) -> float:
    """有限値を十進で指定桁へ四捨五入し、負のゼロを正規化する。

    Args:
        value: 丸める有限値。
        ndigits: 小数点以下の桁数。負の値も指定できる。

    Returns:
        四捨五入後の値。
    """
    if isinstance(value, bool) or not isinstance(value, (float, int)):
        raise TypeError("valueにはfloatを指定してください")
    value = float(value)
    if not isfinite(value):
        raise ValueError("valueには有限の値を指定してください")
    if type(ndigits) is not int:
        raise TypeError("ndigitsにはintを指定してください")

    source = Decimal(str(value))
    quantum = Decimal(1).scaleb(-ndigits)
    # 大きな整数部と細かな小数部を併せても量子化できる精度を確保する
    with localcontext() as context:
        context.prec = max(28, source.adjusted() + ndigits + 2)
        rounded = source.quantize(quantum, rounding=ROUND_HALF_UP)
    if rounded.is_zero():
        return 0.0
    result = float(rounded)
    if not isfinite(result):
        raise ValueError("丸めた値はfloatの範囲を超えています")
    return result


def round_maya_scalar(
    value: float,
    ndigits: int,
    *,
    kind: MayaScalarKind,
    rounding_unit: RoundingUnit = "canonical",
) -> float:
    """cm・degree の値を正本とし、指定単位の十進四捨五入を行う。

    Args:
        value: 距離ならcentimeter、角度ならdegreeの値。
        ndigits: 小数点以下の桁数。負の値も指定できる。
        kind: 距離または角度の種類。
        rounding_unit: ``"canonical"`` はcm・degreeで、``"display"`` は
            Mayaの現在の表示単位で丸める。

    Returns:
        丸めた値をcentimeterまたはdegreeで返す。
    """
    if kind not in ("distance", "angle"):
        raise ValueError("kindには'distance'か'angle'を指定してください")
    if rounding_unit not in ("canonical", "display"):
        raise ValueError(
            "rounding_unitには'canonical'か'display'を指定してください"
        )
    if rounding_unit == "canonical":
        return round_decimal_half_up(value, ndigits)

    if kind == "distance":
        unit = om.MDistance.uiUnit()
        scale = om.MDistance(1.0, om.MDistance.kCentimeters).asUnits(unit)
    else:
        unit = om.MAngle.uiUnit()
        scale = om.MAngle(1.0, om.MAngle.kDegrees).asUnits(unit)
    # 既存の FloatPresentation と同じ倍率で往復し、表示値の境界を揃える
    rounded = round_decimal_half_up(value * scale, ndigits)
    result = rounded / scale
    if not isfinite(result):
        raise ValueError("丸めた値はfloatの範囲を超えています")
    return result
