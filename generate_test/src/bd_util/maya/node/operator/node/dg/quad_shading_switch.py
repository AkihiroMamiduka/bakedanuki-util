# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.quad_shading_switch import (
    DefaultField,
    InputField,
    OutputField,
)
from ...attr.define.std.at.addr import AddrField


class QuadShadingSwitch(DG):
    __slots__ = ()

    NODE_TYPE = "quadShadingSwitch"

    objectId = AddrField()
    id = objectId

    input = InputField(multi=True)
    i = input

    # TODO: input.inTriple (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: input.inComp1 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: input.inComp2 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: input.inComp3 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: input.inSingle (attributeType=None, dataType=None) は未対応のため手動で追加してください

    default = DefaultField()
    def_ = default
    defTriple = default.defTriple
    dtr = defTriple
    defSingle = default.defSingle
    dsi = defSingle

    output = OutputField()
    out = output
    outTriple = output.outTriple
    otr = outTriple
    outSingle = output.outSingle
    osi = outSingle
