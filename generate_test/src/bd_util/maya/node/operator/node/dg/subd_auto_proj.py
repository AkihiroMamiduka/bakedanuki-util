# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.matrix import DataMatrixField


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


class LayoutEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ALONG_U = 1
    INTO_SQUARE = 2


class LayoutEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ALONG_U = 1
    INTO_SQUARE = 2

    NAME_MAP = {
        ALONG_U: "Along U",
        INTO_SQUARE: "Into Square",
    }


class LayoutEnumField(
    EnumField[LayoutEnumAttrOperator, LayoutEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LayoutEnumAttrOperator
    PLUG_CLS = LayoutEnumPlugOperator


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


class SubdAutoProj(DG):
    __slots__ = ()

    NODE_TYPE = "subdAutoProj"

    outSubdiv = TypedField()
    os = outSubdiv

    inSubdiv = TypedField()
    is_ = inSubdiv

    cachedSubdiv = TypedField()
    ic = cachedSubdiv

    inputComponents = TypedField()
    ics = inputComponents

    inputMatrix = DataMatrixField()
    ix = inputMatrix

    worldSpace = BoolField()
    ws = worldSpace

    manipMatrix = DataMatrixField()
    mp = manipMatrix

    planes = LongField()
    p = planes

    optimize = OptimizeEnumField()
    o = optimize

    skipIntersect = BoolField()
    si = skipIntersect

    layout = LayoutEnumField()
    l = layout

    layoutMethod = LayoutMethodEnumField()
    lm = layoutMethod

    percentageSpace = FloatField()
    ps = percentageSpace

    scale = ScaleEnumField()
    sc = scale

    denseLayout = BoolField()
    dl = denseLayout
