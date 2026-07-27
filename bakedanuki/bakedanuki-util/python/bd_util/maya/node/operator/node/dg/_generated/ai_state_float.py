# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


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


class GeneratedAiStateFloat(DG):
    __slots__ = ()

    NODE_TYPE = "aiStateFloat"

    outValue = FloatField(default_value=0.0, writable=False)
    out = outValue

    sx = FloatField(default_value=0.0, writable=False)

    sy = FloatField(default_value=0.0, writable=False)

    px = FloatField(default_value=0.0, writable=False)

    py = FloatField(default_value=0.0, writable=False)

    time = FloatField(default_value=0.0, writable=False)

    Rl = FloatField(default_value=0.0, writable=False)

    bu = FloatField(default_value=0.0, writable=False)

    bv = FloatField(default_value=0.0, writable=False)

    u = FloatField(default_value=0.0, writable=False)

    v = FloatField(default_value=0.0, writable=False)

    area = FloatField(default_value=0.0, writable=False)

    dudx = FloatField(default_value=0.0, writable=False)

    dudy = FloatField(default_value=0.0, writable=False)

    dvdx = FloatField(default_value=0.0, writable=False)

    dvdy = FloatField(default_value=0.0, writable=False)

    shutter_start = FloatField(default_value=0.0, writable=False)

    shutter_end = FloatField(default_value=0.0, writable=False)

    variable = VariableEnumField(default_value=0)
