# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.material_x_surface_shader import OutColorField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long_long_int import LongLongIntField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField


class MaterialXSurfaceShader(DG):
    __slots__ = ()

    NODE_TYPE = "MaterialXSurfaceShader"

    ufePath = DataStringField()
    up = ufePath

    updateId = LongLongIntField()
    upid = updateId

    resyncId = LongLongIntField()
    rsid = resyncId

    stack = TypedField()
    sk = stack

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    vp2Transparency = FloatField()
    vp2t = vp2Transparency

    displacement = FloatField()
    d = displacement

    renderDocument = DataStringField()
    rd = renderDocument
