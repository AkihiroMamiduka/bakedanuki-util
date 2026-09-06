# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.dt.string import DataStringField


class OutputAttributesPlugOperator(
    CompoundPlugOperator["OutputAttributesAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputName", "oname"),
        ("outputValues", "oval"),
    )

    outputName = DataStringField(writable=False)
    oname = outputName

    outputValues = DoubleField(multi=True, default_value=0.0, writable=False)
    oval = outputValues


class OutputAttributesAttrOperator(
    CompoundAttrOperator[OutputAttributesPlugOperator]
):
    __slots__ = ()

    outputName = DataStringField(writable=False)
    oname = outputName

    outputValues = DoubleField(multi=True, default_value=0.0, writable=False)
    oval = outputValues


class OutputAttributesField(
    CompoundField[OutputAttributesAttrOperator, OutputAttributesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttributesAttrOperator
    PLUG_CLS = OutputAttributesPlugOperator
