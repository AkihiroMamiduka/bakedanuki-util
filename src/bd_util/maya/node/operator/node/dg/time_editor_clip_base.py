# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.time_editor_clip_base import (
    ClipField,
    OffsetField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.matrix import DataMatrixField


class TimeEditorClipBase(DG):
    __slots__ = ()

    NODE_TYPE = "timeEditorClipBase"

    clip = ClipField(multi=True)
    clp = clip

    clipColorR = FloatField()
    ccr = clipColorR

    clipColorG = FloatField()
    ccg = clipColorG

    clipColorB = FloatField()
    ccb = clipColorB

    offset = OffsetField()
    ofs = offset
    offsetMode = offset.offsetMode
    ofm = offsetMode
    offsetMtx = offset.offsetMtx
    omt = offsetMtx
    pivotMtx = offset.pivotMtx
    pmt = pivotMtx
    matchclip = offset.matchclip
    mcl = matchclip
    matchTime = offset.matchTime
    mtm = matchTime
    roots = offset.roots
    rts = roots
    matchObj = offset.matchObj
    mob = matchObj

    rootObjLocalXform = DataMatrixField()
    rolx = rootObjLocalXform

    rootObjParentXform = DataMatrixField()
    ropx = rootObjParentXform

    rootObj = MessageField()
    rob = rootObj

    lastEvaluationTime = TimeField()
    let = lastEvaluationTime
