# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_torus import AxisField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class PolyTorus(DG):
    __slots__ = ()

    NODE_TYPE = "polyTorus"

    output = DataMeshField(writable=False)
    out = output

    axis = AxisField(default_value=(0.0, 1.0, 0.0))
    ax = axis
    axisX = axis.axisX
    axx = axisX
    axisY = axis.axisY
    axy = axisY
    axisZ = axis.axisZ
    axz = axisZ

    heightBaseline = DoubleLinearField(default_value=0.0, min_value=-1.0, max_value=1.0)
    hbl = heightBaseline

    paramWarn = BoolField(default_value=True)
    pw = paramWarn

    uvSetName = DataStringField()
    uvs = uvSetName

    componentTagCreate = BoolField(default_value=True)
    ctc = componentTagCreate

    componentTagPrefix = DataStringField()
    pfx = componentTagPrefix

    componentTagSuffix = DataStringField()
    sfx = componentTagSuffix

    radius = DoubleLinearField(default_value=1.0, min_value=0.01, soft_max_value=100.0)
    r = radius

    sectionRadius = DoubleLinearField(default_value=0.5, min_value=0.01, soft_max_value=100.0)
    sr = sectionRadius

    twist = DoubleAngleField(default_value=0.0, min_value=0.0, max_value=360.0)
    tw = twist

    subdivisionsAxis = LongField(default_value=20, min_value=3, soft_max_value=50)
    sa = subdivisionsAxis

    subdivisionsHeight = LongField(default_value=20, min_value=3, soft_max_value=50)
    sh = subdivisionsHeight

    texture = BoolField(default_value=True)
    tx = texture

    createUVs = BoolField(default_value=True)
    cuv = createUVs

    reverseTexture = BoolField(default_value=False)
    rtx = reverseTexture
