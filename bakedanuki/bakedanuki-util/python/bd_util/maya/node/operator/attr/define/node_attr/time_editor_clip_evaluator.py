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

    input = GenericField(readable=False)
    ai = input

    value = DoubleField(default_value=0.0)
    av = value

    start = TimeField(default_value=0.0)
    as_ = start

    switcher = BoolField(default_value=False)
    sw = switcher

    source = DataStringField()
    src = source


class AttributeAttrOperator(
    CompoundAttrOperator[AttributePlugOperator]
):
    __slots__ = ()

    input = GenericField(readable=False)
    ai = input

    value = DoubleField(default_value=0.0)
    av = value

    start = TimeField(default_value=0.0)
    as_ = start

    switcher = BoolField(default_value=False)
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

    layerAttributeIndex = LongField(default_value=-1, min_value=0)
    lai = layerAttributeIndex

    layerAttributeLayerId = LongField(default_value=-1)
    lid = layerAttributeLayerId

    layerAttributeInput = GenericField()
    lin = layerAttributeInput

    layerAttributeValue = DoubleField(default_value=0.0)
    lv = layerAttributeValue


class LayerAttributeAttrOperator(
    CompoundAttrOperator[LayerAttributePlugOperator]
):
    __slots__ = ()

    layerAttributeIndex = LongField(default_value=-1, min_value=0)
    lai = layerAttributeIndex

    layerAttributeLayerId = LongField(default_value=-1)
    lid = layerAttributeLayerId

    layerAttributeInput = GenericField()
    lin = layerAttributeInput

    layerAttributeValue = DoubleField(default_value=0.0)
    lv = layerAttributeValue


class LayerAttributeField(
    CompoundField[LayerAttributeAttrOperator, LayerAttributePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LayerAttributeAttrOperator
    PLUG_CLS = LayerAttributePlugOperator
