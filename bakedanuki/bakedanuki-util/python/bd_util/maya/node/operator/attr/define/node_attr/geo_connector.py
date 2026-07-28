# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.at.typed import TypedField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class IdMappingPlugOperator(CompoundPlugOperator["IdMappingAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sortedId", "sid"),
        ("idIndex", "idix"),
    )

    sortedId = TypedField(writable=False)
    sid = sortedId

    idIndex = TypedField(writable=False)
    idix = idIndex


class IdMappingAttrOperator(CompoundAttrOperator[IdMappingPlugOperator]):
    __slots__ = ()

    sortedId = TypedField(writable=False)
    sid = sortedId

    idIndex = TypedField(writable=False)
    idix = idIndex


class IdMappingField(
    CompoundField[IdMappingAttrOperator, IdMappingPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IdMappingAttrOperator
    PLUG_CLS = IdMappingPlugOperator

    sortedId = TypedField(writable=False)
    sid = sortedId

    idIndex = TypedField(writable=False)
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

    ownerCentroidX = DoubleLinearField(default_value=0.0, writable=False)
    ocx = ownerCentroidX

    ownerCentroidY = DoubleLinearField(default_value=0.0, writable=False)
    ocy = ownerCentroidY

    ownerCentroidZ = DoubleLinearField(default_value=0.0, writable=False)
    ocz = ownerCentroidZ


class OwnerCentroidAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OwnerCentroidPlugOperator]
):
    __slots__ = ()

    ownerCentroidX = DoubleLinearField(default_value=0.0, writable=False)
    ocx = ownerCentroidX

    ownerCentroidY = DoubleLinearField(default_value=0.0, writable=False)
    ocy = ownerCentroidY

    ownerCentroidZ = DoubleLinearField(default_value=0.0, writable=False)
    ocz = ownerCentroidZ


class OwnerCentroidField(
    DoubleLinear3CompoundBaseField[
        OwnerCentroidAttrOperator, OwnerCentroidPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OwnerCentroidAttrOperator
    PLUG_CLS = OwnerCentroidPlugOperator

    ownerCentroidX = DoubleLinearField(default_value=0.0, writable=False)
    ocx = ownerCentroidX

    ownerCentroidY = DoubleLinearField(default_value=0.0, writable=False)
    ocy = ownerCentroidY

    ownerCentroidZ = DoubleLinearField(default_value=0.0, writable=False)
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

    ownerCentroidLocalX = DoubleLinearField(default_value=0.0, writable=False)
    olcx = ownerCentroidLocalX

    ownerCentroidLocalY = DoubleLinearField(default_value=0.0, writable=False)
    ocly = ownerCentroidLocalY

    ownerCentroidLocalZ = DoubleLinearField(default_value=0.0, writable=False)
    oclz = ownerCentroidLocalZ


class OwnerCentroidLocalAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OwnerCentroidLocalPlugOperator]
):
    __slots__ = ()

    ownerCentroidLocalX = DoubleLinearField(default_value=0.0, writable=False)
    olcx = ownerCentroidLocalX

    ownerCentroidLocalY = DoubleLinearField(default_value=0.0, writable=False)
    ocly = ownerCentroidLocalY

    ownerCentroidLocalZ = DoubleLinearField(default_value=0.0, writable=False)
    oclz = ownerCentroidLocalZ


class OwnerCentroidLocalField(
    DoubleLinear3CompoundBaseField[
        OwnerCentroidLocalAttrOperator, OwnerCentroidLocalPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OwnerCentroidLocalAttrOperator
    PLUG_CLS = OwnerCentroidLocalPlugOperator

    ownerCentroidLocalX = DoubleLinearField(default_value=0.0, writable=False)
    olcx = ownerCentroidLocalX

    ownerCentroidLocalY = DoubleLinearField(default_value=0.0, writable=False)
    ocly = ownerCentroidLocalY

    ownerCentroidLocalZ = DoubleLinearField(default_value=0.0, writable=False)
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

    componentCentroidX = DoubleLinearField(default_value=0.0, writable=False)
    ccx = componentCentroidX

    componentCentroidY = DoubleLinearField(default_value=0.0, writable=False)
    ccy = componentCentroidY

    componentCentroidZ = DoubleLinearField(default_value=0.0, writable=False)
    ccz = componentCentroidZ


class ComponentCentroidAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ComponentCentroidPlugOperator]
):
    __slots__ = ()

    componentCentroidX = DoubleLinearField(default_value=0.0, writable=False)
    ccx = componentCentroidX

    componentCentroidY = DoubleLinearField(default_value=0.0, writable=False)
    ccy = componentCentroidY

    componentCentroidZ = DoubleLinearField(default_value=0.0, writable=False)
    ccz = componentCentroidZ


class ComponentCentroidField(
    DoubleLinear3CompoundBaseField[
        ComponentCentroidAttrOperator, ComponentCentroidPlugOperator
    ]
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

    componentCentroidLocalX = DoubleLinearField(
        default_value=0.0, writable=False
    )
    cclx = componentCentroidLocalX

    componentCentroidLocalY = DoubleLinearField(
        default_value=0.0, writable=False
    )
    clcy = componentCentroidLocalY

    componentCentroidLocalZ = DoubleLinearField(
        default_value=0.0, writable=False
    )
    clcz = componentCentroidLocalZ


class ComponentCentroidLocalAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ComponentCentroidLocalPlugOperator]
):
    __slots__ = ()

    componentCentroidLocalX = DoubleLinearField(
        default_value=0.0, writable=False
    )
    cclx = componentCentroidLocalX

    componentCentroidLocalY = DoubleLinearField(
        default_value=0.0, writable=False
    )
    clcy = componentCentroidLocalY

    componentCentroidLocalZ = DoubleLinearField(
        default_value=0.0, writable=False
    )
    clcz = componentCentroidLocalZ


class ComponentCentroidLocalField(
    DoubleLinear3CompoundBaseField[
        ComponentCentroidLocalAttrOperator, ComponentCentroidLocalPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ComponentCentroidLocalAttrOperator
    PLUG_CLS = ComponentCentroidLocalPlugOperator
