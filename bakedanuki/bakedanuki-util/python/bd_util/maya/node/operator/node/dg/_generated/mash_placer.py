# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_placer import (
    MColourField,
    PositionAdjustField,
    RandomIdField,
    RandomRotationField,
    RandomScaleField,
    RotationAdjustField,
    ScaleAdjustField,
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
from ....attr.define.std.dt.mesh import DataMeshField
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


class CollideOnCreateEnumPlugOperator(EnumPlugOperator["CollideOnCreateEnumAttrOperator"]):
    __slots__ = ()

    OFF = 1
    COLLIDE = 2
    STRICT = 3


class CollideOnCreateEnumAttrOperator(EnumAttrOperator[CollideOnCreateEnumPlugOperator]):
    __slots__ = ()

    OFF = 1
    COLLIDE = 2
    STRICT = 3

    NAME_MAP = {
        OFF: "Off",
        COLLIDE: "Collide",
        STRICT: "Strict",
    }


class CollideOnCreateEnumField(
    EnumField[CollideOnCreateEnumAttrOperator, CollideOnCreateEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollideOnCreateEnumAttrOperator
    PLUG_CLS = CollideOnCreateEnumPlugOperator


class AlignBrushAxisEnumPlugOperator(EnumPlugOperator["AlignBrushAxisEnumAttrOperator"]):
    __slots__ = ()

    ALL = 1
    X = 2
    Y = 3
    Z = 4


class AlignBrushAxisEnumAttrOperator(EnumAttrOperator[AlignBrushAxisEnumPlugOperator]):
    __slots__ = ()

    ALL = 1
    X = 2
    Y = 3
    Z = 4

    NAME_MAP = {
        ALL: "All",
        X: "X",
        Y: "Y",
        Z: "Z",
    }


class AlignBrushAxisEnumField(
    EnumField[AlignBrushAxisEnumAttrOperator, AlignBrushAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlignBrushAxisEnumAttrOperator
    PLUG_CLS = AlignBrushAxisEnumPlugOperator


class RotationModeEnumPlugOperator(EnumPlugOperator["RotationModeEnumAttrOperator"]):
    __slots__ = ()

    OFF = 1
    ALIGN_TO_MESH = 2
    ALIGN_TO_BRUSH = 3


class RotationModeEnumAttrOperator(EnumAttrOperator[RotationModeEnumPlugOperator]):
    __slots__ = ()

    OFF = 1
    ALIGN_TO_MESH = 2
    ALIGN_TO_BRUSH = 3

    NAME_MAP = {
        OFF: "Off",
        ALIGN_TO_MESH: "Align to Mesh",
        ALIGN_TO_BRUSH: "Align to Brush",
    }


class RotationModeEnumField(
    EnumField[RotationModeEnumAttrOperator, RotationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationModeEnumAttrOperator
    PLUG_CLS = RotationModeEnumPlugOperator


class IdModeEnumPlugOperator(EnumPlugOperator["IdModeEnumAttrOperator"]):
    __slots__ = ()

    FIXED = 1
    RANDOM = 2


class IdModeEnumAttrOperator(EnumAttrOperator[IdModeEnumPlugOperator]):
    __slots__ = ()

    FIXED = 1
    RANDOM = 2

    NAME_MAP = {
        FIXED: "Fixed",
        RANDOM: "Random",
    }


class IdModeEnumField(
    EnumField[IdModeEnumAttrOperator, IdModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IdModeEnumAttrOperator
    PLUG_CLS = IdModeEnumPlugOperator


class BrushTypeEnumPlugOperator(EnumPlugOperator["BrushTypeEnumAttrOperator"]):
    __slots__ = ()

    POINTS_BRUSH = 1
    COLLIDE_BRUSH = 2
    DELETE_BRUSH = 3
    ID_BRUSH = 4
    MOVE_TOOL = 5
    ROTATE_TOOL = 6
    SCALE_TOOL = 7
    NUDGE_BRUSH = 8


class BrushTypeEnumAttrOperator(EnumAttrOperator[BrushTypeEnumPlugOperator]):
    __slots__ = ()

    POINTS_BRUSH = 1
    COLLIDE_BRUSH = 2
    DELETE_BRUSH = 3
    ID_BRUSH = 4
    MOVE_TOOL = 5
    ROTATE_TOOL = 6
    SCALE_TOOL = 7
    NUDGE_BRUSH = 8

    NAME_MAP = {
        POINTS_BRUSH: "Points Brush",
        COLLIDE_BRUSH: "Collide Brush",
        DELETE_BRUSH: "Delete Brush",
        ID_BRUSH: "ID Brush",
        MOVE_TOOL: "Move Tool",
        ROTATE_TOOL: "Rotate Tool",
        SCALE_TOOL: "Scale Tool",
        NUDGE_BRUSH: "Nudge Brush",
    }


class BrushTypeEnumField(
    EnumField[BrushTypeEnumAttrOperator, BrushTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BrushTypeEnumAttrOperator
    PLUG_CLS = BrushTypeEnumPlugOperator


class GeneratedMASH_Placer(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Placer"

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

    enable = BoolField(default_value=True)

    collideOnCreate = CollideOnCreateEnumField(default_value=1)

    alignBrushAxis = AlignBrushAxisEnumField(default_value=3)

    rotationMode = RotationModeEnumField(default_value=2)

    leanAmount = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    pushAlongNormal = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)

    randomSeed = LongField(default_value=1, min_value=1, soft_max_value=100)

    paintId = LongField(default_value=0, min_value=0, soft_max_value=10)

    brushRadius = FloatField(default_value=2.0, min_value=0.0, soft_max_value=20.0)

    scatterDensity = LongField(default_value=1, min_value=1, soft_max_value=10)

    brushSpacing = FloatField(default_value=2.0, min_value=0.0, soft_max_value=10.0)

    brushStrength = FloatField(default_value=5.0, min_value=0.0, soft_max_value=5.0)

    randomScale = RandomScaleField(default_value=(1.0, 1.0), min_value=(0.0, 0.0))
    randomScale0 = randomScale.randomScale0
    randomScale1 = randomScale.randomScale1

    randomRotation = RandomRotationField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0))
    randomRotation0 = randomRotation.randomRotation0
    randomRotation1 = randomRotation.randomRotation1
    randomRotation2 = randomRotation.randomRotation2

    randomId = RandomIdField(default_value=(0, 0), min_value=(0, 0))
    randomId0 = randomId.randomId0
    randomId1 = randomId.randomId1

    scatter = BoolField(default_value=False)

    paintPoints = TypedField()

    idMode = IdModeEnumField(default_value=1)

    brushType = BrushTypeEnumField(default_value=1)

    paintJson = DataStringField()

    networkJson = DataStringField()

    paintMeshes = DataMeshField(multi=True)

    positionAdjust = PositionAdjustField(default_value=(0.0, 0.0, 0.0))
    positionAdjust0 = positionAdjust.positionAdjust0
    positionAdjust1 = positionAdjust.positionAdjust1
    positionAdjust2 = positionAdjust.positionAdjust2

    rotationAdjust = RotationAdjustField(default_value=(0.0, 0.0, 0.0))
    rotationAdjust0 = rotationAdjust.rotationAdjust0
    rotationAdjust1 = rotationAdjust.rotationAdjust1
    rotationAdjust2 = rotationAdjust.rotationAdjust2

    scaleAdjust = ScaleAdjustField(default_value=(0.0, 0.0, 0.0))
    scaleAdjust0 = scaleAdjust.scaleAdjust0
    scaleAdjust1 = scaleAdjust.scaleAdjust1
    scaleAdjust2 = scaleAdjust.scaleAdjust2

    stickToMesh = BoolField(default_value=False)
