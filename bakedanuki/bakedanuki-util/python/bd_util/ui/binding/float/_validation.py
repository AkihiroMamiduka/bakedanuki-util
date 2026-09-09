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
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("decimalsにはintを指定してください")
    if not 0 <= value <= 323:
        raise ValueError("decimalsは0から323の範囲で指定してください")
    return value


def require_suffix(value: object) -> str:
    if not isinstance(value, str):
        raise TypeError("suffixにはstrを指定してください")
    return value
