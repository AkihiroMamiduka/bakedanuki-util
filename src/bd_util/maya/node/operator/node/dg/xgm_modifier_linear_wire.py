# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.xgm_modifier_linear_wire import MagnitudeScaleField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.typed import TypedField


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


class XgmModifierLinearWire(DG):
    __slots__ = ()

    NODE_TYPE = "xgmModifierLinearWire"

    inSplineData = TypedField(readable=False)
    isd = inSplineData

    outSplineData = TypedField(writable=False)
    osd = outSplineData

    mute = BoolField(default_value=False)
    m = mute

    inWireData = TypedField()
    iwd = inWireData

    mask = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    mk = mask

    magnitude = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    mg = magnitude

    magnitudeScale = MagnitudeScaleField(multi=True, default_value=(0.0, 0.0, 1.0))
    ms = magnitudeScale

    smoothness = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    s = smoothness

    breakage = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    b = breakage

    refWire = TypedField()
    rw = refWire

    transferMode = BoolField(default_value=False)
    tmo = transferMode

    transferModeAlignToNormal = BoolField(default_value=False)
    tan = transferModeAlignToNormal

    transferModeMappingType = TransferModeMappingTypeEnumField(default_value=0)
    tmt = transferModeMappingType
