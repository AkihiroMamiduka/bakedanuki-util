# coding: utf-8
"""一括値入力と値Pasteで共有するenum定義の検証方針。"""

from typing import Literal


def require_enum_validation(
    value: object,
) -> Literal["per_write", "operation"]:
    """動的呼出しからも既知のenum検証方針だけを受け付ける。"""
    if value == "per_write":
        return "per_write"
    if value == "operation":
        return "operation"
    raise ValueError("enum_validationにはper_writeまたはoperationを指定します")
