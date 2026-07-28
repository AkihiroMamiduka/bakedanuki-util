# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class MethodEnumPlugOperator(EnumPlugOperator["MethodEnumAttrOperator"]):
    __slots__ = ()

    CONNECT = 0
    BLEND = 1


class MethodEnumAttrOperator(EnumAttrOperator[MethodEnumPlugOperator]):
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


class GeneratedAttachSurface(DG):
    __slots__ = ()

    NODE_TYPE = "attachSurface"

    inputSurface1 = DataNurbsSurfaceField()
    is1 = inputSurface1

    inputSurface2 = DataNurbsSurfaceField()
    is2 = inputSurface2

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface

    method = MethodEnumField(default_value=0)
    m = method

    directionU = BoolField(default_value=True)
    du = directionU

    reverse1 = BoolField(default_value=False)
    rv1 = reverse1

    reverse2 = BoolField(default_value=False)
    rv2 = reverse2

    swap1 = BoolField(default_value=False)
    sw1 = swap1

    swap2 = BoolField(default_value=False)
    sw2 = swap2

    twist = BoolField(default_value=False)
    tw = twist

    blendBias = DoubleField(
        default_value=0.5, soft_min_value=0.0, soft_max_value=1.0
    )
    bb = blendBias

    blendKnotInsertion = BoolField(default_value=False)
    bki = blendKnotInsertion

    parameter = DoubleField(
        default_value=0.1, soft_min_value=-1.0, soft_max_value=1.0
    )
    p = parameter

    keepMultipleKnots = BoolField(default_value=True)
    kmk = keepMultipleKnots
