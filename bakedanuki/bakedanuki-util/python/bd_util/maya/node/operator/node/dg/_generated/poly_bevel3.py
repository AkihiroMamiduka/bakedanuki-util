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
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField


class MiteringEnumPlugOperator(EnumPlugOperator["MiteringEnumAttrOperator"]):
    __slots__ = ()

    AUTO = 0
    UNIFORM = 1
    PATCH = 2
    RADIAL = 3
    NONE = 4


class MiteringEnumAttrOperator(EnumAttrOperator[MiteringEnumPlugOperator]):
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


class MiterAlongEnumPlugOperator(
    EnumPlugOperator["MiterAlongEnumAttrOperator"]
):
    __slots__ = ()

    AUTO = 0
    CENTER = 1
    EDGE = 2
    HARD_EDGE = 3


class MiterAlongEnumAttrOperator(EnumAttrOperator[MiterAlongEnumPlugOperator]):
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


class GeneratedPolyBevel3(DG):
    __slots__ = ()

    NODE_TYPE = "polyBevel3"

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

    forceParallel = BoolField(default_value=False)
    fp = forceParallel

    offset = DoubleLinearField(
        default_value=0.2, min_value=0.0, soft_max_value=5.0
    )
    o = offset

    fraction = DoubleField(
        default_value=0.5, min_value=0.0, soft_max_value=1.0
    )
    f = fraction

    roundness = DoubleField(
        default_value=0.5,
        min_value=-1.0,
        soft_min_value=-0.5,
        soft_max_value=0.5,
    )
    r = roundness

    segments = LongField(default_value=1, min_value=1, soft_max_value=12)
    sg = segments

    depth = DoubleField(
        default_value=1.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    d = depth

    mitering = MiteringEnumField(default_value=0)
    m = mitering

    miterAlong = MiterAlongEnumField(default_value=0)
    mia = miterAlong

    chamfer = BoolField(default_value=True)
    c = chamfer

    autoFit = BoolField(default_value=True)
    af = autoFit

    angleTolerance = DoubleField(
        default_value=20.0, min_value=0.0, soft_max_value=180.0
    )
    at = angleTolerance

    subdivideNgons = BoolField(default_value=False)
    sn = subdivideNgons

    mergeVertices = BoolField(default_value=False)
    mv = mergeVertices

    mergeVertexTolerance = DoubleLinearField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0
    )
    mvt = mergeVertexTolerance

    smoothingAngle = DoubleField(
        default_value=0.0, min_value=0.0, soft_max_value=180.0
    )
    sa = smoothingAngle

    miteringAngle = DoubleField(
        default_value=0.0, min_value=0.0, soft_max_value=180.0
    )
    ma = miteringAngle

    maya2015 = BoolField(default_value=True)
    m15 = maya2015

    maya2016SP3 = BoolField(default_value=True)
    m16 = maya2016SP3

    maya2017Update1 = BoolField(default_value=True)
    m17 = maya2017Update1

    filterEdgesByAngle = BoolField(default_value=False)
    fea = filterEdgesByAngle

    filterAngle = DoubleAngleField(
        default_value=29.999999999999996, min_value=0.0, max_value=180.0
    )
    fan = filterAngle

    filterHardEdges = BoolField(default_value=False)
    fhe = filterHardEdges
