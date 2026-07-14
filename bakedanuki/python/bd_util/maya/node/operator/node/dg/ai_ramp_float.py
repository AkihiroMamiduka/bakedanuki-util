# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_ramp_float import (
    OutTransparencyField,
    RampField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class TypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CUSTOM = 0
    U = 1
    V = 2
    DIAGONAL = 3
    RADIAL = 4
    CIRCULAR = 5
    BOX = 6
    TIME = 7


class TypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CUSTOM = 0
    U = 1
    V = 2
    DIAGONAL = 3
    RADIAL = 4
    CIRCULAR = 5
    BOX = 6
    TIME = 7

    NAME_MAP = {
        CUSTOM: "custom",
        U: "u",
        V: "v",
        DIAGONAL: "diagonal",
        RADIAL: "radial",
        CIRCULAR: "circular",
        BOX: "box",
        TIME: "time",
    }


class TypeEnumField(
    EnumField[TypeEnumAttrOperator, TypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TypeEnumAttrOperator
    PLUG_CLS = TypeEnumPlugOperator


class UseImplicitUvsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1
    CURVES_ONLY = 2


class UseImplicitUvsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1
    CURVES_ONLY = 2

    NAME_MAP = {
        OFF: "off",
        ON: "on",
        CURVES_ONLY: "curves_only",
    }


class UseImplicitUvsEnumField(
    EnumField[UseImplicitUvsEnumAttrOperator, UseImplicitUvsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UseImplicitUvsEnumAttrOperator
    PLUG_CLS = UseImplicitUvsEnumPlugOperator


class AiRampFloat(DG):
    __slots__ = ()

    NODE_TYPE = "aiRampFloat"

    outValue = FloatField(default_value=0.0, writable=False)
    out = outValue

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    type = TypeEnumField(default_value=2)

    input = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    uvset = DataStringField()

    useImplicitUvs = UseImplicitUvsEnumField(default_value=0)
    use_implicit_uvs = useImplicitUvs

    wrapUvs = BoolField(default_value=False)
    wrap_uvs = wrapUvs

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    ramp = RampField(multi=True, default_value=(0.0, 0.0, 1.0), category="arnold")
    aiRamp = ramp
