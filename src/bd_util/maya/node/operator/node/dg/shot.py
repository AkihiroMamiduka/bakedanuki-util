# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.string import DataStringField


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


class Shot(DG):
    __slots__ = ()

    NODE_TYPE = "shot"

    startFrame = TimeField()
    sf = startFrame

    endFrame = TimeField()
    ef = endFrame

    sequenceStartFrame = TimeField()
    ssf = sequenceStartFrame

    scale = DoubleField()
    s = scale

    preHold = TimeField()
    prh = preHold

    postHold = TimeField()
    psh = postHold

    sequenceEndFrame = TimeField()
    se = sequenceEndFrame

    clip = MessageField()
    clp = clip

    clipScale = DoubleField()
    cs = clipScale

    clipPreHold = TimeField()
    cprh = clipPreHold

    clipPostHold = TimeField()
    cpsh = clipPostHold

    clipZeroOffset = TimeField()
    czo = clipZeroOffset

    clipDuration = TimeField()
    cdr = clipDuration

    clipValid = BoolField()
    cv = clipValid

    favorite = BoolField()
    fav = favorite

    userStatus1 = BoolField()
    us1 = userStatus1

    userStatus2 = BoolField()
    us2 = userStatus2

    audio = MessageField()
    aud = audio

    cameras = MessageField(multi=True)
    cam = cameras

    currentCamera = MessageField()
    ccm = currentCamera

    track = LongField()
    tk = track

    trackState = ShortField()
    ts = trackState

    shotName = DataStringField()
    sn = shotName

    members = MessageField()
    mbr = members

    wResolution = LongField()
    wres = wResolution

    hResolution = LongField()
    hres = hResolution

    customAnim = DoubleField()
    ca = customAnim

    flags = LongField()
    f = flags

    transitionInType = TransitionInTypeEnumField()
    tit = transitionInType

    transitionOutType = TransitionOutTypeEnumField()
    tot = transitionOutType

    transitionInLength = TimeField()
    til = transitionInLength

    transitionOutLength = TimeField()
    tol = transitionOutLength

    hasIncomingStt = BoolField()
    his = hasIncomingStt

    hasOutgoingStt = BoolField()
    hos = hasOutgoingStt
