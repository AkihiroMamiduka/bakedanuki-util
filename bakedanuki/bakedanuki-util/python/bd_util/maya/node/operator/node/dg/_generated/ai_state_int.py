# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class VariableEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X = 0
    Y = 1
    SI = 2
    RT = 3
    TRANSP_INDEX = 4
    TID = 5
    BOUNCES = 6
    BOUNCES_DIFFUSE = 7
    BOUNCES_SPECULAR = 8
    BOUNCES_REFLECT = 9
    BOUNCES_TRANSMIT = 10
    BOUNCES_VOLUME = 11
    FHEMI = 12
    FI = 13
    NLIGHTS = 14
    INCLUSIVE_TRACESET = 15
    SKIP_SHADOW = 16
    SC = 17


class VariableEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X = 0
    Y = 1
    SI = 2
    RT = 3
    TRANSP_INDEX = 4
    TID = 5
    BOUNCES = 6
    BOUNCES_DIFFUSE = 7
    BOUNCES_SPECULAR = 8
    BOUNCES_REFLECT = 9
    BOUNCES_TRANSMIT = 10
    BOUNCES_VOLUME = 11
    FHEMI = 12
    FI = 13
    NLIGHTS = 14
    INCLUSIVE_TRACESET = 15
    SKIP_SHADOW = 16
    SC = 17

    NAME_MAP = {
        X: "x",
        Y: "y",
        SI: "si",
        RT: "Rt",
        TRANSP_INDEX: "transp_index",
        TID: "tid",
        BOUNCES: "bounces",
        BOUNCES_DIFFUSE: "bounces_diffuse",
        BOUNCES_SPECULAR: "bounces_specular",
        BOUNCES_REFLECT: "bounces_reflect",
        BOUNCES_TRANSMIT: "bounces_transmit",
        BOUNCES_VOLUME: "bounces_volume",
        FHEMI: "fhemi",
        FI: "fi",
        NLIGHTS: "nlights",
        INCLUSIVE_TRACESET: "inclusive_traceset",
        SKIP_SHADOW: "skip_shadow",
        SC: "sc",
    }


class VariableEnumField(
    EnumField[VariableEnumAttrOperator, VariableEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VariableEnumAttrOperator
    PLUG_CLS = VariableEnumPlugOperator


class GeneratedAiStateInt(DG):
    __slots__ = ()

    NODE_TYPE = "aiStateInt"

    outValue = LongField(default_value=0, writable=False)
    out = outValue

    x = LongField(default_value=0, writable=False)

    y = LongField(default_value=0, writable=False)

    si = LongField(default_value=0, writable=False)

    Rt = LongField(default_value=0, writable=False)

    transp_index = LongField(default_value=0, writable=False)

    tid = LongField(default_value=0, writable=False)

    bounces = LongField(default_value=0, writable=False)

    bounces_diffuse = LongField(default_value=0, writable=False)

    bounces_specular = LongField(default_value=0, writable=False)

    bounces_reflect = LongField(default_value=0, writable=False)

    bounces_transmit = LongField(default_value=0, writable=False)

    bounces_volume = LongField(default_value=0, writable=False)

    fhemi = LongField(default_value=0, writable=False)

    fi = LongField(default_value=0, writable=False)

    nlights = LongField(default_value=0, writable=False)

    inclusive_traceset = LongField(default_value=0, writable=False)

    skip_shadow = LongField(default_value=0, writable=False)

    sc = LongField(default_value=0, writable=False)

    variable = VariableEnumField(default_value=0)
