# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class OutSurfacePlugOperator(
    Float3CompoundBasePlugOperator["OutSurfaceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outSurfaceR", "osr"),
        ("outSurfaceG", "osg"),
        ("outSurfaceB", "osb"),
    )

    outSurfaceR = FloatField()
    osr = outSurfaceR

    outSurfaceG = FloatField()
    osg = outSurfaceG

    outSurfaceB = FloatField()
    osb = outSurfaceB


class OutSurfaceAttrOperator(
    Float3CompoundBaseAttrOperator[OutSurfacePlugOperator]
):
    __slots__ = ()

    outSurfaceR = FloatField()
    osr = outSurfaceR

    outSurfaceG = FloatField()
    osg = outSurfaceG

    outSurfaceB = FloatField()
    osb = outSurfaceB


class OutSurfaceField(
    Float3CompoundBaseField[OutSurfaceAttrOperator, OutSurfacePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutSurfaceAttrOperator
    PLUG_CLS = OutSurfacePlugOperator

    outSurfaceR = FloatField()
    osr = outSurfaceR

    outSurfaceG = FloatField()
    osg = outSurfaceG

    outSurfaceB = FloatField()
    osb = outSurfaceB


class OutVolumePlugOperator(
    Float3CompoundBasePlugOperator["OutVolumeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outVolumeR", "ovr"),
        ("outVolumeG", "ovg"),
        ("outVolumeB", "ovb"),
    )

    outVolumeR = FloatField()
    ovr = outVolumeR

    outVolumeG = FloatField()
    ovg = outVolumeG

    outVolumeB = FloatField()
    ovb = outVolumeB


class OutVolumeAttrOperator(
    Float3CompoundBaseAttrOperator[OutVolumePlugOperator]
):
    __slots__ = ()

    outVolumeR = FloatField()
    ovr = outVolumeR

    outVolumeG = FloatField()
    ovg = outVolumeG

    outVolumeB = FloatField()
    ovb = outVolumeB


class OutVolumeField(
    Float3CompoundBaseField[OutVolumeAttrOperator, OutVolumePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutVolumeAttrOperator
    PLUG_CLS = OutVolumePlugOperator

    outVolumeR = FloatField()
    ovr = outVolumeR

    outVolumeG = FloatField()
    ovg = outVolumeG

    outVolumeB = FloatField()
    ovb = outVolumeB
