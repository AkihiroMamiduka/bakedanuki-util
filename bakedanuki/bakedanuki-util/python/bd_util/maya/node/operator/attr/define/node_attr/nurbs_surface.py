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
from ..std.at.scalar.numeric.range.short import ShortField
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
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    Short2CompoundBaseAttrOperator,
    Short2CompoundBasePlugOperator,
    Short2CompoundBaseField,
    Long2CompoundBaseAttrOperator,
    Long2CompoundBasePlugOperator,
    Long2CompoundBaseField,
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


class CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumPlugOperator(
    EnumPlugOperator[
        "CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumAttrOperator"
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumAttrOperator(
    EnumAttrOperator[
        CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumPlugOperator
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumField(
    EnumField[
        CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumAttrOperator,
        CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumAttrOperator
    PLUG_CLS = CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumPlugOperator


class CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumPlugOperator(
    EnumPlugOperator[
        "CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumAttrOperator"
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumAttrOperator(
    EnumAttrOperator[
        CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumPlugOperator
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumField(
    EnumField[
        CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumAttrOperator,
        CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumAttrOperator
    PLUG_CLS = CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumPlugOperator


class CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumPlugOperator(
    EnumPlugOperator[
        "CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumAttrOperator"
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumAttrOperator(
    EnumAttrOperator[
        CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumPlugOperator
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumField(
    EnumField[
        CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumAttrOperator,
        CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumAttrOperator
    PLUG_CLS = CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumPlugOperator


class CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumPlugOperator(
    EnumPlugOperator[
        "CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumAttrOperator"
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumAttrOperator(
    EnumAttrOperator[
        CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumPlugOperator
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumField(
    EnumField[
        CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumAttrOperator,
        CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumAttrOperator
    PLUG_CLS = CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumPlugOperator


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


class BoundingBoxScalePlugOperator(
    Float3CompoundBasePlugOperator["BoundingBoxScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("boundingBoxScaleX", "bscx"),
        ("boundingBoxScaleY", "bscy"),
        ("boundingBoxScaleZ", "bscz"),
    )

    boundingBoxScaleX = FloatField(default_value=1.5, min_value=1.0)
    bscx = boundingBoxScaleX

    boundingBoxScaleY = FloatField(default_value=1.5, min_value=1.0)
    bscy = boundingBoxScaleY

    boundingBoxScaleZ = FloatField(default_value=1.5, min_value=1.0)
    bscz = boundingBoxScaleZ


class BoundingBoxScaleAttrOperator(
    Float3CompoundBaseAttrOperator[BoundingBoxScalePlugOperator]
):
    __slots__ = ()

    boundingBoxScaleX = FloatField(default_value=1.5, min_value=1.0)
    bscx = boundingBoxScaleX

    boundingBoxScaleY = FloatField(default_value=1.5, min_value=1.0)
    bscy = boundingBoxScaleY

    boundingBoxScaleZ = FloatField(default_value=1.5, min_value=1.0)
    bscz = boundingBoxScaleZ


class BoundingBoxScaleField(
    Float3CompoundBaseField[
        BoundingBoxScaleAttrOperator, BoundingBoxScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = BoundingBoxScaleAttrOperator
    PLUG_CLS = BoundingBoxScalePlugOperator

    boundingBoxScaleX = FloatField(default_value=1.5, min_value=1.0)
    bscx = boundingBoxScaleX

    boundingBoxScaleY = FloatField(default_value=1.5, min_value=1.0)
    bscy = boundingBoxScaleY

    boundingBoxScaleZ = FloatField(default_value=1.5, min_value=1.0)
    bscz = boundingBoxScaleZ


class CollisionOffsetVelocityIncrementPlugOperator(
    CompoundPlugOperator["CollisionOffsetVelocityIncrementAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionOffsetVelocityIncrement_Position", "covip"),
        ("collisionOffsetVelocityIncrement_FloatValue", "covifv"),
        ("collisionOffsetVelocityIncrement_Interp", "covii"),
    )

    collisionOffsetVelocityIncrement_Position = FloatField(default_value=0.0)
    covip = collisionOffsetVelocityIncrement_Position

    collisionOffsetVelocityIncrement_FloatValue = FloatField(default_value=0.0)
    covifv = collisionOffsetVelocityIncrement_FloatValue

    collisionOffsetVelocityIncrement_Interp = CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumField(
        default_value=0
    )
    covii = collisionOffsetVelocityIncrement_Interp


class CollisionOffsetVelocityIncrementAttrOperator(
    CompoundAttrOperator[CollisionOffsetVelocityIncrementPlugOperator]
):
    __slots__ = ()

    collisionOffsetVelocityIncrement_Position = FloatField(default_value=0.0)
    covip = collisionOffsetVelocityIncrement_Position

    collisionOffsetVelocityIncrement_FloatValue = FloatField(default_value=0.0)
    covifv = collisionOffsetVelocityIncrement_FloatValue

    collisionOffsetVelocityIncrement_Interp = CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumField(
        default_value=0
    )
    covii = collisionOffsetVelocityIncrement_Interp


class CollisionOffsetVelocityIncrementField(
    CompoundField[
        CollisionOffsetVelocityIncrementAttrOperator,
        CollisionOffsetVelocityIncrementPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionOffsetVelocityIncrementAttrOperator
    PLUG_CLS = CollisionOffsetVelocityIncrementPlugOperator


class CollisionDepthVelocityIncrementPlugOperator(
    CompoundPlugOperator["CollisionDepthVelocityIncrementAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionDepthVelocityIncrement_Position", "cdvip"),
        ("collisionDepthVelocityIncrement_FloatValue", "cdvifv"),
        ("collisionDepthVelocityIncrement_Interp", "cdvii"),
    )

    collisionDepthVelocityIncrement_Position = FloatField(default_value=0.0)
    cdvip = collisionDepthVelocityIncrement_Position

    collisionDepthVelocityIncrement_FloatValue = FloatField(default_value=0.0)
    cdvifv = collisionDepthVelocityIncrement_FloatValue

    collisionDepthVelocityIncrement_Interp = CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumField(
        default_value=0
    )
    cdvii = collisionDepthVelocityIncrement_Interp


class CollisionDepthVelocityIncrementAttrOperator(
    CompoundAttrOperator[CollisionDepthVelocityIncrementPlugOperator]
):
    __slots__ = ()

    collisionDepthVelocityIncrement_Position = FloatField(default_value=0.0)
    cdvip = collisionDepthVelocityIncrement_Position

    collisionDepthVelocityIncrement_FloatValue = FloatField(default_value=0.0)
    cdvifv = collisionDepthVelocityIncrement_FloatValue

    collisionDepthVelocityIncrement_Interp = CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumField(
        default_value=0
    )
    cdvii = collisionDepthVelocityIncrement_Interp


class CollisionDepthVelocityIncrementField(
    CompoundField[
        CollisionDepthVelocityIncrementAttrOperator,
        CollisionDepthVelocityIncrementPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionDepthVelocityIncrementAttrOperator
    PLUG_CLS = CollisionDepthVelocityIncrementPlugOperator


class CollisionOffsetVelocityMultiplierPlugOperator(
    CompoundPlugOperator["CollisionOffsetVelocityMultiplierAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionOffsetVelocityMultiplier_Position", "covmp"),
        ("collisionOffsetVelocityMultiplier_FloatValue", "covmfv"),
        ("collisionOffsetVelocityMultiplier_Interp", "covmi"),
    )

    collisionOffsetVelocityMultiplier_Position = FloatField(default_value=0.0)
    covmp = collisionOffsetVelocityMultiplier_Position

    collisionOffsetVelocityMultiplier_FloatValue = FloatField(
        default_value=0.0
    )
    covmfv = collisionOffsetVelocityMultiplier_FloatValue

    collisionOffsetVelocityMultiplier_Interp = CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumField(
        default_value=0
    )
    covmi = collisionOffsetVelocityMultiplier_Interp


class CollisionOffsetVelocityMultiplierAttrOperator(
    CompoundAttrOperator[CollisionOffsetVelocityMultiplierPlugOperator]
):
    __slots__ = ()

    collisionOffsetVelocityMultiplier_Position = FloatField(default_value=0.0)
    covmp = collisionOffsetVelocityMultiplier_Position

    collisionOffsetVelocityMultiplier_FloatValue = FloatField(
        default_value=0.0
    )
    covmfv = collisionOffsetVelocityMultiplier_FloatValue

    collisionOffsetVelocityMultiplier_Interp = CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumField(
        default_value=0
    )
    covmi = collisionOffsetVelocityMultiplier_Interp


class CollisionOffsetVelocityMultiplierField(
    CompoundField[
        CollisionOffsetVelocityMultiplierAttrOperator,
        CollisionOffsetVelocityMultiplierPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionOffsetVelocityMultiplierAttrOperator
    PLUG_CLS = CollisionOffsetVelocityMultiplierPlugOperator


class CollisionDepthVelocityMultiplierPlugOperator(
    CompoundPlugOperator["CollisionDepthVelocityMultiplierAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionDepthVelocityMultiplier_Position", "cdvmp"),
        ("collisionDepthVelocityMultiplier_FloatValue", "cdvmfv"),
        ("collisionDepthVelocityMultiplier_Interp", "cdvmi"),
    )

    collisionDepthVelocityMultiplier_Position = FloatField(default_value=0.0)
    cdvmp = collisionDepthVelocityMultiplier_Position

    collisionDepthVelocityMultiplier_FloatValue = FloatField(default_value=0.0)
    cdvmfv = collisionDepthVelocityMultiplier_FloatValue

    collisionDepthVelocityMultiplier_Interp = CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumField(
        default_value=0
    )
    cdvmi = collisionDepthVelocityMultiplier_Interp


class CollisionDepthVelocityMultiplierAttrOperator(
    CompoundAttrOperator[CollisionDepthVelocityMultiplierPlugOperator]
):
    __slots__ = ()

    collisionDepthVelocityMultiplier_Position = FloatField(default_value=0.0)
    cdvmp = collisionDepthVelocityMultiplier_Position

    collisionDepthVelocityMultiplier_FloatValue = FloatField(default_value=0.0)
    cdvmfv = collisionDepthVelocityMultiplier_FloatValue

    collisionDepthVelocityMultiplier_Interp = CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumField(
        default_value=0
    )
    cdvmi = collisionDepthVelocityMultiplier_Interp


class CollisionDepthVelocityMultiplierField(
    CompoundField[
        CollisionDepthVelocityMultiplierAttrOperator,
        CollisionDepthVelocityMultiplierPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionDepthVelocityMultiplierAttrOperator
    PLUG_CLS = CollisionDepthVelocityMultiplierPlugOperator


class MinMaxRangeUPlugOperator(
    Double2CompoundBasePlugOperator["MinMaxRangeUAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minValueU", "mnu"),
        ("maxValueU", "mxu"),
    )

    minValueU = DoubleField(default_value=0.0, writable=False)
    mnu = minValueU

    maxValueU = DoubleField(default_value=0.0, writable=False)
    mxu = maxValueU


class MinMaxRangeUAttrOperator(
    Double2CompoundBaseAttrOperator[MinMaxRangeUPlugOperator]
):
    __slots__ = ()

    minValueU = DoubleField(default_value=0.0, writable=False)
    mnu = minValueU

    maxValueU = DoubleField(default_value=0.0, writable=False)
    mxu = maxValueU


class MinMaxRangeUField(
    Double2CompoundBaseField[
        MinMaxRangeUAttrOperator, MinMaxRangeUPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = MinMaxRangeUAttrOperator
    PLUG_CLS = MinMaxRangeUPlugOperator

    minValueU = DoubleField(default_value=0.0, writable=False)
    mnu = minValueU

    maxValueU = DoubleField(default_value=0.0, writable=False)
    mxu = maxValueU


class MinMaxRangeVPlugOperator(
    Double2CompoundBasePlugOperator["MinMaxRangeVAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minValueV", "mnv"),
        ("maxValueV", "mxv"),
    )

    minValueV = DoubleField(default_value=0.0, writable=False)
    mnv = minValueV

    maxValueV = DoubleField(default_value=0.0, writable=False)
    mxv = maxValueV


class MinMaxRangeVAttrOperator(
    Double2CompoundBaseAttrOperator[MinMaxRangeVPlugOperator]
):
    __slots__ = ()

    minValueV = DoubleField(default_value=0.0, writable=False)
    mnv = minValueV

    maxValueV = DoubleField(default_value=0.0, writable=False)
    mxv = maxValueV


class MinMaxRangeVField(
    Double2CompoundBaseField[
        MinMaxRangeVAttrOperator, MinMaxRangeVPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = MinMaxRangeVAttrOperator
    PLUG_CLS = MinMaxRangeVPlugOperator

    minValueV = DoubleField(default_value=0.0, writable=False)
    mnv = minValueV

    maxValueV = DoubleField(default_value=0.0, writable=False)
    mxv = maxValueV


class DegreeUVPlugOperator(
    Short2CompoundBasePlugOperator["DegreeUVAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("degreeU", "du"),
        ("degreeV", "dv"),
    )

    degreeU = ShortField(default_value=0, writable=False)
    du = degreeU

    degreeV = ShortField(default_value=0, writable=False)
    dv = degreeV


class DegreeUVAttrOperator(
    Short2CompoundBaseAttrOperator[DegreeUVPlugOperator]
):
    __slots__ = ()

    degreeU = ShortField(default_value=0, writable=False)
    du = degreeU

    degreeV = ShortField(default_value=0, writable=False)
    dv = degreeV


class DegreeUVField(
    Short2CompoundBaseField[DegreeUVAttrOperator, DegreeUVPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DegreeUVAttrOperator
    PLUG_CLS = DegreeUVPlugOperator

    degreeU = ShortField(default_value=0, writable=False)
    du = degreeU

    degreeV = ShortField(default_value=0, writable=False)
    dv = degreeV


class SpansUVPlugOperator(
    Long2CompoundBasePlugOperator["SpansUVAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("spansU", "su"),
        ("spansV", "sv"),
    )

    spansU = LongField(default_value=0, writable=False)
    su = spansU

    spansV = LongField(default_value=0, writable=False)
    sv = spansV


class SpansUVAttrOperator(Long2CompoundBaseAttrOperator[SpansUVPlugOperator]):
    __slots__ = ()

    spansU = LongField(default_value=0, writable=False)
    su = spansU

    spansV = LongField(default_value=0, writable=False)
    sv = spansV


class SpansUVField(
    Long2CompoundBaseField[SpansUVAttrOperator, SpansUVPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpansUVAttrOperator
    PLUG_CLS = SpansUVPlugOperator

    spansU = LongField(default_value=0, writable=False)
    su = spansU

    spansV = LongField(default_value=0, writable=False)
    sv = spansV
