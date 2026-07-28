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


class OsEnumPlugOperator(EnumPlugOperator["OsEnumAttrOperator"]):
    __slots__ = ()

    ANY = 0
    LINUX = 1
    WINDOWS = 2
    MAC = 3


class OsEnumAttrOperator(EnumAttrOperator[OsEnumPlugOperator]):
    __slots__ = ()

    ANY = 0
    LINUX = 1
    WINDOWS = 2
    MAC = 3

    NAME_MAP = {
        ANY: "any",
        LINUX: "linux",
        WINDOWS: "windows",
        MAC: "mac",
    }


class OsEnumField(
    EnumField[OsEnumAttrOperator, OsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OsEnumAttrOperator
    PLUG_CLS = OsEnumPlugOperator


class GeneratedAiStringReplace(DG):
    __slots__ = ()

    NODE_TYPE = "aiStringReplace"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    inputs = MessageField(multi=True)

    selection = DataStringField()

    match = DataStringField()

    replace = DataStringField()

    os = OsEnumField(default_value=0)
