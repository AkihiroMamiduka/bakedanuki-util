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

    inSplineData = TypedField()
    isd = inSplineData

    outSplineData = TypedField()
    osd = outSplineData

    mute = BoolField()
    m = mute

    cutMode = CutModeEnumField()
    ctm = cutMode

    mask = FloatField()
    mk = mask

    amount = DoubleLinearField()
    a = amount

    percentage = FloatField()
    pt = percentage

    minRemainLength = FloatField()
    mrl = minRemainLength

    redistributingCV = BoolField()
    rd = redistributingCV
