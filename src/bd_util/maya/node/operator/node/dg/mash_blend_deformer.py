# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_blend_deformer import (
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
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


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


class MASH_BlendDeformer(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_BlendDeformer"

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

    blendMesh = DataMeshField()

    smoothingIterations = LongField()

    guideCurve = DataNurbsCurveField()

    inflate = FloatField()

    blendValue = FloatField()

    curveRamp = CurveRampField(multi=True)

    inflationRamp = InflationRampField(multi=True)

    blendRamp = BlendRampField(multi=True)

    smoothingRamp = SmoothingRampField(multi=True)

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
    env = Envelope

    randEnvelope = FloatField()
    raEn = randEnvelope

    StepEnvelope = FloatField()
    StEnv = StepEnvelope

    bilateralOne = FloatField()

    bilateralTwo = FloatField()

    falloffAffects = FalloffAffectsEnumField()

    mapAffects = MapAffectsEnumField()

    radialBlend = BoolField()

    mFalloffInfo = TypedField(multi=True)

    enableStrengthX = BoolField()

    enableStrengthY = BoolField()

    enableStrengthZ = BoolField()

    strengthPP = TypedField(multi=True)
