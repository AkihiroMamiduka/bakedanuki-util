# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class BendVectorPlugOperator(
    Float3CompoundBasePlugOperator["BendVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("bendVectorX", "bx"),
        ("bendVectorY", "by"),
        ("bendVectorZ", "bz"),
    )

    bendVectorX = FloatField()
    bx = bendVectorX

    bendVectorY = FloatField()
    by = bendVectorY

    bendVectorZ = FloatField()
    bz = bendVectorZ


class BendVectorAttrOperator(
    Float3CompoundBaseAttrOperator[BendVectorPlugOperator]
):
    __slots__ = ()

    bendVectorX = FloatField()
    bx = bendVectorX

    bendVectorY = FloatField()
    by = bendVectorY

    bendVectorZ = FloatField()
    bz = bendVectorZ


class BendVectorField(
    Float3CompoundBaseField[BendVectorAttrOperator, BendVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BendVectorAttrOperator
    PLUG_CLS = BendVectorPlugOperator

    bendVectorX = FloatField()
    bx = bendVectorX

    bendVectorY = FloatField()
    by = bendVectorY

    bendVectorZ = FloatField()
    bz = bendVectorZ
