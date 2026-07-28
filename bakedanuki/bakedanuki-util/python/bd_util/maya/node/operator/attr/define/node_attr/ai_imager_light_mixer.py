# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class LayerTintPlugOperator(
    Float3CompoundBasePlugOperator["LayerTintAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("layerTintR", "layer_tintr"),
        ("layerTintG", "layer_tintg"),
        ("layerTintB", "layer_tintb"),
    )

    layerTintR = FloatField()
    layer_tintr = layerTintR

    layerTintG = FloatField()
    layer_tintg = layerTintG

    layerTintB = FloatField(default_value=1.0)
    layer_tintb = layerTintB


class LayerTintAttrOperator(
    Float3CompoundBaseAttrOperator[LayerTintPlugOperator]
):
    __slots__ = ()

    layerTintR = FloatField()
    layer_tintr = layerTintR

    layerTintG = FloatField()
    layer_tintg = layerTintG

    layerTintB = FloatField(default_value=1.0)
    layer_tintb = layerTintB


class LayerTintField(
    Float3CompoundBaseField[LayerTintAttrOperator, LayerTintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LayerTintAttrOperator
    PLUG_CLS = LayerTintPlugOperator
