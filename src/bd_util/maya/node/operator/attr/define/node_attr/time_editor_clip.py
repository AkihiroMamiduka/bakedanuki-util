# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.message import MessageField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField
from ..std.at.unit_scalar.time import TimeField
from ..std.dt.matrix import DataMatrixField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class ClipPlugOperator(
    CompoundPlugOperator["ClipAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("clipid", "cid"),
        ("clipName", "cn"),
        ("clipType", "ct"),
        ("clipStart", "cst"),
        ("clipDuration", "cpd"),
        ("clipScale", "cscl"),
        ("speedInput", "sin"),
        ("timeWarped", "tw"),
        ("timeWarpType", "twt"),
        ("clipLoopAfter", "cla"),
        ("clipLoopBefore", "clb"),
        ("clipLoopBeforeMode", "clbm"),
        ("clipLoopAfterMode", "clam"),
        ("clipHoldBefore", "chb"),
        ("clipHoldAfter", "cha"),
        ("clipBlendMode", "cbm"),
        ("clipMuted", "cm"),
        ("clipEvaluationData", "ced"),
        ("clipParent", "cprn"),
        ("useClipColor", "ucc"),
        ("clipColor", "cc"),
        ("curveStart", "cvst"),
        ("localTime", "clt"),
        ("parentTime", "cpt"),
    )

    clipid = LongField()
    cid = clipid

    clipName = DataStringField()
    cn = clipName

    clipType = EnumField()
    ct = clipType

    clipStart = TimeField()
    cst = clipStart

    clipDuration = TimeField()
    cpd = clipDuration

    clipScale = DoubleField()
    cscl = clipScale

    speedInput = DoubleField()
    sin = speedInput

    timeWarped = BoolField()
    tw = timeWarped

    timeWarpType = EnumField()
    twt = timeWarpType

    clipLoopAfter = DoubleField()
    cla = clipLoopAfter

    clipLoopBefore = DoubleField()
    clb = clipLoopBefore

    clipLoopBeforeMode = EnumField()
    clbm = clipLoopBeforeMode

    clipLoopAfterMode = EnumField()
    clam = clipLoopAfterMode

    clipHoldBefore = TimeField()
    chb = clipHoldBefore

    clipHoldAfter = TimeField()
    cha = clipHoldAfter

    clipBlendMode = EnumField()
    cbm = clipBlendMode

    clipMuted = BoolField()
    cm = clipMuted

    clipEvaluationData = TypedField()
    ced = clipEvaluationData

    clipParent = TypedField()
    cprn = clipParent

    useClipColor = BoolField()
    ucc = useClipColor

    clipColor = Float3Field()
    cc = clipColor

    curveStart = TimeField()
    cvst = curveStart

    localTime = TimeField()
    clt = localTime

    parentTime = TimeField()
    cpt = parentTime


class ClipAttrOperator(
    CompoundAttrOperator[ClipPlugOperator]
):
    __slots__ = ()

    clipid = LongField()
    cid = clipid

    clipName = DataStringField()
    cn = clipName

    clipType = EnumField()
    ct = clipType

    clipStart = TimeField()
    cst = clipStart

    clipDuration = TimeField()
    cpd = clipDuration

    clipScale = DoubleField()
    cscl = clipScale

    speedInput = DoubleField()
    sin = speedInput

    timeWarped = BoolField()
    tw = timeWarped

    timeWarpType = EnumField()
    twt = timeWarpType

    clipLoopAfter = DoubleField()
    cla = clipLoopAfter

    clipLoopBefore = DoubleField()
    clb = clipLoopBefore

    clipLoopBeforeMode = EnumField()
    clbm = clipLoopBeforeMode

    clipLoopAfterMode = EnumField()
    clam = clipLoopAfterMode

    clipHoldBefore = TimeField()
    chb = clipHoldBefore

    clipHoldAfter = TimeField()
    cha = clipHoldAfter

    clipBlendMode = EnumField()
    cbm = clipBlendMode

    clipMuted = BoolField()
    cm = clipMuted

    clipEvaluationData = TypedField()
    ced = clipEvaluationData

    clipParent = TypedField()
    cprn = clipParent

    useClipColor = BoolField()
    ucc = useClipColor

    clipColor = Float3Field()
    cc = clipColor

    curveStart = TimeField()
    cvst = curveStart

    localTime = TimeField()
    clt = localTime

    parentTime = TimeField()
    cpt = parentTime


class ClipField(
    CompoundField[ClipAttrOperator, ClipPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClipAttrOperator
    PLUG_CLS = ClipPlugOperator


class OffsetPlugOperator(
    CompoundPlugOperator["OffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetMode", "ofm"),
        ("offsetMtx", "omt"),
        ("pivotMtx", "pmt"),
        ("matchclip", "mcl"),
        ("matchTime", "mtm"),
        ("roots", "rts"),
        ("matchObj", "mob"),
    )

    offsetMode = LongField()
    ofm = offsetMode

    offsetMtx = DataMatrixField()
    omt = offsetMtx

    pivotMtx = DataMatrixField()
    pmt = pivotMtx

    matchclip = LongField()
    mcl = matchclip

    matchTime = TimeField()
    mtm = matchTime

    roots = CompoundField()
    rts = roots

    matchObj = MessageField()
    mob = matchObj


class OffsetAttrOperator(
    CompoundAttrOperator[OffsetPlugOperator]
):
    __slots__ = ()

    offsetMode = LongField()
    ofm = offsetMode

    offsetMtx = DataMatrixField()
    omt = offsetMtx

    pivotMtx = DataMatrixField()
    pmt = pivotMtx

    matchclip = LongField()
    mcl = matchclip

    matchTime = TimeField()
    mtm = matchTime

    roots = CompoundField()
    rts = roots

    matchObj = MessageField()
    mob = matchObj


class OffsetField(
    CompoundField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetMode = LongField()
    ofm = offsetMode

    offsetMtx = DataMatrixField()
    omt = offsetMtx

    pivotMtx = DataMatrixField()
    pmt = pivotMtx

    matchclip = LongField()
    mcl = matchclip

    matchTime = TimeField()
    mtm = matchTime

    roots = CompoundField()
    rts = roots

    matchObj = MessageField()
    mob = matchObj


class LayerPlugOperator(
    CompoundPlugOperator["LayerAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("layerName", "ln"),
        ("layerIndex", "li"),
        ("layerId", "lid"),
        ("layerWeight", "lw"),
        ("layerMode", "lm"),
        ("layerMuted", "lmd"),
        ("layerSolo", "lsl"),
    )

    layerName = DataStringField()
    ln = layerName

    layerIndex = LongField()
    li = layerIndex

    layerId = LongField()
    lid = layerId

    layerWeight = DoubleField()
    lw = layerWeight

    layerMode = EnumField()
    lm = layerMode

    layerMuted = BoolField()
    lmd = layerMuted

    layerSolo = BoolField()
    lsl = layerSolo


class LayerAttrOperator(
    CompoundAttrOperator[LayerPlugOperator]
):
    __slots__ = ()

    layerName = DataStringField()
    ln = layerName

    layerIndex = LongField()
    li = layerIndex

    layerId = LongField()
    lid = layerId

    layerWeight = DoubleField()
    lw = layerWeight

    layerMode = EnumField()
    lm = layerMode

    layerMuted = BoolField()
    lmd = layerMuted

    layerSolo = BoolField()
    lsl = layerSolo


class LayerField(
    CompoundField[LayerAttrOperator, LayerPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LayerAttrOperator
    PLUG_CLS = LayerPlugOperator


class GhostColorPlugOperator(
    Float3CompoundBasePlugOperator["GhostColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ghostColorR", "gcr"),
        ("ghostColorG", "gcg"),
        ("ghostColorB", "gcb"),
    )

    ghostColorR = FloatField()
    gcr = ghostColorR

    ghostColorG = FloatField()
    gcg = ghostColorG

    ghostColorB = FloatField()
    gcb = ghostColorB


class GhostColorAttrOperator(
    Float3CompoundBaseAttrOperator[GhostColorPlugOperator]
):
    __slots__ = ()

    ghostColorR = FloatField()
    gcr = ghostColorR

    ghostColorG = FloatField()
    gcg = ghostColorG

    ghostColorB = FloatField()
    gcb = ghostColorB


class GhostColorField(
    Float3CompoundBaseField[GhostColorAttrOperator, GhostColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GhostColorAttrOperator
    PLUG_CLS = GhostColorPlugOperator

    ghostColorR = FloatField()
    gcr = ghostColorR

    ghostColorG = FloatField()
    gcg = ghostColorG

    ghostColorB = FloatField()
    gcb = ghostColorB


class GhostPostColorPlugOperator(
    Float3CompoundBasePlugOperator["GhostPostColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ghostPostColorR", "gtr"),
        ("ghostPostColorG", "gtg"),
        ("ghostPostColorB", "gtb"),
    )

    ghostPostColorR = FloatField()
    gtr = ghostPostColorR

    ghostPostColorG = FloatField()
    gtg = ghostPostColorG

    ghostPostColorB = FloatField()
    gtb = ghostPostColorB


class GhostPostColorAttrOperator(
    Float3CompoundBaseAttrOperator[GhostPostColorPlugOperator]
):
    __slots__ = ()

    ghostPostColorR = FloatField()
    gtr = ghostPostColorR

    ghostPostColorG = FloatField()
    gtg = ghostPostColorG

    ghostPostColorB = FloatField()
    gtb = ghostPostColorB


class GhostPostColorField(
    Float3CompoundBaseField[GhostPostColorAttrOperator, GhostPostColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GhostPostColorAttrOperator
    PLUG_CLS = GhostPostColorPlugOperator

    ghostPostColorR = FloatField()
    gtr = ghostPostColorR

    ghostPostColorG = FloatField()
    gtg = ghostPostColorG

    ghostPostColorB = FloatField()
    gtb = ghostPostColorB


class GhostPreColorPlugOperator(
    Float3CompoundBasePlugOperator["GhostPreColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ghostPreColorR", "ger"),
        ("ghostPreColorG", "geg"),
        ("ghostPreColorB", "geb"),
    )

    ghostPreColorR = FloatField()
    ger = ghostPreColorR

    ghostPreColorG = FloatField()
    geg = ghostPreColorG

    ghostPreColorB = FloatField()
    geb = ghostPreColorB


class GhostPreColorAttrOperator(
    Float3CompoundBaseAttrOperator[GhostPreColorPlugOperator]
):
    __slots__ = ()

    ghostPreColorR = FloatField()
    ger = ghostPreColorR

    ghostPreColorG = FloatField()
    geg = ghostPreColorG

    ghostPreColorB = FloatField()
    geb = ghostPreColorB


class GhostPreColorField(
    Float3CompoundBaseField[GhostPreColorAttrOperator, GhostPreColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GhostPreColorAttrOperator
    PLUG_CLS = GhostPreColorPlugOperator

    ghostPreColorR = FloatField()
    ger = ghostPreColorR

    ghostPreColorG = FloatField()
    geg = ghostPreColorG

    ghostPreColorB = FloatField()
    geb = ghostPreColorB
