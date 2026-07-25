# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_user_data_color import (
    DefaultField,
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedAiUserDataColor(DG):
    __slots__ = ()

    NODE_TYPE = "aiUserDataColor"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    outa = outAlpha

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    attribute = DataStringField()
    colorAttrName = attribute

    defaultA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    defaultValuea = defaultA

    default = DefaultField(default_value=(0.0, 0.0, 0.0))
    defaultValue = default
    defaultR = default.defaultR
    defaultValuer = defaultR
    defaultG = default.defaultG
    defaultValueg = defaultG
    defaultB = default.defaultB
    defaultValueb = defaultB
