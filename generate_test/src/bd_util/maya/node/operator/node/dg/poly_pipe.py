# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_pipe import AxisField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class PolyPipe(DG):
    __slots__ = ()

    NODE_TYPE = "polyPipe"

    output = DataMeshField()
    out = output

    axis = AxisField()
    ax = axis
    axisX = axis.axisX
    axx = axisX
    axisY = axis.axisY
    axy = axisY
    axisZ = axis.axisZ
    axz = axisZ

    heightBaseline = DoubleLinearField()
    hbl = heightBaseline

    paramWarn = BoolField()
    pw = paramWarn

    uvSetName = DataStringField()
    uvs = uvSetName

    componentTagCreate = BoolField()
    ctc = componentTagCreate

    componentTagPrefix = DataStringField()
    pfx = componentTagPrefix

    componentTagSuffix = DataStringField()
    sfx = componentTagSuffix

    radius = DoubleLinearField()
    r = radius

    height = DoubleLinearField()
    h = height

    thickness = DoubleLinearField()
    t = thickness

    subdivisionsAxis = LongField()
    sa = subdivisionsAxis

    subdivisionsHeight = LongField()
    sh = subdivisionsHeight

    subdivisionsCaps = LongField()
    sc = subdivisionsCaps

    texture = BoolField()
    tx = texture

    createUVs = BoolField()
    cuv = createUVs

    roundCap = BoolField()
    rcp = roundCap

    roundCapHeightCompensation = BoolField()
    rch = roundCapHeightCompensation
