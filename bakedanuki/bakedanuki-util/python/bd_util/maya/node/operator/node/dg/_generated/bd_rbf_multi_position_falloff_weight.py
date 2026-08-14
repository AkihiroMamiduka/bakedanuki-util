# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_rbf_multi_position_falloff_weight import (
    PoseField,
    SourceField,
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
    NOSOURCES = 6
    INVALIDINFLUENCE = 7
    INCOMPLETEPOSE = 8


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
    NOSOURCES = 6
    INVALIDINFLUENCE = 7
    INCOMPLETEPOSE = 8

    NAME_MAP = {
        SUCCESS: "Success",
        NOPOSES: "NoPoses",
        INVALIDRADIUS: "InvalidRadius",
        INVALIDPOSITION: "InvalidPosition",
        UNSUPPORTEDFALLOFF: "UnsupportedFalloff",
        NUMERICALFAILURE: "NumericalFailure",
        NOSOURCES: "NoSources",
        INVALIDINFLUENCE: "InvalidInfluence",
        INCOMPLETEPOSE: "IncompletePose",
    }


class FalloffStatusEnumField(
    EnumField[FalloffStatusEnumAttrOperator, FalloffStatusEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffStatusEnumAttrOperator
    PLUG_CLS = FalloffStatusEnumPlugOperator


class GeneratedBdRbfMultiPositionFalloffWeight(DG):
    __slots__ = ()

    NODE_TYPE = "bdRbf_MultiPositionFalloffWeight"

    source = SourceField(multi=True)
    src = source

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

    falloffStatus = FalloffStatusEnumField(default_value=6, writable=False)
    fs = falloffStatus
