# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.string import DataStringField


class AnimatedEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NOTANIMATED = 0
    ANIMATED = 1
    ANIMATEDNOCALLBACK = 2


class AnimatedEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NOTANIMATED = 0
    ANIMATED = 1
    ANIMATEDNOCALLBACK = 2

    NAME_MAP = {
        NOTANIMATED: "NotAnimated",
        ANIMATED: "Animated",
        ANIMATEDNOCALLBACK: "AnimatedNoCallback",
    }


class AnimatedEnumField(
    EnumField[AnimatedEnumAttrOperator, AnimatedEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AnimatedEnumAttrOperator
    PLUG_CLS = AnimatedEnumPlugOperator


class UnitOptionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ALL = 0
    NONE = 1
    ANGULARONLY = 2


class UnitOptionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ALL = 0
    NONE = 1
    ANGULARONLY = 2

    NAME_MAP = {
        ALL: "All",
        NONE: "None",
        ANGULARONLY: "AngularOnly",
    }


class UnitOptionEnumField(
    EnumField[UnitOptionEnumAttrOperator, UnitOptionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UnitOptionEnumAttrOperator
    PLUG_CLS = UnitOptionEnumPlugOperator


class Expression(DG):
    __slots__ = ()

    NODE_TYPE = "expression"

    input = DoubleField(multi=True)
    in_ = input

    output = DoubleField(multi=True)
    out = output

    object = DataStringField()
    ob = object

    attribute = DataStringField()
    a = attribute

    expression = DataStringField()
    e = expression

    exprConnCount = LongField()
    xcc = exprConnCount

    internalExpression = DataStringField()
    ixp = internalExpression

    time = TimeField()
    tim = time

    frame = TimeField()
    frm = frame

    lastTimeEvaluated = TimeField()
    lte = lastTimeEvaluated

    evaluateNow = ShortField()
    xen = evaluateNow

    animated = AnimatedEnumField()
    ani = animated

    newFileFormat = ShortField()
    nff = newFileFormat

    objectMsg = MessageField()
    obm = objectMsg

    unitOption = UnitOptionEnumField()
    uno = unitOption
