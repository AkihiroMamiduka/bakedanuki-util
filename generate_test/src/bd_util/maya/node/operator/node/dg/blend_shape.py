# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.blend_shape import (
    BaseOriginField,
    EnvelopeWeightsListField,
    FunctionField,
    InbetweenInfoGroupField,
    InputField,
    InputTargetField,
    OffsetDeformerField,
    TargetDirectoryField,
    TargetOriginField,
    WeightListField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.double_array import DataDoubleArrayField
from ...attr.define.std.dt.string import DataStringField


class OriginEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 0
    LOCAL = 1
    USER = 2


class OriginEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 0
    LOCAL = 1
    USER = 2

    NAME_MAP = {
        WORLD: "world",
        LOCAL: "local",
        USER: "user",
    }


class OriginEnumField(
    EnumField[OriginEnumAttrOperator, OriginEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OriginEnumAttrOperator
    PLUG_CLS = OriginEnumPlugOperator


class DeformationOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PRE_MINUS_DEFORMATION = 0
    POST_MINUS_DEFORMATION = 1
    OTHER_DEFORMATION = 2


class DeformationOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PRE_MINUS_DEFORMATION = 0
    POST_MINUS_DEFORMATION = 1
    OTHER_DEFORMATION = 2

    NAME_MAP = {
        PRE_MINUS_DEFORMATION: "pre-deformation",
        POST_MINUS_DEFORMATION: "post-deformation",
        OTHER_DEFORMATION: "other deformation",
    }


class DeformationOrderEnumField(
    EnumField[DeformationOrderEnumAttrOperator, DeformationOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DeformationOrderEnumAttrOperator
    PLUG_CLS = DeformationOrderEnumPlugOperator


class BlendShape(DG):
    __slots__ = ()

    NODE_TYPE = "blendShape"

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

    topologyCheck = BoolField()
    tc = topologyCheck

    .weight = FloatField(multi=True)
    .w = .weight

    icon = DataStringField(multi=True)
    icn = icon

    inputTarget = InputTargetField(multi=True)
    it = inputTarget

    # TODO: inputTarget.vertex (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: inputTarget.vertex.xVertex (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: inputTarget.vertex.yVertex (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: inputTarget.vertex.zVertex (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: inputTarget.controlPoints (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: inputTarget.controlPoints.xValue (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: inputTarget.controlPoints.yValue (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: inputTarget.controlPoints.zValue (attributeType=None, dataType=None) は未対応のため手動で追加してください

    origin = OriginEnumField()
    or_ = origin

    baseOrigin = BaseOriginField()
    bo = baseOrigin
    baseOriginX = baseOrigin.baseOriginX
    bx = baseOriginX
    baseOriginY = baseOrigin.baseOriginY
    by = baseOriginY
    baseOriginZ = baseOrigin.baseOriginZ
    bz = baseOriginZ

    targetOrigin = TargetOriginField()
    to = targetOrigin
    targetOriginX = targetOrigin.targetOriginX
    tx = targetOriginX
    targetOriginY = targetOrigin.targetOriginY
    ty = targetOriginY
    targetOriginZ = targetOrigin.targetOriginZ
    tz = targetOriginZ

    parallelBlender = BoolField()
    pb = parallelBlender

    useTargetCompWeights = BoolField()
    itcw = useTargetCompWeights

    supportNegativeWeights = BoolField()
    sn = supportNegativeWeights

    paintWeights = DataDoubleArrayField()
    ptw = paintWeights

    offsetDeformer = OffsetDeformerField()
    ofm = offsetDeformer
    offsetX = offsetDeformer.offsetX
    ofx = offsetX
    offsetY = offsetDeformer.offsetY
    ofy = offsetY
    offsetZ = offsetDeformer.offsetZ
    ofz = offsetZ

    localVertexFrame = BoolField()
    lvf = localVertexFrame

    midLayerId = LongField()
    mlid = midLayerId

    midLayerParent = LongField()
    mlpr = midLayerParent

    nextNode = LongField()
    nxnd = nextNode

    parentDirectory = LongField(multi=True)
    pndr = parentDirectory

    nextTarget = LongField(multi=True)
    nxtg = nextTarget

    targetVisibility = BoolField(multi=True)
    tgvs = targetVisibility

    targetParentVisibility = BoolField(multi=True)
    tpvs = targetParentVisibility

    targetDirectory = TargetDirectoryField(multi=True)
    tgdt = targetDirectory

    deformationOrder = DeformationOrderEnumField()
    dfo = deformationOrder

    inbetweenInfoGroup = InbetweenInfoGroupField(multi=True)
    ibig = inbetweenInfoGroup

    symmetryEdge = DataStringField(multi=True)
    syme = symmetryEdge
