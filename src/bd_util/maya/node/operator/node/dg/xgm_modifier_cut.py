# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class CutModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ABSOLUTE = 0
    RELATIVE = 1


class CutModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ABSOLUTE = 0
    RELATIVE = 1

    NAME_MAP = {
        ABSOLUTE: "Absolute",
        RELATIVE: "Relative",
    }


class CutModeEnumField(
    EnumField[CutModeEnumAttrOperator, CutModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CutModeEnumAttrOperator
    PLUG_CLS = CutModeEnumPlugOperator


class XgmModifierCut(DG):
    __slots__ = ()

    NODE_TYPE = "xgmModifierCut"

    inSplineData = TypedField(readable=False)
    isd = inSplineData

    outSplineData = TypedField(writable=False)
    osd = outSplineData

    mute = BoolField(default_value=False)
    m = mute

    cutMode = CutModeEnumField(default_value=0)
    ctm = cutMode

    mask = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    mk = mask

    amount = DoubleLinearField(default_value=0.0, min_value=0.0, soft_max_value=10.0)
    a = amount

    percentage = FloatField(default_value=10.0, min_value=0.0, max_value=100.0)
    pt = percentage

    minRemainLength = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)
    mrl = minRemainLength

    redistributingCV = BoolField(default_value=True)
    rd = redistributingCV
