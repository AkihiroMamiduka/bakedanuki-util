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

    outColor = OutColorField(default_value=(0.5, 0.5, 0.5), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.5, 0.5, 0.5), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    normalCamera = NormalCameraField(default_value=(0.0, 0.0, 0.0))
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    hardwareColor = HardwareColorField(default_value=(0.5, 0.5, 0.5))
    hwc = hardwareColor
    hardwareColorR = hardwareColor.hardwareColorR
    hwcr = hardwareColorR
    hardwareColorG = hardwareColor.hardwareColorG
    hwcg = hardwareColorG
    hardwareColorB = hardwareColor.hardwareColorB
    hwcb = hardwareColorB

    lineWidth = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    line_width = lineWidth

    fillColor = FillColorField(default_value=(1.0, 1.0, 1.0))
    fill_color = fillColor
    fillColorR = fillColor.fillColorR
    fill_colorr = fillColorR
    fillColorG = fillColor.fillColorG
    fill_colorg = fillColorG
    fillColorB = fillColor.fillColorB
    fill_colorb = fillColorB

    lineColor = LineColorField(default_value=(0.0, 0.0, 0.0))
    line_color = lineColor
    lineColorR = lineColor.lineColorR
    line_colorr = lineColorR
    lineColorG = lineColor.lineColorG
    line_colorg = lineColorG
    lineColorB = lineColor.lineColorB
    line_colorb = lineColorB

    rasterSpace = BoolField(default_value=True)
    raster_space = rasterSpace

    edgeType = EdgeTypeEnumField(default_value=0)
    edge_type = edgeType
