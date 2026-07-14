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


class PreserveShapeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    IGNORE = 0
    PRESERVE = 1
    BLEND = 2


class PreserveShapeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    IGNORE = 0
    PRESERVE = 1
    BLEND = 2

    NAME_MAP = {
        IGNORE: "Ignore",
        PRESERVE: "Preserve",
        BLEND: "Blend",
    }


class PreserveShapeEnumField(
    EnumField[PreserveShapeEnumAttrOperator, PreserveShapeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PreserveShapeEnumAttrOperator
    PLUG_CLS = PreserveShapeEnumPlugOperator


class DirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    U = 0
    V = 1
    U_AMP_V = 2


class DirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    U = 0
    V = 1
    U_AMP_V = 2

    NAME_MAP = {
        U: "U",
        V: "V",
        U_AMP_V: "U & V",
    }


class DirectionEnumField(
    EnumField[DirectionEnumAttrOperator, DirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DirectionEnumAttrOperator
    PLUG_CLS = DirectionEnumPlugOperator


class CloseSurface(DG):
    __slots__ = ()

    NODE_TYPE = "closeSurface"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    preserveShape = PreserveShapeEnumField(default_value=1)
    ps = preserveShape

    blendBias = DoubleField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    bb = blendBias

    blendKnotInsertion = BoolField(default_value=False)
    bki = blendKnotInsertion

    parameter = DoubleField(default_value=0.1, soft_min_value=-1.0, soft_max_value=1.0)
    p = parameter

    direction = DirectionEnumField(default_value=0)
    d = direction

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface
