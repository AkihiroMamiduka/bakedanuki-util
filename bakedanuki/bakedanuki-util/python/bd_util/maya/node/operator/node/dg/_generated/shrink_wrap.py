# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.shrink_wrap import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    WeightListField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ....attr.define.std.dt.mesh import DataMeshField


class BoundaryRuleEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LEGACY = 0
    CREASE_ALL = 1
    CREASE_EDGES = 2


class BoundaryRuleEnumAttrOperator(EnumAttrOperator):
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


class KeepMapBordersEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    INTERNAL = 1
    ALL = 2


class KeepMapBordersEnumAttrOperator(EnumAttrOperator):
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


class ProjectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TOWARD_INNER_OBJECT = 0
    TOWARD_CENTER = 1
    PARALLEL_TO_AXES = 2
    VERTEX_NORMALS = 3
    CLOSEST = 4


class ProjectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TOWARD_INNER_OBJECT = 0
    TOWARD_CENTER = 1
    PARALLEL_TO_AXES = 2
    VERTEX_NORMALS = 3
    CLOSEST = 4

    NAME_MAP = {
        TOWARD_INNER_OBJECT: "Toward Inner Object",
        TOWARD_CENTER: "Toward Center",
        PARALLEL_TO_AXES: "Parallel To Axes",
        VERTEX_NORMALS: "Vertex Normals",
        CLOSEST: "Closest",
    }


class ProjectionEnumField(
    EnumField[ProjectionEnumAttrOperator, ProjectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ProjectionEnumAttrOperator
    PLUG_CLS = ProjectionEnumPlugOperator


class AxisReferenceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TARGET_LOCAL = 0
    DEFORMED_LOCAL = 1
    GLOBAL = 3


class AxisReferenceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TARGET_LOCAL = 0
    DEFORMED_LOCAL = 1
    GLOBAL = 3

    NAME_MAP = {
        TARGET_LOCAL: "Target Local",
        DEFORMED_LOCAL: "Deformed Local",
        GLOBAL: "Global",
    }


class AxisReferenceEnumField(
    EnumField[AxisReferenceEnumAttrOperator, AxisReferenceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisReferenceEnumAttrOperator
    PLUG_CLS = AxisReferenceEnumPlugOperator


class ShapePreservationReprojectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NO_REPROJECTION = 0
    SINGLE_REPROJECTION = 1
    REPROJECTION_PER_STEP = 2


class ShapePreservationReprojectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NO_REPROJECTION = 0
    SINGLE_REPROJECTION = 1
    REPROJECTION_PER_STEP = 2

    NAME_MAP = {
        NO_REPROJECTION: "No Reprojection",
        SINGLE_REPROJECTION: "Single Reprojection",
        REPROJECTION_PER_STEP: "Reprojection Per Step",
    }


class ShapePreservationReprojectionEnumField(
    EnumField[ShapePreservationReprojectionEnumAttrOperator, ShapePreservationReprojectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShapePreservationReprojectionEnumAttrOperator
    PLUG_CLS = ShapePreservationReprojectionEnumPlugOperator


class ShapePreservationMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    EDGES = 0
    TRIANGLES = 1


class ShapePreservationMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    EDGES = 0
    TRIANGLES = 1

    NAME_MAP = {
        EDGES: "Edges",
        TRIANGLES: "Triangles",
    }


class ShapePreservationMethodEnumField(
    EnumField[ShapePreservationMethodEnumAttrOperator, ShapePreservationMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShapePreservationMethodEnumAttrOperator
    PLUG_CLS = ShapePreservationMethodEnumPlugOperator


class _GeneratedShrinkWrap(DG):
    __slots__ = ()

    NODE_TYPE = "shrinkWrap"

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

    targetGeom = TypedField()
    tgt = targetGeom

    cachedSmoothTarget = DataMeshField()
    cst = cachedSmoothTarget

    targetSmoothLevel = ShortField(default_value=0, min_value=0, max_value=7, soft_min_value=0, soft_max_value=4)
    tsl = targetSmoothLevel

    continuity = FloatField(default_value=1.0, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
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

    innerGeom = TypedField()
    in_ = innerGeom

    innerGroupId = LongField(default_value=0)
    igi = innerGroupId

    projection = ProjectionEnumField(default_value=0)
    prj = projection

    closestIfNoIntersection = BoolField(default_value=False)
    cni = closestIfNoIntersection

    reverse = BoolField(default_value=False)
    rev = reverse

    bidirectional = BoolField(default_value=False)
    bi = bidirectional

    boundingBoxCenter = BoolField(default_value=False)
    bbc = boundingBoxCenter

    axisReference = AxisReferenceEnumField(default_value=0)
    ar = axisReference

    alongX = BoolField(default_value=False)
    ax = alongX

    alongY = BoolField(default_value=False)
    ay = alongY

    alongZ = BoolField(default_value=False)
    az = alongZ

    offset = DoubleLinearField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    o = offset

    targetInflation = DoubleLinearField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ti = targetInflation

    cachedInflatedTarget = DataMeshField()
    cit = cachedInflatedTarget

    falloff = DoubleLinearField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fo = falloff

    falloffIterations = ShortField(default_value=1, min_value=1, soft_min_value=1, soft_max_value=10)
    fi = falloffIterations

    shapePreservationEnable = BoolField(default_value=False)
    spe = shapePreservationEnable

    shapePreservationSteps = ShortField(default_value=1, min_value=1, soft_min_value=1, soft_max_value=100)
    sps = shapePreservationSteps

    shapePreservationIterations = ShortField(default_value=1, min_value=1, soft_min_value=1, soft_max_value=10)
    spi = shapePreservationIterations

    shapePreservationReprojection = ShapePreservationReprojectionEnumField(default_value=1)
    spr = shapePreservationReprojection

    shapePreservationMethod = ShapePreservationMethodEnumField(default_value=0)
    spm = shapePreservationMethod

    inputEnvelope = FloatField(multi=True, default_value=1.0, min_value=-2.0, max_value=2.0, soft_min_value=0.0, soft_max_value=1.0)
    ien = inputEnvelope
