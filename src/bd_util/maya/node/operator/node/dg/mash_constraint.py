# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_constraint import (
    AngularMotorMaxForceField,
    AngularMotorTargetSpeedField,
    ConnectionColourField,
    ConstraintMaximumPositionLimitField,
    ConstraintMaximumRotationLimitField,
    ConstraintMinimumPositionLimitField,
    ConstraintMinimumRotationLimitField,
    LinearMotorMaxForceField,
    LinearMotorTargetSpeedField,
    MColourField,
    PointOffsetField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField


class MapDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class MapDirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4

    NAME_MAP = {
        UV: "UV",
        Y: "Y",
        X: "X",
        Z: "Z",
    }


class MapDirectionEnumField(
    EnumField[MapDirectionEnumAttrOperator, MapDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MapDirectionEnumAttrOperator
    PLUG_CLS = MapDirectionEnumPlugOperator


class TransformationSpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2


class TransformationSpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2

    NAME_MAP = {
        WORLD: "World",
        LOCAL: "Local",
    }


class TransformationSpaceEnumField(
    EnumField[TransformationSpaceEnumAttrOperator, TransformationSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransformationSpaceEnumAttrOperator
    PLUG_CLS = TransformationSpaceEnumPlugOperator


class ConnectionMapDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class ConnectionMapDirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4

    NAME_MAP = {
        UV: "UV",
        Y: "Y",
        X: "X",
        Z: "Z",
    }


class ConnectionMapDirectionEnumField(
    EnumField[ConnectionMapDirectionEnumAttrOperator, ConnectionMapDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConnectionMapDirectionEnumAttrOperator
    PLUG_CLS = ConnectionMapDirectionEnumPlugOperator


class ConstraintLimitPositionXEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3


class ConstraintLimitPositionXEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3

    NAME_MAP = {
        FREE: "Free",
        FIXED: "Fixed",
        LIMITED: "Limited",
    }


class ConstraintLimitPositionXEnumField(
    EnumField[ConstraintLimitPositionXEnumAttrOperator, ConstraintLimitPositionXEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintLimitPositionXEnumAttrOperator
    PLUG_CLS = ConstraintLimitPositionXEnumPlugOperator


class ConstraintLimitPositionYEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3


class ConstraintLimitPositionYEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3

    NAME_MAP = {
        FREE: "Free",
        FIXED: "Fixed",
        LIMITED: "Limited",
    }


class ConstraintLimitPositionYEnumField(
    EnumField[ConstraintLimitPositionYEnumAttrOperator, ConstraintLimitPositionYEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintLimitPositionYEnumAttrOperator
    PLUG_CLS = ConstraintLimitPositionYEnumPlugOperator


class ConstraintLimitPositionZEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3


class ConstraintLimitPositionZEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3

    NAME_MAP = {
        FREE: "Free",
        FIXED: "Fixed",
        LIMITED: "Limited",
    }


class ConstraintLimitPositionZEnumField(
    EnumField[ConstraintLimitPositionZEnumAttrOperator, ConstraintLimitPositionZEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintLimitPositionZEnumAttrOperator
    PLUG_CLS = ConstraintLimitPositionZEnumPlugOperator


class ConstraintLimitRotationXEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3


class ConstraintLimitRotationXEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3

    NAME_MAP = {
        FREE: "Free",
        FIXED: "Fixed",
        LIMITED: "Limited",
    }


class ConstraintLimitRotationXEnumField(
    EnumField[ConstraintLimitRotationXEnumAttrOperator, ConstraintLimitRotationXEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintLimitRotationXEnumAttrOperator
    PLUG_CLS = ConstraintLimitRotationXEnumPlugOperator


class ConstraintLimitRotationYEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3


class ConstraintLimitRotationYEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3

    NAME_MAP = {
        FREE: "Free",
        FIXED: "Fixed",
        LIMITED: "Limited",
    }


class ConstraintLimitRotationYEnumField(
    EnumField[ConstraintLimitRotationYEnumAttrOperator, ConstraintLimitRotationYEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintLimitRotationYEnumAttrOperator
    PLUG_CLS = ConstraintLimitRotationYEnumPlugOperator


class ConstraintLimitRotationZEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3


class ConstraintLimitRotationZEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3

    NAME_MAP = {
        FREE: "Free",
        FIXED: "Fixed",
        LIMITED: "Limited",
    }


class ConstraintLimitRotationZEnumField(
    EnumField[ConstraintLimitRotationZEnumAttrOperator, ConstraintLimitRotationZEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintLimitRotationZEnumAttrOperator
    PLUG_CLS = ConstraintLimitRotationZEnumPlugOperator


class ConstraintTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    GLUE = 1
    SPRING = 2
    SLIDER = 3
    CUSTOM = 10


class ConstraintTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    GLUE = 1
    SPRING = 2
    SLIDER = 3
    CUSTOM = 10

    NAME_MAP = {
        GLUE: "Glue",
        SPRING: "Spring",
        SLIDER: "Slider",
        CUSTOM: "Custom...",
    }


class ConstraintTypeEnumField(
    EnumField[ConstraintTypeEnumAttrOperator, ConstraintTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintTypeEnumAttrOperator
    PLUG_CLS = ConstraintTypeEnumPlugOperator


class ConstraintModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONNECT_TOUCHING = 1
    CONNECT_NEAREST = 2
    CONNECT_TO_POINT = 3
    CONNECT_TO_OFFSET_POINT = 4
    CONNECT_TO_INPUT_POINTS = 5


class ConstraintModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONNECT_TOUCHING = 1
    CONNECT_NEAREST = 2
    CONNECT_TO_POINT = 3
    CONNECT_TO_OFFSET_POINT = 4
    CONNECT_TO_INPUT_POINTS = 5

    NAME_MAP = {
        CONNECT_TOUCHING: "Connect Touching",
        CONNECT_NEAREST: "Connect Nearest",
        CONNECT_TO_POINT: "Connect To Point",
        CONNECT_TO_OFFSET_POINT: "Connect To Offset Point",
        CONNECT_TO_INPUT_POINTS: "Connect To Input Points",
    }


class ConstraintModeEnumField(
    EnumField[ConstraintModeEnumAttrOperator, ConstraintModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintModeEnumAttrOperator
    PLUG_CLS = ConstraintModeEnumPlugOperator


class MASH_Constraint(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Constraint"

    savedData = TypedField()

    mColour = MColourField()
    mc = mColour
    mColourR = mColour.mColourR
    mcr = mColourR
    mColourG = mColour.mColourG
    mcg = mColourG
    mColourB = mColour.mColourB
    mcb = mColourB

    inMapMatrix = MatrixField()

    mapDirection = MapDirectionEnumField()

    Envelope = FloatField()

    randEnvelope = FloatField()

    StepEnvelope = FloatField()

    mFalloffInfo = TypedField(multi=True)

    enableStrengthX = BoolField()

    enableStrengthY = BoolField()

    enableStrengthZ = BoolField()

    stringOn = DataStringField()

    stringOff = DataStringField()

    strengthPP = TypedField(multi=True)

    transformationSpace = TransformationSpaceEnumField()

    outputPoints = TypedField()

    inputPoints = TypedField()

    connectionColour = ConnectionColourField()
    connectionColorRed = connectionColour.connectionColorRed
    connectionColorGreen = connectionColour.connectionColorGreen
    connectionColorBlue = connectionColour.connectionColorBlue

    connectionMapMatrix = MatrixField()

    connectionMapDirection = ConnectionMapDirectionEnumField()

    connectionColorThreshold = FloatField()

    dynamicsPP = TypedField(multi=True)

    constraintEnable = BoolField()

    continuousCreation = BoolField()

    constraintBreakable = BoolField()

    constraintMaxCount = LongField()

    constraintDistance = FloatField()

    constraintThreshold = FloatField()

    constrainSpringPositiontStiffness = FloatField()

    constraintSpringPositionDamping = FloatField()

    constrainSpringAngularStiffness = FloatField()

    constraintSpringAngularDamping = FloatField()

    springRestLength = FloatField()

    springRange = FloatField()

    linearSpringEnabledX = BoolField()

    linearSpringEnabledY = BoolField()

    linearSpringEnabledZ = BoolField()

    angularSpringEnabledX = BoolField()

    angularSpringEnabledY = BoolField()

    angularSpringEnabledZ = BoolField()

    linearMotorEnabled = BoolField()

    linearMotorTargetSpeed = LinearMotorTargetSpeedField()
    linearMotorTargetSpeedX = linearMotorTargetSpeed.linearMotorTargetSpeedX
    linearMotorTargetSpeedx = linearMotorTargetSpeedX
    linearMotorTargetSpeedY = linearMotorTargetSpeed.linearMotorTargetSpeedY
    linearMotorTargetSpeedy = linearMotorTargetSpeedY
    linearMotorTargetSpeedZ = linearMotorTargetSpeed.linearMotorTargetSpeedZ
    linearMotorTargetSpeedz = linearMotorTargetSpeedZ

    linearMotorMaxForce = LinearMotorMaxForceField()
    linearMotorMaxForceX = linearMotorMaxForce.linearMotorMaxForceX
    linearMotorMaxForcex = linearMotorMaxForceX
    linearMotorMaxForceY = linearMotorMaxForce.linearMotorMaxForceY
    linearMotorMaxForcey = linearMotorMaxForceY
    linearMotorMaxForceZ = linearMotorMaxForce.linearMotorMaxForceZ
    linearMotorMaxForcez = linearMotorMaxForceZ

    angularMotorEnabled = BoolField()

    angularMotorTargetSpeed = AngularMotorTargetSpeedField()
    angularMotorTargetSpeedX = angularMotorTargetSpeed.angularMotorTargetSpeedX
    angularMotorTargetSpeedx = angularMotorTargetSpeedX
    angularMotorTargetSpeedY = angularMotorTargetSpeed.angularMotorTargetSpeedY
    angularMotorTargetSpeedy = angularMotorTargetSpeedY
    angularMotorTargetSpeedZ = angularMotorTargetSpeed.angularMotorTargetSpeedZ
    angularMotorTargetSpeedz = angularMotorTargetSpeedZ

    angularMotorMaxForce = AngularMotorMaxForceField()
    angularMotorMaxForceX = angularMotorMaxForce.angularMotorMaxForceX
    angularMotorMaxForcex = angularMotorMaxForceX
    angularMotorMaxForceY = angularMotorMaxForce.angularMotorMaxForceY
    angularMotorMaxForcey = angularMotorMaxForceY
    angularMotorMaxForceZ = angularMotorMaxForce.angularMotorMaxForceZ
    angularMotorMaxForcez = angularMotorMaxForceZ

    constraintMinimumPositionLimit = ConstraintMinimumPositionLimitField()
    constraintMinimumPositionLimitX = constraintMinimumPositionLimit.constraintMinimumPositionLimitX
    constraintMinimumPositionLimitx = constraintMinimumPositionLimitX
    constraintMinimumPositionLimitY = constraintMinimumPositionLimit.constraintMinimumPositionLimitY
    constraintMinimumPositionLimity = constraintMinimumPositionLimitY
    constraintMinimumPositionLimitZ = constraintMinimumPositionLimit.constraintMinimumPositionLimitZ
    constraintMinimumPositionLimitz = constraintMinimumPositionLimitZ

    constraintMaximumPositionLimit = ConstraintMaximumPositionLimitField()
    constraintMaximumPositionLimitX = constraintMaximumPositionLimit.constraintMaximumPositionLimitX
    constraintMaximumPositionLimitx = constraintMaximumPositionLimitX
    constraintMaximumPositionLimitY = constraintMaximumPositionLimit.constraintMaximumPositionLimitY
    constraintMaximumPositionLimity = constraintMaximumPositionLimitY
    constraintMaximumPositionLimitZ = constraintMaximumPositionLimit.constraintMaximumPositionLimitZ
    constraintMaximumPositionLimitz = constraintMaximumPositionLimitZ

    constraintMinimumRotationLimit = ConstraintMinimumRotationLimitField()
    constraintMinimumRotationLimitX = constraintMinimumRotationLimit.constraintMinimumRotationLimitX
    constraintMinimumRotationLimitx = constraintMinimumRotationLimitX
    constraintMinimumRotationLimitY = constraintMinimumRotationLimit.constraintMinimumRotationLimitY
    constraintMinimumRotationLimity = constraintMinimumRotationLimitY
    constraintMinimumRotationLimitZ = constraintMinimumRotationLimit.constraintMinimumRotationLimitZ
    constraintMinimumRotationLimitz = constraintMinimumRotationLimitZ

    constraintMaximumRotationLimit = ConstraintMaximumRotationLimitField()
    constraintMaximumRotationLimitX = constraintMaximumRotationLimit.constraintMaximumRotationLimitX
    constraintMaximumRotationLimitx = constraintMaximumRotationLimitX
    constraintMaximumRotationLimitY = constraintMaximumRotationLimit.constraintMaximumRotationLimitY
    constraintMaximumRotationLimity = constraintMaximumRotationLimitY
    constraintMaximumRotationLimitZ = constraintMaximumRotationLimit.constraintMaximumRotationLimitZ
    constraintMaximumRotationLimitz = constraintMaximumRotationLimitZ

    constraintLimitPositionX = ConstraintLimitPositionXEnumField()

    constraintLimitPositionY = ConstraintLimitPositionYEnumField()

    constraintLimitPositionZ = ConstraintLimitPositionZEnumField()

    constraintLimitRotationX = ConstraintLimitRotationXEnumField()

    constraintLimitRotationY = ConstraintLimitRotationYEnumField()

    constraintLimitRotationZ = ConstraintLimitRotationZEnumField()

    constraintType = ConstraintTypeEnumField()

    constraintMode = ConstraintModeEnumField()

    constraintConnectionPoint = MatrixField()

    pointOffset = PointOffsetField()
    pointOffsetX = pointOffset.pointOffsetX
    pointOffsetx = pointOffsetX
    pointOffsetY = pointOffset.pointOffsetY
    pointOffsety = pointOffsetY
    pointOffsetZ = pointOffset.pointOffsetZ
    pointOffsetz = pointOffsetZ

    offsetPointsNetwork = TypedField()
