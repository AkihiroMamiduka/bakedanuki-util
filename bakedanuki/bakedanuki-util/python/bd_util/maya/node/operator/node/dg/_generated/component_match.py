# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


class MatchModeEnumPlugOperator(EnumPlugOperator["MatchModeEnumAttrOperator"]):
    __slots__ = ()

    CLOSESTPOINT = 0
    OTHER = 1


class MatchModeEnumAttrOperator(EnumAttrOperator[MatchModeEnumPlugOperator]):
    __slots__ = ()

    CLOSESTPOINT = 0
    OTHER = 1

    NAME_MAP = {
        CLOSESTPOINT: "ClosestPoint",
        OTHER: "Other",
    }


class MatchModeEnumField(
    EnumField[MatchModeEnumAttrOperator, MatchModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MatchModeEnumAttrOperator
    PLUG_CLS = MatchModeEnumPlugOperator


class GeneratedComponentMatch(DG):
    __slots__ = ()

    NODE_TYPE = "componentMatch"

    inputGeometry = TypedField()
    ig = inputGeometry

    targetGeometry = TypedField()
    tg = targetGeometry

    componentTagExpression = DataStringField()
    gtg = componentTagExpression

    matchMode = MatchModeEnumField(default_value=0)
    mmde = matchMode

    uniqueMatch = BoolField(default_value=True)
    unq = uniqueMatch

    componentLookup = LongField(multi=True, default_value=0, writable=False)
    clkp = componentLookup
