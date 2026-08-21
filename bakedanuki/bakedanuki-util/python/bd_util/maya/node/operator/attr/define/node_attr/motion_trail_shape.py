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


class LocalPositionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["LocalPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localPositionX", "lpx"),
        ("localPositionY", "lpy"),
        ("localPositionZ", "lpz"),
    )

    localPositionX = DoubleLinearField(default_value=0.0)
    lpx = localPositionX

    localPositionY = DoubleLinearField(default_value=0.0)
    lpy = localPositionY

    localPositionZ = DoubleLinearField(default_value=0.0)
    lpz = localPositionZ


class LocalPositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[LocalPositionPlugOperator]
):
    __slots__ = ()

    localPositionX = DoubleLinearField(default_value=0.0)
    lpx = localPositionX

    localPositionY = DoubleLinearField(default_value=0.0)
    lpy = localPositionY

    localPositionZ = DoubleLinearField(default_value=0.0)
    lpz = localPositionZ


class LocalPositionField(
    DoubleLinear3CompoundBaseField[
        LocalPositionAttrOperator, LocalPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = LocalPositionAttrOperator
    PLUG_CLS = LocalPositionPlugOperator

    localPositionX = DoubleLinearField(default_value=0.0)
    lpx = localPositionX

    localPositionY = DoubleLinearField(default_value=0.0)
    lpy = localPositionY

    localPositionZ = DoubleLinearField(default_value=0.0)
    lpz = localPositionZ


class TrailColorPlugOperator(
    Float3CompoundBasePlugOperator["TrailColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("trailColorR", "tcr"),
        ("trailColorG", "tcg"),
        ("trailColorB", "tcb"),
    )

    trailColorR = FloatField(default_value=0.49000000953674316)
    tcr = trailColorR

    trailColorG = FloatField(default_value=0.09799999743700027)
    tcg = trailColorG

    trailColorB = FloatField(default_value=0.125)
    tcb = trailColorB


class TrailColorAttrOperator(
    Float3CompoundBaseAttrOperator[TrailColorPlugOperator]
):
    __slots__ = ()

    trailColorR = FloatField(default_value=0.49000000953674316)
    tcr = trailColorR

    trailColorG = FloatField(default_value=0.09799999743700027)
    tcg = trailColorG

    trailColorB = FloatField(default_value=0.125)
    tcb = trailColorB


class TrailColorField(
    Float3CompoundBaseField[TrailColorAttrOperator, TrailColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TrailColorAttrOperator
    PLUG_CLS = TrailColorPlugOperator

    trailColorR = FloatField(default_value=0.49000000953674316)
    tcr = trailColorR

    trailColorG = FloatField(default_value=0.09799999743700027)
    tcg = trailColorG

    trailColorB = FloatField(default_value=0.125)
    tcb = trailColorB


class ExtraTrailColorPlugOperator(
    Float3CompoundBasePlugOperator["ExtraTrailColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("extraTrailColorR", "etcr"),
        ("extraTrailColorG", "etcg"),
        ("extraTrailColorB", "etcb"),
    )

    extraTrailColorR = FloatField(default_value=0.125)
    etcr = extraTrailColorR

    extraTrailColorG = FloatField(default_value=0.09799999743700027)
    etcg = extraTrailColorG

    extraTrailColorB = FloatField(default_value=0.49000000953674316)
    etcb = extraTrailColorB


class ExtraTrailColorAttrOperator(
    Float3CompoundBaseAttrOperator[ExtraTrailColorPlugOperator]
):
    __slots__ = ()

    extraTrailColorR = FloatField(default_value=0.125)
    etcr = extraTrailColorR

    extraTrailColorG = FloatField(default_value=0.09799999743700027)
    etcg = extraTrailColorG

    extraTrailColorB = FloatField(default_value=0.49000000953674316)
    etcb = extraTrailColorB


class ExtraTrailColorField(
    Float3CompoundBaseField[
        ExtraTrailColorAttrOperator, ExtraTrailColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ExtraTrailColorAttrOperator
    PLUG_CLS = ExtraTrailColorPlugOperator

    extraTrailColorR = FloatField(default_value=0.125)
    etcr = extraTrailColorR

    extraTrailColorG = FloatField(default_value=0.09799999743700027)
    etcg = extraTrailColorG

    extraTrailColorB = FloatField(default_value=0.49000000953674316)
    etcb = extraTrailColorB


class KeyframeColorPlugOperator(
    Float3CompoundBasePlugOperator["KeyframeColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("keyframeColorR", "kcr"),
        ("keyframeColorG", "kcg"),
        ("keyframeColorB", "kcb"),
    )

    keyframeColorR = FloatField(default_value=1.0)
    kcr = keyframeColorR

    keyframeColorG = FloatField(default_value=1.0)
    kcg = keyframeColorG

    keyframeColorB = FloatField(default_value=1.0)
    kcb = keyframeColorB


class KeyframeColorAttrOperator(
    Float3CompoundBaseAttrOperator[KeyframeColorPlugOperator]
):
    __slots__ = ()

    keyframeColorR = FloatField(default_value=1.0)
    kcr = keyframeColorR

    keyframeColorG = FloatField(default_value=1.0)
    kcg = keyframeColorG

    keyframeColorB = FloatField(default_value=1.0)
    kcb = keyframeColorB


class KeyframeColorField(
    Float3CompoundBaseField[
        KeyframeColorAttrOperator, KeyframeColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = KeyframeColorAttrOperator
    PLUG_CLS = KeyframeColorPlugOperator

    keyframeColorR = FloatField(default_value=1.0)
    kcr = keyframeColorR

    keyframeColorG = FloatField(default_value=1.0)
    kcg = keyframeColorG

    keyframeColorB = FloatField(default_value=1.0)
    kcb = keyframeColorB


class ActiveKeyframeColorPlugOperator(
    Float3CompoundBasePlugOperator["ActiveKeyframeColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("activeKeyframeColorR", "akr"),
        ("activeKeyframeColorG", "akg"),
        ("activeKeyframeColorB", "akb"),
    )

    activeKeyframeColorR = FloatField(default_value=1.0)
    akr = activeKeyframeColorR

    activeKeyframeColorG = FloatField(default_value=1.0)
    akg = activeKeyframeColorG

    activeKeyframeColorB = FloatField(default_value=0.0)
    akb = activeKeyframeColorB


class ActiveKeyframeColorAttrOperator(
    Float3CompoundBaseAttrOperator[ActiveKeyframeColorPlugOperator]
):
    __slots__ = ()

    activeKeyframeColorR = FloatField(default_value=1.0)
    akr = activeKeyframeColorR

    activeKeyframeColorG = FloatField(default_value=1.0)
    akg = activeKeyframeColorG

    activeKeyframeColorB = FloatField(default_value=0.0)
    akb = activeKeyframeColorB


class ActiveKeyframeColorField(
    Float3CompoundBaseField[
        ActiveKeyframeColorAttrOperator, ActiveKeyframeColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ActiveKeyframeColorAttrOperator
    PLUG_CLS = ActiveKeyframeColorPlugOperator

    activeKeyframeColorR = FloatField(default_value=1.0)
    akr = activeKeyframeColorR

    activeKeyframeColorG = FloatField(default_value=1.0)
    akg = activeKeyframeColorG

    activeKeyframeColorB = FloatField(default_value=0.0)
    akb = activeKeyframeColorB


class BeadColorPlugOperator(
    Float3CompoundBasePlugOperator["BeadColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("beadColorR", "bcr"),
        ("beadColorG", "bcg"),
        ("beadColorB", "bcb"),
    )

    beadColorR = FloatField(default_value=1.0)
    bcr = beadColorR

    beadColorG = FloatField(default_value=0.0)
    bcg = beadColorG

    beadColorB = FloatField(default_value=1.0)
    bcb = beadColorB


class BeadColorAttrOperator(
    Float3CompoundBaseAttrOperator[BeadColorPlugOperator]
):
    __slots__ = ()

    beadColorR = FloatField(default_value=1.0)
    bcr = beadColorR

    beadColorG = FloatField(default_value=0.0)
    bcg = beadColorG

    beadColorB = FloatField(default_value=1.0)
    bcb = beadColorB


class BeadColorField(
    Float3CompoundBaseField[BeadColorAttrOperator, BeadColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BeadColorAttrOperator
    PLUG_CLS = BeadColorPlugOperator

    beadColorR = FloatField(default_value=1.0)
    bcr = beadColorR

    beadColorG = FloatField(default_value=0.0)
    bcg = beadColorG

    beadColorB = FloatField(default_value=1.0)
    bcb = beadColorB


class SlowTrailColorPlugOperator(
    Float3CompoundBasePlugOperator["SlowTrailColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("slowTrailColorR", "str"),
        ("slowTrailColorG", "stg"),
        ("slowTrailColorB", "stb"),
    )

    slowTrailColorR = FloatField(default_value=0.23000000417232513)
    str = slowTrailColorR

    slowTrailColorG = FloatField(default_value=0.07100000232458115)
    stg = slowTrailColorG

    slowTrailColorB = FloatField(default_value=0.40400001406669617)
    stb = slowTrailColorB


class SlowTrailColorAttrOperator(
    Float3CompoundBaseAttrOperator[SlowTrailColorPlugOperator]
):
    __slots__ = ()

    slowTrailColorR = FloatField(default_value=0.23000000417232513)
    str = slowTrailColorR

    slowTrailColorG = FloatField(default_value=0.07100000232458115)
    stg = slowTrailColorG

    slowTrailColorB = FloatField(default_value=0.40400001406669617)
    stb = slowTrailColorB


class SlowTrailColorField(
    Float3CompoundBaseField[
        SlowTrailColorAttrOperator, SlowTrailColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SlowTrailColorAttrOperator
    PLUG_CLS = SlowTrailColorPlugOperator

    slowTrailColorR = FloatField(default_value=0.23000000417232513)
    str = slowTrailColorR

    slowTrailColorG = FloatField(default_value=0.07100000232458115)
    stg = slowTrailColorG

    slowTrailColorB = FloatField(default_value=0.40400001406669617)
    stb = slowTrailColorB


class FastTrailColorPlugOperator(
    Float3CompoundBasePlugOperator["FastTrailColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fastTrailColorR", "ftr"),
        ("fastTrailColorG", "ftg"),
        ("fastTrailColorB", "ftb"),
    )

    fastTrailColorR = FloatField(default_value=0.6119999885559082)
    ftr = fastTrailColorR

    fastTrailColorG = FloatField(default_value=0.0)
    ftg = fastTrailColorG

    fastTrailColorB = FloatField(default_value=0.0)
    ftb = fastTrailColorB


class FastTrailColorAttrOperator(
    Float3CompoundBaseAttrOperator[FastTrailColorPlugOperator]
):
    __slots__ = ()

    fastTrailColorR = FloatField(default_value=0.6119999885559082)
    ftr = fastTrailColorR

    fastTrailColorG = FloatField(default_value=0.0)
    ftg = fastTrailColorG

    fastTrailColorB = FloatField(default_value=0.0)
    ftb = fastTrailColorB


class FastTrailColorField(
    Float3CompoundBaseField[
        FastTrailColorAttrOperator, FastTrailColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = FastTrailColorAttrOperator
    PLUG_CLS = FastTrailColorPlugOperator

    fastTrailColorR = FloatField(default_value=0.6119999885559082)
    ftr = fastTrailColorR

    fastTrailColorG = FloatField(default_value=0.0)
    ftg = fastTrailColorG

    fastTrailColorB = FloatField(default_value=0.0)
    ftb = fastTrailColorB


class TangentPointsPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["TangentPointsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("txValue", "txv"),
        ("tyValue", "tyv"),
        ("tzValue", "tzv"),
    )

    txValue = DoubleLinearField(default_value=0.0)
    txv = txValue

    tyValue = DoubleLinearField(default_value=0.0)
    tyv = tyValue

    tzValue = DoubleLinearField(default_value=0.0)
    tzv = tzValue


class TangentPointsAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[TangentPointsPlugOperator]
):
    __slots__ = ()

    txValue = DoubleLinearField(default_value=0.0)
    txv = txValue

    tyValue = DoubleLinearField(default_value=0.0)
    tyv = tyValue

    tzValue = DoubleLinearField(default_value=0.0)
    tzv = tzValue


class TangentPointsField(
    DoubleLinear3CompoundBaseField[
        TangentPointsAttrOperator, TangentPointsPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = TangentPointsAttrOperator
    PLUG_CLS = TangentPointsPlugOperator


class FrameMarkerColorPlugOperator(
    Float3CompoundBasePlugOperator["FrameMarkerColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("frameMarkerColorR", "fcr"),
        ("frameMarkerColorG", "fcg"),
        ("frameMarkerColorB", "fcb"),
    )

    frameMarkerColorR = FloatField(default_value=0.1550000011920929)
    fcr = frameMarkerColorR

    frameMarkerColorG = FloatField(default_value=0.5529999732971191)
    fcg = frameMarkerColorG

    frameMarkerColorB = FloatField(default_value=0.11100000143051147)
    fcb = frameMarkerColorB


class FrameMarkerColorAttrOperator(
    Float3CompoundBaseAttrOperator[FrameMarkerColorPlugOperator]
):
    __slots__ = ()

    frameMarkerColorR = FloatField(default_value=0.1550000011920929)
    fcr = frameMarkerColorR

    frameMarkerColorG = FloatField(default_value=0.5529999732971191)
    fcg = frameMarkerColorG

    frameMarkerColorB = FloatField(default_value=0.11100000143051147)
    fcb = frameMarkerColorB


class FrameMarkerColorField(
    Float3CompoundBaseField[
        FrameMarkerColorAttrOperator, FrameMarkerColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = FrameMarkerColorAttrOperator
    PLUG_CLS = FrameMarkerColorPlugOperator

    frameMarkerColorR = FloatField(default_value=0.1550000011920929)
    fcr = frameMarkerColorR

    frameMarkerColorG = FloatField(default_value=0.5529999732971191)
    fcg = frameMarkerColorG

    frameMarkerColorB = FloatField(default_value=0.11100000143051147)
    fcb = frameMarkerColorB


class ExtraKeyframeColorPlugOperator(
    Float3CompoundBasePlugOperator["ExtraKeyframeColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("extraKeyframeColorR", "ecr"),
        ("extraKeyframeColorG", "ecg"),
        ("extraKeyframeColorB", "ecb"),
    )

    extraKeyframeColorR = FloatField(default_value=0.45100000500679016)
    ecr = extraKeyframeColorR

    extraKeyframeColorG = FloatField(default_value=0.45100000500679016)
    ecg = extraKeyframeColorG

    extraKeyframeColorB = FloatField(default_value=0.45100000500679016)
    ecb = extraKeyframeColorB


class ExtraKeyframeColorAttrOperator(
    Float3CompoundBaseAttrOperator[ExtraKeyframeColorPlugOperator]
):
    __slots__ = ()

    extraKeyframeColorR = FloatField(default_value=0.45100000500679016)
    ecr = extraKeyframeColorR

    extraKeyframeColorG = FloatField(default_value=0.45100000500679016)
    ecg = extraKeyframeColorG

    extraKeyframeColorB = FloatField(default_value=0.45100000500679016)
    ecb = extraKeyframeColorB


class ExtraKeyframeColorField(
    Float3CompoundBaseField[
        ExtraKeyframeColorAttrOperator, ExtraKeyframeColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ExtraKeyframeColorAttrOperator
    PLUG_CLS = ExtraKeyframeColorPlugOperator

    extraKeyframeColorR = FloatField(default_value=0.45100000500679016)
    ecr = extraKeyframeColorR

    extraKeyframeColorG = FloatField(default_value=0.45100000500679016)
    ecg = extraKeyframeColorG

    extraKeyframeColorB = FloatField(default_value=0.45100000500679016)
    ecb = extraKeyframeColorB
