# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_imager_overlay import (
    BackgroundColorField,
    FontColorField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class ValignEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TOP = 0
    CENTER = 1
    BOTTOM = 2


class ValignEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TOP = 0
    CENTER = 1
    BOTTOM = 2

    NAME_MAP = {
        TOP: "top",
        CENTER: "center",
        BOTTOM: "bottom",
    }


class ValignEnumField(
    EnumField[ValignEnumAttrOperator, ValignEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ValignEnumAttrOperator
    PLUG_CLS = ValignEnumPlugOperator


class HalignEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LEFT = 0
    CENTER = 1
    RIGHT = 2


class HalignEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LEFT = 0
    CENTER = 1
    RIGHT = 2

    NAME_MAP = {
        LEFT: "left",
        CENTER: "center",
        RIGHT: "right",
    }


class HalignEnumField(
    EnumField[HalignEnumAttrOperator, HalignEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HalignEnumAttrOperator
    PLUG_CLS = HalignEnumPlugOperator


class _GeneratedAiImagerOverlay(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerOverlay"

    out = MessageField(writable=False)

    input = MessageField()

    enable = BoolField(default_value=True)

    layerSelection = DataStringField()
    layer_selection = layerSelection

    outputSuffix = DataStringField()
    output_suffix = outputSuffix

    text = DataStringField()

    valign = ValignEnumField(default_value=2)

    halign = HalignEnumField(default_value=0)

    marginLeft = LongField(default_value=20, min_value=0, soft_max_value=100)
    margin_left = marginLeft

    marginRight = LongField(default_value=20, min_value=0, soft_max_value=100)
    margin_right = marginRight

    marginTop = LongField(default_value=20, min_value=0, soft_max_value=100)
    margin_top = marginTop

    marginBottom = LongField(default_value=20, min_value=0, soft_max_value=100)
    margin_bottom = marginBottom

    font = DataStringField()

    fontSize = LongField(default_value=24, min_value=0, soft_max_value=100)
    font_size = fontSize

    adjustFontSize = BoolField(default_value=True)
    adjust_font_size = adjustFontSize

    fontColor = FontColorField(default_value=(1.0, 1.0, 1.0))
    font_color = fontColor
    fontColorR = fontColor.fontColorR
    font_colorr = fontColorR
    fontColorG = fontColor.fontColorG
    font_colorg = fontColorG
    fontColorB = fontColor.fontColorB
    font_colorb = fontColorB

    backgroundOpacity = FloatField(default_value=0.699999988079071, min_value=0.0, max_value=1.0)
    background_opacity = backgroundOpacity

    backgroundColor = BackgroundColorField(default_value=(0.05000000074505806, 0.05000000074505806, 0.05000000074505806))
    background_color = backgroundColor
    backgroundColorR = backgroundColor.backgroundColorR
    background_colorr = backgroundColorR
    backgroundColorG = backgroundColor.backgroundColorG
    background_colorg = backgroundColorG
    backgroundColorB = backgroundColor.backgroundColorB
    background_colorb = backgroundColorB

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    customTokens = DataStringField(category="arnold")
    cusTok = customTokens
