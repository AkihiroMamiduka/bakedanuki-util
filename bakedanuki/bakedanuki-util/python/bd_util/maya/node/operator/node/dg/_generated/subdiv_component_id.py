# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class InLevelEnumPlugOperator(EnumPlugOperator["InLevelEnumAttrOperator"]):
    __slots__ = ()

    BASE_0 = 0
    COARSE_1 = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6
    _7 = 7
    _8 = 8
    _9 = 9
    _10 = 10
    _11 = 11
    FINEST_12 = 12


class InLevelEnumAttrOperator(EnumAttrOperator[InLevelEnumPlugOperator]):
    __slots__ = ()

    BASE_0 = 0
    COARSE_1 = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6
    _7 = 7
    _8 = 8
    _9 = 9
    _10 = 10
    _11 = 11
    FINEST_12 = 12

    NAME_MAP = {
        BASE_0: "Base 0",
        COARSE_1: "Coarse 1",
        _2: "2",
        _3: "3",
        _4: "4",
        _5: "5",
        _6: "6",
        _7: "7",
        _8: "8",
        _9: "9",
        _10: "10",
        _11: "11",
        FINEST_12: "Finest 12",
    }


class InLevelEnumField(
    EnumField[InLevelEnumAttrOperator, InLevelEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InLevelEnumAttrOperator
    PLUG_CLS = InLevelEnumPlugOperator


class InFinalEnumPlugOperator(EnumPlugOperator["InFinalEnumAttrOperator"]):
    __slots__ = ()

    _0 = 0
    _1 = 1
    _2 = 2
    _3 = 3


class InFinalEnumAttrOperator(EnumAttrOperator[InFinalEnumPlugOperator]):
    __slots__ = ()

    _0 = 0
    _1 = 1
    _2 = 2
    _3 = 3

    NAME_MAP = {
        _0: "0",
        _1: "1",
        _2: "2",
        _3: "3",
    }


class InFinalEnumField(
    EnumField[InFinalEnumAttrOperator, InFinalEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InFinalEnumAttrOperator
    PLUG_CLS = InFinalEnumPlugOperator


class OutLevelEnumPlugOperator(EnumPlugOperator["OutLevelEnumAttrOperator"]):
    __slots__ = ()

    BASE_0 = 0
    COARSE_1 = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6
    _7 = 7
    _8 = 8
    _9 = 9
    _10 = 10
    _11 = 11
    FINEST_12 = 12


class OutLevelEnumAttrOperator(EnumAttrOperator[OutLevelEnumPlugOperator]):
    __slots__ = ()

    BASE_0 = 0
    COARSE_1 = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6
    _7 = 7
    _8 = 8
    _9 = 9
    _10 = 10
    _11 = 11
    FINEST_12 = 12

    NAME_MAP = {
        BASE_0: "Base 0",
        COARSE_1: "Coarse 1",
        _2: "2",
        _3: "3",
        _4: "4",
        _5: "5",
        _6: "6",
        _7: "7",
        _8: "8",
        _9: "9",
        _10: "10",
        _11: "11",
        FINEST_12: "Finest 12",
    }


class OutLevelEnumField(
    EnumField[OutLevelEnumAttrOperator, OutLevelEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutLevelEnumAttrOperator
    PLUG_CLS = OutLevelEnumPlugOperator


class OutFinalEnumPlugOperator(EnumPlugOperator["OutFinalEnumAttrOperator"]):
    __slots__ = ()

    _0 = 0
    _1 = 1
    _2 = 2
    _3 = 3


class OutFinalEnumAttrOperator(EnumAttrOperator[OutFinalEnumPlugOperator]):
    __slots__ = ()

    _0 = 0
    _1 = 1
    _2 = 2
    _3 = 3

    NAME_MAP = {
        _0: "0",
        _1: "1",
        _2: "2",
        _3: "3",
    }


class OutFinalEnumField(
    EnumField[OutFinalEnumAttrOperator, OutFinalEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutFinalEnumAttrOperator
    PLUG_CLS = OutFinalEnumPlugOperator


class GeneratedSubdivComponentId(DG):
    __slots__ = ()

    NODE_TYPE = "subdivComponentId"

    inBase = LongField(default_value=0)
    ib = inBase

    inEdge = LongField(default_value=0)
    ie = inEdge

    inLevel = InLevelEnumField(default_value=0)
    il = inLevel

    inPath = LongField(default_value=0)
    ip = inPath

    inFinal = InFinalEnumField(default_value=0)
    if_ = inFinal

    outLeft = LongField(default_value=0, writable=False)
    olt = outLeft

    outRight = LongField(default_value=0, writable=False)
    or_ = outRight

    inLeft = LongField(default_value=0)
    ilt = inLeft

    inRight = LongField(default_value=0)
    ir = inRight

    outBase = LongField(default_value=0, writable=False)
    ob = outBase

    outEdge = LongField(default_value=0, writable=False)
    oe = outEdge

    outLevel = OutLevelEnumField(default_value=0, writable=False)
    ol = outLevel

    outPath = LongField(default_value=0, writable=False)
    op = outPath

    outFinal = OutFinalEnumField(default_value=0, writable=False)
    of = outFinal
