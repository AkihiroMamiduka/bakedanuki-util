# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.xgm_modifier_sculpt import (
    TweakGroupsField,
    TweaksField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string_array import DataStringArrayField


class TransferModeMappingTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    POSITION_BASED = 0
    UV_BASED = 1


class TransferModeMappingTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    POSITION_BASED = 0
    UV_BASED = 1

    NAME_MAP = {
        POSITION_BASED: "Position Based",
        UV_BASED: "UV Based",
    }


class TransferModeMappingTypeEnumField(
    EnumField[TransferModeMappingTypeEnumAttrOperator, TransferModeMappingTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransferModeMappingTypeEnumAttrOperator
    PLUG_CLS = TransferModeMappingTypeEnumPlugOperator


class XgmModifierSculpt(DG):
    __slots__ = ()

    NODE_TYPE = "xgmModifierSculpt"

    inSplineData = TypedField()
    isd = inSplineData

    outSplineData = TypedField()
    osd = outSplineData

    mute = BoolField()
    m = mute

    tweaks = TweaksField(multi=True)
    ts = tweaks

    groups = DataStringArrayField()
    gs = groups

    tweakGroups = TweakGroupsField(multi=True)
    tg = tweakGroups

    activeTweak = LongField()
    a = activeTweak

    mask = FloatField()
    mk = mask

    transferMode = BoolField()
    tmo = transferMode

    transferModeAlignToNormal = BoolField()
    tan = transferModeAlignToNormal

    transferModeMappingType = TransferModeMappingTypeEnumField()
    tmt = transferModeMappingType
