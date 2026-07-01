# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.shrink_wrap import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    WeightListField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.mesh import DataMeshField


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


class ShrinkWrap(DG):
    __slots__ = ()

    NODE_TYPE = "shrinkWrap"

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

    targetGeom = TypedField()
    tgt = targetGeom

    cachedSmoothTarget = DataMeshField()
    cst = cachedSmoothTarget

    targetSmoothLevel = ShortField()
    tsl = targetSmoothLevel

    continuity = FloatField()
    co = continuity

    smoothUVs = BoolField()
    suv = smoothUVs

    keepBorder = BoolField()
    kb = keepBorder

    boundaryRule = BoundaryRuleEnumField()
    bnr = boundaryRule

    keepHardEdge = BoolField()
    khe = keepHardEdge

    propagateEdgeHardness = BoolField()
    peh = propagateEdgeHardness

    keepMapBorders = KeepMapBordersEnumField()
    kmb = keepMapBorders

    innerGeom = TypedField()
    in_ = innerGeom

    innerGroupId = LongField()
    igi = innerGroupId

    projection = ProjectionEnumField()
    prj = projection

    closestIfNoIntersection = BoolField()
    cni = closestIfNoIntersection

    reverse = BoolField()
    rev = reverse

    bidirectional = BoolField()
    bi = bidirectional

    boundingBoxCenter = BoolField()
    bbc = boundingBoxCenter

    axisReference = AxisReferenceEnumField()
    ar = axisReference

    alongX = BoolField()
    ax = alongX

    alongY = BoolField()
    ay = alongY

    alongZ = BoolField()
    az = alongZ

    offset = DoubleLinearField()
    o = offset

    targetInflation = DoubleLinearField()
    ti = targetInflation

    cachedInflatedTarget = DataMeshField()
    cit = cachedInflatedTarget

    falloff = DoubleLinearField()
    fo = falloff

    falloffIterations = ShortField()
    fi = falloffIterations

    shapePreservationEnable = BoolField()
    spe = shapePreservationEnable

    shapePreservationSteps = ShortField()
    sps = shapePreservationSteps

    shapePreservationIterations = ShortField()
    spi = shapePreservationIterations

    shapePreservationReprojection = ShapePreservationReprojectionEnumField()
    spr = shapePreservationReprojection

    shapePreservationMethod = ShapePreservationMethodEnumField()
    spm = shapePreservationMethod

    inputEnvelope = FloatField(multi=True)
    ien = inputEnvelope
