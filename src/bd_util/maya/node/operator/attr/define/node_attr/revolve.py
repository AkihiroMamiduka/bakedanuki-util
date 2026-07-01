# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class AxisPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["AxisAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("axisX", "axx"),
        ("axisY", "axy"),
        ("axisZ", "axz"),
    )

    axisX = DoubleLinearField()
    axx = axisX

    axisY = DoubleLinearField()
    axy = axisY

    axisZ = DoubleLinearField()
    axz = axisZ


class AxisAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[AxisPlugOperator]
):
    __slots__ = ()

    axisX = DoubleLinearField()
    axx = axisX

    axisY = DoubleLinearField()
    axy = axisY

    axisZ = DoubleLinearField()
    axz = axisZ


class AxisField(
    DoubleLinear3CompoundBaseField[AxisAttrOperator, AxisPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisAttrOperator
    PLUG_CLS = AxisPlugOperator

    axisX = DoubleLinearField()
    axx = axisX

    axisY = DoubleLinearField()
    axy = axisY

    axisZ = DoubleLinearField()
    axz = axisZ


class PivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["PivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pivotX", "px"),
        ("pivotY", "py"),
        ("pivotZ", "pz"),
    )

    pivotX = DoubleLinearField()
    px = pivotX

    pivotY = DoubleLinearField()
    py = pivotY

    pivotZ = DoubleLinearField()
    pz = pivotZ


class PivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[PivotPlugOperator]
):
    __slots__ = ()

    pivotX = DoubleLinearField()
    px = pivotX

    pivotY = DoubleLinearField()
    py = pivotY

    pivotZ = DoubleLinearField()
    pz = pivotZ


class PivotField(
    DoubleLinear3CompoundBaseField[PivotAttrOperator, PivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PivotAttrOperator
    PLUG_CLS = PivotPlugOperator

    pivotX = DoubleLinearField()
    px = pivotX

    pivotY = DoubleLinearField()
    py = pivotY

    pivotZ = DoubleLinearField()
    pz = pivotZ


class CompAxisPlugOperator(
    Double3CompoundBasePlugOperator["CompAxisAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("compAxisX", "cax"),
        ("compAxisY", "cay"),
        ("compAxisZ", "caz"),
    )

    compAxisX = DoubleField()
    cax = compAxisX

    compAxisY = DoubleField()
    cay = compAxisY

    compAxisZ = DoubleField()
    caz = compAxisZ


class CompAxisAttrOperator(
    Double3CompoundBaseAttrOperator[CompAxisPlugOperator]
):
    __slots__ = ()

    compAxisX = DoubleField()
    cax = compAxisX

    compAxisY = DoubleField()
    cay = compAxisY

    compAxisZ = DoubleField()
    caz = compAxisZ


class CompAxisField(
    Double3CompoundBaseField[CompAxisAttrOperator, CompAxisPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompAxisAttrOperator
    PLUG_CLS = CompAxisPlugOperator

    compAxisX = DoubleField()
    cax = compAxisX

    compAxisY = DoubleField()
    cay = compAxisY

    compAxisZ = DoubleField()
    caz = compAxisZ


class CompPivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["CompPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("compPivotX", "cpx"),
        ("compPivotY", "cpy"),
        ("compPivotZ", "cpz"),
    )

    compPivotX = DoubleLinearField()
    cpx = compPivotX

    compPivotY = DoubleLinearField()
    cpy = compPivotY

    compPivotZ = DoubleLinearField()
    cpz = compPivotZ


class CompPivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CompPivotPlugOperator]
):
    __slots__ = ()

    compPivotX = DoubleLinearField()
    cpx = compPivotX

    compPivotY = DoubleLinearField()
    cpy = compPivotY

    compPivotZ = DoubleLinearField()
    cpz = compPivotZ


class CompPivotField(
    DoubleLinear3CompoundBaseField[CompPivotAttrOperator, CompPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompPivotAttrOperator
    PLUG_CLS = CompPivotPlugOperator

    compPivotX = DoubleLinearField()
    cpx = compPivotX

    compPivotY = DoubleLinearField()
    cpy = compPivotY

    compPivotZ = DoubleLinearField()
    cpz = compPivotZ


class CompAnchorPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["CompAnchorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("compAnchorX", "cnx"),
        ("compAnchorY", "cny"),
        ("compAnchorZ", "cnz"),
    )

    compAnchorX = DoubleLinearField()
    cnx = compAnchorX

    compAnchorY = DoubleLinearField()
    cny = compAnchorY

    compAnchorZ = DoubleLinearField()
    cnz = compAnchorZ


class CompAnchorAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CompAnchorPlugOperator]
):
    __slots__ = ()

    compAnchorX = DoubleLinearField()
    cnx = compAnchorX

    compAnchorY = DoubleLinearField()
    cny = compAnchorY

    compAnchorZ = DoubleLinearField()
    cnz = compAnchorZ


class CompAnchorField(
    DoubleLinear3CompoundBaseField[CompAnchorAttrOperator, CompAnchorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompAnchorAttrOperator
    PLUG_CLS = CompAnchorPlugOperator

    compAnchorX = DoubleLinearField()
    cnx = compAnchorX

    compAnchorY = DoubleLinearField()
    cny = compAnchorY

    compAnchorZ = DoubleLinearField()
    cnz = compAnchorZ
