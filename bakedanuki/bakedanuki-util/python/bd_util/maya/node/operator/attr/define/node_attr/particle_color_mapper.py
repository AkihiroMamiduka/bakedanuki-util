# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ParticleColorPlugOperator(
    Float3CompoundBasePlugOperator["ParticleColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("particleColorR", "pcr"),
        ("particleColorG", "pcg"),
        ("particleColorB", "pcb"),
    )

    particleColorR = FloatField(default_value=0.0)
    pcr = particleColorR

    particleColorG = FloatField(default_value=0.0)
    pcg = particleColorG

    particleColorB = FloatField(default_value=0.0)
    pcb = particleColorB


class ParticleColorAttrOperator(
    Float3CompoundBaseAttrOperator[ParticleColorPlugOperator]
):
    __slots__ = ()

    particleColorR = FloatField(default_value=0.0)
    pcr = particleColorR

    particleColorG = FloatField(default_value=0.0)
    pcg = particleColorG

    particleColorB = FloatField(default_value=0.0)
    pcb = particleColorB


class ParticleColorField(
    Float3CompoundBaseField[
        ParticleColorAttrOperator, ParticleColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ParticleColorAttrOperator
    PLUG_CLS = ParticleColorPlugOperator

    particleColorR = FloatField(default_value=0.0)
    pcr = particleColorR

    particleColorG = FloatField(default_value=0.0)
    pcg = particleColorG

    particleColorB = FloatField(default_value=0.0)
    pcb = particleColorB
