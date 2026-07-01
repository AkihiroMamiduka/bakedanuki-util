# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.simple_volume_shader import (
    ColorField,
    FarPointWorldField,
    OutColorField,
    OutTransparencyField,
    PointWorldField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class SimpleVolumeShader(DG):
    __slots__ = ()

    NODE_TYPE = "simpleVolumeShader"

    parameter1 = FloatField()
    p1 = parameter1

    color = ColorField()
    c = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    pointWorld = PointWorldField()
    p = pointWorld
    pointWorldX = pointWorld.pointWorldX
    px = pointWorldX
    pointWorldY = pointWorld.pointWorldY
    py = pointWorldY
    pointWorldZ = pointWorld.pointWorldZ
    pz = pointWorldZ

    farPointWorld = FarPointWorldField()
    fp = farPointWorld
    farPointWorldX = farPointWorld.farPointWorldX
    fpx = farPointWorldX
    farPointWorldY = farPointWorld.farPointWorldY
    fpy = farPointWorldY
    farPointWorldZ = farPointWorld.farPointWorldZ
    fpz = farPointWorldZ

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB
