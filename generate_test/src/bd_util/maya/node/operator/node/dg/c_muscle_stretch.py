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

    outputGeometry = TypedField(multi=True)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(multi=True)
    ocw = envelopeWeightsList

    blockGPU = BoolField()
    bgp = blockGPU

    envelope = FloatField()
    en = envelope

    function = FunctionField()
    f = function
    fchild1 = function.fchild1
    f1 = fchild1
    fchild2 = function.fchild2
    f2 = fchild2
    fchild3 = function.fchild3
    f3 = fchild3

    map64BitIndices = TypedField()
    map = map64BitIndices

    weightList = WeightListField(multi=True)
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

    SCALING = SCALINGEnumField()
    SCL = SCALING

    manualSquish = DoubleField()
    mans = manualSquish

    maxStretch = DoubleField()
    mst = maxStretch

    stretchStart = DoubleField()
    st1 = stretchStart

    stretchMid = DoubleField()
    st2 = stretchMid

    stretchEnd = DoubleField()
    st3 = stretchEnd

    maxSquash = DoubleField()
    msq = maxSquash

    squashStart = DoubleField()
    sq1 = squashStart

    squashMid = DoubleField()
    sq2 = squashMid

    squashEnd = DoubleField()
    sq3 = squashEnd

    xFactor = DoubleField()
    xfc = xFactor

    zFactor = DoubleField()
    zfc = zFactor

    WEIGHTING = WEIGHTINGEnumField()
    WTNG = WEIGHTING

    innerFalloffStart = DoubleField()
    ifs = innerFalloffStart

    innerFalloffMid = DoubleField()
    ifm = innerFalloffMid

    innerFalloffEnd = DoubleField()
    ife = innerFalloffEnd

    outerFalloffStart = DoubleField()
    ofs = outerFalloffStart

    outerFalloffMid = DoubleField()
    ofm = outerFalloffMid

    outerFalloffEnd = DoubleField()
    ofe = outerFalloffEnd

    weightStart = DoubleField()
    wts = weightStart

    weightMid = DoubleField()
    wtm = weightMid

    weightEnd = DoubleField()
    wte = weightEnd

    JIGGLE = JIGGLEEnumField()
    JIG = JIGGLE

    resetFrame = DoubleField()
    rf = resetFrame

    inTime = DoubleField()
    it = inTime

    jiggleStart = DoubleField()
    js = jiggleStart

    jiggleMid = DoubleField()
    jm = jiggleMid

    jiggleEnd = DoubleField()
    je = jiggleEnd

    cycleStart = DoubleField()
    cs = cycleStart

    cycleMid = DoubleField()
    cm = cycleMid

    cycleEnd = DoubleField()
    ce = cycleEnd

    restStart = LongField()
    rs = restStart

    restMid = LongField()
    rm = restMid

    restEnd = LongField()
    re = restEnd

    dampenOnSquash = DoubleField()
    dmpsq = dampenOnSquash

    dampenOnStretch = DoubleField()
    dmpst = dampenOnStretch

    forceStart = ForceStartField(multi=True)
    fst = forceStart

    forceMid = ForceMidField(multi=True)
    fmd = forceMid

    forceEnd = ForceEndField(multi=True)
    fed = forceEnd

    lengthCalc = DoubleField()
    len = lengthCalc
