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

    outputGeometry = TypedField(multi=True, writable=False)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(multi=True, default_value=1.0, writable=False)
    ocw = envelopeWeightsList

    blockGPU = BoolField(default_value=False)
    bgp = blockGPU

    envelope = FloatField(default_value=1.0, min_value=-2.0, max_value=2.0, soft_min_value=0.0, soft_max_value=1.0)
    en = envelope

    function = FunctionField(default_value=(0, 0, 0), readable=False)
    f = function
    fchild1 = function.fchild1
    f1 = fchild1
    fchild2 = function.fchild2
    f2 = fchild2
    fchild3 = function.fchild3
    f3 = fchild3

    map64BitIndices = TypedField()
    map = map64BitIndices

    weightList = WeightListField(multi=True, default_value=1.0)
    wl = weightList

    inputPoints = TypedField()

    inputArray = DataVectorArrayField()
    inArray = inputArray

    outputArray = DataVectorArrayField()
    outArray = outputArray

    falloffInfo = TypedField()

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    time = TimeField(default_value=1.0)
    ti = time

    inIterations = LongField(default_value=0)
    inIter = inIterations

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

    randEnvelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    raEn = randEnvelope

    StepEnvelope = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)
    StEnv = StepEnvelope

    strengthPP = TypedField(multi=True)

    Envelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    env = Envelope

    falloffObject = FalloffObjectField(default_value=(0.0, 0.0, 0.0))
    fallObj = falloffObject
    falloffObjectX = falloffObject.falloffObjectX
    fallObjx = falloffObjectX
    falloffObjectY = falloffObject.falloffObjectY
    fallObjy = falloffObjectY
    falloffObjectZ = falloffObject.falloffObjectZ
    fallObjz = falloffObjectZ

    localGlobalEnv = BoolField(default_value=True)

    falloffX = BoolField(default_value=True)
    fax = falloffX

    falloffY = BoolField(default_value=True)
    fay = falloffY

    falloffZ = BoolField(default_value=True)
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

    enablePosition = BoolField(default_value=True)
    enpos = enablePosition

    enableRotation = BoolField(default_value=True)
    enrot = enableRotation

    enableScale = BoolField(default_value=True)
    ensca = enableScale

    componentType = ComponentTypeEnumField(default_value=2)
    cty = componentType
