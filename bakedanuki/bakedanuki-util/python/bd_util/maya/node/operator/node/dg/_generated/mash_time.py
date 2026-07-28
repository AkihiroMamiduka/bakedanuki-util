# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_time import MColourField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
from ....attr.define.std.dt.string import DataStringField


class MapDirectionEnumPlugOperator(EnumPlugOperator["MapDirectionEnumAttrOperator"]):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class MapDirectionEnumAttrOperator(EnumAttrOperator[MapDirectionEnumPlugOperator]):
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


class TransformationSpaceEnumPlugOperator(EnumPlugOperator["TransformationSpaceEnumAttrOperator"]):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2


class TransformationSpaceEnumAttrOperator(EnumAttrOperator[TransformationSpaceEnumPlugOperator]):
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


class StrengthModeEnumPlugOperator(EnumPlugOperator["StrengthModeEnumAttrOperator"]):
    __slots__ = ()

    NONE = 1
    ANIMATION_FRAME = 2
    ANIMATION_TRIGGER = 3


class StrengthModeEnumAttrOperator(EnumAttrOperator[StrengthModeEnumPlugOperator]):
    __slots__ = ()

    NONE = 1
    ANIMATION_FRAME = 2
    ANIMATION_TRIGGER = 3

    NAME_MAP = {
        NONE: "None",
        ANIMATION_FRAME: "Animation Frame",
        ANIMATION_TRIGGER: "Animation Trigger",
    }


class StrengthModeEnumField(
    EnumField[StrengthModeEnumAttrOperator, StrengthModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StrengthModeEnumAttrOperator
    PLUG_CLS = StrengthModeEnumPlugOperator


class GeneratedMASH_Time(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Time"

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

    Envelope = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)

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

    inFrames = DataDoubleArrayField()

    time = TimeField(default_value=0.0)

    enable = BoolField(default_value=False)

    enableVelocity = BoolField(default_value=False)

    limitLoops = BoolField(default_value=False)

    randomStagger = BoolField(default_value=False)

    simulateTime = BoolField(default_value=False)

    roundTime = BoolField(default_value=False)

    randomSeed = LongField(default_value=1, min_value=1, soft_max_value=100)

    timeOffset = LongField(default_value=0)

    animationStart = LongField(default_value=0, soft_min_value=0, soft_max_value=100)

    animationEnd = LongField(default_value=25, soft_min_value=1, soft_max_value=100)

    staggerFrames = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)

    timeScale = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=3.0)

    timeScaleRandom = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=3.0)

    numberOfLoops = LongField(default_value=3, min_value=1, soft_max_value=10)

    simStartFrame = LongField(default_value=0)

    strengthMode = StrengthModeEnumField(default_value=1)
