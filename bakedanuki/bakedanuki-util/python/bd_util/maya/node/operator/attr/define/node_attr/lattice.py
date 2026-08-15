# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
    Double2CompoundBaseAttrOperator,
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseField,
)


class ColorSet_representationEnumPlugOperator(
    EnumPlugOperator["ColorSet_representationEnumAttrOperator"]
):
    __slots__ = ()

    A = 1
    LA = 2
    RGB = 3
    RGBA = 4


class ColorSet_representationEnumAttrOperator(
    EnumAttrOperator[ColorSet_representationEnumPlugOperator]
):
    __slots__ = ()

    A = 1
    LA = 2
    RGB = 3
    RGBA = 4

    NAME_MAP = {
        A: "A",
        LA: "LA",
        RGB: "RGB",
        RGBA: "RGBA",
    }


class ColorSet_representationEnumField(
    EnumField[
        ColorSet_representationEnumAttrOperator,
        ColorSet_representationEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ColorSet_representationEnumAttrOperator
    PLUG_CLS = ColorSet_representationEnumPlugOperator


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


class UvSet_uvSetPointsPlugOperator(
    Float2CompoundBasePlugOperator["UvSet_uvSetPointsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvSetPointsU", "uvpu"),
        ("uvSetPointsV", "uvpv"),
    )

    uvSetPointsU = FloatField(default_value=0.0)
    uvpu = uvSetPointsU

    uvSetPointsV = FloatField(default_value=0.0)
    uvpv = uvSetPointsV


class UvSet_uvSetPointsAttrOperator(
    Float2CompoundBaseAttrOperator[UvSet_uvSetPointsPlugOperator]
):
    __slots__ = ()

    uvSetPointsU = FloatField(default_value=0.0)
    uvpu = uvSetPointsU

    uvSetPointsV = FloatField(default_value=0.0)
    uvpv = uvSetPointsV


class UvSet_uvSetPointsField(
    Float2CompoundBaseField[
        UvSet_uvSetPointsAttrOperator, UvSet_uvSetPointsPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = UvSet_uvSetPointsAttrOperator
    PLUG_CLS = UvSet_uvSetPointsPlugOperator


class ColorSet_colorSetPointsPlugOperator(
    CompoundPlugOperator["ColorSet_colorSetPointsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorSetPointsR", "clpr"),
        ("colorSetPointsG", "clpg"),
        ("colorSetPointsB", "clpb"),
        ("colorSetPointsA", "clpa"),
    )

    colorSetPointsR = FloatField(default_value=0.0)
    clpr = colorSetPointsR

    colorSetPointsG = FloatField(default_value=0.0)
    clpg = colorSetPointsG

    colorSetPointsB = FloatField(default_value=0.0)
    clpb = colorSetPointsB

    colorSetPointsA = FloatField(default_value=0.0)
    clpa = colorSetPointsA


class ColorSet_colorSetPointsAttrOperator(
    CompoundAttrOperator[ColorSet_colorSetPointsPlugOperator]
):
    __slots__ = ()

    colorSetPointsR = FloatField(default_value=0.0)
    clpr = colorSetPointsR

    colorSetPointsG = FloatField(default_value=0.0)
    clpg = colorSetPointsG

    colorSetPointsB = FloatField(default_value=0.0)
    clpb = colorSetPointsB

    colorSetPointsA = FloatField(default_value=0.0)
    clpa = colorSetPointsA


class ColorSet_colorSetPointsField(
    CompoundField[
        ColorSet_colorSetPointsAttrOperator,
        ColorSet_colorSetPointsPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ColorSet_colorSetPointsAttrOperator
    PLUG_CLS = ColorSet_colorSetPointsPlugOperator


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


class ControlPointsPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ControlPointsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("xValue", "xv"),
        ("yValue", "yv"),
        ("zValue", "zv"),
    )

    xValue = DoubleLinearField(default_value=0.0)
    xv = xValue

    yValue = DoubleLinearField(default_value=0.0)
    yv = yValue

    zValue = DoubleLinearField(default_value=0.0)
    zv = zValue


class ControlPointsAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ControlPointsPlugOperator]
):
    __slots__ = ()

    xValue = DoubleLinearField(default_value=0.0)
    xv = xValue

    yValue = DoubleLinearField(default_value=0.0)
    yv = yValue

    zValue = DoubleLinearField(default_value=0.0)
    zv = zValue


class ControlPointsField(
    DoubleLinear3CompoundBaseField[
        ControlPointsAttrOperator, ControlPointsPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ControlPointsAttrOperator
    PLUG_CLS = ControlPointsPlugOperator


class UvPivotPlugOperator(
    Double2CompoundBasePlugOperator["UvPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvPivotX", "pvx"),
        ("uvPivotY", "pvy"),
    )

    uvPivotX = DoubleField(default_value=0.0)
    pvx = uvPivotX

    uvPivotY = DoubleField(default_value=0.0)
    pvy = uvPivotY


class UvPivotAttrOperator(
    Double2CompoundBaseAttrOperator[UvPivotPlugOperator]
):
    __slots__ = ()

    uvPivotX = DoubleField(default_value=0.0)
    pvx = uvPivotX

    uvPivotY = DoubleField(default_value=0.0)
    pvy = uvPivotY


class UvPivotField(
    Double2CompoundBaseField[UvPivotAttrOperator, UvPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvPivotAttrOperator
    PLUG_CLS = UvPivotPlugOperator

    uvPivotX = DoubleField(default_value=0.0)
    pvx = uvPivotX

    uvPivotY = DoubleField(default_value=0.0)
    pvy = uvPivotY


class UvSetPlugOperator(CompoundPlugOperator["UvSetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvSetName", "uvsn"),
        ("uvSetPoints", "uvsp"),
        ("uvSetTweakLocation", "uvtw"),
    )

    uvSetName = DataStringField()
    uvsn = uvSetName

    uvSetPoints = UvSet_uvSetPointsField(multi=True, default_value=(0.0, 0.0))
    uvsp = uvSetPoints

    uvSetTweakLocation = TypedField(readable=False)
    uvtw = uvSetTweakLocation


class UvSetAttrOperator(CompoundAttrOperator[UvSetPlugOperator]):
    __slots__ = ()

    uvSetName = DataStringField()
    uvsn = uvSetName

    uvSetPoints = UvSet_uvSetPointsField(multi=True, default_value=(0.0, 0.0))
    uvsp = uvSetPoints

    uvSetTweakLocation = TypedField(readable=False)
    uvtw = uvSetTweakLocation


class UvSetField(CompoundField[UvSetAttrOperator, UvSetPlugOperator]):
    __slots__ = ()

    ATTR_CLS = UvSetAttrOperator
    PLUG_CLS = UvSetPlugOperator


class ColorSetPlugOperator(CompoundPlugOperator["ColorSetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorName", "clsn"),
        ("clamped", "clam"),
        ("representation", "rprt"),
        ("colorSetPoints", "clsp"),
    )

    colorName = DataStringField()
    clsn = colorName

    clamped = BoolField(default_value=False)
    clam = clamped

    representation = ColorSet_representationEnumField(default_value=4)
    rprt = representation

    colorSetPoints = ColorSet_colorSetPointsField(
        multi=True, default_value=(0.0, 0.0, 0.0, 0.0)
    )
    clsp = colorSetPoints


class ColorSetAttrOperator(CompoundAttrOperator[ColorSetPlugOperator]):
    __slots__ = ()

    colorName = DataStringField()
    clsn = colorName

    clamped = BoolField(default_value=False)
    clam = clamped

    representation = ColorSet_representationEnumField(default_value=4)
    rprt = representation

    colorSetPoints = ColorSet_colorSetPointsField(
        multi=True, default_value=(0.0, 0.0, 0.0, 0.0)
    )
    clsp = colorSetPoints


class ColorSetField(CompoundField[ColorSetAttrOperator, ColorSetPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ColorSetAttrOperator
    PLUG_CLS = ColorSetPlugOperator


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
