# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_move_facet_uv import (
    AxisLenField,
    PivotField,
    ScaleField,
    TranslateField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class PolyMoveFacetUV(DG):
    __slots__ = ()

    NODE_TYPE = "polyMoveFacetUV"

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

    translate = TranslateField()
    t = translate
    translateU = translate.translateU
    tu = translateU
    translateV = translate.translateV
    tv = translateV

    rotationAngle = DoubleAngleField()
    ra = rotationAngle

    pivot = PivotField()
    pvt = pivot
    pivotU = pivot.pivotU
    pvu = pivotU
    pivotV = pivot.pivotV
    pvv = pivotV

    scale = ScaleField()
    s = scale
    scaleU = scale.scaleU
    su = scaleU
    scaleV = scale.scaleV
    sv = scaleV

    random = FloatField()
    ran = random

    randomSeed = LongField()
    rs = randomSeed

    axisLen = AxisLenField()
    l = axisLen
    axisLenX = axisLen.axisLenX
    lx = axisLenX
    axisLenY = axisLen.axisLenY
    ly = axisLenY

    compId = LongField()
    cid = compId

    uvSetName = DataStringField()
    uvs = uvSetName
