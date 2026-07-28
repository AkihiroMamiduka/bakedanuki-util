# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class BloomTintPlugOperator(
    Float3CompoundBasePlugOperator["BloomTintAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("bloomTintR", "bloom_tintr"),
        ("bloomTintG", "bloom_tintg"),
        ("bloomTintB", "bloom_tintb"),
    )

    bloomTintR = FloatField(default_value=1.0)
    bloom_tintr = bloomTintR

    bloomTintG = FloatField(default_value=1.0)
    bloom_tintg = bloomTintG

    bloomTintB = FloatField(default_value=1.0)
    bloom_tintb = bloomTintB


class BloomTintAttrOperator(
    Float3CompoundBaseAttrOperator[BloomTintPlugOperator]
):
    __slots__ = ()

    bloomTintR = FloatField(default_value=1.0)
    bloom_tintr = bloomTintR

    bloomTintG = FloatField(default_value=1.0)
    bloom_tintg = bloomTintG

    bloomTintB = FloatField(default_value=1.0)
    bloom_tintb = bloomTintB


class BloomTintField(
    Float3CompoundBaseField[BloomTintAttrOperator, BloomTintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BloomTintAttrOperator
    PLUG_CLS = BloomTintPlugOperator

    bloomTintR = FloatField(default_value=1.0)
    bloom_tintr = bloomTintR

    bloomTintG = FloatField(default_value=1.0)
    bloom_tintg = bloomTintG

    bloomTintB = FloatField(default_value=1.0)
    bloom_tintb = bloomTintB
