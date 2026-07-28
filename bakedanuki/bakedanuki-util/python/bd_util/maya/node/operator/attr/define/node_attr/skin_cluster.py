# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
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
    CHILD_ATTR_NAMES = (("weights", "w"),)

    weights = DoubleField(multi=True, default_value=0.0)
    w = weights


class WeightListAttrOperator(CompoundAttrOperator[WeightListPlugOperator]):
    __slots__ = ()

    weights = DoubleField(multi=True, default_value=0.0)
    w = weights


class WeightListField(
    CompoundField[WeightListAttrOperator, WeightListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListAttrOperator
    PLUG_CLS = WeightListPlugOperator


class PerInfluenceWeightsPlugOperator(
    CompoundPlugOperator["PerInfluenceWeightsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("perInfluenceVertexWeights", "pivw"),)

    perInfluenceVertexWeights = DoubleField(
        multi=True, default_value=0.0, writable=False
    )
    pivw = perInfluenceVertexWeights


class PerInfluenceWeightsAttrOperator(
    CompoundAttrOperator[PerInfluenceWeightsPlugOperator]
):
    __slots__ = ()

    perInfluenceVertexWeights = DoubleField(
        multi=True, default_value=0.0, writable=False
    )
    pivw = perInfluenceVertexWeights


class PerInfluenceWeightsField(
    CompoundField[
        PerInfluenceWeightsAttrOperator, PerInfluenceWeightsPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = PerInfluenceWeightsAttrOperator
    PLUG_CLS = PerInfluenceWeightsPlugOperator


class InfluenceColorPlugOperator(
    Float3CompoundBasePlugOperator["InfluenceColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("influenceColorR", "ifcr"),
        ("influenceColorG", "ifcg"),
        ("influenceColorB", "ifcb"),
    )

    influenceColorR = FloatField(default_value=0.0)
    ifcr = influenceColorR

    influenceColorG = FloatField(default_value=0.0)
    ifcg = influenceColorG

    influenceColorB = FloatField(default_value=0.0)
    ifcb = influenceColorB


class InfluenceColorAttrOperator(
    Float3CompoundBaseAttrOperator[InfluenceColorPlugOperator]
):
    __slots__ = ()

    influenceColorR = FloatField(default_value=0.0)
    ifcr = influenceColorR

    influenceColorG = FloatField(default_value=0.0)
    ifcg = influenceColorG

    influenceColorB = FloatField(default_value=0.0)
    ifcb = influenceColorB


class InfluenceColorField(
    Float3CompoundBaseField[
        InfluenceColorAttrOperator, InfluenceColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = InfluenceColorAttrOperator
    PLUG_CLS = InfluenceColorPlugOperator


class DqsScalePlugOperator(
    Double3CompoundBasePlugOperator["DqsScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dqsScaleX", "dscx"),
        ("dqsScaleY", "dscy"),
        ("dqsScaleZ", "dscz"),
    )

    dqsScaleX = DoubleField(default_value=1.0)
    dscx = dqsScaleX

    dqsScaleY = DoubleField(default_value=1.0)
    dscy = dqsScaleY

    dqsScaleZ = DoubleField(default_value=1.0)
    dscz = dqsScaleZ


class DqsScaleAttrOperator(
    Double3CompoundBaseAttrOperator[DqsScalePlugOperator]
):
    __slots__ = ()

    dqsScaleX = DoubleField(default_value=1.0)
    dscx = dqsScaleX

    dqsScaleY = DoubleField(default_value=1.0)
    dscy = dqsScaleY

    dqsScaleZ = DoubleField(default_value=1.0)
    dscz = dqsScaleZ


class DqsScaleField(
    Double3CompoundBaseField[DqsScaleAttrOperator, DqsScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DqsScaleAttrOperator
    PLUG_CLS = DqsScalePlugOperator

    dqsScaleX = DoubleField(default_value=1.0)
    dscx = dqsScaleX

    dqsScaleY = DoubleField(default_value=1.0)
    dscy = dqsScaleY

    dqsScaleZ = DoubleField(default_value=1.0)
    dscz = dqsScaleZ
