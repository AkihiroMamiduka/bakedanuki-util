# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.dt.string import DataStringField


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


class _GeneratedAiMaterialx(DG):
    __slots__ = ()

    NODE_TYPE = "aiMaterialx"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    inputs = MessageField(multi=True)

    selection = DataStringField()

    filename = DataStringField()

    look = DataStringField()

    assignType = AssignTypeEnumField(default_value=0)
    assign_type = assignType

    assignMaterials = BoolField(default_value=True)
    assign_materials = assignMaterials

    assignProperties = BoolField(default_value=True)
    assign_properties = assignProperties

    assignVisibilities = BoolField(default_value=True)
    assign_visibilities = assignVisibilities
