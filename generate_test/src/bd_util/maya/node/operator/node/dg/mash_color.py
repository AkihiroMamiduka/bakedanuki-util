# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_color import (
    BackgroundColorField,
    ColorField,
    MColourField,
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
from ...attr.define.std.at.unit_scalar.time import TimeField
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


class MASH_Color(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Color"

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

    time = TimeField()

    enable = BoolField()

    enableVelocity = BoolField()

    enableBackgroundColor = BoolField()

    randomSeed = LongField()

    uvTileMode = UvTileModeEnumField()

    blendMode = BlendModeEnumField()

    color = ColorField()
    colorR = color.colorR
    colorr = colorR
    colorG = color.colorG
    colorg = colorG
    colorB = color.colorB
    colorb = colorB

    uvMatrix = MatrixField()

    backgroundColor = BackgroundColorField()
    backgroundColorR = backgroundColor.backgroundColorR
    backgroundColorr = backgroundColorR
    backgroundColorG = backgroundColor.backgroundColorG
    backgroundColorg = backgroundColorG
    backgroundColorB = backgroundColor.backgroundColorB
    backgroundColorb = backgroundColorB

    hueRandom = FloatField()

    saturationRandom = FloatField()

    valueRandom = FloatField()

    enableMaxTiles = BoolField()

    randomUVTile = BoolField()

    maxTiles = LongField()

    colorSetName = DataStringField()
