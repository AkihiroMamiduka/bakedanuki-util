# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.c_muscle_spline_deformer import (
    ControlDataBaseField,
    ControlDataField,
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    ShapeDataField,
    SquashDataField,
    WeightListField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField


class CMuscleSplineDeformer(DG):
    __slots__ = ()

    NODE_TYPE = "cMuscleSplineDeformer"

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

    controlData = ControlDataField(multi=True)
    cdata = controlData

    pointX = DoubleField()
    px = pointX

    pointY = DoubleField()
    py = pointY

    pointZ = DoubleField()
    pz = pointZ

    pointJiggleX = DoubleField()
    pjx = pointJiggleX

    pointJiggleY = DoubleField()
    pjy = pointJiggleY

    pointJiggleZ = DoubleField()
    pjz = pointJiggleZ

    tangentX = DoubleField()
    tgx = tangentX

    tangentY = DoubleField()
    tgy = tangentY

    tangentZ = DoubleField()
    tgz = tangentZ

    upX = DoubleField()
    ux = upX

    upY = DoubleField()
    uy = upY

    upZ = DoubleField()
    uz = upZ

    controlDataBase = ControlDataBaseField(multi=True)
    cdatab = controlDataBase

    pointXBase = DoubleField()
    pxb = pointXBase

    pointYBase = DoubleField()
    pyb = pointYBase

    pointZBase = DoubleField()
    pzb = pointZBase

    pointJiggleXBase = DoubleField()
    pjxb = pointJiggleXBase

    pointJiggleYBase = DoubleField()
    pjyb = pointJiggleYBase

    pointJiggleZBase = DoubleField()
    pjzb = pointJiggleZBase

    tangentXBase = DoubleField()
    tgxb = tangentXBase

    tangentYBase = DoubleField()
    tgyb = tangentYBase

    tangentZBase = DoubleField()
    tgzb = tangentZBase

    upXBase = DoubleField()
    uxb = upXBase

    upYBase = DoubleField()
    uyb = upYBase

    upZBase = DoubleField()
    uzb = upZBase

    uWts = DoubleField(multi=True, default_value=0.0)
    uwt = uWts

    squashData = SquashDataField(default_value=(0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1e-05, 0.0, 1.0, 0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0))
    sdata = squashData
    STATE = squashData.STATE
    STA = STATE
    curLen = squashData.curLen
    clen = curLen
    pctSquash = squashData.pctSquash
    psq = pctSquash
    pctStretch = squashData.pctStretch
    pst = pctStretch
    soften = squashData.soften
    sft = soften
    biasX = squashData.biasX
    bix = biasX
    biasZ = squashData.biasZ
    biz = biasZ
    biasTolernace = squashData.biasTolernace
    btol = biasTolernace
    manualSqSt = squashData.manualSqSt
    msqst = manualSqSt
    userScale = squashData.userScale
    usc = userScale
    SHAPING = squashData.SHAPING
    SHA = SHAPING
    enableShaping = squashData.enableShaping
    eshp = enableShaping
    shapingBlend = squashData.shapingBlend
    shbl = shapingBlend
    SQUASH = squashData.SQUASH
    SQA = SQUASH
    squashXStart = squashData.squashXStart
    sqxsta = squashXStart
    squashZStart = squashData.squashZStart
    sqzsta = squashZStart
    squashXMid = squashData.squashXMid
    sqxmid = squashXMid
    squashZMid = squashData.squashZMid
    sqzmid = squashZMid
    squashXEnd = squashData.squashXEnd
    sqxend = squashXEnd
    squashZEnd = squashData.squashZEnd
    sqzend = squashZEnd
    STRETCH = squashData.STRETCH
    STE = STRETCH
    stretchXStart = squashData.stretchXStart
    stxsta = stretchXStart
    stretchZStart = squashData.stretchZStart
    stzsta = stretchZStart
    stretchXMid = squashData.stretchXMid
    stxmid = stretchXMid
    stretchZMid = squashData.stretchZMid
    stzmid = stretchZMid
    stretchXEnd = squashData.stretchXEnd
    stxend = stretchXEnd
    stretchZEnd = squashData.stretchZEnd
    stzend = stretchZEnd

    shapeData = ShapeDataField(multi=True)
    shp = shapeData
