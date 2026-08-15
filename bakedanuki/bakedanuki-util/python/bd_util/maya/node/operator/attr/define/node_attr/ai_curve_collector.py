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
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class AiWidthProfile_aiWidthProfile_InterpEnumPlugOperator(
    EnumPlugOperator["AiWidthProfile_aiWidthProfile_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class AiWidthProfile_aiWidthProfile_InterpEnumAttrOperator(
    EnumAttrOperator[AiWidthProfile_aiWidthProfile_InterpEnumPlugOperator]
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


class AiWidthProfile_aiWidthProfile_InterpEnumField(
    EnumField[
        AiWidthProfile_aiWidthProfile_InterpEnumAttrOperator,
        AiWidthProfile_aiWidthProfile_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = AiWidthProfile_aiWidthProfile_InterpEnumAttrOperator
    PLUG_CLS = AiWidthProfile_aiWidthProfile_InterpEnumPlugOperator


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


class WorldPositionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["WorldPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldPositionX", "wpx"),
        ("worldPositionY", "wpy"),
        ("worldPositionZ", "wpz"),
    )

    worldPositionX = DoubleLinearField(default_value=0.0, writable=False)
    wpx = worldPositionX

    worldPositionY = DoubleLinearField(default_value=0.0, writable=False)
    wpy = worldPositionY

    worldPositionZ = DoubleLinearField(default_value=0.0, writable=False)
    wpz = worldPositionZ


class WorldPositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[WorldPositionPlugOperator]
):
    __slots__ = ()

    worldPositionX = DoubleLinearField(default_value=0.0, writable=False)
    wpx = worldPositionX

    worldPositionY = DoubleLinearField(default_value=0.0, writable=False)
    wpy = worldPositionY

    worldPositionZ = DoubleLinearField(default_value=0.0, writable=False)
    wpz = worldPositionZ


class WorldPositionField(
    DoubleLinear3CompoundBaseField[
        WorldPositionAttrOperator, WorldPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = WorldPositionAttrOperator
    PLUG_CLS = WorldPositionPlugOperator


class LocalScalePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["LocalScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localScaleX", "lsx"),
        ("localScaleY", "lsy"),
        ("localScaleZ", "lsz"),
    )

    localScaleX = DoubleLinearField(default_value=1.0)
    lsx = localScaleX

    localScaleY = DoubleLinearField(default_value=1.0)
    lsy = localScaleY

    localScaleZ = DoubleLinearField(default_value=1.0)
    lsz = localScaleZ


class LocalScaleAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[LocalScalePlugOperator]
):
    __slots__ = ()

    localScaleX = DoubleLinearField(default_value=1.0)
    lsx = localScaleX

    localScaleY = DoubleLinearField(default_value=1.0)
    lsy = localScaleY

    localScaleZ = DoubleLinearField(default_value=1.0)
    lsz = localScaleZ


class LocalScaleField(
    DoubleLinear3CompoundBaseField[
        LocalScaleAttrOperator, LocalScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = LocalScaleAttrOperator
    PLUG_CLS = LocalScalePlugOperator

    localScaleX = DoubleLinearField(default_value=1.0)
    lsx = localScaleX

    localScaleY = DoubleLinearField(default_value=1.0)
    lsy = localScaleY

    localScaleZ = DoubleLinearField(default_value=1.0)
    lsz = localScaleZ


class AiCurveShaderPlugOperator(
    Float3CompoundBasePlugOperator["AiCurveShaderAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiCurveShaderR", "aiCurveShaderr"),
        ("aiCurveShaderG", "aiCurveShaderg"),
        ("aiCurveShaderB", "aiCurveShaderb"),
    )

    aiCurveShaderR = FloatField(default_value=0.0)
    aiCurveShaderr = aiCurveShaderR

    aiCurveShaderG = FloatField(default_value=0.0)
    aiCurveShaderg = aiCurveShaderG

    aiCurveShaderB = FloatField(default_value=0.0)
    aiCurveShaderb = aiCurveShaderB


class AiCurveShaderAttrOperator(
    Float3CompoundBaseAttrOperator[AiCurveShaderPlugOperator]
):
    __slots__ = ()

    aiCurveShaderR = FloatField(default_value=0.0)
    aiCurveShaderr = aiCurveShaderR

    aiCurveShaderG = FloatField(default_value=0.0)
    aiCurveShaderg = aiCurveShaderG

    aiCurveShaderB = FloatField(default_value=0.0)
    aiCurveShaderb = aiCurveShaderB


class AiCurveShaderField(
    Float3CompoundBaseField[
        AiCurveShaderAttrOperator, AiCurveShaderPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiCurveShaderAttrOperator
    PLUG_CLS = AiCurveShaderPlugOperator

    aiCurveShaderR = FloatField(default_value=0.0)
    aiCurveShaderr = aiCurveShaderR

    aiCurveShaderG = FloatField(default_value=0.0)
    aiCurveShaderg = aiCurveShaderG

    aiCurveShaderB = FloatField(default_value=0.0)
    aiCurveShaderb = aiCurveShaderB


class AiWidthProfilePlugOperator(
    CompoundPlugOperator["AiWidthProfileAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiWidthProfile_Position", "wdthPp"),
        ("aiWidthProfile_FloatValue", "wdthPfv"),
        ("aiWidthProfile_Interp", "wdthPi"),
    )

    aiWidthProfile_Position = FloatField(default_value=0.0)
    wdthPp = aiWidthProfile_Position

    aiWidthProfile_FloatValue = FloatField(default_value=0.0)
    wdthPfv = aiWidthProfile_FloatValue

    aiWidthProfile_Interp = AiWidthProfile_aiWidthProfile_InterpEnumField(
        default_value=1
    )
    wdthPi = aiWidthProfile_Interp


class AiWidthProfileAttrOperator(
    CompoundAttrOperator[AiWidthProfilePlugOperator]
):
    __slots__ = ()

    aiWidthProfile_Position = FloatField(default_value=0.0)
    wdthPp = aiWidthProfile_Position

    aiWidthProfile_FloatValue = FloatField(default_value=0.0)
    wdthPfv = aiWidthProfile_FloatValue

    aiWidthProfile_Interp = AiWidthProfile_aiWidthProfile_InterpEnumField(
        default_value=1
    )
    wdthPi = aiWidthProfile_Interp


class AiWidthProfileField(
    CompoundField[AiWidthProfileAttrOperator, AiWidthProfilePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiWidthProfileAttrOperator
    PLUG_CLS = AiWidthProfilePlugOperator
