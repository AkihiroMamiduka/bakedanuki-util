# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class PositionalContinuityTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MOVE_FIRST = 1
    MOVE_SECOND = 2
    MOVE_BOTH = 3
    MODIFY_FIRST = 4
    MODIFY_SECOND = 5
    MODIFY_BOTH = 6


class PositionalContinuityTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MOVE_FIRST = 1
    MOVE_SECOND = 2
    MOVE_BOTH = 3
    MODIFY_FIRST = 4
    MODIFY_SECOND = 5
    MODIFY_BOTH = 6

    NAME_MAP = {
        MOVE_FIRST: "Move First",
        MOVE_SECOND: "Move Second",
        MOVE_BOTH: "Move Both",
        MODIFY_FIRST: "Modify First",
        MODIFY_SECOND: "Modify Second",
        MODIFY_BOTH: "Modify Both",
    }


class PositionalContinuityTypeEnumField(
    EnumField[PositionalContinuityTypeEnumAttrOperator, PositionalContinuityTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionalContinuityTypeEnumAttrOperator
    PLUG_CLS = PositionalContinuityTypeEnumPlugOperator


class TangentContinuityTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FIRST = 1
    SECOND = 2


class TangentContinuityTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FIRST = 1
    SECOND = 2

    NAME_MAP = {
        FIRST: "First",
        SECOND: "Second",
    }


class TangentContinuityTypeEnumField(
    EnumField[TangentContinuityTypeEnumAttrOperator, TangentContinuityTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentContinuityTypeEnumAttrOperator
    PLUG_CLS = TangentContinuityTypeEnumPlugOperator


class AlignSurface(DG):
    __slots__ = ()

    NODE_TYPE = "alignSurface"

    inputSurface1 = DataNurbsSurfaceField()
    is1 = inputSurface1

    inputSurface2 = DataNurbsSurfaceField()
    is2 = inputSurface2

    outputSurface1 = DataNurbsSurfaceField()
    os1 = outputSurface1

    outputSurface2 = DataNurbsSurfaceField()
    os2 = outputSurface2

    tangentScale1 = DoubleField()
    ts1 = tangentScale1

    tangentScale2 = DoubleField()
    ts2 = tangentScale2

    curvatureScale1 = DoubleField()
    cs1 = curvatureScale1

    curvatureScale2 = DoubleField()
    cs2 = curvatureScale2

    positionalContinuityType = PositionalContinuityTypeEnumField()
    pct = positionalContinuityType

    tangentContinuityType = TangentContinuityTypeEnumField()
    tct = tangentContinuityType

    joinParameter = FloatField()
    jnp = joinParameter

    twist = BoolField()
    tw = twist

    reverse1 = BoolField()
    rv1 = reverse1

    reverse2 = BoolField()
    rv2 = reverse2

    swap1 = BoolField()
    sw1 = swap1

    swap2 = BoolField()
    sw2 = swap2

    attach = BoolField()
    at = attach

    keepMultipleKnots = BoolField()
    kmk = keepMultipleKnots

    positionalContinuity = BoolField()
    pc = positionalContinuity

    tangentContinuity = BoolField()
    tc = tangentContinuity

    curvatureContinuity = BoolField()
    cc = curvatureContinuity

    directionU = BoolField()
    du = directionU
