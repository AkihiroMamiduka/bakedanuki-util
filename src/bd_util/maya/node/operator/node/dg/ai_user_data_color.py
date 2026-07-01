# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_user_data_color import (
    DefaultField,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class AiUserDataColor(DG):
    __slots__ = ()

    NODE_TYPE = "aiUserDataColor"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField()
    outa = outAlpha

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    attribute = DataStringField()
    colorAttrName = attribute

    defaultA = FloatField()
    defaultValuea = defaultA

    default = DefaultField()
    defaultValue = default
    defaultR = default.defaultR
    defaultValuer = defaultR
    defaultG = default.defaultG
    defaultValueg = defaultG
    defaultB = default.defaultB
    defaultValueb = defaultB
