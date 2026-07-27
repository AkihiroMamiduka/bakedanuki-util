# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.xgm_spline_base import InitDirectionField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


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


class GeneratedXgmSplineBase(DG):
    __slots__ = ()

    NODE_TYPE = "xgmSplineBase"

    boundMesh = DataMeshField(multi=True)
    bm = boundMesh

    boundInfoData = TypedField()
    bid = boundInfoData

    resolution = LongField(multi=True, default_value=3, min_value=1, max_value=5)
    r = resolution

    densityMultiplier = FloatField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=100.0)
    dm = densityMultiplier

    densityMask = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    dmk = densityMask

    generatorSeed = LongField(default_value=0, min_value=0)
    gs = generatorSeed

    interpolate = BoolField(default_value=True)
    i = interpolate

    interpFrom = InterpFromEnumField(default_value=0)
    if_ = interpFrom

    interpSource = TypedField()
    is_ = interpSource

    interpSmoothness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    ism = interpSmoothness

    initLength = DoubleLinearField(default_value=1.0, min_value=0.001)
    l = initLength

    initWidth = DoubleLinearField(default_value=0.01, min_value=0.001)
    w = initWidth

    initDirection = InitDirectionField(default_value=(0.0, 0.0, 0.0), writable=False)
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

    cvCount = LongField(default_value=5, min_value=4, max_value=100000)
    cvc = cvCount

    transferMode = BoolField(default_value=False)
    tmo = transferMode

    transferModeAlignToNormal = BoolField(default_value=False)
    tan = transferModeAlignToNormal

    transferModeMappingType = TransferModeMappingTypeEnumField(default_value=0)
    tmt = transferModeMappingType

    transferModeBBInfo = DataStringField()
    tbi = transferModeBBInfo
