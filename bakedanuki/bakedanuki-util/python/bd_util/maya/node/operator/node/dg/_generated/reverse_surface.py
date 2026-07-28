# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class DirectionEnumPlugOperator(EnumPlugOperator["DirectionEnumAttrOperator"]):
    __slots__ = ()

    U = 0
    V = 1
    U_AMP_V = 2
    SWAP = 3


class DirectionEnumAttrOperator(EnumAttrOperator[DirectionEnumPlugOperator]):
    __slots__ = ()

    U = 0
    V = 1
    U_AMP_V = 2
    SWAP = 3

    NAME_MAP = {
        U: "U",
        V: "V",
        U_AMP_V: "U & V",
        SWAP: "Swap",
    }


class DirectionEnumField(
    EnumField[DirectionEnumAttrOperator, DirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DirectionEnumAttrOperator
    PLUG_CLS = DirectionEnumPlugOperator


class GeneratedReverseSurface(DG):
    __slots__ = ()

    NODE_TYPE = "reverseSurface"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    direction = DirectionEnumField(default_value=0)
    d = direction

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface
