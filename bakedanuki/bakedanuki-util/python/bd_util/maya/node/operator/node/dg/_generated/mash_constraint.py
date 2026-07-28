# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_constraint import (
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
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


class MapDirectionEnumPlugOperator(
    EnumPlugOperator["MapDirectionEnumAttrOperator"]
):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class MapDirectionEnumAttrOperator(
    EnumAttrOperator[MapDirectionEnumPlugOperator]
):
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


class TransformationSpaceEnumPlugOperator(
    EnumPlugOperator["TransformationSpaceEnumAttrOperator"]
):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2


class TransformationSpaceEnumAttrOperator(
    EnumAttrOperator[TransformationSpaceEnumPlugOperator]
):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2

    NAME_MAP = {
        WORLD: "World",
        LOCAL: "Local",
    }


class TransformationSpaceEnumField(
    EnumField[
        TransformationSpaceEnumAttrOperator,
        TransformationSpaceEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = TransformationSpaceEnumAttrOperator
    PLUG_CLS = TransformationSpaceEnumPlugOperator


class ConnectionMapDirectionEnumPlugOperator(
    EnumPlugOperator["ConnectionMapDirectionEnumAttrOperator"]
):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class ConnectionMapDirectionEnumAttrOperator(
    EnumAttrOperator[ConnectionMapDirectionEnumPlugOperator]
):
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
    EnumField[
        ConnectionMapDirectionEnumAttrOperator,
        ConnectionMapDirectionEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ConnectionMapDirectionEnumAttrOperator
    PLUG_CLS = ConnectionMapDirectionEnumPlugOperator


class ConstraintLimitPositionXEnumPlugOperator(
    EnumPlugOperator["ConstraintLimitPositionXEnumAttrOperator"]
):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3


class ConstraintLimitPositionXEnumAttrOperator(
    EnumAttrOperator[ConstraintLimitPositionXEnumPlugOperator]
):
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
    EnumField[
        ConstraintLimitPositionXEnumAttrOperator,
        ConstraintLimitPositionXEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintLimitPositionXEnumAttrOperator
    PLUG_CLS = ConstraintLimitPositionXEnumPlugOperator


class ConstraintLimitPositionYEnumPlugOperator(
    EnumPlugOperator["ConstraintLimitPositionYEnumAttrOperator"]
):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3


class ConstraintLimitPositionYEnumAttrOperator(
    EnumAttrOperator[ConstraintLimitPositionYEnumPlugOperator]
):
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
    EnumField[
        ConstraintLimitPositionYEnumAttrOperator,
        ConstraintLimitPositionYEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintLimitPositionYEnumAttrOperator
    PLUG_CLS = ConstraintLimitPositionYEnumPlugOperator


class ConstraintLimitPositionZEnumPlugOperator(
    EnumPlugOperator["ConstraintLimitPositionZEnumAttrOperator"]
):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3


class ConstraintLimitPositionZEnumAttrOperator(
    EnumAttrOperator[ConstraintLimitPositionZEnumPlugOperator]
):
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
    EnumField[
        ConstraintLimitPositionZEnumAttrOperator,
        ConstraintLimitPositionZEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintLimitPositionZEnumAttrOperator
    PLUG_CLS = ConstraintLimitPositionZEnumPlugOperator


class ConstraintLimitRotationXEnumPlugOperator(
    EnumPlugOperator["ConstraintLimitRotationXEnumAttrOperator"]
):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3


class ConstraintLimitRotationXEnumAttrOperator(
    EnumAttrOperator[ConstraintLimitRotationXEnumPlugOperator]
):
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
    EnumField[
        ConstraintLimitRotationXEnumAttrOperator,
        ConstraintLimitRotationXEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintLimitRotationXEnumAttrOperator
    PLUG_CLS = ConstraintLimitRotationXEnumPlugOperator


class ConstraintLimitRotationYEnumPlugOperator(
    EnumPlugOperator["ConstraintLimitRotationYEnumAttrOperator"]
):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3


class ConstraintLimitRotationYEnumAttrOperator(
    EnumAttrOperator[ConstraintLimitRotationYEnumPlugOperator]
):
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
    EnumField[
        ConstraintLimitRotationYEnumAttrOperator,
        ConstraintLimitRotationYEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintLimitRotationYEnumAttrOperator
    PLUG_CLS = ConstraintLimitRotationYEnumPlugOperator


class ConstraintLimitRotationZEnumPlugOperator(
    EnumPlugOperator["ConstraintLimitRotationZEnumAttrOperator"]
):
    __slots__ = ()

    FREE = 1
    FIXED = 2
    LIMITED = 3


class ConstraintLimitRotationZEnumAttrOperator(
    EnumAttrOperator[ConstraintLimitRotationZEnumPlugOperator]
):
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
    EnumField[
        ConstraintLimitRotationZEnumAttrOperator,
        ConstraintLimitRotationZEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintLimitRotationZEnumAttrOperator
    PLUG_CLS = ConstraintLimitRotationZEnumPlugOperator


class ConstraintTypeEnumPlugOperator(
    EnumPlugOperator["ConstraintTypeEnumAttrOperator"]
):
    __slots__ = ()

    GLUE = 1
    SPRING = 2
    SLIDER = 3
    CUSTOM = 10


class ConstraintTypeEnumAttrOperator(
    EnumAttrOperator[ConstraintTypeEnumPlugOperator]
):
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


class ConstraintModeEnumPlugOperator(
    EnumPlugOperator["ConstraintModeEnumAttrOperator"]
):
    __slots__ = ()

    CONNECT_TOUCHING = 1
    CONNECT_NEAREST = 2
    CONNECT_TO_POINT = 3
    CONNECT_TO_OFFSET_POINT = 4
    CONNECT_TO_INPUT_POINTS = 5


class ConstraintModeEnumAttrOperator(
    EnumAttrOperator[ConstraintModeEnumPlugOperator]
):
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


class GeneratedMASH_Constraint(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Constraint"

    savedData = TypedField()

    mColour = MColourField(default_value=(1.0, 1.0, 1.0))
    mc = mColour
    mColourR = mColour.mColourR
    mcr = mColourR
    mColourG = mColour.mColourG
    mcg = mColourG
    mColourB = mColour.mColourB
    mcb = mColourB

    inMapMatrix = MatrixField()

    mapDirection = MapDirectionEnumField(default_value=2)

    Envelope = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )

    randEnvelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    StepEnvelope = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)

    mFalloffInfo = TypedField(multi=True)

    enableStrengthX = BoolField(default_value=True)

    enableStrengthY = BoolField(default_value=True)

    enableStrengthZ = BoolField(default_value=True)

    stringOn = DataStringField()

    stringOff = DataStringField()

    strengthPP = TypedField(multi=True)

    transformationSpace = TransformationSpaceEnumField(default_value=1)

    outputPoints = TypedField(writable=False)

    inputPoints = TypedField()

    connectionColour = ConnectionColourField(default_value=(1.0, 1.0, 1.0))
    connectionColorRed = connectionColour.connectionColorRed
    connectionColorGreen = connectionColour.connectionColorGreen
    connectionColorBlue = connectionColour.connectionColorBlue

    connectionMapMatrix = MatrixField()

    connectionMapDirection = ConnectionMapDirectionEnumField(default_value=2)

    connectionColorThreshold = FloatField(
        default_value=0.10000000149011612, min_value=0.0, max_value=1.0
    )

    dynamicsPP = TypedField(multi=True)

    constraintEnable = BoolField(default_value=True)

    continuousCreation = BoolField(default_value=True)

    constraintBreakable = BoolField(default_value=False)

    constraintMaxCount = LongField(default_value=5)

    constraintDistance = FloatField(
        default_value=5.0, min_value=0.0, soft_max_value=10.0
    )

    constraintThreshold = FloatField(
        default_value=2.0, min_value=0.0, soft_max_value=10.0
    )

    constrainSpringPositiontStiffness = FloatField(
        default_value=20.0, min_value=0.0, soft_max_value=200.0
    )

    constraintSpringPositionDamping = FloatField(
        default_value=0.009999999776482582, min_value=0.0, soft_max_value=200.0
    )

    constrainSpringAngularStiffness = FloatField(
        default_value=20.0, min_value=0.0, soft_max_value=100.0
    )

    constraintSpringAngularDamping = FloatField(
        default_value=0.009999999776482582, min_value=0.0, soft_max_value=100.0
    )

    springRestLength = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=10.0
    )

    springRange = FloatField(
        default_value=2.0, soft_min_value=0.0, soft_max_value=10.0
    )

    linearSpringEnabledX = BoolField(default_value=False)

    linearSpringEnabledY = BoolField(default_value=True)

    linearSpringEnabledZ = BoolField(default_value=False)

    angularSpringEnabledX = BoolField(default_value=True)

    angularSpringEnabledY = BoolField(default_value=False)

    angularSpringEnabledZ = BoolField(default_value=True)

    linearMotorEnabled = BoolField(default_value=False)

    linearMotorTargetSpeed = LinearMotorTargetSpeedField(
        default_value=(0.0, 0.0, 0.0)
    )
    linearMotorTargetSpeedX = linearMotorTargetSpeed.linearMotorTargetSpeedX
    linearMotorTargetSpeedx = linearMotorTargetSpeedX
    linearMotorTargetSpeedY = linearMotorTargetSpeed.linearMotorTargetSpeedY
    linearMotorTargetSpeedy = linearMotorTargetSpeedY
    linearMotorTargetSpeedZ = linearMotorTargetSpeed.linearMotorTargetSpeedZ
    linearMotorTargetSpeedz = linearMotorTargetSpeedZ

    linearMotorMaxForce = LinearMotorMaxForceField(
        default_value=(10.0, 10.0, 10.0)
    )
    linearMotorMaxForceX = linearMotorMaxForce.linearMotorMaxForceX
    linearMotorMaxForcex = linearMotorMaxForceX
    linearMotorMaxForceY = linearMotorMaxForce.linearMotorMaxForceY
    linearMotorMaxForcey = linearMotorMaxForceY
    linearMotorMaxForceZ = linearMotorMaxForce.linearMotorMaxForceZ
    linearMotorMaxForcez = linearMotorMaxForceZ

    angularMotorEnabled = BoolField(default_value=False)

    angularMotorTargetSpeed = AngularMotorTargetSpeedField(
        default_value=(0.0, 0.0, 0.0)
    )
    angularMotorTargetSpeedX = angularMotorTargetSpeed.angularMotorTargetSpeedX
    angularMotorTargetSpeedx = angularMotorTargetSpeedX
    angularMotorTargetSpeedY = angularMotorTargetSpeed.angularMotorTargetSpeedY
    angularMotorTargetSpeedy = angularMotorTargetSpeedY
    angularMotorTargetSpeedZ = angularMotorTargetSpeed.angularMotorTargetSpeedZ
    angularMotorTargetSpeedz = angularMotorTargetSpeedZ

    angularMotorMaxForce = AngularMotorMaxForceField(
        default_value=(10.0, 10.0, 10.0)
    )
    angularMotorMaxForceX = angularMotorMaxForce.angularMotorMaxForceX
    angularMotorMaxForcex = angularMotorMaxForceX
    angularMotorMaxForceY = angularMotorMaxForce.angularMotorMaxForceY
    angularMotorMaxForcey = angularMotorMaxForceY
    angularMotorMaxForceZ = angularMotorMaxForce.angularMotorMaxForceZ
    angularMotorMaxForcez = angularMotorMaxForceZ

    constraintMinimumPositionLimit = ConstraintMinimumPositionLimitField(
        default_value=(0.0, 0.0, 0.0)
    )
    constraintMinimumPositionLimitX = (
        constraintMinimumPositionLimit.constraintMinimumPositionLimitX
    )
    constraintMinimumPositionLimitx = constraintMinimumPositionLimitX
    constraintMinimumPositionLimitY = (
        constraintMinimumPositionLimit.constraintMinimumPositionLimitY
    )
    constraintMinimumPositionLimity = constraintMinimumPositionLimitY
    constraintMinimumPositionLimitZ = (
        constraintMinimumPositionLimit.constraintMinimumPositionLimitZ
    )
    constraintMinimumPositionLimitz = constraintMinimumPositionLimitZ

    constraintMaximumPositionLimit = ConstraintMaximumPositionLimitField(
        default_value=(0.0, 0.0, 0.0)
    )
    constraintMaximumPositionLimitX = (
        constraintMaximumPositionLimit.constraintMaximumPositionLimitX
    )
    constraintMaximumPositionLimitx = constraintMaximumPositionLimitX
    constraintMaximumPositionLimitY = (
        constraintMaximumPositionLimit.constraintMaximumPositionLimitY
    )
    constraintMaximumPositionLimity = constraintMaximumPositionLimitY
    constraintMaximumPositionLimitZ = (
        constraintMaximumPositionLimit.constraintMaximumPositionLimitZ
    )
    constraintMaximumPositionLimitz = constraintMaximumPositionLimitZ

    constraintMinimumRotationLimit = ConstraintMinimumRotationLimitField(
        default_value=(0.0, 0.0, 0.0)
    )
    constraintMinimumRotationLimitX = (
        constraintMinimumRotationLimit.constraintMinimumRotationLimitX
    )
    constraintMinimumRotationLimitx = constraintMinimumRotationLimitX
    constraintMinimumRotationLimitY = (
        constraintMinimumRotationLimit.constraintMinimumRotationLimitY
    )
    constraintMinimumRotationLimity = constraintMinimumRotationLimitY
    constraintMinimumRotationLimitZ = (
        constraintMinimumRotationLimit.constraintMinimumRotationLimitZ
    )
    constraintMinimumRotationLimitz = constraintMinimumRotationLimitZ

    constraintMaximumRotationLimit = ConstraintMaximumRotationLimitField(
        default_value=(0.0, 0.0, 0.0)
    )
    constraintMaximumRotationLimitX = (
        constraintMaximumRotationLimit.constraintMaximumRotationLimitX
    )
    constraintMaximumRotationLimitx = constraintMaximumRotationLimitX
    constraintMaximumRotationLimitY = (
        constraintMaximumRotationLimit.constraintMaximumRotationLimitY
    )
    constraintMaximumRotationLimity = constraintMaximumRotationLimitY
    constraintMaximumRotationLimitZ = (
        constraintMaximumRotationLimit.constraintMaximumRotationLimitZ
    )
    constraintMaximumRotationLimitz = constraintMaximumRotationLimitZ

    constraintLimitPositionX = ConstraintLimitPositionXEnumField(
        default_value=2
    )

    constraintLimitPositionY = ConstraintLimitPositionYEnumField(
        default_value=2
    )

    constraintLimitPositionZ = ConstraintLimitPositionZEnumField(
        default_value=2
    )

    constraintLimitRotationX = ConstraintLimitRotationXEnumField(
        default_value=1
    )

    constraintLimitRotationY = ConstraintLimitRotationYEnumField(
        default_value=1
    )

    constraintLimitRotationZ = ConstraintLimitRotationZEnumField(
        default_value=1
    )

    constraintType = ConstraintTypeEnumField(default_value=1)

    constraintMode = ConstraintModeEnumField(default_value=2)

    constraintConnectionPoint = MatrixField()

    pointOffset = PointOffsetField(default_value=(0.0, 0.0, 0.0))
    pointOffsetX = pointOffset.pointOffsetX
    pointOffsetx = pointOffsetX
    pointOffsetY = pointOffset.pointOffsetY
    pointOffsety = pointOffsetY
    pointOffsetZ = pointOffset.pointOffsetZ
    pointOffsetz = pointOffsetZ

    offsetPointsNetwork = TypedField()
