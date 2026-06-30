# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_deformer import (
    EnvelopeWeightsListField,
    FalloffObjectField,
    FunctionField,
    InputField,
    MColourField,
    TranslateInPPField,
    TranslateOutPPField,
    WeightListField,
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


class ComponentTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    VERTEX = 1
    FACE = 2
    VERTEX_NORMAL = 3


class ComponentTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    VERTEX = 1
    FACE = 2
    VERTEX_NORMAL = 3

    NAME_MAP = {
        VERTEX: "Vertex",
        FACE: "Face",
        VERTEX_NORMAL: "Vertex Normal",
    }


class ComponentTypeEnumField(
    EnumField[ComponentTypeEnumAttrOperator, ComponentTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ComponentTypeEnumAttrOperator
    PLUG_CLS = ComponentTypeEnumPlugOperator


class MASH_Deformer(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Deformer"

    input = InputField(multi=True)
    ip = input

    weightFunction = TypedField(multi=True)
    wfl = weightFunction

    outputGeometry = TypedField(multi=True)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(multi=True)
    ocw = envelopeWeightsList

    blockGPU = BoolField()
    bgp = blockGPU

    envelope = FloatField()
    en = envelope

    function = FunctionField()
    f = function
    fchild1 = function.fchild1
    f1 = fchild1
    fchild2 = function.fchild2
    f2 = fchild2
    fchild3 = function.fchild3
    f3 = fchild3

    map64BitIndices = TypedField()
    map = map64BitIndices

    weightList = WeightListField(multi=True)
    wl = weightList

    inputPoints = TypedField()

    inputArray = DataVectorArrayField()
    inArray = inputArray

    outputArray = DataVectorArrayField()
    outArray = outputArray

    falloffInfo = TypedField()

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    time = TimeField()
    ti = time

    inIterations = LongField()
    inIter = inIterations

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

    randEnvelope = FloatField()
    raEn = randEnvelope

    StepEnvelope = FloatField()
    StEnv = StepEnvelope

    strengthPP = TypedField(multi=True)

    Envelope = FloatField()
    env = Envelope

    falloffObject = FalloffObjectField()
    fallObj = falloffObject
    falloffObjectX = falloffObject.falloffObjectX
    fallObjx = falloffObjectX
    falloffObjectY = falloffObject.falloffObjectY
    fallObjy = falloffObjectY
    falloffObjectZ = falloffObject.falloffObjectZ
    fallObjz = falloffObjectZ

    localGlobalEnv = BoolField()

    falloffX = BoolField()
    fax = falloffX

    falloffY = BoolField()
    fay = falloffY

    falloffZ = BoolField()
    faz = falloffZ

    falloffMessage = MessageField()
    fmsg = falloffMessage

    translateInPP = TranslateInPPField()
    positionInPP = translateInPP.positionInPP
    scaleInPP = translateInPP.scaleInPP
    rotationInPP = translateInPP.rotationInPP

    translateOutPP = TranslateOutPPField()
    positionOutPP = translateOutPP.positionOutPP
    scaleOutPP = translateOutPP.scaleOutPP
    rotationOutPP = translateOutPP.rotationOutPP

    enablePosition = BoolField()
    enpos = enablePosition

    enableRotation = BoolField()
    enrot = enableRotation

    enableScale = BoolField()
    ensca = enableScale

    componentType = ComponentTypeEnumField()
    cty = componentType
