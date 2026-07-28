# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
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

    axisX = DoubleLinearField(default_value=1.0)
    axx = axisX

    axisY = DoubleLinearField(default_value=0.0)
    axy = axisY

    axisZ = DoubleLinearField(default_value=0.0)
    axz = axisZ


class AxisAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[AxisPlugOperator]
):
    __slots__ = ()

    axisX = DoubleLinearField(default_value=1.0)
    axx = axisX

    axisY = DoubleLinearField(default_value=0.0)
    axy = axisY

    axisZ = DoubleLinearField(default_value=0.0)
    axz = axisZ


class AxisField(
    DoubleLinear3CompoundBaseField[AxisAttrOperator, AxisPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisAttrOperator
    PLUG_CLS = AxisPlugOperator

    axisX = DoubleLinearField(default_value=1.0)
    axx = axisX

    axisY = DoubleLinearField(default_value=0.0)
    axy = axisY

    axisZ = DoubleLinearField(default_value=0.0)
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

    pivotX = DoubleLinearField(default_value=0.0)
    px = pivotX

    pivotY = DoubleLinearField(default_value=0.0)
    py = pivotY

    pivotZ = DoubleLinearField(default_value=0.0)
    pz = pivotZ


class PivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[PivotPlugOperator]
):
    __slots__ = ()

    pivotX = DoubleLinearField(default_value=0.0)
    px = pivotX

    pivotY = DoubleLinearField(default_value=0.0)
    py = pivotY

    pivotZ = DoubleLinearField(default_value=0.0)
    pz = pivotZ


class PivotField(
    DoubleLinear3CompoundBaseField[PivotAttrOperator, PivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PivotAttrOperator
    PLUG_CLS = PivotPlugOperator

    pivotX = DoubleLinearField(default_value=0.0)
    px = pivotX

    pivotY = DoubleLinearField(default_value=0.0)
    py = pivotY

    pivotZ = DoubleLinearField(default_value=0.0)
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

    compAxisX = DoubleField(default_value=0.0, writable=False)
    cax = compAxisX

    compAxisY = DoubleField(default_value=0.0, writable=False)
    cay = compAxisY

    compAxisZ = DoubleField(default_value=0.0, writable=False)
    caz = compAxisZ


class CompAxisAttrOperator(
    Double3CompoundBaseAttrOperator[CompAxisPlugOperator]
):
    __slots__ = ()

    compAxisX = DoubleField(default_value=0.0, writable=False)
    cax = compAxisX

    compAxisY = DoubleField(default_value=0.0, writable=False)
    cay = compAxisY

    compAxisZ = DoubleField(default_value=0.0, writable=False)
    caz = compAxisZ


class CompAxisField(
    Double3CompoundBaseField[CompAxisAttrOperator, CompAxisPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompAxisAttrOperator
    PLUG_CLS = CompAxisPlugOperator

    compAxisX = DoubleField(default_value=0.0, writable=False)
    cax = compAxisX

    compAxisY = DoubleField(default_value=0.0, writable=False)
    cay = compAxisY

    compAxisZ = DoubleField(default_value=0.0, writable=False)
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

    compPivotX = DoubleLinearField(default_value=0.0, writable=False)
    cpx = compPivotX

    compPivotY = DoubleLinearField(default_value=0.0, writable=False)
    cpy = compPivotY

    compPivotZ = DoubleLinearField(default_value=0.0, writable=False)
    cpz = compPivotZ


class CompPivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CompPivotPlugOperator]
):
    __slots__ = ()

    compPivotX = DoubleLinearField(default_value=0.0, writable=False)
    cpx = compPivotX

    compPivotY = DoubleLinearField(default_value=0.0, writable=False)
    cpy = compPivotY

    compPivotZ = DoubleLinearField(default_value=0.0, writable=False)
    cpz = compPivotZ


class CompPivotField(
    DoubleLinear3CompoundBaseField[
        CompPivotAttrOperator, CompPivotPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CompPivotAttrOperator
    PLUG_CLS = CompPivotPlugOperator

    compPivotX = DoubleLinearField(default_value=0.0, writable=False)
    cpx = compPivotX

    compPivotY = DoubleLinearField(default_value=0.0, writable=False)
    cpy = compPivotY

    compPivotZ = DoubleLinearField(default_value=0.0, writable=False)
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

    compAnchorX = DoubleLinearField(default_value=0.0, writable=False)
    cnx = compAnchorX

    compAnchorY = DoubleLinearField(default_value=0.0, writable=False)
    cny = compAnchorY

    compAnchorZ = DoubleLinearField(default_value=0.0, writable=False)
    cnz = compAnchorZ


class CompAnchorAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CompAnchorPlugOperator]
):
    __slots__ = ()

    compAnchorX = DoubleLinearField(default_value=0.0, writable=False)
    cnx = compAnchorX

    compAnchorY = DoubleLinearField(default_value=0.0, writable=False)
    cny = compAnchorY

    compAnchorZ = DoubleLinearField(default_value=0.0, writable=False)
    cnz = compAnchorZ


class CompAnchorField(
    DoubleLinear3CompoundBaseField[
        CompAnchorAttrOperator, CompAnchorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CompAnchorAttrOperator
    PLUG_CLS = CompAnchorPlugOperator

    compAnchorX = DoubleLinearField(default_value=0.0, writable=False)
    cnx = compAnchorX

    compAnchorY = DoubleLinearField(default_value=0.0, writable=False)
    cny = compAnchorY

    compAnchorZ = DoubleLinearField(default_value=0.0, writable=False)
    cnz = compAnchorZ
