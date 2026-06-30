# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.anim_clip import (
    LocalStartPositionField,
    WorldStartPositionField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.matrix import DataMatrixField


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


class OffsetEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RELATIVE = 0
    ABSOLUTE = 1


class OffsetEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RELATIVE = 0
    ABSOLUTE = 1

    NAME_MAP = {
        RELATIVE: "Relative",
        ABSOLUTE: "Absolute",
    }


class OffsetEnumField(
    EnumField[OffsetEnumAttrOperator, OffsetEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetEnumAttrOperator
    PLUG_CLS = OffsetEnumPlugOperator


class AnimClip(DG):
    __slots__ = ()

    NODE_TYPE = "animClip"

    enable = BoolField()
    ea = enable

    absoluteChannel = BoolField(multi=True)
    ac = absoluteChannel

    startFrame = TimeField()
    sf = startFrame

    scale = DoubleField()
    sc = scale

    hold = TimeField()
    h = hold

    preCycle = DoubleField()
    cb = preCycle

    postCycle = DoubleField()
    ca = postCycle

    weight = DoubleField()
    w = weight

    weightStyle = WeightStyleEnumField()
    ws = weightStyle

    pose = BoolField()
    ps = pose

    sourceStart = TimeField()
    ss = sourceStart

    sourceEnd = TimeField()
    se = sourceEnd

    clip = MessageField()
    cl = clip

    clipInstance = BoolField()
    ci = clipInstance

    clipData = TypedField()
    cd = clipData

    recomputeOffset = BoolField()
    roff = recomputeOffset

    offsetXform = DataMatrixField()
    oxf = offsetXform

    timeWarp = DoubleField()
    tw = timeWarp

    timeWarpEnable = BoolField()
    twe = timeWarpEnable

    start = TimeField()
    st = start

    duration = TimeField()
    du = duration

    offset = OffsetEnumField()
    o = offset

    absoluteRotations = BoolField()
    abro = absoluteRotations

    cycle = DoubleField()
    cy = cycle

    startTrim = TimeField()
    str = startTrim

    startPercent = DoubleField()
    sp = startPercent

    useChannelOffset = BoolField()
    uco = useChannelOffset

    channelOffset = DoubleField(multi=True)
    co = channelOffset

    worldStartPosition = WorldStartPositionField()
    wsp = worldStartPosition
    worldStartPositionX = worldStartPosition.worldStartPositionX
    wspx = worldStartPositionX
    worldStartPositionY = worldStartPosition.worldStartPositionY
    wspy = worldStartPositionY
    worldStartPositionZ = worldStartPosition.worldStartPositionZ
    wspz = worldStartPositionZ

    localStartPosition = LocalStartPositionField()
    lsp = localStartPosition
    localStartPositionX = localStartPosition.localStartPositionX
    lspx = localStartPositionX
    localStartPositionY = localStartPosition.localStartPositionY
    lspy = localStartPositionY
    localStartPositionZ = localStartPosition.localStartPositionZ
    lspz = localStartPositionZ
