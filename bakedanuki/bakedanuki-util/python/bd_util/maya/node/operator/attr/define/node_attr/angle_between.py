# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import (
    Double3Field,
)
from ..custom.at.scalar_compound.unit_compound.angle_compound.double3._base import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class Vector1PlugOperator(
    DoubleLinear3CompoundBasePlugOperator["Vector1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vector1X", "v1x"),
        ("vector1Y", "v1y"),
        ("vector1Z", "v1z"),
    )

    vector1X = DoubleLinearField(default_value=0.0)
    v1x = vector1X

    vector1Y = DoubleLinearField(default_value=1.0)
    v1y = vector1Y

    vector1Z = DoubleLinearField(default_value=0.0)
    v1z = vector1Z


class Vector1AttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Vector1PlugOperator]
):
    __slots__ = ()

    vector1X = DoubleLinearField(default_value=0.0)
    v1x = vector1X

    vector1Y = DoubleLinearField(default_value=1.0)
    v1y = vector1Y

    vector1Z = DoubleLinearField(default_value=0.0)
    v1z = vector1Z


class Vector1Field(
    DoubleLinear3CompoundBaseField[Vector1AttrOperator, Vector1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Vector1AttrOperator
    PLUG_CLS = Vector1PlugOperator

    vector1X = DoubleLinearField(default_value=0.0)
    v1x = vector1X

    vector1Y = DoubleLinearField(default_value=1.0)
    v1y = vector1Y

    vector1Z = DoubleLinearField(default_value=0.0)
    v1z = vector1Z


class Vector2PlugOperator(
    DoubleLinear3CompoundBasePlugOperator["Vector2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vector2X", "v2x"),
        ("vector2Y", "v2y"),
        ("vector2Z", "v2z"),
    )

    vector2X = DoubleLinearField(default_value=0.0)
    v2x = vector2X

    vector2Y = DoubleLinearField(default_value=0.0)
    v2y = vector2Y

    vector2Z = DoubleLinearField(default_value=1.0)
    v2z = vector2Z


class Vector2AttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Vector2PlugOperator]
):
    __slots__ = ()

    vector2X = DoubleLinearField(default_value=0.0)
    v2x = vector2X

    vector2Y = DoubleLinearField(default_value=0.0)
    v2y = vector2Y

    vector2Z = DoubleLinearField(default_value=1.0)
    v2z = vector2Z


class Vector2Field(
    DoubleLinear3CompoundBaseField[Vector2AttrOperator, Vector2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Vector2AttrOperator
    PLUG_CLS = Vector2PlugOperator

    vector2X = DoubleLinearField(default_value=0.0)
    v2x = vector2X

    vector2Y = DoubleLinearField(default_value=0.0)
    v2y = vector2Y

    vector2Z = DoubleLinearField(default_value=1.0)
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

    axis = Double3Field(default_value=(0.0, 0.0, 1.0), writable=False)
    ax = axis

    angle = DoubleAngleField(default_value=0.0, writable=False)
    a = angle


class AxisAngleAttrOperator(CompoundAttrOperator[AxisAnglePlugOperator]):
    __slots__ = ()

    axis = Double3Field(default_value=(0.0, 0.0, 1.0), writable=False)
    ax = axis

    angle = DoubleAngleField(default_value=0.0, writable=False)
    a = angle


class AxisAngleField(
    CompoundField[AxisAngleAttrOperator, AxisAnglePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisAngleAttrOperator
    PLUG_CLS = AxisAnglePlugOperator

    axis = Double3Field(default_value=(0.0, 0.0, 1.0), writable=False)
    ax = axis

    angle = DoubleAngleField(default_value=0.0, writable=False)
    a = angle
