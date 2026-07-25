# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.unit.time import TimeField


class _GeneratedSequenceManager(DG):
    __slots__ = ()

    NODE_TYPE = "sequenceManager"

    outTime = TimeField(default_value=2.5)
    o = outTime

    rangeMin = TimeField(default_value=0.0)
    rmin = rangeMin

    rangeMax = TimeField(default_value=0.0)
    rmax = rangeMax

    rangeEnabled = BoolField(default_value=False)
    ren = rangeEnabled

    enabled = BoolField(default_value=False)
    en = enabled

    skipGaps = BoolField(default_value=False)
    sg = skipGaps

    sequences = MessageField(multi=True, readable=False)
    seqts = sequences

    trackInfoManager = MessageField()
    tim = trackInfoManager
