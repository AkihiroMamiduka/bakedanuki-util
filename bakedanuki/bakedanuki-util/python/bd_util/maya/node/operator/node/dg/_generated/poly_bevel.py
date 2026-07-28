# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField


class UvAssignmentEnumPlugOperator(EnumPlugOperator["UvAssignmentEnumAttrOperator"]):
    __slots__ = ()

    PLANAR_PROJECT_PER_FACE = 0
    PRESERVE_ORIGINAL_BOUNDARIES = 1


class UvAssignmentEnumAttrOperator(EnumAttrOperator[UvAssignmentEnumPlugOperator]):
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


class GeneratedPolyBevel(DG):
    __slots__ = ()

    NODE_TYPE = "polyBevel"

    output = DataMeshField(writable=False)
    out = output

    inputPolymesh = DataMeshField()
    ip = inputPolymesh

    inMeshCache = DataMeshField()
    imc = inMeshCache

    cacheInput = LongField(default_value=0)
    cin = cacheInput

    useOldPolyArchitecture = BoolField(default_value=False)
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField(default_value=False)
    vmap = vertexIdMap

    edgeIdMap = BoolField(default_value=False)
    emap = edgeIdMap

    faceIdMap = BoolField(default_value=False)
    fmap = faceIdMap

    inputComponents = TypedField()
    ics = inputComponents

    useInputComp = BoolField(default_value=True)
    uic = useInputComp

    inputMatrix = DataMatrixField()
    ix = inputMatrix

    worldSpace = BoolField(default_value=False)
    ws = worldSpace

    manipMatrix = DataMatrixField()
    mp = manipMatrix

    offsetAsFraction = BoolField(default_value=False)
    oaf = offsetAsFraction

    offset = DoubleLinearField(default_value=0.2, min_value=0.0, soft_max_value=5.0)
    o = offset

    fraction = DoubleField(default_value=0.5, min_value=0.0, soft_max_value=1.0)
    f = fraction

    roundness = DoubleField(default_value=0.5, min_value=-1.0, soft_min_value=-0.5, soft_max_value=0.5)
    r = roundness

    segments = LongField(default_value=1, min_value=1, soft_max_value=12)
    sg = segments

    autoFit = BoolField(default_value=True)
    af = autoFit

    angleTolerance = DoubleField(default_value=20.0, min_value=0.0, soft_max_value=180.0)
    at = angleTolerance

    fillNgons = BoolField(default_value=False)
    fn = fillNgons

    uvAssignment = UvAssignmentEnumField(default_value=0)
    ua = uvAssignment

    mergeVertices = BoolField(default_value=False)
    mv = mergeVertices

    mergeVertexTolerance = DoubleLinearField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    mvt = mergeVertexTolerance

    smoothingAngle = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=180.0)
    sa = smoothingAngle

    miteringAngle = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=180.0)
    ma = miteringAngle

    maya2015 = BoolField(default_value=True)
    m15 = maya2015
