# coding: utf-8


def require_string(value: object, argument_name: str = "value") -> str:
    """暗黙変換せず、文字列だけを受け付ける。"""
    if not isinstance(value, str):
        raise TypeError(
            f"{argument_name}にはstrを指定してください: {type(value).__name__}"
        )
    return value
