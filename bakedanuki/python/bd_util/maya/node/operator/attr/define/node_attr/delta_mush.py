# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.numeric_scalar_range.short import ShortField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..std.dt.vector_array import DataVectorArrayField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
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


class ScalePlugOperator(
    Double3CompoundBasePlugOperator["ScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleX", "sx"),
        ("scaleY", "sy"),
        ("scaleZ", "sz"),
    )

    scaleX = DoubleField(default_value=1.0)
    sx = scaleX

    scaleY = DoubleField(default_value=1.0)
    sy = scaleY

    scaleZ = DoubleField(default_value=1.0)
    sz = scaleZ


class ScaleAttrOperator(
    Double3CompoundBaseAttrOperator[ScalePlugOperator]
):
    __slots__ = ()

    scaleX = DoubleField(default_value=1.0)
    sx = scaleX

    scaleY = DoubleField(default_value=1.0)
    sy = scaleY

    scaleZ = DoubleField(default_value=1.0)
    sz = scaleZ


class ScaleField(
    Double3CompoundBaseField[ScaleAttrOperator, ScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAttrOperator
    PLUG_CLS = ScalePlugOperator

    scaleX = DoubleField(default_value=1.0)
    sx = scaleX

    scaleY = DoubleField(default_value=1.0)
    sy = scaleY

    scaleZ = DoubleField(default_value=1.0)
    sz = scaleZ


class CachePlugOperator(
    CompoundPlugOperator["CacheAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cacheSmoothingAlgorithm", "csa"),
        ("cacheSmoothingIterations", "csi"),
        ("cachePinBorderVertices", "cpbv"),
        ("cacheSmoothingStep", "css"),
        ("cacheBindPositions", "cbp"),
        ("cacheDisplacements", "cdis"),
        ("cacheFrames", "cfrm"),
    )

    cacheSmoothingAlgorithm = ShortField(default_value=0)
    csa = cacheSmoothingAlgorithm

    cacheSmoothingIterations = LongField(default_value=0, min_value=0)
    csi = cacheSmoothingIterations

    cachePinBorderVertices = BoolField(default_value=True)
    cpbv = cachePinBorderVertices

    cacheSmoothingStep = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    css = cacheSmoothingStep

    cacheBindPositions = TypedField()
    cbp = cacheBindPositions

    cacheDisplacements = DataVectorArrayField()
    cdis = cacheDisplacements

    cacheFrames = TypedField()
    cfrm = cacheFrames


class CacheAttrOperator(
    CompoundAttrOperator[CachePlugOperator]
):
    __slots__ = ()

    cacheSmoothingAlgorithm = ShortField(default_value=0)
    csa = cacheSmoothingAlgorithm

    cacheSmoothingIterations = LongField(default_value=0, min_value=0)
    csi = cacheSmoothingIterations

    cachePinBorderVertices = BoolField(default_value=True)
    cpbv = cachePinBorderVertices

    cacheSmoothingStep = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    css = cacheSmoothingStep

    cacheBindPositions = TypedField()
    cbp = cacheBindPositions

    cacheDisplacements = DataVectorArrayField()
    cdis = cacheDisplacements

    cacheFrames = TypedField()
    cfrm = cacheFrames


class CacheField(
    CompoundField[CacheAttrOperator, CachePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CacheAttrOperator
    PLUG_CLS = CachePlugOperator
