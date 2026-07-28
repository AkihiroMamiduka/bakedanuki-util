# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
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

    particleTransparencyR = FloatField(default_value=0.0)
    ptr = particleTransparencyR

    particleTransparencyG = FloatField(default_value=0.0)
    ptg = particleTransparencyG

    particleTransparencyB = FloatField(default_value=0.0)
    ptb = particleTransparencyB


class ParticleTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[ParticleTransparencyPlugOperator]
):
    __slots__ = ()

    particleTransparencyR = FloatField(default_value=0.0)
    ptr = particleTransparencyR

    particleTransparencyG = FloatField(default_value=0.0)
    ptg = particleTransparencyG

    particleTransparencyB = FloatField(default_value=0.0)
    ptb = particleTransparencyB


class ParticleTransparencyField(
    Float3CompoundBaseField[
        ParticleTransparencyAttrOperator, ParticleTransparencyPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ParticleTransparencyAttrOperator
    PLUG_CLS = ParticleTransparencyPlugOperator

    particleTransparencyR = FloatField(default_value=0.0)
    ptr = particleTransparencyR

    particleTransparencyG = FloatField(default_value=0.0)
    ptg = particleTransparencyG

    particleTransparencyB = FloatField(default_value=0.0)
    ptb = particleTransparencyB
