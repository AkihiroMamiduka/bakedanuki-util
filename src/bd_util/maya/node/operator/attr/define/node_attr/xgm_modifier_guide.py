# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class MagnitudeScalePlugOperator(
    CompoundPlugOperator["MagnitudeScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("magnitudeScale_Position", "msp"),
        ("magnitudeScale_FloatValue", "msfv"),
        ("magnitudeScale_Interp", "msi"),
    )

    magnitudeScale_Position = FloatField()
    msp = magnitudeScale_Position

    magnitudeScale_FloatValue = FloatField()
    msfv = magnitudeScale_FloatValue

    magnitudeScale_Interp = EnumField()
    msi = magnitudeScale_Interp


class MagnitudeScaleAttrOperator(
    CompoundAttrOperator[MagnitudeScalePlugOperator]
):
    __slots__ = ()

    magnitudeScale_Position = FloatField()
    msp = magnitudeScale_Position

    magnitudeScale_FloatValue = FloatField()
    msfv = magnitudeScale_FloatValue

    magnitudeScale_Interp = EnumField()
    msi = magnitudeScale_Interp


class MagnitudeScaleField(
    CompoundField[MagnitudeScaleAttrOperator, MagnitudeScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MagnitudeScaleAttrOperator
    PLUG_CLS = MagnitudeScalePlugOperator


class RegionMapPlugOperator(
    Float3CompoundBasePlugOperator["RegionMapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("regionMapR", "rmpr"),
        ("regionMapG", "rmpg"),
        ("regionMapB", "rmpb"),
    )

    regionMapR = FloatField()
    rmpr = regionMapR

    regionMapG = FloatField()
    rmpg = regionMapG

    regionMapB = FloatField()
    rmpb = regionMapB


class RegionMapAttrOperator(
    Float3CompoundBaseAttrOperator[RegionMapPlugOperator]
):
    __slots__ = ()

    regionMapR = FloatField()
    rmpr = regionMapR

    regionMapG = FloatField()
    rmpg = regionMapG

    regionMapB = FloatField()
    rmpb = regionMapB


class RegionMapField(
    Float3CompoundBaseField[RegionMapAttrOperator, RegionMapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RegionMapAttrOperator
    PLUG_CLS = RegionMapPlugOperator

    regionMapR = FloatField()
    rmpr = regionMapR

    regionMapG = FloatField()
    rmpg = regionMapG

    regionMapB = FloatField()
    rmpb = regionMapB
