# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.typed import TypedField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class IdMappingPlugOperator(
    CompoundPlugOperator["IdMappingAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sortedId", "sid"),
        ("idIndex", "idix"),
    )

    sortedId = TypedField()
    sid = sortedId

    idIndex = TypedField()
    idix = idIndex


class IdMappingAttrOperator(
    CompoundAttrOperator[IdMappingPlugOperator]
):
    __slots__ = ()

    sortedId = TypedField()
    sid = sortedId

    idIndex = TypedField()
    idix = idIndex


class IdMappingField(
    CompoundField[IdMappingAttrOperator, IdMappingPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IdMappingAttrOperator
    PLUG_CLS = IdMappingPlugOperator

    sortedId = TypedField()
    sid = sortedId

    idIndex = TypedField()
    idix = idIndex


class OwnerCentroidPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OwnerCentroidAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ownerCentroidX", "ocx"),
        ("ownerCentroidY", "ocy"),
        ("ownerCentroidZ", "ocz"),
    )

    ownerCentroidX = DoubleLinearField()
    ocx = ownerCentroidX

    ownerCentroidY = DoubleLinearField()
    ocy = ownerCentroidY

    ownerCentroidZ = DoubleLinearField()
    ocz = ownerCentroidZ


class OwnerCentroidAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OwnerCentroidPlugOperator]
):
    __slots__ = ()

    ownerCentroidX = DoubleLinearField()
    ocx = ownerCentroidX

    ownerCentroidY = DoubleLinearField()
    ocy = ownerCentroidY

    ownerCentroidZ = DoubleLinearField()
    ocz = ownerCentroidZ


class OwnerCentroidField(
    DoubleLinear3CompoundBaseField[OwnerCentroidAttrOperator, OwnerCentroidPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OwnerCentroidAttrOperator
    PLUG_CLS = OwnerCentroidPlugOperator

    ownerCentroidX = DoubleLinearField()
    ocx = ownerCentroidX

    ownerCentroidY = DoubleLinearField()
    ocy = ownerCentroidY

    ownerCentroidZ = DoubleLinearField()
    ocz = ownerCentroidZ


class OwnerCentroidLocalPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OwnerCentroidLocalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ownerCentroidLocalX", "olcx"),
        ("ownerCentroidLocalY", "ocly"),
        ("ownerCentroidLocalZ", "oclz"),
    )

    ownerCentroidLocalX = DoubleLinearField()
    olcx = ownerCentroidLocalX

    ownerCentroidLocalY = DoubleLinearField()
    ocly = ownerCentroidLocalY

    ownerCentroidLocalZ = DoubleLinearField()
    oclz = ownerCentroidLocalZ


class OwnerCentroidLocalAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OwnerCentroidLocalPlugOperator]
):
    __slots__ = ()

    ownerCentroidLocalX = DoubleLinearField()
    olcx = ownerCentroidLocalX

    ownerCentroidLocalY = DoubleLinearField()
    ocly = ownerCentroidLocalY

    ownerCentroidLocalZ = DoubleLinearField()
    oclz = ownerCentroidLocalZ


class OwnerCentroidLocalField(
    DoubleLinear3CompoundBaseField[OwnerCentroidLocalAttrOperator, OwnerCentroidLocalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OwnerCentroidLocalAttrOperator
    PLUG_CLS = OwnerCentroidLocalPlugOperator

    ownerCentroidLocalX = DoubleLinearField()
    olcx = ownerCentroidLocalX

    ownerCentroidLocalY = DoubleLinearField()
    ocly = ownerCentroidLocalY

    ownerCentroidLocalZ = DoubleLinearField()
    oclz = ownerCentroidLocalZ


class ComponentCentroidPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ComponentCentroidAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("componentCentroidX", "ccx"),
        ("componentCentroidY", "ccy"),
        ("componentCentroidZ", "ccz"),
    )

    componentCentroidX = DoubleLinearField()
    ccx = componentCentroidX

    componentCentroidY = DoubleLinearField()
    ccy = componentCentroidY

    componentCentroidZ = DoubleLinearField()
    ccz = componentCentroidZ


class ComponentCentroidAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ComponentCentroidPlugOperator]
):
    __slots__ = ()

    componentCentroidX = DoubleLinearField()
    ccx = componentCentroidX

    componentCentroidY = DoubleLinearField()
    ccy = componentCentroidY

    componentCentroidZ = DoubleLinearField()
    ccz = componentCentroidZ


class ComponentCentroidField(
    DoubleLinear3CompoundBaseField[ComponentCentroidAttrOperator, ComponentCentroidPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ComponentCentroidAttrOperator
    PLUG_CLS = ComponentCentroidPlugOperator


class ComponentCentroidLocalPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ComponentCentroidLocalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("componentCentroidLocalX", "cclx"),
        ("componentCentroidLocalY", "clcy"),
        ("componentCentroidLocalZ", "clcz"),
    )

    componentCentroidLocalX = DoubleLinearField()
    cclx = componentCentroidLocalX

    componentCentroidLocalY = DoubleLinearField()
    clcy = componentCentroidLocalY

    componentCentroidLocalZ = DoubleLinearField()
    clcz = componentCentroidLocalZ


class ComponentCentroidLocalAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ComponentCentroidLocalPlugOperator]
):
    __slots__ = ()

    componentCentroidLocalX = DoubleLinearField()
    cclx = componentCentroidLocalX

    componentCentroidLocalY = DoubleLinearField()
    clcy = componentCentroidLocalY

    componentCentroidLocalZ = DoubleLinearField()
    clcz = componentCentroidLocalZ


class ComponentCentroidLocalField(
    DoubleLinear3CompoundBaseField[ComponentCentroidLocalAttrOperator, ComponentCentroidLocalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ComponentCentroidLocalAttrOperator
    PLUG_CLS = ComponentCentroidLocalPlugOperator
