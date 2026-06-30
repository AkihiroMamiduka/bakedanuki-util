# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class VectorDisplacementPlugOperator(
    Float3CompoundBasePlugOperator["VectorDisplacementAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vectorDisplacementX", "vdx"),
        ("vectorDisplacementY", "vdy"),
        ("vectorDisplacementZ", "vdz"),
    )

    vectorDisplacementX = FloatField()
    vdx = vectorDisplacementX

    vectorDisplacementY = FloatField()
    vdy = vectorDisplacementY

    vectorDisplacementZ = FloatField()
    vdz = vectorDisplacementZ


class VectorDisplacementAttrOperator(
    Float3CompoundBaseAttrOperator[VectorDisplacementPlugOperator]
):
    __slots__ = ()

    vectorDisplacementX = FloatField()
    vdx = vectorDisplacementX

    vectorDisplacementY = FloatField()
    vdy = vectorDisplacementY

    vectorDisplacementZ = FloatField()
    vdz = vectorDisplacementZ


class VectorDisplacementField(
    Float3CompoundBaseField[VectorDisplacementAttrOperator, VectorDisplacementPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VectorDisplacementAttrOperator
    PLUG_CLS = VectorDisplacementPlugOperator

    vectorDisplacementX = FloatField()
    vdx = vectorDisplacementX

    vectorDisplacementY = FloatField()
    vdy = vectorDisplacementY

    vectorDisplacementZ = FloatField()
    vdz = vectorDisplacementZ


class TangentPlugOperator(
    Float3CompoundBasePlugOperator["TangentAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tangentX", "tx"),
        ("tangentY", "ty"),
        ("tangentZ", "tz"),
    )

    tangentX = FloatField()
    tx = tangentX

    tangentY = FloatField()
    ty = tangentY

    tangentZ = FloatField()
    tz = tangentZ


class TangentAttrOperator(
    Float3CompoundBaseAttrOperator[TangentPlugOperator]
):
    __slots__ = ()

    tangentX = FloatField()
    tx = tangentX

    tangentY = FloatField()
    ty = tangentY

    tangentZ = FloatField()
    tz = tangentZ


class TangentField(
    Float3CompoundBaseField[TangentAttrOperator, TangentPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentAttrOperator
    PLUG_CLS = TangentPlugOperator

    tangentX = FloatField()
    tx = tangentX

    tangentY = FloatField()
    ty = tangentY

    tangentZ = FloatField()
    tz = tangentZ
