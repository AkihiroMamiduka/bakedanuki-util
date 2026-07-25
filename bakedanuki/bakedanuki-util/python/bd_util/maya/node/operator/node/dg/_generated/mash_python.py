# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_python import (
    AxillaryInPPField,
    AxillaryOutPPField,
    MColourField,
    TranslateInPPField,
    TranslateOutPPField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.scalar.unit.time import TimeField
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


class _GeneratedMASH_Python(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Python"

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

    translateInPP = TranslateInPPField()
    positionInPP = translateInPP.positionInPP
    scaleInPP = translateInPP.scaleInPP
    rotationInPP = translateInPP.rotationInPP
    idInPP = translateInPP.idInPP
    visibilityInPP = translateInPP.visibilityInPP

    axillaryInPP = AxillaryInPPField()
    colorInPP = axillaryInPP.colorInPP
    uvTileInPP = axillaryInPP.uvTileInPP
    frameInPP = axillaryInPP.frameInPP
    isAnimatedInPP = axillaryInPP.isAnimatedInPP
    velocityInPP = axillaryInPP.velocityInPP
    velocityVecInPP = axillaryInPP.velocityVecInPP
    angularVelocityInPP = axillaryInPP.angularVelocityInPP
    angularVelocityVecInPP = axillaryInPP.angularVelocityVecInPP
    calculatedStrength = axillaryInPP.calculatedStrength

    translateOutPP = TranslateOutPPField()
    positionOutPP = translateOutPP.positionOutPP
    scaleOutPP = translateOutPP.scaleOutPP
    rotationOutPP = translateOutPP.rotationOutPP
    idOutPP = translateOutPP.idOutPP
    visibilityOutPP = translateOutPP.visibilityOutPP

    axillaryOutPP = AxillaryOutPPField()
    colorOutPP = axillaryOutPP.colorOutPP
    uvTileOutPP = axillaryOutPP.uvTileOutPP
    frameOutPP = axillaryOutPP.frameOutPP
    isAnimatedOutPP = axillaryOutPP.isAnimatedOutPP
    velocityOutPP = axillaryOutPP.velocityOutPP
    velocityVecOutPP = axillaryOutPP.velocityVecOutPP
    angularVelocityOutPP = axillaryOutPP.angularVelocityOutPP
    angularVelocityVecOutPP = axillaryOutPP.angularVelocityVecOutPP

    time = TimeField(default_value=0.0)
    tm = time

    pyScript = DataStringField()

    enable = BoolField(default_value=True)
