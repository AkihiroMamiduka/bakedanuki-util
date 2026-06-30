# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.condition import (
    ColorIfFalseField,
    ColorIfTrueField,
    OutColorField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


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


class Condition(DG):
    __slots__ = ()

    NODE_TYPE = "condition"

    operation = OperationEnumField()
    op = operation

    firstTerm = FloatField()
    ft = firstTerm

    secondTerm = FloatField()
    st = secondTerm

    colorIfTrue = ColorIfTrueField()
    ct = colorIfTrue
    colorIfTrueR = colorIfTrue.colorIfTrueR
    ctr = colorIfTrueR
    colorIfTrueG = colorIfTrue.colorIfTrueG
    ctg = colorIfTrueG
    colorIfTrueB = colorIfTrue.colorIfTrueB
    ctb = colorIfTrueB

    colorIfFalse = ColorIfFalseField()
    cf = colorIfFalse
    colorIfFalseR = colorIfFalse.colorIfFalseR
    cfr = colorIfFalseR
    colorIfFalseG = colorIfFalse.colorIfFalseG
    cfg = colorIfFalseG
    colorIfFalseB = colorIfFalse.colorIfFalseB
    cfb = colorIfFalseB

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB
