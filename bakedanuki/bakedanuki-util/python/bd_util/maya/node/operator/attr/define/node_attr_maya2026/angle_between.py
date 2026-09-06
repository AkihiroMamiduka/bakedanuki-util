# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..custom import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)


class AxisAngle_axisPlugOperator(
    Double3CompoundBasePlugOperator["AxisAngle_axisAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("axisX", "axx"),
        ("axisY", "axy"),
        ("axisZ", "axz"),
    )

    axisX = DoubleField(default_value=0.0, writable=False)
    axx = axisX

    axisY = DoubleField(default_value=0.0, writable=False)
    axy = axisY

    axisZ = DoubleField(default_value=1.0, writable=False)
    axz = axisZ


class AxisAngle_axisAttrOperator(
    Double3CompoundBaseAttrOperator[AxisAngle_axisPlugOperator]
):
    __slots__ = ()

    axisX = DoubleField(default_value=0.0, writable=False)
    axx = axisX

    axisY = DoubleField(default_value=0.0, writable=False)
    axy = axisY

    axisZ = DoubleField(default_value=1.0, writable=False)
    axz = axisZ


class AxisAngle_axisField(
    Double3CompoundBaseField[
        AxisAngle_axisAttrOperator, AxisAngle_axisPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AxisAngle_axisAttrOperator
    PLUG_CLS = AxisAngle_axisPlugOperator

    axisX = DoubleField(default_value=0.0, writable=False)
    axx = axisX

    axisY = DoubleField(default_value=0.0, writable=False)
    axy = axisY

    axisZ = DoubleField(default_value=1.0, writable=False)
    axz = axisZ


class Vector1PlugOperator(
    Double3CompoundBasePlugOperator["Vector1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vector1X", "v1x"),
        ("vector1Y", "v1y"),
        ("vector1Z", "v1z"),
    )

    vector1X = DoubleField(default_value=0.0)
    v1x = vector1X

    vector1Y = DoubleField(default_value=1.0)
    v1y = vector1Y

    vector1Z = DoubleField(default_value=0.0)
    v1z = vector1Z


class Vector1AttrOperator(
    Double3CompoundBaseAttrOperator[Vector1PlugOperator]
):
    __slots__ = ()

    vector1X = DoubleField(default_value=0.0)
    v1x = vector1X

    vector1Y = DoubleField(default_value=1.0)
    v1y = vector1Y

    vector1Z = DoubleField(default_value=0.0)
    v1z = vector1Z


class Vector1Field(
    Double3CompoundBaseField[Vector1AttrOperator, Vector1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Vector1AttrOperator
    PLUG_CLS = Vector1PlugOperator

    vector1X = DoubleField(default_value=0.0)
    v1x = vector1X

    vector1Y = DoubleField(default_value=1.0)
    v1y = vector1Y

    vector1Z = DoubleField(default_value=0.0)
    v1z = vector1Z


class Vector2PlugOperator(
    Double3CompoundBasePlugOperator["Vector2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vector2X", "v2x"),
        ("vector2Y", "v2y"),
        ("vector2Z", "v2z"),
    )

    vector2X = DoubleField(default_value=0.0)
    v2x = vector2X

    vector2Y = DoubleField(default_value=0.0)
    v2y = vector2Y

    vector2Z = DoubleField(default_value=1.0)
    v2z = vector2Z


class Vector2AttrOperator(
    Double3CompoundBaseAttrOperator[Vector2PlugOperator]
):
    __slots__ = ()

    vector2X = DoubleField(default_value=0.0)
    v2x = vector2X

    vector2Y = DoubleField(default_value=0.0)
    v2y = vector2Y

    vector2Z = DoubleField(default_value=1.0)
    v2z = vector2Z


class Vector2Field(
    Double3CompoundBaseField[Vector2AttrOperator, Vector2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Vector2AttrOperator
    PLUG_CLS = Vector2PlugOperator

    vector2X = DoubleField(default_value=0.0)
    v2x = vector2X

    vector2Y = DoubleField(default_value=0.0)
    v2y = vector2Y

    vector2Z = DoubleField(default_value=1.0)
    v2z = vector2Z


class EulerPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["EulerAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eulerX", "eux"),
        ("eulerY", "euy"),
        ("eulerZ", "euz"),
    )

    eulerX = DoubleAngleField(default_value=0.0, writable=False)
    eux = eulerX

    eulerY = DoubleAngleField(default_value=0.0, writable=False)
    euy = eulerY

    eulerZ = DoubleAngleField(default_value=0.0, writable=False)
    euz = eulerZ


class EulerAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[EulerPlugOperator]
):
    __slots__ = ()

    eulerX = DoubleAngleField(default_value=0.0, writable=False)
    eux = eulerX

    eulerY = DoubleAngleField(default_value=0.0, writable=False)
    euy = eulerY

    eulerZ = DoubleAngleField(default_value=0.0, writable=False)
    euz = eulerZ


class EulerField(
    DoubleAngle3CompoundBaseField[EulerAttrOperator, EulerPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EulerAttrOperator
    PLUG_CLS = EulerPlugOperator

    eulerX = DoubleAngleField(default_value=0.0, writable=False)
    eux = eulerX

    eulerY = DoubleAngleField(default_value=0.0, writable=False)
    euy = eulerY

    eulerZ = DoubleAngleField(default_value=0.0, writable=False)
    euz = eulerZ


class AxisAnglePlugOperator(CompoundPlugOperator["AxisAngleAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("axis", "ax"),
        ("angle", "a"),
    )

    axis = AxisAngle_axisField(default_value=(0.0, 0.0, 1.0), writable=False)
    ax = axis

    angle = DoubleAngleField(default_value=0.0, writable=False)
    a = angle


class AxisAngleAttrOperator(CompoundAttrOperator[AxisAnglePlugOperator]):
    __slots__ = ()

    axis = AxisAngle_axisField(default_value=(0.0, 0.0, 1.0), writable=False)
    ax = axis

    angle = DoubleAngleField(default_value=0.0, writable=False)
    a = angle


class AxisAngleField(
    CompoundField[AxisAngleAttrOperator, AxisAnglePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisAngleAttrOperator
    PLUG_CLS = AxisAnglePlugOperator

    axis = AxisAngle_axisField(default_value=(0.0, 0.0, 1.0), writable=False)
    ax = axis

    angle = DoubleAngleField(default_value=0.0, writable=False)
    a = angle
