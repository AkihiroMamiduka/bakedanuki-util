# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.unit_scalar.time import TimeField


class SequenceManager(DG):
    __slots__ = ()

    NODE_TYPE = "sequenceManager"

    outTime = TimeField()
    o = outTime

    rangeMin = TimeField()
    rmin = rangeMin

    rangeMax = TimeField()
    rmax = rangeMax

    rangeEnabled = BoolField()
    ren = rangeEnabled

    enabled = BoolField()
    en = enabled

    skipGaps = BoolField()
    sg = skipGaps

    sequences = MessageField(multi=True)
    seqts = sequences

    trackInfoManager = MessageField()
    tim = trackInfoManager
