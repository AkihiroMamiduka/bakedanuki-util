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

    controlData = ControlDataField(multi=True)
    cdata = controlData

    # TODO: controlData.pointX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlData.pointY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlData.pointZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlData.pointJiggleX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlData.pointJiggleY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlData.pointJiggleZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlData.tangentX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlData.tangentY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlData.tangentZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlData.upX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlData.upY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlData.upZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    controlDataBase = ControlDataBaseField(multi=True)
    cdatab = controlDataBase

    # TODO: controlDataBase.pointXBase (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlDataBase.pointYBase (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlDataBase.pointZBase (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlDataBase.pointJiggleXBase (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlDataBase.pointJiggleYBase (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlDataBase.pointJiggleZBase (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlDataBase.tangentXBase (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlDataBase.tangentYBase (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlDataBase.tangentZBase (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlDataBase.upXBase (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlDataBase.upYBase (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: controlDataBase.upZBase (attributeType=None, dataType=None) は未対応のため手動で追加してください

    uWts = DoubleField(multi=True)
    uwt = uWts

    squashData = SquashDataField()
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
