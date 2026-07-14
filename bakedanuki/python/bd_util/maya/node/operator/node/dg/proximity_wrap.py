# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.proximity_wrap import (
    DriversField,
    EnvelopeWeightsListField,
    FalloffRampField,
    FunctionField,
    InputField,
    PerDriverWeightsListField,
    PerVertexWeightsListField,
    WeightListField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField


class WrapModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFFSET = 0
    SURFACE = 1
    SNAP = 2
    RIGID = 3
    CLUSTER = 4


class WrapModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFFSET = 0
    SURFACE = 1
    SNAP = 2
    RIGID = 3
    CLUSTER = 4

    NAME_MAP = {
        OFFSET: "Offset",
        SURFACE: "Surface",
        SNAP: "Snap",
        RIGID: "Rigid",
        CLUSTER: "Cluster",
    }


class WrapModeEnumField(
    EnumField[WrapModeEnumAttrOperator, WrapModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WrapModeEnumAttrOperator
    PLUG_CLS = WrapModeEnumPlugOperator


class CoordinateFramesEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DRIVER = 0
    SNAP = 1


class CoordinateFramesEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DRIVER = 0
    SNAP = 1

    NAME_MAP = {
        DRIVER: "Driver",
        SNAP: "Snap",
    }


class CoordinateFramesEnumField(
    EnumField[CoordinateFramesEnumAttrOperator, CoordinateFramesEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoordinateFramesEnumAttrOperator
    PLUG_CLS = CoordinateFramesEnumPlugOperator


class ProximityWrap(DG):
    __slots__ = ()

    NODE_TYPE = "proximityWrap"

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

    associativeGeometry = TypedField(multi=True)
    associativegeom = associativeGeometry

    drivers = DriversField(multi=True)
    drvr = drivers

    driverWeightFunction = TypedField(multi=True)
    dwfl = driverWeightFunction

    maxDrivers = LongField(default_value=10, min_value=1, max_value=20)
    maxd = maxDrivers

    falloffScale = DoubleField(default_value=1.0, min_value=0.01, soft_min_value=0.01, soft_max_value=10.0)
    sfo = falloffScale

    dropoffRateScale = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    sdpo = dropoffRateScale

    scaleCompensation = DoubleField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    scp = scaleCompensation

    wrapMode = WrapModeEnumField(default_value=1)
    wmd = wrapMode

    coordinateFrames = CoordinateFramesEnumField(default_value=0)
    crdf = coordinateFrames

    smoothNormals = LongField(default_value=0, min_value=0, max_value=20)
    snrm = smoothNormals

    spanSamples = LongField(default_value=2, min_value=1, max_value=10)
    spns = spanSamples

    smoothInfluences = LongField(default_value=0, min_value=0, max_value=20)
    sinf = smoothInfluences

    falloffRamp = FalloffRampField(multi=True, default_value=(0.0, 0.0, 0.0))
    frmp = falloffRamp

    softNormalization = BoolField(default_value=False)
    sftn = softNormalization

    useBindTags = BoolField(default_value=False)
    ubt = useBindTags

    bindTagsFilter = DataStringField()
    btf = bindTagsFilter

    perDriverWeightsList = PerDriverWeightsListField(multi=True, writable=False)
    pdwl = perDriverWeightsList

    perVertexWeightsList = PerVertexWeightsListField(multi=True, writable=False)
    pvwl = perVertexWeightsList
