# coding: utf-8

from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class PositionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["PositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionX", "px"),
        ("positionY", "py"),
        ("positionZ", "pz"),
    )

    positionX = DoubleLinearField(default_value=0.0, writable=False)
    px = positionX

    positionY = DoubleLinearField(default_value=0.0, writable=False)
    py = positionY

    positionZ = DoubleLinearField(default_value=0.0, writable=False)
    pz = positionZ


class PositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[PositionPlugOperator]
):
    __slots__ = ()

    positionX = DoubleLinearField(default_value=0.0, writable=False)
    px = positionX

    positionY = DoubleLinearField(default_value=0.0, writable=False)
    py = positionY

    positionZ = DoubleLinearField(default_value=0.0, writable=False)
    pz = positionZ


class PositionField(
    DoubleLinear3CompoundBaseField[PositionAttrOperator, PositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionAttrOperator
    PLUG_CLS = PositionPlugOperator


class NormalPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["NormalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalX", "nx"),
        ("normalY", "ny"),
        ("normalZ", "nz"),
    )

    normalX = DoubleLinearField(default_value=0.0, writable=False)
    nx = normalX

    normalY = DoubleLinearField(default_value=0.0, writable=False)
    ny = normalY

    normalZ = DoubleLinearField(default_value=0.0, writable=False)
    nz = normalZ


class NormalAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[NormalPlugOperator]
):
    __slots__ = ()

    normalX = DoubleLinearField(default_value=0.0, writable=False)
    nx = normalX

    normalY = DoubleLinearField(default_value=0.0, writable=False)
    ny = normalY

    normalZ = DoubleLinearField(default_value=0.0, writable=False)
    nz = normalZ


class NormalField(
    DoubleLinear3CompoundBaseField[NormalAttrOperator, NormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalAttrOperator
    PLUG_CLS = NormalPlugOperator


class CvPositionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["CvPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cvpositionX", "cvx"),
        ("cvpositionY", "cvy"),
        ("cvpositionZ", "cvz"),
    )

    cvpositionX = DoubleLinearField(default_value=-1.0, writable=False)
    cvx = cvpositionX

    cvpositionY = DoubleLinearField(default_value=-1.0, writable=False)
    cvy = cvpositionY

    cvpositionZ = DoubleLinearField(default_value=-1.0, writable=False)
    cvz = cvpositionZ


class CvPositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CvPositionPlugOperator]
):
    __slots__ = ()

    cvpositionX = DoubleLinearField(default_value=-1.0, writable=False)
    cvx = cvpositionX

    cvpositionY = DoubleLinearField(default_value=-1.0, writable=False)
    cvy = cvpositionY

    cvpositionZ = DoubleLinearField(default_value=-1.0, writable=False)
    cvz = cvpositionZ


class CvPositionField(
    DoubleLinear3CompoundBaseField[
        CvPositionAttrOperator, CvPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CvPositionAttrOperator
    PLUG_CLS = CvPositionPlugOperator
