# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.generic import GenericField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.long import LongField


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
