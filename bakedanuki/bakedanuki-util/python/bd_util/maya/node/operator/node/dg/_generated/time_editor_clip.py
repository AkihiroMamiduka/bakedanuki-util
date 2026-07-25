# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.time_editor_clip import (
    ClipField,
    GhostColorField,
    GhostPostColorField,
    GhostPreColorField,
    LayerField,
    OffsetField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedTimeEditorClip(DG):
    __slots__ = ()

    NODE_TYPE = "timeEditorClip"

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

    lastEvaluationTime = TimeField(default_value=-3921501716349.82)
    let = lastEvaluationTime

    content = MessageField()
    cnt = content

    track = LongField(default_value=0)
    tr = track

    clipWeight = DoubleField(default_value=1.0)
    cwt = clipWeight

    state = TypedField()
    s = state

    clipTrackMuted = BoolField(default_value=False)
    tm = clipTrackMuted

    clipSoloMuted = BoolField(default_value=False)
    clsm = clipSoloMuted

    transitionTo = LongField(default_value=-1)
    trci = transitionTo

    animSource = MessageField()
    as_ = animSource

    audioFile = DataStringField()
    af = audioFile

    layer = LayerField(multi=True)
    l = layer

    blendShapeTarget = MessageField(multi=True)
    bs = blendShapeTarget

    ghost = BoolField(default_value=False)
    gh = ghost

    ghostRootDefault = BoolField(default_value=True)
    grd = ghostRootDefault

    ghostRootCustom = BoolField(default_value=False)
    grc = ghostRootCustom

    ghostColorCustom = BoolField(default_value=False)
    gcc = ghostColorCustom

    ghostColor = GhostColorField(default_value=(0.0, 0.0, 0.0))
    gc = ghostColor
    ghostColorR = ghostColor.ghostColorR
    gcr = ghostColorR
    ghostColorG = ghostColor.ghostColorG
    gcg = ghostColorG
    ghostColorB = ghostColor.ghostColorB
    gcb = ghostColorB

    ghostStepSize = LongField(default_value=0, min_value=1, max_value=10)
    gss = ghostStepSize

    ghostCountPost = LongField(default_value=0, min_value=0, max_value=10)
    gct = ghostCountPost

    ghostCountPre = LongField(default_value=0, min_value=0, max_value=10)
    gce = ghostCountPre

    ghostPostColor = GhostPostColorField(default_value=(0.0, 0.0, 0.0))
    gtc = ghostPostColor
    ghostPostColorR = ghostPostColor.ghostPostColorR
    gtr = ghostPostColorR
    ghostPostColorG = ghostPostColor.ghostPostColorG
    gtg = ghostPostColorG
    ghostPostColorB = ghostPostColor.ghostPostColorB
    gtb = ghostPostColorB

    ghostPreColor = GhostPreColorField(default_value=(0.0, 0.0, 0.0))
    gec = ghostPreColor
    ghostPreColorR = ghostPreColor.ghostPreColorR
    ger = ghostPreColorR
    ghostPreColorG = ghostPreColor.ghostPreColorG
    geg = ghostPreColorG
    ghostPreColorB = ghostPreColor.ghostPreColorB
    geb = ghostPreColorB

    ghostRootTargets = MessageField(multi=True)
    gr = ghostRootTargets
