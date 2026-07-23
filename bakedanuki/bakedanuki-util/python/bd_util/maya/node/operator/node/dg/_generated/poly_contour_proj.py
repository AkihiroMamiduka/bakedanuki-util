# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField
from ....attr.define.std.dt.point_array import DataPointArrayField
from ....attr.define.std.dt.string import DataStringField


class MethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WALK_CONTOURS = 0
    NURBS_PROJECTION = 1


class MethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WALK_CONTOURS = 0
    NURBS_PROJECTION = 1

    NAME_MAP = {
        WALK_CONTOURS: "Walk Contours",
        NURBS_PROJECTION: "NURBS Projection",
    }


class MethodEnumField(
    EnumField[MethodEnumAttrOperator, MethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MethodEnumAttrOperator
    PLUG_CLS = MethodEnumPlugOperator


class _GeneratedPolyContourProj(DG):
    __slots__ = ()

    NODE_TYPE = "polyContourProj"

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

    uvSetName = DataStringField()
    uvs = uvSetName

    method = MethodEnumField(default_value=0)
    m = method

    smoothness0 = DoubleField(default_value=0.0, min_value=0.0, soft_min_value=0.0, soft_max_value=100.0)
    s0 = smoothness0

    smoothness1 = DoubleField(default_value=0.0, min_value=0.0, soft_min_value=0.0, soft_max_value=100.0)
    s1 = smoothness1

    smoothness2 = DoubleField(default_value=0.0, min_value=0.0, soft_min_value=0.0, soft_max_value=100.0)
    s2 = smoothness2

    smoothness3 = DoubleField(default_value=0.0, min_value=0.0, soft_min_value=0.0, soft_max_value=100.0)
    s3 = smoothness3

    offset0 = DoubleLinearField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    o0 = offset0

    offset1 = DoubleLinearField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    o1 = offset1

    offset2 = DoubleLinearField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    o2 = offset2

    offset3 = DoubleLinearField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    o3 = offset3

    userDefinedCorners = BoolField(default_value=False)
    udc = userDefinedCorners

    cornerVertices = TypedField()
    cv = cornerVertices

    flipRails = BoolField(default_value=False)
    fr = flipRails

    reduceShear = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    rs = reduceShear

    surface = DataNurbsSurfaceField(writable=False)
    srf = surface

    manipPoints = DataPointArrayField(writable=False)
    mnp = manipPoints
