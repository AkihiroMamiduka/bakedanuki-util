# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.standard_surface import (
    AiId1Field,
    AiId2Field,
    AiId3Field,
    AiId4Field,
    AiId5Field,
    AiId6Field,
    AiId7Field,
    AiId8Field,
    AiMatteColorField,
    BaseColorField,
    CoatColorField,
    CoatNormalField,
    EmissionColorField,
    HardwareShaderField,
    LightDataArrayField,
    NormalCameraField,
    OpacityField,
    OutColorField,
    OutTransparencyField,
    PointCameraField,
    RayDirectionField,
    SheenColorField,
    SpecularColorField,
    SubsurfaceColorField,
    SubsurfaceRadiusField,
    TangentUCameraField,
    TransmissionColorField,
    TransmissionScatterField,
    TriangleNormalCameraField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.addr import AddrField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.dt.string import DataStringField


class AiSubsurfaceTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DIFFUSION = 0
    RANDOMWALK = 1
    RANDOMWALK_V2 = 2


class AiSubsurfaceTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DIFFUSION = 0
    RANDOMWALK = 1
    RANDOMWALK_V2 = 2

    NAME_MAP = {
        DIFFUSION: "diffusion",
        RANDOMWALK: "randomwalk",
        RANDOMWALK_V2: "randomwalk_v2",
    }


class AiSubsurfaceTypeEnumField(
    EnumField[AiSubsurfaceTypeEnumAttrOperator, AiSubsurfaceTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiSubsurfaceTypeEnumAttrOperator
    PLUG_CLS = AiSubsurfaceTypeEnumPlugOperator


class _GeneratedStandardSurface(DG):
    __slots__ = ()

    NODE_TYPE = "standardSurface"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    base = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    b = base

    baseColor = BaseColorField(default_value=(0.800000011920929, 0.800000011920929, 0.800000011920929))
    bc = baseColor
    baseColorR = baseColor.baseColorR
    bcr = baseColorR
    baseColorG = baseColor.baseColorG
    bcg = baseColorG
    baseColorB = baseColor.baseColorB
    bcb = baseColorB

    diffuseRoughness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    dr = diffuseRoughness

    specular = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    s = specular

    specularColor = SpecularColorField(default_value=(1.0, 1.0, 1.0))
    sc = specularColor
    specularColorR = specularColor.specularColorR
    scr = specularColorR
    specularColorG = specularColor.specularColorG
    scg = specularColorG
    specularColorB = specularColor.specularColorB
    spb = specularColorB

    specularRoughness = FloatField(default_value=0.20000000298023224, min_value=0.0, max_value=1.0)
    sr = specularRoughness

    specularIOR = FloatField(default_value=1.5, min_value=0.0, soft_max_value=3.0)
    sior = specularIOR

    specularAnisotropy = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    sa = specularAnisotropy

    specularRotation = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    srot = specularRotation

    metalness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    m = metalness

    transmission = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    t = transmission

    transmissionColor = TransmissionColorField(default_value=(1.0, 1.0, 1.0))
    trc = transmissionColor
    transmissionColorR = transmissionColor.transmissionColorR
    trcr = transmissionColorR
    transmissionColorG = transmissionColor.transmissionColorG
    trcg = transmissionColorG
    transmissionColorB = transmissionColor.transmissionColorB
    trcb = transmissionColorB

    transmissionDepth = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)
    td = transmissionDepth

    transmissionScatter = TransmissionScatterField(default_value=(0.0, 0.0, 0.0))
    ts = transmissionScatter
    transmissionScatterR = transmissionScatter.transmissionScatterR
    tsr = transmissionScatterR
    transmissionScatterG = transmissionScatter.transmissionScatterG
    tsg = transmissionScatterG
    transmissionScatterB = transmissionScatter.transmissionScatterB
    tsb = transmissionScatterB

    transmissionScatterAnisotropy = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    tsa = transmissionScatterAnisotropy

    transmissionDispersion = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)
    tdi = transmissionDispersion

    transmissionExtraRoughness = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ter = transmissionExtraRoughness

    subsurface = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    sub = subsurface

    subsurfaceColor = SubsurfaceColorField(default_value=(1.0, 1.0, 1.0))
    subc = subsurfaceColor
    subsurfaceColorR = subsurfaceColor.subsurfaceColorR
    subcr = subsurfaceColorR
    subsurfaceColorG = subsurfaceColor.subsurfaceColorG
    subcg = subsurfaceColorG
    subsurfaceColorB = subsurfaceColor.subsurfaceColorB
    subcb = subsurfaceColorB

    subsurfaceRadius = SubsurfaceRadiusField(default_value=(1.0, 1.0, 1.0))
    subr = subsurfaceRadius
    subsurfaceRadiusR = subsurfaceRadius.subsurfaceRadiusR
    subrr = subsurfaceRadiusR
    subsurfaceRadiusG = subsurfaceRadius.subsurfaceRadiusG
    subrg = subsurfaceRadiusG
    subsurfaceRadiusB = subsurfaceRadius.subsurfaceRadiusB
    subrb = subsurfaceRadiusB

    subsurfaceScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    subs = subsurfaceScale

    subsurfaceAnisotropy = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    suba = subsurfaceAnisotropy

    sheen = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    sh = sheen

    sheenColor = SheenColorField(default_value=(1.0, 1.0, 1.0))
    shc = sheenColor
    sheenColorR = sheenColor.sheenColorR
    shcr = sheenColorR
    sheenColorG = sheenColor.sheenColorG
    shcg = sheenColorG
    sheenColorB = sheenColor.sheenColorB
    shcb = sheenColorB

    sheenRoughness = FloatField(default_value=0.30000001192092896, min_value=0.0, max_value=1.0)
    shr = sheenRoughness

    thinWalled = BoolField(default_value=False)
    tw = thinWalled

    coat = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ct = coat

    coatColor = CoatColorField(default_value=(1.0, 1.0, 1.0))
    ctc = coatColor
    coatColorR = coatColor.coatColorR
    ctcr = coatColorR
    coatColorG = coatColor.coatColorG
    ctcg = coatColorG
    coatColorB = coatColor.coatColorB
    ctcb = coatColorB

    coatRoughness = FloatField(default_value=0.10000000149011612, min_value=0.0, max_value=1.0)
    ctr = coatRoughness

    coatIOR = FloatField(default_value=1.5, min_value=0.0, soft_max_value=5.0)
    ctior = coatIOR

    coatAnisotropy = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cta = coatAnisotropy

    coatRotation = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ctro = coatRotation

    coatNormal = CoatNormalField(default_value=(0.0, 0.0, 0.0))
    ctn = coatNormal
    coatNormalX = coatNormal.coatNormalX
    ctnx = coatNormalX
    coatNormalY = coatNormal.coatNormalY
    ctny = coatNormalY
    coatNormalZ = coatNormal.coatNormalZ
    ctnz = coatNormalZ

    coatAffectColor = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ctac = coatAffectColor

    coatAffectRoughness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ctar = coatAffectRoughness

    thinFilmThickness = FloatField(default_value=0.0, min_value=0.0, soft_max_value=2000.0)
    tft = thinFilmThickness

    thinFilmIOR = FloatField(default_value=1.5, min_value=0.0, soft_max_value=3.0)
    tfior = thinFilmIOR

    emission = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    e = emission

    emissionColor = EmissionColorField(default_value=(1.0, 1.0, 1.0))
    ec = emissionColor
    emissionColorR = emissionColor.emissionColorR
    ecr = emissionColorR
    emissionColorG = emissionColor.emissionColorG
    ecg = emissionColorG
    emissionColorB = emissionColor.emissionColorB
    ecb = emissionColorB

    opacity = OpacityField(default_value=(1.0, 1.0, 1.0))
    op = opacity
    opacityR = opacity.opacityR
    opr = opacityR
    opacityG = opacity.opacityG
    opg = opacityG
    opacityB = opacity.opacityB
    opb = opacityB

    objectId = AddrField(default_value=0.0, readable=False)
    oi = objectId

    primitiveId = LongField(default_value=0, readable=False)
    pi = primitiveId

    raySampler = AddrField(default_value=0.0, readable=False)
    rtr = raySampler

    rayDepth = ShortField(default_value=0, readable=False)
    rd = rayDepth

    rayInstance = LongField(default_value=0, readable=False)
    ryi = rayInstance

    rayDirection = RayDirectionField(default_value=(0.0, 0.0, 1.0), readable=False)
    rad = rayDirection
    rayDirectionX = rayDirection.rayDirectionX
    rdx = rayDirectionX
    rayDirectionY = rayDirection.rayDirectionY
    rdy = rayDirectionY
    rayDirectionZ = rayDirection.rayDirectionZ
    rdz = rayDirectionZ

    triangleNormalCamera = TriangleNormalCameraField(default_value=(0.0, 1.0, 0.0))
    tnc = triangleNormalCamera
    triangleNormalCameraX = triangleNormalCamera.triangleNormalCameraX
    tnx = triangleNormalCameraX
    triangleNormalCameraY = triangleNormalCamera.triangleNormalCameraY
    tny = triangleNormalCameraY
    triangleNormalCameraZ = triangleNormalCamera.triangleNormalCameraZ
    tnz = triangleNormalCameraZ

    pointCamera = PointCameraField(default_value=(1.0, 1.0, 1.0))
    pc = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    normalCamera = NormalCameraField(default_value=(1.0, 1.0, 1.0))
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    tangentUCamera = TangentUCameraField(default_value=(1.0, 1.0, 1.0))
    utan = tangentUCamera
    tangentUCameraX = tangentUCamera.tangentUCameraX
    utnx = tangentUCameraX
    tangentUCameraY = tangentUCamera.tangentUCameraY
    utny = tangentUCameraY
    tangentUCameraZ = tangentUCamera.tangentUCameraZ
    utnz = tangentUCameraZ

    lightDataArray = LightDataArrayField(multi=True, readable=False)
    ltd = lightDataArray

    lightDirectionX = FloatField()
    ldx = lightDirectionX

    lightDirectionY = FloatField()
    ldy = lightDirectionY

    lightDirectionZ = FloatField()
    ldz = lightDirectionZ

    lightIntensityR = FloatField()
    lir = lightIntensityR

    lightIntensityG = FloatField()
    lig = lightIntensityG

    lightIntensityB = FloatField()
    lib = lightIntensityB

    hardwareShader = HardwareShaderField(default_value=(0.0, 0.0, 0.0))
    hws = hardwareShader
    hardwareShaderR = hardwareShader.hardwareShaderR
    hwr = hardwareShaderR
    hardwareShaderG = hardwareShader.hardwareShaderG
    hwg = hardwareShaderG
    hardwareShaderB = hardwareShader.hardwareShaderB
    hwb = hardwareShaderB

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiSubsurfaceType = AiSubsurfaceTypeEnumField(default_value=1, category="arnold")
    ai_subsurface_type = aiSubsurfaceType

    aiTransmitAovs = BoolField(default_value=True, category="arnold")
    ai_transmit_aovs = aiTransmitAovs

    aiDielectricPriority = LongField(default_value=0, category="arnold")
    ai_dielectric_priority = aiDielectricPriority

    aiEnableMatte = BoolField(default_value=False, category="arnold")
    ai_enable_matte = aiEnableMatte

    aiMatteColor = AiMatteColorField(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_matte_color = aiMatteColor
    aiMatteColorR = aiMatteColor.aiMatteColorR
    ai_matte_colorr = aiMatteColorR
    aiMatteColorG = aiMatteColor.aiMatteColorG
    ai_matte_colorg = aiMatteColorG
    aiMatteColorB = aiMatteColor.aiMatteColorB
    ai_matte_colorb = aiMatteColorB

    aiMatteColorA = FloatField(default_value=0.0, min_value=0.0, max_value=1.0, category="arnold")
    ai_matte_color_a = aiMatteColorA

    aiAovId1 = DataStringField(category="arnold")
    ai_aov_id1 = aiAovId1

    aiId1 = AiId1Field(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_id1 = aiId1
    aiId1R = aiId1.aiId1R
    ai_id1r = aiId1R
    aiId1G = aiId1.aiId1G
    ai_id1g = aiId1G
    aiId1B = aiId1.aiId1B
    ai_id1b = aiId1B

    aiAovId2 = DataStringField(category="arnold")
    ai_aov_id2 = aiAovId2

    aiId2 = AiId2Field(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_id2 = aiId2
    aiId2R = aiId2.aiId2R
    ai_id2r = aiId2R
    aiId2G = aiId2.aiId2G
    ai_id2g = aiId2G
    aiId2B = aiId2.aiId2B
    ai_id2b = aiId2B

    aiAovId3 = DataStringField(category="arnold")
    ai_aov_id3 = aiAovId3

    aiId3 = AiId3Field(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_id3 = aiId3
    aiId3R = aiId3.aiId3R
    ai_id3r = aiId3R
    aiId3G = aiId3.aiId3G
    ai_id3g = aiId3G
    aiId3B = aiId3.aiId3B
    ai_id3b = aiId3B

    aiAovId4 = DataStringField(category="arnold")
    ai_aov_id4 = aiAovId4

    aiId4 = AiId4Field(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_id4 = aiId4
    aiId4R = aiId4.aiId4R
    ai_id4r = aiId4R
    aiId4G = aiId4.aiId4G
    ai_id4g = aiId4G
    aiId4B = aiId4.aiId4B
    ai_id4b = aiId4B

    aiAovId5 = DataStringField(category="arnold")
    ai_aov_id5 = aiAovId5

    aiId5 = AiId5Field(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_id5 = aiId5
    aiId5R = aiId5.aiId5R
    ai_id5r = aiId5R
    aiId5G = aiId5.aiId5G
    ai_id5g = aiId5G
    aiId5B = aiId5.aiId5B
    ai_id5b = aiId5B

    aiAovId6 = DataStringField(category="arnold")
    ai_aov_id6 = aiAovId6

    aiId6 = AiId6Field(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_id6 = aiId6
    aiId6R = aiId6.aiId6R
    ai_id6r = aiId6R
    aiId6G = aiId6.aiId6G
    ai_id6g = aiId6G
    aiId6B = aiId6.aiId6B
    ai_id6b = aiId6B

    aiAovId7 = DataStringField(category="arnold")
    ai_aov_id7 = aiAovId7

    aiId7 = AiId7Field(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_id7 = aiId7
    aiId7R = aiId7.aiId7R
    ai_id7r = aiId7R
    aiId7G = aiId7.aiId7G
    ai_id7g = aiId7G
    aiId7B = aiId7.aiId7B
    ai_id7b = aiId7B

    aiAovId8 = DataStringField(category="arnold")
    ai_aov_id8 = aiAovId8

    aiId8 = AiId8Field(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_id8 = aiId8
    aiId8R = aiId8.aiId8R
    ai_id8r = aiId8R
    aiId8G = aiId8.aiId8G
    ai_id8g = aiId8G
    aiId8B = aiId8.aiId8B
    ai_id8b = aiId8B

    aiCaustics = BoolField(default_value=False, category="arnold")
    ai_caustics = aiCaustics

    aiExitToBackground = BoolField(default_value=False, category="arnold")
    ai_exit_to_background = aiExitToBackground

    aiInternalReflections = BoolField(default_value=True, category="arnold")
    ai_internal_reflections = aiInternalReflections

    aiIndirectDiffuse = FloatField(default_value=1.0, min_value=0.0, max_value=1.0, category="arnold")
    ai_indirect_diffuse = aiIndirectDiffuse

    aiIndirectSpecular = FloatField(default_value=1.0, min_value=0.0, max_value=1.0, category="arnold")
    ai_indirect_specular = aiIndirectSpecular
