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

    inSplineData = TypedField()
    isd = inSplineData

    outSplineData = TypedField()
    osd = outSplineData

    mute = BoolField()
    m = mute

    inWireData = TypedField()
    iwd = inWireData

    mask = DoubleField()
    mk = mask

    magnitude = DoubleField()
    mg = magnitude

    magnitudeScale = MagnitudeScaleField(multi=True)
    ms = magnitudeScale

    smoothness = DoubleField()
    s = smoothness

    breakage = DoubleField()
    b = breakage

    refWire = TypedField()
    rw = refWire

    transferMode = BoolField()
    tmo = transferMode

    transferModeAlignToNormal = BoolField()
    tan = transferModeAlignToNormal

    transferModeMappingType = TransferModeMappingTypeEnumField()
    tmt = transferModeMappingType
