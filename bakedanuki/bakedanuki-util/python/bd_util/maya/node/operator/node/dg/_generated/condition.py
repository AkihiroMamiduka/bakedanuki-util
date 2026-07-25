# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.condition import (
    ColorIfFalseField,
    ColorIfTrueField,
    OutColorField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class OperationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    EQUAL = 0
    NOT_EQUAL = 1
    GREATER_THAN = 2
    GREATER_OR_EQUAL = 3
    LESS_THAN = 4
    LESS_OR_EQUAL = 5


class OperationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    EQUAL = 0
    NOT_EQUAL = 1
    GREATER_THAN = 2
    GREATER_OR_EQUAL = 3
    LESS_THAN = 4
    LESS_OR_EQUAL = 5

    NAME_MAP = {
        EQUAL: "Equal",
        NOT_EQUAL: "Not Equal",
        GREATER_THAN: "Greater Than",
        GREATER_OR_EQUAL: "Greater or Equal",
        LESS_THAN: "Less Than",
        LESS_OR_EQUAL: "Less or Equal",
    }


class OperationEnumField(
    EnumField[OperationEnumAttrOperator, OperationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OperationEnumAttrOperator
    PLUG_CLS = OperationEnumPlugOperator


class _GeneratedCondition(DG):
    __slots__ = ()

    NODE_TYPE = "condition"

    operation = OperationEnumField(default_value=0)
    op = operation

    firstTerm = FloatField(default_value=0.0)
    ft = firstTerm

    secondTerm = FloatField(default_value=0.0)
    st = secondTerm

    colorIfTrue = ColorIfTrueField(default_value=(0.0, 0.0, 0.0))
    ct = colorIfTrue
    colorIfTrueR = colorIfTrue.colorIfTrueR
    ctr = colorIfTrueR
    colorIfTrueG = colorIfTrue.colorIfTrueG
    ctg = colorIfTrueG
    colorIfTrueB = colorIfTrue.colorIfTrueB
    ctb = colorIfTrueB

    colorIfFalse = ColorIfFalseField(default_value=(1.0, 1.0, 1.0))
    cf = colorIfFalse
    colorIfFalseR = colorIfFalse.colorIfFalseR
    cfr = colorIfFalseR
    colorIfFalseG = colorIfFalse.colorIfFalseG
    cfg = colorIfFalseG
    colorIfFalseB = colorIfFalse.colorIfFalseB
    cfb = colorIfFalseB

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB
