# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_wedge_face import (
    AxisField,
    CenterField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.scalar.unit.range.double_angle import DoubleAngleField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField


class _GeneratedPolyWedgeFace(DG):
    __slots__ = ()

    NODE_TYPE = "polyWedgeFace"

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

    wedgeAngle = DoubleAngleField(default_value=0.0)
    wa = wedgeAngle

    divisions = LongField(default_value=1, min_value=1)
    d = divisions

    edge = LongField(multi=True, default_value=0)
    ed = edge

    center = CenterField(default_value=(0.0, 0.0, 0.0))
    ct = center
    centerX = center.centerX
    ctx = centerX
    centerY = center.centerY
    cty = centerY
    centerZ = center.centerZ
    ctz = centerZ

    axis = AxisField(default_value=(0.0, 0.0, 0.0))
    as_ = axis
    axisX = axis.axisX
    asx = axisX
    axisY = axis.axisY
    asy = axisY
    axisZ = axis.axisZ
    asz = axisZ
