# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.shader_override import AttrValueField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class ShaderOverride(DG):
    __slots__ = ()

    NODE_TYPE = "shaderOverride"

    parentList = MessageField()
    pls = parentList

    next = MessageField()
    nxt = next

    previous = MessageField()
    prv = previous

    selfEnabled = BoolField()
    sen = selfEnabled

    parentEnabled = BoolField()
    pen = parentEnabled

    parentNumIsolatedChildren = LongField()
    pic = parentNumIsolatedChildren

    enabled = BoolField()
    en = enabled

    attribute = DataStringField()
    atr = attribute

    localRender = BoolField()
    local = localRender

    connectionStr = DataStringField()
    cs = connectionStr

    attrValue = AttrValueField()
    atv = attrValue
    attrValueR = attrValue.attrValueR
    atvr = attrValueR
    attrValueG = attrValue.attrValueG
    atvg = attrValueG
    attrValueB = attrValue.attrValueB
    atvb = attrValueB
