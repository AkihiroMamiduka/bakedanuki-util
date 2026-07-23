# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.clip_scheduler import (
    BlendClipsField,
    BlendListField,
    ClipFunctionField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.unit_scalar.time import TimeField


class WeightStyleEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FROM_START = 0
    FROM_ZERO = 1
    ABSOLUTE_FROM_ZERO = 2


class WeightStyleEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FROM_START = 0
    FROM_ZERO = 1
    ABSOLUTE_FROM_ZERO = 2

    NAME_MAP = {
        FROM_START: "From Start",
        FROM_ZERO: "From Zero",
        ABSOLUTE_FROM_ZERO: "Absolute From Zero",
    }


class WeightStyleEnumField(
    EnumField[WeightStyleEnumAttrOperator, WeightStyleEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightStyleEnumAttrOperator
    PLUG_CLS = WeightStyleEnumPlugOperator


class _GeneratedClipScheduler(DG):
    __slots__ = ()

    NODE_TYPE = "clipScheduler"

    blendList = BlendListField(multi=True)
    bl = blendList

    blendClips = BlendClipsField(multi=True, default_value=(0.0, 0.0))
    bc = blendClips

    clipEvaluate = TypedField(writable=False)
    ce = clipEvaluate

    clipStatePercentEval = TypedField(writable=False)
    cspe = clipStatePercentEval

    clipFunction = ClipFunctionField()
    cf = clipFunction
    clipFunction_Hidden = clipFunction.clipFunction_Hidden
    cfh = clipFunction_Hidden
    clipFunction_Raw = clipFunction.clipFunction_Raw
    cfr = clipFunction_Raw
    clipFunction_Inmap = clipFunction.clipFunction_Inmap
    cfi = clipFunction_Inmap
    clipFunction_Outmap = clipFunction.clipFunction_Outmap
    cfo = clipFunction_Outmap

    clipFunction_InmapTo = ShortField()
    cfit = clipFunction_InmapTo

    clipFunction_InmapFrom = ShortField()
    cfif = clipFunction_InmapFrom

    clipFunction_OutmapTo = ShortField()
    cfot = clipFunction_OutmapTo

    clipFunction_OutmapFrom = ShortField()
    cfof = clipFunction_OutmapFrom

    clip = MessageField(multi=True)
    cl = clip

    start = TimeField(multi=True, default_value=0.0)
    st = start

    sourceStart = TimeField(multi=True, default_value=0.0)
    ss = sourceStart

    sourceEnd = TimeField(multi=True, default_value=0.0)
    se = sourceEnd

    scale = DoubleField(multi=True, default_value=1.0, min_value=0.0)
    sc = scale

    hold = TimeField(multi=True, default_value=0.0)
    h = hold

    weight = DoubleField(multi=True, default_value=1.0)
    w = weight

    weightStyle = WeightStyleEnumField(multi=True, default_value=0)
    ws = weightStyle

    preCycle = DoubleField(multi=True, default_value=0.0, min_value=0.0)
    cb = preCycle

    postCycle = DoubleField(multi=True, default_value=0.0, min_value=0.0)
    ca = postCycle

    enable = BoolField(multi=True, default_value=True)
    ea = enable

    track = ShortField(multi=True, default_value=0, min_value=0)
    tr = track

    trackState = ShortField(multi=True, default_value=0, min_value=0)
    ts = trackState

    numTracks = ShortField(default_value=0)
    nt = numTracks

    cycle = DoubleField(multi=True, default_value=1.0)
    cy = cycle

    startPercent = DoubleField(multi=True, default_value=0.0)
    sp = startPercent

    absolute = BoolField(multi=True, default_value=False)
    a = absolute

    absoluteRotations = BoolField(multi=True, default_value=False)
    ar = absoluteRotations
