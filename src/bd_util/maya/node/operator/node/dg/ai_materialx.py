# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.dt.string import DataStringField


class AssignTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LOOK = 0
    MATERIAL = 1


class AssignTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LOOK = 0
    MATERIAL = 1

    NAME_MAP = {
        LOOK: "look",
        MATERIAL: "material",
    }


class AssignTypeEnumField(
    EnumField[AssignTypeEnumAttrOperator, AssignTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AssignTypeEnumAttrOperator
    PLUG_CLS = AssignTypeEnumPlugOperator


class AiMaterialx(DG):
    __slots__ = ()

    NODE_TYPE = "aiMaterialx"

    out = MessageField()

    enable = BoolField()

    inputs = MessageField(multi=True)

    selection = DataStringField()

    filename = DataStringField()

    look = DataStringField()

    assignType = AssignTypeEnumField()
    assign_type = assignType

    assignMaterials = BoolField()
    assign_materials = assignMaterials

    assignProperties = BoolField()
    assign_properties = assignProperties

    assignVisibilities = BoolField()
    assign_visibilities = assignVisibilities
