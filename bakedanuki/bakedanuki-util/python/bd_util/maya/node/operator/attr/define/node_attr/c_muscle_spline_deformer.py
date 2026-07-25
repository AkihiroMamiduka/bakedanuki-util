# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
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

    groupId = LongField(default_value=0)
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputAttrOperator(
    CompoundAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField(default_value=0)
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

    envelopeWeights = FloatField(multi=True, default_value=1.0, writable=False)
    owt = envelopeWeights


class EnvelopeWeightsListAttrOperator(
    CompoundAttrOperator[EnvelopeWeightsListPlugOperator]
):
    __slots__ = ()

    envelopeWeights = FloatField(multi=True, default_value=1.0, writable=False)
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

    fchild1 = LongField(default_value=0, readable=False)
    f1 = fchild1

    fchild2 = LongField(default_value=0, readable=False)
    f2 = fchild2

    fchild3 = LongField(default_value=0, readable=False)
    f3 = fchild3


class FunctionAttrOperator(
    Long3CompoundBaseAttrOperator[FunctionPlugOperator]
):
    __slots__ = ()

    fchild1 = LongField(default_value=0, readable=False)
    f1 = fchild1

    fchild2 = LongField(default_value=0, readable=False)
    f2 = fchild2

    fchild3 = LongField(default_value=0, readable=False)
    f3 = fchild3


class FunctionField(
    Long3CompoundBaseField[FunctionAttrOperator, FunctionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FunctionAttrOperator
    PLUG_CLS = FunctionPlugOperator

    fchild1 = LongField(default_value=0, readable=False)
    f1 = fchild1

    fchild2 = LongField(default_value=0, readable=False)
    f2 = fchild2

    fchild3 = LongField(default_value=0, readable=False)
    f3 = fchild3


class WeightListPlugOperator(
    CompoundPlugOperator["WeightListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weights", "wl.w"),
    )

    weights = FloatField(multi=True, default_value=1.0)


class WeightListAttrOperator(
    CompoundAttrOperator[WeightListPlugOperator]
):
    __slots__ = ()

    weights = FloatField(multi=True, default_value=1.0)


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

    point = CompoundField(default_value=(0.0, 0.0, 0.0))
    pt = point

    pointJiggle = CompoundField(default_value=(0.0, 0.0, 0.0))
    pj = pointJiggle

    tangent = CompoundField(default_value=(0.0, 0.0, 0.0))
    tg = tangent

    up = CompoundField(default_value=(0.0, 0.0, 0.0))
    u = up


class ControlDataAttrOperator(
    CompoundAttrOperator[ControlDataPlugOperator]
):
    __slots__ = ()

    point = CompoundField(default_value=(0.0, 0.0, 0.0))
    pt = point

    pointJiggle = CompoundField(default_value=(0.0, 0.0, 0.0))
    pj = pointJiggle

    tangent = CompoundField(default_value=(0.0, 0.0, 0.0))
    tg = tangent

    up = CompoundField(default_value=(0.0, 0.0, 0.0))
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

    pointBase = CompoundField(default_value=(0.0, 0.0, 0.0))
    ptb = pointBase

    pointJiggleBase = CompoundField(default_value=(0.0, 0.0, 0.0))
    pjb = pointJiggleBase

    tangentBase = CompoundField(default_value=(0.0, 0.0, 0.0))
    tgb = tangentBase

    upBase = CompoundField(default_value=(0.0, 0.0, 0.0))
    ub = upBase


class ControlDataBaseAttrOperator(
    CompoundAttrOperator[ControlDataBasePlugOperator]
):
    __slots__ = ()

    pointBase = CompoundField(default_value=(0.0, 0.0, 0.0))
    ptb = pointBase

    pointJiggleBase = CompoundField(default_value=(0.0, 0.0, 0.0))
    pjb = pointJiggleBase

    tangentBase = CompoundField(default_value=(0.0, 0.0, 0.0))
    tgb = tangentBase

    upBase = CompoundField(default_value=(0.0, 0.0, 0.0))
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

    STATE = STATEEnumField(default_value=0)
    STA = STATE

    curLen = DoubleField(default_value=1.0, min_value=0.0001)
    clen = curLen

    pctSquash = DoubleField(default_value=0.0)
    psq = pctSquash

    pctStretch = DoubleField(default_value=0.0)
    pst = pctStretch

    soften = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    sft = soften

    biasX = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bix = biasX

    biasZ = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    biz = biasZ

    biasTolernace = DoubleField(default_value=1e-05, min_value=0.0)
    btol = biasTolernace

    manualSqSt = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    msqst = manualSqSt

    userScale = DoubleField(default_value=1.0)
    usc = userScale

    SHAPING = SHAPINGEnumField(default_value=0)
    SHA = SHAPING

    enableShaping = BoolField(default_value=False)
    eshp = enableShaping

    shapingBlend = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)
    shbl = shapingBlend

    SQUASH = SQUASHEnumField(default_value=0)
    SQA = SQUASH

    squashXStart = DoubleField(default_value=1.0)
    sqxsta = squashXStart

    squashZStart = DoubleField(default_value=1.0)
    sqzsta = squashZStart

    squashXMid = DoubleField(default_value=2.0)
    sqxmid = squashXMid

    squashZMid = DoubleField(default_value=2.0)
    sqzmid = squashZMid

    squashXEnd = DoubleField(default_value=1.0)
    sqxend = squashXEnd

    squashZEnd = DoubleField(default_value=1.0)
    sqzend = squashZEnd

    STRETCH = STRETCHEnumField(default_value=0)
    STE = STRETCH

    stretchXStart = DoubleField(default_value=1.0)
    stxsta = stretchXStart

    stretchZStart = DoubleField(default_value=1.0)
    stzsta = stretchZStart

    stretchXMid = DoubleField(default_value=0.5)
    stxmid = stretchXMid

    stretchZMid = DoubleField(default_value=0.5)
    stzmid = stretchZMid

    stretchXEnd = DoubleField(default_value=1.0)
    stxend = stretchXEnd

    stretchZEnd = DoubleField(default_value=1.0)
    stzend = stretchZEnd


class SquashDataAttrOperator(
    CompoundAttrOperator[SquashDataPlugOperator]
):
    __slots__ = ()

    STATE = STATEEnumField(default_value=0)
    STA = STATE

    curLen = DoubleField(default_value=1.0, min_value=0.0001)
    clen = curLen

    pctSquash = DoubleField(default_value=0.0)
    psq = pctSquash

    pctStretch = DoubleField(default_value=0.0)
    pst = pctStretch

    soften = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    sft = soften

    biasX = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bix = biasX

    biasZ = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    biz = biasZ

    biasTolernace = DoubleField(default_value=1e-05, min_value=0.0)
    btol = biasTolernace

    manualSqSt = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    msqst = manualSqSt

    userScale = DoubleField(default_value=1.0)
    usc = userScale

    SHAPING = SHAPINGEnumField(default_value=0)
    SHA = SHAPING

    enableShaping = BoolField(default_value=False)
    eshp = enableShaping

    shapingBlend = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)
    shbl = shapingBlend

    SQUASH = SQUASHEnumField(default_value=0)
    SQA = SQUASH

    squashXStart = DoubleField(default_value=1.0)
    sqxsta = squashXStart

    squashZStart = DoubleField(default_value=1.0)
    sqzsta = squashZStart

    squashXMid = DoubleField(default_value=2.0)
    sqxmid = squashXMid

    squashZMid = DoubleField(default_value=2.0)
    sqzmid = squashZMid

    squashXEnd = DoubleField(default_value=1.0)
    sqxend = squashXEnd

    squashZEnd = DoubleField(default_value=1.0)
    sqzend = squashZEnd

    STRETCH = STRETCHEnumField(default_value=0)
    STE = STRETCH

    stretchXStart = DoubleField(default_value=1.0)
    stxsta = stretchXStart

    stretchZStart = DoubleField(default_value=1.0)
    stzsta = stretchZStart

    stretchXMid = DoubleField(default_value=0.5)
    stxmid = stretchXMid

    stretchZMid = DoubleField(default_value=0.5)
    stzmid = stretchZMid

    stretchXEnd = DoubleField(default_value=1.0)
    stxend = stretchXEnd

    stretchZEnd = DoubleField(default_value=1.0)
    stzend = stretchZEnd


class SquashDataField(
    CompoundField[SquashDataAttrOperator, SquashDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SquashDataAttrOperator
    PLUG_CLS = SquashDataPlugOperator

    STATE = STATEEnumField(default_value=0)
    STA = STATE

    curLen = DoubleField(default_value=1.0, min_value=0.0001)
    clen = curLen

    pctSquash = DoubleField(default_value=0.0)
    psq = pctSquash

    pctStretch = DoubleField(default_value=0.0)
    pst = pctStretch

    soften = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    sft = soften

    biasX = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bix = biasX

    biasZ = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    biz = biasZ

    biasTolernace = DoubleField(default_value=1e-05, min_value=0.0)
    btol = biasTolernace

    manualSqSt = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    msqst = manualSqSt

    userScale = DoubleField(default_value=1.0)
    usc = userScale

    SHAPING = SHAPINGEnumField(default_value=0)
    SHA = SHAPING

    enableShaping = BoolField(default_value=False)
    eshp = enableShaping

    shapingBlend = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)
    shbl = shapingBlend

    SQUASH = SQUASHEnumField(default_value=0)
    SQA = SQUASH

    squashXStart = DoubleField(default_value=1.0)
    sqxsta = squashXStart

    squashZStart = DoubleField(default_value=1.0)
    sqzsta = squashZStart

    squashXMid = DoubleField(default_value=2.0)
    sqxmid = squashXMid

    squashZMid = DoubleField(default_value=2.0)
    sqzmid = squashZMid

    squashXEnd = DoubleField(default_value=1.0)
    sqxend = squashXEnd

    squashZEnd = DoubleField(default_value=1.0)
    sqzend = squashZEnd

    STRETCH = STRETCHEnumField(default_value=0)
    STE = STRETCH

    stretchXStart = DoubleField(default_value=1.0)
    stxsta = stretchXStart

    stretchZStart = DoubleField(default_value=1.0)
    stzsta = stretchZStart

    stretchXMid = DoubleField(default_value=0.5)
    stxmid = stretchXMid

    stretchZMid = DoubleField(default_value=0.5)
    stzmid = stretchZMid

    stretchXEnd = DoubleField(default_value=1.0)
    stxend = stretchXEnd

    stretchZEnd = DoubleField(default_value=1.0)
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

    shapeLength = DoubleField(default_value=0.0)
    slen = shapeLength

    shapeActive = BoolField(default_value=False)
    sact = shapeActive

    shapeManualTrigger = DoubleField(default_value=0.0, min_value=0.0, max_value=0.0)
    strg = shapeManualTrigger

    shapeDelta = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    sdlt = shapeDelta


class ShapeDataAttrOperator(
    CompoundAttrOperator[ShapeDataPlugOperator]
):
    __slots__ = ()

    shapeName = DataStringField()
    snm = shapeName

    shapeLength = DoubleField(default_value=0.0)
    slen = shapeLength

    shapeActive = BoolField(default_value=False)
    sact = shapeActive

    shapeManualTrigger = DoubleField(default_value=0.0, min_value=0.0, max_value=0.0)
    strg = shapeManualTrigger

    shapeDelta = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    sdlt = shapeDelta


class ShapeDataField(
    CompoundField[ShapeDataAttrOperator, ShapeDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShapeDataAttrOperator
    PLUG_CLS = ShapeDataPlugOperator
