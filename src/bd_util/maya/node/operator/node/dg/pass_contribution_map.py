# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class PassContributionMap(DG):
    __slots__ = ()

    NODE_TYPE = "passContributionMap"

    owner = MessageField(multi=True, readable=False)
    ow = owner

    active = BoolField(default_value=True)
    a = active

    renderPass = MessageField(multi=True, readable=False)
    rps = renderPass

    light = MessageField(multi=True, readable=False)
    l = light

    dagObjects = MessageField(multi=True, readable=False)
    o = dagObjects
