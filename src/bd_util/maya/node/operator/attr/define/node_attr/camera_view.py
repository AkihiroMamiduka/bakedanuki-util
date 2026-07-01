# coding: utf-8

from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
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

    eyeX = DoubleLinearField()
    ex = eyeX

    eyeY = DoubleLinearField()
    ey = eyeY

    eyeZ = DoubleLinearField()
    ez = eyeZ


class EyeAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[EyePlugOperator]
):
    __slots__ = ()

    eyeX = DoubleLinearField()
    ex = eyeX

    eyeY = DoubleLinearField()
    ey = eyeY

    eyeZ = DoubleLinearField()
    ez = eyeZ


class EyeField(
    DoubleLinear3CompoundBaseField[EyeAttrOperator, EyePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EyeAttrOperator
    PLUG_CLS = EyePlugOperator

    eyeX = DoubleLinearField()
    ex = eyeX

    eyeY = DoubleLinearField()
    ey = eyeY

    eyeZ = DoubleLinearField()
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

    centerOfInterestX = DoubleLinearField()
    cx = centerOfInterestX

    centerOfInterestY = DoubleLinearField()
    cy = centerOfInterestY

    centerOfInterestZ = DoubleLinearField()
    cz = centerOfInterestZ


class CenterOfInterestAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CenterOfInterestPlugOperator]
):
    __slots__ = ()

    centerOfInterestX = DoubleLinearField()
    cx = centerOfInterestX

    centerOfInterestY = DoubleLinearField()
    cy = centerOfInterestY

    centerOfInterestZ = DoubleLinearField()
    cz = centerOfInterestZ


class CenterOfInterestField(
    DoubleLinear3CompoundBaseField[CenterOfInterestAttrOperator, CenterOfInterestPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CenterOfInterestAttrOperator
    PLUG_CLS = CenterOfInterestPlugOperator

    centerOfInterestX = DoubleLinearField()
    cx = centerOfInterestX

    centerOfInterestY = DoubleLinearField()
    cy = centerOfInterestY

    centerOfInterestZ = DoubleLinearField()
    cz = centerOfInterestZ


class UpPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["UpAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("upX", "ux"),
        ("upY", "uy"),
        ("upZ", "uz"),
    )

    upX = DoubleLinearField()
    ux = upX

    upY = DoubleLinearField()
    uy = upY

    upZ = DoubleLinearField()
    uz = upZ


class UpAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[UpPlugOperator]
):
    __slots__ = ()

    upX = DoubleLinearField()
    ux = upX

    upY = DoubleLinearField()
    uy = upY

    upZ = DoubleLinearField()
    uz = upZ


class UpField(
    DoubleLinear3CompoundBaseField[UpAttrOperator, UpPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UpAttrOperator
    PLUG_CLS = UpPlugOperator

    upX = DoubleLinearField()
    ux = upX

    upY = DoubleLinearField()
    uy = upY

    upZ = DoubleLinearField()
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

    tumblePivotX = DoubleLinearField()
    tpx = tumblePivotX

    tumblePivotY = DoubleLinearField()
    tpy = tumblePivotY

    tumblePivotZ = DoubleLinearField()
    tpz = tumblePivotZ


class TumblePivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[TumblePivotPlugOperator]
):
    __slots__ = ()

    tumblePivotX = DoubleLinearField()
    tpx = tumblePivotX

    tumblePivotY = DoubleLinearField()
    tpy = tumblePivotY

    tumblePivotZ = DoubleLinearField()
    tpz = tumblePivotZ


class TumblePivotField(
    DoubleLinear3CompoundBaseField[TumblePivotAttrOperator, TumblePivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TumblePivotAttrOperator
    PLUG_CLS = TumblePivotPlugOperator

    tumblePivotX = DoubleLinearField()
    tpx = tumblePivotX

    tumblePivotY = DoubleLinearField()
    tpy = tumblePivotY

    tumblePivotZ = DoubleLinearField()
    tpz = tumblePivotZ
