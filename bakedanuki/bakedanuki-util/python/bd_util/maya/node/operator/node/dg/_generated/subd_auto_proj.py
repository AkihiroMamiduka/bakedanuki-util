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


class OptimizeEnumPlugOperator(EnumPlugOperator["OptimizeEnumAttrOperator"]):
    __slots__ = ()

    LESS_DISTORTION = 0
    FEWER_PIECES = 1


class OptimizeEnumAttrOperator(EnumAttrOperator[OptimizeEnumPlugOperator]):
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


class LayoutEnumPlugOperator(EnumPlugOperator["LayoutEnumAttrOperator"]):
    __slots__ = ()

    ALONG_U = 1
    INTO_SQUARE = 2


class LayoutEnumAttrOperator(EnumAttrOperator[LayoutEnumPlugOperator]):
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


class LayoutMethodEnumPlugOperator(EnumPlugOperator["LayoutMethodEnumAttrOperator"]):
    __slots__ = ()

    BLOCK_STACKING = 0
    SHAPE_STACKING = 1


class LayoutMethodEnumAttrOperator(EnumAttrOperator[LayoutMethodEnumPlugOperator]):
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


class ScaleEnumField(
    EnumField[ScaleEnumAttrOperator, ScaleEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleEnumAttrOperator
    PLUG_CLS = ScaleEnumPlugOperator


class GeneratedSubdAutoProj(DG):
    __slots__ = ()

    NODE_TYPE = "subdAutoProj"

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

    planes = LongField(default_value=6)
    p = planes

    optimize = OptimizeEnumField(default_value=1)
    o = optimize

    skipIntersect = BoolField(default_value=False)
    si = skipIntersect

    layout = LayoutEnumField(default_value=2)
    l = layout

    layoutMethod = LayoutMethodEnumField(default_value=0)
    lm = layoutMethod

    percentageSpace = FloatField(default_value=0.0, min_value=0.0, max_value=5.0)
    ps = percentageSpace

    scale = ScaleEnumField(default_value=1)
    sc = scale

    denseLayout = BoolField(default_value=False)
    dl = denseLayout
