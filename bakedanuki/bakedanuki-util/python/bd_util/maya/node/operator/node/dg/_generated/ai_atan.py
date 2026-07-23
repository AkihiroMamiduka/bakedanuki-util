# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_atan import (
    OutColorField,
    OutTransparencyField,
    XField,
    YField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)


class UnitsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RADIANS = 0
    DEGREES = 1


class UnitsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RADIANS = 0
    DEGREES = 1

    NAME_MAP = {
        RADIANS: "radians",
        DEGREES: "degrees",
    }


class UnitsEnumField(
    EnumField[UnitsEnumAttrOperator, UnitsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UnitsEnumAttrOperator
    PLUG_CLS = UnitsEnumPlugOperator


class _GeneratedAiAtan(DG):
    __slots__ = ()

    NODE_TYPE = "aiAtan"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    y = YField(default_value=(0.0, 0.0, 0.0))
    yR = y.yR
    yr = yR
    yG = y.yG
    yg = yG
    yB = y.yB
    yb = yB

    x = XField(default_value=(0.0, 0.0, 0.0))
    xR = x.xR
    xr = xR
    xG = x.xG
    xg = xG
    xB = x.xB
    xb = xB

    units = UnitsEnumField(default_value=0)
