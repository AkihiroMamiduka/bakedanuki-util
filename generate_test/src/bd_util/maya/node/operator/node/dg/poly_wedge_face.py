# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_wedge_face import (
    AxisField,
    CenterField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField


class PolyWedgeFace(DG):
    __slots__ = ()

    NODE_TYPE = "polyWedgeFace"

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

    wedgeAngle = DoubleAngleField()
    wa = wedgeAngle

    divisions = LongField()
    d = divisions

    edge = LongField(multi=True)
    ed = edge

    center = CenterField()
    ct = center
    centerX = center.centerX
    ctx = centerX
    centerY = center.centerY
    cty = centerY
    centerZ = center.centerZ
    ctz = centerZ

    axis = AxisField()
    as_ = axis
    axisX = axis.axisX
    asx = axisX
    axisY = axis.axisY
    asy = axisY
    axisZ = axis.axisZ
    asz = axisZ
