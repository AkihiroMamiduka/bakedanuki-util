# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.time_editor_clip_base import (
    ClipField,
    OffsetField,
)
from ...attr.define.std.at.unit_scalar.time import TimeField


class TimeEditorClipBase(DG):
    __slots__ = ()

    NODE_TYPE = "timeEditorClipBase"

    clip = ClipField(multi=True)
    clp = clip

    # TODO: clip.clipColorR (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: clip.clipColorG (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: clip.clipColorB (attributeType=None, dataType=None) は未対応のため手動で追加してください

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

    # TODO: roots.rootObjLocalXform (attributeType=None, dataType=matrix) は未対応のため手動で追加してください

    # TODO: roots.rootObjParentXform (attributeType=None, dataType=matrix) は未対応のため手動で追加してください

    # TODO: roots.rootObj (attributeType=None, dataType=None) は未対応のため手動で追加してください

    lastEvaluationTime = TimeField()
    let = lastEvaluationTime
