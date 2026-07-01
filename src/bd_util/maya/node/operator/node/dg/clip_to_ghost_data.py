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

    clipSourceStart = TimeField(multi=True)
    css = clipSourceStart

    clipSourceEnd = TimeField(multi=True)
    cse = clipSourceEnd

    clipPreCycle = DoubleField(multi=True)
    cpr = clipPreCycle

    clipPostCycle = DoubleField(multi=True)
    cpo = clipPostCycle

    clipIntermediatePoses = LongField(multi=True)
    cip = clipIntermediatePoses

    clipGhostData = TypedField(multi=True)
    cgd = clipGhostData
