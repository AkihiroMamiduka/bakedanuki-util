# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.dt.string import DataStringField


class AssignPlugOperator(CompoundPlugOperator["AssignAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("componentTagExpression", "gtg"),
        ("shadingEngine", "shd"),
    )

    componentTagExpression = DataStringField()
    gtg = componentTagExpression

    shadingEngine = MessageField()
    shd = shadingEngine


class AssignAttrOperator(CompoundAttrOperator[AssignPlugOperator]):
    __slots__ = ()

    componentTagExpression = DataStringField()
    gtg = componentTagExpression

    shadingEngine = MessageField()
    shd = shadingEngine


class AssignField(CompoundField[AssignAttrOperator, AssignPlugOperator]):
    __slots__ = ()

    ATTR_CLS = AssignAttrOperator
    PLUG_CLS = AssignPlugOperator
