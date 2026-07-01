# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ParticleTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["ParticleTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("particleTransparencyR", "ptr"),
        ("particleTransparencyG", "ptg"),
        ("particleTransparencyB", "ptb"),
    )

    particleTransparencyR = FloatField()
    ptr = particleTransparencyR

    particleTransparencyG = FloatField()
    ptg = particleTransparencyG

    particleTransparencyB = FloatField()
    ptb = particleTransparencyB


class ParticleTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[ParticleTransparencyPlugOperator]
):
    __slots__ = ()

    particleTransparencyR = FloatField()
    ptr = particleTransparencyR

    particleTransparencyG = FloatField()
    ptg = particleTransparencyG

    particleTransparencyB = FloatField()
    ptb = particleTransparencyB


class ParticleTransparencyField(
    Float3CompoundBaseField[ParticleTransparencyAttrOperator, ParticleTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParticleTransparencyAttrOperator
    PLUG_CLS = ParticleTransparencyPlugOperator

    particleTransparencyR = FloatField()
    ptr = particleTransparencyR

    particleTransparencyG = FloatField()
    ptg = particleTransparencyG

    particleTransparencyB = FloatField()
    ptb = particleTransparencyB
