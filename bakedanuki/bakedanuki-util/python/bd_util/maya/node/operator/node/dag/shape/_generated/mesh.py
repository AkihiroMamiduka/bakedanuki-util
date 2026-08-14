# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.mesh import (
    AiShadowColorField,
    BoundingBoxField,
    BoundingBoxScaleField,
    CenterField,
    CollisionDepthVelocityIncrementField,
    CollisionDepthVelocityMultiplierField,
    CollisionOffsetVelocityIncrementField,
    CollisionOffsetVelocityMultiplierField,
    ColorField,
    ColorPerVertexField,
    ColorSetField,
    ColorsField,
    CompInstObjGroupsField,
    ComponentTagsField,
    ControlPointsField,
    DrawOverrideField,
    EdgeField,
    GhostColorPostField,
    GhostColorPreField,
    GhostCustomStepsField,
    GhostOpacityRangeField,
    InstObjGroupsField,
    NormalPerVertexField,
    NormalsField,
    ObjectColorRGBField,
    OutlinerColorField,
    PntsField,
    PublishedNodeInfoField,
    RenderInfoField,
    RenderLayerInfoField,
    SmoothOffsetField,
    UvPivotField,
    UvSetField,
    UvptField,
    VrtsField,
    WireColorRGBField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.custom import Float3Field
from .....attr.define.std.at.compound import CompoundField
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.byte import ByteField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.float import FloatField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.numeric.range.short import ShortField
from .....attr.define.std.at.typed import TypedField
from .....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)
from .....attr.define.std.dt.matrix import DataMatrixField
from .....attr.define.std.dt.mesh import DataMeshField
from .....attr.define.std.dt.string import DataStringField


class ViewModeEnumPlugOperator(EnumPlugOperator["ViewModeEnumAttrOperator"]):
    __slots__ = ()

    FLAT = 0
    USE_TEMPLATE = 1
    GROUP_BY_NODE = 2


class ViewModeEnumAttrOperator(EnumAttrOperator[ViewModeEnumPlugOperator]):
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


class UiTreatmentEnumPlugOperator(
    EnumPlugOperator["UiTreatmentEnumAttrOperator"]
):
    __slots__ = ()

    STANDARD = 0
    SHADER = 1
    CUSTOM = 1000


class UiTreatmentEnumAttrOperator(
    EnumAttrOperator[UiTreatmentEnumPlugOperator]
):
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


class UseObjectColorEnumPlugOperator(
    EnumPlugOperator["UseObjectColorEnumAttrOperator"]
):
    __slots__ = ()

    DEFAULT = 0
    INDEXED = 1
    RGB = 2


class UseObjectColorEnumAttrOperator(
    EnumAttrOperator[UseObjectColorEnumPlugOperator]
):
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


class GhostingModeEnumPlugOperator(
    EnumPlugOperator["GhostingModeEnumAttrOperator"]
):
    __slots__ = ()

    PRE_AND_POST_FRAMES = 0
    PRE_FRAMES = 1
    POST_FRAMES = 2
    CUSTOM_FRAMES = 3
    PRE_AND_POST_KEYFRAMES = 4
    ALL_KEYFRAMES = 5


class GhostingModeEnumAttrOperator(
    EnumAttrOperator[GhostingModeEnumPlugOperator]
):
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


class SmoothDrawTypeEnumPlugOperator(
    EnumPlugOperator["SmoothDrawTypeEnumAttrOperator"]
):
    __slots__ = ()

    MAYA_CATMULL_MINUS_CLARK = 0
    OPENSUBDIV_CATMULL_MINUS_CLARK = 2
    OPENSUBDIV_CATMULL_MINUS_CLARK_ADAPTIVE = 3


class SmoothDrawTypeEnumAttrOperator(
    EnumAttrOperator[SmoothDrawTypeEnumPlugOperator]
):
    __slots__ = ()

    MAYA_CATMULL_MINUS_CLARK = 0
    OPENSUBDIV_CATMULL_MINUS_CLARK = 2
    OPENSUBDIV_CATMULL_MINUS_CLARK_ADAPTIVE = 3

    NAME_MAP = {
        MAYA_CATMULL_MINUS_CLARK: "Maya Catmull-Clark",
        OPENSUBDIV_CATMULL_MINUS_CLARK: "OpenSubdiv Catmull-Clark",
        OPENSUBDIV_CATMULL_MINUS_CLARK_ADAPTIVE: (
            "OpenSubdiv Catmull-Clark Adaptive"
        ),
    }


class SmoothDrawTypeEnumField(
    EnumField[SmoothDrawTypeEnumAttrOperator, SmoothDrawTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SmoothDrawTypeEnumAttrOperator
    PLUG_CLS = SmoothDrawTypeEnumPlugOperator


class DisplacementTypeEnumPlugOperator(
    EnumPlugOperator["DisplacementTypeEnumAttrOperator"]
):
    __slots__ = ()

    SCALAR = 0
    VECTOR_GLOBAL_SPACE = 1


class DisplacementTypeEnumAttrOperator(
    EnumAttrOperator[DisplacementTypeEnumPlugOperator]
):
    __slots__ = ()

    SCALAR = 0
    VECTOR_GLOBAL_SPACE = 1

    NAME_MAP = {
        SCALAR: "Scalar",
        VECTOR_GLOBAL_SPACE: "Vector (global space)",
    }


class DisplacementTypeEnumField(
    EnumField[
        DisplacementTypeEnumAttrOperator, DisplacementTypeEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DisplacementTypeEnumAttrOperator
    PLUG_CLS = DisplacementTypeEnumPlugOperator


class OsdVertBoundaryEnumPlugOperator(
    EnumPlugOperator["OsdVertBoundaryEnumAttrOperator"]
):
    __slots__ = ()

    SHARP_EDGES_AND_CORNERS = 1
    SHARP_EDGES = 2


class OsdVertBoundaryEnumAttrOperator(
    EnumAttrOperator[OsdVertBoundaryEnumPlugOperator]
):
    __slots__ = ()

    SHARP_EDGES_AND_CORNERS = 1
    SHARP_EDGES = 2

    NAME_MAP = {
        SHARP_EDGES_AND_CORNERS: "Sharp edges and corners",
        SHARP_EDGES: "Sharp edges",
    }


class OsdVertBoundaryEnumField(
    EnumField[OsdVertBoundaryEnumAttrOperator, OsdVertBoundaryEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OsdVertBoundaryEnumAttrOperator
    PLUG_CLS = OsdVertBoundaryEnumPlugOperator


class OsdFvarBoundaryEnumPlugOperator(
    EnumPlugOperator["OsdFvarBoundaryEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PRESERVE_EDGES_AND_CORNERS = 1
    PRESERVE_EDGES = 2
    MAYA_CATMULL_MINUS_CLARK = 3


class OsdFvarBoundaryEnumAttrOperator(
    EnumAttrOperator[OsdFvarBoundaryEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PRESERVE_EDGES_AND_CORNERS = 1
    PRESERVE_EDGES = 2
    MAYA_CATMULL_MINUS_CLARK = 3

    NAME_MAP = {
        NONE: "None",
        PRESERVE_EDGES_AND_CORNERS: "Preserve Edges and Corners",
        PRESERVE_EDGES: "Preserve Edges",
        MAYA_CATMULL_MINUS_CLARK: "Maya Catmull-Clark",
    }


class OsdFvarBoundaryEnumField(
    EnumField[OsdFvarBoundaryEnumAttrOperator, OsdFvarBoundaryEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OsdFvarBoundaryEnumAttrOperator
    PLUG_CLS = OsdFvarBoundaryEnumPlugOperator


class OsdCreaseMethodEnumPlugOperator(
    EnumPlugOperator["OsdCreaseMethodEnumAttrOperator"]
):
    __slots__ = ()

    NORMAL = 0
    CHAIKIN = 1


class OsdCreaseMethodEnumAttrOperator(
    EnumAttrOperator[OsdCreaseMethodEnumPlugOperator]
):
    __slots__ = ()

    NORMAL = 0
    CHAIKIN = 1

    NAME_MAP = {
        NORMAL: "Normal",
        CHAIKIN: "Chaikin",
    }


class OsdCreaseMethodEnumField(
    EnumField[OsdCreaseMethodEnumAttrOperator, OsdCreaseMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OsdCreaseMethodEnumAttrOperator
    PLUG_CLS = OsdCreaseMethodEnumPlugOperator


class BoundaryRuleEnumPlugOperator(
    EnumPlugOperator["BoundaryRuleEnumAttrOperator"]
):
    __slots__ = ()

    LEGACY = 0
    CREASE_ALL = 1
    CREASE_EDGES = 2


class BoundaryRuleEnumAttrOperator(
    EnumAttrOperator[BoundaryRuleEnumPlugOperator]
):
    __slots__ = ()

    LEGACY = 0
    CREASE_ALL = 1
    CREASE_EDGES = 2

    NAME_MAP = {
        LEGACY: "Legacy",
        CREASE_ALL: "Crease All",
        CREASE_EDGES: "Crease Edges",
    }


class BoundaryRuleEnumField(
    EnumField[BoundaryRuleEnumAttrOperator, BoundaryRuleEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoundaryRuleEnumAttrOperator
    PLUG_CLS = BoundaryRuleEnumPlugOperator


class KeepMapBordersEnumPlugOperator(
    EnumPlugOperator["KeepMapBordersEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    INTERNAL = 1
    ALL = 2


class KeepMapBordersEnumAttrOperator(
    EnumAttrOperator[KeepMapBordersEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    INTERNAL = 1
    ALL = 2

    NAME_MAP = {
        NONE: "None",
        INTERNAL: "Internal",
        ALL: "All",
    }


class KeepMapBordersEnumField(
    EnumField[KeepMapBordersEnumAttrOperator, KeepMapBordersEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KeepMapBordersEnumAttrOperator
    PLUG_CLS = KeepMapBordersEnumPlugOperator


class DisplayEdgesEnumPlugOperator(
    EnumPlugOperator["DisplayEdgesEnumAttrOperator"]
):
    __slots__ = ()

    STANDARD = 0
    SOFT_SLASH_HARD = 1
    HARD_COLOR = 2
    HARD = 3


class DisplayEdgesEnumAttrOperator(
    EnumAttrOperator[DisplayEdgesEnumPlugOperator]
):
    __slots__ = ()

    STANDARD = 0
    SOFT_SLASH_HARD = 1
    HARD_COLOR = 2
    HARD = 3

    NAME_MAP = {
        STANDARD: "Standard",
        SOFT_SLASH_HARD: "Soft/Hard",
        HARD_COLOR: "Hard (color)",
        HARD: "Hard",
    }


class DisplayEdgesEnumField(
    EnumField[DisplayEdgesEnumAttrOperator, DisplayEdgesEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplayEdgesEnumAttrOperator
    PLUG_CLS = DisplayEdgesEnumPlugOperator


class BackfaceCullingEnumPlugOperator(
    EnumPlugOperator["BackfaceCullingEnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    WIRE = 1
    HARD = 2
    FULL = 3


class BackfaceCullingEnumAttrOperator(
    EnumAttrOperator[BackfaceCullingEnumPlugOperator]
):
    __slots__ = ()

    OFF = 0
    WIRE = 1
    HARD = 2
    FULL = 3

    NAME_MAP = {
        OFF: "off",
        WIRE: "wire",
        HARD: "hard",
        FULL: "full",
    }


class BackfaceCullingEnumField(
    EnumField[BackfaceCullingEnumAttrOperator, BackfaceCullingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BackfaceCullingEnumAttrOperator
    PLUG_CLS = BackfaceCullingEnumPlugOperator


class NormalTypeEnumPlugOperator(
    EnumPlugOperator["NormalTypeEnumAttrOperator"]
):
    __slots__ = ()

    FACE = 1
    VTX = 2
    VTXFACE = 3


class NormalTypeEnumAttrOperator(EnumAttrOperator[NormalTypeEnumPlugOperator]):
    __slots__ = ()

    FACE = 1
    VTX = 2
    VTXFACE = 3

    NAME_MAP = {
        FACE: "face",
        VTX: "vtx",
        VTXFACE: "vtxface",
    }


class NormalTypeEnumField(
    EnumField[NormalTypeEnumAttrOperator, NormalTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalTypeEnumAttrOperator
    PLUG_CLS = NormalTypeEnumPlugOperator


class TangentSpaceEnumPlugOperator(
    EnumPlugOperator["TangentSpaceEnumAttrOperator"]
):
    __slots__ = ()

    DETECTWINDINGRIGHTHANDED = 0
    RIGHTHANDED = 1
    DETECTWINDINGLEFTHANDED = 2
    LEFTHANDED = 3


class TangentSpaceEnumAttrOperator(
    EnumAttrOperator[TangentSpaceEnumPlugOperator]
):
    __slots__ = ()

    DETECTWINDINGRIGHTHANDED = 0
    RIGHTHANDED = 1
    DETECTWINDINGLEFTHANDED = 2
    LEFTHANDED = 3

    NAME_MAP = {
        DETECTWINDINGRIGHTHANDED: "detectWindingRightHanded",
        RIGHTHANDED: "rightHanded",
        DETECTWINDINGLEFTHANDED: "detectWindingLeftHanded",
        LEFTHANDED: "leftHanded",
    }


class TangentSpaceEnumField(
    EnumField[TangentSpaceEnumAttrOperator, TangentSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentSpaceEnumAttrOperator
    PLUG_CLS = TangentSpaceEnumPlugOperator


class MaterialBlendEnumPlugOperator(
    EnumPlugOperator["MaterialBlendEnumAttrOperator"]
):
    __slots__ = ()

    OVERWRITE = 0
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    AVERAGE = 5
    MODULATE2X = 6


class MaterialBlendEnumAttrOperator(
    EnumAttrOperator[MaterialBlendEnumPlugOperator]
):
    __slots__ = ()

    OVERWRITE = 0
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    AVERAGE = 5
    MODULATE2X = 6

    NAME_MAP = {
        OVERWRITE: "overwrite",
        ADD: "add",
        SUBTRACT: "subtract",
        MULTIPLY: "multiply",
        DIVIDE: "divide",
        AVERAGE: "average",
        MODULATE2X: "modulate2x",
    }


class MaterialBlendEnumField(
    EnumField[MaterialBlendEnumAttrOperator, MaterialBlendEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaterialBlendEnumAttrOperator
    PLUG_CLS = MaterialBlendEnumPlugOperator


class DispResolutionEnumPlugOperator(
    EnumPlugOperator["DispResolutionEnumAttrOperator"]
):
    __slots__ = ()

    _0_BASE = 0
    _1 = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6_FINEST = 6


class DispResolutionEnumAttrOperator(
    EnumAttrOperator[DispResolutionEnumPlugOperator]
):
    __slots__ = ()

    _0_BASE = 0
    _1 = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6_FINEST = 6

    NAME_MAP = {
        _0_BASE: "0 (Base)",
        _1: "1",
        _2: "2",
        _3: "3",
        _4: "4",
        _5: "5",
        _6_FINEST: "6 (Finest)",
    }


class DispResolutionEnumField(
    EnumField[DispResolutionEnumAttrOperator, DispResolutionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DispResolutionEnumAttrOperator
    PLUG_CLS = DispResolutionEnumPlugOperator


class DisplaySmoothMeshEnumPlugOperator(
    EnumPlugOperator["DisplaySmoothMeshEnumAttrOperator"]
):
    __slots__ = ()

    BASE_MESH_ONLY = 0
    BASE_AND_SMOOTH_MESH = 1
    SMOOTH_MESH_ONLY = 2


class DisplaySmoothMeshEnumAttrOperator(
    EnumAttrOperator[DisplaySmoothMeshEnumPlugOperator]
):
    __slots__ = ()

    BASE_MESH_ONLY = 0
    BASE_AND_SMOOTH_MESH = 1
    SMOOTH_MESH_ONLY = 2

    NAME_MAP = {
        BASE_MESH_ONLY: "Base Mesh Only",
        BASE_AND_SMOOTH_MESH: "Base and Smooth Mesh",
        SMOOTH_MESH_ONLY: "Smooth Mesh Only",
    }


class DisplaySmoothMeshEnumField(
    EnumField[
        DisplaySmoothMeshEnumAttrOperator, DisplaySmoothMeshEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DisplaySmoothMeshEnumAttrOperator
    PLUG_CLS = DisplaySmoothMeshEnumPlugOperator


class SmoothMeshSelectionModeEnumPlugOperator(
    EnumPlugOperator["SmoothMeshSelectionModeEnumAttrOperator"]
):
    __slots__ = ()

    BASE_CAGE = 0
    PROJECTED_CAGE = 1
    BASE_AND_PROJECTED_CAGE = 2


class SmoothMeshSelectionModeEnumAttrOperator(
    EnumAttrOperator[SmoothMeshSelectionModeEnumPlugOperator]
):
    __slots__ = ()

    BASE_CAGE = 0
    PROJECTED_CAGE = 1
    BASE_AND_PROJECTED_CAGE = 2

    NAME_MAP = {
        BASE_CAGE: "Base Cage",
        PROJECTED_CAGE: "Projected Cage",
        BASE_AND_PROJECTED_CAGE: "Base and Projected Cage",
    }


class SmoothMeshSelectionModeEnumField(
    EnumField[
        SmoothMeshSelectionModeEnumAttrOperator,
        SmoothMeshSelectionModeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = SmoothMeshSelectionModeEnumAttrOperator
    PLUG_CLS = SmoothMeshSelectionModeEnumPlugOperator


class QuadSplitEnumPlugOperator(EnumPlugOperator["QuadSplitEnumAttrOperator"]):
    __slots__ = ()

    LEFT = 0
    RIGHT = 1
    BEST_SHAPE = 2


class QuadSplitEnumAttrOperator(EnumAttrOperator[QuadSplitEnumPlugOperator]):
    __slots__ = ()

    LEFT = 0
    RIGHT = 1
    BEST_SHAPE = 2

    NAME_MAP = {
        LEFT: "Left",
        RIGHT: "Right",
        BEST_SHAPE: "Best Shape",
    }


class QuadSplitEnumField(
    EnumField[QuadSplitEnumAttrOperator, QuadSplitEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = QuadSplitEnumAttrOperator
    PLUG_CLS = QuadSplitEnumPlugOperator


class VertexNormalMethodEnumPlugOperator(
    EnumPlugOperator["VertexNormalMethodEnumAttrOperator"]
):
    __slots__ = ()

    UNWEIGHTED = 0
    ANGLE_WEIGHTED = 1
    AREA_WEIGHTED = 2
    ANGLE_AND_AREA_WEIGHTED = 3


class VertexNormalMethodEnumAttrOperator(
    EnumAttrOperator[VertexNormalMethodEnumPlugOperator]
):
    __slots__ = ()

    UNWEIGHTED = 0
    ANGLE_WEIGHTED = 1
    AREA_WEIGHTED = 2
    ANGLE_AND_AREA_WEIGHTED = 3

    NAME_MAP = {
        UNWEIGHTED: "Unweighted",
        ANGLE_WEIGHTED: "Angle Weighted",
        AREA_WEIGHTED: "Area Weighted",
        ANGLE_AND_AREA_WEIGHTED: "Angle And Area Weighted",
    }


class VertexNormalMethodEnumField(
    EnumField[
        VertexNormalMethodEnumAttrOperator, VertexNormalMethodEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = VertexNormalMethodEnumAttrOperator
    PLUG_CLS = VertexNormalMethodEnumPlugOperator


class VertexColorSourceEnumPlugOperator(
    EnumPlugOperator["VertexColorSourceEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    CURRENT_COLOR_SET = 1
    INFLUENCE_COLORS = 2


class VertexColorSourceEnumAttrOperator(
    EnumAttrOperator[VertexColorSourceEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    CURRENT_COLOR_SET = 1
    INFLUENCE_COLORS = 2

    NAME_MAP = {
        NONE: "None",
        CURRENT_COLOR_SET: "Current Color Set",
        INFLUENCE_COLORS: "Influence Colors",
    }


class VertexColorSourceEnumField(
    EnumField[
        VertexColorSourceEnumAttrOperator, VertexColorSourceEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = VertexColorSourceEnumAttrOperator
    PLUG_CLS = VertexColorSourceEnumPlugOperator


class AiSubdivTypeEnumPlugOperator(
    EnumPlugOperator["AiSubdivTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    CATCLARK = 1
    LINEAR = 2


class AiSubdivTypeEnumAttrOperator(
    EnumAttrOperator[AiSubdivTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    CATCLARK = 1
    LINEAR = 2

    NAME_MAP = {
        NONE: "none",
        CATCLARK: "catclark",
        LINEAR: "linear",
    }


class AiSubdivTypeEnumField(
    EnumField[AiSubdivTypeEnumAttrOperator, AiSubdivTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiSubdivTypeEnumAttrOperator
    PLUG_CLS = AiSubdivTypeEnumPlugOperator


class AiSubdivAdaptiveMetricEnumPlugOperator(
    EnumPlugOperator["AiSubdivAdaptiveMetricEnumAttrOperator"]
):
    __slots__ = ()

    AUTO = 0
    EDGE_LENGTH = 1
    FLATNESS = 2


class AiSubdivAdaptiveMetricEnumAttrOperator(
    EnumAttrOperator[AiSubdivAdaptiveMetricEnumPlugOperator]
):
    __slots__ = ()

    AUTO = 0
    EDGE_LENGTH = 1
    FLATNESS = 2

    NAME_MAP = {
        AUTO: "auto",
        EDGE_LENGTH: "edge_length",
        FLATNESS: "flatness",
    }


class AiSubdivAdaptiveMetricEnumField(
    EnumField[
        AiSubdivAdaptiveMetricEnumAttrOperator,
        AiSubdivAdaptiveMetricEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = AiSubdivAdaptiveMetricEnumAttrOperator
    PLUG_CLS = AiSubdivAdaptiveMetricEnumPlugOperator


class AiSubdivAdaptiveSpaceEnumPlugOperator(
    EnumPlugOperator["AiSubdivAdaptiveSpaceEnumAttrOperator"]
):
    __slots__ = ()

    RASTER = 0
    OBJECT = 1


class AiSubdivAdaptiveSpaceEnumAttrOperator(
    EnumAttrOperator[AiSubdivAdaptiveSpaceEnumPlugOperator]
):
    __slots__ = ()

    RASTER = 0
    OBJECT = 1

    NAME_MAP = {
        RASTER: "raster",
        OBJECT: "object",
    }


class AiSubdivAdaptiveSpaceEnumField(
    EnumField[
        AiSubdivAdaptiveSpaceEnumAttrOperator,
        AiSubdivAdaptiveSpaceEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = AiSubdivAdaptiveSpaceEnumAttrOperator
    PLUG_CLS = AiSubdivAdaptiveSpaceEnumPlugOperator


class AiSubdivUvSmoothingEnumPlugOperator(
    EnumPlugOperator["AiSubdivUvSmoothingEnumAttrOperator"]
):
    __slots__ = ()

    PIN_CORNERS = 0
    PIN_BORDERS = 1
    LINEAR = 2
    SMOOTH = 3


class AiSubdivUvSmoothingEnumAttrOperator(
    EnumAttrOperator[AiSubdivUvSmoothingEnumPlugOperator]
):
    __slots__ = ()

    PIN_CORNERS = 0
    PIN_BORDERS = 1
    LINEAR = 2
    SMOOTH = 3

    NAME_MAP = {
        PIN_CORNERS: "pin_corners",
        PIN_BORDERS: "pin_borders",
        LINEAR: "linear",
        SMOOTH: "smooth",
    }


class AiSubdivUvSmoothingEnumField(
    EnumField[
        AiSubdivUvSmoothingEnumAttrOperator,
        AiSubdivUvSmoothingEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = AiSubdivUvSmoothingEnumAttrOperator
    PLUG_CLS = AiSubdivUvSmoothingEnumPlugOperator


class AiMotionVectorUnitEnumPlugOperator(
    EnumPlugOperator["AiMotionVectorUnitEnumAttrOperator"]
):
    __slots__ = ()

    PER_FRAME = 0
    PER_SECOND = 1


class AiMotionVectorUnitEnumAttrOperator(
    EnumAttrOperator[AiMotionVectorUnitEnumPlugOperator]
):
    __slots__ = ()

    PER_FRAME = 0
    PER_SECOND = 1

    NAME_MAP = {
        PER_FRAME: "Per Frame",
        PER_SECOND: "Per Second",
    }


class AiMotionVectorUnitEnumField(
    EnumField[
        AiMotionVectorUnitEnumAttrOperator, AiMotionVectorUnitEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiMotionVectorUnitEnumAttrOperator
    PLUG_CLS = AiMotionVectorUnitEnumPlugOperator


class GeneratedMesh(Shape):
    __slots__ = ()

    NODE_TYPE = "mesh"

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

    renderLayerInfo = RenderLayerInfoField(
        multi=True, default_value=(0.0, 1.0, 0.0)
    )
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

    ghostOpacityRange = GhostOpacityRangeField(
        default_value=(0.15000000596046448, 0.5),
        min_value=(0.0, 0.0),
        max_value=(1.0, 1.0),
    )
    golr = ghostOpacityRange
    ghostFarOpacity = ghostOpacityRange.ghostFarOpacity
    gfro = ghostFarOpacity
    ghostNearOpacity = ghostOpacityRange.ghostNearOpacity
    gnro = ghostNearOpacity

    ghostColorPre = GhostColorPreField(
        default_value=(0.44699999690055847, 1.0, 1.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
    gcp = ghostColorPre
    ghostColorPreR = ghostColorPre.ghostColorPreR
    grr = ghostColorPreR
    ghostColorPreG = ghostColorPre.ghostColorPreG
    gpg = ghostColorPreG
    ghostColorPreB = ghostColorPre.ghostColorPreB
    gpb = ghostColorPreB

    ghostColorPost = GhostColorPostField(
        default_value=(
            0.878000020980835,
            0.6779999732971191,
            0.6629999876022339,
        ),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
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

    hardwareFogMultiplier = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
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

    maxVisibilitySamples = LongField(
        default_value=1, min_value=1, max_value=32, soft_max_value=20
    )
    mvs = maxVisibilitySamples

    geometryAntialiasingOverride = BoolField(default_value=False)
    gao = geometryAntialiasingOverride

    antialiasingLevel = LongField(
        default_value=1, min_value=1, max_value=5, soft_max_value=5
    )
    gal = antialiasingLevel

    shadingSamplesOverride = BoolField(default_value=False)
    sso = shadingSamplesOverride

    shadingSamples = LongField(default_value=1, min_value=1, max_value=32)
    ssa = shadingSamples

    maxShadingSamples = LongField(
        default_value=1, min_value=1, max_value=32, soft_max_value=20
    )
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

    controlPoints = ControlPointsField(
        multi=True, default_value=(0.0, 0.0, 0.0)
    )
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

    boundingBoxScale = BoundingBoxScaleField(
        default_value=(1.5, 1.5, 1.5), min_value=(1.0, 1.0, 1.0)
    )
    bbs = boundingBoxScale
    boundingBoxScaleX = boundingBoxScale.boundingBoxScaleX
    bscx = boundingBoxScaleX
    boundingBoxScaleY = boundingBoxScale.boundingBoxScaleY
    bscy = boundingBoxScaleY
    boundingBoxScaleZ = boundingBoxScale.boundingBoxScaleZ
    bscz = boundingBoxScaleZ

    featureDisplacement = BoolField(default_value=True)
    fbda = featureDisplacement

    initialSampleRate = LongField(
        default_value=6, min_value=0, soft_max_value=100
    )
    dsr = initialSampleRate

    extraSampleRate = LongField(
        default_value=5, min_value=0, soft_max_value=50
    )
    xsr = extraSampleRate

    textureThreshold = LongField(default_value=0, min_value=0, max_value=100)
    fth = textureThreshold

    normalThreshold = FloatField(
        default_value=30.0, min_value=0.0, max_value=180.0
    )
    nat = normalThreshold

    displayHWEnvironment = BoolField(default_value=False)
    dhe = displayHWEnvironment

    collisionOffsetVelocityIncrement = CollisionOffsetVelocityIncrementField(
        multi=True, default_value=(0.0, 0.0, 0.0)
    )
    covi = collisionOffsetVelocityIncrement

    collisionDepthVelocityIncrement = CollisionDepthVelocityIncrementField(
        multi=True, default_value=(0.0, 0.0, 0.0)
    )
    cdvi = collisionDepthVelocityIncrement

    collisionOffsetVelocityMultiplier = CollisionOffsetVelocityMultiplierField(
        multi=True, default_value=(0.0, 0.0, 0.0)
    )
    covm = collisionOffsetVelocityMultiplier

    collisionDepthVelocityMultiplier = CollisionDepthVelocityMultiplierField(
        multi=True, default_value=(0.0, 0.0, 0.0)
    )
    cdvm = collisionDepthVelocityMultiplier

    inMesh = DataMeshField()
    i = inMesh

    outMesh = DataMeshField()
    o = outMesh

    outGeometryClean = MessageField()
    ogc = outGeometryClean

    cachedInMesh = DataMeshField()
    ci = cachedInMesh

    worldMesh = DataMeshField(multi=True, writable=False)
    w = worldMesh

    outSmoothMesh = DataMeshField()
    os = outSmoothMesh

    cachedSmoothMesh = DataMeshField()
    cs = cachedSmoothMesh

    smoothWarn = BoolField(default_value=True)
    sw = smoothWarn

    smoothLevel = ShortField(
        default_value=2,
        min_value=0,
        max_value=15,
        soft_min_value=0,
        soft_max_value=4,
    )
    lev = smoothLevel

    smoothDrawType = SmoothDrawTypeEnumField(default_value=2)
    sdt = smoothDrawType

    useGlobalSmoothDrawType = BoolField(default_value=True)
    ugsdt = useGlobalSmoothDrawType

    outSmoothMeshSubdError = ShortField(default_value=0, writable=False)
    osde = outSmoothMeshSubdError

    showDisplacements = BoolField(default_value=False)
    sdis = showDisplacements

    displacementType = DisplacementTypeEnumField(default_value=0)
    dist = displacementType

    loadTiledTextures = BoolField(default_value=False)
    ltt = loadTiledTextures

    enableOpenCL = BoolField(default_value=True)
    eocl = enableOpenCL

    smoothTessLevel = ShortField(default_value=7, min_value=1, max_value=10)
    stlv = smoothTessLevel

    smoothOsdColorizePatches = BoolField(default_value=False)
    socp = smoothOsdColorizePatches

    useOsdBoundaryMethods = BoolField(default_value=True)
    uob = useOsdBoundaryMethods

    osdVertBoundary = OsdVertBoundaryEnumField(default_value=1)
    ovb = osdVertBoundary

    osdFvarBoundary = OsdFvarBoundaryEnumField(default_value=3)
    ofb = osdFvarBoundary

    osdFvarPropagateCorners = BoolField(default_value=False)
    ofc = osdFvarPropagateCorners

    osdSmoothTriangles = BoolField(default_value=False)
    ost = osdSmoothTriangles

    osdCreaseMethod = OsdCreaseMethodEnumField(default_value=0)
    ocr = osdCreaseMethod

    osdIndependentUVChannels = BoolField(default_value=True)
    iuv = osdIndependentUVChannels

    continuity = FloatField(
        default_value=1.0,
        min_value=0.0,
        max_value=1.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
    co = continuity

    smoothUVs = BoolField(default_value=True)
    suv = smoothUVs

    keepBorder = BoolField(default_value=False)
    kb = keepBorder

    boundaryRule = BoundaryRuleEnumField(default_value=1)
    bnr = boundaryRule

    keepHardEdge = BoolField(default_value=False)
    khe = keepHardEdge

    propagateEdgeHardness = BoolField(default_value=False)
    peh = propagateEdgeHardness

    keepMapBorders = KeepMapBordersEnumField(default_value=1)
    kmb = keepMapBorders

    smoothOffset = SmoothOffsetField(default_value=(0.0, 0.0, 0.0))
    so = smoothOffset
    sofx = smoothOffset.sofx
    sx = sofx
    sofy = smoothOffset.sofy
    sy = sofy
    sofz = smoothOffset.sofz
    sz = sofz

    displaySubdComps = BoolField(default_value=False)
    dsc = displaySubdComps

    useSmoothPreviewForRender = BoolField(default_value=True)
    uspr = useSmoothPreviewForRender

    renderSmoothLevel = ShortField(
        default_value=2, min_value=0, max_value=7, soft_max_value=4
    )
    rsl = renderSmoothLevel

    useMaxEdgeLength = BoolField(default_value=False)
    uxe = useMaxEdgeLength

    useMinEdgeLength = BoolField(default_value=False)
    uie = useMinEdgeLength

    useMaxSubdivisions = BoolField(default_value=False)
    uxs = useMaxSubdivisions

    useMaxUV = BoolField(default_value=False)
    uxu = useMaxUV

    useMinScreen = BoolField(default_value=True)
    uns = useMinScreen

    useNumTriangles = BoolField(default_value=False)
    unp = useNumTriangles

    numTriangles = LongField(default_value=100)
    nt = numTriangles

    maxEdgeLength = FloatField(default_value=0.10000000149011612)
    mxe = maxEdgeLength

    minEdgeLength = FloatField(default_value=0.009999999776482582)
    mne = minEdgeLength

    maxSubd = LongField(default_value=5)
    mxs = maxSubd

    maxUv = FloatField(default_value=0.5)
    xuv = maxUv

    minScreen = FloatField(default_value=14.0)
    mns = minScreen

    maxTriangles = LongField(default_value=60000, min_value=1)
    tsl = maxTriangles

    pnts = PntsField(multi=True, default_value=(0.0, 0.0, 0.0))
    pt = pnts

    vrts = VrtsField(multi=True, default_value=(0.0, 0.0, 0.0))
    vt = vrts

    edge = EdgeField(multi=True, default_value=(0, 0, 0))
    ed = edge

    uvpt = UvptField(multi=True, default_value=(0.0, 0.0))
    uv = uvpt

    colors = ColorsField(multi=True, default_value=(0.0, 0.0, 0.0, 0.0))
    clr = colors

    normals = NormalsField(
        multi=True,
        default_value=(
            1.0000000200408773e20,
            1.0000000200408773e20,
            1.0000000200408773e20,
        ),
    )
    n = normals

    face = TypedField(multi=True)
    fc = face

    faceColorIndices = TypedField(multi=True)
    fcid = faceColorIndices

    creaseData = TypedField()
    cd = creaseData

    creaseVertexData = TypedField()
    cvd = creaseVertexData

    pinData = TypedField(multi=True)
    pd = pinData

    holeFaceData = TypedField()
    hfd = holeFaceData

    colorPerVertex = ColorPerVertexField()
    cpvx = colorPerVertex
    vertexColor = colorPerVertex.vertexColor
    vclr = vertexColor

    vertexColorRGB = Float3Field()
    vrgb = vertexColorRGB

    vertexColorR = FloatField()
    vxcr = vertexColorR

    vertexColorG = FloatField()
    vxcg = vertexColorG

    vertexColorB = FloatField()
    vxcb = vertexColorB

    vertexAlpha = FloatField()
    vxal = vertexAlpha

    vertexFaceColor = CompoundField()
    vfcl = vertexFaceColor

    vertexFaceColorRGB = Float3Field()
    frgb = vertexFaceColorRGB

    vertexFaceColorR = FloatField()
    vfcr = vertexFaceColorR

    vertexFaceColorG = FloatField()
    vfcg = vertexFaceColorG

    vertexFaceColorB = FloatField()
    vfcb = vertexFaceColorB

    vertexFaceAlpha = FloatField()
    vfal = vertexFaceAlpha

    normalPerVertex = NormalPerVertexField()
    npvx = normalPerVertex
    vertexNormal = normalPerVertex.vertexNormal
    vn = vertexNormal

    vertexNormalXYZ = Float3Field()
    nxyz = vertexNormalXYZ

    vertexNormalX = FloatField()
    vxnx = vertexNormalX

    vertexNormalY = FloatField()
    vxny = vertexNormalY

    vertexNormalZ = FloatField()
    vxnz = vertexNormalZ

    vertexFaceNormal = CompoundField()
    vfnl = vertexFaceNormal

    vertexFaceNormalXYZ = Float3Field()
    fnxy = vertexFaceNormalXYZ

    vertexFaceNormalX = FloatField()
    vfnx = vertexFaceNormalX

    vertexFaceNormalY = FloatField()
    vfny = vertexFaceNormalY

    vertexFaceNormalZ = FloatField()
    vfnz = vertexFaceNormalZ

    displayVertices = BoolField(default_value=False)
    dv = displayVertices

    displayBorders = BoolField(default_value=False)
    db = displayBorders

    displayMapBorders = BoolField(default_value=False)
    dmb = displayMapBorders

    displayEdges = DisplayEdgesEnumField(default_value=0)
    de = displayEdges

    displayFacesWithGroupId = LongField(default_value=-2)
    dfgi = displayFacesWithGroupId

    displayCenter = BoolField(default_value=False)
    dc = displayCenter

    displayTriangles = BoolField(default_value=False)
    dt = displayTriangles

    displayUVs = BoolField(default_value=False)
    duv = displayUVs

    displayItemNumbers = LongField(default_value=0)
    din = displayItemNumbers

    displayNonPlanar = BoolField(default_value=False)
    dnp = displayNonPlanar

    backfaceCulling = BackfaceCullingEnumField(default_value=0)
    bck = backfaceCulling

    vertexBackfaceCulling = BoolField(default_value=True)
    vbc = vertexBackfaceCulling

    vertexSize = DoubleField(default_value=3.0)
    vs = vertexSize

    uvSize = DoubleField(default_value=4.0)
    usz = uvSize

    borderWidth = DoubleField(default_value=2.0)
    bw = borderWidth

    normalSize = DoubleField(default_value=0.4)
    ns = normalSize

    normalType = NormalTypeEnumField(default_value=1)
    ndt = normalType

    displayNormal = BoolField(default_value=False)
    dn = displayNormal

    displayTangent = BoolField(default_value=False)
    dtn = displayTangent

    tangentSpace = TangentSpaceEnumField(default_value=0)
    tgsp = tangentSpace

    tangentSmoothingAngle = DoubleAngleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=180.0
    )
    tsa = tangentSmoothingAngle

    tangentNormalThreshold = DoubleAngleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=180.0
    )
    tnt = tangentNormalThreshold

    allowTopologyMod = BoolField(default_value=True)
    atm = allowTopologyMod

    materialBlend = MaterialBlendEnumField(default_value=0)
    matb = materialBlend

    uvTweakLocation = TypedField(readable=False)
    uvtl = uvTweakLocation

    userTrg = DataStringField()
    utrg = userTrg

    dispResolution = DispResolutionEnumField(default_value=0)
    dr = dispResolution

    vertexIdMap = BoolField(default_value=False)
    vmap = vertexIdMap

    edgeIdMap = BoolField(default_value=False)
    emap = edgeIdMap

    faceIdMap = BoolField(default_value=False)
    fmap = faceIdMap

    displaySmoothMesh = DisplaySmoothMeshEnumField(default_value=0)
    dsm = displaySmoothMesh

    smoothMeshSelectionMode = SmoothMeshSelectionModeEnumField(default_value=0)
    ssm = smoothMeshSelectionMode

    inForceNodeUVUpdate = BoolField(default_value=False)
    ifuv = inForceNodeUVUpdate

    outForceNodeUVUpdate = BoolField(default_value=False)
    ofuv = outForceNodeUVUpdate

    alwaysDrawOnTop = BoolField(default_value=False)
    adot = alwaysDrawOnTop

    reuseTriangles = BoolField(default_value=False)
    rtri = reuseTriangles

    quadSplit = QuadSplitEnumField(default_value=2)
    qsp = quadSplit

    vertexNormalMethod = VertexNormalMethodEnumField(default_value=3)
    vnm = vertexNormalMethod

    perInstanceIndex = LongField(multi=True, default_value=-1)
    pii = perInstanceIndex

    perInstanceTag = LongField(multi=True, default_value=-1)
    pit = perInstanceTag

    displayAlphaAsGreyScale = BoolField(default_value=False)
    dags = displayAlphaAsGreyScale

    displayColorAsGreyScale = BoolField(default_value=False)
    dcgs = displayColorAsGreyScale

    displayRedColorChannel = BoolField(default_value=True)
    dred = displayRedColorChannel

    displayGreenColorChannel = BoolField(default_value=True)
    dgrn = displayGreenColorChannel

    displayBlueColorChannel = BoolField(default_value=True)
    dblu = displayBlueColorChannel

    displayInvisibleFaces = BoolField(default_value=False)
    difs = displayInvisibleFaces

    useMeshSculptCache = BoolField(default_value=False)
    umsc = useMeshSculptCache

    computeFromSculptCache = BoolField(default_value=False)
    cfsc = computeFromSculptCache

    useMeshTexSculptCache = BoolField(default_value=False)
    umtsc = useMeshTexSculptCache

    freeze = FloatField(multi=True, default_value=0.0)
    frze = freeze

    motionVectorColorSet = DataStringField()
    mvcs = motionVectorColorSet

    vertexColorSource = VertexColorSourceEnumField(default_value=0)
    vcs = vertexColorSource

    mikktspaceTangentGen = BoolField(default_value=False)
    mttg = mikktspaceTangentGen

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiSelfShadows = BoolField(default_value=True, category="arnold")
    ai_self_shadows = aiSelfShadows

    aiOpaque = BoolField(default_value=True, category="arnold")
    ai_opaque = aiOpaque

    aiMatte = BoolField(default_value=False, category="arnold")
    ai_matte = aiMatte

    aiTraceSets = DataStringField(category="arnold")
    trace_sets = aiTraceSets

    aiSssSetname = DataStringField(category="arnold")
    ai_sss_setname = aiSssSetname

    aiToonId = DataStringField(category="arnold")
    ai_toon_id = aiToonId

    aiVisibleInDiffuseReflection = BoolField(
        default_value=True, category="arnold"
    )
    ai_vidr = aiVisibleInDiffuseReflection

    aiVisibleInSpecularReflection = BoolField(
        default_value=True, category="arnold"
    )
    ai_visr = aiVisibleInSpecularReflection

    aiVisibleInDiffuseTransmission = BoolField(
        default_value=True, category="arnold"
    )
    ai_vidt = aiVisibleInDiffuseTransmission

    aiVisibleInSpecularTransmission = BoolField(
        default_value=True, category="arnold"
    )
    ai_vist = aiVisibleInSpecularTransmission

    aiVisibleInVolume = BoolField(default_value=True, category="arnold")
    ai_viv = aiVisibleInVolume

    aiSubdivType = AiSubdivTypeEnumField(default_value=0, category="arnold")
    ai_subdiv_type = aiSubdivType

    aiSubdivIterations = ByteField(
        default_value=1,
        min_value=0,
        max_value=100,
        soft_min_value=0,
        soft_max_value=10,
        category="arnold",
    )
    ai_subdiv_iterations = aiSubdivIterations

    aiSubdivAdaptiveMetric = AiSubdivAdaptiveMetricEnumField(
        default_value=0, category="arnold"
    )
    ai_subdiv_adaptive_metric = aiSubdivAdaptiveMetric

    aiSubdivPixelError = FloatField(
        default_value=0.0,
        min_value=0.0,
        soft_max_value=10.0,
        category="arnold",
    )
    ai_subdiv_adaptive_error = aiSubdivPixelError

    aiSubdivAdaptiveSpace = AiSubdivAdaptiveSpaceEnumField(
        default_value=0, category="arnold"
    )
    ai_subdiv_adaptive_space = aiSubdivAdaptiveSpace

    aiSubdivUvSmoothing = AiSubdivUvSmoothingEnumField(
        default_value=0, category="arnold"
    )
    ai_subdiv_uv_smoothing = aiSubdivUvSmoothing

    aiSubdivSmoothDerivs = BoolField(default_value=False, category="arnold")
    ai_subdiv_smooth_derivs = aiSubdivSmoothDerivs

    aiSubdivFrustumIgnore = BoolField(default_value=False, category="arnold")
    ai_subdiv_frustum_ignore = aiSubdivFrustumIgnore

    aiDispHeight = FloatField(default_value=1.0, category="arnold")
    ai_disp_height = aiDispHeight

    aiDispPadding = FloatField(default_value=0.0, category="arnold")
    ai_disp_padding = aiDispPadding

    aiDispZeroValue = FloatField(default_value=0.0, category="arnold")
    ai_disp_zero_value = aiDispZeroValue

    aiDispAutobump = BoolField(default_value=False, category="arnold")
    ai_disp_autobump = aiDispAutobump

    aiAutobumpVisibility = ByteField(
        default_value=1, min_value=0, max_value=255, category="arnold"
    )
    ai_autobump_visibility = aiAutobumpVisibility

    aiExportTangents = BoolField(default_value=False, category="arnold")
    ai_exptan = aiExportTangents

    aiExportColors = BoolField(default_value=False, category="arnold")
    ai_expcol = aiExportColors

    aiExportRefPoints = BoolField(default_value=True, category="arnold")
    ai_exprpt = aiExportRefPoints

    aiExportRefNormals = BoolField(default_value=False, category="arnold")
    ai_exprnrm = aiExportRefNormals

    aiExportRefTangents = BoolField(default_value=False, category="arnold")
    ai_exprtan = aiExportRefTangents

    aiStepSize = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0, category="arnold"
    )
    ai_step_size = aiStepSize

    aiVolumePadding = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0, category="arnold"
    )
    ai_volume_padding = aiVolumePadding

    aiMotionVectorSource = DataStringField(category="arnold")
    ai_motion_vector_source = aiMotionVectorSource

    aiMotionVectorUnit = AiMotionVectorUnitEnumField(
        default_value=0, category="arnold"
    )
    ai_motion_vector_unit = aiMotionVectorUnit

    aiMotionVectorScale = FloatField(
        default_value=1.0,
        soft_min_value=0.0,
        soft_max_value=2.0,
        category="arnold",
    )
    ai_motion_vector_scale = aiMotionVectorScale

    dso = DataStringField(category="arnold")

    data = DataStringField(category="arnold")

    aiOverrideLightLinking = BoolField(default_value=True, category="arnold")
    ai_override_light_linking = aiOverrideLightLinking

    aiOverrideShaders = BoolField(default_value=True, category="arnold")
    ai_override_shaders = aiOverrideShaders

    aiUseFrameExtension = BoolField(default_value=False, category="arnold")
    ai_use_frame_extension = aiUseFrameExtension

    aiFrameNumber = LongField(default_value=0, category="arnold")
    ai_frame_number = aiFrameNumber

    aiUseSubFrame = BoolField(default_value=False, category="arnold")
    ai_use_sub_frame = aiUseSubFrame

    aiFrameOffset = FloatField(default_value=0.0, category="arnold")
    ai_frame_offset = aiFrameOffset

    aiOverrideNodes = BoolField(default_value=False, category="arnold")
    ai_override_nodes = aiOverrideNodes

    aiNamespace = DataStringField(category="arnold")
    ai_namespace = aiNamespace

    aiOverrideReceiveShadows = BoolField(
        default_value=False, category="arnold"
    )
    ai_override_receive_shadows = aiOverrideReceiveShadows

    aiOverrideDoubleSided = BoolField(default_value=False, category="arnold")
    ai_override_double_sided = aiOverrideDoubleSided

    aiOverrideSelfShadows = BoolField(default_value=False, category="arnold")
    ai_override_self_shadows = aiOverrideSelfShadows

    aiOverrideOpaque = BoolField(default_value=False, category="arnold")
    ai_override_opaque = aiOverrideOpaque

    aiOverrideMatte = BoolField(default_value=False, category="arnold")
    ai_override_matte = aiOverrideMatte

    aiCastShadows = BoolField(default_value=True, category="arnold")
    ai_cast_shadows = aiCastShadows

    aiShadowDensity = FloatField(
        default_value=1.0,
        min_value=0.0,
        max_value=1.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
        category="arnold",
    )
    ai_shadow_density = aiShadowDensity

    aiExposure = FloatField(
        default_value=0.0,
        soft_min_value=-5.0,
        soft_max_value=5.0,
        category="arnold",
    )
    ai_exposure = aiExposure

    aiSamples = LongField(default_value=1, category="arnold")
    ai_samples = aiSamples

    aiNormalize = BoolField(default_value=True, category="arnold")
    ai_normalize = aiNormalize

    aiFilters = MessageField(multi=True, category="arnold")
    ai_filters = aiFilters

    aiDiffuse = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0, category="arnold"
    )
    ai_diffuse = aiDiffuse

    aiSpecular = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0, category="arnold"
    )
    ai_specular = aiSpecular

    aiSss = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0, category="arnold"
    )
    ai_sss = aiSss

    aiIndirect = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0, category="arnold"
    )
    ai_indirect = aiIndirect

    aiVolume = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0, category="arnold"
    )
    ai_volume = aiVolume

    aiMaxBounces = LongField(default_value=999, category="arnold")
    ai_max_bounces = aiMaxBounces

    aiVolumeSamples = LongField(default_value=2, category="arnold")
    ai_volume_samples = aiVolumeSamples

    aiAov = DataStringField(category="arnold")
    ai_aov = aiAov

    aiUseColorTemperature = BoolField(default_value=False, category="arnold")
    ai_use_color_temperature = aiUseColorTemperature

    aiColorTemperature = FloatField(
        default_value=6500.0,
        min_value=0.0,
        soft_min_value=1000.0,
        soft_max_value=15000.0,
        category="arnold",
    )
    ai_color_temperature = aiColorTemperature

    aiShadowColor = AiShadowColorField(
        default_value=(0.0, 0.0, 0.0), category="arnold"
    )
    ai_shadow_color = aiShadowColor
    aiShadowColorR = aiShadowColor.aiShadowColorR
    ai_shadow_colorr = aiShadowColorR
    aiShadowColorG = aiShadowColor.aiShadowColorG
    ai_shadow_colorg = aiShadowColorG
    aiShadowColorB = aiShadowColor.aiShadowColorB
    ai_shadow_colorb = aiShadowColorB

    aiCastVolumetricShadows = BoolField(default_value=True, category="arnold")
    ai_cast_volumetric_shadows = aiCastVolumetricShadows

    color = ColorField(default_value=(1.0, 1.0, 1.0), category="arnold")
    sc = color
    colorRed = color.colorRed
    scr = colorRed
    colorGreen = color.colorGreen
    scg = colorGreen
    colorBlue = color.colorBlue
    scb = colorBlue

    intensity = FloatField(default_value=1.0, category="arnold")

    lightVisible = BoolField(default_value=False, category="arnold")
    light_visible = lightVisible

    aiTranslator = DataStringField(category="arnold")
    ai_translator = aiTranslator
