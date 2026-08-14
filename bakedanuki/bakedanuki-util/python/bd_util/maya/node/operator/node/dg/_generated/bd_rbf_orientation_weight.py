# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_rbf_orientation_weight import (
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


class KernelEnumPlugOperator(EnumPlugOperator["KernelEnumAttrOperator"]):
    __slots__ = ()

    GAUSSIAN = 0
    EXPONENTIAL = 1
    LINEAR = 2
    COMPACTCUBIC = 3
    COMPACTQUINTIC = 4


class KernelEnumAttrOperator(EnumAttrOperator[KernelEnumPlugOperator]):
    __slots__ = ()

    GAUSSIAN = 0
    EXPONENTIAL = 1
    LINEAR = 2
    COMPACTCUBIC = 3
    COMPACTQUINTIC = 4

    NAME_MAP = {
        GAUSSIAN: "Gaussian",
        EXPONENTIAL: "Exponential",
        LINEAR: "Linear",
        COMPACTCUBIC: "CompactCubic",
        COMPACTQUINTIC: "CompactQuintic",
    }


class KernelEnumField(
    EnumField[KernelEnumAttrOperator, KernelEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KernelEnumAttrOperator
    PLUG_CLS = KernelEnumPlugOperator


class SolveStatusEnumPlugOperator(
    EnumPlugOperator["SolveStatusEnumAttrOperator"]
):
    __slots__ = ()

    SUCCESS = 0
    NOPOSES = 1
    INVALIDRADIUS = 2
    INVALIDREGULARIZATION = 3
    INVALIDQUATERNION = 4
    DUPLICATEPOSE = 5
    RANKDEFICIENT = 6
    NUMERICALFAILURE = 7
    UNSUPPORTEDKERNEL = 8


class SolveStatusEnumAttrOperator(
    EnumAttrOperator[SolveStatusEnumPlugOperator]
):
    __slots__ = ()

    SUCCESS = 0
    NOPOSES = 1
    INVALIDRADIUS = 2
    INVALIDREGULARIZATION = 3
    INVALIDQUATERNION = 4
    DUPLICATEPOSE = 5
    RANKDEFICIENT = 6
    NUMERICALFAILURE = 7
    UNSUPPORTEDKERNEL = 8

    NAME_MAP = {
        SUCCESS: "Success",
        NOPOSES: "NoPoses",
        INVALIDRADIUS: "InvalidRadius",
        INVALIDREGULARIZATION: "InvalidRegularization",
        INVALIDQUATERNION: "InvalidQuaternion",
        DUPLICATEPOSE: "DuplicatePose",
        RANKDEFICIENT: "RankDeficient",
        NUMERICALFAILURE: "NumericalFailure",
        UNSUPPORTEDKERNEL: "UnsupportedKernel",
    }


class SolveStatusEnumField(
    EnumField[SolveStatusEnumAttrOperator, SolveStatusEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SolveStatusEnumAttrOperator
    PLUG_CLS = SolveStatusEnumPlugOperator


class GeneratedBdRbfOrientationWeight(DG):
    __slots__ = ()

    NODE_TYPE = "bdRbf_OrientationWeight"

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

    pose = PoseField(multi=True)
    p = pose

    kernel = KernelEnumField(default_value=4)
    k = kernel

    radius = DoubleAngleField(default_value=59.99999999999999)
    rad = radius

    regularization = DoubleField(default_value=1e-08, min_value=0.0)
    reg = regularization

    allowNegativeWeights = BoolField(default_value=False)
    anw = allowNegativeWeights

    outputWeight = DoubleField(multi=True, default_value=0.0, writable=False)
    ow = outputWeight

    isValid = BoolField(default_value=False, writable=False)
    iv = isValid

    solveStatus = SolveStatusEnumField(default_value=1, writable=False)
    ss = solveStatus
