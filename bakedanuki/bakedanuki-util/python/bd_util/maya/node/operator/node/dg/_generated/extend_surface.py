# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


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


class GeneratedExtendSurface(DG):
    __slots__ = ()

    NODE_TYPE = "extendSurface"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    targetObject = DataNurbsSurfaceField()
    to = targetObject

    extensionType = ExtensionTypeEnumField(default_value=0)
    et = extensionType

    extendMethod = ExtendMethodEnumField(default_value=0)
    em = extendMethod

    extendSide = ExtendSideEnumField(default_value=1)
    es = extendSide

    extendDirection = ExtendDirectionEnumField(default_value=0)
    ed = extendDirection

    join = BoolField(default_value=True)
    jn = join

    distance = DoubleLinearField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    d = distance

    outputSurface = DataNurbsSurfaceField(writable=False)
    oc = outputSurface
