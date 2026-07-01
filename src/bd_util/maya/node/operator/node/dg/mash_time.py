# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_time import MColourField
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
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.double_array import DataDoubleArrayField
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


class StrengthModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 1
    ANIMATION_FRAME = 2
    ANIMATION_TRIGGER = 3


class StrengthModeEnumAttrOperator(EnumAttrOperator):
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


class MASH_Time(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Time"

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

    inFrames = DataDoubleArrayField()

    time = TimeField()

    enable = BoolField()

    enableVelocity = BoolField()

    limitLoops = BoolField()

    randomStagger = BoolField()

    simulateTime = BoolField()

    roundTime = BoolField()

    randomSeed = LongField()

    timeOffset = LongField()

    animationStart = LongField()

    animationEnd = LongField()

    staggerFrames = FloatField()

    timeScale = FloatField()

    timeScaleRandom = FloatField()

    numberOfLoops = LongField()

    simStartFrame = LongField()

    strengthMode = StrengthModeEnumField()
