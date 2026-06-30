# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.long import LongField


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


class AiStateInt(DG):
    __slots__ = ()

    NODE_TYPE = "aiStateInt"

    outValue = LongField()
    out = outValue

    x = LongField()

    y = LongField()

    si = LongField()

    Rt = LongField()

    transp_index = LongField()

    tid = LongField()

    bounces = LongField()

    bounces_diffuse = LongField()

    bounces_specular = LongField()

    bounces_reflect = LongField()

    bounces_transmit = LongField()

    bounces_volume = LongField()

    fhemi = LongField()

    fi = LongField()

    nlights = LongField()

    inclusive_traceset = LongField()

    skip_shadow = LongField()

    sc = LongField()

    variable = VariableEnumField()
