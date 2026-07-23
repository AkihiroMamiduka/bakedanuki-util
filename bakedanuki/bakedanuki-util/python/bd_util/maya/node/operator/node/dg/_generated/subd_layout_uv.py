# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField


class SeparateEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    FOLDS = 1
    ALL_INTERSECTING = 2


class SeparateEnumAttrOperator(EnumAttrOperator):
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


class LayoutEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    ALONG_U = 1
    INTO_SQUARE = 2


class LayoutEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    ALONG_U = 1
    INTO_SQUARE = 2

    NAME_MAP = {
        NONE: "None",
        ALONG_U: "Along U",
        INTO_SQUARE: "Into Square",
    }


class LayoutEnumField(
    EnumField[LayoutEnumAttrOperator, LayoutEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LayoutEnumAttrOperator
    PLUG_CLS = LayoutEnumPlugOperator


class ScaleEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    UNIFORM = 1
    STRETCH_TO_SQUARE = 2


class ScaleEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    UNIFORM = 1
    STRETCH_TO_SQUARE = 2

    NAME_MAP = {
        NONE: "None",
        UNIFORM: "Uniform",
        STRETCH_TO_SQUARE: "Stretch to Square",
    }


class ScaleEnumField(
    EnumField[ScaleEnumAttrOperator, ScaleEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleEnumAttrOperator
    PLUG_CLS = ScaleEnumPlugOperator


class RotateForBestFitEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NO_ROTATION = 0
    _90_DEGREE_ROTATION = 1
    FREE_ROTATION = 2


class RotateForBestFitEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NO_ROTATION = 0
    _90_DEGREE_ROTATION = 1
    FREE_ROTATION = 2

    NAME_MAP = {
        NO_ROTATION: "No Rotation",
        _90_DEGREE_ROTATION: "90 Degree Rotation",
        FREE_ROTATION: "Free Rotation",
    }


class RotateForBestFitEnumField(
    EnumField[RotateForBestFitEnumAttrOperator, RotateForBestFitEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateForBestFitEnumAttrOperator
    PLUG_CLS = RotateForBestFitEnumPlugOperator


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


class _GeneratedSubdLayoutUV(DG):
    __slots__ = ()

    NODE_TYPE = "subdLayoutUV"

    outSubdiv = TypedField(writable=False)
    os = outSubdiv

    inSubdiv = TypedField()
    is_ = inSubdiv

    cachedSubdiv = TypedField()
    ic = cachedSubdiv

    inputComponents = TypedField()
    ics = inputComponents

    inputMatrix = DataMatrixField()
    ix = inputMatrix

    worldSpace = BoolField(default_value=False)
    ws = worldSpace

    manipMatrix = DataMatrixField()
    mp = manipMatrix

    separate = SeparateEnumField(default_value=0)
    se = separate

    flipReversed = BoolField(default_value=True)
    fr = flipReversed

    layout = LayoutEnumField(default_value=2)
    l = layout

    percentageSpace = FloatField(default_value=0.0, min_value=0.0, max_value=5.0)
    ps = percentageSpace

    scale = ScaleEnumField(default_value=1)
    sc = scale

    denseLayout = BoolField(default_value=False)
    dl = denseLayout

    rotateForBestFit = RotateForBestFitEnumField(default_value=0)
    rbf = rotateForBestFit

    layoutMethod = LayoutMethodEnumField(default_value=0)
    lm = layoutMethod
