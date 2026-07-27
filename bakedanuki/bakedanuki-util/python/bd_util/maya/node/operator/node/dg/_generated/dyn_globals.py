# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class GeneratedDynGlobals(DG):
    __slots__ = ()

    NODE_TYPE = "dynGlobals"

    overSamples = LongField(default_value=1, min_value=1)
    os = overSamples

    internalOverSamples = LongField(default_value=0, min_value=1, writable=False)
    ios = internalOverSamples

    useParticleDiskCache = BoolField(default_value=False)
    upd = useParticleDiskCache

    cacheDirectory = DataStringField()
    cd = cacheDirectory

    minFrameCached = LongField(default_value=0)
    mnf = minFrameCached

    maxFrameCached = LongField(default_value=0)
    mxf = maxFrameCached

    confirmedPath = DataStringField()
    cnp = confirmedPath

    confirmSceneName = DataStringField()
    csn = confirmSceneName
