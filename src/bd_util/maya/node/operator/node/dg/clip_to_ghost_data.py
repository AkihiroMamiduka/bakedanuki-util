# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField


class ClipToGhostData(DG):
    __slots__ = ()

    NODE_TYPE = "clipToGhostData"

    members = MessageField(multi=True)
    m = members

    character = MessageField()
    c = character

    clipSourceStart = TimeField(multi=True, default_value=0.0)
    css = clipSourceStart

    clipSourceEnd = TimeField(multi=True, default_value=0.0)
    cse = clipSourceEnd

    clipPreCycle = DoubleField(multi=True, default_value=0.0)
    cpr = clipPreCycle

    clipPostCycle = DoubleField(multi=True, default_value=0.0)
    cpo = clipPostCycle

    clipIntermediatePoses = LongField(multi=True, default_value=0)
    cip = clipIntermediatePoses

    clipGhostData = TypedField(multi=True, writable=False)
    cgd = clipGhostData
