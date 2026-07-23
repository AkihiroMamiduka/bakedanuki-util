# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.dt.matrix import DataMatrixField


class FreezeNormalsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NEVER = 0
    ALWAYS = 1
    NON_MINUS_RIGID_TRANSFORMATIONS_ONLY = 2


class FreezeNormalsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NEVER = 0
    ALWAYS = 1
    NON_MINUS_RIGID_TRANSFORMATIONS_ONLY = 2

    NAME_MAP = {
        NEVER: "Never",
        ALWAYS: "Always",
        NON_MINUS_RIGID_TRANSFORMATIONS_ONLY: "Non-rigid Transformations Only",
    }


class FreezeNormalsEnumField(
    EnumField[FreezeNormalsEnumAttrOperator, FreezeNormalsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FreezeNormalsEnumAttrOperator
    PLUG_CLS = FreezeNormalsEnumPlugOperator


class _GeneratedTransformGeometry(DG):
    __slots__ = ()

    NODE_TYPE = "transformGeometry"

    inputGeometry = GenericField()
    ig = inputGeometry

    transform = DataMatrixField()
    txf = transform

    invertTransform = BoolField(default_value=False)
    itf = invertTransform

    freezeNormals = FreezeNormalsEnumField(default_value=0)
    fn = freezeNormals

    outputGeometry = GenericField(writable=False)
    og = outputGeometry

    reverseNormals = BoolField(default_value=False)
    rn = reverseNormals
