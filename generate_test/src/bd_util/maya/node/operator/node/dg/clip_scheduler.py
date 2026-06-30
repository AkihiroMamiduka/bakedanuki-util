# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.clip_scheduler import (
    BlendClipsField,
    BlendListField,
    ClipFunctionField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField


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


class ClipScheduler(DG):
    __slots__ = ()

    NODE_TYPE = "clipScheduler"

    blendList = BlendListField(multi=True)
    bl = blendList

    blendClips = BlendClipsField(multi=True)
    bc = blendClips

    clipEvaluate = TypedField()
    ce = clipEvaluate

    clipStatePercentEval = TypedField()
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

    # TODO: clipFunction_Inmap.clipFunction_InmapTo (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: clipFunction_Inmap.clipFunction_InmapFrom (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: clipFunction_Outmap.clipFunction_OutmapTo (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: clipFunction_Outmap.clipFunction_OutmapFrom (attributeType=None, dataType=None) は未対応のため手動で追加してください

    clip = MessageField(multi=True)
    cl = clip

    start = TimeField(multi=True)
    st = start

    sourceStart = TimeField(multi=True)
    ss = sourceStart

    sourceEnd = TimeField(multi=True)
    se = sourceEnd

    scale = DoubleField(multi=True)
    sc = scale

    hold = TimeField(multi=True)
    h = hold

    weight = DoubleField(multi=True)
    w = weight

    weightStyle = WeightStyleEnumField(multi=True)
    ws = weightStyle

    preCycle = DoubleField(multi=True)
    cb = preCycle

    postCycle = DoubleField(multi=True)
    ca = postCycle

    enable = BoolField(multi=True)
    ea = enable

    track = ShortField(multi=True)
    tr = track

    trackState = ShortField(multi=True)
    ts = trackState

    numTracks = ShortField()
    nt = numTracks

    cycle = DoubleField(multi=True)
    cy = cycle

    startPercent = DoubleField(multi=True)
    sp = startPercent

    absolute = BoolField(multi=True)
    a = absolute

    absoluteRotations = BoolField(multi=True)
    ar = absoluteRotations
