# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class MethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONNECT = 0
    BLEND = 1


class MethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONNECT = 0
    BLEND = 1

    NAME_MAP = {
        CONNECT: "Connect",
        BLEND: "Blend",
    }


class MethodEnumField(
    EnumField[MethodEnumAttrOperator, MethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MethodEnumAttrOperator
    PLUG_CLS = MethodEnumPlugOperator


class AttachSurface(DG):
    __slots__ = ()

    NODE_TYPE = "attachSurface"

    inputSurface1 = DataNurbsSurfaceField()
    is1 = inputSurface1

    inputSurface2 = DataNurbsSurfaceField()
    is2 = inputSurface2

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface

    method = MethodEnumField()
    m = method

    directionU = BoolField()
    du = directionU

    reverse1 = BoolField()
    rv1 = reverse1

    reverse2 = BoolField()
    rv2 = reverse2

    swap1 = BoolField()
    sw1 = swap1

    swap2 = BoolField()
    sw2 = swap2

    twist = BoolField()
    tw = twist

    blendBias = DoubleField()
    bb = blendBias

    blendKnotInsertion = BoolField()
    bki = blendKnotInsertion

    parameter = DoubleField()
    p = parameter

    keepMultipleKnots = BoolField()
    kmk = keepMultipleKnots
