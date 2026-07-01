# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.dt.string import DataStringField


class ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DISABLE = 0
    ENABLE = 1


class ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DISABLE = 0
    ENABLE = 1

    NAME_MAP = {
        DISABLE: "disable",
        ENABLE: "enable",
    }


class ModeEnumField(
    EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class AiDisable(DG):
    __slots__ = ()

    NODE_TYPE = "aiDisable"

    out = MessageField()

    enable = BoolField()

    inputs = MessageField(multi=True)

    selection = DataStringField()

    mode = ModeEnumField()

    shapes = BoolField()

    lights = BoolField()

    shaders = BoolField()

    operators = BoolField()
