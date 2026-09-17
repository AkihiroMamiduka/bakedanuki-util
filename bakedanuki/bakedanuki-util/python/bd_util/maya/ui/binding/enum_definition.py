# coding: utf-8
"""callbackを作らず、既存Maya enum属性の実定義を取得する。"""

from ....ui import EnumDefinition
from ._enum_plug_value import EnumPlugValue
from .enum_plug_resolver import MayaEnumPlug, require_enum_plug

__all__ = ["read_enum_definition"]


def read_enum_definition(plug: MayaEnumPlug) -> EnumDefinition:
    """scalar enumの現在の定義を読み、scene・値・Undoを変更しない。"""
    return EnumPlugValue(require_enum_plug(plug).plug).definition
