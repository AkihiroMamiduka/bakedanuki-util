# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_strength import (
    MColourField,
    PositionStrengthField,
    PositionStrengthMapField,
    RotationStrengthField,
    RotationStrengthMapField,
    ScaleStrengthField,
    ScaleStrengthMapField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.unit_scalar.time import TimeField
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


class PosMapDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class PosMapDirectionEnumAttrOperator(EnumAttrOperator):
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


class PosMapDirectionEnumField(
    EnumField[PosMapDirectionEnumAttrOperator, PosMapDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PosMapDirectionEnumAttrOperator
    PLUG_CLS = PosMapDirectionEnumPlugOperator


class RotMapDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class RotMapDirectionEnumAttrOperator(EnumAttrOperator):
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


class RotMapDirectionEnumField(
    EnumField[RotMapDirectionEnumAttrOperator, RotMapDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotMapDirectionEnumAttrOperator
    PLUG_CLS = RotMapDirectionEnumPlugOperator


class ScaleMapDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class ScaleMapDirectionEnumAttrOperator(EnumAttrOperator):
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


class ScaleMapDirectionEnumField(
    EnumField[ScaleMapDirectionEnumAttrOperator, ScaleMapDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleMapDirectionEnumAttrOperator
    PLUG_CLS = ScaleMapDirectionEnumPlugOperator


class _GeneratedMASH_Strength(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Strength"

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

    enable = BoolField(default_value=True)

    positionStrength = PositionStrengthField(default_value=(1.0, 1.0, 1.0))
    positionStrength0 = positionStrength.positionStrength0
    positionStrength1 = positionStrength.positionStrength1
    positionStrength2 = positionStrength.positionStrength2

    rotationStrength = RotationStrengthField(default_value=(1.0, 1.0, 1.0))
    rotationStrength0 = rotationStrength.rotationStrength0
    rotationStrength1 = rotationStrength.rotationStrength1
    rotationStrength2 = rotationStrength.rotationStrength2

    scaleStrength = ScaleStrengthField(default_value=(1.0, 1.0, 1.0))
    scaleStrength0 = scaleStrength.scaleStrength0
    scaleStrength1 = scaleStrength.scaleStrength1
    scaleStrength2 = scaleStrength.scaleStrength2

    randomSeed = LongField(default_value=0, min_value=0, soft_max_value=100)

    positionDelay = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=50.0)

    rotationDelay = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=50.0)

    scaleDelay = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=50.0)

    positionStrengthMap = PositionStrengthMapField(default_value=(1.0, 1.0, 1.0))
    positionStrengthMapR = positionStrengthMap.positionStrengthMapR
    positionStrengthMapr = positionStrengthMapR
    positionStrengthMapG = positionStrengthMap.positionStrengthMapG
    positionStrengthMapg = positionStrengthMapG
    positionStrengthMapB = positionStrengthMap.positionStrengthMapB
    positionStrengthMapb = positionStrengthMapB

    rotationStrengthMap = RotationStrengthMapField(default_value=(1.0, 1.0, 1.0))
    rotationStrengthMapR = rotationStrengthMap.rotationStrengthMapR
    rotationStrengthMapr = rotationStrengthMapR
    rotationStrengthMapG = rotationStrengthMap.rotationStrengthMapG
    rotationStrengthMapg = rotationStrengthMapG
    rotationStrengthMapB = rotationStrengthMap.rotationStrengthMapB
    rotationStrengthMapb = rotationStrengthMapB

    scaleStrengthMap = ScaleStrengthMapField(default_value=(1.0, 1.0, 1.0))
    scaleStrengthMapR = scaleStrengthMap.scaleStrengthMapR
    scaleStrengthMapr = scaleStrengthMapR
    scaleStrengthMapG = scaleStrengthMap.scaleStrengthMapG
    scaleStrengthMapg = scaleStrengthMapG
    scaleStrengthMapB = scaleStrengthMap.scaleStrengthMapB
    scaleStrengthMapb = scaleStrengthMapB

    reversePosition = BoolField(default_value=False)

    reverseRotation = BoolField(default_value=False)

    reverseScale = BoolField(default_value=False)

    positionRandomise = BoolField(default_value=False)

    rotationRandomise = BoolField(default_value=False)

    scaleRandomise = BoolField(default_value=False)

    affectsPosition = BoolField(default_value=False)

    affectsRotation = BoolField(default_value=False)

    affectsScale = BoolField(default_value=True)

    positionMapMatrix = MatrixField()

    rotationMapMatrix = MatrixField()

    scaleMapMatrix = MatrixField()

    posMapDirection = PosMapDirectionEnumField(default_value=2)

    rotMapDirection = RotMapDirectionEnumField(default_value=2)

    scaleMapDirection = ScaleMapDirectionEnumField(default_value=2)
