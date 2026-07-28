# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.dt.string import DataStringField


class AnimationPlugOperator(CompoundPlugOperator["AnimationAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("source", "as"),
        ("sourceValue", "asv"),
        ("sourcePath", "asp"),
        ("target", "at"),
    )

    source = MessageField()
    as_ = source

    sourceValue = DoubleField(default_value=0.0)
    asv = sourceValue

    sourcePath = DataStringField()
    asp = sourcePath

    target = DataStringField()
    at = target


class AnimationAttrOperator(CompoundAttrOperator[AnimationPlugOperator]):
    __slots__ = ()

    source = MessageField()
    as_ = source

    sourceValue = DoubleField(default_value=0.0)
    asv = sourceValue

    sourcePath = DataStringField()
    asp = sourcePath

    target = DataStringField()
    at = target


class AnimationField(
    CompoundField[AnimationAttrOperator, AnimationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AnimationAttrOperator
    PLUG_CLS = AnimationPlugOperator
