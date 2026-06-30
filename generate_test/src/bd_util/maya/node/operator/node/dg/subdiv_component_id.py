# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class InLevelEnumPlugOperator(EnumPlugOperator):
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


class InLevelEnumAttrOperator(EnumAttrOperator):
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


class InFinalEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _0 = 0
    _1 = 1
    _2 = 2
    _3 = 3


class InFinalEnumAttrOperator(EnumAttrOperator):
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


class OutLevelEnumPlugOperator(EnumPlugOperator):
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


class OutLevelEnumAttrOperator(EnumAttrOperator):
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


class OutFinalEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _0 = 0
    _1 = 1
    _2 = 2
    _3 = 3


class OutFinalEnumAttrOperator(EnumAttrOperator):
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


class SubdivComponentId(DG):
    __slots__ = ()

    NODE_TYPE = "subdivComponentId"

    inBase = LongField()
    ib = inBase

    inEdge = LongField()
    ie = inEdge

    inLevel = InLevelEnumField()
    il = inLevel

    inPath = LongField()
    ip = inPath

    inFinal = InFinalEnumField()
    if_ = inFinal

    outLeft = LongField()
    olt = outLeft

    outRight = LongField()
    or_ = outRight

    inLeft = LongField()
    ilt = inLeft

    inRight = LongField()
    ir = inRight

    outBase = LongField()
    ob = outBase

    outEdge = LongField()
    oe = outEdge

    outLevel = OutLevelEnumField()
    ol = outLevel

    outPath = LongField()
    op = outPath

    outFinal = OutFinalEnumField()
    of = outFinal
