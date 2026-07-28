# coding: utf-8

from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class EyePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["EyeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eyeX", "ex"),
        ("eyeY", "ey"),
        ("eyeZ", "ez"),
    )

    eyeX = DoubleLinearField(default_value=60.0)
    ex = eyeX

    eyeY = DoubleLinearField(default_value=45.0)
    ey = eyeY

    eyeZ = DoubleLinearField(default_value=60.0)
    ez = eyeZ


class EyeAttrOperator(DoubleLinear3CompoundBaseAttrOperator[EyePlugOperator]):
    __slots__ = ()

    eyeX = DoubleLinearField(default_value=60.0)
    ex = eyeX

    eyeY = DoubleLinearField(default_value=45.0)
    ey = eyeY

    eyeZ = DoubleLinearField(default_value=60.0)
    ez = eyeZ


class EyeField(
    DoubleLinear3CompoundBaseField[EyeAttrOperator, EyePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EyeAttrOperator
    PLUG_CLS = EyePlugOperator

    eyeX = DoubleLinearField(default_value=60.0)
    ex = eyeX

    eyeY = DoubleLinearField(default_value=45.0)
    ey = eyeY

    eyeZ = DoubleLinearField(default_value=60.0)
    ez = eyeZ


class CenterOfInterestPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["CenterOfInterestAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("centerOfInterestX", "cx"),
        ("centerOfInterestY", "cy"),
        ("centerOfInterestZ", "cz"),
    )

    centerOfInterestX = DoubleLinearField(default_value=0.0)
    cx = centerOfInterestX

    centerOfInterestY = DoubleLinearField(default_value=0.0)
    cy = centerOfInterestY

    centerOfInterestZ = DoubleLinearField(default_value=0.0)
    cz = centerOfInterestZ


class CenterOfInterestAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CenterOfInterestPlugOperator]
):
    __slots__ = ()

    centerOfInterestX = DoubleLinearField(default_value=0.0)
    cx = centerOfInterestX

    centerOfInterestY = DoubleLinearField(default_value=0.0)
    cy = centerOfInterestY

    centerOfInterestZ = DoubleLinearField(default_value=0.0)
    cz = centerOfInterestZ


class CenterOfInterestField(
    DoubleLinear3CompoundBaseField[
        CenterOfInterestAttrOperator, CenterOfInterestPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CenterOfInterestAttrOperator
    PLUG_CLS = CenterOfInterestPlugOperator

    centerOfInterestX = DoubleLinearField(default_value=0.0)
    cx = centerOfInterestX

    centerOfInterestY = DoubleLinearField(default_value=0.0)
    cy = centerOfInterestY

    centerOfInterestZ = DoubleLinearField(default_value=0.0)
    cz = centerOfInterestZ


class UpPlugOperator(DoubleLinear3CompoundBasePlugOperator["UpAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("upX", "ux"),
        ("upY", "uy"),
        ("upZ", "uz"),
    )

    upX = DoubleLinearField(default_value=0.0)
    ux = upX

    upY = DoubleLinearField(default_value=1.0)
    uy = upY

    upZ = DoubleLinearField(default_value=0.0)
    uz = upZ


class UpAttrOperator(DoubleLinear3CompoundBaseAttrOperator[UpPlugOperator]):
    __slots__ = ()

    upX = DoubleLinearField(default_value=0.0)
    ux = upX

    upY = DoubleLinearField(default_value=1.0)
    uy = upY

    upZ = DoubleLinearField(default_value=0.0)
    uz = upZ


class UpField(DoubleLinear3CompoundBaseField[UpAttrOperator, UpPlugOperator]):
    __slots__ = ()

    ATTR_CLS = UpAttrOperator
    PLUG_CLS = UpPlugOperator

    upX = DoubleLinearField(default_value=0.0)
    ux = upX

    upY = DoubleLinearField(default_value=1.0)
    uy = upY

    upZ = DoubleLinearField(default_value=0.0)
    uz = upZ


class TumblePivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["TumblePivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tumblePivotX", "tpx"),
        ("tumblePivotY", "tpy"),
        ("tumblePivotZ", "tpz"),
    )

    tumblePivotX = DoubleLinearField(default_value=0.0)
    tpx = tumblePivotX

    tumblePivotY = DoubleLinearField(default_value=0.0)
    tpy = tumblePivotY

    tumblePivotZ = DoubleLinearField(default_value=0.0)
    tpz = tumblePivotZ


class TumblePivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[TumblePivotPlugOperator]
):
    __slots__ = ()

    tumblePivotX = DoubleLinearField(default_value=0.0)
    tpx = tumblePivotX

    tumblePivotY = DoubleLinearField(default_value=0.0)
    tpy = tumblePivotY

    tumblePivotZ = DoubleLinearField(default_value=0.0)
    tpz = tumblePivotZ


class TumblePivotField(
    DoubleLinear3CompoundBaseField[
        TumblePivotAttrOperator, TumblePivotPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = TumblePivotAttrOperator
    PLUG_CLS = TumblePivotPlugOperator

    tumblePivotX = DoubleLinearField(default_value=0.0)
    tpx = tumblePivotX

    tumblePivotY = DoubleLinearField(default_value=0.0)
    tpy = tumblePivotY

    tumblePivotZ = DoubleLinearField(default_value=0.0)
    tpz = tumblePivotZ
