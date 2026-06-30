# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.dt.string import DataStringField


class LooksPlugOperator(
    CompoundPlugOperator["LooksAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("variantName", "name"),
        ("inputs", "ipts"),
    )

    variantName = DataStringField()
    name = variantName

    inputs = MessageField()
    ipts = inputs


class LooksAttrOperator(
    CompoundAttrOperator[LooksPlugOperator]
):
    __slots__ = ()

    variantName = DataStringField()
    name = variantName

    inputs = MessageField()
    ipts = inputs


class LooksField(
    CompoundField[LooksAttrOperator, LooksPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LooksAttrOperator
    PLUG_CLS = LooksPlugOperator
