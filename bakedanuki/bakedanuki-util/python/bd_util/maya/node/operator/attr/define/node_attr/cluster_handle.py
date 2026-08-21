# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.dt.matrix import DataMatrixField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class ClusterTransformsPlugOperator(
    CompoundPlugOperator["ClusterTransformsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("preWeightedMatrixTransform", "pre"),
        ("weightedMatrixTransform", "wt"),
        ("postWeightedMatrixTransform", "post"),
    )

    preWeightedMatrixTransform = DataMatrixField(writable=False)
    pre = preWeightedMatrixTransform

    weightedMatrixTransform = DataMatrixField(writable=False)
    wt = weightedMatrixTransform

    postWeightedMatrixTransform = DataMatrixField(writable=False)
    post = postWeightedMatrixTransform


class ClusterTransformsAttrOperator(
    CompoundAttrOperator[ClusterTransformsPlugOperator]
):
    __slots__ = ()

    preWeightedMatrixTransform = DataMatrixField(writable=False)
    pre = preWeightedMatrixTransform

    weightedMatrixTransform = DataMatrixField(writable=False)
    wt = weightedMatrixTransform

    postWeightedMatrixTransform = DataMatrixField(writable=False)
    post = postWeightedMatrixTransform


class ClusterTransformsField(
    CompoundField[ClusterTransformsAttrOperator, ClusterTransformsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClusterTransformsAttrOperator
    PLUG_CLS = ClusterTransformsPlugOperator


class OriginPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OriginAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("originX", "ox"),
        ("originY", "oy"),
        ("originZ", "oz"),
    )

    originX = DoubleLinearField(default_value=0.0)
    ox = originX

    originY = DoubleLinearField(default_value=0.0)
    oy = originY

    originZ = DoubleLinearField(default_value=0.0)
    oz = originZ


class OriginAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OriginPlugOperator]
):
    __slots__ = ()

    originX = DoubleLinearField(default_value=0.0)
    ox = originX

    originY = DoubleLinearField(default_value=0.0)
    oy = originY

    originZ = DoubleLinearField(default_value=0.0)
    oz = originZ


class OriginField(
    DoubleLinear3CompoundBaseField[OriginAttrOperator, OriginPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OriginAttrOperator
    PLUG_CLS = OriginPlugOperator

    originX = DoubleLinearField(default_value=0.0)
    ox = originX

    originY = DoubleLinearField(default_value=0.0)
    oy = originY

    originZ = DoubleLinearField(default_value=0.0)
    oz = originZ
