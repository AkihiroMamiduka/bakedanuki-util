# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
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

    falloffObjectX = FloatField(default_value=0.0)
    fallObjx = falloffObjectX

    falloffObjectY = FloatField(default_value=0.0)
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField(default_value=0.0)
    fallObjz = falloffObjectZ


class FalloffObjectAttrOperator(
    Float3CompoundBaseAttrOperator[FalloffObjectPlugOperator]
):
    __slots__ = ()

    falloffObjectX = FloatField(default_value=0.0)
    fallObjx = falloffObjectX

    falloffObjectY = FloatField(default_value=0.0)
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField(default_value=0.0)
    fallObjz = falloffObjectZ


class FalloffObjectField(
    Float3CompoundBaseField[
        FalloffObjectAttrOperator, FalloffObjectPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = FalloffObjectAttrOperator
    PLUG_CLS = FalloffObjectPlugOperator

    falloffObjectX = FloatField(default_value=0.0)
    fallObjx = falloffObjectX

    falloffObjectY = FloatField(default_value=0.0)
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField(default_value=0.0)
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

    pointLocation0 = FloatField(default_value=0.0)
    pointLoc0 = pointLocation0

    pointLocation1 = FloatField(default_value=0.0)
    pointLoc1 = pointLocation1

    pointLocation2 = FloatField(default_value=0.0)
    pointLoc2 = pointLocation2


class PointLocationAttrOperator(
    Float3CompoundBaseAttrOperator[PointLocationPlugOperator]
):
    __slots__ = ()

    pointLocation0 = FloatField(default_value=0.0)
    pointLoc0 = pointLocation0

    pointLocation1 = FloatField(default_value=0.0)
    pointLoc1 = pointLocation1

    pointLocation2 = FloatField(default_value=0.0)
    pointLoc2 = pointLocation2


class PointLocationField(
    Float3CompoundBaseField[
        PointLocationAttrOperator, PointLocationPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = PointLocationAttrOperator
    PLUG_CLS = PointLocationPlugOperator

    pointLocation0 = FloatField(default_value=0.0)
    pointLoc0 = pointLocation0

    pointLocation1 = FloatField(default_value=0.0)
    pointLoc1 = pointLocation1

    pointLocation2 = FloatField(default_value=0.0)
    pointLoc2 = pointLocation2
