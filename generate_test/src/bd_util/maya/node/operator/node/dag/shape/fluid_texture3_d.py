# coding: utf-8
from ._core import Shape
from ....attr.define.node_attr.fluid_texture3_d import (
    AiVolumeTextureField,
    AmbientColorField,
    BoundingBoxField,
    BoundingBoxScaleField,
    CenterField,
    CollisionDataField,
    CollisionDepthVelocityIncrementField,
    CollisionDepthVelocityMultiplierField,
    CollisionOffsetVelocityIncrementField,
    CollisionOffsetVelocityMultiplierField,
    ColorField,
    ColorSetField,
    CompInstObjGroupsField,
    ComponentTagsField,
    ControlPointsField,
    DefaultColorField,
    DimensionsField,
    DirectionalLightField,
    DrawOverrideField,
    DynamicOffsetField,
    EmissionListField,
    EnvironmentField,
    FarPointObjField,
    FarPointWorldField,
    FieldDataField,
    FieldListField,
    FilterSizeField,
    FluidLightColorField,
    GhostColorPostField,
    GhostColorPreField,
    GhostCustomStepsField,
    GhostOpacityRangeField,
    ImplodeCenterField,
    IncandescenceField,
    InputDataField,
    InstObjGroupsField,
    LightColorField,
    LightDataArrayField,
    ObjectColorRGBField,
    OpacityField,
    OutColorField,
    OutCoordField,
    OutGlowColorField,
    OutMatteOpacityField,
    OutTransparencyField,
    OutlinerColorField,
    PointLightField,
    PointObjField,
    PointWorldField,
    PublishedNodeInfoField,
    RefPointCameraField,
    RenderInfoField,
    RenderLayerInfoField,
    ResolutionField,
    SpecularColorField,
    SubVolumeCenterField,
    SubVolumeSizeField,
    TextureOriginField,
    TextureRotateField,
    TextureScaleField,
    TransparencyField,
    UvPivotField,
    UvSetField,
    VelocityScaleField,
    WireColorRGBField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.compound import CompoundField
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.char import CharField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.unit_scalar.time import TimeField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


class ViewModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FLAT = 0
    USE_TEMPLATE = 1
    GROUP_BY_NODE = 2


class ViewModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FLAT = 0
    USE_TEMPLATE = 1
    GROUP_BY_NODE = 2

    NAME_MAP = {
        FLAT: "Flat",
        USE_TEMPLATE: "Use Template",
        GROUP_BY_NODE: "Group By Node",
    }


class ViewModeEnumField(
    EnumField[ViewModeEnumAttrOperator, ViewModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ViewModeEnumAttrOperator
    PLUG_CLS = ViewModeEnumPlugOperator


class UiTreatmentEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    STANDARD = 0
    SHADER = 1
    CUSTOM = 1000


class UiTreatmentEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    STANDARD = 0
    SHADER = 1
    CUSTOM = 1000

    NAME_MAP = {
        STANDARD: "Standard",
        SHADER: "Shader",
        CUSTOM: "Custom",
    }


class UiTreatmentEnumField(
    EnumField[UiTreatmentEnumAttrOperator, UiTreatmentEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UiTreatmentEnumAttrOperator
    PLUG_CLS = UiTreatmentEnumPlugOperator


class UseObjectColorEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DEFAULT = 0
    INDEXED = 1
    RGB = 2


class UseObjectColorEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DEFAULT = 0
    INDEXED = 1
    RGB = 2

    NAME_MAP = {
        DEFAULT: "Default",
        INDEXED: "Indexed",
        RGB: "RGB",
    }


class UseObjectColorEnumField(
    EnumField[UseObjectColorEnumAttrOperator, UseObjectColorEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UseObjectColorEnumAttrOperator
    PLUG_CLS = UseObjectColorEnumPlugOperator


class GhostingModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PRE_AND_POST_FRAMES = 0
    PRE_FRAMES = 1
    POST_FRAMES = 2
    CUSTOM_FRAMES = 3
    PRE_AND_POST_KEYFRAMES = 4
    ALL_KEYFRAMES = 5


class GhostingModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PRE_AND_POST_FRAMES = 0
    PRE_FRAMES = 1
    POST_FRAMES = 2
    CUSTOM_FRAMES = 3
    PRE_AND_POST_KEYFRAMES = 4
    ALL_KEYFRAMES = 5

    NAME_MAP = {
        PRE_AND_POST_FRAMES: "Pre And Post Frames",
        PRE_FRAMES: "Pre Frames",
        POST_FRAMES: "Post Frames",
        CUSTOM_FRAMES: "Custom Frames",
        PRE_AND_POST_KEYFRAMES: "Pre And Post Keyframes",
        ALL_KEYFRAMES: "All Keyframes",
    }


class GhostingModeEnumField(
    EnumField[GhostingModeEnumAttrOperator, GhostingModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GhostingModeEnumAttrOperator
    PLUG_CLS = GhostingModeEnumPlugOperator


class VoxelQualityEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FASTER = 1
    BETTER = 2


class VoxelQualityEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FASTER = 1
    BETTER = 2

    NAME_MAP = {
        FASTER: "Faster",
        BETTER: "Better",
    }


class VoxelQualityEnumField(
    EnumField[VoxelQualityEnumAttrOperator, VoxelQualityEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VoxelQualityEnumAttrOperator
    PLUG_CLS = VoxelQualityEnumPlugOperator


class BoundaryDrawEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BOTTOM = 0
    REDUCED = 1
    OUTLINE = 2
    FULL = 3
    BOUNDING_BOX = 4
    NONE = 5


class BoundaryDrawEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BOTTOM = 0
    REDUCED = 1
    OUTLINE = 2
    FULL = 3
    BOUNDING_BOX = 4
    NONE = 5

    NAME_MAP = {
        BOTTOM: "Bottom",
        REDUCED: "Reduced",
        OUTLINE: "Outline",
        FULL: "Full",
        BOUNDING_BOX: "Bounding box",
        NONE: "None",
    }


class BoundaryDrawEnumField(
    EnumField[BoundaryDrawEnumAttrOperator, BoundaryDrawEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoundaryDrawEnumAttrOperator
    PLUG_CLS = BoundaryDrawEnumPlugOperator


class ShadedDisplayEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AS_RENDER = 1
    DENSITY = 2
    TEMPERATURE = 3
    FUEL = 4
    COLLISION = 5
    DENSITY_AND_COLOR = 6
    DENSITY_AND_TEMP = 7
    DENSITY_AND_FUEL = 8
    DENSITY_AND_COLLISION = 9
    FALLOFF = 10


class ShadedDisplayEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AS_RENDER = 1
    DENSITY = 2
    TEMPERATURE = 3
    FUEL = 4
    COLLISION = 5
    DENSITY_AND_COLOR = 6
    DENSITY_AND_TEMP = 7
    DENSITY_AND_FUEL = 8
    DENSITY_AND_COLLISION = 9
    FALLOFF = 10

    NAME_MAP = {
        OFF: "Off",
        AS_RENDER: "As Render",
        DENSITY: "Density",
        TEMPERATURE: "Temperature",
        FUEL: "Fuel",
        COLLISION: "Collision",
        DENSITY_AND_COLOR: "Density And Color",
        DENSITY_AND_TEMP: "Density And Temp",
        DENSITY_AND_FUEL: "Density And Fuel",
        DENSITY_AND_COLLISION: "Density And Collision",
        FALLOFF: "Falloff",
    }


class ShadedDisplayEnumField(
    EnumField[ShadedDisplayEnumAttrOperator, ShadedDisplayEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShadedDisplayEnumAttrOperator
    PLUG_CLS = ShadedDisplayEnumPlugOperator


class WireframeDisplayEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    RECTANGLES = 1
    PARTICLES = 2


class WireframeDisplayEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    RECTANGLES = 1
    PARTICLES = 2

    NAME_MAP = {
        OFF: "Off",
        RECTANGLES: "Rectangles",
        PARTICLES: "Particles",
    }


class WireframeDisplayEnumField(
    EnumField[WireframeDisplayEnumAttrOperator, WireframeDisplayEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WireframeDisplayEnumAttrOperator
    PLUG_CLS = WireframeDisplayEnumPlugOperator


class NumericDisplayEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    DENSITY = 1
    TEMPERATURE = 2
    FUEL = 6


class NumericDisplayEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    DENSITY = 1
    TEMPERATURE = 2
    FUEL = 6

    NAME_MAP = {
        OFF: "Off",
        DENSITY: "Density",
        TEMPERATURE: "Temperature",
        FUEL: "Fuel",
    }


class NumericDisplayEnumField(
    EnumField[NumericDisplayEnumAttrOperator, NumericDisplayEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NumericDisplayEnumAttrOperator
    PLUG_CLS = NumericDisplayEnumPlugOperator


class CoordinateMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FIXED = 0
    GRID = 1


class CoordinateMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FIXED = 0
    GRID = 1

    NAME_MAP = {
        FIXED: "Fixed",
        GRID: "Grid",
    }


class CoordinateMethodEnumField(
    EnumField[CoordinateMethodEnumAttrOperator, CoordinateMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoordinateMethodEnumAttrOperator
    PLUG_CLS = CoordinateMethodEnumPlugOperator


class GridInterpolatorEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 0
    HERMITE = 2


class GridInterpolatorEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LINEAR = 0
    HERMITE = 2

    NAME_MAP = {
        LINEAR: "linear",
        HERMITE: "hermite",
    }


class GridInterpolatorEnumField(
    EnumField[GridInterpolatorEnumAttrOperator, GridInterpolatorEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GridInterpolatorEnumAttrOperator
    PLUG_CLS = GridInterpolatorEnumPlugOperator


class SolverEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    NAVIER_MINUS_STOKES = 1
    SPRING_MESH = 2


class SolverEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    NAVIER_MINUS_STOKES = 1
    SPRING_MESH = 2

    NAME_MAP = {
        NONE: "none",
        NAVIER_MINUS_STOKES: "Navier-Stokes",
        SPRING_MESH: "Spring Mesh",
    }


class SolverEnumField(
    EnumField[SolverEnumAttrOperator, SolverEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SolverEnumAttrOperator
    PLUG_CLS = SolverEnumPlugOperator


class HighDetailSolveEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ALL_GRIDS_EXCEPT_VELOCITY = 1
    VELOCITY_ONLY = 2
    ALL_GRIDS = 3


class HighDetailSolveEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ALL_GRIDS_EXCEPT_VELOCITY = 1
    VELOCITY_ONLY = 2
    ALL_GRIDS = 3

    NAME_MAP = {
        OFF: "Off",
        ALL_GRIDS_EXCEPT_VELOCITY: "All Grids Except Velocity",
        VELOCITY_ONLY: "Velocity Only",
        ALL_GRIDS: "All Grids",
    }


class HighDetailSolveEnumField(
    EnumField[HighDetailSolveEnumAttrOperator, HighDetailSolveEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HighDetailSolveEnumAttrOperator
    PLUG_CLS = HighDetailSolveEnumPlugOperator


class LiquidMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LIQUID_AND_AIR = 1
    DENSITY_BASED_MASS = 2


class LiquidMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LIQUID_AND_AIR = 1
    DENSITY_BASED_MASS = 2

    NAME_MAP = {
        LIQUID_AND_AIR: "Liquid and Air",
        DENSITY_BASED_MASS: "Density Based Mass",
    }


class LiquidMethodEnumField(
    EnumField[LiquidMethodEnumAttrOperator, LiquidMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LiquidMethodEnumAttrOperator
    PLUG_CLS = LiquidMethodEnumPlugOperator


class BoundaryXEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    BOTH_SIDES = 1
    MINUS_X_SIDE = 2
    X_SIDE = 3
    WRAPPING = 4


class BoundaryXEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    BOTH_SIDES = 1
    MINUS_X_SIDE = 2
    X_SIDE = 3
    WRAPPING = 4

    NAME_MAP = {
        NONE: "None",
        BOTH_SIDES: "Both Sides",
        MINUS_X_SIDE: "-X Side",
        X_SIDE: "X Side",
        WRAPPING: "Wrapping",
    }


class BoundaryXEnumField(
    EnumField[BoundaryXEnumAttrOperator, BoundaryXEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoundaryXEnumAttrOperator
    PLUG_CLS = BoundaryXEnumPlugOperator


class BoundaryYEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    BOTH_SIDES = 1
    MINUS_Y_SIDE = 2
    Y_SIDE = 3
    WRAPPING = 4


class BoundaryYEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    BOTH_SIDES = 1
    MINUS_Y_SIDE = 2
    Y_SIDE = 3
    WRAPPING = 4

    NAME_MAP = {
        NONE: "None",
        BOTH_SIDES: "Both Sides",
        MINUS_Y_SIDE: "-Y Side",
        Y_SIDE: "Y Side",
        WRAPPING: "Wrapping",
    }


class BoundaryYEnumField(
    EnumField[BoundaryYEnumAttrOperator, BoundaryYEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoundaryYEnumAttrOperator
    PLUG_CLS = BoundaryYEnumPlugOperator


class BoundaryZEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    BOTH_SIDES = 1
    MINUS_Z_SIDE = 2
    Z_SIDE = 3
    WRAPPING = 4


class BoundaryZEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    BOTH_SIDES = 1
    MINUS_Z_SIDE = 2
    Z_SIDE = 3
    WRAPPING = 4

    NAME_MAP = {
        NONE: "None",
        BOTH_SIDES: "Both Sides",
        MINUS_Z_SIDE: "-Z Side",
        Z_SIDE: "Z Side",
        WRAPPING: "Wrapping",
    }


class BoundaryZEnumField(
    EnumField[BoundaryZEnumAttrOperator, BoundaryZEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoundaryZEnumAttrOperator
    PLUG_CLS = BoundaryZEnumPlugOperator


class FalloffMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF_ZERO = 0
    STATIC_GRID = 1


class FalloffMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF_ZERO = 0
    STATIC_GRID = 1

    NAME_MAP = {
        OFF_ZERO: "Off(zero)",
        STATIC_GRID: "Static Grid",
    }


class FalloffMethodEnumField(
    EnumField[FalloffMethodEnumAttrOperator, FalloffMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffMethodEnumAttrOperator
    PLUG_CLS = FalloffMethodEnumPlugOperator


class DensityMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF_ZERO = 0
    STATIC_GRID = 1
    DYNAMIC_GRID = 2
    GRADIENT = 3


class DensityMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF_ZERO = 0
    STATIC_GRID = 1
    DYNAMIC_GRID = 2
    GRADIENT = 3

    NAME_MAP = {
        OFF_ZERO: "Off(zero)",
        STATIC_GRID: "Static Grid",
        DYNAMIC_GRID: "Dynamic Grid",
        GRADIENT: "Gradient",
    }


class DensityMethodEnumField(
    EnumField[DensityMethodEnumAttrOperator, DensityMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DensityMethodEnumAttrOperator
    PLUG_CLS = DensityMethodEnumPlugOperator


class DensityGradientEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONSTANT = 4
    X_GRADIENT = 5
    Y_GRADIENT = 6
    Z_GRADIENT = 7
    MINUS_X_GRADIENT = 8
    MINUS_Y_GRADIENT = 9
    MINUS_Z_GRADIENT = 10
    CENTER_GRADIENT = 11


class DensityGradientEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONSTANT = 4
    X_GRADIENT = 5
    Y_GRADIENT = 6
    Z_GRADIENT = 7
    MINUS_X_GRADIENT = 8
    MINUS_Y_GRADIENT = 9
    MINUS_Z_GRADIENT = 10
    CENTER_GRADIENT = 11

    NAME_MAP = {
        CONSTANT: "Constant",
        X_GRADIENT: "X Gradient",
        Y_GRADIENT: "Y Gradient",
        Z_GRADIENT: "Z Gradient",
        MINUS_X_GRADIENT: "-X Gradient",
        MINUS_Y_GRADIENT: "-Y Gradient",
        MINUS_Z_GRADIENT: "-Z Gradient",
        CENTER_GRADIENT: "Center Gradient",
    }


class DensityGradientEnumField(
    EnumField[DensityGradientEnumAttrOperator, DensityGradientEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DensityGradientEnumAttrOperator
    PLUG_CLS = DensityGradientEnumPlugOperator


class SelfForceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF_ZERO = 0
    DENSITY = 1
    TEMPERATURE = 2


class SelfForceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF_ZERO = 0
    DENSITY = 1
    TEMPERATURE = 2

    NAME_MAP = {
        OFF_ZERO: "Off(zero)",
        DENSITY: "Density",
        TEMPERATURE: "Temperature",
    }


class SelfForceEnumField(
    EnumField[SelfForceEnumAttrOperator, SelfForceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SelfForceEnumAttrOperator
    PLUG_CLS = SelfForceEnumPlugOperator


class VelocityMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF_ZERO = 0
    STATIC_GRID = 1
    DYNAMIC_GRID = 2
    GRADIENT = 3


class VelocityMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF_ZERO = 0
    STATIC_GRID = 1
    DYNAMIC_GRID = 2
    GRADIENT = 3

    NAME_MAP = {
        OFF_ZERO: "Off(zero)",
        STATIC_GRID: "Static Grid",
        DYNAMIC_GRID: "Dynamic Grid",
        GRADIENT: "Gradient",
    }


class VelocityMethodEnumField(
    EnumField[VelocityMethodEnumAttrOperator, VelocityMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VelocityMethodEnumAttrOperator
    PLUG_CLS = VelocityMethodEnumPlugOperator


class VelocityGradientEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONSTANT = 4
    X_GRADIENT = 5
    Y_GRADIENT = 6
    Z_GRADIENT = 7
    MINUS_X_GRADIENT = 8
    MINUS_Y_GRADIENT = 9
    MINUS_Z_GRADIENT = 10
    CENTER_GRADIENT = 11


class VelocityGradientEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONSTANT = 4
    X_GRADIENT = 5
    Y_GRADIENT = 6
    Z_GRADIENT = 7
    MINUS_X_GRADIENT = 8
    MINUS_Y_GRADIENT = 9
    MINUS_Z_GRADIENT = 10
    CENTER_GRADIENT = 11

    NAME_MAP = {
        CONSTANT: "Constant",
        X_GRADIENT: "X Gradient",
        Y_GRADIENT: "Y Gradient",
        Z_GRADIENT: "Z Gradient",
        MINUS_X_GRADIENT: "-X Gradient",
        MINUS_Y_GRADIENT: "-Y Gradient",
        MINUS_Z_GRADIENT: "-Z Gradient",
        CENTER_GRADIENT: "Center Gradient",
    }


class VelocityGradientEnumField(
    EnumField[VelocityGradientEnumAttrOperator, VelocityGradientEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VelocityGradientEnumAttrOperator
    PLUG_CLS = VelocityGradientEnumPlugOperator


class TemperatureMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF_ZERO = 0
    STATIC_GRID = 1
    DYNAMIC_GRID = 2
    GRADIENT = 3


class TemperatureMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF_ZERO = 0
    STATIC_GRID = 1
    DYNAMIC_GRID = 2
    GRADIENT = 3

    NAME_MAP = {
        OFF_ZERO: "Off(zero)",
        STATIC_GRID: "Static Grid",
        DYNAMIC_GRID: "Dynamic Grid",
        GRADIENT: "Gradient",
    }


class TemperatureMethodEnumField(
    EnumField[TemperatureMethodEnumAttrOperator, TemperatureMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TemperatureMethodEnumAttrOperator
    PLUG_CLS = TemperatureMethodEnumPlugOperator


class TemperatureGradientEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONSTANT = 4
    X_GRADIENT = 5
    Y_GRADIENT = 6
    Z_GRADIENT = 7
    MINUS_X_GRADIENT = 8
    MINUS_Y_GRADIENT = 9
    MINUS_Z_GRADIENT = 10
    CENTER_GRADIENT = 11


class TemperatureGradientEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONSTANT = 4
    X_GRADIENT = 5
    Y_GRADIENT = 6
    Z_GRADIENT = 7
    MINUS_X_GRADIENT = 8
    MINUS_Y_GRADIENT = 9
    MINUS_Z_GRADIENT = 10
    CENTER_GRADIENT = 11

    NAME_MAP = {
        CONSTANT: "Constant",
        X_GRADIENT: "X Gradient",
        Y_GRADIENT: "Y Gradient",
        Z_GRADIENT: "Z Gradient",
        MINUS_X_GRADIENT: "-X Gradient",
        MINUS_Y_GRADIENT: "-Y Gradient",
        MINUS_Z_GRADIENT: "-Z Gradient",
        CENTER_GRADIENT: "Center Gradient",
    }


class TemperatureGradientEnumField(
    EnumField[TemperatureGradientEnumAttrOperator, TemperatureGradientEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TemperatureGradientEnumAttrOperator
    PLUG_CLS = TemperatureGradientEnumPlugOperator


class ColorMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    USE_SHADING_COLOR = 0
    STATIC_GRID = 1
    DYNAMIC_GRID = 2


class ColorMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    USE_SHADING_COLOR = 0
    STATIC_GRID = 1
    DYNAMIC_GRID = 2

    NAME_MAP = {
        USE_SHADING_COLOR: "Use Shading Color",
        STATIC_GRID: "Static Grid",
        DYNAMIC_GRID: "Dynamic Grid",
    }


class ColorMethodEnumField(
    EnumField[ColorMethodEnumAttrOperator, ColorMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorMethodEnumAttrOperator
    PLUG_CLS = ColorMethodEnumPlugOperator


class FuelMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF_ZERO = 0
    DYNAMIC_GRID = 2
    GRADIENT = 3


class FuelMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF_ZERO = 0
    DYNAMIC_GRID = 2
    GRADIENT = 3

    NAME_MAP = {
        OFF_ZERO: "Off(zero)",
        DYNAMIC_GRID: "Dynamic Grid",
        GRADIENT: "Gradient",
    }


class FuelMethodEnumField(
    EnumField[FuelMethodEnumAttrOperator, FuelMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FuelMethodEnumAttrOperator
    PLUG_CLS = FuelMethodEnumPlugOperator


class FuelGradientEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONSTANT = 4
    X_GRADIENT = 5
    Y_GRADIENT = 6
    Z_GRADIENT = 7
    MINUS_X_GRADIENT = 8
    MINUS_Y_GRADIENT = 9
    MINUS_Z_GRADIENT = 10
    CENTER_GRADIENT = 11


class FuelGradientEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONSTANT = 4
    X_GRADIENT = 5
    Y_GRADIENT = 6
    Z_GRADIENT = 7
    MINUS_X_GRADIENT = 8
    MINUS_Y_GRADIENT = 9
    MINUS_Z_GRADIENT = 10
    CENTER_GRADIENT = 11

    NAME_MAP = {
        CONSTANT: "Constant",
        X_GRADIENT: "X Gradient",
        Y_GRADIENT: "Y Gradient",
        Z_GRADIENT: "Z Gradient",
        MINUS_X_GRADIENT: "-X Gradient",
        MINUS_Y_GRADIENT: "-Y Gradient",
        MINUS_Z_GRADIENT: "-Z Gradient",
        CENTER_GRADIENT: "Center Gradient",
    }


class FuelGradientEnumField(
    EnumField[FuelGradientEnumAttrOperator, FuelGradientEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FuelGradientEnumAttrOperator
    PLUG_CLS = FuelGradientEnumPlugOperator


class MatteOpacityModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BLACK_HOLE = 0
    SOLID_MATTE = 1
    OPACITY_GAIN = 2


class MatteOpacityModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BLACK_HOLE = 0
    SOLID_MATTE = 1
    OPACITY_GAIN = 2

    NAME_MAP = {
        BLACK_HOLE: "Black Hole",
        SOLID_MATTE: "Solid Matte",
        OPACITY_GAIN: "Opacity Gain",
    }


class MatteOpacityModeEnumField(
    EnumField[MatteOpacityModeEnumAttrOperator, MatteOpacityModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MatteOpacityModeEnumAttrOperator
    PLUG_CLS = MatteOpacityModeEnumPlugOperator


class RenderInterpolatorEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 0
    SMOOTH = 3


class RenderInterpolatorEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LINEAR = 0
    SMOOTH = 3

    NAME_MAP = {
        LINEAR: "linear",
        SMOOTH: "smooth",
    }


class RenderInterpolatorEnumField(
    EnumField[RenderInterpolatorEnumAttrOperator, RenderInterpolatorEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RenderInterpolatorEnumAttrOperator
    PLUG_CLS = RenderInterpolatorEnumPlugOperator


class ColorInputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONSTANT = 0
    X_GRADIENT = 1
    Y_GRADIENT = 2
    Z_GRADIENT = 3
    CENTER_GRADIENT = 4
    DENSITY = 5
    TEMPERATURE = 6
    FUEL = 7
    PRESSURE = 8
    SPEED = 9
    DENSITY_AND_FUEL = 10


class ColorInputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONSTANT = 0
    X_GRADIENT = 1
    Y_GRADIENT = 2
    Z_GRADIENT = 3
    CENTER_GRADIENT = 4
    DENSITY = 5
    TEMPERATURE = 6
    FUEL = 7
    PRESSURE = 8
    SPEED = 9
    DENSITY_AND_FUEL = 10

    NAME_MAP = {
        CONSTANT: "Constant",
        X_GRADIENT: "X Gradient",
        Y_GRADIENT: "Y Gradient",
        Z_GRADIENT: "Z Gradient",
        CENTER_GRADIENT: "Center Gradient",
        DENSITY: "Density",
        TEMPERATURE: "Temperature",
        FUEL: "Fuel",
        PRESSURE: "Pressure",
        SPEED: "Speed",
        DENSITY_AND_FUEL: "Density And Fuel",
    }


class ColorInputEnumField(
    EnumField[ColorInputEnumAttrOperator, ColorInputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorInputEnumAttrOperator
    PLUG_CLS = ColorInputEnumPlugOperator


class OpacityInputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONSTANT = 0
    X_GRADIENT = 1
    Y_GRADIENT = 2
    Z_GRADIENT = 3
    CENTER_GRADIENT = 4
    DENSITY = 5
    TEMPERATURE = 6
    FUEL = 7
    PRESSURE = 8
    SPEED = 9
    DENSITY_AND_FUEL = 10


class OpacityInputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONSTANT = 0
    X_GRADIENT = 1
    Y_GRADIENT = 2
    Z_GRADIENT = 3
    CENTER_GRADIENT = 4
    DENSITY = 5
    TEMPERATURE = 6
    FUEL = 7
    PRESSURE = 8
    SPEED = 9
    DENSITY_AND_FUEL = 10

    NAME_MAP = {
        CONSTANT: "Constant",
        X_GRADIENT: "X Gradient",
        Y_GRADIENT: "Y Gradient",
        Z_GRADIENT: "Z Gradient",
        CENTER_GRADIENT: "Center Gradient",
        DENSITY: "Density",
        TEMPERATURE: "Temperature",
        FUEL: "Fuel",
        PRESSURE: "Pressure",
        SPEED: "Speed",
        DENSITY_AND_FUEL: "Density And Fuel",
    }


class OpacityInputEnumField(
    EnumField[OpacityInputEnumAttrOperator, OpacityInputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OpacityInputEnumAttrOperator
    PLUG_CLS = OpacityInputEnumPlugOperator


class LightTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DIAGONAL = 0
    DIRECTIONAL = 1
    POINT = 2


class LightTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DIAGONAL = 0
    DIRECTIONAL = 1
    POINT = 2

    NAME_MAP = {
        DIAGONAL: "Diagonal",
        DIRECTIONAL: "Directional",
        POINT: "Point",
    }


class LightTypeEnumField(
    EnumField[LightTypeEnumAttrOperator, LightTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightTypeEnumAttrOperator
    PLUG_CLS = LightTypeEnumPlugOperator


class PointLightDecayEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NO_DECAY = 0
    LINEAR = 1
    QUADRATIC = 2
    CUBIC = 3


class PointLightDecayEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NO_DECAY = 0
    LINEAR = 1
    QUADRATIC = 2
    CUBIC = 3

    NAME_MAP = {
        NO_DECAY: "No Decay",
        LINEAR: "Linear",
        QUADRATIC: "Quadratic",
        CUBIC: "Cubic",
    }


class PointLightDecayEnumField(
    EnumField[PointLightDecayEnumAttrOperator, PointLightDecayEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointLightDecayEnumAttrOperator
    PLUG_CLS = PointLightDecayEnumPlugOperator


class IncandescenceInputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONSTANT = 0
    X_GRADIENT = 1
    Y_GRADIENT = 2
    Z_GRADIENT = 3
    CENTER_GRADIENT = 4
    DENSITY = 5
    TEMPERATURE = 6
    FUEL = 7
    PRESSURE = 8
    SPEED = 9
    DENSITY_AND_FUEL = 10


class IncandescenceInputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONSTANT = 0
    X_GRADIENT = 1
    Y_GRADIENT = 2
    Z_GRADIENT = 3
    CENTER_GRADIENT = 4
    DENSITY = 5
    TEMPERATURE = 6
    FUEL = 7
    PRESSURE = 8
    SPEED = 9
    DENSITY_AND_FUEL = 10

    NAME_MAP = {
        CONSTANT: "Constant",
        X_GRADIENT: "X Gradient",
        Y_GRADIENT: "Y Gradient",
        Z_GRADIENT: "Z Gradient",
        CENTER_GRADIENT: "Center Gradient",
        DENSITY: "Density",
        TEMPERATURE: "Temperature",
        FUEL: "Fuel",
        PRESSURE: "Pressure",
        SPEED: "Speed",
        DENSITY_AND_FUEL: "Density And Fuel",
    }


class IncandescenceInputEnumField(
    EnumField[IncandescenceInputEnumAttrOperator, IncandescenceInputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IncandescenceInputEnumAttrOperator
    PLUG_CLS = IncandescenceInputEnumPlugOperator


class DropoffShapeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    SPHERE = 1
    CUBE = 2
    CONE = 3
    DOUBLE_CONE = 4
    X_GRADIENT = 5
    Y_GRADIENT = 6
    Z_GRADIENT = 7
    MINUS_X_GRADIENT = 8
    MINUS_Y_GRADIENT = 9
    MINUS_Z_GRADIENT = 10
    USE_FALLOFF_GRID = 12


class DropoffShapeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    SPHERE = 1
    CUBE = 2
    CONE = 3
    DOUBLE_CONE = 4
    X_GRADIENT = 5
    Y_GRADIENT = 6
    Z_GRADIENT = 7
    MINUS_X_GRADIENT = 8
    MINUS_Y_GRADIENT = 9
    MINUS_Z_GRADIENT = 10
    USE_FALLOFF_GRID = 12

    NAME_MAP = {
        OFF: "Off",
        SPHERE: "Sphere",
        CUBE: "Cube",
        CONE: "Cone",
        DOUBLE_CONE: "Double Cone",
        X_GRADIENT: "X Gradient",
        Y_GRADIENT: "Y Gradient",
        Z_GRADIENT: "Z Gradient",
        MINUS_X_GRADIENT: "-X Gradient",
        MINUS_Y_GRADIENT: "-Y Gradient",
        MINUS_Z_GRADIENT: "-Z Gradient",
        USE_FALLOFF_GRID: "Use Falloff Grid",
    }


class DropoffShapeEnumField(
    EnumField[DropoffShapeEnumAttrOperator, DropoffShapeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DropoffShapeEnumAttrOperator
    PLUG_CLS = DropoffShapeEnumPlugOperator


class MeshMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TRIANGLE_MESH = 0
    QUAD_MESH = 1
    TETRAHEDRA = 2
    ACUTE_TETRAHEDRA = 3


class MeshMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TRIANGLE_MESH = 0
    QUAD_MESH = 1
    TETRAHEDRA = 2
    ACUTE_TETRAHEDRA = 3

    NAME_MAP = {
        TRIANGLE_MESH: "Triangle Mesh",
        QUAD_MESH: "Quad Mesh",
        TETRAHEDRA: "Tetrahedra",
        ACUTE_TETRAHEDRA: "Acute Tetrahedra",
    }


class MeshMethodEnumField(
    EnumField[MeshMethodEnumAttrOperator, MeshMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MeshMethodEnumAttrOperator
    PLUG_CLS = MeshMethodEnumPlugOperator


class SampleMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UNIFORM = 0
    JITTERED = 1
    ADAPTIVE = 2
    ADAPTIVEJITTERED = 3


class SampleMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    UNIFORM = 0
    JITTERED = 1
    ADAPTIVE = 2
    ADAPTIVEJITTERED = 3

    NAME_MAP = {
        UNIFORM: "Uniform",
        JITTERED: "Jittered",
        ADAPTIVE: "Adaptive",
        ADAPTIVEJITTERED: "AdaptiveJittered",
    }


class SampleMethodEnumField(
    EnumField[SampleMethodEnumAttrOperator, SampleMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SampleMethodEnumAttrOperator
    PLUG_CLS = SampleMethodEnumPlugOperator


class TextureTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PERLIN_NOISE = 0
    BILLOW = 1
    VOLUME_WAVE = 2
    WISPY = 3
    SPACETIME = 4
    MANDELBROT = 5


class TextureTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PERLIN_NOISE = 0
    BILLOW = 1
    VOLUME_WAVE = 2
    WISPY = 3
    SPACETIME = 4
    MANDELBROT = 5

    NAME_MAP = {
        PERLIN_NOISE: "Perlin Noise",
        BILLOW: "Billow",
        VOLUME_WAVE: "Volume Wave",
        WISPY: "Wispy",
        SPACETIME: "SpaceTime",
        MANDELBROT: "Mandelbrot",
    }


class TextureTypeEnumField(
    EnumField[TextureTypeEnumAttrOperator, TextureTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TextureTypeEnumAttrOperator
    PLUG_CLS = TextureTypeEnumPlugOperator


class FalloffEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 0
    SMOOTH = 1
    FAST = 2
    BUBBLE = 3


class FalloffEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LINEAR = 0
    SMOOTH = 1
    FAST = 2
    BUBBLE = 3

    NAME_MAP = {
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        FAST: "Fast",
        BUBBLE: "Bubble",
    }


class FalloffEnumField(
    EnumField[FalloffEnumAttrOperator, FalloffEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffEnumAttrOperator
    PLUG_CLS = FalloffEnumPlugOperator


class MandelbrotTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    JULIA_SET = 0
    MANDELBROT_SET = 1
    MANDELBOX = 2
    BOX_WITH_JULIA_SET = 3
    BOX_WITH_MANDELBROT_SET = 4


class MandelbrotTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    JULIA_SET = 0
    MANDELBROT_SET = 1
    MANDELBOX = 2
    BOX_WITH_JULIA_SET = 3
    BOX_WITH_MANDELBROT_SET = 4

    NAME_MAP = {
        JULIA_SET: "Julia Set",
        MANDELBROT_SET: "Mandelbrot Set",
        MANDELBOX: "Mandelbox",
        BOX_WITH_JULIA_SET: "Box with Julia Set",
        BOX_WITH_MANDELBROT_SET: "Box with Mandelbrot Set",
    }


class MandelbrotTypeEnumField(
    EnumField[MandelbrotTypeEnumAttrOperator, MandelbrotTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MandelbrotTypeEnumAttrOperator
    PLUG_CLS = MandelbrotTypeEnumPlugOperator


class MandelbrotShadeMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CLASSIC = 0
    SMOOTH = 1
    MINIMUM_RADIUS = 2
    ESCAPE_RADIUS = 3
    LINES_ONLY = 4


class MandelbrotShadeMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CLASSIC = 0
    SMOOTH = 1
    MINIMUM_RADIUS = 2
    ESCAPE_RADIUS = 3
    LINES_ONLY = 4

    NAME_MAP = {
        CLASSIC: "Classic",
        SMOOTH: "Smooth",
        MINIMUM_RADIUS: "Minimum Radius",
        ESCAPE_RADIUS: "Escape Radius",
        LINES_ONLY: "Lines Only",
    }


class MandelbrotShadeMethodEnumField(
    EnumField[MandelbrotShadeMethodEnumAttrOperator, MandelbrotShadeMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MandelbrotShadeMethodEnumAttrOperator
    PLUG_CLS = MandelbrotShadeMethodEnumPlugOperator


class MandelbrotInsideMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ZERO = 0
    MAX_ITERATION = 1
    SHADED_INSIDE = 2
    SHADED_WITHOUT_LINES = 3
    LINES = 4
    INNER_LINES_ONLY = 5


class MandelbrotInsideMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ZERO = 0
    MAX_ITERATION = 1
    SHADED_INSIDE = 2
    SHADED_WITHOUT_LINES = 3
    LINES = 4
    INNER_LINES_ONLY = 5

    NAME_MAP = {
        ZERO: "Zero",
        MAX_ITERATION: "Max Iteration",
        SHADED_INSIDE: "Shaded Inside",
        SHADED_WITHOUT_LINES: "Shaded Without Lines",
        LINES: "Lines",
        INNER_LINES_ONLY: "Inner Lines Only",
    }


class MandelbrotInsideMethodEnumField(
    EnumField[MandelbrotInsideMethodEnumAttrOperator, MandelbrotInsideMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MandelbrotInsideMethodEnumAttrOperator
    PLUG_CLS = MandelbrotInsideMethodEnumPlugOperator


class AiTextureCoordinateMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FIXED = 0
    GRID = 1


class AiTextureCoordinateMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FIXED = 0
    GRID = 1

    NAME_MAP = {
        FIXED: "Fixed",
        GRID: "Grid",
    }


class AiTextureCoordinateMethodEnumField(
    EnumField[AiTextureCoordinateMethodEnumAttrOperator, AiTextureCoordinateMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiTextureCoordinateMethodEnumAttrOperator
    PLUG_CLS = AiTextureCoordinateMethodEnumPlugOperator


class AiFilterTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CLOSEST = 0
    LINEAR = 1
    CUBIC = 2


class AiFilterTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CLOSEST = 0
    LINEAR = 1
    CUBIC = 2

    NAME_MAP = {
        CLOSEST: "Closest",
        LINEAR: "Linear",
        CUBIC: "Cubic",
    }


class AiFilterTypeEnumField(
    EnumField[AiFilterTypeEnumAttrOperator, AiFilterTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiFilterTypeEnumAttrOperator
    PLUG_CLS = AiFilterTypeEnumPlugOperator


class FluidTexture3D(Shape):
    __slots__ = ()

    NODE_TYPE = "fluidTexture3D"

    hyperLayout = MessageField()
    hl = hyperLayout

    isCollapsed = BoolField(default_value=False)
    isc = isCollapsed

    blackBox = BoolField(default_value=False)
    bbx = blackBox

    borderConnections = MessageField(multi=True)
    boc = borderConnections

    isHierarchicalConnection = BoolField(multi=True, default_value=False)
    ish = isHierarchicalConnection

    publishedNodeInfo = PublishedNodeInfoField(multi=True)
    pni = publishedNodeInfo

    rmbCommand = DataStringField()
    rmc = rmbCommand

    templateName = DataStringField()
    tna = templateName

    templatePath = DataStringField()
    tpt = templatePath

    viewName = DataStringField()
    vwn = viewName

    iconName = DataStringField()
    icn = iconName

    viewMode = ViewModeEnumField(default_value=2)
    vwm = viewMode

    templateVersion = LongField(default_value=0)
    tpv = templateVersion

    uiTreatment = UiTreatmentEnumField(default_value=0)
    uit = uiTreatment

    customTreatment = DataStringField()
    ctrt = customTreatment

    creator = DataStringField()
    ctor = creator

    creationDate = DataStringField()
    cdat = creationDate

    containerType = DataStringField()
    ctyp = containerType

    boundingBox = BoundingBoxField(writable=False)
    bb = boundingBox
    boundingBoxMin = boundingBox.boundingBoxMin
    bbmn = boundingBoxMin
    boundingBoxMax = boundingBox.boundingBoxMax
    bbmx = boundingBoxMax
    boundingBoxSize = boundingBox.boundingBoxSize
    bbsi = boundingBoxSize

    center = CenterField(default_value=(0.0, 0.0, 0.0), writable=False)
    c = center
    boundingBoxCenterX = center.boundingBoxCenterX
    bcx = boundingBoxCenterX
    boundingBoxCenterY = center.boundingBoxCenterY
    bcy = boundingBoxCenterY
    boundingBoxCenterZ = center.boundingBoxCenterZ
    bcz = boundingBoxCenterZ

    matrix = DataMatrixField(writable=False)
    m = matrix

    inverseMatrix = DataMatrixField(writable=False)
    im = inverseMatrix

    worldMatrix = DataMatrixField(multi=True, writable=False)
    wm = worldMatrix

    worldInverseMatrix = DataMatrixField(multi=True, writable=False)
    wim = worldInverseMatrix

    parentMatrix = DataMatrixField(multi=True, writable=False)
    pm = parentMatrix

    parentInverseMatrix = DataMatrixField(multi=True, writable=False)
    pim = parentInverseMatrix

    visibility = BoolField(default_value=True)
    v = visibility

    intermediateObject = BoolField(default_value=False)
    io = intermediateObject

    template = BoolField(default_value=False)
    tmp = template

    instObjGroups = InstObjGroupsField(multi=True)
    iog = instObjGroups

    objectColorRGB = ObjectColorRGBField(default_value=(0.0, 0.0, 0.0))
    obcc = objectColorRGB
    objectColorR = objectColorRGB.objectColorR
    obcr = objectColorR
    objectColorG = objectColorRGB.objectColorG
    obcg = objectColorG
    objectColorB = objectColorRGB.objectColorB
    obcb = objectColorB

    wireColorRGB = WireColorRGBField(default_value=(0.0, 0.0, 0.0))
    wfcc = wireColorRGB
    wireColorR = wireColorRGB.wireColorR
    wfcr = wireColorR
    wireColorG = wireColorRGB.wireColorG
    wfcg = wireColorG
    wireColorB = wireColorRGB.wireColorB
    wfcb = wireColorB

    useObjectColor = UseObjectColorEnumField(default_value=0)
    uoc = useObjectColor

    objectColor = ShortField(default_value=0, min_value=0, max_value=7)
    oc = objectColor

    drawOverride = DrawOverrideField()
    do = drawOverride
    overrideDisplayType = drawOverride.overrideDisplayType
    ovdt = overrideDisplayType
    overrideLevelOfDetail = drawOverride.overrideLevelOfDetail
    ovlod = overrideLevelOfDetail
    overrideShading = drawOverride.overrideShading
    ovs = overrideShading
    overrideTexturing = drawOverride.overrideTexturing
    ovt = overrideTexturing
    overridePlayback = drawOverride.overridePlayback
    ovp = overridePlayback
    overrideEnabled = drawOverride.overrideEnabled
    ove = overrideEnabled
    overrideVisibility = drawOverride.overrideVisibility
    ovv = overrideVisibility
    hideOnPlayback = drawOverride.hideOnPlayback
    hpb = hideOnPlayback
    overrideRGBColors = drawOverride.overrideRGBColors
    ovrgbf = overrideRGBColors
    overrideColor = drawOverride.overrideColor
    ovc = overrideColor
    overrideColorRGB = drawOverride.overrideColorRGB
    ovrgb = overrideColorRGB
    overrideColorA = drawOverride.overrideColorA
    ovca = overrideColorA

    lodVisibility = BoolField(default_value=True)
    lodv = lodVisibility

    selectionChildHighlighting = BoolField(default_value=True)
    sech = selectionChildHighlighting

    renderInfo = RenderInfoField(default_value=(0.0, 1.0, 0.0))
    ri = renderInfo
    identification = renderInfo.identification
    rlid = identification
    layerRenderable = renderInfo.layerRenderable
    rndr = layerRenderable
    layerOverrideColor = renderInfo.layerOverrideColor
    lovc = layerOverrideColor

    renderLayerInfo = RenderLayerInfoField(multi=True, default_value=(0.0, 1.0, 0.0))
    rlio = renderLayerInfo

    ghosting = BoolField(default_value=False)
    gh = ghosting

    ghostingMode = GhostingModeEnumField(default_value=0)
    gm = ghostingMode

    ghostCustomSteps = GhostCustomStepsField(default_value=(3.0, 3.0, 1.0))
    gcs = ghostCustomSteps
    ghostPreFrames = ghostCustomSteps.ghostPreFrames
    gprf = ghostPreFrames
    ghostPostFrames = ghostCustomSteps.ghostPostFrames
    gpof = ghostPostFrames
    ghostsStep = ghostCustomSteps.ghostsStep
    gstp = ghostsStep

    ghostFrames = TypedField()
    gf = ghostFrames

    ghostOpacityRange = GhostOpacityRangeField(default_value=(0.15000000596046448, 0.5), min_value=(0.0, 0.0), max_value=(1.0, 1.0))
    golr = ghostOpacityRange
    ghostFarOpacity = ghostOpacityRange.ghostFarOpacity
    gfro = ghostFarOpacity
    ghostNearOpacity = ghostOpacityRange.ghostNearOpacity
    gnro = ghostNearOpacity

    ghostColorPre = GhostColorPreField(default_value=(0.44699999690055847, 1.0, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    gcp = ghostColorPre
    ghostColorPreR = ghostColorPre.ghostColorPreR
    grr = ghostColorPreR
    ghostColorPreG = ghostColorPre.ghostColorPreG
    gpg = ghostColorPreG
    ghostColorPreB = ghostColorPre.ghostColorPreB
    gpb = ghostColorPreB

    ghostColorPost = GhostColorPostField(default_value=(0.878000020980835, 0.6779999732971191, 0.6629999876022339), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    gac = ghostColorPost
    ghostColorPostR = ghostColorPost.ghostColorPostR
    gar = ghostColorPostR
    ghostColorPostG = ghostColorPost.ghostColorPostG
    gag = ghostColorPostG
    ghostColorPostB = ghostColorPost.ghostColorPostB
    gab = ghostColorPostB

    ghostDriver = MessageField()
    gdr = ghostDriver

    ghostUseDriver = BoolField(default_value=False)
    gud = ghostUseDriver

    hiddenInOutliner = BoolField(default_value=False)
    hio = hiddenInOutliner

    useOutlinerColor = BoolField(default_value=False)
    uocol = useOutlinerColor

    outlinerColor = OutlinerColorField(default_value=(0.0, 0.0, 0.0))
    oclr = outlinerColor
    outlinerColorR = outlinerColor.outlinerColorR
    oclrr = outlinerColorR
    outlinerColorG = outlinerColor.outlinerColorG
    oclrg = outlinerColorG
    outlinerColorB = outlinerColor.outlinerColorB
    oclrb = outlinerColorB

    renderType = ShortField(default_value=0)
    rt = renderType

    renderVolume = BoolField(default_value=False)
    rv = renderVolume

    visibleFraction = FloatField(default_value=1.0)
    vf = visibleFraction

    hardwareFogMultiplier = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    hfm = hardwareFogMultiplier

    motionBlur = BoolField(default_value=True)
    mb = motionBlur

    visibleInReflections = BoolField(default_value=False)
    vir = visibleInReflections

    visibleInRefractions = BoolField(default_value=False)
    vif = visibleInRefractions

    castsShadows = BoolField(default_value=True)
    csh = castsShadows

    receiveShadows = BoolField(default_value=True)
    rcsh = receiveShadows

    asBackground = BoolField(default_value=False)
    asbg = asBackground

    maxVisibilitySamplesOverride = BoolField(default_value=False)
    vbo = maxVisibilitySamplesOverride

    maxVisibilitySamples = LongField(default_value=1, min_value=1, max_value=32, soft_max_value=20)
    mvs = maxVisibilitySamples

    geometryAntialiasingOverride = BoolField(default_value=False)
    gao = geometryAntialiasingOverride

    antialiasingLevel = LongField(default_value=1, min_value=1, max_value=5, soft_max_value=5)
    gal = antialiasingLevel

    shadingSamplesOverride = BoolField(default_value=False)
    sso = shadingSamplesOverride

    shadingSamples = LongField(default_value=1, min_value=1, max_value=32)
    ssa = shadingSamples

    maxShadingSamples = LongField(default_value=1, min_value=1, max_value=32, soft_max_value=20)
    msa = maxShadingSamples

    volumeSamplesOverride = BoolField(default_value=False)
    vso = volumeSamplesOverride

    volumeSamples = LongField(default_value=1, soft_max_value=20)
    vss = volumeSamples

    depthJitter = BoolField(default_value=False)
    dej = depthJitter

    ignoreSelfShadowing = BoolField(default_value=False)
    iss = ignoreSelfShadowing

    primaryVisibility = BoolField(default_value=True)
    vis = primaryVisibility

    referenceObject = MessageField()
    rob = referenceObject

    compInstObjGroups = CompInstObjGroupsField(multi=True)
    ciog = compInstObjGroups

    componentTags = ComponentTagsField(multi=True)
    gtag = componentTags

    instMaterialAssign = MessageField(multi=True)
    imtla = instMaterialAssign

    pickTexture = MessageField()
    pte = pickTexture

    tweak = BoolField(default_value=False)
    tw = tweak

    relativeTweak = BoolField(default_value=True)
    rtw = relativeTweak

    controlPoints = ControlPointsField(multi=True, default_value=(0.0, 0.0, 0.0))
    cp = controlPoints

    weights = DoubleField(multi=True, default_value=1.0)
    wt = weights

    tweakLocation = TypedField(readable=False)
    twl = tweakLocation

    blindDataNodes = MessageField(multi=True, readable=False)
    bn = blindDataNodes

    uvPivot = UvPivotField(default_value=(0.0, 0.0))
    pv = uvPivot
    uvPivotX = uvPivot.uvPivotX
    pvx = uvPivotX
    uvPivotY = uvPivot.uvPivotY
    pvy = uvPivotY

    uvSet = UvSetField(multi=True)
    uvst = uvSet

    currentUVSet = DataStringField()
    cuvs = currentUVSet

    displayImmediate = BoolField(default_value=False)
    di = displayImmediate

    displayColors = BoolField(default_value=False)
    dcol = displayColors

    displayColorChannel = DataStringField()
    dcc = displayColorChannel

    currentColorSet = DataStringField()
    ccls = currentColorSet

    colorSet = ColorSetField(multi=True)
    clst = colorSet

    ignoreHwShader = BoolField(default_value=False)
    ih = ignoreHwShader

    doubleSided = BoolField(default_value=True)
    ds = doubleSided

    opposite = BoolField(default_value=False)
    op = opposite

    holdOut = BoolField(default_value=False)
    hot = holdOut

    smoothShading = BoolField(default_value=True)
    smo = smoothShading

    boundingBoxScale = BoundingBoxScaleField(default_value=(1.5, 1.5, 1.5), min_value=(1.0, 1.0, 1.0))
    bbs = boundingBoxScale
    boundingBoxScaleX = boundingBoxScale.boundingBoxScaleX
    bscx = boundingBoxScaleX
    boundingBoxScaleY = boundingBoxScale.boundingBoxScaleY
    bscy = boundingBoxScaleY
    boundingBoxScaleZ = boundingBoxScale.boundingBoxScaleZ
    bscz = boundingBoxScaleZ

    featureDisplacement = BoolField(default_value=True)
    fbda = featureDisplacement

    initialSampleRate = LongField(default_value=6, min_value=0, soft_max_value=100)
    dsr = initialSampleRate

    extraSampleRate = LongField(default_value=5, min_value=0, soft_max_value=50)
    xsr = extraSampleRate

    textureThreshold = LongField(default_value=0, min_value=0, max_value=100)
    fth = textureThreshold

    normalThreshold = FloatField(default_value=30.0, min_value=0.0, max_value=180.0)
    nat = normalThreshold

    displayHWEnvironment = BoolField(default_value=False)
    dhe = displayHWEnvironment

    collisionOffsetVelocityIncrement = CollisionOffsetVelocityIncrementField(multi=True, default_value=(0.0, 0.0, 0.0))
    covi = collisionOffsetVelocityIncrement

    collisionDepthVelocityIncrement = CollisionDepthVelocityIncrementField(multi=True, default_value=(0.0, 0.0, 0.0))
    cdvi = collisionDepthVelocityIncrement

    collisionOffsetVelocityMultiplier = CollisionOffsetVelocityMultiplierField(multi=True, default_value=(0.0, 0.0, 0.0))
    covm = collisionOffsetVelocityMultiplier

    collisionDepthVelocityMultiplier = CollisionDepthVelocityMultiplierField(multi=True, default_value=(0.0, 0.0, 0.0))
    cdvm = collisionDepthVelocityMultiplier

    outGrid = TypedField(writable=False)
    out = outGrid

    currentTime = TimeField(default_value=0.0)
    cti = currentTime

    startTime = TimeField(default_value=0.0, writable=False)
    sti = startTime

    startFrame = DoubleField(default_value=1.0)
    stf = startFrame

    lastEvalTime = TimeField(default_value=-2.5)
    lst = lastEvalTime

    disableInteractiveEval = BoolField(default_value=False)
    die = disableInteractiveEval

    is2d = BoolField(default_value=False)
    is2 = is2d

    baseResolution = LongField(default_value=10, min_value=3, soft_max_value=200)
    bres = baseResolution

    squareVoxels = BoolField(default_value=False)
    sqvx = squareVoxels

    resolution = ResolutionField(default_value=(10.0, 10.0, 10.0), min_value=(3.0, 3.0, 1.0))
    res = resolution
    resolutionW = resolution.resolutionW
    rw = resolutionW
    resolutionH = resolution.resolutionH
    rh = resolutionH
    resolutionD = resolution.resolutionD
    rd = resolutionD

    dimensions = DimensionsField(default_value=(3.0, 3.0, 3.0), min_value=(1e-05, 1e-05, 1e-05))
    dim = dimensions
    dimensionsW = dimensions.dimensionsW
    dw = dimensionsW
    dimensionsH = dimensions.dimensionsH
    dh = dimensionsH
    dimensionsD = dimensions.dimensionsD
    dd = dimensionsD

    autoResize = BoolField(default_value=False)
    aure = autoResize

    resizeClosedBoundaries = BoolField(default_value=True)
    rcbd = resizeClosedBoundaries

    autoResizeThreshold = FloatField(default_value=0.009999999776482582, min_value=1e-06, soft_max_value=0.1)
    aurt = autoResizeThreshold

    maxResolution = LongField(default_value=200, min_value=4, soft_max_value=300)
    mres = maxResolution

    resizeToEmitter = BoolField(default_value=True)
    rste = resizeToEmitter

    resizeInSubsteps = BoolField(default_value=True)
    riss = resizeInSubsteps

    autoResizeMargin = LongField(default_value=0, min_value=0, soft_max_value=20)
    armg = autoResizeMargin

    dynamicOffset = DynamicOffsetField(default_value=(0.0, 0.0, 0.0))
    dofs = dynamicOffset
    dynamicOffsetX = dynamicOffset.dynamicOffsetX
    dofx = dynamicOffsetX
    dynamicOffsetY = dynamicOffset.dynamicOffsetY
    dofy = dynamicOffsetY
    dynamicOffsetZ = dynamicOffset.dynamicOffsetZ
    dofz = dynamicOffsetZ

    initialConditions = MessageField(writable=False)
    inc = initialConditions

    doFields = BoolField(default_value=True)
    dfr = doFields

    inputForce = DataVectorArrayField(multi=True)
    ifc = inputForce

    fieldData = FieldDataField(writable=False)
    fd = fieldData
    fieldDataPosition = fieldData.fieldDataPosition
    fdp = fieldDataPosition
    fieldDataVelocity = fieldData.fieldDataVelocity
    fdv = fieldDataVelocity
    fieldDataMass = fieldData.fieldDataMass
    fdm = fieldDataMass
    fieldDataDeltaTime = fieldData.fieldDataDeltaTime
    fdt = fieldDataDeltaTime

    fieldList = FieldListField(multi=True)
    fll = fieldList

    fieldFunction_Hidden = TypedField()
    frfh = fieldFunction_Hidden

    fieldFunction_Raw = TypedField()
    frfr = fieldFunction_Raw

    fieldFunction_Inmap = CompoundField()
    frfi = fieldFunction_Inmap

    fieldFunction_InmapTo = ShortField()
    frfit = fieldFunction_InmapTo

    fieldFunction_InmapFrom = ShortField()
    frfif = fieldFunction_InmapFrom

    fieldFunction_Outmap = CompoundField()
    frfo = fieldFunction_Outmap

    fieldFunction_OutmapTo = ShortField()
    frfot = fieldFunction_OutmapTo

    fieldFunction_OutmapFrom = ShortField()
    frfof = fieldFunction_OutmapFrom

    doEmission = BoolField(default_value=True)
    de = doEmission

    isFull = BoolField(default_value=False, writable=False)
    ifl = isFull

    inheritFactor = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    inh = inheritFactor

    seed = LongField(multi=True, default_value=1)
    sd = seed

    fluidColorEmission = BoolField(multi=True, default_value=False)
    fce = fluidColorEmission

    fluidReactantEmission = BoolField(multi=True, default_value=False)
    frm = fluidReactantEmission

    emissionList = EmissionListField(multi=True)
    eml = emissionList

    emissionFunction_Hidden = TypedField()
    emfh = emissionFunction_Hidden

    emissionFunction_Raw = TypedField()
    emfr = emissionFunction_Raw

    emissionFunction_Inmap = CompoundField()
    emfi = emissionFunction_Inmap

    emissionFunction_InmapTo = ShortField()
    emfit = emissionFunction_InmapTo

    emissionFunction_InmapFrom = ShortField()
    emfif = emissionFunction_InmapFrom

    emissionFunction_Outmap = CompoundField()
    emfo = emissionFunction_Outmap

    emissionFunction_OutmapTo = ShortField()
    emfot = emissionFunction_OutmapTo

    emissionFunction_OutmapFrom = ShortField()
    emfof = emissionFunction_OutmapFrom

    slices = LongField(default_value=2, min_value=1, max_value=12)
    sli = slices

    voxelQuality = VoxelQualityEnumField(default_value=1)
    vqu = voxelQuality

    drawSubVolume = BoolField(default_value=False)
    dsv = drawSubVolume

    subVolumeCenter = SubVolumeCenterField(default_value=(-1.0, -1.0, -1.0), min_value=(-1.0, -1.0, -1.0))
    svc = subVolumeCenter
    subVolumeCenterW = subVolumeCenter.subVolumeCenterW
    scw = subVolumeCenterW
    subVolumeCenterH = subVolumeCenter.subVolumeCenterH
    sch = subVolumeCenterH
    subVolumeCenterD = subVolumeCenter.subVolumeCenterD
    scd = subVolumeCenterD

    subVolumeSize = SubVolumeSizeField(default_value=(-1.0, -1.0, -1.0), min_value=(-1.0, -1.0, -1.0))
    svs = subVolumeSize
    subVolumeSizeW = subVolumeSize.subVolumeSizeW
    ssw = subVolumeSizeW
    subVolumeSizeH = subVolumeSize.subVolumeSizeH
    ssh = subVolumeSizeH
    subVolumeSizeD = subVolumeSize.subVolumeSizeD
    ssd = subVolumeSizeD

    lockDrawAxis = BoolField(default_value=False)
    lda = lockDrawAxis

    boundaryDraw = BoundaryDrawEnumField(default_value=0)
    bod = boundaryDraw

    drawHeads = BoolField(default_value=True)
    dhd = drawHeads

    velocityDraw = BoolField(default_value=False)
    vld = velocityDraw

    velocityDrawLength = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)
    vdl = velocityDrawLength

    velocityDrawSkip = LongField(default_value=1, min_value=0, soft_max_value=5)
    vds = velocityDrawSkip

    shadedDisplay = ShadedDisplayEnumField(default_value=1)
    sdp = shadedDisplay

    opacityPreviewGain = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    opg = opacityPreviewGain

    wireframeDisplay = WireframeDisplayEnumField(default_value=2)
    wdp = wireframeDisplay

    numericDisplay = NumericDisplayEnumField(default_value=0)
    nud = numericDisplay

    hardwareSelfShadow = BoolField(default_value=True)
    hss = hardwareSelfShadow

    coordinateMethod = CoordinateMethodEnumField(default_value=0)
    cmet = coordinateMethod

    overrideTimeStep = TimeField(default_value=2.5)
    ots = overrideTimeStep

    simulationRateScale = FloatField(default_value=1.0)
    srs = simulationRateScale

    gridInterpolator = GridInterpolatorEnumField(default_value=0)
    gdi = gridInterpolator

    forceDynamics = BoolField(default_value=False)
    fdn = forceDynamics

    solver = SolverEnumField(default_value=1)
    sol = solver

    solverQuality = LongField(default_value=20, min_value=0, max_value=1000, soft_max_value=100)
    sql = solverQuality

    substeps = LongField(default_value=1, min_value=1, soft_max_value=20)
    sbst = substeps

    emitInSubsteps = BoolField(default_value=False)
    eiss = emitInSubsteps

    highDetailSolve = HighDetailSolveEnumField(default_value=0)
    hds = highDetailSolve

    enableLiquidSimulation = BoolField(default_value=False)
    elsm = enableLiquidSimulation

    liquidMethod = LiquidMethodEnumField(default_value=1)
    lmth = liquidMethod

    liquidMinDensity = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    lqmd = liquidMinDensity

    liquidMistFall = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    lmsf = liquidMistFall

    massRange = FloatField(default_value=200.0, soft_min_value=0.0, soft_max_value=5000.0)
    msrn = massRange

    forwardAdvection = BoolField(default_value=False)
    foad = forwardAdvection

    boundaryX = BoundaryXEnumField(default_value=1)
    bndx = boundaryX

    boundaryY = BoundaryYEnumField(default_value=1)
    bndy = boundaryY

    boundaryZ = BoundaryZEnumField(default_value=1)
    bndz = boundaryZ

    massConversion = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    mcv = massConversion

    falloffMethod = FalloffMethodEnumField(default_value=0)
    fmt = falloffMethod

    densityMethod = DensityMethodEnumField(default_value=2)
    dmt = densityMethod

    densityGradient = DensityGradientEnumField(default_value=4)
    dgr = densityGradient

    densityScale = FloatField(default_value=0.5, min_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    dsc = densityScale

    densityDissipation = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    dds = densityDissipation

    densityDiffusion = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    ddf = densityDiffusion

    conserveMass = BoolField(default_value=True)
    cm = conserveMass

    densityBuoyancy = FloatField(default_value=1.0, soft_min_value=-5.0, soft_max_value=5.0)
    dsb = densityBuoyancy

    densityGradientForce = FloatField(default_value=0.0, soft_min_value=-5.0, soft_max_value=5.0)
    dsgf = densityGradientForce

    densityTension = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    dstn = densityTension

    tensionForce = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    tnsf = tensionForce

    densityNoise = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    dsns = densityNoise

    densityPressure = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    dspr = densityPressure

    densityPressureThreshold = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    dspt = densityPressureThreshold

    selfForce = SelfForceEnumField(default_value=0)
    slfc = selfForce

    selfAttract = FloatField(default_value=0.10000000149011612, soft_min_value=0.0, soft_max_value=5.0)
    sfat = selfAttract

    selfRepel = FloatField(default_value=0.10000000149011612, soft_min_value=0.0, soft_max_value=5.0)
    sfrp = selfRepel

    equilibriumValue = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=2.0)
    eqvl = equilibriumValue

    selfForceDistance = LongField(default_value=16, min_value=1, soft_max_value=100)
    sfds = selfForceDistance

    gravity = FloatField(default_value=9.800000190734863, soft_min_value=0.0, soft_max_value=10.0)
    grv = gravity

    velocityMethod = VelocityMethodEnumField(default_value=2)
    vmt = velocityMethod

    velocityGradient = VelocityGradientEnumField(default_value=4)
    vgr = velocityGradient

    velocityScale = VelocityScaleField(default_value=(1.0, 1.0, 1.0))
    vsc = velocityScale
    velocityScaleX = velocityScale.velocityScaleX
    vsx = velocityScaleX
    velocityScaleY = velocityScale.velocityScaleY
    vsy = velocityScaleY
    velocityScaleZ = velocityScale.velocityScaleZ
    vsz = velocityScaleZ

    viscosity = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    viy = viscosity

    friction = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fri = friction

    velocitySwirl = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)
    vsw = velocitySwirl

    velocityNoise = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    vsns = velocityNoise

    velocityDamp = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    vdp = velocityDamp

    velocityAdvect = BoolField(default_value=True)
    va = velocityAdvect

    velocityProject = BoolField(default_value=True)
    vi = velocityProject

    turbulenceStrength = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    tst = turbulenceStrength

    turbulenceFrequency = FloatField(default_value=0.20000000298023224, min_value=0.0, soft_max_value=2.0)
    tfr = turbulenceFrequency

    turbulenceSpeed = FloatField(default_value=0.20000000298023224, min_value=0.0, soft_max_value=2.0)
    tbs = turbulenceSpeed

    turbulenceRes = LongField(default_value=10)
    trs = turbulenceRes

    temperatureMethod = TemperatureMethodEnumField(default_value=0)
    tmet = temperatureMethod

    temperatureGradient = TemperatureGradientEnumField(default_value=4)
    tgr = temperatureGradient

    temperatureScale = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    tmsc = temperatureScale

    temperatureDissipation = DoubleField(default_value=0.1, soft_min_value=0.0, soft_max_value=1.0)
    tds = temperatureDissipation

    temperatureDiffusion = DoubleField(default_value=0.1, soft_min_value=0.0, soft_max_value=2.0)
    tdf = temperatureDiffusion

    temperatureTurbulence = FloatField(default_value=0.10000000149011612, soft_min_value=0.0, soft_max_value=5.0)
    ttb = temperatureTurbulence

    temperatureNoise = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    tmns = temperatureNoise

    temperaturePressure = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    tmpr = temperaturePressure

    temperaturePressureThreshold = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    tmpt = temperaturePressureThreshold

    buoyancy = FloatField(default_value=3.0, soft_min_value=-10.0, soft_max_value=10.0)
    buo = buoyancy

    temperatureTension = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    tttn = temperatureTension

    colorMethod = ColorMethodEnumField(default_value=0)
    cmt = colorMethod

    colorDissipation = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    cds = colorDissipation

    colorDiffusion = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    cdf = colorDiffusion

    fuelMethod = FuelMethodEnumField(default_value=0)
    fmet = fuelMethod

    fuelGradient = FuelGradientEnumField(default_value=4)
    fgr = fuelGradient

    fuelScale = FloatField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    fesc = fuelScale

    reactionSpeed = FloatField(default_value=0.05000000074505806, soft_min_value=0.0, soft_max_value=1.0)
    resp = reactionSpeed

    fuelIgnitionTemp = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fuit = fuelIgnitionTemp

    maxReactionTemp = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    mxrt = maxReactionTemp

    airFuelRatio = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=50.0)
    afrt = airFuelRatio

    heatReleased = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    hre = heatReleased

    lightReleased = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    lre = lightReleased

    lightColor = LightColorField(default_value=(1.0, 1.0, 1.0))
    lco = lightColor
    lightColorR = lightColor.lightColorR
    lcor = lightColorR
    lightColorG = lightColor.lightColorG
    lcog = lightColorG
    lightColorB = lightColor.lightColorB
    lcob = lightColorB

    usePre70Dynamics = BoolField(default_value=False)
    updy = usePre70Dynamics

    outMesh = DataMeshField(writable=False)
    o = outMesh

    inputData = InputDataField(multi=True)
    ind = inputData

    inputForce2 = DataVectorArrayField(multi=True)
    in2 = inputForce2

    outputForce = DataVectorArrayField(multi=True, writable=False)
    of = outputForce

    matteOpacityMode = MatteOpacityModeEnumField(default_value=2)
    mom = matteOpacityMode

    matteOpacity = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    mog = matteOpacity

    filterSize = FilterSizeField(default_value=(0.0, 0.0, 0.0), readable=False)
    fs = filterSize
    filterSizeX = filterSize.filterSizeX
    fsx = filterSizeX
    filterSizeY = filterSize.filterSizeY
    fsy = filterSizeY
    filterSizeZ = filterSize.filterSizeZ
    fsz = filterSizeZ

    matrixEyeToWorld = FltMatrixField()
    e2w = matrixEyeToWorld

    matrixWorldToObject = FltMatrixField()
    w2o = matrixWorldToObject

    pointWorld = PointWorldField(default_value=(0.0, 0.0, 0.0))
    pw = pointWorld
    pointWorldX = pointWorld.pointWorldX
    pwx = pointWorldX
    pointWorldY = pointWorld.pointWorldY
    pwy = pointWorldY
    pointWorldZ = pointWorld.pointWorldZ
    pwz = pointWorldZ

    farPointWorld = FarPointWorldField(default_value=(1.0, 1.0, 1.0))
    fw = farPointWorld
    farPointWorldX = farPointWorld.farPointWorldX
    fwx = farPointWorldX
    farPointWorldY = farPointWorld.farPointWorldY
    fwy = farPointWorldY
    farPointWorldZ = farPointWorld.farPointWorldZ
    fwz = farPointWorldZ

    pointObj = PointObjField(default_value=(0.0, 0.0, 0.0))
    po = pointObj
    pointObjX = pointObj.pointObjX
    pox = pointObjX
    pointObjY = pointObj.pointObjY
    poy = pointObjY
    pointObjZ = pointObj.pointObjZ
    poz = pointObjZ

    farPointObj = FarPointObjField(default_value=(1.0, 1.0, 1.0))
    fo = farPointObj
    farPointObjectX = farPointObj.farPointObjectX
    fox = farPointObjectX
    farPointObjectY = farPointObj.farPointObjectY
    foy = farPointObjectY
    farPointObjectZ = farPointObj.farPointObjectZ
    foz = farPointObjectZ

    rayInstance = LongField(default_value=0)
    ryi = rayInstance

    lightDataArray = LightDataArrayField(multi=True, readable=False)
    ltd = lightDataArray

    lightDirectionX = FloatField()
    ldx = lightDirectionX

    lightDirectionY = FloatField()
    ldy = lightDirectionY

    lightDirectionZ = FloatField()
    ldz = lightDirectionZ

    lightIntensityR = FloatField()
    lir = lightIntensityR

    lightIntensityG = FloatField()
    lig = lightIntensityG

    lightIntensityB = FloatField()
    lib = lightIntensityB

    selfShadowing = BoolField(default_value=False)
    ss = selfShadowing

    quality = FloatField(default_value=1.0, min_value=0.0001, soft_min_value=0.01, soft_max_value=10.0)
    qua = quality

    renderInterpolator = RenderInterpolatorEnumField(default_value=0)
    rin = renderInterpolator

    color = ColorField(multi=True)
    cl = color

    color_ColorR = FloatField()
    clcr = color_ColorR

    color_ColorG = FloatField()
    clcg = color_ColorG

    color_ColorB = FloatField()
    clcb = color_ColorB

    colorInput = ColorInputEnumField(default_value=0)
    coi = colorInput

    colorInputBias = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    cib = colorInputBias

    opacity = OpacityField(multi=True, default_value=(0.0, 0.0, 0.0))
    opa = opacity

    opacityInput = OpacityInputEnumField(default_value=5)
    opi = opacityInput

    opacityInputBias = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    oib = opacityInputBias

    transparency = TransparencyField(default_value=(0.25, 0.25, 0.25))
    t = transparency
    transparencyR = transparency.transparencyR
    tr = transparencyR
    transparencyG = transparency.transparencyG
    tg = transparencyG
    transparencyB = transparency.transparencyB
    tb = transparencyB

    shadowOpacity = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    shp = shadowOpacity

    shadowDiffusion = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)
    sdfu = shadowDiffusion

    lightType = LightTypeEnumField(default_value=1)
    ltyp = lightType

    lightBrightness = FloatField(default_value=1.0, min_value=0.0, soft_max_value=5.0)
    lbrt = lightBrightness

    pointLightDecay = PointLightDecayEnumField(default_value=1)
    pldy = pointLightDecay

    fluidLightColor = FluidLightColorField(default_value=(1.0, 1.0, 1.0))
    flic = fluidLightColor
    fluidLightColorR = fluidLightColor.fluidLightColorR
    flir = fluidLightColorR
    fluidLightColorG = fluidLightColor.fluidLightColorG
    flig = fluidLightColorG
    fluidLightColorB = fluidLightColor.fluidLightColorB
    flib = fluidLightColorB

    ambientBrightness = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    abrt = ambientBrightness

    ambientDiffusion = FloatField(default_value=2.0, min_value=0.0, soft_max_value=20.0)
    adfu = ambientDiffusion

    ambientColor = AmbientColorField(default_value=(0.5, 0.699999988079071, 1.0))
    ambc = ambientColor
    ambientColorR = ambientColor.ambientColorR
    ambr = ambientColorR
    ambientColorG = ambientColor.ambientColorG
    ambg = ambientColorG
    ambientColorB = ambientColor.ambientColorB
    ambb = ambientColorB

    incandescence = IncandescenceField(multi=True)
    i = incandescence

    incandescence_ColorR = FloatField()
    icr = incandescence_ColorR

    incandescence_ColorG = FloatField()
    icg = incandescence_ColorG

    incandescence_ColorB = FloatField()
    icb = incandescence_ColorB

    incandescenceInput = IncandescenceInputEnumField(default_value=6)
    ili = incandescenceInput

    incandescenceInputBias = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    iib = incandescenceInputBias

    glowIntensity = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    gi = glowIntensity

    specularColor = SpecularColorField(default_value=(0.0, 0.0, 0.0))
    spc = specularColor
    specularColorR = specularColor.specularColorR
    spr = specularColorR
    specularColorG = specularColor.specularColorG
    spg = specularColorG
    specularColorB = specularColor.specularColorB
    spb = specularColorB

    cosinePower = FloatField(default_value=20.0, min_value=2.0, soft_max_value=100.0)
    csp = cosinePower

    environment = EnvironmentField(multi=True)
    env = environment

    environment_ColorR = FloatField()
    envcr = environment_ColorR

    environment_ColorG = FloatField()
    envcg = environment_ColorG

    environment_ColorB = FloatField()
    envcb = environment_ColorB

    dropoffShape = DropoffShapeEnumField(default_value=2)
    dos = dropoffShape

    edgeDropoff = FloatField(default_value=0.05000000074505806, soft_min_value=0.0, soft_max_value=1.0)
    edr = edgeDropoff

    contrastTolerance = FloatField(default_value=0.009999999776482582, min_value=1e-05, soft_min_value=0.001, soft_max_value=1.0)
    ctl = contrastTolerance

    heightField = BoolField(default_value=False)
    hfld = heightField

    surfaceRender = BoolField(default_value=False)
    srr = surfaceRender

    surfaceThreshold = FloatField(default_value=0.009999999776482582, min_value=0.001, soft_max_value=1.0)
    srt = surfaceThreshold

    surfaceTolerance = FloatField(default_value=0.10000000149011612, min_value=0.001, soft_max_value=1.0)
    stl = surfaceTolerance

    softSurface = BoolField(default_value=False)
    ssf = softSurface

    meshSmoothingIterations = LongField(default_value=0, min_value=0, soft_max_value=10)
    msit = meshSmoothingIterations

    meshMethod = MeshMethodEnumField(default_value=0)
    mmd = meshMethod

    meshResolution = FloatField(default_value=2.0, min_value=0.0, soft_min_value=1.0, soft_max_value=4.0)
    mre = meshResolution

    colorPerVertex = BoolField(default_value=False)
    cpvx = colorPerVertex

    opacityPerVertex = BoolField(default_value=False)
    opvx = opacityPerVertex

    incandescencePerVertex = BoolField(default_value=False)
    ipvx = incandescencePerVertex

    velocityPerVertex = BoolField(default_value=True)
    vpvx = velocityPerVertex

    uvwPerVertex = BoolField(default_value=False)
    upvx = uvwPerVertex

    useGradientNormals = BoolField(default_value=False)
    ugn = useGradientNormals

    refractiveIndex = FloatField(default_value=1.7999999523162842, min_value=0.0, soft_min_value=1.0, soft_max_value=5.0)
    rei = refractiveIndex

    sampleMethod = SampleMethodEnumField(default_value=3)
    smpm = sampleMethod

    realLights = BoolField(default_value=True)
    rl = realLights

    pointLight = PointLightField(default_value=(0.0, 0.0, 0.0))
    poli = pointLight
    pointLightX = pointLight.pointLightX
    polx = pointLightX
    pointLightY = pointLight.pointLightY
    poly = pointLightY
    pointLightZ = pointLight.pointLightZ
    polz = pointLightZ

    directionalLight = DirectionalLightField(default_value=(0.5, 0.800000011920929, 0.5))
    dl = directionalLight
    directionalLightX = directionalLight.directionalLightX
    dlx = directionalLightX
    directionalLightY = directionalLight.directionalLightY
    dly = directionalLightY
    directionalLightZ = directionalLight.directionalLightZ
    dlz = directionalLightZ

    textureType = TextureTypeEnumField(default_value=0)
    tty = textureType

    colorTexture = BoolField(default_value=False)
    ctx = colorTexture

    colorTexGain = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)
    ctxg = colorTexGain

    incandTexture = BoolField(default_value=False)
    itx = incandTexture

    incandTexGain = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)
    itxg = incandTexGain

    opacityTexture = BoolField(default_value=False)
    otx = opacityTexture

    opacityTexGain = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)
    otxg = opacityTexGain

    invertTexture = BoolField(default_value=False)
    ivt = invertTexture

    amplitude = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    a = amplitude

    ratio = FloatField(default_value=0.7070000171661377, min_value=0.0, max_value=1.0)
    ra = ratio

    threshold = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    th = threshold

    textureScale = TextureScaleField(default_value=(1.0, 1.0, 1.0), min_value=(0.0, 0.0, 0.0))
    txsc = textureScale
    textureScaleX = textureScale.textureScaleX
    tscx = textureScaleX
    textureScaleY = textureScale.textureScaleY
    tscy = textureScaleY
    textureScaleZ = textureScale.textureScaleZ
    tscz = textureScaleZ

    textureOrigin = TextureOriginField(default_value=(0.0, 0.0, 0.0), soft_min_value=(-100.0, -100.0, -100.0), soft_max_value=(100.0, 100.0, 100.0))
    tor = textureOrigin
    textureOriginX = textureOrigin.textureOriginX
    torx = textureOriginX
    textureOriginY = textureOrigin.textureOriginY
    tory = textureOriginY
    textureOriginZ = textureOrigin.textureOriginZ
    torz = textureOriginZ

    textureRotate = TextureRotateField(default_value=(0.0, 0.0, 0.0))
    trt = textureRotate
    textureRotateX = textureRotate.textureRotateX
    trtx = textureRotateX
    textureRotateY = textureRotate.textureRotateY
    trty = textureRotateY
    textureRotateZ = textureRotate.textureRotateZ
    trtz = textureRotateZ

    depthMax = ShortField(default_value=2, min_value=1, max_value=80, soft_max_value=8)
    dm = depthMax

    frequency = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)
    fq = frequency

    frequencyRatio = FloatField(default_value=2.0, soft_min_value=1.0, soft_max_value=10.0)
    fr = frequencyRatio

    inflection = BoolField(default_value=False)
    in_ = inflection

    textureTime = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    tti = textureTime

    billowDensity = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    bd = billowDensity

    spottyness = FloatField(default_value=0.10000000149011612, min_value=0.0, soft_max_value=1.0)
    sp = spottyness

    sizeRand = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    sr = sizeRand

    randomness = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    rnd = randomness

    falloff = FalloffEnumField(default_value=2)
    falo = falloff

    numWaves = ShortField(default_value=5, min_value=1, soft_max_value=20)
    nw = numWaves

    implode = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    imp = implode

    implodeCenter = ImplodeCenterField(default_value=(0.0, 0.0, 0.0))
    imc = implodeCenter
    implodeCenterX = implodeCenter.implodeCenterX
    imx = implodeCenterX
    implodeCenterY = implodeCenter.implodeCenterY
    imy = implodeCenterY
    implodeCenterZ = implodeCenter.implodeCenterZ
    imz = implodeCenterZ

    mandelbrotDepth = LongField(default_value=7, min_value=1, soft_max_value=100)
    mdm = mandelbrotDepth

    focus = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    foc = focus

    zoomFactor = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    zfc = zoomFactor

    escapeRadius = FloatField(default_value=2.0, soft_min_value=0.0, soft_max_value=10.0)
    esr = escapeRadius

    lobes = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    lbs = lobes

    leafEffect = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    lef = leafEffect

    checker = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    chk = checker

    lineBlending = BoolField(default_value=False)
    lbl = lineBlending

    lineFocus = FloatField(default_value=0.5, max_value=1.0, soft_min_value=0.0)
    lfc = lineFocus

    points = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    pts = points

    stalksU = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    stku = stalksU

    stalksV = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    stkv = stalksV

    circles = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    cir = circles

    circleRadius = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    ccr = circleRadius

    circleSizeRatio = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    csr = circleSizeRatio

    lineOffsetU = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    lou = lineOffsetU

    lineOffsetV = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    lov = lineOffsetV

    lineOffsetRatio = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    lor = lineOffsetRatio

    juliaU = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    jlu = juliaU

    juliaV = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    jlv = juliaV

    boxRadius = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)
    bxr = boxRadius

    boxMinRadius = FloatField(default_value=0.5, min_value=0.0, soft_max_value=2.0)
    bxm = boxMinRadius

    boxRatio = FloatField(default_value=-3.0, soft_min_value=-4.0, soft_max_value=4.0)
    brt = boxRatio

    mandelbrotType = MandelbrotTypeEnumField(default_value=1)
    nty = mandelbrotType

    mandelbrotShadeMethod = MandelbrotShadeMethodEnumField(default_value=1)
    msm = mandelbrotShadeMethod

    mandelbrotInsideMethod = MandelbrotInsideMethodEnumField(default_value=2)
    mim = mandelbrotInsideMethod

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    ocl = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outGlowColor = OutGlowColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    ogc = outGlowColor
    outGlowColorR = outGlowColor.outGlowColorR
    ogr = outGlowColorR
    outGlowColorG = outGlowColor.outGlowColorG
    ogg = outGlowColorG
    outGlowColorB = outGlowColor.outGlowColorB
    ogb = outGlowColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    outMatteOpacity = OutMatteOpacityField(default_value=(0.0, 0.0, 0.0), writable=False)
    omo = outMatteOpacity
    outMatteOpacityR = outMatteOpacity.outMatteOpacityR
    omor = outMatteOpacityR
    outMatteOpacityG = outMatteOpacity.outMatteOpacityG
    omog = outMatteOpacityG
    outMatteOpacityB = outMatteOpacity.outMatteOpacityB
    omob = outMatteOpacityB

    diskCache = MessageField()
    dc = diskCache

    diskCacheIC = MessageField()
    dcic = diskCacheIC

    cacheDensity = BoolField(default_value=True)
    cdns = cacheDensity

    loadDensity = BoolField(default_value=True)
    ldns = loadDensity

    cacheVelocity = BoolField(default_value=True)
    cvel = cacheVelocity

    loadVelocity = BoolField(default_value=True)
    lvel = loadVelocity

    cacheTemperature = BoolField(default_value=True)
    ctmp = cacheTemperature

    loadTemperature = BoolField(default_value=True)
    ltmp = loadTemperature

    cacheColor = BoolField(default_value=True)
    ccol = cacheColor

    loadColor = BoolField(default_value=True)
    lcol = loadColor

    cacheReaction = BoolField(default_value=True)
    crea = cacheReaction

    loadReaction = BoolField(default_value=True)
    lrea = loadReaction

    cacheTextureCoordinates = BoolField(default_value=True)
    catc = cacheTextureCoordinates

    loadTextureCoordinates = BoolField(default_value=True)
    lotc = loadTextureCoordinates

    cacheFalloff = BoolField(default_value=True)
    cfal = cacheFalloff

    loadFalloff = BoolField(default_value=True)
    lfal = loadFalloff

    playFromCache = BoolField(default_value=False)
    pfch = playFromCache

    inResolution = TypedField()
    ires = inResolution

    inOffset = TypedField()
    ioff = inOffset

    inDensity = TypedField()
    idns = inDensity

    inVelocity = TypedField()
    ivel = inVelocity

    inTemperature = TypedField()
    itmp = inTemperature

    inReaction = TypedField()
    irea = inReaction

    inColor = TypedField()
    icol = inColor

    inTextureCoordinates = TypedField()
    itxc = inTextureCoordinates

    inFalloff = TypedField()
    ifal = inFalloff

    collisionData = CollisionDataField(readable=False)
    cda = collisionData
    collisionGeometry = collisionData.collisionGeometry
    cge = collisionGeometry
    collisionResilience = collisionData.collisionResilience
    crs = collisionResilience
    collisionFriction = collisionData.collisionFriction
    cfr = collisionFriction

    collide = BoolField(default_value=True)
    cld = collide

    objectType = CharField(default_value=2, min_value=0, max_value=255, readable=False)
    obt = objectType

    surfaceShaderDepth = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    susd = surfaceShaderDepth

    particleWeight = FloatField(default_value=0.0)
    we = particleWeight

    coordinateSpeed = FloatField(default_value=0.20000000298023224, soft_min_value=0.0, soft_max_value=1.0)
    csd = coordinateSpeed

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiStepSize = FloatField(default_value=0.10000000149011612, min_value=0.0, soft_max_value=2.0, category="arnold")
    ai_step_size = aiStepSize

    aiPhaseFunc = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0, category="arnold")

    aiOverrideTextures = BoolField(default_value=False, category="arnold")
    ai_override_textures = aiOverrideTextures

    aiTextureAffectColor = BoolField(default_value=False, category="arnold")
    ai_texture_affect_color = aiTextureAffectColor

    aiTextureAffectIncand = BoolField(default_value=False, category="arnold")
    ai_texture_affect_incand = aiTextureAffectIncand

    aiTextureAffectOpacity = BoolField(default_value=False, category="arnold")
    ai_texture_affect_opacity = aiTextureAffectOpacity

    aiEnableDeformationBlur = BoolField(default_value=False, category="arnold")
    ai_enable_deformation_blur = aiEnableDeformationBlur

    aiMotionVectorScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0, category="arnold")
    ai_motion_vector_scale = aiMotionVectorScale

    aiVolumeTexture = AiVolumeTextureField(default_value=(1.0, 0.0, 0.0), category="arnold")
    ai_volume_texture = aiVolumeTexture
    aiVolumeTextureR = aiVolumeTexture.aiVolumeTextureR
    ai_volume_texturer = aiVolumeTextureR
    aiVolumeTextureG = aiVolumeTexture.aiVolumeTextureG
    ai_volume_textureg = aiVolumeTextureG
    aiVolumeTextureB = aiVolumeTexture.aiVolumeTextureB
    ai_volume_textureb = aiVolumeTextureB

    aiTextureCoordinateMethod = AiTextureCoordinateMethodEnumField(default_value=0, category="arnold")
    ai_texture_coordinate_method = aiTextureCoordinateMethod

    aiFilterType = AiFilterTypeEnumField(default_value=1, category="arnold")
    ai_filter_type = aiFilterType

    aiVisibleInDiffuseReflection = BoolField(default_value=True, category="arnold")
    ai_vidr = aiVisibleInDiffuseReflection

    aiVisibleInSpecularReflection = BoolField(default_value=True, category="arnold")
    ai_visr = aiVisibleInSpecularReflection

    aiVisibleInDiffuseTransmission = BoolField(default_value=True, category="arnold")
    ai_vidt = aiVisibleInDiffuseTransmission

    aiVisibleInSpecularTransmission = BoolField(default_value=True, category="arnold")
    ai_vist = aiVisibleInSpecularTransmission

    aiVisibleInVolume = BoolField(default_value=True, category="arnold")
    ai_viv = aiVisibleInVolume

    refPointCamera = RefPointCameraField(default_value=(1.0, 1.0, 1.0))
    rpc = refPointCamera
    refPointCameraX = refPointCamera.refPointCameraX
    rcx = refPointCameraX
    refPointCameraY = refPointCamera.refPointCameraY
    rcy = refPointCameraY
    refPointCameraZ = refPointCamera.refPointCameraZ
    rcz = refPointCameraZ

    outAlpha = FloatField(default_value=0.0, writable=False)
    oa = outAlpha

    outCoord = OutCoordField(default_value=(0.0, 0.0, 0.0), writable=False)
    ouc = outCoord
    oucx = outCoord.oucx
    ocx = oucx
    oucy = outCoord.oucy
    ocy = oucy
    oucz = outCoord.oucz
    ocz = oucz

    alphaGain = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    ag = alphaGain

    alphaOffset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    ao = alphaOffset

    defaultColor = DefaultColorField(default_value=(0.5, 0.5, 0.5), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    dcl = defaultColor
    defaultColorR = defaultColor.defaultColorR
    dcr = defaultColorR
    defaultColorG = defaultColor.defaultColorG
    dcg = defaultColorG
    defaultColorB = defaultColor.defaultColorB
    dcb = defaultColorB
