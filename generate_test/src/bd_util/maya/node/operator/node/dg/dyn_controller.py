# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class DynController(DG):
    __slots__ = ()

    NODE_TYPE = "dynController"

    lastEvalTime = DoubleField()
    let = lastEvalTime

    evalTime = DoubleField()
    evt = evalTime

    startTime = DoubleField()
    stt = startTime

    startFrame = DoubleField()
    stf = startFrame

    currEvalTime = DoubleField()
    cet = currEvalTime

    makeDirty = LongField()
    md = makeDirty

    output = BoolField()
    out = output

    traceDepth = LongField()
    td = traceDepth

    particleCache = BoolField()
    pc = particleCache

    cacheTime = DoubleField()
    ct = cacheTime

    doRunup = BoolField()
    dru = doRunup

    particlesOn = BoolField()
    pon = particlesOn

    allOn = BoolField()
    aon = allOn

    rigidOn = BoolField()
    rgo = rigidOn

    particleLOD = DoubleField()
    pld = particleLOD

    oversample = LongField()
    os = oversample

    seed = LongField()
    sd = seed

    autoCreate = BoolField()
    ac = autoCreate

    firstEval = BoolField()
    fev = firstEval

    allOnWhenRun = BoolField()
    awr = allOnWhenRun

    startRunup = BoolField()
    str = startRunup

    breakRunup = BoolField()
    brr = breakRunup
