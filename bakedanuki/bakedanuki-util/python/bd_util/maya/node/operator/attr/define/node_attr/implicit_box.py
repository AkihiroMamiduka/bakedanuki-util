# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class CompInstObjGroups_compObjectGroupsPlugOperator(
    CompoundPlugOperator["CompInstObjGroups_compObjectGroupsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("compObjectGrpCompList", "cgcl"),
        ("compObjectGroupId", "cgid"),
    )

    compObjectGrpCompList = TypedField()
    cgcl = compObjectGrpCompList

    compObjectGroupId = LongField(default_value=0)
    cgid = compObjectGroupId


class CompInstObjGroups_compObjectGroupsAttrOperator(
    CompoundAttrOperator[CompInstObjGroups_compObjectGroupsPlugOperator]
):
    __slots__ = ()

    compObjectGrpCompList = TypedField()
    cgcl = compObjectGrpCompList

    compObjectGroupId = LongField(default_value=0)
    cgid = compObjectGroupId


class CompInstObjGroups_compObjectGroupsField(
    CompoundField[
        CompInstObjGroups_compObjectGroupsAttrOperator,
        CompInstObjGroups_compObjectGroupsPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CompInstObjGroups_compObjectGroupsAttrOperator
    PLUG_CLS = CompInstObjGroups_compObjectGroupsPlugOperator


class CompInstObjGroupsPlugOperator(
    CompoundPlugOperator["CompInstObjGroupsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("compObjectGroups", "cog"),)

    compObjectGroups = CompInstObjGroups_compObjectGroupsField(multi=True)
    cog = compObjectGroups


class CompInstObjGroupsAttrOperator(
    CompoundAttrOperator[CompInstObjGroupsPlugOperator]
):
    __slots__ = ()

    compObjectGroups = CompInstObjGroups_compObjectGroupsField(multi=True)
    cog = compObjectGroups


class CompInstObjGroupsField(
    CompoundField[CompInstObjGroupsAttrOperator, CompInstObjGroupsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompInstObjGroupsAttrOperator
    PLUG_CLS = CompInstObjGroupsPlugOperator


class ComponentTagsPlugOperator(
    CompoundPlugOperator["ComponentTagsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("componentTagName", "gtagnm"),
        ("componentTagContents", "gtagcmp"),
    )

    componentTagName = DataStringField()
    gtagnm = componentTagName

    componentTagContents = TypedField()
    gtagcmp = componentTagContents


class ComponentTagsAttrOperator(
    CompoundAttrOperator[ComponentTagsPlugOperator]
):
    __slots__ = ()

    componentTagName = DataStringField()
    gtagnm = componentTagName

    componentTagContents = TypedField()
    gtagcmp = componentTagContents


class ComponentTagsField(
    CompoundField[ComponentTagsAttrOperator, ComponentTagsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ComponentTagsAttrOperator
    PLUG_CLS = ComponentTagsPlugOperator


class SizePlugOperator(Double3CompoundBasePlugOperator["SizeAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sizeX", "szx"),
        ("sizeY", "szy"),
        ("sizeZ", "szz"),
    )

    sizeX = DoubleField(
        default_value=2.0, soft_min_value=0.0, soft_max_value=10.0
    )
    szx = sizeX

    sizeY = DoubleField(
        default_value=2.0, soft_min_value=0.0, soft_max_value=10.0
    )
    szy = sizeY

    sizeZ = DoubleField(
        default_value=2.0, soft_min_value=0.0, soft_max_value=10.0
    )
    szz = sizeZ


class SizeAttrOperator(Double3CompoundBaseAttrOperator[SizePlugOperator]):
    __slots__ = ()

    sizeX = DoubleField(
        default_value=2.0, soft_min_value=0.0, soft_max_value=10.0
    )
    szx = sizeX

    sizeY = DoubleField(
        default_value=2.0, soft_min_value=0.0, soft_max_value=10.0
    )
    szy = sizeY

    sizeZ = DoubleField(
        default_value=2.0, soft_min_value=0.0, soft_max_value=10.0
    )
    szz = sizeZ


class SizeField(Double3CompoundBaseField[SizeAttrOperator, SizePlugOperator]):
    __slots__ = ()

    ATTR_CLS = SizeAttrOperator
    PLUG_CLS = SizePlugOperator

    sizeX = DoubleField(
        default_value=2.0, soft_min_value=0.0, soft_max_value=10.0
    )
    szx = sizeX

    sizeY = DoubleField(
        default_value=2.0, soft_min_value=0.0, soft_max_value=10.0
    )
    szy = sizeY

    sizeZ = DoubleField(
        default_value=2.0, soft_min_value=0.0, soft_max_value=10.0
    )
    szz = sizeZ
