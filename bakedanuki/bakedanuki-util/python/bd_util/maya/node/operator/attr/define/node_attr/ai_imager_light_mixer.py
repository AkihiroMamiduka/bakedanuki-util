# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
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

    layerTintR = FloatField(default_value=-2.2096994373166368e-13)
    layer_tintr = layerTintR

    layerTintG = FloatField(default_value=9.332647772403282e-43)
    layer_tintg = layerTintG

    layerTintB = FloatField(default_value=1.0)
    layer_tintb = layerTintB


class LayerTintAttrOperator(
    Float3CompoundBaseAttrOperator[LayerTintPlugOperator]
):
    __slots__ = ()

    layerTintR = FloatField(default_value=-2.2096994373166368e-13)
    layer_tintr = layerTintR

    layerTintG = FloatField(default_value=9.332647772403282e-43)
    layer_tintg = layerTintG

    layerTintB = FloatField(default_value=1.0)
    layer_tintb = layerTintB


class LayerTintField(
    Float3CompoundBaseField[LayerTintAttrOperator, LayerTintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LayerTintAttrOperator
    PLUG_CLS = LayerTintPlugOperator
