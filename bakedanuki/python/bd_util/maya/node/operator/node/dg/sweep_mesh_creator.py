# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.sweep_mesh_creator import TaperCurveField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class SweepProfileTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    REGULAR_POLYGON = 0
    ROUNDED_RECTANGLE = 1
    LINE = 2
    ARC = 3
    WAVE = 4
    CUSTOM = 5


class SweepProfileTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    REGULAR_POLYGON = 0
    ROUNDED_RECTANGLE = 1
    LINE = 2
    ARC = 3
    WAVE = 4
    CUSTOM = 5

    NAME_MAP = {
        REGULAR_POLYGON: "Regular Polygon",
        ROUNDED_RECTANGLE: "Rounded Rectangle",
        LINE: "Line",
        ARC: "Arc",
        WAVE: "Wave",
        CUSTOM: "Custom",
    }


class SweepProfileTypeEnumField(
    EnumField[SweepProfileTypeEnumAttrOperator, SweepProfileTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SweepProfileTypeEnumAttrOperator
    PLUG_CLS = SweepProfileTypeEnumPlugOperator


class ProfilePolyTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONVEX = 0
    STAR = 1


class ProfilePolyTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONVEX = 0
    STAR = 1

    NAME_MAP = {
        CONVEX: "Convex",
        STAR: "Star",
    }


class ProfilePolyTypeEnumField(
    EnumField[ProfilePolyTypeEnumAttrOperator, ProfilePolyTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ProfilePolyTypeEnumAttrOperator
    PLUG_CLS = ProfilePolyTypeEnumPlugOperator


class PatternDistributionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RADIAL = 0
    SQUARE = 1
    LINEAR = 2


class PatternDistributionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RADIAL = 0
    SQUARE = 1
    LINEAR = 2

    NAME_MAP = {
        RADIAL: "Radial",
        SQUARE: "Square",
        LINEAR: "Linear",
    }


class PatternDistributionEnumField(
    EnumField[PatternDistributionEnumAttrOperator, PatternDistributionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PatternDistributionEnumAttrOperator
    PLUG_CLS = PatternDistributionEnumPlugOperator


class AlignProfileHorizontalEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LEFT = 0
    CENTER = 1
    RIGHT = 2


class AlignProfileHorizontalEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LEFT = 0
    CENTER = 1
    RIGHT = 2

    NAME_MAP = {
        LEFT: "Left",
        CENTER: "Center",
        RIGHT: "Right",
    }


class AlignProfileHorizontalEnumField(
    EnumField[AlignProfileHorizontalEnumAttrOperator, AlignProfileHorizontalEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlignProfileHorizontalEnumAttrOperator
    PLUG_CLS = AlignProfileHorizontalEnumPlugOperator


class AlignProfileVerticalEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TOP = 0
    CENTER = 1
    BOTTOM = 2


class AlignProfileVerticalEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TOP = 0
    CENTER = 1
    BOTTOM = 2

    NAME_MAP = {
        TOP: "Top",
        CENTER: "Center",
        BOTTOM: "Bottom",
    }


class AlignProfileVerticalEnumField(
    EnumField[AlignProfileVerticalEnumAttrOperator, AlignProfileVerticalEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlignProfileVerticalEnumAttrOperator
    PLUG_CLS = AlignProfileVerticalEnumPlugOperator


class InterpolationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PRECISION = 0
    START_TO_END = 1
    EP_TO_EP = 2
    DISTANCE = 3


class InterpolationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PRECISION = 0
    START_TO_END = 1
    EP_TO_EP = 2
    DISTANCE = 3

    NAME_MAP = {
        PRECISION: "Precision",
        START_TO_END: "Start to End",
        EP_TO_EP: "EP to EP",
        DISTANCE: "Distance",
    }


class InterpolationModeEnumField(
    EnumField[InterpolationModeEnumAttrOperator, InterpolationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InterpolationModeEnumAttrOperator
    PLUG_CLS = InterpolationModeEnumPlugOperator


class CreateUVsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    UNIFORM = 1
    UNFOLD = 2


class CreateUVsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    UNIFORM = 1
    UNFOLD = 2

    NAME_MAP = {
        NONE: "None",
        UNIFORM: "Uniform",
        UNFOLD: "Unfold",
    }


class CreateUVsEnumField(
    EnumField[CreateUVsEnumAttrOperator, CreateUVsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CreateUVsEnumAttrOperator
    PLUG_CLS = CreateUVsEnumPlugOperator


class SweepMeshCreator(DG):
    __slots__ = ()

    NODE_TYPE = "sweepMeshCreator"

    sweepProfileType = SweepProfileTypeEnumField(default_value=0)

    customSweepProfileData = TypedField(readable=False)

    profileArcAngle = DoubleAngleField(default_value=180.0, min_value=0.0, max_value=360.0)

    profileArcSegments = LongField(default_value=4, min_value=1, soft_max_value=40)

    profilePolyType = ProfilePolyTypeEnumField(default_value=0)

    profilePolySides = LongField(default_value=8, min_value=3, soft_max_value=20)

    profilePolyInnerRadius = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)

    profileRectWidth = DoubleLinearField(default_value=0.0, min_value=0.0, soft_max_value=2.0)

    profileRectHeight = DoubleLinearField(default_value=0.0, min_value=0.0, soft_max_value=2.0)

    profileRectCornerRadius = DoubleLinearField(default_value=0.0, min_value=0.0, soft_max_value=1.0)

    profileRectCornerSegments = LongField(default_value=2, min_value=1, soft_max_value=5)

    profileRectCornerDepth = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)

    profileWaveAmplitude = DoubleLinearField(default_value=0.0, min_value=0.0, soft_max_value=0.5)

    profileWaveCycles = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)

    profileWaveOffset = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)

    profileWaveSegments = LongField(default_value=6, min_value=1, soft_max_value=40)

    patternEnable = BoolField(default_value=False)

    patternDistribution = PatternDistributionEnumField(default_value=0)

    patternNumberOfElements = LongField(default_value=5, min_value=0, soft_max_value=10)

    patternScaleElementsUniform = BoolField(default_value=True)

    patternScaleElementsX = FloatField(default_value=0.5, min_value=0.0, soft_max_value=1.0)

    patternScaleElementsY = FloatField(default_value=0.5, min_value=0.0, soft_max_value=1.0)

    patternAutomaticOrientation = BoolField(default_value=True)

    patternRotateElements = DoubleAngleField(default_value=0.0, min_value=-360.0, max_value=360.0)

    patternCoverage = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    alignProfileEnable = BoolField(default_value=False)

    alignProfileHorizontal = AlignProfileHorizontalEnumField(default_value=1)

    alignProfileVertical = AlignProfileVerticalEnumField(default_value=1)

    automaticRoll = BoolField(default_value=True)

    scaleProfileUniform = BoolField(default_value=True)

    scaleProfileX = FloatField(default_value=1.0, min_value=0.0, soft_max_value=5.0)

    scaleProfileY = FloatField(default_value=1.0, min_value=0.0, soft_max_value=5.0)

    rotateProfile = DoubleAngleField(default_value=0.0, min_value=-360.0, max_value=360.0)

    translateProfileX = DoubleLinearField(default_value=0.0, soft_min_value=-2.0, soft_max_value=2.0)

    translateProfileY = DoubleLinearField(default_value=0.0, soft_min_value=-2.0, soft_max_value=2.0)

    twist = FloatField(default_value=0.0, soft_min_value=-2.0, soft_max_value=2.0)

    taper = FloatField(default_value=1.0, min_value=0.0, soft_max_value=5.0)

    taperCurve = TaperCurveField(multi=True, default_value=(0.0, 0.0, 1.0))

    interpolationMode = InterpolationModeEnumField(default_value=0)

    interpolationPrecision = FloatField(default_value=75.0, min_value=0.0, max_value=100.0)

    interpolationSteps = LongField(default_value=20, min_value=1, soft_max_value=50)

    interpolationDistance = DoubleLinearField(default_value=0.0, min_value=0.01, soft_min_value=0.5, soft_max_value=10.0)

    interpolationOptimize = BoolField(default_value=False)

    normalsReverse = BoolField(default_value=False)

    normalsSmoothing = DoubleAngleField(default_value=59.99999999999999, min_value=0.0, max_value=180.0)

    createUVs = CreateUVsEnumField(default_value=2)

    capsEnable = BoolField(default_value=False)

    inCurveArray = DataNurbsCurveField(multi=True, readable=False)

    outMeshArray = DataMeshField(multi=True, writable=False)
