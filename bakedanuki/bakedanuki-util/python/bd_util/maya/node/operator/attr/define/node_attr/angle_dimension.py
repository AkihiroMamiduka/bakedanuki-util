# coding: utf-8

from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class StartPointPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["StartPointAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("startPointX", "spx"),
        ("startPointY", "spy"),
        ("startPointZ", "spz"),
    )

    startPointX = DoubleLinearField(default_value=0.0, readable=False)
    spx = startPointX

    startPointY = DoubleLinearField(default_value=0.0, readable=False)
    spy = startPointY

    startPointZ = DoubleLinearField(default_value=0.0, readable=False)
    spz = startPointZ


class StartPointAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[StartPointPlugOperator]
):
    __slots__ = ()

    startPointX = DoubleLinearField(default_value=0.0, readable=False)
    spx = startPointX

    startPointY = DoubleLinearField(default_value=0.0, readable=False)
    spy = startPointY

    startPointZ = DoubleLinearField(default_value=0.0, readable=False)
    spz = startPointZ


class StartPointField(
    DoubleLinear3CompoundBaseField[
        StartPointAttrOperator, StartPointPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = StartPointAttrOperator
    PLUG_CLS = StartPointPlugOperator

    startPointX = DoubleLinearField(default_value=0.0, readable=False)
    spx = startPointX

    startPointY = DoubleLinearField(default_value=0.0, readable=False)
    spy = startPointY

    startPointZ = DoubleLinearField(default_value=0.0, readable=False)
    spz = startPointZ


class MiddlePointPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["MiddlePointAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("middlePointX", "mpx"),
        ("middlePointY", "mpy"),
        ("middlePointZ", "mpz"),
    )

    middlePointX = DoubleLinearField(default_value=0.0, readable=False)
    mpx = middlePointX

    middlePointY = DoubleLinearField(default_value=0.0, readable=False)
    mpy = middlePointY

    middlePointZ = DoubleLinearField(default_value=0.0, readable=False)
    mpz = middlePointZ


class MiddlePointAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[MiddlePointPlugOperator]
):
    __slots__ = ()

    middlePointX = DoubleLinearField(default_value=0.0, readable=False)
    mpx = middlePointX

    middlePointY = DoubleLinearField(default_value=0.0, readable=False)
    mpy = middlePointY

    middlePointZ = DoubleLinearField(default_value=0.0, readable=False)
    mpz = middlePointZ


class MiddlePointField(
    DoubleLinear3CompoundBaseField[
        MiddlePointAttrOperator, MiddlePointPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = MiddlePointAttrOperator
    PLUG_CLS = MiddlePointPlugOperator

    middlePointX = DoubleLinearField(default_value=0.0, readable=False)
    mpx = middlePointX

    middlePointY = DoubleLinearField(default_value=0.0, readable=False)
    mpy = middlePointY

    middlePointZ = DoubleLinearField(default_value=0.0, readable=False)
    mpz = middlePointZ


class EndPointPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["EndPointAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("endPointX", "epx"),
        ("endPointY", "epy"),
        ("endPointZ", "epz"),
    )

    endPointX = DoubleLinearField(default_value=0.0, readable=False)
    epx = endPointX

    endPointY = DoubleLinearField(default_value=0.0, readable=False)
    epy = endPointY

    endPointZ = DoubleLinearField(default_value=0.0, readable=False)
    epz = endPointZ


class EndPointAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[EndPointPlugOperator]
):
    __slots__ = ()

    endPointX = DoubleLinearField(default_value=0.0, readable=False)
    epx = endPointX

    endPointY = DoubleLinearField(default_value=0.0, readable=False)
    epy = endPointY

    endPointZ = DoubleLinearField(default_value=0.0, readable=False)
    epz = endPointZ


class EndPointField(
    DoubleLinear3CompoundBaseField[EndPointAttrOperator, EndPointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EndPointAttrOperator
    PLUG_CLS = EndPointPlugOperator

    endPointX = DoubleLinearField(default_value=0.0, readable=False)
    epx = endPointX

    endPointY = DoubleLinearField(default_value=0.0, readable=False)
    epy = endPointY

    endPointZ = DoubleLinearField(default_value=0.0, readable=False)
    epz = endPointZ
