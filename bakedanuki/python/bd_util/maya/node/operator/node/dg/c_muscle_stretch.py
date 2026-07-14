# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.c_muscle_stretch import (
    EnvelopeWeightsListField,
    ForceEndField,
    ForceMidField,
    ForceStartField,
    FunctionField,
    InputField,
    WeightListField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField


class SCALINGEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class SCALINGEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class SCALINGEnumField(
    EnumField[SCALINGEnumAttrOperator, SCALINGEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SCALINGEnumAttrOperator
    PLUG_CLS = SCALINGEnumPlugOperator


class WEIGHTINGEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class WEIGHTINGEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class WEIGHTINGEnumField(
    EnumField[WEIGHTINGEnumAttrOperator, WEIGHTINGEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WEIGHTINGEnumAttrOperator
    PLUG_CLS = WEIGHTINGEnumPlugOperator


class JIGGLEEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class JIGGLEEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class JIGGLEEnumField(
    EnumField[JIGGLEEnumAttrOperator, JIGGLEEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = JIGGLEEnumAttrOperator
    PLUG_CLS = JIGGLEEnumPlugOperator


class CMuscleStretch(DG):
    __slots__ = ()

    NODE_TYPE = "cMuscleStretch"

    input = InputField(multi=True)
    ip = input

    weightFunction = TypedField(multi=True)
    wfl = weightFunction

    outputGeometry = TypedField(multi=True, writable=False)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(multi=True, default_value=1.0, writable=False)
    ocw = envelopeWeightsList

    blockGPU = BoolField(default_value=False)
    bgp = blockGPU

    envelope = FloatField(default_value=1.0, min_value=-2.0, max_value=2.0, soft_min_value=0.0, soft_max_value=1.0)
    en = envelope

    function = FunctionField(default_value=(0, 0, 0), readable=False)
    f = function
    fchild1 = function.fchild1
    f1 = fchild1
    fchild2 = function.fchild2
    f2 = fchild2
    fchild3 = function.fchild3
    f3 = fchild3

    map64BitIndices = TypedField()
    map = map64BitIndices

    weightList = WeightListField(multi=True, default_value=1.0)
    wl = weightList

    worldMatrixStart = MatrixField()
    wms = worldMatrixStart

    worldMatrixMid = MatrixField()
    wmm = worldMatrixMid

    worldMatrixEnd = MatrixField()
    wme = worldMatrixEnd

    worldMatrixStartBase = MatrixField()
    wmsb = worldMatrixStartBase

    worldMatrixMidBase = MatrixField()
    wmmb = worldMatrixMidBase

    worldMatrixEndBase = MatrixField()
    wmeb = worldMatrixEndBase

    SCALING = SCALINGEnumField(default_value=0)
    SCL = SCALING

    manualSquish = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    mans = manualSquish

    maxStretch = DoubleField(default_value=2.0, min_value=1.0)
    mst = maxStretch

    stretchStart = DoubleField(default_value=1.0)
    st1 = stretchStart

    stretchMid = DoubleField(default_value=0.5)
    st2 = stretchMid

    stretchEnd = DoubleField(default_value=1.0)
    st3 = stretchEnd

    maxSquash = DoubleField(default_value=0.5, min_value=1e-06, max_value=1.0)
    msq = maxSquash

    squashStart = DoubleField(default_value=1.0)
    sq1 = squashStart

    squashMid = DoubleField(default_value=1.5)
    sq2 = squashMid

    squashEnd = DoubleField(default_value=1.0)
    sq3 = squashEnd

    xFactor = DoubleField(default_value=1.0)
    xfc = xFactor

    zFactor = DoubleField(default_value=1.0)
    zfc = zFactor

    WEIGHTING = WEIGHTINGEnumField(default_value=0)
    WTNG = WEIGHTING

    innerFalloffStart = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    ifs = innerFalloffStart

    innerFalloffMid = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    ifm = innerFalloffMid

    innerFalloffEnd = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    ife = innerFalloffEnd

    outerFalloffStart = DoubleField(default_value=0.9, min_value=0.0, max_value=1.0)
    ofs = outerFalloffStart

    outerFalloffMid = DoubleField(default_value=0.9, min_value=0.0, max_value=1.0)
    ofm = outerFalloffMid

    outerFalloffEnd = DoubleField(default_value=0.9, min_value=0.0, max_value=1.0)
    ofe = outerFalloffEnd

    weightStart = DoubleField(default_value=1.0, min_value=0.0)
    wts = weightStart

    weightMid = DoubleField(default_value=1.0, min_value=0.0)
    wtm = weightMid

    weightEnd = DoubleField(default_value=1.0, min_value=0.0)
    wte = weightEnd

    JIGGLE = JIGGLEEnumField(default_value=0)
    JIG = JIGGLE

    resetFrame = DoubleField(default_value=0.0, min_value=-1024.0)
    rf = resetFrame

    inTime = DoubleField(default_value=0.0)
    it = inTime

    jiggleStart = DoubleField(default_value=0.0, min_value=0.0)
    js = jiggleStart

    jiggleMid = DoubleField(default_value=1.0, min_value=0.0)
    jm = jiggleMid

    jiggleEnd = DoubleField(default_value=0.0, min_value=0.0)
    je = jiggleEnd

    cycleStart = DoubleField(default_value=8.0, min_value=0.0)
    cs = cycleStart

    cycleMid = DoubleField(default_value=8.0, min_value=0.0)
    cm = cycleMid

    cycleEnd = DoubleField(default_value=8.0, min_value=0.0)
    ce = cycleEnd

    restStart = LongField(default_value=24, min_value=0)
    rs = restStart

    restMid = LongField(default_value=24, min_value=0)
    rm = restMid

    restEnd = LongField(default_value=24, min_value=0)
    re = restEnd

    dampenOnSquash = DoubleField(default_value=0.75, min_value=0.0, max_value=1.0)
    dmpsq = dampenOnSquash

    dampenOnStretch = DoubleField(default_value=0.75, min_value=0.0, max_value=1.0)
    dmpst = dampenOnStretch

    forceStart = ForceStartField(multi=True, default_value=(0.0, 0.0, 0.0))
    fst = forceStart

    forceMid = ForceMidField(multi=True, default_value=(0.0, 0.0, 0.0))
    fmd = forceMid

    forceEnd = ForceEndField(multi=True, default_value=(0.0, 0.0, 0.0))
    fed = forceEnd

    lengthCalc = DoubleField(default_value=0.0)
    len = lengthCalc
