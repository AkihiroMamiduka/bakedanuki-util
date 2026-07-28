# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.blend_shape import (
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
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import (
    Double3Field,
)
from ....attr.define.custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import (
    Float3Field,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
from ....attr.define.std.dt.string import DataStringField


class OriginEnumPlugOperator(EnumPlugOperator["OriginEnumAttrOperator"]):
    __slots__ = ()

    WORLD = 0
    LOCAL = 1
    USER = 2


class OriginEnumAttrOperator(EnumAttrOperator[OriginEnumPlugOperator]):
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


class DeformationOrderEnumPlugOperator(
    EnumPlugOperator["DeformationOrderEnumAttrOperator"]
):
    __slots__ = ()

    PRE_MINUS_DEFORMATION = 0
    POST_MINUS_DEFORMATION = 1
    OTHER_DEFORMATION = 2


class DeformationOrderEnumAttrOperator(
    EnumAttrOperator[DeformationOrderEnumPlugOperator]
):
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
    EnumField[
        DeformationOrderEnumAttrOperator, DeformationOrderEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DeformationOrderEnumAttrOperator
    PLUG_CLS = DeformationOrderEnumPlugOperator


class GeneratedBlendShape(DG):
    __slots__ = ()

    NODE_TYPE = "blendShape"

    input = InputField(multi=True)
    ip = input

    weightFunction = TypedField(multi=True)
    wfl = weightFunction

    outputGeometry = TypedField(multi=True, writable=False)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(
        multi=True, default_value=1.0, writable=False
    )
    ocw = envelopeWeightsList

    blockGPU = BoolField(default_value=False)
    bgp = blockGPU

    envelope = FloatField(
        default_value=1.0,
        min_value=-2.0,
        max_value=2.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
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

    topologyCheck = BoolField(default_value=True)
    tc = topologyCheck

    weight = FloatField(
        multi=True,
        default_value=0.0,
        min_value=-10.0,
        max_value=10.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
        long_name=".weight",
        short_name=".w",
    )

    icon = DataStringField(multi=True, readable=False)
    icn = icon

    inputTarget = InputTargetField(multi=True)
    it = inputTarget

    vertex = Float3Field()
    vt = vertex

    xVertex = DoubleLinearField()
    vx = xVertex

    yVertex = DoubleLinearField()
    vy = yVertex

    zVertex = DoubleLinearField()
    vz = zVertex

    controlPoints = Double3Field()
    cp = controlPoints

    xValue = DoubleLinearField()
    xv = xValue

    yValue = DoubleLinearField()
    yv = yValue

    zValue = DoubleLinearField()
    zv = zValue

    origin = OriginEnumField(default_value=1)
    or_ = origin

    baseOrigin = BaseOriginField(default_value=(0.0, 0.0, 0.0))
    bo = baseOrigin
    baseOriginX = baseOrigin.baseOriginX
    bx = baseOriginX
    baseOriginY = baseOrigin.baseOriginY
    by = baseOriginY
    baseOriginZ = baseOrigin.baseOriginZ
    bz = baseOriginZ

    targetOrigin = TargetOriginField(default_value=(0.0, 0.0, 0.0))
    to = targetOrigin
    targetOriginX = targetOrigin.targetOriginX
    tx = targetOriginX
    targetOriginY = targetOrigin.targetOriginY
    ty = targetOriginY
    targetOriginZ = targetOrigin.targetOriginZ
    tz = targetOriginZ

    parallelBlender = BoolField(default_value=False)
    pb = parallelBlender

    useTargetCompWeights = BoolField(default_value=True)
    itcw = useTargetCompWeights

    supportNegativeWeights = BoolField(default_value=False)
    sn = supportNegativeWeights

    paintWeights = DataDoubleArrayField()
    ptw = paintWeights

    offsetDeformer = OffsetDeformerField(default_value=(0.0, 0.0, 0.0))
    ofm = offsetDeformer
    offsetX = offsetDeformer.offsetX
    ofx = offsetX
    offsetY = offsetDeformer.offsetY
    ofy = offsetY
    offsetZ = offsetDeformer.offsetZ
    ofz = offsetZ

    localVertexFrame = BoolField(default_value=True)
    lvf = localVertexFrame

    midLayerId = LongField(default_value=-2147483648)
    mlid = midLayerId

    midLayerParent = LongField(default_value=-1)
    mlpr = midLayerParent

    nextNode = LongField(default_value=-2147483648)
    nxnd = nextNode

    parentDirectory = LongField(multi=True, default_value=-1)
    pndr = parentDirectory

    nextTarget = LongField(multi=True, default_value=-2147483648)
    nxtg = nextTarget

    targetVisibility = BoolField(multi=True, default_value=True)
    tgvs = targetVisibility

    targetParentVisibility = BoolField(multi=True, default_value=True)
    tpvs = targetParentVisibility

    targetDirectory = TargetDirectoryField(multi=True)
    tgdt = targetDirectory

    deformationOrder = DeformationOrderEnumField(default_value=0)
    dfo = deformationOrder

    inbetweenInfoGroup = InbetweenInfoGroupField(multi=True)
    ibig = inbetweenInfoGroup

    symmetryEdge = DataStringField(multi=True)
    syme = symmetryEdge
