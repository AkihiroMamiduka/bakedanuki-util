# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.time_editor_clip import (
    ClipField,
    GhostColorField,
    GhostPostColorField,
    GhostPreColorField,
    LayerField,
    OffsetField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.string import DataStringField


class TimeEditorClip(DG):
    __slots__ = ()

    NODE_TYPE = "timeEditorClip"

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

    content = MessageField()
    cnt = content

    track = LongField()
    tr = track

    clipWeight = DoubleField()
    cwt = clipWeight

    state = TypedField()
    s = state

    clipTrackMuted = BoolField()
    tm = clipTrackMuted

    clipSoloMuted = BoolField()
    clsm = clipSoloMuted

    transitionTo = LongField()
    trci = transitionTo

    animSource = MessageField()
    as_ = animSource

    audioFile = DataStringField()
    af = audioFile

    layer = LayerField(multi=True)
    l = layer

    blendShapeTarget = MessageField(multi=True)
    bs = blendShapeTarget

    ghost = BoolField()
    gh = ghost

    ghostRootDefault = BoolField()
    grd = ghostRootDefault

    ghostRootCustom = BoolField()
    grc = ghostRootCustom

    ghostColorCustom = BoolField()
    gcc = ghostColorCustom

    ghostColor = GhostColorField()
    gc = ghostColor
    ghostColorR = ghostColor.ghostColorR
    gcr = ghostColorR
    ghostColorG = ghostColor.ghostColorG
    gcg = ghostColorG
    ghostColorB = ghostColor.ghostColorB
    gcb = ghostColorB

    ghostStepSize = LongField()
    gss = ghostStepSize

    ghostCountPost = LongField()
    gct = ghostCountPost

    ghostCountPre = LongField()
    gce = ghostCountPre

    ghostPostColor = GhostPostColorField()
    gtc = ghostPostColor
    ghostPostColorR = ghostPostColor.ghostPostColorR
    gtr = ghostPostColorR
    ghostPostColorG = ghostPostColor.ghostPostColorG
    gtg = ghostPostColorG
    ghostPostColorB = ghostPostColor.ghostPostColorB
    gtb = ghostPostColorB

    ghostPreColor = GhostPreColorField()
    gec = ghostPreColor
    ghostPreColorR = ghostPreColor.ghostPreColorR
    ger = ghostPreColorR
    ghostPreColorG = ghostPreColor.ghostPreColorG
    geg = ghostPreColorG
    ghostPreColorB = ghostPreColor.ghostPreColorB
    geb = ghostPreColorB

    ghostRootTargets = MessageField(multi=True)
    gr = ghostRootTargets
