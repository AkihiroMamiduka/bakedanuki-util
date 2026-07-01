# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_channel_random import (
    MColourField,
    StartVectorField,
    VarianceVectorMaxField,
    VarianceVectorMinField,
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


class DynamicsChannelNameEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONSTRAINT = 0
    ACTIVE = 1
    BOUNCE = 2
    DAMPING = 3
    DAMPING_ROTATION = 4
    FRICTION = 5
    FRICTION_ROLLING = 6
    INITIAL_VELOCITY = 9
    INITIAL_VELOCITY_ROTATION = 10
    MASS = 11
    MAXIMUM_VELOCITY = 12
    MAXIMUM_VELOCITY_ROTATION = 13
    POSITION_STRENGTH = 14
    ROTATION_STRENGTH = 15


class DynamicsChannelNameEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONSTRAINT = 0
    ACTIVE = 1
    BOUNCE = 2
    DAMPING = 3
    DAMPING_ROTATION = 4
    FRICTION = 5
    FRICTION_ROLLING = 6
    INITIAL_VELOCITY = 9
    INITIAL_VELOCITY_ROTATION = 10
    MASS = 11
    MAXIMUM_VELOCITY = 12
    MAXIMUM_VELOCITY_ROTATION = 13
    POSITION_STRENGTH = 14
    ROTATION_STRENGTH = 15

    NAME_MAP = {
        CONSTRAINT: "Constraint",
        ACTIVE: "Active",
        BOUNCE: "Bounce",
        DAMPING: "Damping",
        DAMPING_ROTATION: "Damping (Rotation)",
        FRICTION: "Friction",
        FRICTION_ROLLING: "Friction (Rolling)",
        INITIAL_VELOCITY: "Initial Velocity",
        INITIAL_VELOCITY_ROTATION: "Initial Velocity (Rotation)",
        MASS: "Mass",
        MAXIMUM_VELOCITY: "Maximum Velocity",
        MAXIMUM_VELOCITY_ROTATION: "Maximum Velocity (Rotation)",
        POSITION_STRENGTH: "Position Strength",
        ROTATION_STRENGTH: "Rotation Strength",
    }


class DynamicsChannelNameEnumField(
    EnumField[DynamicsChannelNameEnumAttrOperator, DynamicsChannelNameEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DynamicsChannelNameEnumAttrOperator
    PLUG_CLS = DynamicsChannelNameEnumPlugOperator


class ConstraintChannelNameEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ENABLE = 1
    BREAKABLE = 2
    BREAKING_IMPULSE = 3
    CONTINIOUS_CREATION = 4
    MAXIMUM_LINEAR_FORCE = 5
    LINEAR_TARGET_SPEED = 6
    MAXIMUM_ANGULAR_FORCE = 7
    ANGULAR_TARGET_SPEED = 8
    SPRING_REST_LENGTH = 9
    SPRING_RANGE = 10
    SPRING_POSITION_STIFFNESS = 11
    SPRING_POSITION_DAMPING = 12
    SPRING_ROTATIONAL_STIFFNESS = 13
    SPRING_ROTATIONAL_DAMPING = 14
    MINIMUM_POSITION_LIMIT = 15
    MAXIMUM_POSITION_LIMIT = 16
    MINIMUM_ROTATION_LIMIT = 17
    MAXIMUM_ROTATION_LIMIT = 18


class ConstraintChannelNameEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ENABLE = 1
    BREAKABLE = 2
    BREAKING_IMPULSE = 3
    CONTINIOUS_CREATION = 4
    MAXIMUM_LINEAR_FORCE = 5
    LINEAR_TARGET_SPEED = 6
    MAXIMUM_ANGULAR_FORCE = 7
    ANGULAR_TARGET_SPEED = 8
    SPRING_REST_LENGTH = 9
    SPRING_RANGE = 10
    SPRING_POSITION_STIFFNESS = 11
    SPRING_POSITION_DAMPING = 12
    SPRING_ROTATIONAL_STIFFNESS = 13
    SPRING_ROTATIONAL_DAMPING = 14
    MINIMUM_POSITION_LIMIT = 15
    MAXIMUM_POSITION_LIMIT = 16
    MINIMUM_ROTATION_LIMIT = 17
    MAXIMUM_ROTATION_LIMIT = 18

    NAME_MAP = {
        ENABLE: "Enable",
        BREAKABLE: "Breakable",
        BREAKING_IMPULSE: "Breaking Impulse",
        CONTINIOUS_CREATION: "Continious Creation",
        MAXIMUM_LINEAR_FORCE: "Maximum Linear Force",
        LINEAR_TARGET_SPEED: "Linear Target Speed",
        MAXIMUM_ANGULAR_FORCE: "Maximum Angular Force",
        ANGULAR_TARGET_SPEED: "Angular Target Speed",
        SPRING_REST_LENGTH: "Spring Rest Length",
        SPRING_RANGE: "Spring Range",
        SPRING_POSITION_STIFFNESS: "Spring Position Stiffness",
        SPRING_POSITION_DAMPING: "Spring Position Damping",
        SPRING_ROTATIONAL_STIFFNESS: "Spring Rotational Stiffness",
        SPRING_ROTATIONAL_DAMPING: "Spring Rotational Damping",
        MINIMUM_POSITION_LIMIT: "Minimum Position Limit",
        MAXIMUM_POSITION_LIMIT: "Maximum Position Limit",
        MINIMUM_ROTATION_LIMIT: "Minimum Rotation Limit",
        MAXIMUM_ROTATION_LIMIT: "Maximum Rotation Limit",
    }


class ConstraintChannelNameEnumField(
    EnumField[ConstraintChannelNameEnumAttrOperator, ConstraintChannelNameEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintChannelNameEnumAttrOperator
    PLUG_CLS = ConstraintChannelNameEnumPlugOperator


class MASH_ChannelRandom(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_ChannelRandom"

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

    enable = BoolField()

    startValue = FloatField()

    startVector = StartVectorField()
    startVector0 = startVector.startVector0
    startVector1 = startVector.startVector1
    startVector2 = startVector.startVector2

    varianceVectorMin = VarianceVectorMinField()
    varianceVectorMin0 = varianceVectorMin.varianceVectorMin0
    varianceVectorMin1 = varianceVectorMin.varianceVectorMin1
    varianceVectorMin2 = varianceVectorMin.varianceVectorMin2

    varianceMin = FloatField()

    varianceVectorMax = VarianceVectorMaxField()
    varianceVectorMax0 = varianceVectorMax.varianceVectorMax0
    varianceVectorMax1 = varianceVectorMax.varianceVectorMax1
    varianceVectorMax2 = varianceVectorMax.varianceVectorMax2

    varianceMax = FloatField()

    randomSeed = LongField()

    dynamicsChannelName = DynamicsChannelNameEnumField()

    constraintChannelName = ConstraintChannelNameEnumField()
