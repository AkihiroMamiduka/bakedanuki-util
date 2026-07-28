# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.unit.time import TimeField
from ..std.at.typed import TypedField
from ..std.dt.matrix import DataMatrixField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import (
    Float3Field,
)


class ClipTypeEnumPlugOperator(EnumPlugOperator["ClipTypeEnumAttrOperator"]):
    __slots__ = ()

    ANIMATION = 0
    AUDIO = 1


class ClipTypeEnumAttrOperator(EnumAttrOperator[ClipTypeEnumPlugOperator]):
    __slots__ = ()

    ANIMATION = 0
    AUDIO = 1

    NAME_MAP = {
        ANIMATION: "Animation",
        AUDIO: "Audio",
    }


class ClipTypeEnumField(
    EnumField[ClipTypeEnumAttrOperator, ClipTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClipTypeEnumAttrOperator
    PLUG_CLS = ClipTypeEnumPlugOperator


class TimeWarpTypeEnumPlugOperator(
    EnumPlugOperator["TimeWarpTypeEnumAttrOperator"]
):
    __slots__ = ()

    TIME_WARP = 0
    SPEED_CURVE = 1


class TimeWarpTypeEnumAttrOperator(
    EnumAttrOperator[TimeWarpTypeEnumPlugOperator]
):
    __slots__ = ()

    TIME_WARP = 0
    SPEED_CURVE = 1

    NAME_MAP = {
        TIME_WARP: "Time Warp",
        SPEED_CURVE: "Speed Curve",
    }


class TimeWarpTypeEnumField(
    EnumField[TimeWarpTypeEnumAttrOperator, TimeWarpTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TimeWarpTypeEnumAttrOperator
    PLUG_CLS = TimeWarpTypeEnumPlugOperator


class ClipLoopBeforeModeEnumPlugOperator(
    EnumPlugOperator["ClipLoopBeforeModeEnumAttrOperator"]
):
    __slots__ = ()

    LOOP = 0
    LOOP_PROGRESSIVE = 1
    HOLD = 2


class ClipLoopBeforeModeEnumAttrOperator(
    EnumAttrOperator[ClipLoopBeforeModeEnumPlugOperator]
):
    __slots__ = ()

    LOOP = 0
    LOOP_PROGRESSIVE = 1
    HOLD = 2

    NAME_MAP = {
        LOOP: "Loop",
        LOOP_PROGRESSIVE: "Loop Progressive",
        HOLD: "Hold",
    }


class ClipLoopBeforeModeEnumField(
    EnumField[
        ClipLoopBeforeModeEnumAttrOperator, ClipLoopBeforeModeEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ClipLoopBeforeModeEnumAttrOperator
    PLUG_CLS = ClipLoopBeforeModeEnumPlugOperator


class ClipLoopAfterModeEnumPlugOperator(
    EnumPlugOperator["ClipLoopAfterModeEnumAttrOperator"]
):
    __slots__ = ()

    LOOP = 0
    LOOP_PROGRESSIVE = 1
    HOLD = 2


class ClipLoopAfterModeEnumAttrOperator(
    EnumAttrOperator[ClipLoopAfterModeEnumPlugOperator]
):
    __slots__ = ()

    LOOP = 0
    LOOP_PROGRESSIVE = 1
    HOLD = 2

    NAME_MAP = {
        LOOP: "Loop",
        LOOP_PROGRESSIVE: "Loop Progressive",
        HOLD: "Hold",
    }


class ClipLoopAfterModeEnumField(
    EnumField[
        ClipLoopAfterModeEnumAttrOperator, ClipLoopAfterModeEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ClipLoopAfterModeEnumAttrOperator
    PLUG_CLS = ClipLoopAfterModeEnumPlugOperator


class ClipBlendModeEnumPlugOperator(
    EnumPlugOperator["ClipBlendModeEnumAttrOperator"]
):
    __slots__ = ()

    NORMAL = 0
    ADDITIVE = 1


class ClipBlendModeEnumAttrOperator(
    EnumAttrOperator[ClipBlendModeEnumPlugOperator]
):
    __slots__ = ()

    NORMAL = 0
    ADDITIVE = 1

    NAME_MAP = {
        NORMAL: "Normal",
        ADDITIVE: "Additive",
    }


class ClipBlendModeEnumField(
    EnumField[ClipBlendModeEnumAttrOperator, ClipBlendModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClipBlendModeEnumAttrOperator
    PLUG_CLS = ClipBlendModeEnumPlugOperator


class LayerModeEnumPlugOperator(EnumPlugOperator["LayerModeEnumAttrOperator"]):
    __slots__ = ()

    ADDITIVE = 0
    ADDITIVE_OVERRIDE = 1
    OVERRIDE = 2
    OVERRIDE_PASS_MINUS_THROUGH = 3


class LayerModeEnumAttrOperator(EnumAttrOperator[LayerModeEnumPlugOperator]):
    __slots__ = ()

    ADDITIVE = 0
    ADDITIVE_OVERRIDE = 1
    OVERRIDE = 2
    OVERRIDE_PASS_MINUS_THROUGH = 3

    NAME_MAP = {
        ADDITIVE: "Additive",
        ADDITIVE_OVERRIDE: "Additive Override",
        OVERRIDE: "Override",
        OVERRIDE_PASS_MINUS_THROUGH: "Override Pass-through",
    }


class LayerModeEnumField(
    EnumField[LayerModeEnumAttrOperator, LayerModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LayerModeEnumAttrOperator
    PLUG_CLS = LayerModeEnumPlugOperator


class ClipPlugOperator(CompoundPlugOperator["ClipAttrOperator"]):
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

    clipid = LongField(default_value=0, min_value=0)
    cid = clipid

    clipName = DataStringField()
    cn = clipName

    clipType = ClipTypeEnumField(default_value=0)
    ct = clipType

    clipStart = TimeField(default_value=0.0)
    cst = clipStart

    clipDuration = TimeField(default_value=0.0, min_value=0.01)
    cpd = clipDuration

    clipScale = DoubleField(default_value=0.0, min_value=0.01)
    cscl = clipScale

    speedInput = DoubleField(default_value=0.0)
    sin = speedInput

    timeWarped = BoolField(default_value=False)
    tw = timeWarped

    timeWarpType = TimeWarpTypeEnumField(default_value=1)
    twt = timeWarpType

    clipLoopAfter = DoubleField(default_value=0.0, min_value=0.0)
    cla = clipLoopAfter

    clipLoopBefore = DoubleField(default_value=0.0, min_value=0.0)
    clb = clipLoopBefore

    clipLoopBeforeMode = ClipLoopBeforeModeEnumField(default_value=0)
    clbm = clipLoopBeforeMode

    clipLoopAfterMode = ClipLoopAfterModeEnumField(default_value=0)
    clam = clipLoopAfterMode

    clipHoldBefore = TimeField(default_value=0.0, min_value=0.0)
    chb = clipHoldBefore

    clipHoldAfter = TimeField(default_value=0.0, min_value=0.0)
    cha = clipHoldAfter

    clipBlendMode = ClipBlendModeEnumField(default_value=0)
    cbm = clipBlendMode

    clipMuted = BoolField(default_value=False)
    cm = clipMuted

    clipEvaluationData = TypedField(writable=False)
    ced = clipEvaluationData

    clipParent = TypedField(readable=False)
    cprn = clipParent

    useClipColor = BoolField(default_value=False)
    ucc = useClipColor

    clipColor = Float3Field(
        default_value=(
            0.5839999914169312,
            0.4350000023841858,
            0.09799999743700027,
        ),
        min_value=(0.0, 0.0, 0.0),
    )
    cc = clipColor

    curveStart = TimeField(default_value=0.0)
    cvst = curveStart

    localTime = TimeField(default_value=0.0)
    clt = localTime

    parentTime = TimeField(default_value=0.0)
    cpt = parentTime


class ClipAttrOperator(CompoundAttrOperator[ClipPlugOperator]):
    __slots__ = ()

    clipid = LongField(default_value=0, min_value=0)
    cid = clipid

    clipName = DataStringField()
    cn = clipName

    clipType = ClipTypeEnumField(default_value=0)
    ct = clipType

    clipStart = TimeField(default_value=0.0)
    cst = clipStart

    clipDuration = TimeField(default_value=0.0, min_value=0.01)
    cpd = clipDuration

    clipScale = DoubleField(default_value=0.0, min_value=0.01)
    cscl = clipScale

    speedInput = DoubleField(default_value=0.0)
    sin = speedInput

    timeWarped = BoolField(default_value=False)
    tw = timeWarped

    timeWarpType = TimeWarpTypeEnumField(default_value=1)
    twt = timeWarpType

    clipLoopAfter = DoubleField(default_value=0.0, min_value=0.0)
    cla = clipLoopAfter

    clipLoopBefore = DoubleField(default_value=0.0, min_value=0.0)
    clb = clipLoopBefore

    clipLoopBeforeMode = ClipLoopBeforeModeEnumField(default_value=0)
    clbm = clipLoopBeforeMode

    clipLoopAfterMode = ClipLoopAfterModeEnumField(default_value=0)
    clam = clipLoopAfterMode

    clipHoldBefore = TimeField(default_value=0.0, min_value=0.0)
    chb = clipHoldBefore

    clipHoldAfter = TimeField(default_value=0.0, min_value=0.0)
    cha = clipHoldAfter

    clipBlendMode = ClipBlendModeEnumField(default_value=0)
    cbm = clipBlendMode

    clipMuted = BoolField(default_value=False)
    cm = clipMuted

    clipEvaluationData = TypedField(writable=False)
    ced = clipEvaluationData

    clipParent = TypedField(readable=False)
    cprn = clipParent

    useClipColor = BoolField(default_value=False)
    ucc = useClipColor

    clipColor = Float3Field(
        default_value=(
            0.5839999914169312,
            0.4350000023841858,
            0.09799999743700027,
        ),
        min_value=(0.0, 0.0, 0.0),
    )
    cc = clipColor

    curveStart = TimeField(default_value=0.0)
    cvst = curveStart

    localTime = TimeField(default_value=0.0)
    clt = localTime

    parentTime = TimeField(default_value=0.0)
    cpt = parentTime


class ClipField(CompoundField[ClipAttrOperator, ClipPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ClipAttrOperator
    PLUG_CLS = ClipPlugOperator


class OffsetPlugOperator(CompoundPlugOperator["OffsetAttrOperator"]):
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

    offsetMode = LongField(default_value=0)
    ofm = offsetMode

    offsetMtx = DataMatrixField()
    omt = offsetMtx

    pivotMtx = DataMatrixField()
    pmt = pivotMtx

    matchclip = LongField(default_value=-1)
    mcl = matchclip

    matchTime = TimeField(default_value=0.0)
    mtm = matchTime

    roots = CompoundField(multi=True)
    rts = roots

    matchObj = MessageField()
    mob = matchObj


class OffsetAttrOperator(CompoundAttrOperator[OffsetPlugOperator]):
    __slots__ = ()

    offsetMode = LongField(default_value=0)
    ofm = offsetMode

    offsetMtx = DataMatrixField()
    omt = offsetMtx

    pivotMtx = DataMatrixField()
    pmt = pivotMtx

    matchclip = LongField(default_value=-1)
    mcl = matchclip

    matchTime = TimeField(default_value=0.0)
    mtm = matchTime

    roots = CompoundField(multi=True)
    rts = roots

    matchObj = MessageField()
    mob = matchObj


class OffsetField(CompoundField[OffsetAttrOperator, OffsetPlugOperator]):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetMode = LongField(default_value=0)
    ofm = offsetMode

    offsetMtx = DataMatrixField()
    omt = offsetMtx

    pivotMtx = DataMatrixField()
    pmt = pivotMtx

    matchclip = LongField(default_value=-1)
    mcl = matchclip

    matchTime = TimeField(default_value=0.0)
    mtm = matchTime

    roots = CompoundField(multi=True)
    rts = roots

    matchObj = MessageField()
    mob = matchObj


class LayerPlugOperator(CompoundPlugOperator["LayerAttrOperator"]):
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

    layerIndex = LongField(default_value=0)
    li = layerIndex

    layerId = LongField(default_value=-1)
    lid = layerId

    layerWeight = DoubleField(default_value=1.0)
    lw = layerWeight

    layerMode = LayerModeEnumField(default_value=0)
    lm = layerMode

    layerMuted = BoolField(default_value=False)
    lmd = layerMuted

    layerSolo = BoolField(default_value=False)
    lsl = layerSolo


class LayerAttrOperator(CompoundAttrOperator[LayerPlugOperator]):
    __slots__ = ()

    layerName = DataStringField()
    ln = layerName

    layerIndex = LongField(default_value=0)
    li = layerIndex

    layerId = LongField(default_value=-1)
    lid = layerId

    layerWeight = DoubleField(default_value=1.0)
    lw = layerWeight

    layerMode = LayerModeEnumField(default_value=0)
    lm = layerMode

    layerMuted = BoolField(default_value=False)
    lmd = layerMuted

    layerSolo = BoolField(default_value=False)
    lsl = layerSolo


class LayerField(CompoundField[LayerAttrOperator, LayerPlugOperator]):
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

    ghostColorR = FloatField(default_value=0.0)
    gcr = ghostColorR

    ghostColorG = FloatField(default_value=0.0)
    gcg = ghostColorG

    ghostColorB = FloatField(default_value=0.0)
    gcb = ghostColorB


class GhostColorAttrOperator(
    Float3CompoundBaseAttrOperator[GhostColorPlugOperator]
):
    __slots__ = ()

    ghostColorR = FloatField(default_value=0.0)
    gcr = ghostColorR

    ghostColorG = FloatField(default_value=0.0)
    gcg = ghostColorG

    ghostColorB = FloatField(default_value=0.0)
    gcb = ghostColorB


class GhostColorField(
    Float3CompoundBaseField[GhostColorAttrOperator, GhostColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GhostColorAttrOperator
    PLUG_CLS = GhostColorPlugOperator

    ghostColorR = FloatField(default_value=0.0)
    gcr = ghostColorR

    ghostColorG = FloatField(default_value=0.0)
    gcg = ghostColorG

    ghostColorB = FloatField(default_value=0.0)
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

    ghostPostColorR = FloatField(default_value=0.0)
    gtr = ghostPostColorR

    ghostPostColorG = FloatField(default_value=0.0)
    gtg = ghostPostColorG

    ghostPostColorB = FloatField(default_value=0.0)
    gtb = ghostPostColorB


class GhostPostColorAttrOperator(
    Float3CompoundBaseAttrOperator[GhostPostColorPlugOperator]
):
    __slots__ = ()

    ghostPostColorR = FloatField(default_value=0.0)
    gtr = ghostPostColorR

    ghostPostColorG = FloatField(default_value=0.0)
    gtg = ghostPostColorG

    ghostPostColorB = FloatField(default_value=0.0)
    gtb = ghostPostColorB


class GhostPostColorField(
    Float3CompoundBaseField[
        GhostPostColorAttrOperator, GhostPostColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = GhostPostColorAttrOperator
    PLUG_CLS = GhostPostColorPlugOperator

    ghostPostColorR = FloatField(default_value=0.0)
    gtr = ghostPostColorR

    ghostPostColorG = FloatField(default_value=0.0)
    gtg = ghostPostColorG

    ghostPostColorB = FloatField(default_value=0.0)
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

    ghostPreColorR = FloatField(default_value=0.0)
    ger = ghostPreColorR

    ghostPreColorG = FloatField(default_value=0.0)
    geg = ghostPreColorG

    ghostPreColorB = FloatField(default_value=0.0)
    geb = ghostPreColorB


class GhostPreColorAttrOperator(
    Float3CompoundBaseAttrOperator[GhostPreColorPlugOperator]
):
    __slots__ = ()

    ghostPreColorR = FloatField(default_value=0.0)
    ger = ghostPreColorR

    ghostPreColorG = FloatField(default_value=0.0)
    geg = ghostPreColorG

    ghostPreColorB = FloatField(default_value=0.0)
    geb = ghostPreColorB


class GhostPreColorField(
    Float3CompoundBaseField[
        GhostPreColorAttrOperator, GhostPreColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = GhostPreColorAttrOperator
    PLUG_CLS = GhostPreColorPlugOperator

    ghostPreColorR = FloatField(default_value=0.0)
    ger = ghostPreColorR

    ghostPreColorG = FloatField(default_value=0.0)
    geg = ghostPreColorG

    ghostPreColorB = FloatField(default_value=0.0)
    geb = ghostPreColorB
