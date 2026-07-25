# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.scalar.numeric.range.float import FloatField


class InputPlugOperator(
    CompoundPlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inSingle", "it"),
        ("inShape", "is"),
    )

    inSingle = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    it = inSingle

    inShape = MessageField()
    is_ = inShape


class InputAttrOperator(
    CompoundAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inSingle = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    it = inSingle

    inShape = MessageField()
    is_ = inShape


class InputField(
    CompoundField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator
