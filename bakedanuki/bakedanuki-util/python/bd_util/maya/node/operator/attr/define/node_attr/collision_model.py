# coding: utf-8

from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class OwnerCentroidPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OwnerCentroidAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ownerCentroidX", "ocx"),
        ("ownerCentroidY", "ocy"),
        ("ownerCentroidZ", "ocz"),
    )

    ownerCentroidX = DoubleLinearField(default_value=0.0)
    ocx = ownerCentroidX

    ownerCentroidY = DoubleLinearField(default_value=0.0)
    ocy = ownerCentroidY

    ownerCentroidZ = DoubleLinearField(default_value=0.0)
    ocz = ownerCentroidZ


class OwnerCentroidAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OwnerCentroidPlugOperator]
):
    __slots__ = ()

    ownerCentroidX = DoubleLinearField(default_value=0.0)
    ocx = ownerCentroidX

    ownerCentroidY = DoubleLinearField(default_value=0.0)
    ocy = ownerCentroidY

    ownerCentroidZ = DoubleLinearField(default_value=0.0)
    ocz = ownerCentroidZ


class OwnerCentroidField(
    DoubleLinear3CompoundBaseField[
        OwnerCentroidAttrOperator, OwnerCentroidPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OwnerCentroidAttrOperator
    PLUG_CLS = OwnerCentroidPlugOperator

    ownerCentroidX = DoubleLinearField(default_value=0.0)
    ocx = ownerCentroidX

    ownerCentroidY = DoubleLinearField(default_value=0.0)
    ocy = ownerCentroidY

    ownerCentroidZ = DoubleLinearField(default_value=0.0)
    ocz = ownerCentroidZ
