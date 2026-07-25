# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.dt.string import DataStringField


class TransitionInTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FADE = 0
    DISSOLVE = 1


class TransitionInTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FADE = 0
    DISSOLVE = 1

    NAME_MAP = {
        FADE: "fade",
        DISSOLVE: "dissolve",
    }


class TransitionInTypeEnumField(
    EnumField[TransitionInTypeEnumAttrOperator, TransitionInTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransitionInTypeEnumAttrOperator
    PLUG_CLS = TransitionInTypeEnumPlugOperator


class TransitionOutTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FADE = 0
    DISSOLVE = 1


class TransitionOutTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FADE = 0
    DISSOLVE = 1

    NAME_MAP = {
        FADE: "fade",
        DISSOLVE: "dissolve",
    }


class TransitionOutTypeEnumField(
    EnumField[TransitionOutTypeEnumAttrOperator, TransitionOutTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransitionOutTypeEnumAttrOperator
    PLUG_CLS = TransitionOutTypeEnumPlugOperator


class _GeneratedShot(DG):
    __slots__ = ()

    NODE_TYPE = "shot"

    startFrame = TimeField(default_value=0.0)
    sf = startFrame

    endFrame = TimeField(default_value=60.0)
    ef = endFrame

    sequenceStartFrame = TimeField(default_value=0.0)
    ssf = sequenceStartFrame

    scale = DoubleField(default_value=1.0)
    s = scale

    preHold = TimeField(default_value=0.0, min_value=0.0)
    prh = preHold

    postHold = TimeField(default_value=0.0, min_value=0.0)
    psh = postHold

    sequenceEndFrame = TimeField(default_value=60.0, writable=False)
    se = sequenceEndFrame

    clip = MessageField()
    clp = clip

    clipScale = DoubleField(default_value=1.0)
    cs = clipScale

    clipPreHold = TimeField(default_value=0.0, min_value=0.0)
    cprh = clipPreHold

    clipPostHold = TimeField(default_value=0.0, min_value=0.0)
    cpsh = clipPostHold

    clipZeroOffset = TimeField(default_value=0.0)
    czo = clipZeroOffset

    clipDuration = TimeField(default_value=0.0)
    cdr = clipDuration

    clipValid = BoolField(default_value=True)
    cv = clipValid

    favorite = BoolField(default_value=False)
    fav = favorite

    userStatus1 = BoolField(default_value=False)
    us1 = userStatus1

    userStatus2 = BoolField(default_value=False)
    us2 = userStatus2

    audio = MessageField()
    aud = audio

    cameras = MessageField(multi=True)
    cam = cameras

    currentCamera = MessageField()
    ccm = currentCamera

    track = LongField(default_value=1)
    tk = track

    trackState = ShortField(default_value=0, min_value=0)
    ts = trackState

    shotName = DataStringField()
    sn = shotName

    members = MessageField()
    mbr = members

    wResolution = LongField(default_value=1024)
    wres = wResolution

    hResolution = LongField(default_value=778)
    hres = hResolution

    customAnim = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    ca = customAnim

    flags = LongField(default_value=0)
    f = flags

    transitionInType = TransitionInTypeEnumField(default_value=0)
    tit = transitionInType

    transitionOutType = TransitionOutTypeEnumField(default_value=0)
    tot = transitionOutType

    transitionInLength = TimeField(default_value=0.0, min_value=0.0)
    til = transitionInLength

    transitionOutLength = TimeField(default_value=0.0, min_value=0.0)
    tol = transitionOutLength

    hasIncomingStt = BoolField(default_value=False)
    his = hasIncomingStt

    hasOutgoingStt = BoolField(default_value=False)
    hos = hasOutgoingStt
