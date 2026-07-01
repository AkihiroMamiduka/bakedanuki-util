# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class FalloffObjectPlugOperator(
    Float3CompoundBasePlugOperator["FalloffObjectAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("falloffObjectX", "fallObjx"),
        ("falloffObjectY", "fallObjy"),
        ("falloffObjectZ", "fallObjz"),
    )

    falloffObjectX = FloatField()
    fallObjx = falloffObjectX

    falloffObjectY = FloatField()
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField()
    fallObjz = falloffObjectZ


class FalloffObjectAttrOperator(
    Float3CompoundBaseAttrOperator[FalloffObjectPlugOperator]
):
    __slots__ = ()

    falloffObjectX = FloatField()
    fallObjx = falloffObjectX

    falloffObjectY = FloatField()
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField()
    fallObjz = falloffObjectZ


class FalloffObjectField(
    Float3CompoundBaseField[FalloffObjectAttrOperator, FalloffObjectPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffObjectAttrOperator
    PLUG_CLS = FalloffObjectPlugOperator

    falloffObjectX = FloatField()
    fallObjx = falloffObjectX

    falloffObjectY = FloatField()
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField()
    fallObjz = falloffObjectZ


class PointLocationPlugOperator(
    Float3CompoundBasePlugOperator["PointLocationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointLocation0", "pointLoc0"),
        ("pointLocation1", "pointLoc1"),
        ("pointLocation2", "pointLoc2"),
    )

    pointLocation0 = FloatField()
    pointLoc0 = pointLocation0

    pointLocation1 = FloatField()
    pointLoc1 = pointLocation1

    pointLocation2 = FloatField()
    pointLoc2 = pointLocation2


class PointLocationAttrOperator(
    Float3CompoundBaseAttrOperator[PointLocationPlugOperator]
):
    __slots__ = ()

    pointLocation0 = FloatField()
    pointLoc0 = pointLocation0

    pointLocation1 = FloatField()
    pointLoc1 = pointLocation1

    pointLocation2 = FloatField()
    pointLoc2 = pointLocation2


class PointLocationField(
    Float3CompoundBaseField[PointLocationAttrOperator, PointLocationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointLocationAttrOperator
    PLUG_CLS = PointLocationPlugOperator

    pointLocation0 = FloatField()
    pointLoc0 = pointLocation0

    pointLocation1 = FloatField()
    pointLoc1 = pointLocation1

    pointLocation2 = FloatField()
    pointLoc2 = pointLocation2
