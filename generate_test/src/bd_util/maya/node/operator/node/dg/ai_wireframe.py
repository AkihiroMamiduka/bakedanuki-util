# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_wireframe import (
    FillColorField,
    HardwareColorField,
    LineColorField,
    NormalCameraField,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class EdgeTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TRIANGLES = 0
    POLYGONS = 1
    PATCHES = 2


class EdgeTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TRIANGLES = 0
    POLYGONS = 1
    PATCHES = 2

    NAME_MAP = {
        TRIANGLES: "triangles",
        POLYGONS: "polygons",
        PATCHES: "patches",
    }


class EdgeTypeEnumField(
    EnumField[EdgeTypeEnumAttrOperator, EdgeTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EdgeTypeEnumAttrOperator
    PLUG_CLS = EdgeTypeEnumPlugOperator


class AiWireframe(DG):
    __slots__ = ()

    NODE_TYPE = "aiWireframe"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    normalCamera = NormalCameraField()
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    hardwareColor = HardwareColorField()
    hwc = hardwareColor
    hardwareColorR = hardwareColor.hardwareColorR
    hwcr = hardwareColorR
    hardwareColorG = hardwareColor.hardwareColorG
    hwcg = hardwareColorG
    hardwareColorB = hardwareColor.hardwareColorB
    hwcb = hardwareColorB

    lineWidth = FloatField()
    line_width = lineWidth

    fillColor = FillColorField()
    fill_color = fillColor
    fillColorR = fillColor.fillColorR
    fill_colorr = fillColorR
    fillColorG = fillColor.fillColorG
    fill_colorg = fillColorG
    fillColorB = fillColor.fillColorB
    fill_colorb = fillColorB

    lineColor = LineColorField()
    line_color = lineColor
    lineColorR = lineColor.lineColorR
    line_colorr = lineColorR
    lineColorG = lineColor.lineColorG
    line_colorg = lineColorG
    lineColorB = lineColor.lineColorB
    line_colorb = lineColorB

    rasterSpace = BoolField()
    raster_space = rasterSpace

    edgeType = EdgeTypeEnumField()
    edge_type = edgeType
