# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
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

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class MColourAttrOperator(
    Float3CompoundBaseAttrOperator[MColourPlugOperator]
):
    __slots__ = ()

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class MColourField(
    Float3CompoundBaseField[MColourAttrOperator, MColourPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MColourAttrOperator
    PLUG_CLS = MColourPlugOperator

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
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

    connectionColorRed = FloatField()

    connectionColorGreen = FloatField()

    connectionColorBlue = FloatField()


class ConnectionColourAttrOperator(
    Float3CompoundBaseAttrOperator[ConnectionColourPlugOperator]
):
    __slots__ = ()

    connectionColorRed = FloatField()

    connectionColorGreen = FloatField()

    connectionColorBlue = FloatField()


class ConnectionColourField(
    Float3CompoundBaseField[ConnectionColourAttrOperator, ConnectionColourPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConnectionColourAttrOperator
    PLUG_CLS = ConnectionColourPlugOperator

    connectionColorRed = FloatField()

    connectionColorGreen = FloatField()

    connectionColorBlue = FloatField()


class LinearMotorTargetSpeedPlugOperator(
    Float3CompoundBasePlugOperator["LinearMotorTargetSpeedAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("linearMotorTargetSpeedX", "linearMotorTargetSpeedx"),
        ("linearMotorTargetSpeedY", "linearMotorTargetSpeedy"),
        ("linearMotorTargetSpeedZ", "linearMotorTargetSpeedz"),
    )

    linearMotorTargetSpeedX = FloatField()
    linearMotorTargetSpeedx = linearMotorTargetSpeedX

    linearMotorTargetSpeedY = FloatField()
    linearMotorTargetSpeedy = linearMotorTargetSpeedY

    linearMotorTargetSpeedZ = FloatField()
    linearMotorTargetSpeedz = linearMotorTargetSpeedZ


class LinearMotorTargetSpeedAttrOperator(
    Float3CompoundBaseAttrOperator[LinearMotorTargetSpeedPlugOperator]
):
    __slots__ = ()

    linearMotorTargetSpeedX = FloatField()
    linearMotorTargetSpeedx = linearMotorTargetSpeedX

    linearMotorTargetSpeedY = FloatField()
    linearMotorTargetSpeedy = linearMotorTargetSpeedY

    linearMotorTargetSpeedZ = FloatField()
    linearMotorTargetSpeedz = linearMotorTargetSpeedZ


class LinearMotorTargetSpeedField(
    Float3CompoundBaseField[LinearMotorTargetSpeedAttrOperator, LinearMotorTargetSpeedPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LinearMotorTargetSpeedAttrOperator
    PLUG_CLS = LinearMotorTargetSpeedPlugOperator

    linearMotorTargetSpeedX = FloatField()
    linearMotorTargetSpeedx = linearMotorTargetSpeedX

    linearMotorTargetSpeedY = FloatField()
    linearMotorTargetSpeedy = linearMotorTargetSpeedY

    linearMotorTargetSpeedZ = FloatField()
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

    linearMotorMaxForceX = FloatField()
    linearMotorMaxForcex = linearMotorMaxForceX

    linearMotorMaxForceY = FloatField()
    linearMotorMaxForcey = linearMotorMaxForceY

    linearMotorMaxForceZ = FloatField()
    linearMotorMaxForcez = linearMotorMaxForceZ


class LinearMotorMaxForceAttrOperator(
    Float3CompoundBaseAttrOperator[LinearMotorMaxForcePlugOperator]
):
    __slots__ = ()

    linearMotorMaxForceX = FloatField()
    linearMotorMaxForcex = linearMotorMaxForceX

    linearMotorMaxForceY = FloatField()
    linearMotorMaxForcey = linearMotorMaxForceY

    linearMotorMaxForceZ = FloatField()
    linearMotorMaxForcez = linearMotorMaxForceZ


class LinearMotorMaxForceField(
    Float3CompoundBaseField[LinearMotorMaxForceAttrOperator, LinearMotorMaxForcePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LinearMotorMaxForceAttrOperator
    PLUG_CLS = LinearMotorMaxForcePlugOperator

    linearMotorMaxForceX = FloatField()
    linearMotorMaxForcex = linearMotorMaxForceX

    linearMotorMaxForceY = FloatField()
    linearMotorMaxForcey = linearMotorMaxForceY

    linearMotorMaxForceZ = FloatField()
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

    angularMotorTargetSpeedX = FloatField()
    angularMotorTargetSpeedx = angularMotorTargetSpeedX

    angularMotorTargetSpeedY = FloatField()
    angularMotorTargetSpeedy = angularMotorTargetSpeedY

    angularMotorTargetSpeedZ = FloatField()
    angularMotorTargetSpeedz = angularMotorTargetSpeedZ


class AngularMotorTargetSpeedAttrOperator(
    Float3CompoundBaseAttrOperator[AngularMotorTargetSpeedPlugOperator]
):
    __slots__ = ()

    angularMotorTargetSpeedX = FloatField()
    angularMotorTargetSpeedx = angularMotorTargetSpeedX

    angularMotorTargetSpeedY = FloatField()
    angularMotorTargetSpeedy = angularMotorTargetSpeedY

    angularMotorTargetSpeedZ = FloatField()
    angularMotorTargetSpeedz = angularMotorTargetSpeedZ


class AngularMotorTargetSpeedField(
    Float3CompoundBaseField[AngularMotorTargetSpeedAttrOperator, AngularMotorTargetSpeedPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AngularMotorTargetSpeedAttrOperator
    PLUG_CLS = AngularMotorTargetSpeedPlugOperator

    angularMotorTargetSpeedX = FloatField()
    angularMotorTargetSpeedx = angularMotorTargetSpeedX

    angularMotorTargetSpeedY = FloatField()
    angularMotorTargetSpeedy = angularMotorTargetSpeedY

    angularMotorTargetSpeedZ = FloatField()
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

    angularMotorMaxForceX = FloatField()
    angularMotorMaxForcex = angularMotorMaxForceX

    angularMotorMaxForceY = FloatField()
    angularMotorMaxForcey = angularMotorMaxForceY

    angularMotorMaxForceZ = FloatField()
    angularMotorMaxForcez = angularMotorMaxForceZ


class AngularMotorMaxForceAttrOperator(
    Float3CompoundBaseAttrOperator[AngularMotorMaxForcePlugOperator]
):
    __slots__ = ()

    angularMotorMaxForceX = FloatField()
    angularMotorMaxForcex = angularMotorMaxForceX

    angularMotorMaxForceY = FloatField()
    angularMotorMaxForcey = angularMotorMaxForceY

    angularMotorMaxForceZ = FloatField()
    angularMotorMaxForcez = angularMotorMaxForceZ


class AngularMotorMaxForceField(
    Float3CompoundBaseField[AngularMotorMaxForceAttrOperator, AngularMotorMaxForcePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AngularMotorMaxForceAttrOperator
    PLUG_CLS = AngularMotorMaxForcePlugOperator

    angularMotorMaxForceX = FloatField()
    angularMotorMaxForcex = angularMotorMaxForceX

    angularMotorMaxForceY = FloatField()
    angularMotorMaxForcey = angularMotorMaxForceY

    angularMotorMaxForceZ = FloatField()
    angularMotorMaxForcez = angularMotorMaxForceZ


class ConstraintMinimumPositionLimitPlugOperator(
    Float3CompoundBasePlugOperator["ConstraintMinimumPositionLimitAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintMinimumPositionLimitX", "constraintMinimumPositionLimitx"),
        ("constraintMinimumPositionLimitY", "constraintMinimumPositionLimity"),
        ("constraintMinimumPositionLimitZ", "constraintMinimumPositionLimitz"),
    )

    constraintMinimumPositionLimitX = FloatField()
    constraintMinimumPositionLimitx = constraintMinimumPositionLimitX

    constraintMinimumPositionLimitY = FloatField()
    constraintMinimumPositionLimity = constraintMinimumPositionLimitY

    constraintMinimumPositionLimitZ = FloatField()
    constraintMinimumPositionLimitz = constraintMinimumPositionLimitZ


class ConstraintMinimumPositionLimitAttrOperator(
    Float3CompoundBaseAttrOperator[ConstraintMinimumPositionLimitPlugOperator]
):
    __slots__ = ()

    constraintMinimumPositionLimitX = FloatField()
    constraintMinimumPositionLimitx = constraintMinimumPositionLimitX

    constraintMinimumPositionLimitY = FloatField()
    constraintMinimumPositionLimity = constraintMinimumPositionLimitY

    constraintMinimumPositionLimitZ = FloatField()
    constraintMinimumPositionLimitz = constraintMinimumPositionLimitZ


class ConstraintMinimumPositionLimitField(
    Float3CompoundBaseField[ConstraintMinimumPositionLimitAttrOperator, ConstraintMinimumPositionLimitPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintMinimumPositionLimitAttrOperator
    PLUG_CLS = ConstraintMinimumPositionLimitPlugOperator

    constraintMinimumPositionLimitX = FloatField()
    constraintMinimumPositionLimitx = constraintMinimumPositionLimitX

    constraintMinimumPositionLimitY = FloatField()
    constraintMinimumPositionLimity = constraintMinimumPositionLimitY

    constraintMinimumPositionLimitZ = FloatField()
    constraintMinimumPositionLimitz = constraintMinimumPositionLimitZ


class ConstraintMaximumPositionLimitPlugOperator(
    Float3CompoundBasePlugOperator["ConstraintMaximumPositionLimitAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintMaximumPositionLimitX", "constraintMaximumPositionLimitx"),
        ("constraintMaximumPositionLimitY", "constraintMaximumPositionLimity"),
        ("constraintMaximumPositionLimitZ", "constraintMaximumPositionLimitz"),
    )

    constraintMaximumPositionLimitX = FloatField()
    constraintMaximumPositionLimitx = constraintMaximumPositionLimitX

    constraintMaximumPositionLimitY = FloatField()
    constraintMaximumPositionLimity = constraintMaximumPositionLimitY

    constraintMaximumPositionLimitZ = FloatField()
    constraintMaximumPositionLimitz = constraintMaximumPositionLimitZ


class ConstraintMaximumPositionLimitAttrOperator(
    Float3CompoundBaseAttrOperator[ConstraintMaximumPositionLimitPlugOperator]
):
    __slots__ = ()

    constraintMaximumPositionLimitX = FloatField()
    constraintMaximumPositionLimitx = constraintMaximumPositionLimitX

    constraintMaximumPositionLimitY = FloatField()
    constraintMaximumPositionLimity = constraintMaximumPositionLimitY

    constraintMaximumPositionLimitZ = FloatField()
    constraintMaximumPositionLimitz = constraintMaximumPositionLimitZ


class ConstraintMaximumPositionLimitField(
    Float3CompoundBaseField[ConstraintMaximumPositionLimitAttrOperator, ConstraintMaximumPositionLimitPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintMaximumPositionLimitAttrOperator
    PLUG_CLS = ConstraintMaximumPositionLimitPlugOperator

    constraintMaximumPositionLimitX = FloatField()
    constraintMaximumPositionLimitx = constraintMaximumPositionLimitX

    constraintMaximumPositionLimitY = FloatField()
    constraintMaximumPositionLimity = constraintMaximumPositionLimitY

    constraintMaximumPositionLimitZ = FloatField()
    constraintMaximumPositionLimitz = constraintMaximumPositionLimitZ


class ConstraintMinimumRotationLimitPlugOperator(
    Float3CompoundBasePlugOperator["ConstraintMinimumRotationLimitAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintMinimumRotationLimitX", "constraintMinimumRotationLimitx"),
        ("constraintMinimumRotationLimitY", "constraintMinimumRotationLimity"),
        ("constraintMinimumRotationLimitZ", "constraintMinimumRotationLimitz"),
    )

    constraintMinimumRotationLimitX = FloatField()
    constraintMinimumRotationLimitx = constraintMinimumRotationLimitX

    constraintMinimumRotationLimitY = FloatField()
    constraintMinimumRotationLimity = constraintMinimumRotationLimitY

    constraintMinimumRotationLimitZ = FloatField()
    constraintMinimumRotationLimitz = constraintMinimumRotationLimitZ


class ConstraintMinimumRotationLimitAttrOperator(
    Float3CompoundBaseAttrOperator[ConstraintMinimumRotationLimitPlugOperator]
):
    __slots__ = ()

    constraintMinimumRotationLimitX = FloatField()
    constraintMinimumRotationLimitx = constraintMinimumRotationLimitX

    constraintMinimumRotationLimitY = FloatField()
    constraintMinimumRotationLimity = constraintMinimumRotationLimitY

    constraintMinimumRotationLimitZ = FloatField()
    constraintMinimumRotationLimitz = constraintMinimumRotationLimitZ


class ConstraintMinimumRotationLimitField(
    Float3CompoundBaseField[ConstraintMinimumRotationLimitAttrOperator, ConstraintMinimumRotationLimitPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintMinimumRotationLimitAttrOperator
    PLUG_CLS = ConstraintMinimumRotationLimitPlugOperator

    constraintMinimumRotationLimitX = FloatField()
    constraintMinimumRotationLimitx = constraintMinimumRotationLimitX

    constraintMinimumRotationLimitY = FloatField()
    constraintMinimumRotationLimity = constraintMinimumRotationLimitY

    constraintMinimumRotationLimitZ = FloatField()
    constraintMinimumRotationLimitz = constraintMinimumRotationLimitZ


class ConstraintMaximumRotationLimitPlugOperator(
    Float3CompoundBasePlugOperator["ConstraintMaximumRotationLimitAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintMaximumRotationLimitX", "constraintMaximumRotationLimitx"),
        ("constraintMaximumRotationLimitY", "constraintMaximumRotationLimity"),
        ("constraintMaximumRotationLimitZ", "constraintMaximumRotationLimitz"),
    )

    constraintMaximumRotationLimitX = FloatField()
    constraintMaximumRotationLimitx = constraintMaximumRotationLimitX

    constraintMaximumRotationLimitY = FloatField()
    constraintMaximumRotationLimity = constraintMaximumRotationLimitY

    constraintMaximumRotationLimitZ = FloatField()
    constraintMaximumRotationLimitz = constraintMaximumRotationLimitZ


class ConstraintMaximumRotationLimitAttrOperator(
    Float3CompoundBaseAttrOperator[ConstraintMaximumRotationLimitPlugOperator]
):
    __slots__ = ()

    constraintMaximumRotationLimitX = FloatField()
    constraintMaximumRotationLimitx = constraintMaximumRotationLimitX

    constraintMaximumRotationLimitY = FloatField()
    constraintMaximumRotationLimity = constraintMaximumRotationLimitY

    constraintMaximumRotationLimitZ = FloatField()
    constraintMaximumRotationLimitz = constraintMaximumRotationLimitZ


class ConstraintMaximumRotationLimitField(
    Float3CompoundBaseField[ConstraintMaximumRotationLimitAttrOperator, ConstraintMaximumRotationLimitPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintMaximumRotationLimitAttrOperator
    PLUG_CLS = ConstraintMaximumRotationLimitPlugOperator

    constraintMaximumRotationLimitX = FloatField()
    constraintMaximumRotationLimitx = constraintMaximumRotationLimitX

    constraintMaximumRotationLimitY = FloatField()
    constraintMaximumRotationLimity = constraintMaximumRotationLimitY

    constraintMaximumRotationLimitZ = FloatField()
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

    pointOffsetX = FloatField()
    pointOffsetx = pointOffsetX

    pointOffsetY = FloatField()
    pointOffsety = pointOffsetY

    pointOffsetZ = FloatField()
    pointOffsetz = pointOffsetZ


class PointOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[PointOffsetPlugOperator]
):
    __slots__ = ()

    pointOffsetX = FloatField()
    pointOffsetx = pointOffsetX

    pointOffsetY = FloatField()
    pointOffsety = pointOffsetY

    pointOffsetZ = FloatField()
    pointOffsetz = pointOffsetZ


class PointOffsetField(
    Float3CompoundBaseField[PointOffsetAttrOperator, PointOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointOffsetAttrOperator
    PLUG_CLS = PointOffsetPlugOperator

    pointOffsetX = FloatField()
    pointOffsetx = pointOffsetX

    pointOffsetY = FloatField()
    pointOffsety = pointOffsetY

    pointOffsetZ = FloatField()
    pointOffsetz = pointOffsetZ
