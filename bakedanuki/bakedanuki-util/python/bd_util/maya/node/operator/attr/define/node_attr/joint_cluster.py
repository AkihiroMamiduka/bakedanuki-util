# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.at.typed import TypedField
from ..std.dt.matrix import DataMatrixField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.long_compound.long3_compound._base import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class InputPlugOperator(CompoundPlugOperator["InputAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputGeometry", "ig"),
        ("groupId", "gi"),
        ("componentTagExpression", "gtg"),
    )

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField(default_value=0)
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputAttrOperator(CompoundAttrOperator[InputPlugOperator]):
    __slots__ = ()

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField(default_value=0)
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputField(CompoundField[InputAttrOperator, InputPlugOperator]):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator


class EnvelopeWeightsListPlugOperator(
    CompoundPlugOperator["EnvelopeWeightsListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("envelopeWeights", "owt"),)

    envelopeWeights = FloatField(multi=True, default_value=1.0, writable=False)
    owt = envelopeWeights


class EnvelopeWeightsListAttrOperator(
    CompoundAttrOperator[EnvelopeWeightsListPlugOperator]
):
    __slots__ = ()

    envelopeWeights = FloatField(multi=True, default_value=1.0, writable=False)
    owt = envelopeWeights


class EnvelopeWeightsListField(
    CompoundField[
        EnvelopeWeightsListAttrOperator, EnvelopeWeightsListPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = EnvelopeWeightsListAttrOperator
    PLUG_CLS = EnvelopeWeightsListPlugOperator


class FunctionPlugOperator(
    Long3CompoundBasePlugOperator["FunctionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fchild1", "f1"),
        ("fchild2", "f2"),
        ("fchild3", "f3"),
    )

    fchild1 = LongField(default_value=0, readable=False)
    f1 = fchild1

    fchild2 = LongField(default_value=0, readable=False)
    f2 = fchild2

    fchild3 = LongField(default_value=0, readable=False)
    f3 = fchild3


class FunctionAttrOperator(
    Long3CompoundBaseAttrOperator[FunctionPlugOperator]
):
    __slots__ = ()

    fchild1 = LongField(default_value=0, readable=False)
    f1 = fchild1

    fchild2 = LongField(default_value=0, readable=False)
    f2 = fchild2

    fchild3 = LongField(default_value=0, readable=False)
    f3 = fchild3


class FunctionField(
    Long3CompoundBaseField[FunctionAttrOperator, FunctionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FunctionAttrOperator
    PLUG_CLS = FunctionPlugOperator

    fchild1 = LongField(default_value=0, readable=False)
    f1 = fchild1

    fchild2 = LongField(default_value=0, readable=False)
    f2 = fchild2

    fchild3 = LongField(default_value=0, readable=False)
    f3 = fchild3


class WeightListPlugOperator(CompoundPlugOperator["WeightListAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("weights", "wl.w"),)

    weights = FloatField(multi=True, default_value=1.0)


class WeightListAttrOperator(CompoundAttrOperator[WeightListPlugOperator]):
    __slots__ = ()

    weights = FloatField(multi=True, default_value=1.0)


class WeightListField(
    CompoundField[WeightListAttrOperator, WeightListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListAttrOperator
    PLUG_CLS = WeightListPlugOperator


class ClusterXformsPlugOperator(
    CompoundPlugOperator["ClusterXformsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("preMatrix", "pre"),
        ("weightedMatrix", "wt"),
        ("postMatrix", "post"),
    )

    preMatrix = DataMatrixField()
    pre = preMatrix

    weightedMatrix = DataMatrixField()
    wt = weightedMatrix

    postMatrix = DataMatrixField()
    post = postMatrix


class ClusterXformsAttrOperator(
    CompoundAttrOperator[ClusterXformsPlugOperator]
):
    __slots__ = ()

    preMatrix = DataMatrixField()
    pre = preMatrix

    weightedMatrix = DataMatrixField()
    wt = weightedMatrix

    postMatrix = DataMatrixField()
    post = postMatrix


class ClusterXformsField(
    CompoundField[ClusterXformsAttrOperator, ClusterXformsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClusterXformsAttrOperator
    PLUG_CLS = ClusterXformsPlugOperator

    preMatrix = DataMatrixField()
    pre = preMatrix

    weightedMatrix = DataMatrixField()
    wt = weightedMatrix

    postMatrix = DataMatrixField()
    post = postMatrix


class ChildJointClusterXformsPlugOperator(
    CompoundPlugOperator["ChildJointClusterXformsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("childJointPreMatrix", "cpr"),
        ("childJointWeightedMatrix", "cjw"),
        ("childJointPostMatrix", "cpo"),
    )

    childJointPreMatrix = DataMatrixField()
    cpr = childJointPreMatrix

    childJointWeightedMatrix = DataMatrixField()
    cjw = childJointWeightedMatrix

    childJointPostMatrix = DataMatrixField()
    cpo = childJointPostMatrix


class ChildJointClusterXformsAttrOperator(
    CompoundAttrOperator[ChildJointClusterXformsPlugOperator]
):
    __slots__ = ()

    childJointPreMatrix = DataMatrixField()
    cpr = childJointPreMatrix

    childJointWeightedMatrix = DataMatrixField()
    cjw = childJointWeightedMatrix

    childJointPostMatrix = DataMatrixField()
    cpo = childJointPostMatrix


class ChildJointClusterXformsField(
    CompoundField[
        ChildJointClusterXformsAttrOperator,
        ChildJointClusterXformsPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ChildJointClusterXformsAttrOperator
    PLUG_CLS = ChildJointClusterXformsPlugOperator


class JointMidplaneAxisPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["JointMidplaneAxisAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("jointMidplaneAxisX", "jmx"),
        ("jointMidplaneAxisY", "jmy"),
        ("jointMidplaneAxisZ", "jmz"),
    )

    jointMidplaneAxisX = DoubleLinearField(default_value=0.0)
    jmx = jointMidplaneAxisX

    jointMidplaneAxisY = DoubleLinearField(default_value=0.0)
    jmy = jointMidplaneAxisY

    jointMidplaneAxisZ = DoubleLinearField(default_value=0.0)
    jmz = jointMidplaneAxisZ


class JointMidplaneAxisAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[JointMidplaneAxisPlugOperator]
):
    __slots__ = ()

    jointMidplaneAxisX = DoubleLinearField(default_value=0.0)
    jmx = jointMidplaneAxisX

    jointMidplaneAxisY = DoubleLinearField(default_value=0.0)
    jmy = jointMidplaneAxisY

    jointMidplaneAxisZ = DoubleLinearField(default_value=0.0)
    jmz = jointMidplaneAxisZ


class JointMidplaneAxisField(
    DoubleLinear3CompoundBaseField[
        JointMidplaneAxisAttrOperator, JointMidplaneAxisPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = JointMidplaneAxisAttrOperator
    PLUG_CLS = JointMidplaneAxisPlugOperator

    jointMidplaneAxisX = DoubleLinearField(default_value=0.0)
    jmx = jointMidplaneAxisX

    jointMidplaneAxisY = DoubleLinearField(default_value=0.0)
    jmy = jointMidplaneAxisY

    jointMidplaneAxisZ = DoubleLinearField(default_value=0.0)
    jmz = jointMidplaneAxisZ


class NextJointClusterXformsPlugOperator(
    CompoundPlugOperator["NextJointClusterXformsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("nextJointPreMatrix", "npr"),
        ("nextJointWeightedMatrix", "njw"),
        ("nextJointPostMatrix", "npo"),
    )

    nextJointPreMatrix = DataMatrixField()
    npr = nextJointPreMatrix

    nextJointWeightedMatrix = DataMatrixField()
    njw = nextJointWeightedMatrix

    nextJointPostMatrix = DataMatrixField()
    npo = nextJointPostMatrix


class NextJointClusterXformsAttrOperator(
    CompoundAttrOperator[NextJointClusterXformsPlugOperator]
):
    __slots__ = ()

    nextJointPreMatrix = DataMatrixField()
    npr = nextJointPreMatrix

    nextJointWeightedMatrix = DataMatrixField()
    njw = nextJointWeightedMatrix

    nextJointPostMatrix = DataMatrixField()
    npo = nextJointPostMatrix


class NextJointClusterXformsField(
    CompoundField[
        NextJointClusterXformsAttrOperator, NextJointClusterXformsPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = NextJointClusterXformsAttrOperator
    PLUG_CLS = NextJointClusterXformsPlugOperator

    nextJointPreMatrix = DataMatrixField()
    npr = nextJointPreMatrix

    nextJointWeightedMatrix = DataMatrixField()
    njw = nextJointWeightedMatrix

    nextJointPostMatrix = DataMatrixField()
    npo = nextJointPostMatrix


class NextJointMidplaneAxisPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["NextJointMidplaneAxisAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("nextjointMidplaneAxisX", "nmx"),
        ("nextjointMidplaneAxisY", "nmy"),
        ("nextjointMidplaneAxisZ", "nmz"),
    )

    nextjointMidplaneAxisX = DoubleLinearField(default_value=0.0)
    nmx = nextjointMidplaneAxisX

    nextjointMidplaneAxisY = DoubleLinearField(default_value=0.0)
    nmy = nextjointMidplaneAxisY

    nextjointMidplaneAxisZ = DoubleLinearField(default_value=0.0)
    nmz = nextjointMidplaneAxisZ


class NextJointMidplaneAxisAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[NextJointMidplaneAxisPlugOperator]
):
    __slots__ = ()

    nextjointMidplaneAxisX = DoubleLinearField(default_value=0.0)
    nmx = nextjointMidplaneAxisX

    nextjointMidplaneAxisY = DoubleLinearField(default_value=0.0)
    nmy = nextjointMidplaneAxisY

    nextjointMidplaneAxisZ = DoubleLinearField(default_value=0.0)
    nmz = nextjointMidplaneAxisZ


class NextJointMidplaneAxisField(
    DoubleLinear3CompoundBaseField[
        NextJointMidplaneAxisAttrOperator, NextJointMidplaneAxisPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = NextJointMidplaneAxisAttrOperator
    PLUG_CLS = NextJointMidplaneAxisPlugOperator

    nextjointMidplaneAxisX = DoubleLinearField(default_value=0.0)
    nmx = nextjointMidplaneAxisX

    nextjointMidplaneAxisY = DoubleLinearField(default_value=0.0)
    nmy = nextjointMidplaneAxisY

    nextjointMidplaneAxisZ = DoubleLinearField(default_value=0.0)
    nmz = nextjointMidplaneAxisZ


class ChildJointMidplaneAxisPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ChildJointMidplaneAxisAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("childjointMidplaneAxisX", "cmx"),
        ("childjointMidplaneAxisY", "cmy"),
        ("childjointMidplaneAxisZ", "cmz"),
    )

    childjointMidplaneAxisX = DoubleLinearField(default_value=0.0)
    cmx = childjointMidplaneAxisX

    childjointMidplaneAxisY = DoubleLinearField(default_value=0.0)
    cmy = childjointMidplaneAxisY

    childjointMidplaneAxisZ = DoubleLinearField(default_value=0.0)
    cmz = childjointMidplaneAxisZ


class ChildJointMidplaneAxisAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ChildJointMidplaneAxisPlugOperator]
):
    __slots__ = ()

    childjointMidplaneAxisX = DoubleLinearField(default_value=0.0)
    cmx = childjointMidplaneAxisX

    childjointMidplaneAxisY = DoubleLinearField(default_value=0.0)
    cmy = childjointMidplaneAxisY

    childjointMidplaneAxisZ = DoubleLinearField(default_value=0.0)
    cmz = childjointMidplaneAxisZ


class ChildJointMidplaneAxisField(
    DoubleLinear3CompoundBaseField[
        ChildJointMidplaneAxisAttrOperator, ChildJointMidplaneAxisPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ChildJointMidplaneAxisAttrOperator
    PLUG_CLS = ChildJointMidplaneAxisPlugOperator


class DistanceListPlugOperator(
    CompoundPlugOperator["DistanceListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("distances", "cd"),)

    distances = FloatField(multi=True, default_value=0.0)
    cd = distances


class DistanceListAttrOperator(CompoundAttrOperator[DistanceListPlugOperator]):
    __slots__ = ()

    distances = FloatField(multi=True, default_value=0.0)
    cd = distances


class DistanceListField(
    CompoundField[DistanceListAttrOperator, DistanceListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DistanceListAttrOperator
    PLUG_CLS = DistanceListPlugOperator
