# coding: utf-8
from math import isfinite


def require_float(value: object, argument_name: str = "value") -> float:
    """boolと暗黙の文字列変換を拒否し、有限の浮動小数点値を返す。"""
    if isinstance(value, bool) or not isinstance(value, (float, int)):
        raise TypeError(f"{argument_name}にはfloatを指定してください")
    result = float(value)
    if not isfinite(result):
        raise ValueError(f"{argument_name}には有限の値を指定してください")
    return result


def require_decimals(value: object) -> int:
    """Qtの小数表示桁数として受け付ける整数を検証する。"""
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("decimalsにはintを指定してください")
    if not 0 <= value <= 323:
        raise ValueError("decimalsは0から323の範囲で指定してください")
    return value


def require_suffix(value: object) -> str:
    """数値の末尾へ付加する文字列を検証する。"""
    if not isinstance(value, str):
        raise TypeError("suffixにはstrを指定してください")
    return value


def require_slider_range(
    minimum: float, maximum: float
) -> tuple[float, float]:
    """有限で昇順の操作範囲を、公開単位の値として検証する。"""
    minimum = require_float(minimum, "minimum")
    maximum = require_float(maximum, "maximum")
    if minimum >= maximum:
        raise ValueError("minimumはmaximum未満にしてください")
    return minimum, maximum


def require_slider_steps(value: object) -> int:
    """Qtの整数位置に収まる正の分割数を検証する。"""
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("stepsには整数を指定してください")
    if not 1 <= value <= 2147483647:
        raise ValueError("stepsは1～2147483647にしてください")
    return value
