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

    sweepProfileType = SweepProfileTypeEnumField()

    customSweepProfileData = TypedField()

    profileArcAngle = DoubleAngleField()

    profileArcSegments = LongField()

    profilePolyType = ProfilePolyTypeEnumField()

    profilePolySides = LongField()

    profilePolyInnerRadius = FloatField()

    profileRectWidth = DoubleLinearField()

    profileRectHeight = DoubleLinearField()

    profileRectCornerRadius = DoubleLinearField()

    profileRectCornerSegments = LongField()

    profileRectCornerDepth = FloatField()

    profileWaveAmplitude = DoubleLinearField()

    profileWaveCycles = FloatField()

    profileWaveOffset = FloatField()

    profileWaveSegments = LongField()

    patternEnable = BoolField()

    patternDistribution = PatternDistributionEnumField()

    patternNumberOfElements = LongField()

    patternScaleElementsUniform = BoolField()

    patternScaleElementsX = FloatField()

    patternScaleElementsY = FloatField()

    patternAutomaticOrientation = BoolField()

    patternRotateElements = DoubleAngleField()

    patternCoverage = FloatField()

    alignProfileEnable = BoolField()

    alignProfileHorizontal = AlignProfileHorizontalEnumField()

    alignProfileVertical = AlignProfileVerticalEnumField()

    automaticRoll = BoolField()

    scaleProfileUniform = BoolField()

    scaleProfileX = FloatField()

    scaleProfileY = FloatField()

    rotateProfile = DoubleAngleField()

    translateProfileX = DoubleLinearField()

    translateProfileY = DoubleLinearField()

    twist = FloatField()

    taper = FloatField()

    taperCurve = TaperCurveField(multi=True)

    interpolationMode = InterpolationModeEnumField()

    interpolationPrecision = FloatField()

    interpolationSteps = LongField()

    interpolationDistance = DoubleLinearField()

    interpolationOptimize = BoolField()

    normalsReverse = BoolField()

    normalsSmoothing = DoubleAngleField()

    createUVs = CreateUVsEnumField()

    capsEnable = BoolField()

    inCurveArray = DataNurbsCurveField(multi=True)

    outMeshArray = DataMeshField(multi=True)
