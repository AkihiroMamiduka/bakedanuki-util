# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.xgm_spline_base import InitDirectionField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class InterpFromEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CURRENT_DESCRIPTION = 0
    INTERPOLATION_SOURCE = 1


class InterpFromEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CURRENT_DESCRIPTION = 0
    INTERPOLATION_SOURCE = 1

    NAME_MAP = {
        CURRENT_DESCRIPTION: "Current Description",
        INTERPOLATION_SOURCE: "Interpolation Source",
    }


class InterpFromEnumField(
    EnumField[InterpFromEnumAttrOperator, InterpFromEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InterpFromEnumAttrOperator
    PLUG_CLS = InterpFromEnumPlugOperator


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


class XgmSplineBase(DG):
    __slots__ = ()

    NODE_TYPE = "xgmSplineBase"

    boundMesh = DataMeshField(multi=True)
    bm = boundMesh

    boundInfoData = TypedField()
    bid = boundInfoData

    resolution = LongField(multi=True)
    r = resolution

    densityMultiplier = FloatField()
    dm = densityMultiplier

    densityMask = DoubleField()
    dmk = densityMask

    generatorSeed = LongField()
    gs = generatorSeed

    interpolate = BoolField()
    i = interpolate

    interpFrom = InterpFromEnumField()
    if_ = interpFrom

    interpSource = TypedField()
    is_ = interpSource

    interpSmoothness = FloatField()
    ism = interpSmoothness

    initLength = DoubleLinearField()
    l = initLength

    initWidth = DoubleLinearField()
    w = initWidth

    initDirection = InitDirectionField()
    d = initDirection
    initDirectionX = initDirection.initDirectionX
    dx = initDirectionX
    initDirectionY = initDirection.initDirectionY
    dy = initDirectionY
    initDirectionZ = initDirection.initDirectionZ
    dz = initDirectionZ

    cachedInSplineData = TypedField()
    csd = cachedInSplineData

    outSplineData = TypedField()
    osd = outSplineData

    outMeshData = TypedField()
    omd = outMeshData

    cvCount = LongField()
    cvc = cvCount

    transferMode = BoolField()
    tmo = transferMode

    transferModeAlignToNormal = BoolField()
    tan = transferModeAlignToNormal

    transferModeMappingType = TransferModeMappingTypeEnumField()
    tmt = transferModeMappingType

    transferModeBBInfo = DataStringField()
    tbi = transferModeBBInfo
