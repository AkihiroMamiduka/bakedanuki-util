# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_rbf_position_falloff_weight import (
    InputPositionField,
    PoseField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)


class FalloffEnumPlugOperator(EnumPlugOperator["FalloffEnumAttrOperator"]):
    __slots__ = ()

    LINEAR = 0
    COMPACTCUBIC = 1
    COMPACTQUINTIC = 2


class FalloffEnumAttrOperator(EnumAttrOperator[FalloffEnumPlugOperator]):
    __slots__ = ()

    LINEAR = 0
    COMPACTCUBIC = 1
    COMPACTQUINTIC = 2

    NAME_MAP = {
        LINEAR: "Linear",
        COMPACTCUBIC: "CompactCubic",
        COMPACTQUINTIC: "CompactQuintic",
    }


class FalloffEnumField(
    EnumField[FalloffEnumAttrOperator, FalloffEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffEnumAttrOperator
    PLUG_CLS = FalloffEnumPlugOperator


class FalloffStatusEnumPlugOperator(
    EnumPlugOperator["FalloffStatusEnumAttrOperator"]
):
    __slots__ = ()

    SUCCESS = 0
    NOPOSES = 1
    INVALIDRADIUS = 2
    INVALIDPOSITION = 3
    UNSUPPORTEDFALLOFF = 4
    NUMERICALFAILURE = 5


class FalloffStatusEnumAttrOperator(
    EnumAttrOperator[FalloffStatusEnumPlugOperator]
):
    __slots__ = ()

    SUCCESS = 0
    NOPOSES = 1
    INVALIDRADIUS = 2
    INVALIDPOSITION = 3
    UNSUPPORTEDFALLOFF = 4
    NUMERICALFAILURE = 5

    NAME_MAP = {
        SUCCESS: "Success",
        NOPOSES: "NoPoses",
        INVALIDRADIUS: "InvalidRadius",
        INVALIDPOSITION: "InvalidPosition",
        UNSUPPORTEDFALLOFF: "UnsupportedFalloff",
        NUMERICALFAILURE: "NumericalFailure",
    }


class FalloffStatusEnumField(
    EnumField[FalloffStatusEnumAttrOperator, FalloffStatusEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffStatusEnumAttrOperator
    PLUG_CLS = FalloffStatusEnumPlugOperator


class GeneratedBdRbfPositionFalloffWeight(DG):
    __slots__ = ()

    NODE_TYPE = "bdRbf_PositionFalloffWeight"

    inputPosition = InputPositionField(default_value=(0.0, 0.0, 0.0))
    ip = inputPosition
    inputPositionX = inputPosition.inputPositionX
    ipx = inputPositionX
    inputPositionY = inputPosition.inputPositionY
    ipy = inputPositionY
    inputPositionZ = inputPosition.inputPositionZ
    ipz = inputPositionZ

    innerRadius = DoubleLinearField(default_value=0.0, min_value=0.0)
    inr = innerRadius

    outerRadius = DoubleLinearField(default_value=1.0, min_value=0.0)
    outr = outerRadius

    falloff = FalloffEnumField(default_value=2)
    fo = falloff

    pose = PoseField(multi=True)
    p = pose

    outputWeight = DoubleField(multi=True, default_value=0.0, writable=False)
    ow = outputWeight

    isValid = BoolField(default_value=False, writable=False)
    iv = isValid

    falloffStatus = FalloffStatusEnumField(default_value=1, writable=False)
    fs = falloffStatus
