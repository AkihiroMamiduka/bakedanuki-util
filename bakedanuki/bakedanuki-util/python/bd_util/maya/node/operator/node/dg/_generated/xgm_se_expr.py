# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.xgm_se_expr import OutColorField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedXgmSeExpr(DG):
    __slots__ = ()

    NODE_TYPE = "xgmSeExpr"

    expression = DataStringField()
    expr = expression

    outAlpha = FloatField(default_value=1.0, writable=False)
    oa = outAlpha

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB
