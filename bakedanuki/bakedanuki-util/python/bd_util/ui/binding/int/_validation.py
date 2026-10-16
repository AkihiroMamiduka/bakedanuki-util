# coding: utf-8
"""符号付き32-bit整数の入力契約。"""

INT32_MIN = -(2**31)
INT32_MAX = 2**31 - 1


def require_int(value: object, argument_name: str = "value") -> int:
    """boolと暗黙変換を拒否し、符号付き32-bit整数を返す。"""
    if type(value) is not int:
        raise TypeError(f"{argument_name}にはintを指定してください")
    if not INT32_MIN <= value <= INT32_MAX:
        raise ValueError(
            f"{argument_name}は符号付き32-bit整数の範囲で指定してください"
        )
    return value


def require_step(value: object, argument_name: str = "single_step") -> int:
    """Qtで保持できる正の整数Stepを暗黙変換せず検証する。"""
    value = require_int(value, argument_name)
    if value < 1:
        raise ValueError(f"{argument_name}は1以上の整数にしてください")
    return value


def require_slider_range(minimum: object, maximum: object) -> tuple[int, int]:
    """32-bit整数の両端を検証し、操作できる昇順範囲を返す。"""
    lower = require_int(minimum, "minimum")
    upper = require_int(maximum, "maximum")
    if lower >= upper:
        raise ValueError("操作範囲はminimum < maximumにしてください")
    return lower, upper
