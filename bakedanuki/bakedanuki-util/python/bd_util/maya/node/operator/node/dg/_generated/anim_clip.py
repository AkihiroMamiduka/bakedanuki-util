# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.anim_clip import (
    LocalStartPositionField,
    WorldStartPositionField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField


class WeightStyleEnumPlugOperator(
    EnumPlugOperator["WeightStyleEnumAttrOperator"]
):
    __slots__ = ()

    FROM_START = 0
    FROM_ZERO = 1
    ABSOLUTE_FROM_ZERO = 2


class WeightStyleEnumAttrOperator(
    EnumAttrOperator[WeightStyleEnumPlugOperator]
):
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


class OffsetEnumPlugOperator(EnumPlugOperator["OffsetEnumAttrOperator"]):
    __slots__ = ()

    RELATIVE = 0
    ABSOLUTE = 1


class OffsetEnumAttrOperator(EnumAttrOperator[OffsetEnumPlugOperator]):
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


class GeneratedAnimClip(DG):
    __slots__ = ()

    NODE_TYPE = "animClip"

    enable = BoolField(default_value=True)
    ea = enable

    absoluteChannel = BoolField(multi=True, default_value=False)
    ac = absoluteChannel

    startFrame = TimeField(default_value=0.0)
    sf = startFrame

    scale = DoubleField(default_value=1.0, min_value=0.0)
    sc = scale

    hold = TimeField(default_value=0.0, min_value=0.0)
    h = hold

    preCycle = DoubleField(default_value=0.0, min_value=0.0)
    cb = preCycle

    postCycle = DoubleField(default_value=0.0, min_value=0.0)
    ca = postCycle

    weight = DoubleField(default_value=1.0)
    w = weight

    weightStyle = WeightStyleEnumField(default_value=0)
    ws = weightStyle

    pose = BoolField(default_value=False)
    ps = pose

    sourceStart = TimeField(default_value=0.0)
    ss = sourceStart

    sourceEnd = TimeField(default_value=0.0)
    se = sourceEnd

    clip = MessageField()
    cl = clip

    clipInstance = BoolField(default_value=True)
    ci = clipInstance

    clipData = TypedField()
    cd = clipData

    recomputeOffset = BoolField(default_value=False, writable=False)
    roff = recomputeOffset

    offsetXform = DataMatrixField()
    oxf = offsetXform

    timeWarp = DoubleField(default_value=0.0)
    tw = timeWarp

    timeWarpEnable = BoolField(default_value=False)
    twe = timeWarpEnable

    start = TimeField(default_value=0.0)
    st = start

    duration = TimeField(default_value=0.0)
    du = duration

    offset = OffsetEnumField(default_value=0)
    o = offset

    absoluteRotations = BoolField(default_value=False)
    abro = absoluteRotations

    cycle = DoubleField(default_value=1.0)
    cy = cycle

    startTrim = TimeField(default_value=0.0)
    str = startTrim

    startPercent = DoubleField(default_value=0.0)
    sp = startPercent

    useChannelOffset = BoolField(default_value=True)
    uco = useChannelOffset

    channelOffset = DoubleField(multi=True, default_value=0.0)
    co = channelOffset

    worldStartPosition = WorldStartPositionField(default_value=(0.0, 0.0, 0.0))
    wsp = worldStartPosition
    worldStartPositionX = worldStartPosition.worldStartPositionX
    wspx = worldStartPositionX
    worldStartPositionY = worldStartPosition.worldStartPositionY
    wspy = worldStartPositionY
    worldStartPositionZ = worldStartPosition.worldStartPositionZ
    wspz = worldStartPositionZ

    localStartPosition = LocalStartPositionField(default_value=(0.0, 0.0, 0.0))
    lsp = localStartPosition
    localStartPositionX = localStartPosition.localStartPositionX
    lspx = localStartPositionX
    localStartPositionY = localStartPosition.localStartPositionY
    lspy = localStartPositionY
    localStartPositionZ = localStartPosition.localStartPositionZ
    lspz = localStartPositionZ
