# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
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

    particleIncandescenceR = FloatField()
    pir = particleIncandescenceR

    particleIncandescenceG = FloatField()
    pig = particleIncandescenceG

    particleIncandescenceB = FloatField()
    pib = particleIncandescenceB


class ParticleIncandescenceAttrOperator(
    Float3CompoundBaseAttrOperator[ParticleIncandescencePlugOperator]
):
    __slots__ = ()

    particleIncandescenceR = FloatField()
    pir = particleIncandescenceR

    particleIncandescenceG = FloatField()
    pig = particleIncandescenceG

    particleIncandescenceB = FloatField()
    pib = particleIncandescenceB


class ParticleIncandescenceField(
    Float3CompoundBaseField[ParticleIncandescenceAttrOperator, ParticleIncandescencePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParticleIncandescenceAttrOperator
    PLUG_CLS = ParticleIncandescencePlugOperator

    particleIncandescenceR = FloatField()
    pir = particleIncandescenceR

    particleIncandescenceG = FloatField()
    pig = particleIncandescenceG

    particleIncandescenceB = FloatField()
    pib = particleIncandescenceB
