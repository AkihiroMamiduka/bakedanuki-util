# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
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

    layerTintR = FloatField(default_value=2.246063752498668e+26)
    layer_tintr = layerTintR

    layerTintG = FloatField(default_value=6.305843089461677e-43)
    layer_tintg = layerTintG

    layerTintB = FloatField(default_value=1.0)
    layer_tintb = layerTintB


class LayerTintAttrOperator(
    Float3CompoundBaseAttrOperator[LayerTintPlugOperator]
):
    __slots__ = ()

    layerTintR = FloatField(default_value=2.246063752498668e+26)
    layer_tintr = layerTintR

    layerTintG = FloatField(default_value=6.305843089461677e-43)
    layer_tintg = layerTintG

    layerTintB = FloatField(default_value=1.0)
    layer_tintb = layerTintB


class LayerTintField(
    Float3CompoundBaseField[LayerTintAttrOperator, LayerTintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LayerTintAttrOperator
    PLUG_CLS = LayerTintPlugOperator
