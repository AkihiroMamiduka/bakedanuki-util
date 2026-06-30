# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ValuePlugOperator(
    Float3CompoundBasePlugOperator["ValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("valueX", "vx"),
        ("valueY", "vy"),
        ("valueZ", "vz"),
    )

    valueX = FloatField()
    vx = valueX

    valueY = FloatField()
    vy = valueY

    valueZ = FloatField()
    vz = valueZ


class ValueAttrOperator(
    Float3CompoundBaseAttrOperator[ValuePlugOperator]
):
    __slots__ = ()

    valueX = FloatField()
    vx = valueX

    valueY = FloatField()
    vy = valueY

    valueZ = FloatField()
    vz = valueZ


class ValueField(
    Float3CompoundBaseField[ValueAttrOperator, ValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ValueAttrOperator
    PLUG_CLS = ValuePlugOperator

    valueX = FloatField()
    vx = valueX

    valueY = FloatField()
    vy = valueY

    valueZ = FloatField()
    vz = valueZ


class MinPlugOperator(
    Float3CompoundBasePlugOperator["MinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minX", "nx"),
        ("minY", "ny"),
        ("minZ", "nz"),
    )

    minX = FloatField()
    nx = minX

    minY = FloatField()
    ny = minY

    minZ = FloatField()
    nz = minZ


class MinAttrOperator(
    Float3CompoundBaseAttrOperator[MinPlugOperator]
):
    __slots__ = ()

    minX = FloatField()
    nx = minX

    minY = FloatField()
    ny = minY

    minZ = FloatField()
    nz = minZ


class MinField(
    Float3CompoundBaseField[MinAttrOperator, MinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MinAttrOperator
    PLUG_CLS = MinPlugOperator

    minX = FloatField()
    nx = minX

    minY = FloatField()
    ny = minY

    minZ = FloatField()
    nz = minZ


class MaxPlugOperator(
    Float3CompoundBasePlugOperator["MaxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maxX", "mx"),
        ("maxY", "my"),
        ("maxZ", "mz"),
    )

    maxX = FloatField()
    mx = maxX

    maxY = FloatField()
    my = maxY

    maxZ = FloatField()
    mz = maxZ


class MaxAttrOperator(
    Float3CompoundBaseAttrOperator[MaxPlugOperator]
):
    __slots__ = ()

    maxX = FloatField()
    mx = maxX

    maxY = FloatField()
    my = maxY

    maxZ = FloatField()
    mz = maxZ


class MaxField(
    Float3CompoundBaseField[MaxAttrOperator, MaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaxAttrOperator
    PLUG_CLS = MaxPlugOperator

    maxX = FloatField()
    mx = maxX

    maxY = FloatField()
    my = maxY

    maxZ = FloatField()
    mz = maxZ


class OldMinPlugOperator(
    Float3CompoundBasePlugOperator["OldMinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("oldMinX", "onx"),
        ("oldMinY", "ony"),
        ("oldMinZ", "onz"),
    )

    oldMinX = FloatField()
    onx = oldMinX

    oldMinY = FloatField()
    ony = oldMinY

    oldMinZ = FloatField()
    onz = oldMinZ


class OldMinAttrOperator(
    Float3CompoundBaseAttrOperator[OldMinPlugOperator]
):
    __slots__ = ()

    oldMinX = FloatField()
    onx = oldMinX

    oldMinY = FloatField()
    ony = oldMinY

    oldMinZ = FloatField()
    onz = oldMinZ


class OldMinField(
    Float3CompoundBaseField[OldMinAttrOperator, OldMinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OldMinAttrOperator
    PLUG_CLS = OldMinPlugOperator

    oldMinX = FloatField()
    onx = oldMinX

    oldMinY = FloatField()
    ony = oldMinY

    oldMinZ = FloatField()
    onz = oldMinZ


class OldMaxPlugOperator(
    Float3CompoundBasePlugOperator["OldMaxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("oldMaxX", "omx"),
        ("oldMaxY", "omy"),
        ("oldMaxZ", "omz"),
    )

    oldMaxX = FloatField()
    omx = oldMaxX

    oldMaxY = FloatField()
    omy = oldMaxY

    oldMaxZ = FloatField()
    omz = oldMaxZ


class OldMaxAttrOperator(
    Float3CompoundBaseAttrOperator[OldMaxPlugOperator]
):
    __slots__ = ()

    oldMaxX = FloatField()
    omx = oldMaxX

    oldMaxY = FloatField()
    omy = oldMaxY

    oldMaxZ = FloatField()
    omz = oldMaxZ


class OldMaxField(
    Float3CompoundBaseField[OldMaxAttrOperator, OldMaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OldMaxAttrOperator
    PLUG_CLS = OldMaxPlugOperator

    oldMaxX = FloatField()
    omx = oldMaxX

    oldMaxY = FloatField()
    omy = oldMaxY

    oldMaxZ = FloatField()
    omz = oldMaxZ


class OutValuePlugOperator(
    Float3CompoundBasePlugOperator["OutValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outValueX", "ox"),
        ("outValueY", "oy"),
        ("outValueZ", "oz"),
    )

    outValueX = FloatField()
    ox = outValueX

    outValueY = FloatField()
    oy = outValueY

    outValueZ = FloatField()
    oz = outValueZ


class OutValueAttrOperator(
    Float3CompoundBaseAttrOperator[OutValuePlugOperator]
):
    __slots__ = ()

    outValueX = FloatField()
    ox = outValueX

    outValueY = FloatField()
    oy = outValueY

    outValueZ = FloatField()
    oz = outValueZ


class OutValueField(
    Float3CompoundBaseField[OutValueAttrOperator, OutValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutValueAttrOperator
    PLUG_CLS = OutValuePlugOperator

    outValueX = FloatField()
    ox = outValueX

    outValueY = FloatField()
    oy = outValueY

    outValueZ = FloatField()
    oz = outValueZ
