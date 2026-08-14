# coding: utf-8
from .._core import DG
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


class SeparateEnumPlugOperator(EnumPlugOperator["SeparateEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    FOLDS = 1
    ALL_INTERSECTING = 2


class SeparateEnumAttrOperator(EnumAttrOperator[SeparateEnumPlugOperator]):
    __slots__ = ()

    NONE = 0
    FOLDS = 1
    ALL_INTERSECTING = 2

    NAME_MAP = {
        NONE: "None",
        FOLDS: "Folds",
        ALL_INTERSECTING: "All Intersecting",
    }


class SeparateEnumField(
    EnumField[SeparateEnumAttrOperator, SeparateEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SeparateEnumAttrOperator
    PLUG_CLS = SeparateEnumPlugOperator


class LayoutEnumPlugOperator(EnumPlugOperator["LayoutEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    ALONG_U = 1
    INTO_SQUARE = 2
    GRID = 3
    NEAREST_REGION = 4


class LayoutEnumAttrOperator(EnumAttrOperator[LayoutEnumPlugOperator]):
    __slots__ = ()

    NONE = 0
    ALONG_U = 1
    INTO_SQUARE = 2
    GRID = 3
    NEAREST_REGION = 4

    NAME_MAP = {
        NONE: "None",
        ALONG_U: "Along U",
        INTO_SQUARE: "Into Square",
        GRID: "Grid",
        NEAREST_REGION: "Nearest Region",
    }


class LayoutEnumField(
    EnumField[LayoutEnumAttrOperator, LayoutEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LayoutEnumAttrOperator
    PLUG_CLS = LayoutEnumPlugOperator


class ScaleEnumPlugOperator(EnumPlugOperator["ScaleEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    UNIFORM = 1
    STRETCH_TO_SQUARE = 2


class ScaleEnumAttrOperator(EnumAttrOperator[ScaleEnumPlugOperator]):
    __slots__ = ()

    NONE = 0
    UNIFORM = 1
    STRETCH_TO_SQUARE = 2

    NAME_MAP = {
        NONE: "None",
        UNIFORM: "Uniform",
        STRETCH_TO_SQUARE: "Stretch to Square",
    }


class ScaleEnumField(EnumField[ScaleEnumAttrOperator, ScaleEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ScaleEnumAttrOperator
    PLUG_CLS = ScaleEnumPlugOperator


class RotateForBestFitEnumPlugOperator(
    EnumPlugOperator["RotateForBestFitEnumAttrOperator"]
):
    __slots__ = ()

    NO_ROTATION = 0
    _90_DEGREE_ROTATION = 1
    FREE_ROTATION = 2
    BEST_BOUNDING_BOX_AREA = 3


class RotateForBestFitEnumAttrOperator(
    EnumAttrOperator[RotateForBestFitEnumPlugOperator]
):
    __slots__ = ()

    NO_ROTATION = 0
    _90_DEGREE_ROTATION = 1
    FREE_ROTATION = 2
    BEST_BOUNDING_BOX_AREA = 3

    NAME_MAP = {
        NO_ROTATION: "No Rotation",
        _90_DEGREE_ROTATION: "90 Degree Rotation",
        FREE_ROTATION: "Free Rotation",
        BEST_BOUNDING_BOX_AREA: "Best Bounding Box Area",
    }


class RotateForBestFitEnumField(
    EnumField[
        RotateForBestFitEnumAttrOperator, RotateForBestFitEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RotateForBestFitEnumAttrOperator
    PLUG_CLS = RotateForBestFitEnumPlugOperator


class LayoutMethodEnumPlugOperator(
    EnumPlugOperator["LayoutMethodEnumAttrOperator"]
):
    __slots__ = ()

    BLOCK_STACKING = 0
    SHAPE_STACKING = 1


class LayoutMethodEnumAttrOperator(
    EnumAttrOperator[LayoutMethodEnumPlugOperator]
):
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


class GeneratedPolyLayoutUV(DG):
    __slots__ = ()

    NODE_TYPE = "polyLayoutUV"

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

    separate = SeparateEnumField(default_value=0)
    se = separate

    flipReversed = BoolField(default_value=True)
    fr = flipReversed

    layout = LayoutEnumField(default_value=2)
    l = layout

    gridU = LongField(default_value=1)
    gu = gridU

    gridV = LongField(default_value=1)
    gv = gridV

    percentageSpace = FloatField(
        default_value=0.0, min_value=0.0, max_value=5.0
    )
    ps = percentageSpace

    scale = ScaleEnumField(default_value=1)
    sc = scale

    denseLayout = BoolField(default_value=False)
    dl = denseLayout

    rotateForBestFit = RotateForBestFitEnumField(default_value=0)
    rbf = rotateForBestFit

    layoutMethod = LayoutMethodEnumField(default_value=0)
    lm = layoutMethod

    twoSidedLayout = BoolField(default_value=True)
    tl = twoSidedLayout
