# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField


class RepresentationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    A = 1
    LA = 2
    RGB = 3
    RGBA = 4


class RepresentationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    A = 1
    LA = 2
    RGB = 3
    RGBA = 4

    NAME_MAP = {
        A: "A",
        LA: "LA",
        RGB: "RGB",
        RGBA: "RGBA",
    }


class RepresentationEnumField(
    EnumField[RepresentationEnumAttrOperator, RepresentationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RepresentationEnumAttrOperator
    PLUG_CLS = RepresentationEnumPlugOperator


class CreateColorSet(DG):
    __slots__ = ()

    NODE_TYPE = "createColorSet"

    inputGeometry = TypedField()
    ig = inputGeometry

    outputGeometry = TypedField()
    og = outputGeometry

    colorSetName = DataStringField()
    colos = colorSetName

    clamped = BoolField(default_value=True)
    clam = clamped

    representation = RepresentationEnumField(default_value=4)
    rprt = representation
