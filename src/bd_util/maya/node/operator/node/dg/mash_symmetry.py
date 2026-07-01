# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_symmetry import (
    CentreOfSymmetryField,
    FalloffObjectField,
    MColourField,
    OffsetPositionField,
    ReflectionVectorField,
    TranslateInPPField,
    TranslateOutPPField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.string import DataStringField
from ...attr.define.std.dt.vector_array import DataVectorArrayField


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


class AxisOfSymmetryEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X = 1
    Y = 3
    Z = 5


class AxisOfSymmetryEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X = 1
    Y = 3
    Z = 5

    NAME_MAP = {
        X: "X",
        Y: "Y",
        Z: "Z",
    }


class AxisOfSymmetryEnumField(
    EnumField[AxisOfSymmetryEnumAttrOperator, AxisOfSymmetryEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisOfSymmetryEnumAttrOperator
    PLUG_CLS = AxisOfSymmetryEnumPlugOperator


class PlacementModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MIRROR_PLANE = 1
    BOUNDING_BOX_PLUS = 2
    BOUNDING_BOX_MINUS = 3


class PlacementModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MIRROR_PLANE = 1
    BOUNDING_BOX_PLUS = 2
    BOUNDING_BOX_MINUS = 3

    NAME_MAP = {
        MIRROR_PLANE: "Mirror Plane",
        BOUNDING_BOX_PLUS: "Bounding Box +",
        BOUNDING_BOX_MINUS: "Bounding Box -",
    }


class PlacementModeEnumField(
    EnumField[PlacementModeEnumAttrOperator, PlacementModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PlacementModeEnumAttrOperator
    PLUG_CLS = PlacementModeEnumPlugOperator


class MASH_Symmetry(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Symmetry"

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

    translateInPP = TranslateInPPField()
    positionInPP = translateInPP.positionInPP
    scaleInPP = translateInPP.scaleInPP
    rotationInPP = translateInPP.rotationInPP
    idInPP = translateInPP.idInPP
    visibilityInPP = translateInPP.visibilityInPP

    translateOutPP = TranslateOutPPField()
    positionOutPP = translateOutPP.positionOutPP
    scaleOutPP = translateOutPP.scaleOutPP
    rotationOutPP = translateOutPP.rotationOutPP
    idOutPP = translateOutPP.idOutPP
    visibilityOutPP = translateOutPP.visibilityOutPP

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    time = TimeField()
    ti = time

    inIterations = LongField()
    inIter = inIterations

    centreOfSymmetry = CentreOfSymmetryField()
    centreOfSymmetry0 = centreOfSymmetry.centreOfSymmetry0
    centreOfSymmetry1 = centreOfSymmetry.centreOfSymmetry1
    centreOfSymmetry2 = centreOfSymmetry.centreOfSymmetry2

    reflectionVector = ReflectionVectorField()
    reflectionVector0 = reflectionVector.reflectionVector0
    reflectionVector1 = reflectionVector.reflectionVector1
    reflectionVector2 = reflectionVector.reflectionVector2

    offsetPosition = OffsetPositionField()
    offsetPosition0 = offsetPosition.offsetPosition0
    offsetPosition1 = offsetPosition.offsetPosition1
    offsetPosition2 = offsetPosition.offsetPosition2

    axisOfSymmetry = AxisOfSymmetryEnumField()

    placementMode = PlacementModeEnumField()

    enable = BoolField()
    en = enable

    enableScale = BoolField()

    enableRotation = BoolField()

    falloffObject = FalloffObjectField()
    fallObj = falloffObject
    falloffObjectX = falloffObject.falloffObjectX
    fallObjx = falloffObjectX
    falloffObjectY = falloffObject.falloffObjectY
    fallObjy = falloffObjectY
    falloffObjectZ = falloffObject.falloffObjectZ
    fallObjz = falloffObjectZ

    falloffX = BoolField()
    fax = falloffX

    falloffY = BoolField()
    fay = falloffY

    falloffZ = BoolField()
    faz = falloffZ

    falloffMessage = MessageField()
    fmsg = falloffMessage

    falloffInfo = TypedField()
