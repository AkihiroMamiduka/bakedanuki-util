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

    groupId = LongField()
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputAttrOperator(
    CompoundAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField()
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

    envelopeWeights = FloatField()
    owt = envelopeWeights


class EnvelopeWeightsListAttrOperator(
    CompoundAttrOperator[EnvelopeWeightsListPlugOperator]
):
    __slots__ = ()

    envelopeWeights = FloatField()
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

    fchild1 = LongField()
    f1 = fchild1

    fchild2 = LongField()
    f2 = fchild2

    fchild3 = LongField()
    f3 = fchild3


class FunctionAttrOperator(
    Long3CompoundBaseAttrOperator[FunctionPlugOperator]
):
    __slots__ = ()

    fchild1 = LongField()
    f1 = fchild1

    fchild2 = LongField()
    f2 = fchild2

    fchild3 = LongField()
    f3 = fchild3


class FunctionField(
    Long3CompoundBaseField[FunctionAttrOperator, FunctionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FunctionAttrOperator
    PLUG_CLS = FunctionPlugOperator

    fchild1 = LongField()
    f1 = fchild1

    fchild2 = LongField()
    f2 = fchild2

    fchild3 = LongField()
    f3 = fchild3


class WeightListPlugOperator(
    CompoundPlugOperator["WeightListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weights", "wl.w"),
    )

    weights = FloatField()


class WeightListAttrOperator(
    CompoundAttrOperator[WeightListPlugOperator]
):
    __slots__ = ()

    weights = FloatField()


class WeightListField(
    CompoundField[WeightListAttrOperator, WeightListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListAttrOperator
    PLUG_CLS = WeightListPlugOperator


class GeoDataPlugOperator(
    CompoundPlugOperator["GeoDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldMatrixGeo", "wmg"),
    )

    worldMatrixGeo = MatrixField()
    wmg = worldMatrixGeo


class GeoDataAttrOperator(
    CompoundAttrOperator[GeoDataPlugOperator]
):
    __slots__ = ()

    worldMatrixGeo = MatrixField()
    wmg = worldMatrixGeo


class GeoDataField(
    CompoundField[GeoDataAttrOperator, GeoDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GeoDataAttrOperator
    PLUG_CLS = GeoDataPlugOperator


class CollisionDataPlugOperator(
    CompoundPlugOperator["CollisionDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tolerance", "tol"),
        ("falloff", "fal"),
        ("volumize", "vol"),
        ("blurIterations", "blrit"),
        ("relaxIterations", "rxi"),
        ("relaxStrength", "rxstr"),
        ("smoothIterations", "smi"),
        ("smoothStrength", "smstr"),
        ("smoothHold", "hld"),
    )

    tolerance = DoubleField()
    tol = tolerance

    falloff = DoubleField()
    fal = falloff

    volumize = DoubleField()
    vol = volumize

    blurIterations = LongField()
    blrit = blurIterations

    relaxIterations = LongField()
    rxi = relaxIterations

    relaxStrength = DoubleField()
    rxstr = relaxStrength

    smoothIterations = LongField()
    smi = smoothIterations

    smoothStrength = DoubleField()
    smstr = smoothStrength

    smoothHold = DoubleField()
    hld = smoothHold


class CollisionDataAttrOperator(
    CompoundAttrOperator[CollisionDataPlugOperator]
):
    __slots__ = ()

    tolerance = DoubleField()
    tol = tolerance

    falloff = DoubleField()
    fal = falloff

    volumize = DoubleField()
    vol = volumize

    blurIterations = LongField()
    blrit = blurIterations

    relaxIterations = LongField()
    rxi = relaxIterations

    relaxStrength = DoubleField()
    rxstr = relaxStrength

    smoothIterations = LongField()
    smi = smoothIterations

    smoothStrength = DoubleField()
    smstr = smoothStrength

    smoothHold = DoubleField()
    hld = smoothHold


class CollisionDataField(
    CompoundField[CollisionDataAttrOperator, CollisionDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollisionDataAttrOperator
    PLUG_CLS = CollisionDataPlugOperator

    tolerance = DoubleField()
    tol = tolerance

    falloff = DoubleField()
    fal = falloff

    volumize = DoubleField()
    vol = volumize

    blurIterations = LongField()
    blrit = blurIterations

    relaxIterations = LongField()
    rxi = relaxIterations

    relaxStrength = DoubleField()
    rxstr = relaxStrength

    smoothIterations = LongField()
    smi = smoothIterations

    smoothStrength = DoubleField()
    smstr = smoothStrength

    smoothHold = DoubleField()
    hld = smoothHold
