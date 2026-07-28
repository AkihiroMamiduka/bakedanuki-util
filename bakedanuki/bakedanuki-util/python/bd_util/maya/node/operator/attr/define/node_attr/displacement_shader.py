# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
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

    vectorDisplacementX = FloatField(default_value=0.0)
    vdx = vectorDisplacementX

    vectorDisplacementY = FloatField(default_value=0.0)
    vdy = vectorDisplacementY

    vectorDisplacementZ = FloatField(default_value=0.0)
    vdz = vectorDisplacementZ


class VectorDisplacementAttrOperator(
    Float3CompoundBaseAttrOperator[VectorDisplacementPlugOperator]
):
    __slots__ = ()

    vectorDisplacementX = FloatField(default_value=0.0)
    vdx = vectorDisplacementX

    vectorDisplacementY = FloatField(default_value=0.0)
    vdy = vectorDisplacementY

    vectorDisplacementZ = FloatField(default_value=0.0)
    vdz = vectorDisplacementZ


class VectorDisplacementField(
    Float3CompoundBaseField[
        VectorDisplacementAttrOperator, VectorDisplacementPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = VectorDisplacementAttrOperator
    PLUG_CLS = VectorDisplacementPlugOperator

    vectorDisplacementX = FloatField(default_value=0.0)
    vdx = vectorDisplacementX

    vectorDisplacementY = FloatField(default_value=0.0)
    vdy = vectorDisplacementY

    vectorDisplacementZ = FloatField(default_value=0.0)
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

    tangentX = FloatField(default_value=0.0)
    tx = tangentX

    tangentY = FloatField(default_value=0.0)
    ty = tangentY

    tangentZ = FloatField(default_value=0.0)
    tz = tangentZ


class TangentAttrOperator(Float3CompoundBaseAttrOperator[TangentPlugOperator]):
    __slots__ = ()

    tangentX = FloatField(default_value=0.0)
    tx = tangentX

    tangentY = FloatField(default_value=0.0)
    ty = tangentY

    tangentZ = FloatField(default_value=0.0)
    tz = tangentZ


class TangentField(
    Float3CompoundBaseField[TangentAttrOperator, TangentPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentAttrOperator
    PLUG_CLS = TangentPlugOperator

    tangentX = FloatField(default_value=0.0)
    tx = tangentX

    tangentY = FloatField(default_value=0.0)
    ty = tangentY

    tangentZ = FloatField(default_value=0.0)
    tz = tangentZ
