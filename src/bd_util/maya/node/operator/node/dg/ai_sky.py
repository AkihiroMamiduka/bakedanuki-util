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

    color = ColorField()
    colorR = color.colorR
    colorr = colorR
    colorG = color.colorG
    colorg = colorG
    colorB = color.colorB
    colorb = colorB

    intensity = FloatField()

    visibility = ByteField()

    opaqueAlpha = BoolField()
    opaque_alpha = opaqueAlpha

    format = FormatEnumField()

    XAngle = FloatField()
    X_angle = XAngle

    YAngle = FloatField()
    Y_angle = YAngle

    ZAngle = FloatField()
    Z_angle = ZAngle

    X = XField()
    XX = X.XX
    Xx = XX
    XY = X.XY
    Xy = XY
    XZ = X.XZ
    Xz = XZ

    Y = YField()
    YX = Y.YX
    Yx = YX
    YY = Y.YY
    Yy = YY
    YZ = Y.YZ
    Yz = YZ

    Z = ZField()
    ZX = Z.ZX
    Zx = ZX
    ZY = Z.ZY
    Zy = ZY
    ZZ = Z.ZZ
    Zz = ZZ
