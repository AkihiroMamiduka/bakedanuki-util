# coding: utf-8

from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
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

    positionX = DoubleLinearField()
    px = positionX

    positionY = DoubleLinearField()
    py = positionY

    positionZ = DoubleLinearField()
    pz = positionZ


class PositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[PositionPlugOperator]
):
    __slots__ = ()

    positionX = DoubleLinearField()
    px = positionX

    positionY = DoubleLinearField()
    py = positionY

    positionZ = DoubleLinearField()
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

    normalX = DoubleLinearField()
    nx = normalX

    normalY = DoubleLinearField()
    ny = normalY

    normalZ = DoubleLinearField()
    nz = normalZ


class NormalAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[NormalPlugOperator]
):
    __slots__ = ()

    normalX = DoubleLinearField()
    nx = normalX

    normalY = DoubleLinearField()
    ny = normalY

    normalZ = DoubleLinearField()
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

    cvpositionX = DoubleLinearField()
    cvx = cvpositionX

    cvpositionY = DoubleLinearField()
    cvy = cvpositionY

    cvpositionZ = DoubleLinearField()
    cvz = cvpositionZ


class CvPositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CvPositionPlugOperator]
):
    __slots__ = ()

    cvpositionX = DoubleLinearField()
    cvx = cvpositionX

    cvpositionY = DoubleLinearField()
    cvy = cvpositionY

    cvpositionZ = DoubleLinearField()
    cvz = cvpositionZ


class CvPositionField(
    DoubleLinear3CompoundBaseField[CvPositionAttrOperator, CvPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CvPositionAttrOperator
    PLUG_CLS = CvPositionPlugOperator
