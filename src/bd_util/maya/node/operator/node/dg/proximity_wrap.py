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

    associativeGeometry = TypedField(multi=True)
    associativegeom = associativeGeometry

    drivers = DriversField(multi=True)
    drvr = drivers

    driverWeightFunction = TypedField(multi=True)
    dwfl = driverWeightFunction

    maxDrivers = LongField()
    maxd = maxDrivers

    falloffScale = DoubleField()
    sfo = falloffScale

    dropoffRateScale = DoubleField()
    sdpo = dropoffRateScale

    scaleCompensation = DoubleField()
    scp = scaleCompensation

    wrapMode = WrapModeEnumField()
    wmd = wrapMode

    coordinateFrames = CoordinateFramesEnumField()
    crdf = coordinateFrames

    smoothNormals = LongField()
    snrm = smoothNormals

    spanSamples = LongField()
    spns = spanSamples

    smoothInfluences = LongField()
    sinf = smoothInfluences

    falloffRamp = FalloffRampField(multi=True)
    frmp = falloffRamp

    softNormalization = BoolField()
    sftn = softNormalization

    useBindTags = BoolField()
    ubt = useBindTags

    bindTagsFilter = DataStringField()
    btf = bindTagsFilter

    perDriverWeightsList = PerDriverWeightsListField(multi=True)
    pdwl = perDriverWeightsList

    perVertexWeightsList = PerVertexWeightsListField(multi=True)
    pvwl = perVertexWeightsList
