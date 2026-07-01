# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_chip_off import (
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
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField


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


class PolyChipOff(DG):
    __slots__ = ()

    NODE_TYPE = "polyChipOff"

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

    translate = TranslateField()
    t = translate
    translateX = translate.translateX
    tx = translateX
    translateY = translate.translateY
    ty = translateY
    translateZ = translate.translateZ
    tz = translateZ

    rotate = RotateField()
    ro = rotate
    rotateX = rotate.rotateX
    rx = rotateX
    rotateY = rotate.rotateY
    ry = rotateY
    rotateZ = rotate.rotateZ
    rz = rotateZ

    scale = ScaleField()
    s = scale
    scaleX = scale.scaleX
    sx = scaleX
    scaleY = scale.scaleY
    sy = scaleY
    scaleZ = scale.scaleZ
    sz = scaleZ

    pivot = PivotField()
    pvt = pivot
    pivotX = pivot.pivotX
    pvx = pivotX
    pivotY = pivot.pivotY
    pvy = pivotY
    pivotZ = pivot.pivotZ
    pvz = pivotZ

    random = FloatField()
    ran = random

    randomSeed = LongField()
    rs = randomSeed

    localTranslate = LocalTranslateField()
    lt = localTranslate
    localTranslateX = localTranslate.localTranslateX
    ltx = localTranslateX
    localTranslateY = localTranslate.localTranslateY
    lty = localTranslateY
    localTranslateZ = localTranslate.localTranslateZ
    ltz = localTranslateZ

    localDirection = LocalDirectionField()
    ld = localDirection
    localDirectionX = localDirection.localDirectionX
    ldx = localDirectionX
    localDirectionY = localDirection.localDirectionY
    ldy = localDirectionY
    localDirectionZ = localDirection.localDirectionZ
    ldz = localDirectionZ

    matrix = DataMatrixField()
    cma = matrix

    compId = LongField()
    cid = compId

    gain = FloatField(multi=True)
    ga = gain

    localRotate = LocalRotateField()
    lr = localRotate
    localRotateX = localRotate.localRotateX
    lrx = localRotateX
    localRotateY = localRotate.localRotateY
    lry = localRotateY
    localRotateZ = localRotate.localRotateZ
    lrz = localRotateZ

    localScale = LocalScaleField()
    ls = localScale
    localScaleX = localScale.localScaleX
    lsx = localScaleX
    localScaleY = localScale.localScaleY
    lsy = localScaleY
    localScaleZ = localScale.localScaleZ
    lsz = localScaleZ

    localCenter = LocalCenterEnumField()
    lc = localCenter

    offset = FloatField()
    off = offset

    weight = DoubleField()
    w = weight

    gravity = GravityField()
    g = gravity
    gravityX = gravity.gravityX
    gx = gravityX
    gravityY = gravity.gravityY
    gy = gravityY
    gravityZ = gravity.gravityZ
    gz = gravityZ

    attraction = DoubleField()
    att = attraction

    magnet = MagnetField()
    m = magnet
    magnX = magnet.magnX
    mx = magnX
    magnY = magnet.magnY
    my = magnY
    magnZ = magnet.magnZ
    mz = magnZ

    keepFacesTogether = BoolField()
    kft = keepFacesTogether

    duplicate = BoolField()
    dup = duplicate
