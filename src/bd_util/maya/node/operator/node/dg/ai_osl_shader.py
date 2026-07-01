# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_osl_shader import OutTransparencyField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.dt.string import DataStringField


class AiOslShader(DG):
    __slots__ = ()

    NODE_TYPE = "aiOslShader"

    outValue = MessageField()
    out = outValue

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    shadername = DataStringField()

    code = DataStringField()

    aiUserOptions = DataStringField()
    ai_user_options = aiUserOptions

    codeCache = DataStringField()
    code_cache = codeCache
