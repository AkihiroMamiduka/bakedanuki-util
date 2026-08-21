# coding: utf-8
from .._core import Shape
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.typed import TypedField


class ConstraintMethodEnumPlugOperator(
    EnumPlugOperator["ConstraintMethodEnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    RUBBER_BAND = 1
    TRANSFORM = 2
    STICK = 3
    HAIR_TO_HAIR = 4
    HAIR_BUNCH = 5
    COLLIDE_SPHERE = 6
    COLLIDE_CUBE = 7


class ConstraintMethodEnumAttrOperator(
    EnumAttrOperator[ConstraintMethodEnumPlugOperator]
):
    __slots__ = ()

    OFF = 0
    RUBBER_BAND = 1
    TRANSFORM = 2
    STICK = 3
    HAIR_TO_HAIR = 4
    HAIR_BUNCH = 5
    COLLIDE_SPHERE = 6
    COLLIDE_CUBE = 7

    NAME_MAP = {
        OFF: "Off",
        RUBBER_BAND: "Rubber Band",
        TRANSFORM: "Transform",
        STICK: "Stick",
        HAIR_TO_HAIR: "Hair To Hair",
        HAIR_BUNCH: "Hair Bunch",
        COLLIDE_SPHERE: "Collide Sphere",
        COLLIDE_CUBE: "Collide Cube",
    }


class ConstraintMethodEnumField(
    EnumField[
        ConstraintMethodEnumAttrOperator, ConstraintMethodEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintMethodEnumAttrOperator
    PLUG_CLS = ConstraintMethodEnumPlugOperator


class PointMethodEnumPlugOperator(
    EnumPlugOperator["PointMethodEnumAttrOperator"]
):
    __slots__ = ()

    NEAREST = 0
    U_PARAMETER = 1
    U_DISTANCE = 2


class PointMethodEnumAttrOperator(
    EnumAttrOperator[PointMethodEnumPlugOperator]
):
    __slots__ = ()

    NEAREST = 0
    U_PARAMETER = 1
    U_DISTANCE = 2

    NAME_MAP = {
        NEAREST: "Nearest",
        U_PARAMETER: "U Parameter",
        U_DISTANCE: "U Distance",
    }


class PointMethodEnumField(
    EnumField[PointMethodEnumAttrOperator, PointMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointMethodEnumAttrOperator
    PLUG_CLS = PointMethodEnumPlugOperator


class GeneratedHairConstraint(Shape):
    __slots__ = ()

    NODE_TYPE = "hairConstraint"

    curveIndices = LongField(multi=True, default_value=0)
    cin = curveIndices

    constraintMethod = ConstraintMethodEnumField(default_value=1)
    cm = constraintMethod

    pointMethod = PointMethodEnumField(default_value=0)
    pmt = pointMethod

    stiffness = DoubleField(
        default_value=0.5, soft_min_value=0.0, soft_max_value=1.0
    )
    stf = stiffness

    glueStrength = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    gst = glueStrength

    uParameter = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    upr = uParameter

    uDistance = DoubleField(
        default_value=1.0, min_value=0.0, soft_max_value=50.0
    )
    udi = uDistance

    outPin = TypedField(multi=True, writable=False)
    opn = outPin
