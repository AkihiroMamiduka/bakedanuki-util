# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_material_x_shader import (
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.dt.string import DataStringField


class AiMaterialXShader(DG):
    __slots__ = ()

    NODE_TYPE = "aiMaterialXShader"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    ocl = outColor
    outColorR = outColor.outColorR
    oclr = outColorR
    outColorG = outColor.outColorG
    oclg = outColorG
    outColorB = outColor.outColorB
    oclb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    materialXFilePath = DataStringField()
    mtlxpath = materialXFilePath

    materialName = DataStringField()
    mtlname = materialName

    outDisplacement = MessageField()
    disp = outDisplacement

    outVolume = MessageField()
    volm = outVolume
