# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.xgm_se_expr import OutColorField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class XgmSeExpr(DG):
    __slots__ = ()

    NODE_TYPE = "xgmSeExpr"

    expression = DataStringField()
    expr = expression

    outAlpha = FloatField()
    oa = outAlpha

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB
