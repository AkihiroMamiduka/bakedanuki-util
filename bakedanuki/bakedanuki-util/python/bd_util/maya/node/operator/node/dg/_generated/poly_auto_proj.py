# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_auto_proj import (
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
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


class OptimizeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LESS_DISTORTION = 0
    FEWER_PIECES = 1


class OptimizeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LESS_DISTORTION = 0
    FEWER_PIECES = 1

    NAME_MAP = {
        LESS_DISTORTION: "Less Distortion",
        FEWER_PIECES: "Fewer Pieces",
    }


class OptimizeEnumField(
    EnumField[OptimizeEnumAttrOperator, OptimizeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OptimizeEnumAttrOperator
    PLUG_CLS = OptimizeEnumPlugOperator


class LayoutMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BLOCK_STACKING = 0
    SHAPE_STACKING = 1


class LayoutMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BLOCK_STACKING = 0
    SHAPE_STACKING = 1

    NAME_MAP = {
        BLOCK_STACKING: "Block Stacking",
        SHAPE_STACKING: "Shape Stacking",
    }


class LayoutMethodEnumField(
    EnumField[LayoutMethodEnumAttrOperator, LayoutMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LayoutMethodEnumAttrOperator
    PLUG_CLS = LayoutMethodEnumPlugOperator


class LayoutEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OVERLAP = 0
    ALONG_U = 1
    INTO_SQUARE = 2
    TILE = 3


class LayoutEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OVERLAP = 0
    ALONG_U = 1
    INTO_SQUARE = 2
    TILE = 3

    NAME_MAP = {
        OVERLAP: "Overlap",
        ALONG_U: "Along U",
        INTO_SQUARE: "Into Square",
        TILE: "Tile",
    }


class LayoutEnumField(
    EnumField[LayoutEnumAttrOperator, LayoutEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LayoutEnumAttrOperator
    PLUG_CLS = LayoutEnumPlugOperator


class ScaleModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    UNIFORM = 1
    STRETCH_TO_SQUARE = 2


class ScaleModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    UNIFORM = 1
    STRETCH_TO_SQUARE = 2

    NAME_MAP = {
        NONE: "None",
        UNIFORM: "Uniform",
        STRETCH_TO_SQUARE: "Stretch to Square",
    }


class ScaleModeEnumField(
    EnumField[ScaleModeEnumAttrOperator, ScaleModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleModeEnumAttrOperator
    PLUG_CLS = ScaleModeEnumPlugOperator


class _GeneratedPolyAutoProj(DG):
    __slots__ = ()

    NODE_TYPE = "polyAutoProj"

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

    uvSetName = DataStringField()
    uvs = uvSetName

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

    planes = LongField(default_value=6, min_value=3, max_value=12)
    p = planes

    optimize = OptimizeEnumField(default_value=1)
    o = optimize

    layoutMethod = LayoutMethodEnumField(default_value=0)
    lm = layoutMethod

    skipIntersect = BoolField(default_value=False)
    si = skipIntersect

    layout = LayoutEnumField(default_value=2)
    l = layout

    percentageSpace = FloatField(default_value=0.0, min_value=0.0, max_value=5.0)
    ps = percentageSpace

    scaleMode = ScaleModeEnumField(default_value=1)
    sc = scaleMode

    denseLayout = BoolField(default_value=False)
    dl = denseLayout

    projectBothDirections = BoolField(default_value=False)
    pb = projectBothDirections

    polyGeomObject = TypedField()
    pg = polyGeomObject

    maintainSymmetry = BoolField(default_value=True)
    ms = maintainSymmetry

    twoSidedLayout = BoolField(default_value=True)
    tl = twoSidedLayout
