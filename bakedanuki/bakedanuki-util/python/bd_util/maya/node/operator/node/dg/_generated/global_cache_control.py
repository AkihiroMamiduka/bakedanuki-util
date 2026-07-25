# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField


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


class _GeneratedGlobalCacheControl(DG):
    __slots__ = ()

    NODE_TYPE = "globalCacheControl"

    enableStatus = EnableStatusEnumField(default_value=0)
    ebls = enableStatus

    writeEnable = BoolField(default_value=False)
    webl = writeEnable
