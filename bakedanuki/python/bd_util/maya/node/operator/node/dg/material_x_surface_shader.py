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

    updateId = LongLongIntField(default_value=1, writable=False)
    upid = updateId

    resyncId = LongLongIntField(default_value=1, writable=False)
    rsid = resyncId

    stack = TypedField(readable=False)
    sk = stack

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    vp2Transparency = FloatField(default_value=0.0)
    vp2t = vp2Transparency

    displacement = FloatField(default_value=0.0, writable=False)
    d = displacement

    renderDocument = DataStringField(writable=False)
    rd = renderDocument
