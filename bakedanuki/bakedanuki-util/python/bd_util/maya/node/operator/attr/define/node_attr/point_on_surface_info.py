# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..custom import Double3Field


class ResultPlugOperator(CompoundPlugOperator["ResultAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("position", "p"),
        ("normal", "n"),
        ("normalizedNormal", "nn"),
        ("tangentU", "tu"),
        ("normalizedTangentU", "ntu"),
        ("tangentV", "tv"),
        ("normalizedTangentV", "ntv"),
    )

    position = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    p = position

    normal = Double3Field(default_value=(0.0, 0.0, 1.0), writable=False)
    n = normal

    normalizedNormal = Double3Field(
        default_value=(0.0, 0.0, 1.0), writable=False
    )
    nn = normalizedNormal

    tangentU = Double3Field(default_value=(1.0, 0.0, 0.0), writable=False)
    tu = tangentU

    normalizedTangentU = Double3Field(
        default_value=(1.0, 0.0, 0.0), writable=False
    )
    ntu = normalizedTangentU

    tangentV = Double3Field(default_value=(1.0, 0.0, 0.0), writable=False)
    tv = tangentV

    normalizedTangentV = Double3Field(
        default_value=(1.0, 0.0, 0.0), writable=False
    )
    ntv = normalizedTangentV


class ResultAttrOperator(CompoundAttrOperator[ResultPlugOperator]):
    __slots__ = ()

    position = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    p = position

    normal = Double3Field(default_value=(0.0, 0.0, 1.0), writable=False)
    n = normal

    normalizedNormal = Double3Field(
        default_value=(0.0, 0.0, 1.0), writable=False
    )
    nn = normalizedNormal

    tangentU = Double3Field(default_value=(1.0, 0.0, 0.0), writable=False)
    tu = tangentU

    normalizedTangentU = Double3Field(
        default_value=(1.0, 0.0, 0.0), writable=False
    )
    ntu = normalizedTangentU

    tangentV = Double3Field(default_value=(1.0, 0.0, 0.0), writable=False)
    tv = tangentV

    normalizedTangentV = Double3Field(
        default_value=(1.0, 0.0, 0.0), writable=False
    )
    ntv = normalizedTangentV


class ResultField(CompoundField[ResultAttrOperator, ResultPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ResultAttrOperator
    PLUG_CLS = ResultPlugOperator

    position = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    p = position

    normal = Double3Field(default_value=(0.0, 0.0, 1.0), writable=False)
    n = normal

    normalizedNormal = Double3Field(
        default_value=(0.0, 0.0, 1.0), writable=False
    )
    nn = normalizedNormal

    tangentU = Double3Field(default_value=(1.0, 0.0, 0.0), writable=False)
    tu = tangentU

    normalizedTangentU = Double3Field(
        default_value=(1.0, 0.0, 0.0), writable=False
    )
    ntu = normalizedTangentU

    tangentV = Double3Field(default_value=(1.0, 0.0, 0.0), writable=False)
    tv = tangentV

    normalizedTangentV = Double3Field(
        default_value=(1.0, 0.0, 0.0), writable=False
    )
    ntv = normalizedTangentV
