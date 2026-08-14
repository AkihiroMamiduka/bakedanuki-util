# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_rbf_multi_bend_twist_falloff_weight import (
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
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class ModeEnumPlugOperator(EnumPlugOperator["ModeEnumAttrOperator"]):
    __slots__ = ()

    BENDTWIST = 0
    BENDONLY = 1


class ModeEnumAttrOperator(EnumAttrOperator[ModeEnumPlugOperator]):
    __slots__ = ()

    BENDTWIST = 0
    BENDONLY = 1

    NAME_MAP = {
        BENDTWIST: "BendTwist",
        BENDONLY: "BendOnly",
    }


class ModeEnumField(EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


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
    INVALIDQUATERNION = 3
    UNSUPPORTEDFALLOFF = 4
    UNSUPPORTEDMODE = 5
    UNSUPPORTEDORDER = 6
    NUMERICALFAILURE = 7
    NOSOURCES = 8
    INVALIDINFLUENCE = 9
    INCOMPLETEPOSE = 10


class FalloffStatusEnumAttrOperator(
    EnumAttrOperator[FalloffStatusEnumPlugOperator]
):
    __slots__ = ()

    SUCCESS = 0
    NOPOSES = 1
    INVALIDRADIUS = 2
    INVALIDQUATERNION = 3
    UNSUPPORTEDFALLOFF = 4
    UNSUPPORTEDMODE = 5
    UNSUPPORTEDORDER = 6
    NUMERICALFAILURE = 7
    NOSOURCES = 8
    INVALIDINFLUENCE = 9
    INCOMPLETEPOSE = 10

    NAME_MAP = {
        SUCCESS: "Success",
        NOPOSES: "NoPoses",
        INVALIDRADIUS: "InvalidRadius",
        INVALIDQUATERNION: "InvalidQuaternion",
        UNSUPPORTEDFALLOFF: "UnsupportedFalloff",
        UNSUPPORTEDMODE: "UnsupportedMode",
        UNSUPPORTEDORDER: "UnsupportedOrder",
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


class GeneratedBdRbfMultiBendTwistFalloffWeight(DG):
    __slots__ = ()

    NODE_TYPE = "bdRbf_MultiBendTwistFalloffWeight"

    source = SourceField(multi=True)
    src = source

    mode = ModeEnumField(default_value=0)
    md = mode

    bendInnerRadius = DoubleAngleField(default_value=0.0, min_value=0.0)
    bir = bendInnerRadius

    bendOuterRadius = DoubleAngleField(
        default_value=59.99999999999999, min_value=0.0
    )
    bor = bendOuterRadius

    twistInnerRadius = DoubleAngleField(default_value=0.0, min_value=0.0)
    tir = twistInnerRadius

    twistOuterRadius = DoubleAngleField(
        default_value=59.99999999999999, min_value=0.0
    )
    tor = twistOuterRadius

    falloff = FalloffEnumField(default_value=2)
    fo = falloff

    pose = PoseField(multi=True)
    p = pose

    outputWeight = DoubleField(multi=True, default_value=0.0, writable=False)
    ow = outputWeight

    isValid = BoolField(default_value=False, writable=False)
    iv = isValid

    falloffStatus = FalloffStatusEnumField(default_value=8, writable=False)
    fs = falloffStatus
