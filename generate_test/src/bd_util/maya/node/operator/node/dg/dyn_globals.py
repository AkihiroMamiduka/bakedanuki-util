# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class DynGlobals(DG):
    __slots__ = ()

    NODE_TYPE = "dynGlobals"

    overSamples = LongField()
    os = overSamples

    internalOverSamples = LongField()
    ios = internalOverSamples

    useParticleDiskCache = BoolField()
    upd = useParticleDiskCache

    cacheDirectory = DataStringField()
    cd = cacheDirectory

    minFrameCached = LongField()
    mnf = minFrameCached

    maxFrameCached = LongField()
    mxf = maxFrameCached

    confirmedPath = DataStringField()
    cnp = confirmedPath

    confirmSceneName = DataStringField()
    csn = confirmSceneName
