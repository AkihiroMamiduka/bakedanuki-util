# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class ExtensionTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TANGENT = 0
    EXTRAPOLATE = 2


class ExtensionTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TANGENT = 0
    EXTRAPOLATE = 2

    NAME_MAP = {
        TANGENT: "Tangent",
        EXTRAPOLATE: "Extrapolate",
    }


class ExtensionTypeEnumField(
    EnumField[ExtensionTypeEnumAttrOperator, ExtensionTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExtensionTypeEnumAttrOperator
    PLUG_CLS = ExtensionTypeEnumPlugOperator


class ExtendMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DISTANCE = 0


class ExtendMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DISTANCE = 0

    NAME_MAP = {
        DISTANCE: "Distance",
    }


class ExtendMethodEnumField(
    EnumField[ExtendMethodEnumAttrOperator, ExtendMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExtendMethodEnumAttrOperator
    PLUG_CLS = ExtendMethodEnumPlugOperator


class ExtendSideEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    END = 0
    START = 1
    BOTH = 2


class ExtendSideEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    END = 0
    START = 1
    BOTH = 2

    NAME_MAP = {
        END: "End",
        START: "Start",
        BOTH: "Both",
    }


class ExtendSideEnumField(
    EnumField[ExtendSideEnumAttrOperator, ExtendSideEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExtendSideEnumAttrOperator
    PLUG_CLS = ExtendSideEnumPlugOperator


class ExtendDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    U = 0
    V = 1
    BOTH = 2


class ExtendDirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    U = 0
    V = 1
    BOTH = 2

    NAME_MAP = {
        U: "U",
        V: "V",
        BOTH: "Both",
    }


class ExtendDirectionEnumField(
    EnumField[ExtendDirectionEnumAttrOperator, ExtendDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExtendDirectionEnumAttrOperator
    PLUG_CLS = ExtendDirectionEnumPlugOperator


class ExtendSurface(DG):
    __slots__ = ()

    NODE_TYPE = "extendSurface"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    targetObject = DataNurbsSurfaceField()
    to = targetObject

    extensionType = ExtensionTypeEnumField()
    et = extensionType

    extendMethod = ExtendMethodEnumField()
    em = extendMethod

    extendSide = ExtendSideEnumField()
    es = extendSide

    extendDirection = ExtendDirectionEnumField()
    ed = extendDirection

    join = BoolField()
    jn = join

    distance = DoubleLinearField()
    d = distance

    outputSurface = DataNurbsSurfaceField()
    oc = outputSurface
