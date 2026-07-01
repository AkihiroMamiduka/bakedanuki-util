# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class PassContributionMap(DG):
    __slots__ = ()

    NODE_TYPE = "passContributionMap"

    owner = MessageField(multi=True)
    ow = owner

    active = BoolField()
    a = active

    renderPass = MessageField(multi=True)
    rps = renderPass

    light = MessageField(multi=True)
    l = light

    dagObjects = MessageField(multi=True)
    o = dagObjects
