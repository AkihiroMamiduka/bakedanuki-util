# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
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

    valueX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    vx = valueX

    valueY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    vy = valueY

    valueZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    vz = valueZ


class ValueAttrOperator(
    Float3CompoundBaseAttrOperator[ValuePlugOperator]
):
    __slots__ = ()

    valueX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    vx = valueX

    valueY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    vy = valueY

    valueZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    vz = valueZ


class ValueField(
    Float3CompoundBaseField[ValueAttrOperator, ValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ValueAttrOperator
    PLUG_CLS = ValuePlugOperator

    valueX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    vx = valueX

    valueY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    vy = valueY

    valueZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
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

    minX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    nx = minX

    minY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ny = minY

    minZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    nz = minZ


class MinAttrOperator(
    Float3CompoundBaseAttrOperator[MinPlugOperator]
):
    __slots__ = ()

    minX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    nx = minX

    minY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ny = minY

    minZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    nz = minZ


class MinField(
    Float3CompoundBaseField[MinAttrOperator, MinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MinAttrOperator
    PLUG_CLS = MinPlugOperator

    minX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    nx = minX

    minY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ny = minY

    minZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
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

    maxX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mx = maxX

    maxY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    my = maxY

    maxZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mz = maxZ


class MaxAttrOperator(
    Float3CompoundBaseAttrOperator[MaxPlugOperator]
):
    __slots__ = ()

    maxX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mx = maxX

    maxY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    my = maxY

    maxZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mz = maxZ


class MaxField(
    Float3CompoundBaseField[MaxAttrOperator, MaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaxAttrOperator
    PLUG_CLS = MaxPlugOperator

    maxX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mx = maxX

    maxY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    my = maxY

    maxZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
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

    oldMinX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    onx = oldMinX

    oldMinY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ony = oldMinY

    oldMinZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    onz = oldMinZ


class OldMinAttrOperator(
    Float3CompoundBaseAttrOperator[OldMinPlugOperator]
):
    __slots__ = ()

    oldMinX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    onx = oldMinX

    oldMinY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ony = oldMinY

    oldMinZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    onz = oldMinZ


class OldMinField(
    Float3CompoundBaseField[OldMinAttrOperator, OldMinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OldMinAttrOperator
    PLUG_CLS = OldMinPlugOperator

    oldMinX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    onx = oldMinX

    oldMinY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ony = oldMinY

    oldMinZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
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

    oldMaxX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    omx = oldMaxX

    oldMaxY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    omy = oldMaxY

    oldMaxZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    omz = oldMaxZ


class OldMaxAttrOperator(
    Float3CompoundBaseAttrOperator[OldMaxPlugOperator]
):
    __slots__ = ()

    oldMaxX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    omx = oldMaxX

    oldMaxY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    omy = oldMaxY

    oldMaxZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    omz = oldMaxZ


class OldMaxField(
    Float3CompoundBaseField[OldMaxAttrOperator, OldMaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OldMaxAttrOperator
    PLUG_CLS = OldMaxPlugOperator

    oldMaxX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    omx = oldMaxX

    oldMaxY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    omy = oldMaxY

    oldMaxZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
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

    outValueX = FloatField(default_value=0.0, writable=False)
    ox = outValueX

    outValueY = FloatField(default_value=0.0, writable=False)
    oy = outValueY

    outValueZ = FloatField(default_value=0.0, writable=False)
    oz = outValueZ


class OutValueAttrOperator(
    Float3CompoundBaseAttrOperator[OutValuePlugOperator]
):
    __slots__ = ()

    outValueX = FloatField(default_value=0.0, writable=False)
    ox = outValueX

    outValueY = FloatField(default_value=0.0, writable=False)
    oy = outValueY

    outValueZ = FloatField(default_value=0.0, writable=False)
    oz = outValueZ


class OutValueField(
    Float3CompoundBaseField[OutValueAttrOperator, OutValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutValueAttrOperator
    PLUG_CLS = OutValuePlugOperator

    outValueX = FloatField(default_value=0.0, writable=False)
    ox = outValueX

    outValueY = FloatField(default_value=0.0, writable=False)
    oy = outValueY

    outValueZ = FloatField(default_value=0.0, writable=False)
    oz = outValueZ
