# coding: utf-8
from ._core import Transform
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ....attr.define.std.dt.matrix import DataMatrixField


class DisplayLevelEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    USELOD = 0
    SHOW = 1
    HIDE = 2


class DisplayLevelEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    USELOD = 0
    SHOW = 1
    HIDE = 2

    NAME_MAP = {
        USELOD: "uselod",
        SHOW: "show",
        HIDE: "hide",
    }


class DisplayLevelEnumField(
    EnumField[DisplayLevelEnumAttrOperator, DisplayLevelEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplayLevelEnumAttrOperator
    PLUG_CLS = DisplayLevelEnumPlugOperator


class LodGroup(Transform):
    __slots__ = ()

    NODE_TYPE = "lodGroup"

    cameraMatrix = DataMatrixField()
    cm = cameraMatrix

    threshold = DoubleLinearField(multi=True, default_value=0.0)
    th = threshold

    displayLevel = DisplayLevelEnumField(multi=True, default_value=0)
    dl = displayLevel

    useScreenHeightPercentage = BoolField(default_value=False)
    ush = useScreenHeightPercentage

    percentageThreshold = DoubleField(multi=True, default_value=0.0)
    pth = percentageThreshold

    worldSpace = BoolField(default_value=True)
    ws = worldSpace

    minMaxDistance = BoolField(default_value=False)
    mmd = minMaxDistance

    minDistance = DoubleField(default_value=-100.0)
    mid = minDistance

    maxDistance = DoubleField(default_value=100.0)
    mxd = maxDistance

    distance = DoubleLinearField(default_value=0.0)
    d = distance

    screenHeightPercentage = DoubleField(default_value=0.0)
    shp = screenHeightPercentage

    activeLevel = LongField(default_value=0)
    al = activeLevel

    output = BoolField(multi=True, default_value=False, writable=False)
    o = output

    focalLength = DoubleField(default_value=0.0)
    fl = focalLength
