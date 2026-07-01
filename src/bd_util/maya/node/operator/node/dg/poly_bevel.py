# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField


class UvAssignmentEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PLANAR_PROJECT_PER_FACE = 0
    PRESERVE_ORIGINAL_BOUNDARIES = 1


class UvAssignmentEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PLANAR_PROJECT_PER_FACE = 0
    PRESERVE_ORIGINAL_BOUNDARIES = 1

    NAME_MAP = {
        PLANAR_PROJECT_PER_FACE: "Planar project per face",
        PRESERVE_ORIGINAL_BOUNDARIES: "Preserve original boundaries",
    }


class UvAssignmentEnumField(
    EnumField[UvAssignmentEnumAttrOperator, UvAssignmentEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvAssignmentEnumAttrOperator
    PLUG_CLS = UvAssignmentEnumPlugOperator


class PolyBevel(DG):
    __slots__ = ()

    NODE_TYPE = "polyBevel"

    output = DataMeshField()
    out = output

    inputPolymesh = DataMeshField()
    ip = inputPolymesh

    inMeshCache = DataMeshField()
    imc = inMeshCache

    cacheInput = LongField()
    cin = cacheInput

    useOldPolyArchitecture = BoolField()
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField()
    vmap = vertexIdMap

    edgeIdMap = BoolField()
    emap = edgeIdMap

    faceIdMap = BoolField()
    fmap = faceIdMap

    inputComponents = TypedField()
    ics = inputComponents

    useInputComp = BoolField()
    uic = useInputComp

    inputMatrix = DataMatrixField()
    ix = inputMatrix

    worldSpace = BoolField()
    ws = worldSpace

    manipMatrix = DataMatrixField()
    mp = manipMatrix

    offsetAsFraction = BoolField()
    oaf = offsetAsFraction

    offset = DoubleLinearField()
    o = offset

    fraction = DoubleField()
    f = fraction

    roundness = DoubleField()
    r = roundness

    segments = LongField()
    sg = segments

    autoFit = BoolField()
    af = autoFit

    angleTolerance = DoubleField()
    at = angleTolerance

    fillNgons = BoolField()
    fn = fillNgons

    uvAssignment = UvAssignmentEnumField()
    ua = uvAssignment

    mergeVertices = BoolField()
    mv = mergeVertices

    mergeVertexTolerance = DoubleLinearField()
    mvt = mergeVertexTolerance

    smoothingAngle = DoubleField()
    sa = smoothingAngle

    miteringAngle = DoubleField()
    ma = miteringAngle

    maya2015 = BoolField()
    m15 = maya2015
