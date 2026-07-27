# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_chip_off import (
    GravityField,
    LocalDirectionField,
    LocalRotateField,
    LocalScaleField,
    LocalTranslateField,
    MagnetField,
    PivotField,
    RotateField,
    ScaleField,
    TranslateField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField


class LocalCenterEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MIDDLE = 0
    START = 1
    END = 2


class LocalCenterEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MIDDLE = 0
    START = 1
    END = 2

    NAME_MAP = {
        MIDDLE: "middle",
        START: "start",
        END: "end",
    }


class LocalCenterEnumField(
    EnumField[LocalCenterEnumAttrOperator, LocalCenterEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LocalCenterEnumAttrOperator
    PLUG_CLS = LocalCenterEnumPlugOperator


class GeneratedPolyChipOff(DG):
    __slots__ = ()

    NODE_TYPE = "polyChipOff"

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

    localRotate = LocalRotateField(default_value=(0.0, 0.0, 0.0))
    lr = localRotate
    localRotateX = localRotate.localRotateX
    lrx = localRotateX
    localRotateY = localRotate.localRotateY
    lry = localRotateY
    localRotateZ = localRotate.localRotateZ
    lrz = localRotateZ

    localScale = LocalScaleField(default_value=(1.0, 1.0, 1.0))
    ls = localScale
    localScaleX = localScale.localScaleX
    lsx = localScaleX
    localScaleY = localScale.localScaleY
    lsy = localScaleY
    localScaleZ = localScale.localScaleZ
    lsz = localScaleZ

    localCenter = LocalCenterEnumField(default_value=0)
    lc = localCenter

    offset = FloatField(default_value=0.0)
    off = offset

    weight = DoubleField(default_value=0.0)
    w = weight

    gravity = GravityField(default_value=(0.0, -1.0, 0.0))
    g = gravity
    gravityX = gravity.gravityX
    gx = gravityX
    gravityY = gravity.gravityY
    gy = gravityY
    gravityZ = gravity.gravityZ
    gz = gravityZ

    attraction = DoubleField(default_value=0.0)
    att = attraction

    magnet = MagnetField(default_value=(0.0, 0.0, 0.0))
    m = magnet
    magnX = magnet.magnX
    mx = magnX
    magnY = magnet.magnY
    my = magnY
    magnZ = magnet.magnZ
    mz = magnZ

    keepFacesTogether = BoolField(default_value=True)
    kft = keepFacesTogether

    duplicate = BoolField(default_value=True)
    dup = duplicate
