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
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField
from ...attr.define.std.dt.point_array import DataPointArrayField
from ...attr.define.std.dt.string import DataStringField


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


class PolyContourProj(DG):
    __slots__ = ()

    NODE_TYPE = "polyContourProj"

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

    uvSetName = DataStringField()
    uvs = uvSetName

    method = MethodEnumField()
    m = method

    smoothness0 = DoubleField()
    s0 = smoothness0

    smoothness1 = DoubleField()
    s1 = smoothness1

    smoothness2 = DoubleField()
    s2 = smoothness2

    smoothness3 = DoubleField()
    s3 = smoothness3

    offset0 = DoubleLinearField()
    o0 = offset0

    offset1 = DoubleLinearField()
    o1 = offset1

    offset2 = DoubleLinearField()
    o2 = offset2

    offset3 = DoubleLinearField()
    o3 = offset3

    userDefinedCorners = BoolField()
    udc = userDefinedCorners

    cornerVertices = TypedField()
    cv = cornerVertices

    flipRails = BoolField()
    fr = flipRails

    reduceShear = DoubleField()
    rs = reduceShear

    surface = DataNurbsSurfaceField()
    srf = surface

    manipPoints = DataPointArrayField()
    mnp = manipPoints
