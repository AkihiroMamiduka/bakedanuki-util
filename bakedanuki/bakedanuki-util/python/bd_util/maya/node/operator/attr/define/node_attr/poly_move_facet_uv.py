# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double2_compound._base import (
    Double2CompoundBaseAttrOperator,
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseField,
)


class TranslatePlugOperator(
    Double2CompoundBasePlugOperator["TranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("translateU", "tu"),
        ("translateV", "tv"),
    )

    translateU = DoubleField(default_value=0.0)
    tu = translateU

    translateV = DoubleField(default_value=0.0)
    tv = translateV


class TranslateAttrOperator(
    Double2CompoundBaseAttrOperator[TranslatePlugOperator]
):
    __slots__ = ()

    translateU = DoubleField(default_value=0.0)
    tu = translateU

    translateV = DoubleField(default_value=0.0)
    tv = translateV


class TranslateField(
    Double2CompoundBaseField[TranslateAttrOperator, TranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateAttrOperator
    PLUG_CLS = TranslatePlugOperator

    translateU = DoubleField(default_value=0.0)
    tu = translateU

    translateV = DoubleField(default_value=0.0)
    tv = translateV


class PivotPlugOperator(
    Double2CompoundBasePlugOperator["PivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pivotU", "pvu"),
        ("pivotV", "pvv"),
    )

    pivotU = DoubleField(default_value=0.5)
    pvu = pivotU

    pivotV = DoubleField(default_value=0.5)
    pvv = pivotV


class PivotAttrOperator(
    Double2CompoundBaseAttrOperator[PivotPlugOperator]
):
    __slots__ = ()

    pivotU = DoubleField(default_value=0.5)
    pvu = pivotU

    pivotV = DoubleField(default_value=0.5)
    pvv = pivotV


class PivotField(
    Double2CompoundBaseField[PivotAttrOperator, PivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PivotAttrOperator
    PLUG_CLS = PivotPlugOperator

    pivotU = DoubleField(default_value=0.5)
    pvu = pivotU

    pivotV = DoubleField(default_value=0.5)
    pvv = pivotV


class ScalePlugOperator(
    Double2CompoundBasePlugOperator["ScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleU", "su"),
        ("scaleV", "sv"),
    )

    scaleU = DoubleField(default_value=1.0)
    su = scaleU

    scaleV = DoubleField(default_value=1.0)
    sv = scaleV


class ScaleAttrOperator(
    Double2CompoundBaseAttrOperator[ScalePlugOperator]
):
    __slots__ = ()

    scaleU = DoubleField(default_value=1.0)
    su = scaleU

    scaleV = DoubleField(default_value=1.0)
    sv = scaleV


class ScaleField(
    Double2CompoundBaseField[ScaleAttrOperator, ScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAttrOperator
    PLUG_CLS = ScalePlugOperator

    scaleU = DoubleField(default_value=1.0)
    su = scaleU

    scaleV = DoubleField(default_value=1.0)
    sv = scaleV


class AxisLenPlugOperator(
    Double2CompoundBasePlugOperator["AxisLenAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("axisLenX", "lx"),
        ("axisLenY", "ly"),
    )

    axisLenX = DoubleField(default_value=1.0)
    lx = axisLenX

    axisLenY = DoubleField(default_value=1.0)
    ly = axisLenY


class AxisLenAttrOperator(
    Double2CompoundBaseAttrOperator[AxisLenPlugOperator]
):
    __slots__ = ()

    axisLenX = DoubleField(default_value=1.0)
    lx = axisLenX

    axisLenY = DoubleField(default_value=1.0)
    ly = axisLenY


class AxisLenField(
    Double2CompoundBaseField[AxisLenAttrOperator, AxisLenPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisLenAttrOperator
    PLUG_CLS = AxisLenPlugOperator

    axisLenX = DoubleField(default_value=1.0)
    lx = axisLenX

    axisLenY = DoubleField(default_value=1.0)
    ly = axisLenY
