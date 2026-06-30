# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_fog import (
    ColorField,
    GroundNormalField,
    GroundPointField,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiFog(DG):
    __slots__ = ()

    NODE_TYPE = "aiFog"

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

    distance = FloatField()

    height = FloatField()

    color = ColorField()
    colorR = color.colorR
    colorr = colorR
    colorG = color.colorG
    colorg = colorG
    colorB = color.colorB
    colorb = colorB

    groundPoint = GroundPointField()
    ground_point = groundPoint
    groundPointX = groundPoint.groundPointX
    ground_pointx = groundPointX
    groundPointY = groundPoint.groundPointY
    ground_pointy = groundPointY
    groundPointZ = groundPoint.groundPointZ
    ground_pointz = groundPointZ

    groundNormal = GroundNormalField()
    ground_normal = groundNormal
    groundNormalX = groundNormal.groundNormalX
    ground_normalx = groundNormalX
    groundNormalY = groundNormal.groundNormalY
    ground_normaly = groundNormalY
    groundNormalZ = groundNormal.groundNormalZ
    ground_normalz = groundNormalZ
