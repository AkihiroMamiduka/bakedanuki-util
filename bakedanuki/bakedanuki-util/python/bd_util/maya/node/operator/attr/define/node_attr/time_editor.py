# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.scalar.numeric.range.double import DoubleField


class AttributesPlugOperator(
    CompoundPlugOperator["AttributesAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("attribute", "a"),
        ("animationSource", "as"),
        ("value", "v"),
    )

    attribute = MessageField()
    a = attribute

    animationSource = MessageField()
    as_ = animationSource

    value = DoubleField(default_value=0.0)
    v = value


class AttributesAttrOperator(
    CompoundAttrOperator[AttributesPlugOperator]
):
    __slots__ = ()

    attribute = MessageField()
    a = attribute

    animationSource = MessageField()
    as_ = animationSource

    value = DoubleField(default_value=0.0)
    v = value


class AttributesField(
    CompoundField[AttributesAttrOperator, AttributesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttributesAttrOperator
    PLUG_CLS = AttributesPlugOperator
