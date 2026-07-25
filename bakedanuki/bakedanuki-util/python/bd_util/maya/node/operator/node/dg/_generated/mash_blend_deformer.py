# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_blend_deformer import (
    BlendRampField,
    CurveRampField,
    EnvelopeWeightsListField,
    FunctionField,
    InflationRampField,
    InputField,
    MColourField,
    SmoothingRampField,
    WeightListField,
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
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


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


class FalloffAffectsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ALL = 1
    BLEND_ONLY = 2


class FalloffAffectsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ALL = 1
    BLEND_ONLY = 2

    NAME_MAP = {
        ALL: "All",
        BLEND_ONLY: "Blend Only",
    }


class FalloffAffectsEnumField(
    EnumField[FalloffAffectsEnumAttrOperator, FalloffAffectsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffAffectsEnumAttrOperator
    PLUG_CLS = FalloffAffectsEnumPlugOperator


class MapAffectsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ALL = 1
    BLEND_ONLY = 2


class MapAffectsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ALL = 1
    BLEND_ONLY = 2

    NAME_MAP = {
        ALL: "All",
        BLEND_ONLY: "Blend Only",
    }


class MapAffectsEnumField(
    EnumField[MapAffectsEnumAttrOperator, MapAffectsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MapAffectsEnumAttrOperator
    PLUG_CLS = MapAffectsEnumPlugOperator


class _GeneratedMASH_BlendDeformer(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_BlendDeformer"

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

    blendMesh = DataMeshField()

    smoothingIterations = LongField(default_value=0, min_value=0, max_value=100, soft_max_value=50)

    guideCurve = DataNurbsCurveField()

    inflate = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)

    blendValue = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    curveRamp = CurveRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    inflationRamp = InflationRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    blendRamp = BlendRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    smoothingRamp = SmoothingRampField(multi=True, default_value=(0.0, 0.0, 1.0))

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

    Envelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    env = Envelope

    randEnvelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    raEn = randEnvelope

    StepEnvelope = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)
    StEnv = StepEnvelope

    bilateralOne = FloatField(default_value=0.75, min_value=0.01, soft_max_value=1.0)

    bilateralTwo = FloatField(default_value=0.10000000149011612, min_value=0.01, soft_max_value=1.0)

    falloffAffects = FalloffAffectsEnumField(default_value=1)

    mapAffects = MapAffectsEnumField(default_value=1)

    radialBlend = BoolField(default_value=False)

    mFalloffInfo = TypedField(multi=True)

    enableStrengthX = BoolField(default_value=True)

    enableStrengthY = BoolField(default_value=True)

    enableStrengthZ = BoolField(default_value=True)

    strengthPP = TypedField(multi=True)
