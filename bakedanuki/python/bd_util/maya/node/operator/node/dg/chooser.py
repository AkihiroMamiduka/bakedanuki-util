# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class DisplayLevelEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    USELOD = 0
    SHOW = 1
    HIDE = 2


class DisplayLevelEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    USELOD = 0
    SHOW = 1
    HIDE = 2

    NAME_MAP = {
        USELOD: "uselod",
        SHOW: "show",
        HIDE: "hide",
    }


class DisplayLevelEnumField(
    EnumField[DisplayLevelEnumAttrOperator, DisplayLevelEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplayLevelEnumAttrOperator
    PLUG_CLS = DisplayLevelEnumPlugOperator


class Chooser(DG):
    __slots__ = ()

    NODE_TYPE = "chooser"

    inLevel = BoolField(multi=True, default_value=False)
    il = inLevel

    displayLevel = DisplayLevelEnumField(multi=True, default_value=0)
    dl = displayLevel

    output = BoolField(multi=True, default_value=False, writable=False)
    o = output
