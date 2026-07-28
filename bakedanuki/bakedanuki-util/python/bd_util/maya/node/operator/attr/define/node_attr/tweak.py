# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
    Double3Field,
    Float3Field,
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


class PlistPlugOperator(CompoundPlugOperator["PlistAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("controlPoints", "cp"),)

    controlPoints = Double3Field(multi=True, default_value=(0.0, 0.0, 0.0))
    cp = controlPoints


class PlistAttrOperator(CompoundAttrOperator[PlistPlugOperator]):
    __slots__ = ()

    controlPoints = Double3Field(multi=True, default_value=(0.0, 0.0, 0.0))
    cp = controlPoints


class PlistField(CompoundField[PlistAttrOperator, PlistPlugOperator]):
    __slots__ = ()

    ATTR_CLS = PlistAttrOperator
    PLUG_CLS = PlistPlugOperator


class VlistPlugOperator(CompoundPlugOperator["VlistAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("vertex", "vt"),)

    vertex = Float3Field(multi=True, default_value=(0.0, 0.0, 0.0))
    vt = vertex


class VlistAttrOperator(CompoundAttrOperator[VlistPlugOperator]):
    __slots__ = ()

    vertex = Float3Field(multi=True, default_value=(0.0, 0.0, 0.0))
    vt = vertex


class VlistField(CompoundField[VlistAttrOperator, VlistPlugOperator]):
    __slots__ = ()

    ATTR_CLS = VlistAttrOperator
    PLUG_CLS = VlistPlugOperator
