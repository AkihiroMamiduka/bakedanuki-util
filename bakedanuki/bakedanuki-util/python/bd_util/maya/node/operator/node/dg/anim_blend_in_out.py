# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.typed import TypedField


class RotateInterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    QUATERNION = 0
    EULER = 1


class RotateInterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    QUATERNION = 0
    EULER = 1

    NAME_MAP = {
        QUATERNION: "Quaternion",
        EULER: "Euler",
    }


class RotateInterpEnumField(
    EnumField[RotateInterpEnumAttrOperator, RotateInterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateInterpEnumAttrOperator
    PLUG_CLS = RotateInterpEnumPlugOperator


class AnimBlendInOut(DG):
    __slots__ = ()

    NODE_TYPE = "animBlendInOut"

    blend = TypedField(writable=False)
    b = blend

    weight = DoubleField(default_value=0.0)
    w = weight

    rotateInterp = RotateInterpEnumField(default_value=0)
    ri = rotateInterp
