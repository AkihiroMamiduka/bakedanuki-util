# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string_array import DataStringArrayField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.long_compound.long2_compound._base import (
    Long2CompoundBaseAttrOperator,
    Long2CompoundBasePlugOperator,
    Long2CompoundBaseField,
)


class BatchRenderControlsPlugOperator(
    CompoundPlugOperator["BatchRenderControlsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("renderMode", "rm"),
        ("lightingMode", "lm"),
        ("objectTypeFilterNameArray", "otfna"),
        ("objectTypeFilterValueArray", "otfva"),
        ("pluginObjectTypeFilterNameArray", "potfna"),
        ("pluginObjectTypeFilterValueArray", "potfva"),
    )

    renderMode = EnumField()
    rm = renderMode

    lightingMode = EnumField()
    lm = lightingMode

    objectTypeFilterNameArray = DataStringArrayField()
    otfna = objectTypeFilterNameArray

    objectTypeFilterValueArray = TypedField()
    otfva = objectTypeFilterValueArray

    pluginObjectTypeFilterNameArray = DataStringArrayField()
    potfna = pluginObjectTypeFilterNameArray

    pluginObjectTypeFilterValueArray = TypedField()
    potfva = pluginObjectTypeFilterValueArray


class BatchRenderControlsAttrOperator(
    CompoundAttrOperator[BatchRenderControlsPlugOperator]
):
    __slots__ = ()

    renderMode = EnumField()
    rm = renderMode

    lightingMode = EnumField()
    lm = lightingMode

    objectTypeFilterNameArray = DataStringArrayField()
    otfna = objectTypeFilterNameArray

    objectTypeFilterValueArray = TypedField()
    otfva = objectTypeFilterValueArray

    pluginObjectTypeFilterNameArray = DataStringArrayField()
    potfna = pluginObjectTypeFilterNameArray

    pluginObjectTypeFilterValueArray = TypedField()
    potfva = pluginObjectTypeFilterValueArray


class BatchRenderControlsField(
    CompoundField[BatchRenderControlsAttrOperator, BatchRenderControlsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BatchRenderControlsAttrOperator
    PLUG_CLS = BatchRenderControlsPlugOperator

    renderMode = EnumField()
    rm = renderMode

    lightingMode = EnumField()
    lm = lightingMode

    objectTypeFilterNameArray = DataStringArrayField()
    otfna = objectTypeFilterNameArray

    objectTypeFilterValueArray = TypedField()
    otfva = objectTypeFilterValueArray

    pluginObjectTypeFilterNameArray = DataStringArrayField()
    potfna = pluginObjectTypeFilterNameArray

    pluginObjectTypeFilterValueArray = TypedField()
    potfva = pluginObjectTypeFilterValueArray


class HwFogColorPlugOperator(
    Float3CompoundBasePlugOperator["HwFogColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hwFogColorR", "hfcr"),
        ("hwFogColorG", "hfcg"),
        ("hwFogColorB", "hfcb"),
    )

    hwFogColorR = FloatField()
    hfcr = hwFogColorR

    hwFogColorG = FloatField()
    hfcg = hwFogColorG

    hwFogColorB = FloatField()
    hfcb = hwFogColorB


class HwFogColorAttrOperator(
    Float3CompoundBaseAttrOperator[HwFogColorPlugOperator]
):
    __slots__ = ()

    hwFogColorR = FloatField()
    hfcr = hwFogColorR

    hwFogColorG = FloatField()
    hfcg = hwFogColorG

    hwFogColorB = FloatField()
    hfcb = hwFogColorB


class HwFogColorField(
    Float3CompoundBaseField[HwFogColorAttrOperator, HwFogColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HwFogColorAttrOperator
    PLUG_CLS = HwFogColorPlugOperator

    hwFogColorR = FloatField()
    hfcr = hwFogColorR

    hwFogColorG = FloatField()
    hfcg = hwFogColorG

    hwFogColorB = FloatField()
    hfcb = hwFogColorB


class MotionBlurFadeTintPlugOperator(
    Float3CompoundBasePlugOperator["MotionBlurFadeTintAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("motionBlurFadeTintR", "mbftr"),
        ("motionBlurFadeTintG", "mbftg"),
        ("motionBlurFadeTintB", "mbftb"),
    )

    motionBlurFadeTintR = FloatField()
    mbftr = motionBlurFadeTintR

    motionBlurFadeTintG = FloatField()
    mbftg = motionBlurFadeTintG

    motionBlurFadeTintB = FloatField()
    mbftb = motionBlurFadeTintB


class MotionBlurFadeTintAttrOperator(
    Float3CompoundBaseAttrOperator[MotionBlurFadeTintPlugOperator]
):
    __slots__ = ()

    motionBlurFadeTintR = FloatField()
    mbftr = motionBlurFadeTintR

    motionBlurFadeTintG = FloatField()
    mbftg = motionBlurFadeTintG

    motionBlurFadeTintB = FloatField()
    mbftb = motionBlurFadeTintB


class MotionBlurFadeTintField(
    Float3CompoundBaseField[MotionBlurFadeTintAttrOperator, MotionBlurFadeTintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MotionBlurFadeTintAttrOperator
    PLUG_CLS = MotionBlurFadeTintPlugOperator

    motionBlurFadeTintR = FloatField()
    mbftr = motionBlurFadeTintR

    motionBlurFadeTintG = FloatField()
    mbftg = motionBlurFadeTintG

    motionBlurFadeTintB = FloatField()
    mbftb = motionBlurFadeTintB


class MotionBlurMultiframeChartSizePlugOperator(
    Long2CompoundBasePlugOperator["MotionBlurMultiframeChartSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("motionBlurMultiframeChartSizeX", "mbcsx"),
        ("motionBlurMultiframeChartSizeY", "mbcsy"),
    )

    motionBlurMultiframeChartSizeX = LongField()
    mbcsx = motionBlurMultiframeChartSizeX

    motionBlurMultiframeChartSizeY = LongField()
    mbcsy = motionBlurMultiframeChartSizeY


class MotionBlurMultiframeChartSizeAttrOperator(
    Long2CompoundBaseAttrOperator[MotionBlurMultiframeChartSizePlugOperator]
):
    __slots__ = ()

    motionBlurMultiframeChartSizeX = LongField()
    mbcsx = motionBlurMultiframeChartSizeX

    motionBlurMultiframeChartSizeY = LongField()
    mbcsy = motionBlurMultiframeChartSizeY


class MotionBlurMultiframeChartSizeField(
    Long2CompoundBaseField[MotionBlurMultiframeChartSizeAttrOperator, MotionBlurMultiframeChartSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MotionBlurMultiframeChartSizeAttrOperator
    PLUG_CLS = MotionBlurMultiframeChartSizePlugOperator

    motionBlurMultiframeChartSizeX = LongField()
    mbcsx = motionBlurMultiframeChartSizeX

    motionBlurMultiframeChartSizeY = LongField()
    mbcsy = motionBlurMultiframeChartSizeY


class MotionBlurAtlasSizePlugOperator(
    Long2CompoundBasePlugOperator["MotionBlurAtlasSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("motionBlurAtlasSizeX", "mbasx"),
        ("motionBlurAtlasSizeY", "mbasy"),
    )

    motionBlurAtlasSizeX = LongField()
    mbasx = motionBlurAtlasSizeX

    motionBlurAtlasSizeY = LongField()
    mbasy = motionBlurAtlasSizeY


class MotionBlurAtlasSizeAttrOperator(
    Long2CompoundBaseAttrOperator[MotionBlurAtlasSizePlugOperator]
):
    __slots__ = ()

    motionBlurAtlasSizeX = LongField()
    mbasx = motionBlurAtlasSizeX

    motionBlurAtlasSizeY = LongField()
    mbasy = motionBlurAtlasSizeY


class MotionBlurAtlasSizeField(
    Long2CompoundBaseField[MotionBlurAtlasSizeAttrOperator, MotionBlurAtlasSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MotionBlurAtlasSizeAttrOperator
    PLUG_CLS = MotionBlurAtlasSizePlugOperator

    motionBlurAtlasSizeX = LongField()
    mbasx = motionBlurAtlasSizeX

    motionBlurAtlasSizeY = LongField()
    mbasy = motionBlurAtlasSizeY


class QuadDrawOverrideColorPlugOperator(
    Float3CompoundBasePlugOperator["QuadDrawOverrideColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("quadDrawOverrideColorR", "qdocr"),
        ("quadDrawOverrideColorG", "qdocg"),
        ("quadDrawOverrideColorB", "qdocb"),
    )

    quadDrawOverrideColorR = FloatField()
    qdocr = quadDrawOverrideColorR

    quadDrawOverrideColorG = FloatField()
    qdocg = quadDrawOverrideColorG

    quadDrawOverrideColorB = FloatField()
    qdocb = quadDrawOverrideColorB


class QuadDrawOverrideColorAttrOperator(
    Float3CompoundBaseAttrOperator[QuadDrawOverrideColorPlugOperator]
):
    __slots__ = ()

    quadDrawOverrideColorR = FloatField()
    qdocr = quadDrawOverrideColorR

    quadDrawOverrideColorG = FloatField()
    qdocg = quadDrawOverrideColorG

    quadDrawOverrideColorB = FloatField()
    qdocb = quadDrawOverrideColorB


class QuadDrawOverrideColorField(
    Float3CompoundBaseField[QuadDrawOverrideColorAttrOperator, QuadDrawOverrideColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = QuadDrawOverrideColorAttrOperator
    PLUG_CLS = QuadDrawOverrideColorPlugOperator

    quadDrawOverrideColorR = FloatField()
    qdocr = quadDrawOverrideColorR

    quadDrawOverrideColorG = FloatField()
    qdocg = quadDrawOverrideColorG

    quadDrawOverrideColorB = FloatField()
    qdocb = quadDrawOverrideColorB


class CustomUVBorderColorPlugOperator(
    Float3CompoundBasePlugOperator["CustomUVBorderColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("customUVBorderColorR", "uvbcr"),
        ("customUVBorderColorG", "uvbcg"),
        ("customUVBorderColorB", "uvbcb"),
    )

    customUVBorderColorR = FloatField()
    uvbcr = customUVBorderColorR

    customUVBorderColorG = FloatField()
    uvbcg = customUVBorderColorG

    customUVBorderColorB = FloatField()
    uvbcb = customUVBorderColorB


class CustomUVBorderColorAttrOperator(
    Float3CompoundBaseAttrOperator[CustomUVBorderColorPlugOperator]
):
    __slots__ = ()

    customUVBorderColorR = FloatField()
    uvbcr = customUVBorderColorR

    customUVBorderColorG = FloatField()
    uvbcg = customUVBorderColorG

    customUVBorderColorB = FloatField()
    uvbcb = customUVBorderColorB


class CustomUVBorderColorField(
    Float3CompoundBaseField[CustomUVBorderColorAttrOperator, CustomUVBorderColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CustomUVBorderColorAttrOperator
    PLUG_CLS = CustomUVBorderColorPlugOperator

    customUVBorderColorR = FloatField()
    uvbcr = customUVBorderColorR

    customUVBorderColorG = FloatField()
    uvbcg = customUVBorderColorG

    customUVBorderColorB = FloatField()
    uvbcb = customUVBorderColorB
