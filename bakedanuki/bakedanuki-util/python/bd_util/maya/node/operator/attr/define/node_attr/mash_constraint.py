# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class MColourPlugOperator(
    Float3CompoundBasePlugOperator["MColourAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("mColourR", "mcr"),
        ("mColourG", "mcg"),
        ("mColourB", "mcb"),
    )

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
    mcb = mColourB


class MColourAttrOperator(Float3CompoundBaseAttrOperator[MColourPlugOperator]):
    __slots__ = ()

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
    mcb = mColourB


class MColourField(
    Float3CompoundBaseField[MColourAttrOperator, MColourPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MColourAttrOperator
    PLUG_CLS = MColourPlugOperator

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
    mcb = mColourB


class ConnectionColourPlugOperator(
    Float3CompoundBasePlugOperator["ConnectionColourAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("connectionColorRed", "connectionColorRed"),
        ("connectionColorGreen", "connectionColorGreen"),
        ("connectionColorBlue", "connectionColorBlue"),
    )

    connectionColorRed = FloatField(default_value=1.0)

    connectionColorGreen = FloatField(default_value=1.0)

    connectionColorBlue = FloatField(default_value=1.0)


class ConnectionColourAttrOperator(
    Float3CompoundBaseAttrOperator[ConnectionColourPlugOperator]
):
    __slots__ = ()

    connectionColorRed = FloatField(default_value=1.0)

    connectionColorGreen = FloatField(default_value=1.0)

    connectionColorBlue = FloatField(default_value=1.0)


class ConnectionColourField(
    Float3CompoundBaseField[
        ConnectionColourAttrOperator, ConnectionColourPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ConnectionColourAttrOperator
    PLUG_CLS = ConnectionColourPlugOperator

    connectionColorRed = FloatField(default_value=1.0)

    connectionColorGreen = FloatField(default_value=1.0)

    connectionColorBlue = FloatField(default_value=1.0)


class LinearMotorTargetSpeedPlugOperator(
    Float3CompoundBasePlugOperator["LinearMotorTargetSpeedAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("linearMotorTargetSpeedX", "linearMotorTargetSpeedx"),
        ("linearMotorTargetSpeedY", "linearMotorTargetSpeedy"),
        ("linearMotorTargetSpeedZ", "linearMotorTargetSpeedz"),
    )

    linearMotorTargetSpeedX = FloatField(default_value=0.0)
    linearMotorTargetSpeedx = linearMotorTargetSpeedX

    linearMotorTargetSpeedY = FloatField(default_value=0.0)
    linearMotorTargetSpeedy = linearMotorTargetSpeedY

    linearMotorTargetSpeedZ = FloatField(default_value=0.0)
    linearMotorTargetSpeedz = linearMotorTargetSpeedZ


class LinearMotorTargetSpeedAttrOperator(
    Float3CompoundBaseAttrOperator[LinearMotorTargetSpeedPlugOperator]
):
    __slots__ = ()

    linearMotorTargetSpeedX = FloatField(default_value=0.0)
    linearMotorTargetSpeedx = linearMotorTargetSpeedX

    linearMotorTargetSpeedY = FloatField(default_value=0.0)
    linearMotorTargetSpeedy = linearMotorTargetSpeedY

    linearMotorTargetSpeedZ = FloatField(default_value=0.0)
    linearMotorTargetSpeedz = linearMotorTargetSpeedZ


class LinearMotorTargetSpeedField(
    Float3CompoundBaseField[
        LinearMotorTargetSpeedAttrOperator, LinearMotorTargetSpeedPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = LinearMotorTargetSpeedAttrOperator
    PLUG_CLS = LinearMotorTargetSpeedPlugOperator

    linearMotorTargetSpeedX = FloatField(default_value=0.0)
    linearMotorTargetSpeedx = linearMotorTargetSpeedX

    linearMotorTargetSpeedY = FloatField(default_value=0.0)
    linearMotorTargetSpeedy = linearMotorTargetSpeedY

    linearMotorTargetSpeedZ = FloatField(default_value=0.0)
    linearMotorTargetSpeedz = linearMotorTargetSpeedZ


class LinearMotorMaxForcePlugOperator(
    Float3CompoundBasePlugOperator["LinearMotorMaxForceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("linearMotorMaxForceX", "linearMotorMaxForcex"),
        ("linearMotorMaxForceY", "linearMotorMaxForcey"),
        ("linearMotorMaxForceZ", "linearMotorMaxForcez"),
    )

    linearMotorMaxForceX = FloatField(default_value=10.0)
    linearMotorMaxForcex = linearMotorMaxForceX

    linearMotorMaxForceY = FloatField(default_value=10.0)
    linearMotorMaxForcey = linearMotorMaxForceY

    linearMotorMaxForceZ = FloatField(default_value=10.0)
    linearMotorMaxForcez = linearMotorMaxForceZ


class LinearMotorMaxForceAttrOperator(
    Float3CompoundBaseAttrOperator[LinearMotorMaxForcePlugOperator]
):
    __slots__ = ()

    linearMotorMaxForceX = FloatField(default_value=10.0)
    linearMotorMaxForcex = linearMotorMaxForceX

    linearMotorMaxForceY = FloatField(default_value=10.0)
    linearMotorMaxForcey = linearMotorMaxForceY

    linearMotorMaxForceZ = FloatField(default_value=10.0)
    linearMotorMaxForcez = linearMotorMaxForceZ


class LinearMotorMaxForceField(
    Float3CompoundBaseField[
        LinearMotorMaxForceAttrOperator, LinearMotorMaxForcePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = LinearMotorMaxForceAttrOperator
    PLUG_CLS = LinearMotorMaxForcePlugOperator

    linearMotorMaxForceX = FloatField(default_value=10.0)
    linearMotorMaxForcex = linearMotorMaxForceX

    linearMotorMaxForceY = FloatField(default_value=10.0)
    linearMotorMaxForcey = linearMotorMaxForceY

    linearMotorMaxForceZ = FloatField(default_value=10.0)
    linearMotorMaxForcez = linearMotorMaxForceZ


class AngularMotorTargetSpeedPlugOperator(
    Float3CompoundBasePlugOperator["AngularMotorTargetSpeedAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("angularMotorTargetSpeedX", "angularMotorTargetSpeedx"),
        ("angularMotorTargetSpeedY", "angularMotorTargetSpeedy"),
        ("angularMotorTargetSpeedZ", "angularMotorTargetSpeedz"),
    )

    angularMotorTargetSpeedX = FloatField(default_value=0.0)
    angularMotorTargetSpeedx = angularMotorTargetSpeedX

    angularMotorTargetSpeedY = FloatField(default_value=0.0)
    angularMotorTargetSpeedy = angularMotorTargetSpeedY

    angularMotorTargetSpeedZ = FloatField(default_value=0.0)
    angularMotorTargetSpeedz = angularMotorTargetSpeedZ


class AngularMotorTargetSpeedAttrOperator(
    Float3CompoundBaseAttrOperator[AngularMotorTargetSpeedPlugOperator]
):
    __slots__ = ()

    angularMotorTargetSpeedX = FloatField(default_value=0.0)
    angularMotorTargetSpeedx = angularMotorTargetSpeedX

    angularMotorTargetSpeedY = FloatField(default_value=0.0)
    angularMotorTargetSpeedy = angularMotorTargetSpeedY

    angularMotorTargetSpeedZ = FloatField(default_value=0.0)
    angularMotorTargetSpeedz = angularMotorTargetSpeedZ


class AngularMotorTargetSpeedField(
    Float3CompoundBaseField[
        AngularMotorTargetSpeedAttrOperator,
        AngularMotorTargetSpeedPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = AngularMotorTargetSpeedAttrOperator
    PLUG_CLS = AngularMotorTargetSpeedPlugOperator

    angularMotorTargetSpeedX = FloatField(default_value=0.0)
    angularMotorTargetSpeedx = angularMotorTargetSpeedX

    angularMotorTargetSpeedY = FloatField(default_value=0.0)
    angularMotorTargetSpeedy = angularMotorTargetSpeedY

    angularMotorTargetSpeedZ = FloatField(default_value=0.0)
    angularMotorTargetSpeedz = angularMotorTargetSpeedZ


class AngularMotorMaxForcePlugOperator(
    Float3CompoundBasePlugOperator["AngularMotorMaxForceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("angularMotorMaxForceX", "angularMotorMaxForcex"),
        ("angularMotorMaxForceY", "angularMotorMaxForcey"),
        ("angularMotorMaxForceZ", "angularMotorMaxForcez"),
    )

    angularMotorMaxForceX = FloatField(default_value=10.0)
    angularMotorMaxForcex = angularMotorMaxForceX

    angularMotorMaxForceY = FloatField(default_value=10.0)
    angularMotorMaxForcey = angularMotorMaxForceY

    angularMotorMaxForceZ = FloatField(default_value=10.0)
    angularMotorMaxForcez = angularMotorMaxForceZ


class AngularMotorMaxForceAttrOperator(
    Float3CompoundBaseAttrOperator[AngularMotorMaxForcePlugOperator]
):
    __slots__ = ()

    angularMotorMaxForceX = FloatField(default_value=10.0)
    angularMotorMaxForcex = angularMotorMaxForceX

    angularMotorMaxForceY = FloatField(default_value=10.0)
    angularMotorMaxForcey = angularMotorMaxForceY

    angularMotorMaxForceZ = FloatField(default_value=10.0)
    angularMotorMaxForcez = angularMotorMaxForceZ


class AngularMotorMaxForceField(
    Float3CompoundBaseField[
        AngularMotorMaxForceAttrOperator, AngularMotorMaxForcePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AngularMotorMaxForceAttrOperator
    PLUG_CLS = AngularMotorMaxForcePlugOperator

    angularMotorMaxForceX = FloatField(default_value=10.0)
    angularMotorMaxForcex = angularMotorMaxForceX

    angularMotorMaxForceY = FloatField(default_value=10.0)
    angularMotorMaxForcey = angularMotorMaxForceY

    angularMotorMaxForceZ = FloatField(default_value=10.0)
    angularMotorMaxForcez = angularMotorMaxForceZ


class ConstraintMinimumPositionLimitPlugOperator(
    Float3CompoundBasePlugOperator[
        "ConstraintMinimumPositionLimitAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintMinimumPositionLimitX", "constraintMinimumPositionLimitx"),
        ("constraintMinimumPositionLimitY", "constraintMinimumPositionLimity"),
        ("constraintMinimumPositionLimitZ", "constraintMinimumPositionLimitz"),
    )

    constraintMinimumPositionLimitX = FloatField(default_value=0.0)
    constraintMinimumPositionLimitx = constraintMinimumPositionLimitX

    constraintMinimumPositionLimitY = FloatField(default_value=0.0)
    constraintMinimumPositionLimity = constraintMinimumPositionLimitY

    constraintMinimumPositionLimitZ = FloatField(default_value=0.0)
    constraintMinimumPositionLimitz = constraintMinimumPositionLimitZ


class ConstraintMinimumPositionLimitAttrOperator(
    Float3CompoundBaseAttrOperator[ConstraintMinimumPositionLimitPlugOperator]
):
    __slots__ = ()

    constraintMinimumPositionLimitX = FloatField(default_value=0.0)
    constraintMinimumPositionLimitx = constraintMinimumPositionLimitX

    constraintMinimumPositionLimitY = FloatField(default_value=0.0)
    constraintMinimumPositionLimity = constraintMinimumPositionLimitY

    constraintMinimumPositionLimitZ = FloatField(default_value=0.0)
    constraintMinimumPositionLimitz = constraintMinimumPositionLimitZ


class ConstraintMinimumPositionLimitField(
    Float3CompoundBaseField[
        ConstraintMinimumPositionLimitAttrOperator,
        ConstraintMinimumPositionLimitPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintMinimumPositionLimitAttrOperator
    PLUG_CLS = ConstraintMinimumPositionLimitPlugOperator

    constraintMinimumPositionLimitX = FloatField(default_value=0.0)
    constraintMinimumPositionLimitx = constraintMinimumPositionLimitX

    constraintMinimumPositionLimitY = FloatField(default_value=0.0)
    constraintMinimumPositionLimity = constraintMinimumPositionLimitY

    constraintMinimumPositionLimitZ = FloatField(default_value=0.0)
    constraintMinimumPositionLimitz = constraintMinimumPositionLimitZ


class ConstraintMaximumPositionLimitPlugOperator(
    Float3CompoundBasePlugOperator[
        "ConstraintMaximumPositionLimitAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintMaximumPositionLimitX", "constraintMaximumPositionLimitx"),
        ("constraintMaximumPositionLimitY", "constraintMaximumPositionLimity"),
        ("constraintMaximumPositionLimitZ", "constraintMaximumPositionLimitz"),
    )

    constraintMaximumPositionLimitX = FloatField(default_value=0.0)
    constraintMaximumPositionLimitx = constraintMaximumPositionLimitX

    constraintMaximumPositionLimitY = FloatField(default_value=0.0)
    constraintMaximumPositionLimity = constraintMaximumPositionLimitY

    constraintMaximumPositionLimitZ = FloatField(default_value=0.0)
    constraintMaximumPositionLimitz = constraintMaximumPositionLimitZ


class ConstraintMaximumPositionLimitAttrOperator(
    Float3CompoundBaseAttrOperator[ConstraintMaximumPositionLimitPlugOperator]
):
    __slots__ = ()

    constraintMaximumPositionLimitX = FloatField(default_value=0.0)
    constraintMaximumPositionLimitx = constraintMaximumPositionLimitX

    constraintMaximumPositionLimitY = FloatField(default_value=0.0)
    constraintMaximumPositionLimity = constraintMaximumPositionLimitY

    constraintMaximumPositionLimitZ = FloatField(default_value=0.0)
    constraintMaximumPositionLimitz = constraintMaximumPositionLimitZ


class ConstraintMaximumPositionLimitField(
    Float3CompoundBaseField[
        ConstraintMaximumPositionLimitAttrOperator,
        ConstraintMaximumPositionLimitPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintMaximumPositionLimitAttrOperator
    PLUG_CLS = ConstraintMaximumPositionLimitPlugOperator

    constraintMaximumPositionLimitX = FloatField(default_value=0.0)
    constraintMaximumPositionLimitx = constraintMaximumPositionLimitX

    constraintMaximumPositionLimitY = FloatField(default_value=0.0)
    constraintMaximumPositionLimity = constraintMaximumPositionLimitY

    constraintMaximumPositionLimitZ = FloatField(default_value=0.0)
    constraintMaximumPositionLimitz = constraintMaximumPositionLimitZ


class ConstraintMinimumRotationLimitPlugOperator(
    Float3CompoundBasePlugOperator[
        "ConstraintMinimumRotationLimitAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintMinimumRotationLimitX", "constraintMinimumRotationLimitx"),
        ("constraintMinimumRotationLimitY", "constraintMinimumRotationLimity"),
        ("constraintMinimumRotationLimitZ", "constraintMinimumRotationLimitz"),
    )

    constraintMinimumRotationLimitX = FloatField(default_value=0.0)
    constraintMinimumRotationLimitx = constraintMinimumRotationLimitX

    constraintMinimumRotationLimitY = FloatField(default_value=0.0)
    constraintMinimumRotationLimity = constraintMinimumRotationLimitY

    constraintMinimumRotationLimitZ = FloatField(default_value=0.0)
    constraintMinimumRotationLimitz = constraintMinimumRotationLimitZ


class ConstraintMinimumRotationLimitAttrOperator(
    Float3CompoundBaseAttrOperator[ConstraintMinimumRotationLimitPlugOperator]
):
    __slots__ = ()

    constraintMinimumRotationLimitX = FloatField(default_value=0.0)
    constraintMinimumRotationLimitx = constraintMinimumRotationLimitX

    constraintMinimumRotationLimitY = FloatField(default_value=0.0)
    constraintMinimumRotationLimity = constraintMinimumRotationLimitY

    constraintMinimumRotationLimitZ = FloatField(default_value=0.0)
    constraintMinimumRotationLimitz = constraintMinimumRotationLimitZ


class ConstraintMinimumRotationLimitField(
    Float3CompoundBaseField[
        ConstraintMinimumRotationLimitAttrOperator,
        ConstraintMinimumRotationLimitPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintMinimumRotationLimitAttrOperator
    PLUG_CLS = ConstraintMinimumRotationLimitPlugOperator

    constraintMinimumRotationLimitX = FloatField(default_value=0.0)
    constraintMinimumRotationLimitx = constraintMinimumRotationLimitX

    constraintMinimumRotationLimitY = FloatField(default_value=0.0)
    constraintMinimumRotationLimity = constraintMinimumRotationLimitY

    constraintMinimumRotationLimitZ = FloatField(default_value=0.0)
    constraintMinimumRotationLimitz = constraintMinimumRotationLimitZ


class ConstraintMaximumRotationLimitPlugOperator(
    Float3CompoundBasePlugOperator[
        "ConstraintMaximumRotationLimitAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintMaximumRotationLimitX", "constraintMaximumRotationLimitx"),
        ("constraintMaximumRotationLimitY", "constraintMaximumRotationLimity"),
        ("constraintMaximumRotationLimitZ", "constraintMaximumRotationLimitz"),
    )

    constraintMaximumRotationLimitX = FloatField(default_value=0.0)
    constraintMaximumRotationLimitx = constraintMaximumRotationLimitX

    constraintMaximumRotationLimitY = FloatField(default_value=0.0)
    constraintMaximumRotationLimity = constraintMaximumRotationLimitY

    constraintMaximumRotationLimitZ = FloatField(default_value=0.0)
    constraintMaximumRotationLimitz = constraintMaximumRotationLimitZ


class ConstraintMaximumRotationLimitAttrOperator(
    Float3CompoundBaseAttrOperator[ConstraintMaximumRotationLimitPlugOperator]
):
    __slots__ = ()

    constraintMaximumRotationLimitX = FloatField(default_value=0.0)
    constraintMaximumRotationLimitx = constraintMaximumRotationLimitX

    constraintMaximumRotationLimitY = FloatField(default_value=0.0)
    constraintMaximumRotationLimity = constraintMaximumRotationLimitY

    constraintMaximumRotationLimitZ = FloatField(default_value=0.0)
    constraintMaximumRotationLimitz = constraintMaximumRotationLimitZ


class ConstraintMaximumRotationLimitField(
    Float3CompoundBaseField[
        ConstraintMaximumRotationLimitAttrOperator,
        ConstraintMaximumRotationLimitPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintMaximumRotationLimitAttrOperator
    PLUG_CLS = ConstraintMaximumRotationLimitPlugOperator

    constraintMaximumRotationLimitX = FloatField(default_value=0.0)
    constraintMaximumRotationLimitx = constraintMaximumRotationLimitX

    constraintMaximumRotationLimitY = FloatField(default_value=0.0)
    constraintMaximumRotationLimity = constraintMaximumRotationLimitY

    constraintMaximumRotationLimitZ = FloatField(default_value=0.0)
    constraintMaximumRotationLimitz = constraintMaximumRotationLimitZ


class PointOffsetPlugOperator(
    Float3CompoundBasePlugOperator["PointOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointOffsetX", "pointOffsetx"),
        ("pointOffsetY", "pointOffsety"),
        ("pointOffsetZ", "pointOffsetz"),
    )

    pointOffsetX = FloatField(default_value=0.0)
    pointOffsetx = pointOffsetX

    pointOffsetY = FloatField(default_value=0.0)
    pointOffsety = pointOffsetY

    pointOffsetZ = FloatField(default_value=0.0)
    pointOffsetz = pointOffsetZ


class PointOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[PointOffsetPlugOperator]
):
    __slots__ = ()

    pointOffsetX = FloatField(default_value=0.0)
    pointOffsetx = pointOffsetX

    pointOffsetY = FloatField(default_value=0.0)
    pointOffsety = pointOffsetY

    pointOffsetZ = FloatField(default_value=0.0)
    pointOffsetz = pointOffsetZ


class PointOffsetField(
    Float3CompoundBaseField[PointOffsetAttrOperator, PointOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointOffsetAttrOperator
    PLUG_CLS = PointOffsetPlugOperator

    pointOffsetX = FloatField(default_value=0.0)
    pointOffsetx = pointOffsetX

    pointOffsetY = FloatField(default_value=0.0)
    pointOffsety = pointOffsetY

    pointOffsetZ = FloatField(default_value=0.0)
    pointOffsetz = pointOffsetZ
