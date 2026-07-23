# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


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


class _GeneratedCloseCurve(DG):
    __slots__ = ()

    NODE_TYPE = "closeCurve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    preserveShape = PreserveShapeEnumField(default_value=1)
    ps = preserveShape

    blendBias = DoubleField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    bb = blendBias

    blendKnotInsertion = BoolField(default_value=False)
    bki = blendKnotInsertion

    parameter = DoubleField(default_value=0.1, soft_min_value=-1.0, soft_max_value=1.0)
    p = parameter

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve
