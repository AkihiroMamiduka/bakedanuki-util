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
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
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


class WorldNormalPlugOperator(
    Double3CompoundBasePlugOperator["WorldNormalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldNormalX", "wnx"),
        ("worldNormalY", "wny"),
        ("worldNormalZ", "wnz"),
    )

    worldNormalX = DoubleField(default_value=0.0, writable=False)
    wnx = worldNormalX

    worldNormalY = DoubleField(default_value=0.0, writable=False)
    wny = worldNormalY

    worldNormalZ = DoubleField(default_value=0.0, writable=False)
    wnz = worldNormalZ


class WorldNormalAttrOperator(
    Double3CompoundBaseAttrOperator[WorldNormalPlugOperator]
):
    __slots__ = ()

    worldNormalX = DoubleField(default_value=0.0, writable=False)
    wnx = worldNormalX

    worldNormalY = DoubleField(default_value=0.0, writable=False)
    wny = worldNormalY

    worldNormalZ = DoubleField(default_value=0.0, writable=False)
    wnz = worldNormalZ


class WorldNormalField(
    Double3CompoundBaseField[WorldNormalAttrOperator, WorldNormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WorldNormalAttrOperator
    PLUG_CLS = WorldNormalPlugOperator


class EditPointsPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["EditPointsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("xValueEp", "xve"),
        ("yValueEp", "yve"),
        ("zValueEp", "zve"),
    )

    xValueEp = DoubleLinearField(default_value=0.0, writable=False)
    xve = xValueEp

    yValueEp = DoubleLinearField(default_value=0.0, writable=False)
    yve = yValueEp

    zValueEp = DoubleLinearField(default_value=0.0, writable=False)
    zve = zValueEp


class EditPointsAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[EditPointsPlugOperator]
):
    __slots__ = ()

    xValueEp = DoubleLinearField(default_value=0.0, writable=False)
    xve = xValueEp

    yValueEp = DoubleLinearField(default_value=0.0, writable=False)
    yve = yValueEp

    zValueEp = DoubleLinearField(default_value=0.0, writable=False)
    zve = zValueEp


class EditPointsField(
    DoubleLinear3CompoundBaseField[
        EditPointsAttrOperator, EditPointsPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = EditPointsAttrOperator
    PLUG_CLS = EditPointsPlugOperator


class MinMaxValuePlugOperator(
    Double2CompoundBasePlugOperator["MinMaxValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minValue", "min"),
        ("maxValue", "max"),
    )

    minValue = DoubleField(default_value=0.0, writable=False)
    min = minValue

    maxValue = DoubleField(default_value=0.0, writable=False)
    max = maxValue


class MinMaxValueAttrOperator(
    Double2CompoundBaseAttrOperator[MinMaxValuePlugOperator]
):
    __slots__ = ()

    minValue = DoubleField(default_value=0.0, writable=False)
    min = minValue

    maxValue = DoubleField(default_value=0.0, writable=False)
    max = maxValue


class MinMaxValueField(
    Double2CompoundBaseField[MinMaxValueAttrOperator, MinMaxValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MinMaxValueAttrOperator
    PLUG_CLS = MinMaxValuePlugOperator

    minValue = DoubleField(default_value=0.0, writable=False)
    min = minValue

    maxValue = DoubleField(default_value=0.0, writable=False)
    max = maxValue


class AiCurveShaderPlugOperator(
    Float3CompoundBasePlugOperator["AiCurveShaderAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiCurveShaderR", "ai_curve_shaderr"),
        ("aiCurveShaderG", "ai_curve_shaderg"),
        ("aiCurveShaderB", "ai_curve_shaderb"),
    )

    aiCurveShaderR = FloatField(default_value=0.0)
    ai_curve_shaderr = aiCurveShaderR

    aiCurveShaderG = FloatField(default_value=0.0)
    ai_curve_shaderg = aiCurveShaderG

    aiCurveShaderB = FloatField(default_value=0.0)
    ai_curve_shaderb = aiCurveShaderB


class AiCurveShaderAttrOperator(
    Float3CompoundBaseAttrOperator[AiCurveShaderPlugOperator]
):
    __slots__ = ()

    aiCurveShaderR = FloatField(default_value=0.0)
    ai_curve_shaderr = aiCurveShaderR

    aiCurveShaderG = FloatField(default_value=0.0)
    ai_curve_shaderg = aiCurveShaderG

    aiCurveShaderB = FloatField(default_value=0.0)
    ai_curve_shaderb = aiCurveShaderB


class AiCurveShaderField(
    Float3CompoundBaseField[
        AiCurveShaderAttrOperator, AiCurveShaderPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiCurveShaderAttrOperator
    PLUG_CLS = AiCurveShaderPlugOperator

    aiCurveShaderR = FloatField(default_value=0.0)
    ai_curve_shaderr = aiCurveShaderR

    aiCurveShaderG = FloatField(default_value=0.0)
    ai_curve_shaderg = aiCurveShaderG

    aiCurveShaderB = FloatField(default_value=0.0)
    ai_curve_shaderb = aiCurveShaderB
