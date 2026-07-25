# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_move_uv import (
    AxisLenField,
    PivotField,
    ScaleField,
    TranslateField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.scalar.unit.range.double_angle import DoubleAngleField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedPolyMoveUV(DG):
    __slots__ = ()

    NODE_TYPE = "polyMoveUV"

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

    translate = TranslateField(default_value=(0.0, 0.0))
    t = translate
    translateU = translate.translateU
    tu = translateU
    translateV = translate.translateV
    tv = translateV

    rotationAngle = DoubleAngleField(default_value=0.0)
    ra = rotationAngle

    pivot = PivotField(default_value=(0.5, 0.5))
    pvt = pivot
    pivotU = pivot.pivotU
    pvu = pivotU
    pivotV = pivot.pivotV
    pvv = pivotV

    scale = ScaleField(default_value=(1.0, 1.0))
    s = scale
    scaleU = scale.scaleU
    su = scaleU
    scaleV = scale.scaleV
    sv = scaleV

    random = FloatField(default_value=0.0)
    ran = random

    randomSeed = LongField(default_value=0)
    rs = randomSeed

    axisLen = AxisLenField(default_value=(1.0, 1.0))
    l = axisLen
    axisLenX = axisLen.axisLenX
    lx = axisLenX
    axisLenY = axisLen.axisLenY
    ly = axisLenY

    compId = LongField(default_value=0, writable=False)
    cid = compId

    uvSetName = DataStringField()
    uvs = uvSetName
