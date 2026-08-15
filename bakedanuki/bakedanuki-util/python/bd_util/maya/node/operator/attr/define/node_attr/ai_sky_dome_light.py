# coding: utf-8

from ..std.at.addr import AddrField
from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.light_data import (
    LightDataAttrOperator,
    LightDataPlugOperator,
    LightDataField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
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


class LightData_lightDirectionPlugOperator(
    Float3CompoundBasePlugOperator["LightData_lightDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightDirectionX", "ldx"),
        ("lightDirectionY", "ldy"),
        ("lightDirectionZ", "ldz"),
    )

    lightDirectionX = FloatField(default_value=-1.0, writable=False)
    ldx = lightDirectionX

    lightDirectionY = FloatField(default_value=0.0, writable=False)
    ldy = lightDirectionY

    lightDirectionZ = FloatField(default_value=0.0, writable=False)
    ldz = lightDirectionZ


class LightData_lightDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[LightData_lightDirectionPlugOperator]
):
    __slots__ = ()

    lightDirectionX = FloatField(default_value=-1.0, writable=False)
    ldx = lightDirectionX

    lightDirectionY = FloatField(default_value=0.0, writable=False)
    ldy = lightDirectionY

    lightDirectionZ = FloatField(default_value=0.0, writable=False)
    ldz = lightDirectionZ


class LightData_lightDirectionField(
    Float3CompoundBaseField[
        LightData_lightDirectionAttrOperator,
        LightData_lightDirectionPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = LightData_lightDirectionAttrOperator
    PLUG_CLS = LightData_lightDirectionPlugOperator

    lightDirectionX = FloatField(default_value=-1.0, writable=False)
    ldx = lightDirectionX

    lightDirectionY = FloatField(default_value=0.0, writable=False)
    ldy = lightDirectionY

    lightDirectionZ = FloatField(default_value=0.0, writable=False)
    ldz = lightDirectionZ


class LightData_lightIntensityPlugOperator(
    Float3CompoundBasePlugOperator["LightData_lightIntensityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightIntensityR", "lir"),
        ("lightIntensityG", "lig"),
        ("lightIntensityB", "lib"),
    )

    lightIntensityR = FloatField(default_value=1.0, writable=False)
    lir = lightIntensityR

    lightIntensityG = FloatField(default_value=0.5, writable=False)
    lig = lightIntensityG

    lightIntensityB = FloatField(
        default_value=0.20000000298023224, writable=False
    )
    lib = lightIntensityB


class LightData_lightIntensityAttrOperator(
    Float3CompoundBaseAttrOperator[LightData_lightIntensityPlugOperator]
):
    __slots__ = ()

    lightIntensityR = FloatField(default_value=1.0, writable=False)
    lir = lightIntensityR

    lightIntensityG = FloatField(default_value=0.5, writable=False)
    lig = lightIntensityG

    lightIntensityB = FloatField(
        default_value=0.20000000298023224, writable=False
    )
    lib = lightIntensityB


class LightData_lightIntensityField(
    Float3CompoundBaseField[
        LightData_lightIntensityAttrOperator,
        LightData_lightIntensityPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = LightData_lightIntensityAttrOperator
    PLUG_CLS = LightData_lightIntensityPlugOperator

    lightIntensityR = FloatField(default_value=1.0, writable=False)
    lir = lightIntensityR

    lightIntensityG = FloatField(default_value=0.5, writable=False)
    lig = lightIntensityG

    lightIntensityB = FloatField(
        default_value=0.20000000298023224, writable=False
    )
    lib = lightIntensityB


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


class ColorPlugOperator(Float3CompoundBasePlugOperator["ColorAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "scr"),
        ("colorG", "scg"),
        ("colorB", "scb"),
    )

    colorR = FloatField(default_value=1.0)
    scr = colorR

    colorG = FloatField(default_value=1.0)
    scg = colorG

    colorB = FloatField(default_value=1.0)
    scb = colorB


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=1.0)
    scr = colorR

    colorG = FloatField(default_value=1.0)
    scg = colorG

    colorB = FloatField(default_value=1.0)
    scb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=1.0)
    scr = colorR

    colorG = FloatField(default_value=1.0)
    scg = colorG

    colorB = FloatField(default_value=1.0)
    scb = colorB


class PointCameraPlugOperator(
    Float3CompoundBasePlugOperator["PointCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointCameraX", "px"),
        ("pointCameraY", "py"),
        ("pointCameraZ", "pz"),
    )

    pointCameraX = FloatField(default_value=0.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=0.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=0.0)
    pz = pointCameraZ


class PointCameraAttrOperator(
    Float3CompoundBaseAttrOperator[PointCameraPlugOperator]
):
    __slots__ = ()

    pointCameraX = FloatField(default_value=0.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=0.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=0.0)
    pz = pointCameraZ


class PointCameraField(
    Float3CompoundBaseField[PointCameraAttrOperator, PointCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointCameraAttrOperator
    PLUG_CLS = PointCameraPlugOperator

    pointCameraX = FloatField(default_value=0.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=0.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=0.0)
    pz = pointCameraZ


class NormalCameraPlugOperator(
    Float3CompoundBasePlugOperator["NormalCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalCameraX", "nx"),
        ("normalCameraY", "ny"),
        ("normalCameraZ", "nz"),
    )

    normalCameraX = FloatField(default_value=0.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=0.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=0.0)
    nz = normalCameraZ


class NormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[NormalCameraPlugOperator]
):
    __slots__ = ()

    normalCameraX = FloatField(default_value=0.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=0.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=0.0)
    nz = normalCameraZ


class NormalCameraField(
    Float3CompoundBaseField[NormalCameraAttrOperator, NormalCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalCameraAttrOperator
    PLUG_CLS = NormalCameraPlugOperator

    normalCameraX = FloatField(default_value=0.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=0.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=0.0)
    nz = normalCameraZ


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "oclr"),
        ("outColorG", "oclg"),
        ("outColorB", "oclb"),
    )

    outColorR = FloatField(default_value=0.0, writable=False)
    oclr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    oclg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    oclb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    oclr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    oclg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    oclb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    oclr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    oclg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    oclb = outColorB


class OutTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["OutTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTransparencyR", "otr"),
        ("outTransparencyG", "otg"),
        ("outTransparencyB", "otb"),
    )

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[
        OutTransparencyAttrOperator, OutTransparencyPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class LightDataValuePlugOperator(
    LightDataPlugOperator["LightDataValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightDirection", "ld"),
        ("lightIntensity", "li"),
        ("lightAmbient", "la"),
        ("lightDiffuse", "ldf"),
        ("lightSpecular", "ls"),
        ("lightShadowFraction", "lsf"),
        ("preShadowIntensity", "psi"),
        ("lightBlindData", "lbld"),
    )

    lightDirection = LightData_lightDirectionField(
        default_value=(-1.0, 0.0, 0.0), writable=False
    )
    ld = lightDirection

    lightIntensity = LightData_lightIntensityField(
        default_value=(1.0, 0.5, 0.20000000298023224), writable=False
    )
    li = lightIntensity

    lightAmbient = BoolField(default_value=True, writable=False)
    la = lightAmbient

    lightDiffuse = BoolField(default_value=True, writable=False)
    ldf = lightDiffuse

    lightSpecular = BoolField(default_value=True, writable=False)
    ls = lightSpecular

    lightShadowFraction = FloatField(default_value=0.0, writable=False)
    lsf = lightShadowFraction

    preShadowIntensity = FloatField(default_value=1.0, writable=False)
    psi = preShadowIntensity

    lightBlindData = AddrField(default_value=0.0, writable=False)
    lbld = lightBlindData


class LightDataValueAttrOperator(
    LightDataAttrOperator[LightDataValuePlugOperator]
):
    __slots__ = ()

    lightDirection = LightData_lightDirectionField(
        default_value=(-1.0, 0.0, 0.0), writable=False
    )
    ld = lightDirection

    lightIntensity = LightData_lightIntensityField(
        default_value=(1.0, 0.5, 0.20000000298023224), writable=False
    )
    li = lightIntensity

    lightAmbient = BoolField(default_value=True, writable=False)
    la = lightAmbient

    lightDiffuse = BoolField(default_value=True, writable=False)
    ldf = lightDiffuse

    lightSpecular = BoolField(default_value=True, writable=False)
    ls = lightSpecular

    lightShadowFraction = FloatField(default_value=0.0, writable=False)
    lsf = lightShadowFraction

    preShadowIntensity = FloatField(default_value=1.0, writable=False)
    psi = preShadowIntensity

    lightBlindData = AddrField(default_value=0.0, writable=False)
    lbld = lightBlindData


class LightDataValueField(
    LightDataField[LightDataValueAttrOperator, LightDataValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightDataValueAttrOperator
    PLUG_CLS = LightDataValuePlugOperator

    lightDirection = LightData_lightDirectionField(
        default_value=(-1.0, 0.0, 0.0), writable=False
    )
    ld = lightDirection

    lightIntensity = LightData_lightIntensityField(
        default_value=(1.0, 0.5, 0.20000000298023224), writable=False
    )
    li = lightIntensity

    lightAmbient = BoolField(default_value=True, writable=False)
    la = lightAmbient

    lightDiffuse = BoolField(default_value=True, writable=False)
    ldf = lightDiffuse

    lightSpecular = BoolField(default_value=True, writable=False)
    ls = lightSpecular

    lightShadowFraction = FloatField(default_value=0.0, writable=False)
    lsf = lightShadowFraction

    preShadowIntensity = FloatField(default_value=1.0, writable=False)
    psi = preShadowIntensity

    lightBlindData = AddrField(default_value=0.0, writable=False)
    lbld = lightBlindData


class AiShadowColorPlugOperator(
    Float3CompoundBasePlugOperator["AiShadowColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiShadowColorR", "ai_shadow_colorr"),
        ("aiShadowColorG", "ai_shadow_colorg"),
        ("aiShadowColorB", "ai_shadow_colorb"),
    )

    aiShadowColorR = FloatField(default_value=0.0)
    ai_shadow_colorr = aiShadowColorR

    aiShadowColorG = FloatField(default_value=0.0)
    ai_shadow_colorg = aiShadowColorG

    aiShadowColorB = FloatField(default_value=0.0)
    ai_shadow_colorb = aiShadowColorB


class AiShadowColorAttrOperator(
    Float3CompoundBaseAttrOperator[AiShadowColorPlugOperator]
):
    __slots__ = ()

    aiShadowColorR = FloatField(default_value=0.0)
    ai_shadow_colorr = aiShadowColorR

    aiShadowColorG = FloatField(default_value=0.0)
    ai_shadow_colorg = aiShadowColorG

    aiShadowColorB = FloatField(default_value=0.0)
    ai_shadow_colorb = aiShadowColorB


class AiShadowColorField(
    Float3CompoundBaseField[
        AiShadowColorAttrOperator, AiShadowColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiShadowColorAttrOperator
    PLUG_CLS = AiShadowColorPlugOperator

    aiShadowColorR = FloatField(default_value=0.0)
    ai_shadow_colorr = aiShadowColorR

    aiShadowColorG = FloatField(default_value=0.0)
    ai_shadow_colorg = aiShadowColorG

    aiShadowColorB = FloatField(default_value=0.0)
    ai_shadow_colorb = aiShadowColorB
