# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_rbf_bend_twist_falloff_weight import (
    AxisQuatField,
    InputQuatField,
    PoseField,
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


class OrderEnumPlugOperator(EnumPlugOperator["OrderEnumAttrOperator"]):
    __slots__ = ()

    TWISTBEND = 0
    BENDTWIST = 1


class OrderEnumAttrOperator(EnumAttrOperator[OrderEnumPlugOperator]):
    __slots__ = ()

    TWISTBEND = 0
    BENDTWIST = 1

    NAME_MAP = {
        TWISTBEND: "TwistBend",
        BENDTWIST: "BendTwist",
    }


class OrderEnumField(EnumField[OrderEnumAttrOperator, OrderEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = OrderEnumAttrOperator
    PLUG_CLS = OrderEnumPlugOperator


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

    NAME_MAP = {
        SUCCESS: "Success",
        NOPOSES: "NoPoses",
        INVALIDRADIUS: "InvalidRadius",
        INVALIDQUATERNION: "InvalidQuaternion",
        UNSUPPORTEDFALLOFF: "UnsupportedFalloff",
        UNSUPPORTEDMODE: "UnsupportedMode",
        UNSUPPORTEDORDER: "UnsupportedOrder",
        NUMERICALFAILURE: "NumericalFailure",
    }


class FalloffStatusEnumField(
    EnumField[FalloffStatusEnumAttrOperator, FalloffStatusEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffStatusEnumAttrOperator
    PLUG_CLS = FalloffStatusEnumPlugOperator


class GeneratedBdRbfBendTwistFalloffWeight(DG):
    __slots__ = ()

    NODE_TYPE = "bdRbf_BendTwistFalloffWeight"

    inputQuat = InputQuatField(default_value=(0.0, 0.0, 0.0, 1.0))
    iq = inputQuat
    inputQuatX = inputQuat.inputQuatX
    iqx = inputQuatX
    inputQuatY = inputQuat.inputQuatY
    iqy = inputQuatY
    inputQuatZ = inputQuat.inputQuatZ
    iqz = inputQuatZ
    inputQuatW = inputQuat.inputQuatW
    iqw = inputQuatW

    axisQuat = AxisQuatField(default_value=(0.0, 0.0, 0.0, 1.0))
    aq = axisQuat
    axisQuatX = axisQuat.axisQuatX
    aqx = axisQuatX
    axisQuatY = axisQuat.axisQuatY
    aqy = axisQuatY
    axisQuatZ = axisQuat.axisQuatZ
    aqz = axisQuatZ
    axisQuatW = axisQuat.axisQuatW
    aqw = axisQuatW

    order = OrderEnumField(default_value=0)
    ord = order

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

    falloffStatus = FalloffStatusEnumField(default_value=1, writable=False)
    fs = falloffStatus
