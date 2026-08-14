# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_rbf_multi_position_weight import (
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
    INVALIDPOSITION = 4
    DUPLICATEPOSE = 5
    RANKDEFICIENT = 6
    NUMERICALFAILURE = 7
    UNSUPPORTEDKERNEL = 8
    NOSOURCES = 10
    INVALIDINFLUENCE = 11
    INCOMPLETEPOSE = 12


class SolveStatusEnumAttrOperator(
    EnumAttrOperator[SolveStatusEnumPlugOperator]
):
    __slots__ = ()

    SUCCESS = 0
    NOPOSES = 1
    INVALIDRADIUS = 2
    INVALIDREGULARIZATION = 3
    INVALIDPOSITION = 4
    DUPLICATEPOSE = 5
    RANKDEFICIENT = 6
    NUMERICALFAILURE = 7
    UNSUPPORTEDKERNEL = 8
    NOSOURCES = 10
    INVALIDINFLUENCE = 11
    INCOMPLETEPOSE = 12

    NAME_MAP = {
        SUCCESS: "Success",
        NOPOSES: "NoPoses",
        INVALIDRADIUS: "InvalidRadius",
        INVALIDREGULARIZATION: "InvalidRegularization",
        INVALIDPOSITION: "InvalidPosition",
        DUPLICATEPOSE: "DuplicatePose",
        RANKDEFICIENT: "RankDeficient",
        NUMERICALFAILURE: "NumericalFailure",
        UNSUPPORTEDKERNEL: "UnsupportedKernel",
        NOSOURCES: "NoSources",
        INVALIDINFLUENCE: "InvalidInfluence",
        INCOMPLETEPOSE: "IncompletePose",
    }


class SolveStatusEnumField(
    EnumField[SolveStatusEnumAttrOperator, SolveStatusEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SolveStatusEnumAttrOperator
    PLUG_CLS = SolveStatusEnumPlugOperator


class GeneratedBdRbfMultiPositionWeight(DG):
    __slots__ = ()

    NODE_TYPE = "bdRbf_MultiPositionWeight"

    source = SourceField(multi=True)
    src = source

    pose = PoseField(multi=True)
    p = pose

    kernel = KernelEnumField(default_value=4)
    k = kernel

    radius = DoubleLinearField(default_value=1.0, min_value=0.0)
    rad = radius

    regularization = DoubleField(default_value=1e-08, min_value=0.0)
    reg = regularization

    allowNegativeWeights = BoolField(default_value=False)
    anw = allowNegativeWeights

    outputWeight = DoubleField(multi=True, default_value=0.0, writable=False)
    ow = outputWeight

    isValid = BoolField(default_value=False, writable=False)
    iv = isValid

    solveStatus = SolveStatusEnumField(default_value=10, writable=False)
    ss = solveStatus
