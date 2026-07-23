# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class OutputTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NURBS = 0
    BEZIERS = 1


class OutputTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NURBS = 0
    BEZIERS = 1

    NAME_MAP = {
        NURBS: "NURBS",
        BEZIERS: "Beziers",
    }


class OutputTypeEnumField(
    EnumField[OutputTypeEnumAttrOperator, OutputTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputTypeEnumAttrOperator
    PLUG_CLS = OutputTypeEnumPlugOperator


class _GeneratedSubdivToNurbs(DG):
    __slots__ = ()

    NODE_TYPE = "subdivToNurbs"

    inSubdiv = TypedField(readable=False)
    i = inSubdiv

    outputSurfaces = DataNurbsSurfaceField(multi=True, writable=False)
    os = outputSurfaces

    outputType = OutputTypeEnumField(default_value=0)
    ot = outputType

    applyMatrixToResult = BoolField(default_value=True)
    amr = applyMatrixToResult
