# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.matrix import MatrixField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.long_compound.long3_compound._base import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
)


class InputPlugOperator(
    CompoundPlugOperator["InputAttrOperator"]
):
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


class InputAttrOperator(
    CompoundAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField(default_value=0)
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputField(
    CompoundField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator


class EnvelopeWeightsListPlugOperator(
    CompoundPlugOperator["EnvelopeWeightsListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("envelopeWeights", "owt"),
    )

    envelopeWeights = FloatField(multi=True, default_value=1.0, writable=False)
    owt = envelopeWeights


class EnvelopeWeightsListAttrOperator(
    CompoundAttrOperator[EnvelopeWeightsListPlugOperator]
):
    __slots__ = ()

    envelopeWeights = FloatField(multi=True, default_value=1.0, writable=False)
    owt = envelopeWeights


class EnvelopeWeightsListField(
    CompoundField[EnvelopeWeightsListAttrOperator, EnvelopeWeightsListPlugOperator]
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


class WeightListPlugOperator(
    CompoundPlugOperator["WeightListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weights", "wl.w"),
    )

    weights = FloatField(multi=True, default_value=1.0)


class WeightListAttrOperator(
    CompoundAttrOperator[WeightListPlugOperator]
):
    __slots__ = ()

    weights = FloatField(multi=True, default_value=1.0)


class WeightListField(
    CompoundField[WeightListAttrOperator, WeightListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListAttrOperator
    PLUG_CLS = WeightListPlugOperator


class DeformedLatticePlugOperator(
    CompoundPlugOperator["DeformedLatticeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("deformedLatticePoints", "dlp"),
        ("deformedLatticeMatrix", "dlm"),
    )

    deformedLatticePoints = TypedField()
    dlp = deformedLatticePoints

    deformedLatticeMatrix = MatrixField()
    dlm = deformedLatticeMatrix


class DeformedLatticeAttrOperator(
    CompoundAttrOperator[DeformedLatticePlugOperator]
):
    __slots__ = ()

    deformedLatticePoints = TypedField()
    dlp = deformedLatticePoints

    deformedLatticeMatrix = MatrixField()
    dlm = deformedLatticeMatrix


class DeformedLatticeField(
    CompoundField[DeformedLatticeAttrOperator, DeformedLatticePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DeformedLatticeAttrOperator
    PLUG_CLS = DeformedLatticePlugOperator

    deformedLatticePoints = TypedField()
    dlp = deformedLatticePoints

    deformedLatticeMatrix = MatrixField()
    dlm = deformedLatticeMatrix


class BaseLatticePlugOperator(
    CompoundPlugOperator["BaseLatticeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("baseLatticePoints", "blp"),
        ("baseLatticeMatrix", "blm"),
    )

    baseLatticePoints = TypedField()
    blp = baseLatticePoints

    baseLatticeMatrix = MatrixField()
    blm = baseLatticeMatrix


class BaseLatticeAttrOperator(
    CompoundAttrOperator[BaseLatticePlugOperator]
):
    __slots__ = ()

    baseLatticePoints = TypedField()
    blp = baseLatticePoints

    baseLatticeMatrix = MatrixField()
    blm = baseLatticeMatrix


class BaseLatticeField(
    CompoundField[BaseLatticeAttrOperator, BaseLatticePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BaseLatticeAttrOperator
    PLUG_CLS = BaseLatticePlugOperator

    baseLatticePoints = TypedField()
    blp = baseLatticePoints

    baseLatticeMatrix = MatrixField()
    blm = baseLatticeMatrix


class StuCacheListPlugOperator(
    CompoundPlugOperator["StuCacheListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("stuCache", "stu"),
    )

    stuCache = DoubleField(multi=True, default_value=0.0)
    stu = stuCache


class StuCacheListAttrOperator(
    CompoundAttrOperator[StuCacheListPlugOperator]
):
    __slots__ = ()

    stuCache = DoubleField(multi=True, default_value=0.0)
    stu = stuCache


class StuCacheListField(
    CompoundField[StuCacheListAttrOperator, StuCacheListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StuCacheListAttrOperator
    PLUG_CLS = StuCacheListPlugOperator
