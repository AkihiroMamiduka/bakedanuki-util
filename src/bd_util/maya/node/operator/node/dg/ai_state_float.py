# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class VariableEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SX = 0
    SY = 1
    PX = 2
    PY = 3
    TIME = 4
    RL = 5
    BU = 6
    BV = 7
    U = 8
    V = 9
    AREA = 10
    DUDX = 11
    DUDY = 12
    DVDX = 13
    DVDY = 14
    SHUTTER_START = 15
    SHUTTER_END = 16


class VariableEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SX = 0
    SY = 1
    PX = 2
    PY = 3
    TIME = 4
    RL = 5
    BU = 6
    BV = 7
    U = 8
    V = 9
    AREA = 10
    DUDX = 11
    DUDY = 12
    DVDX = 13
    DVDY = 14
    SHUTTER_START = 15
    SHUTTER_END = 16

    NAME_MAP = {
        SX: "sx",
        SY: "sy",
        PX: "px",
        PY: "py",
        TIME: "time",
        RL: "Rl",
        BU: "bu",
        BV: "bv",
        U: "u",
        V: "v",
        AREA: "area",
        DUDX: "dudx",
        DUDY: "dudy",
        DVDX: "dvdx",
        DVDY: "dvdy",
        SHUTTER_START: "shutter_start",
        SHUTTER_END: "shutter_end",
    }


class VariableEnumField(
    EnumField[VariableEnumAttrOperator, VariableEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VariableEnumAttrOperator
    PLUG_CLS = VariableEnumPlugOperator


class AiStateFloat(DG):
    __slots__ = ()

    NODE_TYPE = "aiStateFloat"

    outValue = FloatField()
    out = outValue

    sx = FloatField()

    sy = FloatField()

    px = FloatField()

    py = FloatField()

    time = FloatField()

    Rl = FloatField()

    bu = FloatField()

    bv = FloatField()

    u = FloatField()

    v = FloatField()

    area = FloatField()

    dudx = FloatField()

    dudy = FloatField()

    dvdx = FloatField()

    dvdy = FloatField()

    shutter_start = FloatField()

    shutter_end = FloatField()

    variable = VariableEnumField()
