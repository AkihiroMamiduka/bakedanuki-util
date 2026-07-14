# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.soft_mod import (
    EnvelopeWeightsListField,
    FalloffCenterField,
    FalloffCurveField,
    FunctionField,
    InputField,
    SoftModXformsField,
    WeightListField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.matrix import DataMatrixField


class UsePartialResolutionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FULL = 0
    PARTIAL = 1


class UsePartialResolutionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FULL = 0
    PARTIAL = 1

    NAME_MAP = {
        FULL: "Full",
        PARTIAL: "Partial",
    }


class UsePartialResolutionEnumField(
    EnumField[UsePartialResolutionEnumAttrOperator, UsePartialResolutionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UsePartialResolutionEnumAttrOperator
    PLUG_CLS = UsePartialResolutionEnumPlugOperator


class AngleInterpolationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CLOSEST = 0
    POSITIVE = 1
    NEGATIVE = 2


class AngleInterpolationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CLOSEST = 0
    POSITIVE = 1
    NEGATIVE = 2

    NAME_MAP = {
        CLOSEST: "Closest",
        POSITIVE: "Positive",
        NEGATIVE: "Negative",
    }


class AngleInterpolationEnumField(
    EnumField[AngleInterpolationEnumAttrOperator, AngleInterpolationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AngleInterpolationEnumAttrOperator
    PLUG_CLS = AngleInterpolationEnumPlugOperator


class FalloffModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    VOLUME = 0
    SURFACE = 1


class FalloffModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    VOLUME = 0
    SURFACE = 1

    NAME_MAP = {
        VOLUME: "Volume",
        SURFACE: "Surface",
    }


class FalloffModeEnumField(
    EnumField[FalloffModeEnumAttrOperator, FalloffModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffModeEnumAttrOperator
    PLUG_CLS = FalloffModeEnumPlugOperator


class SoftMod(DG):
    __slots__ = ()

    NODE_TYPE = "softMod"

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

    percentResolution = FloatField(default_value=5.0, min_value=0.0, max_value=10.0)
    ptr = percentResolution

    usePartialResolution = UsePartialResolutionEnumField(default_value=0)
    upr = usePartialResolution

    relative = BoolField(default_value=False)
    rel = relative

    softModXforms = SoftModXformsField()
    x = softModXforms
    preMatrix = softModXforms.preMatrix
    pre = preMatrix
    weightedMatrix = softModXforms.weightedMatrix
    wt = weightedMatrix
    postMatrix = softModXforms.postMatrix
    post = postMatrix

    weightedCompensationMatrix = DataMatrixField()
    wcm = weightedCompensationMatrix

    geomMatrix = DataMatrixField(multi=True)
    gm = geomMatrix

    matrix = DataMatrixField()
    ma = matrix

    bindPreMatrix = DataMatrixField()
    pm = bindPreMatrix

    falloffCurve = FalloffCurveField(multi=True, default_value=(0.0, 0.0, 0.0))
    fc = falloffCurve

    falloffRadius = DoubleLinearField(default_value=5.0, soft_min_value=0.0, soft_max_value=25.0)
    fr = falloffRadius

    falloffCenter = FalloffCenterField(default_value=(0.0, 0.0, 0.0))
    fcr = falloffCenter
    falloffCenterX = falloffCenter.falloffCenterX
    fcx = falloffCenterX
    falloffCenterY = falloffCenter.falloffCenterY
    fcy = falloffCenterY
    falloffCenterZ = falloffCenter.falloffCenterZ
    fcz = falloffCenterZ

    falloffInX = BoolField(default_value=True)
    fix = falloffInX

    falloffInY = BoolField(default_value=True)
    fiy = falloffInY

    falloffInZ = BoolField(default_value=True)
    fiz = falloffInZ

    falloffAroundSelection = BoolField(default_value=False)
    fas = falloffAroundSelection

    falloffMasking = BoolField(default_value=True)
    fm = falloffMasking

    influenceMatrix = DataMatrixField()
    im = influenceMatrix

    angleInterpolation = AngleInterpolationEnumField(default_value=0)
    ait = angleInterpolation

    useDistanceCache = BoolField(default_value=True)
    udc = useDistanceCache

    limitCacheUpdates = BoolField(default_value=False)
    lcu = limitCacheUpdates

    distanceCacheDirty = BoolField(default_value=True, writable=False)
    dcd = distanceCacheDirty

    falloffMode = FalloffModeEnumField(default_value=0)
    fom = falloffMode

    distanceCache = TypedField(multi=True, writable=False)
    dic = distanceCache

    fastFalloffCenter = BoolField(default_value=False)
    ffc = fastFalloffCenter
