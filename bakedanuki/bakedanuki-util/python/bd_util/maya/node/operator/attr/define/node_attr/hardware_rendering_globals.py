# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string_array import DataStringArrayField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    Long2CompoundBaseAttrOperator,
    Long2CompoundBasePlugOperator,
    Long2CompoundBaseField,
)


class RenderModeEnumPlugOperator(
    EnumPlugOperator["RenderModeEnumAttrOperator"]
):
    __slots__ = ()

    WIRE = 0
    SHADED = 1
    WIRE_ON_SHADED = 2
    DEFAULT_MATERIAL = 3
    SHADED_AND_TEXTURED = 4
    WIRE_ON_SHADED_AND_TEXTURED = 5
    BOUNDING_BOX = 6


class RenderModeEnumAttrOperator(EnumAttrOperator[RenderModeEnumPlugOperator]):
    __slots__ = ()

    WIRE = 0
    SHADED = 1
    WIRE_ON_SHADED = 2
    DEFAULT_MATERIAL = 3
    SHADED_AND_TEXTURED = 4
    WIRE_ON_SHADED_AND_TEXTURED = 5
    BOUNDING_BOX = 6

    NAME_MAP = {
        WIRE: "Wire",
        SHADED: "Shaded",
        WIRE_ON_SHADED: "Wire On Shaded",
        DEFAULT_MATERIAL: "Default Material",
        SHADED_AND_TEXTURED: "Shaded And Textured",
        WIRE_ON_SHADED_AND_TEXTURED: "Wire On Shaded And Textured",
        BOUNDING_BOX: "Bounding Box",
    }


class RenderModeEnumField(
    EnumField[RenderModeEnumAttrOperator, RenderModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RenderModeEnumAttrOperator
    PLUG_CLS = RenderModeEnumPlugOperator


class LightingModeEnumPlugOperator(
    EnumPlugOperator["LightingModeEnumAttrOperator"]
):
    __slots__ = ()

    DEFAULT = 0
    ALL = 1
    NONE = 2
    ACTIVE = 3
    FULL_AMBIENT = 4


class LightingModeEnumAttrOperator(
    EnumAttrOperator[LightingModeEnumPlugOperator]
):
    __slots__ = ()

    DEFAULT = 0
    ALL = 1
    NONE = 2
    ACTIVE = 3
    FULL_AMBIENT = 4

    NAME_MAP = {
        DEFAULT: "Default",
        ALL: "All",
        NONE: "None",
        ACTIVE: "Active",
        FULL_AMBIENT: "Full Ambient",
    }


class LightingModeEnumField(
    EnumField[LightingModeEnumAttrOperator, LightingModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightingModeEnumAttrOperator
    PLUG_CLS = LightingModeEnumPlugOperator


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

    renderMode = RenderModeEnumField(default_value=4)
    rm = renderMode

    lightingMode = LightingModeEnumField(default_value=1)
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

    renderMode = RenderModeEnumField(default_value=4)
    rm = renderMode

    lightingMode = LightingModeEnumField(default_value=1)
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
    CompoundField[
        BatchRenderControlsAttrOperator, BatchRenderControlsPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = BatchRenderControlsAttrOperator
    PLUG_CLS = BatchRenderControlsPlugOperator

    renderMode = RenderModeEnumField(default_value=4)
    rm = renderMode

    lightingMode = LightingModeEnumField(default_value=1)
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

    hwFogColorR = FloatField(default_value=0.5)
    hfcr = hwFogColorR

    hwFogColorG = FloatField(default_value=0.5)
    hfcg = hwFogColorG

    hwFogColorB = FloatField(default_value=0.5)
    hfcb = hwFogColorB


class HwFogColorAttrOperator(
    Float3CompoundBaseAttrOperator[HwFogColorPlugOperator]
):
    __slots__ = ()

    hwFogColorR = FloatField(default_value=0.5)
    hfcr = hwFogColorR

    hwFogColorG = FloatField(default_value=0.5)
    hfcg = hwFogColorG

    hwFogColorB = FloatField(default_value=0.5)
    hfcb = hwFogColorB


class HwFogColorField(
    Float3CompoundBaseField[HwFogColorAttrOperator, HwFogColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HwFogColorAttrOperator
    PLUG_CLS = HwFogColorPlugOperator

    hwFogColorR = FloatField(default_value=0.5)
    hfcr = hwFogColorR

    hwFogColorG = FloatField(default_value=0.5)
    hfcg = hwFogColorG

    hwFogColorB = FloatField(default_value=0.5)
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

    motionBlurFadeTintR = FloatField(default_value=0.0)
    mbftr = motionBlurFadeTintR

    motionBlurFadeTintG = FloatField(default_value=0.0)
    mbftg = motionBlurFadeTintG

    motionBlurFadeTintB = FloatField(default_value=0.0)
    mbftb = motionBlurFadeTintB


class MotionBlurFadeTintAttrOperator(
    Float3CompoundBaseAttrOperator[MotionBlurFadeTintPlugOperator]
):
    __slots__ = ()

    motionBlurFadeTintR = FloatField(default_value=0.0)
    mbftr = motionBlurFadeTintR

    motionBlurFadeTintG = FloatField(default_value=0.0)
    mbftg = motionBlurFadeTintG

    motionBlurFadeTintB = FloatField(default_value=0.0)
    mbftb = motionBlurFadeTintB


class MotionBlurFadeTintField(
    Float3CompoundBaseField[
        MotionBlurFadeTintAttrOperator, MotionBlurFadeTintPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = MotionBlurFadeTintAttrOperator
    PLUG_CLS = MotionBlurFadeTintPlugOperator

    motionBlurFadeTintR = FloatField(default_value=0.0)
    mbftr = motionBlurFadeTintR

    motionBlurFadeTintG = FloatField(default_value=0.0)
    mbftg = motionBlurFadeTintG

    motionBlurFadeTintB = FloatField(default_value=0.0)
    mbftb = motionBlurFadeTintB


class MotionBlurMultiframeChartSizePlugOperator(
    Long2CompoundBasePlugOperator["MotionBlurMultiframeChartSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("motionBlurMultiframeChartSizeX", "mbcsx"),
        ("motionBlurMultiframeChartSizeY", "mbcsy"),
    )

    motionBlurMultiframeChartSizeX = LongField(
        default_value=256, min_value=1, max_value=4096
    )
    mbcsx = motionBlurMultiframeChartSizeX

    motionBlurMultiframeChartSizeY = LongField(
        default_value=256, min_value=1, max_value=4096
    )
    mbcsy = motionBlurMultiframeChartSizeY


class MotionBlurMultiframeChartSizeAttrOperator(
    Long2CompoundBaseAttrOperator[MotionBlurMultiframeChartSizePlugOperator]
):
    __slots__ = ()

    motionBlurMultiframeChartSizeX = LongField(
        default_value=256, min_value=1, max_value=4096
    )
    mbcsx = motionBlurMultiframeChartSizeX

    motionBlurMultiframeChartSizeY = LongField(
        default_value=256, min_value=1, max_value=4096
    )
    mbcsy = motionBlurMultiframeChartSizeY


class MotionBlurMultiframeChartSizeField(
    Long2CompoundBaseField[
        MotionBlurMultiframeChartSizeAttrOperator,
        MotionBlurMultiframeChartSizePlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = MotionBlurMultiframeChartSizeAttrOperator
    PLUG_CLS = MotionBlurMultiframeChartSizePlugOperator

    motionBlurMultiframeChartSizeX = LongField(
        default_value=256, min_value=1, max_value=4096
    )
    mbcsx = motionBlurMultiframeChartSizeX

    motionBlurMultiframeChartSizeY = LongField(
        default_value=256, min_value=1, max_value=4096
    )
    mbcsy = motionBlurMultiframeChartSizeY


class MotionBlurAtlasSizePlugOperator(
    Long2CompoundBasePlugOperator["MotionBlurAtlasSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("motionBlurAtlasSizeX", "mbasx"),
        ("motionBlurAtlasSizeY", "mbasy"),
    )

    motionBlurAtlasSizeX = LongField(
        default_value=8, min_value=1, max_value=32
    )
    mbasx = motionBlurAtlasSizeX

    motionBlurAtlasSizeY = LongField(
        default_value=4, min_value=1, max_value=32
    )
    mbasy = motionBlurAtlasSizeY


class MotionBlurAtlasSizeAttrOperator(
    Long2CompoundBaseAttrOperator[MotionBlurAtlasSizePlugOperator]
):
    __slots__ = ()

    motionBlurAtlasSizeX = LongField(
        default_value=8, min_value=1, max_value=32
    )
    mbasx = motionBlurAtlasSizeX

    motionBlurAtlasSizeY = LongField(
        default_value=4, min_value=1, max_value=32
    )
    mbasy = motionBlurAtlasSizeY


class MotionBlurAtlasSizeField(
    Long2CompoundBaseField[
        MotionBlurAtlasSizeAttrOperator, MotionBlurAtlasSizePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = MotionBlurAtlasSizeAttrOperator
    PLUG_CLS = MotionBlurAtlasSizePlugOperator

    motionBlurAtlasSizeX = LongField(
        default_value=8, min_value=1, max_value=32
    )
    mbasx = motionBlurAtlasSizeX

    motionBlurAtlasSizeY = LongField(
        default_value=4, min_value=1, max_value=32
    )
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

    quadDrawOverrideColorR = FloatField(default_value=-1.0)
    qdocr = quadDrawOverrideColorR

    quadDrawOverrideColorG = FloatField(default_value=-1.0)
    qdocg = quadDrawOverrideColorG

    quadDrawOverrideColorB = FloatField(default_value=-1.0)
    qdocb = quadDrawOverrideColorB


class QuadDrawOverrideColorAttrOperator(
    Float3CompoundBaseAttrOperator[QuadDrawOverrideColorPlugOperator]
):
    __slots__ = ()

    quadDrawOverrideColorR = FloatField(default_value=-1.0)
    qdocr = quadDrawOverrideColorR

    quadDrawOverrideColorG = FloatField(default_value=-1.0)
    qdocg = quadDrawOverrideColorG

    quadDrawOverrideColorB = FloatField(default_value=-1.0)
    qdocb = quadDrawOverrideColorB


class QuadDrawOverrideColorField(
    Float3CompoundBaseField[
        QuadDrawOverrideColorAttrOperator, QuadDrawOverrideColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = QuadDrawOverrideColorAttrOperator
    PLUG_CLS = QuadDrawOverrideColorPlugOperator

    quadDrawOverrideColorR = FloatField(default_value=-1.0)
    qdocr = quadDrawOverrideColorR

    quadDrawOverrideColorG = FloatField(default_value=-1.0)
    qdocg = quadDrawOverrideColorG

    quadDrawOverrideColorB = FloatField(default_value=-1.0)
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

    customUVBorderColorR = FloatField(default_value=-1.0)
    uvbcr = customUVBorderColorR

    customUVBorderColorG = FloatField(default_value=-1.0)
    uvbcg = customUVBorderColorG

    customUVBorderColorB = FloatField(default_value=-1.0)
    uvbcb = customUVBorderColorB


class CustomUVBorderColorAttrOperator(
    Float3CompoundBaseAttrOperator[CustomUVBorderColorPlugOperator]
):
    __slots__ = ()

    customUVBorderColorR = FloatField(default_value=-1.0)
    uvbcr = customUVBorderColorR

    customUVBorderColorG = FloatField(default_value=-1.0)
    uvbcg = customUVBorderColorG

    customUVBorderColorB = FloatField(default_value=-1.0)
    uvbcb = customUVBorderColorB


class CustomUVBorderColorField(
    Float3CompoundBaseField[
        CustomUVBorderColorAttrOperator, CustomUVBorderColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CustomUVBorderColorAttrOperator
    PLUG_CLS = CustomUVBorderColorPlugOperator

    customUVBorderColorR = FloatField(default_value=-1.0)
    uvbcr = customUVBorderColorR

    customUVBorderColorG = FloatField(default_value=-1.0)
    uvbcg = customUVBorderColorG

    customUVBorderColorB = FloatField(default_value=-1.0)
    uvbcb = customUVBorderColorB
