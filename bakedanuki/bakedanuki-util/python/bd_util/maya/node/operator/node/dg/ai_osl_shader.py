# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_osl_shader import OutTransparencyField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.dt.string import DataStringField


class AiOslShader(DG):
    __slots__ = ()

    NODE_TYPE = "aiOslShader"

    outValue = MessageField(writable=False)
    out = outValue

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    shadername = DataStringField()

    code = DataStringField()

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    codeCache = DataStringField(category="arnold")
    code_cache = codeCache
