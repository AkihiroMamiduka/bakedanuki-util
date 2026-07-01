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
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField


class MiteringEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTO = 0
    UNIFORM = 1
    PATCH = 2
    RADIAL = 3
    NONE = 4


class MiteringEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTO = 0
    UNIFORM = 1
    PATCH = 2
    RADIAL = 3
    NONE = 4

    NAME_MAP = {
        AUTO: "Auto",
        UNIFORM: "Uniform",
        PATCH: "Patch",
        RADIAL: "Radial",
        NONE: "None",
    }


class MiteringEnumField(
    EnumField[MiteringEnumAttrOperator, MiteringEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MiteringEnumAttrOperator
    PLUG_CLS = MiteringEnumPlugOperator


class MiterAlongEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTO = 0
    CENTER = 1
    EDGE = 2
    HARD_EDGE = 3


class MiterAlongEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTO = 0
    CENTER = 1
    EDGE = 2
    HARD_EDGE = 3

    NAME_MAP = {
        AUTO: "Auto",
        CENTER: "Center",
        EDGE: "Edge",
        HARD_EDGE: "Hard Edge",
    }


class MiterAlongEnumField(
    EnumField[MiterAlongEnumAttrOperator, MiterAlongEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MiterAlongEnumAttrOperator
    PLUG_CLS = MiterAlongEnumPlugOperator


class PolyBevel3(DG):
    __slots__ = ()

    NODE_TYPE = "polyBevel3"

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

    forceParallel = BoolField()
    fp = forceParallel

    offset = DoubleLinearField()
    o = offset

    fraction = DoubleField()
    f = fraction

    roundness = DoubleField()
    r = roundness

    segments = LongField()
    sg = segments

    depth = DoubleField()
    d = depth

    mitering = MiteringEnumField()
    m = mitering

    miterAlong = MiterAlongEnumField()
    mia = miterAlong

    chamfer = BoolField()
    c = chamfer

    autoFit = BoolField()
    af = autoFit

    angleTolerance = DoubleField()
    at = angleTolerance

    subdivideNgons = BoolField()
    sn = subdivideNgons

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

    maya2016SP3 = BoolField()
    m16 = maya2016SP3

    maya2017Update1 = BoolField()
    m17 = maya2017Update1

    filterEdgesByAngle = BoolField()
    fea = filterEdgesByAngle

    filterAngle = DoubleAngleField()
    fan = filterAngle

    filterHardEdges = BoolField()
    fhe = filterHardEdges
