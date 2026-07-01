# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.generic import GenericField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.unit_scalar.time import TimeField
from ..std.dt.string import DataStringField


class AttributePlugOperator(
    CompoundPlugOperator["AttributeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input", "ai"),
        ("value", "av"),
        ("start", "as"),
        ("switcher", "sw"),
        ("source", "src"),
    )

    input = GenericField()
    ai = input

    value = DoubleField()
    av = value

    start = TimeField()
    as_ = start

    switcher = BoolField()
    sw = switcher

    source = DataStringField()
    src = source


class AttributeAttrOperator(
    CompoundAttrOperator[AttributePlugOperator]
):
    __slots__ = ()

    input = GenericField()
    ai = input

    value = DoubleField()
    av = value

    start = TimeField()
    as_ = start

    switcher = BoolField()
    sw = switcher

    source = DataStringField()
    src = source


class AttributeField(
    CompoundField[AttributeAttrOperator, AttributePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttributeAttrOperator
    PLUG_CLS = AttributePlugOperator


class LayerAttributePlugOperator(
    CompoundPlugOperator["LayerAttributeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("layerAttributeIndex", "lai"),
        ("layerAttributeLayerId", "lid"),
        ("layerAttributeInput", "lin"),
        ("layerAttributeValue", "lv"),
    )

    layerAttributeIndex = LongField()
    lai = layerAttributeIndex

    layerAttributeLayerId = LongField()
    lid = layerAttributeLayerId

    layerAttributeInput = GenericField()
    lin = layerAttributeInput

    layerAttributeValue = DoubleField()
    lv = layerAttributeValue


class LayerAttributeAttrOperator(
    CompoundAttrOperator[LayerAttributePlugOperator]
):
    __slots__ = ()

    layerAttributeIndex = LongField()
    lai = layerAttributeIndex

    layerAttributeLayerId = LongField()
    lid = layerAttributeLayerId

    layerAttributeInput = GenericField()
    lin = layerAttributeInput

    layerAttributeValue = DoubleField()
    lv = layerAttributeValue


class LayerAttributeField(
    CompoundField[LayerAttributeAttrOperator, LayerAttributePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LayerAttributeAttrOperator
    PLUG_CLS = LayerAttributePlugOperator
