# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ParticleIncandescencePlugOperator(
    Float3CompoundBasePlugOperator["ParticleIncandescenceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("particleIncandescenceR", "pir"),
        ("particleIncandescenceG", "pig"),
        ("particleIncandescenceB", "pib"),
    )

    particleIncandescenceR = FloatField(default_value=0.0)
    pir = particleIncandescenceR

    particleIncandescenceG = FloatField(default_value=0.0)
    pig = particleIncandescenceG

    particleIncandescenceB = FloatField(default_value=0.0)
    pib = particleIncandescenceB


class ParticleIncandescenceAttrOperator(
    Float3CompoundBaseAttrOperator[ParticleIncandescencePlugOperator]
):
    __slots__ = ()

    particleIncandescenceR = FloatField(default_value=0.0)
    pir = particleIncandescenceR

    particleIncandescenceG = FloatField(default_value=0.0)
    pig = particleIncandescenceG

    particleIncandescenceB = FloatField(default_value=0.0)
    pib = particleIncandescenceB


class ParticleIncandescenceField(
    Float3CompoundBaseField[ParticleIncandescenceAttrOperator, ParticleIncandescencePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParticleIncandescenceAttrOperator
    PLUG_CLS = ParticleIncandescencePlugOperator

    particleIncandescenceR = FloatField(default_value=0.0)
    pir = particleIncandescenceR

    particleIncandescenceG = FloatField(default_value=0.0)
    pig = particleIncandescenceG

    particleIncandescenceB = FloatField(default_value=0.0)
    pib = particleIncandescenceB
