# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.dt.string import DataStringField


class ModeEnumPlugOperator(EnumPlugOperator["ModeEnumAttrOperator"]):
    __slots__ = ()

    DISABLE = 0
    ENABLE = 1


class ModeEnumAttrOperator(EnumAttrOperator[ModeEnumPlugOperator]):
    __slots__ = ()

    DISABLE = 0
    ENABLE = 1

    NAME_MAP = {
        DISABLE: "disable",
        ENABLE: "enable",
    }


class ModeEnumField(EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class GeneratedAiDisable(DG):
    __slots__ = ()

    NODE_TYPE = "aiDisable"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    inputs = MessageField(multi=True)

    selection = DataStringField()

    mode = ModeEnumField(default_value=0)

    shapes = BoolField(default_value=True)

    lights = BoolField(default_value=True)

    shaders = BoolField(default_value=True)

    operators = BoolField(default_value=True)
