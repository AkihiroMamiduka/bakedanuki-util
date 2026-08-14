# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class GeneratedCustomRigRetargeterNode(DG):
    __slots__ = ()

    NODE_TYPE = "CustomRigRetargeterNode"

    connected = LongField(default_value=0)
    c = connected

    source = MessageField()
    s = source

    destination = MessageField()
    d = destination

    mappings = MessageField(multi=True)
    ms = mappings

    pythonVar = DataStringField()
    pv = pythonVar
