# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.long_compound.long3_compound._base import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
)


class STATEEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class STATEEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class STATEEnumField(
    EnumField[STATEEnumAttrOperator, STATEEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = STATEEnumAttrOperator
    PLUG_CLS = STATEEnumPlugOperator


class SHAPINGEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class SHAPINGEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class SHAPINGEnumField(
    EnumField[SHAPINGEnumAttrOperator, SHAPINGEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SHAPINGEnumAttrOperator
    PLUG_CLS = SHAPINGEnumPlugOperator


class SQUASHEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class SQUASHEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class SQUASHEnumField(
    EnumField[SQUASHEnumAttrOperator, SQUASHEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SQUASHEnumAttrOperator
    PLUG_CLS = SQUASHEnumPlugOperator


class STRETCHEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class STRETCHEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class STRETCHEnumField(
    EnumField[STRETCHEnumAttrOperator, STRETCHEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = STRETCHEnumAttrOperator
    PLUG_CLS = STRETCHEnumPlugOperator


class InputPlugOperator(
    CompoundPlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputGeometry", "ig"),
        ("groupId", "gi"),
        ("componentTagExpression", "gtg"),
    )

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField()
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputAttrOperator(
    CompoundAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField()
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputField(
    CompoundField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator


class EnvelopeWeightsListPlugOperator(
    CompoundPlugOperator["EnvelopeWeightsListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("envelopeWeights", "owt"),
    )

    envelopeWeights = FloatField()
    owt = envelopeWeights


class EnvelopeWeightsListAttrOperator(
    CompoundAttrOperator[EnvelopeWeightsListPlugOperator]
):
    __slots__ = ()

    envelopeWeights = FloatField()
    owt = envelopeWeights


class EnvelopeWeightsListField(
    CompoundField[EnvelopeWeightsListAttrOperator, EnvelopeWeightsListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EnvelopeWeightsListAttrOperator
    PLUG_CLS = EnvelopeWeightsListPlugOperator


class FunctionPlugOperator(
    Long3CompoundBasePlugOperator["FunctionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fchild1", "f1"),
        ("fchild2", "f2"),
        ("fchild3", "f3"),
    )

    fchild1 = LongField()
    f1 = fchild1

    fchild2 = LongField()
    f2 = fchild2

    fchild3 = LongField()
    f3 = fchild3


class FunctionAttrOperator(
    Long3CompoundBaseAttrOperator[FunctionPlugOperator]
):
    __slots__ = ()

    fchild1 = LongField()
    f1 = fchild1

    fchild2 = LongField()
    f2 = fchild2

    fchild3 = LongField()
    f3 = fchild3


class FunctionField(
    Long3CompoundBaseField[FunctionAttrOperator, FunctionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FunctionAttrOperator
    PLUG_CLS = FunctionPlugOperator

    fchild1 = LongField()
    f1 = fchild1

    fchild2 = LongField()
    f2 = fchild2

    fchild3 = LongField()
    f3 = fchild3


class WeightListPlugOperator(
    CompoundPlugOperator["WeightListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weights", "wl.w"),
    )

    weights = FloatField()


class WeightListAttrOperator(
    CompoundAttrOperator[WeightListPlugOperator]
):
    __slots__ = ()

    weights = FloatField()


class WeightListField(
    CompoundField[WeightListAttrOperator, WeightListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListAttrOperator
    PLUG_CLS = WeightListPlugOperator


class ControlDataPlugOperator(
    CompoundPlugOperator["ControlDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("point", "pt"),
        ("pointJiggle", "pj"),
        ("tangent", "tg"),
        ("up", "u"),
    )

    point = CompoundField()
    pt = point

    pointJiggle = CompoundField()
    pj = pointJiggle

    tangent = CompoundField()
    tg = tangent

    up = CompoundField()
    u = up


class ControlDataAttrOperator(
    CompoundAttrOperator[ControlDataPlugOperator]
):
    __slots__ = ()

    point = CompoundField()
    pt = point

    pointJiggle = CompoundField()
    pj = pointJiggle

    tangent = CompoundField()
    tg = tangent

    up = CompoundField()
    u = up


class ControlDataField(
    CompoundField[ControlDataAttrOperator, ControlDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ControlDataAttrOperator
    PLUG_CLS = ControlDataPlugOperator


class ControlDataBasePlugOperator(
    CompoundPlugOperator["ControlDataBaseAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointBase", "ptb"),
        ("pointJiggleBase", "pjb"),
        ("tangentBase", "tgb"),
        ("upBase", "ub"),
    )

    pointBase = CompoundField()
    ptb = pointBase

    pointJiggleBase = CompoundField()
    pjb = pointJiggleBase

    tangentBase = CompoundField()
    tgb = tangentBase

    upBase = CompoundField()
    ub = upBase


class ControlDataBaseAttrOperator(
    CompoundAttrOperator[ControlDataBasePlugOperator]
):
    __slots__ = ()

    pointBase = CompoundField()
    ptb = pointBase

    pointJiggleBase = CompoundField()
    pjb = pointJiggleBase

    tangentBase = CompoundField()
    tgb = tangentBase

    upBase = CompoundField()
    ub = upBase


class ControlDataBaseField(
    CompoundField[ControlDataBaseAttrOperator, ControlDataBasePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ControlDataBaseAttrOperator
    PLUG_CLS = ControlDataBasePlugOperator


class SquashDataPlugOperator(
    CompoundPlugOperator["SquashDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("STATE", "STA"),
        ("curLen", "clen"),
        ("pctSquash", "psq"),
        ("pctStretch", "pst"),
        ("soften", "sft"),
        ("biasX", "bix"),
        ("biasZ", "biz"),
        ("biasTolernace", "btol"),
        ("manualSqSt", "msqst"),
        ("userScale", "usc"),
        ("SHAPING", "SHA"),
        ("enableShaping", "eshp"),
        ("shapingBlend", "shbl"),
        ("SQUASH", "SQA"),
        ("squashXStart", "sqxsta"),
        ("squashZStart", "sqzsta"),
        ("squashXMid", "sqxmid"),
        ("squashZMid", "sqzmid"),
        ("squashXEnd", "sqxend"),
        ("squashZEnd", "sqzend"),
        ("STRETCH", "STE"),
        ("stretchXStart", "stxsta"),
        ("stretchZStart", "stzsta"),
        ("stretchXMid", "stxmid"),
        ("stretchZMid", "stzmid"),
        ("stretchXEnd", "stxend"),
        ("stretchZEnd", "stzend"),
    )

    STATE = STATEEnumField()
    STA = STATE

    curLen = DoubleField()
    clen = curLen

    pctSquash = DoubleField()
    psq = pctSquash

    pctStretch = DoubleField()
    pst = pctStretch

    soften = DoubleField()
    sft = soften

    biasX = DoubleField()
    bix = biasX

    biasZ = DoubleField()
    biz = biasZ

    biasTolernace = DoubleField()
    btol = biasTolernace

    manualSqSt = DoubleField()
    msqst = manualSqSt

    userScale = DoubleField()
    usc = userScale

    SHAPING = SHAPINGEnumField()
    SHA = SHAPING

    enableShaping = BoolField()
    eshp = enableShaping

    shapingBlend = DoubleField()
    shbl = shapingBlend

    SQUASH = SQUASHEnumField()
    SQA = SQUASH

    squashXStart = DoubleField()
    sqxsta = squashXStart

    squashZStart = DoubleField()
    sqzsta = squashZStart

    squashXMid = DoubleField()
    sqxmid = squashXMid

    squashZMid = DoubleField()
    sqzmid = squashZMid

    squashXEnd = DoubleField()
    sqxend = squashXEnd

    squashZEnd = DoubleField()
    sqzend = squashZEnd

    STRETCH = STRETCHEnumField()
    STE = STRETCH

    stretchXStart = DoubleField()
    stxsta = stretchXStart

    stretchZStart = DoubleField()
    stzsta = stretchZStart

    stretchXMid = DoubleField()
    stxmid = stretchXMid

    stretchZMid = DoubleField()
    stzmid = stretchZMid

    stretchXEnd = DoubleField()
    stxend = stretchXEnd

    stretchZEnd = DoubleField()
    stzend = stretchZEnd


class SquashDataAttrOperator(
    CompoundAttrOperator[SquashDataPlugOperator]
):
    __slots__ = ()

    STATE = STATEEnumField()
    STA = STATE

    curLen = DoubleField()
    clen = curLen

    pctSquash = DoubleField()
    psq = pctSquash

    pctStretch = DoubleField()
    pst = pctStretch

    soften = DoubleField()
    sft = soften

    biasX = DoubleField()
    bix = biasX

    biasZ = DoubleField()
    biz = biasZ

    biasTolernace = DoubleField()
    btol = biasTolernace

    manualSqSt = DoubleField()
    msqst = manualSqSt

    userScale = DoubleField()
    usc = userScale

    SHAPING = SHAPINGEnumField()
    SHA = SHAPING

    enableShaping = BoolField()
    eshp = enableShaping

    shapingBlend = DoubleField()
    shbl = shapingBlend

    SQUASH = SQUASHEnumField()
    SQA = SQUASH

    squashXStart = DoubleField()
    sqxsta = squashXStart

    squashZStart = DoubleField()
    sqzsta = squashZStart

    squashXMid = DoubleField()
    sqxmid = squashXMid

    squashZMid = DoubleField()
    sqzmid = squashZMid

    squashXEnd = DoubleField()
    sqxend = squashXEnd

    squashZEnd = DoubleField()
    sqzend = squashZEnd

    STRETCH = STRETCHEnumField()
    STE = STRETCH

    stretchXStart = DoubleField()
    stxsta = stretchXStart

    stretchZStart = DoubleField()
    stzsta = stretchZStart

    stretchXMid = DoubleField()
    stxmid = stretchXMid

    stretchZMid = DoubleField()
    stzmid = stretchZMid

    stretchXEnd = DoubleField()
    stxend = stretchXEnd

    stretchZEnd = DoubleField()
    stzend = stretchZEnd


class SquashDataField(
    CompoundField[SquashDataAttrOperator, SquashDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SquashDataAttrOperator
    PLUG_CLS = SquashDataPlugOperator

    STATE = STATEEnumField()
    STA = STATE

    curLen = DoubleField()
    clen = curLen

    pctSquash = DoubleField()
    psq = pctSquash

    pctStretch = DoubleField()
    pst = pctStretch

    soften = DoubleField()
    sft = soften

    biasX = DoubleField()
    bix = biasX

    biasZ = DoubleField()
    biz = biasZ

    biasTolernace = DoubleField()
    btol = biasTolernace

    manualSqSt = DoubleField()
    msqst = manualSqSt

    userScale = DoubleField()
    usc = userScale

    SHAPING = SHAPINGEnumField()
    SHA = SHAPING

    enableShaping = BoolField()
    eshp = enableShaping

    shapingBlend = DoubleField()
    shbl = shapingBlend

    SQUASH = SQUASHEnumField()
    SQA = SQUASH

    squashXStart = DoubleField()
    sqxsta = squashXStart

    squashZStart = DoubleField()
    sqzsta = squashZStart

    squashXMid = DoubleField()
    sqxmid = squashXMid

    squashZMid = DoubleField()
    sqzmid = squashZMid

    squashXEnd = DoubleField()
    sqxend = squashXEnd

    squashZEnd = DoubleField()
    sqzend = squashZEnd

    STRETCH = STRETCHEnumField()
    STE = STRETCH

    stretchXStart = DoubleField()
    stxsta = stretchXStart

    stretchZStart = DoubleField()
    stzsta = stretchZStart

    stretchXMid = DoubleField()
    stxmid = stretchXMid

    stretchZMid = DoubleField()
    stzmid = stretchZMid

    stretchXEnd = DoubleField()
    stxend = stretchXEnd

    stretchZEnd = DoubleField()
    stzend = stretchZEnd


class ShapeDataPlugOperator(
    CompoundPlugOperator["ShapeDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shapeName", "snm"),
        ("shapeLength", "slen"),
        ("shapeActive", "sact"),
        ("shapeManualTrigger", "strg"),
        ("shapeDelta", "sdlt"),
    )

    shapeName = DataStringField()
    snm = shapeName

    shapeLength = DoubleField()
    slen = shapeLength

    shapeActive = BoolField()
    sact = shapeActive

    shapeManualTrigger = DoubleField()
    strg = shapeManualTrigger

    shapeDelta = CompoundField()
    sdlt = shapeDelta


class ShapeDataAttrOperator(
    CompoundAttrOperator[ShapeDataPlugOperator]
):
    __slots__ = ()

    shapeName = DataStringField()
    snm = shapeName

    shapeLength = DoubleField()
    slen = shapeLength

    shapeActive = BoolField()
    sact = shapeActive

    shapeManualTrigger = DoubleField()
    strg = shapeManualTrigger

    shapeDelta = CompoundField()
    sdlt = shapeDelta


class ShapeDataField(
    CompoundField[ShapeDataAttrOperator, ShapeDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShapeDataAttrOperator
    PLUG_CLS = ShapeDataPlugOperator
