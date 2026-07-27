# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_fog import (
    ColorField,
    GroundNormalField,
    GroundPointField,
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class GeneratedAiFog(DG):
    __slots__ = ()

    NODE_TYPE = "aiFog"

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

    distance = FloatField(default_value=0.019999999552965164, min_value=0.0, soft_max_value=1000.0)

    height = FloatField(default_value=5.0, min_value=0.0, soft_max_value=1000.0)

    color = ColorField(default_value=(1.0, 1.0, 1.0))
    colorR = color.colorR
    colorr = colorR
    colorG = color.colorG
    colorg = colorG
    colorB = color.colorB
    colorb = colorB

    groundPoint = GroundPointField(default_value=(0.0, 0.0, 0.0))
    ground_point = groundPoint
    groundPointX = groundPoint.groundPointX
    ground_pointx = groundPointX
    groundPointY = groundPoint.groundPointY
    ground_pointy = groundPointY
    groundPointZ = groundPoint.groundPointZ
    ground_pointz = groundPointZ

    groundNormal = GroundNormalField(default_value=(0.0, 0.0, 1.0))
    ground_normal = groundNormal
    groundNormalX = groundNormal.groundNormalX
    ground_normalx = groundNormalX
    groundNormalY = groundNormal.groundNormalY
    ground_normaly = groundNormalY
    groundNormalZ = groundNormal.groundNormalZ
    ground_normalz = groundNormalZ
