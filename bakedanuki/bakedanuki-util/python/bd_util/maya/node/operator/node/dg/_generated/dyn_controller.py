# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class _GeneratedDynController(DG):
    __slots__ = ()

    NODE_TYPE = "dynController"

    lastEvalTime = DoubleField(default_value=0.0)
    let = lastEvalTime

    evalTime = DoubleField(default_value=0.0)
    evt = evalTime

    startTime = DoubleField(default_value=0.0)
    stt = startTime

    startFrame = DoubleField(default_value=1.0)
    stf = startFrame

    currEvalTime = DoubleField(default_value=0.0)
    cet = currEvalTime

    makeDirty = LongField(default_value=0)
    md = makeDirty

    output = BoolField(default_value=False, writable=False)
    out = output

    traceDepth = LongField(default_value=10)
    td = traceDepth

    particleCache = BoolField(default_value=False)
    pc = particleCache

    cacheTime = DoubleField(default_value=0.0)
    ct = cacheTime

    doRunup = BoolField(default_value=True)
    dru = doRunup

    particlesOn = BoolField(default_value=True)
    pon = particlesOn

    allOn = BoolField(default_value=True)
    aon = allOn

    rigidOn = BoolField(default_value=True)
    rgo = rigidOn

    particleLOD = DoubleField(default_value=1.0)
    pld = particleLOD

    oversample = LongField(default_value=1)
    os = oversample

    seed = LongField(default_value=0)
    sd = seed

    autoCreate = BoolField(default_value=True)
    ac = autoCreate

    firstEval = BoolField(default_value=True)
    fev = firstEval

    allOnWhenRun = BoolField(default_value=True)
    awr = allOnWhenRun

    startRunup = BoolField(default_value=False)
    str = startRunup

    breakRunup = BoolField(default_value=False)
    brr = breakRunup
