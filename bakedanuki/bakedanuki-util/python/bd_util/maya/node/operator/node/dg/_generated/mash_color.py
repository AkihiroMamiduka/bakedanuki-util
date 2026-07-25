# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_color import (
    BackgroundColorField,
    ColorField,
    MColourField,
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
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


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


class UvTileModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PASS_THROUGH = 1
    BY_ID = 2
    UNIQUE = 3


class UvTileModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PASS_THROUGH = 1
    BY_ID = 2
    UNIQUE = 3

    NAME_MAP = {
        PASS_THROUGH: "Pass Through",
        BY_ID: "By Id",
        UNIQUE: "Unique",
    }


class UvTileModeEnumField(
    EnumField[UvTileModeEnumAttrOperator, UvTileModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvTileModeEnumAttrOperator
    PLUG_CLS = UvTileModeEnumPlugOperator


class BlendModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 1
    ADD = 2
    SUBTRACT = 3
    MULTIPLY = 4
    SCREEN = 5
    OVERLAY = 6


class BlendModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 1
    ADD = 2
    SUBTRACT = 3
    MULTIPLY = 4
    SCREEN = 5
    OVERLAY = 6

    NAME_MAP = {
        NORMAL: "Normal",
        ADD: "Add",
        SUBTRACT: "Subtract",
        MULTIPLY: "Multiply",
        SCREEN: "Screen",
        OVERLAY: "Overlay",
    }


class BlendModeEnumField(
    EnumField[BlendModeEnumAttrOperator, BlendModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlendModeEnumAttrOperator
    PLUG_CLS = BlendModeEnumPlugOperator


class _GeneratedMASH_Color(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Color"

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

    time = TimeField(default_value=0.0)

    enable = BoolField(default_value=False)

    enableVelocity = BoolField(default_value=False)

    enableBackgroundColor = BoolField(default_value=False)

    randomSeed = LongField(default_value=1, min_value=1, soft_max_value=100)

    uvTileMode = UvTileModeEnumField(default_value=1)

    blendMode = BlendModeEnumField(default_value=1)

    color = ColorField(default_value=(1.0, 1.0, 1.0))
    colorR = color.colorR
    colorr = colorR
    colorG = color.colorG
    colorg = colorG
    colorB = color.colorB
    colorb = colorB

    uvMatrix = MatrixField()

    backgroundColor = BackgroundColorField(default_value=(0.0, 0.0, 0.0))
    backgroundColorR = backgroundColor.backgroundColorR
    backgroundColorr = backgroundColorR
    backgroundColorG = backgroundColor.backgroundColorG
    backgroundColorg = backgroundColorG
    backgroundColorB = backgroundColor.backgroundColorB
    backgroundColorb = backgroundColorB

    hueRandom = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    saturationRandom = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    valueRandom = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    enableMaxTiles = BoolField(default_value=False)

    randomUVTile = BoolField(default_value=False)

    maxTiles = LongField(default_value=4, min_value=1, soft_max_value=10)

    colorSetName = DataStringField()
