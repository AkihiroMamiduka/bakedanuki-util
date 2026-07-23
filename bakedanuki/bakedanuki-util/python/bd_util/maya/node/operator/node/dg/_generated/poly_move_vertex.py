# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_move_vertex import (
    LocalDirectionField,
    LocalTranslateField,
    PivotField,
    RotateField,
    ScaleField,
    TranslateField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField


class _GeneratedPolyMoveVertex(DG):
    __slots__ = ()

    NODE_TYPE = "polyMoveVertex"

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

    translate = TranslateField(default_value=(0.0, 0.0, 0.0))
    t = translate
    translateX = translate.translateX
    tx = translateX
    translateY = translate.translateY
    ty = translateY
    translateZ = translate.translateZ
    tz = translateZ

    rotate = RotateField(default_value=(0.0, 0.0, 0.0))
    ro = rotate
    rotateX = rotate.rotateX
    rx = rotateX
    rotateY = rotate.rotateY
    ry = rotateY
    rotateZ = rotate.rotateZ
    rz = rotateZ

    scale = ScaleField(default_value=(1.0, 1.0, 1.0))
    s = scale
    scaleX = scale.scaleX
    sx = scaleX
    scaleY = scale.scaleY
    sy = scaleY
    scaleZ = scale.scaleZ
    sz = scaleZ

    pivot = PivotField(default_value=(0.0, 0.0, 0.0))
    pvt = pivot
    pivotX = pivot.pivotX
    pvx = pivotX
    pivotY = pivot.pivotY
    pvy = pivotY
    pivotZ = pivot.pivotZ
    pvz = pivotZ

    random = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ran = random

    randomSeed = LongField(default_value=0)
    rs = randomSeed

    localTranslate = LocalTranslateField(default_value=(0.0, 0.0, 0.0))
    lt = localTranslate
    localTranslateX = localTranslate.localTranslateX
    ltx = localTranslateX
    localTranslateY = localTranslate.localTranslateY
    lty = localTranslateY
    localTranslateZ = localTranslate.localTranslateZ
    ltz = localTranslateZ

    localDirection = LocalDirectionField(default_value=(1.0, 0.0, 0.0))
    ld = localDirection
    localDirectionX = localDirection.localDirectionX
    ldx = localDirectionX
    localDirectionY = localDirection.localDirectionY
    ldy = localDirectionY
    localDirectionZ = localDirection.localDirectionZ
    ldz = localDirectionZ

    matrix = DataMatrixField(writable=False)
    cma = matrix

    compId = LongField(default_value=0, writable=False)
    cid = compId

    gain = FloatField(multi=True, default_value=1.0)
    ga = gain
