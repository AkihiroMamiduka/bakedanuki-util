# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.generic import GenericField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.long import LongField


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
