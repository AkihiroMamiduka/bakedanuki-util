# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_sky import (
    ColorField,
    OutColorField,
    OutTransparencyField,
    XField,
    YField,
    ZField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.byte import ByteField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class FormatEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MIRRORED_BALL = 0
    ANGULAR = 1
    LATLONG = 2


class FormatEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MIRRORED_BALL = 0
    ANGULAR = 1
    LATLONG = 2

    NAME_MAP = {
        MIRRORED_BALL: "mirrored_ball",
        ANGULAR: "angular",
        LATLONG: "latlong",
    }


class FormatEnumField(
    EnumField[FormatEnumAttrOperator, FormatEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FormatEnumAttrOperator
    PLUG_CLS = FormatEnumPlugOperator


class AiSky(DG):
    __slots__ = ()

    NODE_TYPE = "aiSky"

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

    color = ColorField(default_value=(1.0, 1.0, 1.0))
    colorR = color.colorR
    colorr = colorR
    colorG = color.colorG
    colorg = colorG
    colorB = color.colorB
    colorb = colorB

    intensity = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)

    visibility = ByteField(default_value=255, min_value=0, max_value=255)

    opaqueAlpha = BoolField(default_value=True)
    opaque_alpha = opaqueAlpha

    format = FormatEnumField(default_value=1)

    XAngle = FloatField(default_value=0.0)
    X_angle = XAngle

    YAngle = FloatField(default_value=0.0)
    Y_angle = YAngle

    ZAngle = FloatField(default_value=0.0)
    Z_angle = ZAngle

    X = XField(default_value=(1.0, 0.0, 0.0))
    XX = X.XX
    Xx = XX
    XY = X.XY
    Xy = XY
    XZ = X.XZ
    Xz = XZ

    Y = YField(default_value=(0.0, 1.0, 0.0))
    YX = Y.YX
    Yx = YX
    YY = Y.YY
    Yy = YY
    YZ = Y.YZ
    Yz = YZ

    Z = ZField(default_value=(0.0, 0.0, 1.0))
    ZX = Z.ZX
    Zx = ZX
    ZY = Z.ZY
    Zy = ZY
    ZZ = Z.ZZ
    Zz = ZZ
