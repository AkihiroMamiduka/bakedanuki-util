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
