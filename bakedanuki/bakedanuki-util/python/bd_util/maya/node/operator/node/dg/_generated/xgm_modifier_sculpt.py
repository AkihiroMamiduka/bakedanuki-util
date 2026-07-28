# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.xgm_modifier_sculpt import (
    TweakGroupsField,
    TweaksField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string_array import DataStringArrayField


class TransferModeMappingTypeEnumPlugOperator(EnumPlugOperator["TransferModeMappingTypeEnumAttrOperator"]):
    __slots__ = ()

    POSITION_BASED = 0
    UV_BASED = 1


class TransferModeMappingTypeEnumAttrOperator(EnumAttrOperator[TransferModeMappingTypeEnumPlugOperator]):
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


class GeneratedXgmModifierSculpt(DG):
    __slots__ = ()

    NODE_TYPE = "xgmModifierSculpt"

    inSplineData = TypedField(readable=False)
    isd = inSplineData

    outSplineData = TypedField(writable=False)
    osd = outSplineData

    mute = BoolField(default_value=False)
    m = mute

    tweaks = TweaksField(multi=True)
    ts = tweaks

    groups = DataStringArrayField()
    gs = groups

    tweakGroups = TweakGroupsField(multi=True)
    tg = tweakGroups

    activeTweak = LongField(default_value=1, min_value=1)
    a = activeTweak

    mask = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    mk = mask

    transferMode = BoolField(default_value=False)
    tmo = transferMode

    transferModeAlignToNormal = BoolField(default_value=False)
    tan = transferModeAlignToNormal

    transferModeMappingType = TransferModeMappingTypeEnumField(default_value=0)
    tmt = transferModeMappingType
