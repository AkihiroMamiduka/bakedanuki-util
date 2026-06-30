# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class EnableStatusEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ENABLE_ALL = 0
    DISABLE_ALL = 1


class EnableStatusEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ENABLE_ALL = 0
    DISABLE_ALL = 1

    NAME_MAP = {
        ENABLE_ALL: "Enable All",
        DISABLE_ALL: "Disable All",
    }


class EnableStatusEnumField(
    EnumField[EnableStatusEnumAttrOperator, EnableStatusEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EnableStatusEnumAttrOperator
    PLUG_CLS = EnableStatusEnumPlugOperator


class GlobalCacheControl(DG):
    __slots__ = ()

    NODE_TYPE = "globalCacheControl"

    enableStatus = EnableStatusEnumField()
    ebls = enableStatus

    writeEnable = BoolField()
    webl = writeEnable
