# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.standard_surface import (
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
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.addr import AddrField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.dt.string import DataStringField


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


class StandardSurface(DG):
    __slots__ = ()

    NODE_TYPE = "standardSurface"

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    base = FloatField()
    b = base

    baseColor = BaseColorField()
    bc = baseColor
    baseColorR = baseColor.baseColorR
    bcr = baseColorR
    baseColorG = baseColor.baseColorG
    bcg = baseColorG
    baseColorB = baseColor.baseColorB
    bcb = baseColorB

    diffuseRoughness = FloatField()
    dr = diffuseRoughness

    specular = FloatField()
    s = specular

    specularColor = SpecularColorField()
    sc = specularColor
    specularColorR = specularColor.specularColorR
    scr = specularColorR
    specularColorG = specularColor.specularColorG
    scg = specularColorG
    specularColorB = specularColor.specularColorB
    spb = specularColorB

    specularRoughness = FloatField()
    sr = specularRoughness

    specularIOR = FloatField()
    sior = specularIOR

    specularAnisotropy = FloatField()
    sa = specularAnisotropy

    specularRotation = FloatField()
    srot = specularRotation

    metalness = FloatField()
    m = metalness

    transmission = FloatField()
    t = transmission

    transmissionColor = TransmissionColorField()
    trc = transmissionColor
    transmissionColorR = transmissionColor.transmissionColorR
    trcr = transmissionColorR
    transmissionColorG = transmissionColor.transmissionColorG
    trcg = transmissionColorG
    transmissionColorB = transmissionColor.transmissionColorB
    trcb = transmissionColorB

    transmissionDepth = FloatField()
    td = transmissionDepth

    transmissionScatter = TransmissionScatterField()
    ts = transmissionScatter
    transmissionScatterR = transmissionScatter.transmissionScatterR
    tsr = transmissionScatterR
    transmissionScatterG = transmissionScatter.transmissionScatterG
    tsg = transmissionScatterG
    transmissionScatterB = transmissionScatter.transmissionScatterB
    tsb = transmissionScatterB

    transmissionScatterAnisotropy = FloatField()
    tsa = transmissionScatterAnisotropy

    transmissionDispersion = FloatField()
    tdi = transmissionDispersion

    transmissionExtraRoughness = FloatField()
    ter = transmissionExtraRoughness

    subsurface = FloatField()
    sub = subsurface

    subsurfaceColor = SubsurfaceColorField()
    subc = subsurfaceColor
    subsurfaceColorR = subsurfaceColor.subsurfaceColorR
    subcr = subsurfaceColorR
    subsurfaceColorG = subsurfaceColor.subsurfaceColorG
    subcg = subsurfaceColorG
    subsurfaceColorB = subsurfaceColor.subsurfaceColorB
    subcb = subsurfaceColorB

    subsurfaceRadius = SubsurfaceRadiusField()
    subr = subsurfaceRadius
    subsurfaceRadiusR = subsurfaceRadius.subsurfaceRadiusR
    subrr = subsurfaceRadiusR
    subsurfaceRadiusG = subsurfaceRadius.subsurfaceRadiusG
    subrg = subsurfaceRadiusG
    subsurfaceRadiusB = subsurfaceRadius.subsurfaceRadiusB
    subrb = subsurfaceRadiusB

    subsurfaceScale = FloatField()
    subs = subsurfaceScale

    subsurfaceAnisotropy = FloatField()
    suba = subsurfaceAnisotropy

    sheen = FloatField()
    sh = sheen

    sheenColor = SheenColorField()
    shc = sheenColor
    sheenColorR = sheenColor.sheenColorR
    shcr = sheenColorR
    sheenColorG = sheenColor.sheenColorG
    shcg = sheenColorG
    sheenColorB = sheenColor.sheenColorB
    shcb = sheenColorB

    sheenRoughness = FloatField()
    shr = sheenRoughness

    thinWalled = BoolField()
    tw = thinWalled

    coat = FloatField()
    ct = coat

    coatColor = CoatColorField()
    ctc = coatColor
    coatColorR = coatColor.coatColorR
    ctcr = coatColorR
    coatColorG = coatColor.coatColorG
    ctcg = coatColorG
    coatColorB = coatColor.coatColorB
    ctcb = coatColorB

    coatRoughness = FloatField()
    ctr = coatRoughness

    coatIOR = FloatField()
    ctior = coatIOR

    coatAnisotropy = FloatField()
    cta = coatAnisotropy

    coatRotation = FloatField()
    ctro = coatRotation

    coatNormal = CoatNormalField()
    ctn = coatNormal
    coatNormalX = coatNormal.coatNormalX
    ctnx = coatNormalX
    coatNormalY = coatNormal.coatNormalY
    ctny = coatNormalY
    coatNormalZ = coatNormal.coatNormalZ
    ctnz = coatNormalZ

    coatAffectColor = FloatField()
    ctac = coatAffectColor

    coatAffectRoughness = FloatField()
    ctar = coatAffectRoughness

    thinFilmThickness = FloatField()
    tft = thinFilmThickness

    thinFilmIOR = FloatField()
    tfior = thinFilmIOR

    emission = FloatField()
    e = emission

    emissionColor = EmissionColorField()
    ec = emissionColor
    emissionColorR = emissionColor.emissionColorR
    ecr = emissionColorR
    emissionColorG = emissionColor.emissionColorG
    ecg = emissionColorG
    emissionColorB = emissionColor.emissionColorB
    ecb = emissionColorB

    opacity = OpacityField()
    op = opacity
    opacityR = opacity.opacityR
    opr = opacityR
    opacityG = opacity.opacityG
    opg = opacityG
    opacityB = opacity.opacityB
    opb = opacityB

    objectId = AddrField()
    oi = objectId

    primitiveId = LongField()
    pi = primitiveId

    raySampler = AddrField()
    rtr = raySampler

    rayDepth = ShortField()
    rd = rayDepth

    rayInstance = LongField()
    ryi = rayInstance

    rayDirection = RayDirectionField()
    rad = rayDirection
    rayDirectionX = rayDirection.rayDirectionX
    rdx = rayDirectionX
    rayDirectionY = rayDirection.rayDirectionY
    rdy = rayDirectionY
    rayDirectionZ = rayDirection.rayDirectionZ
    rdz = rayDirectionZ

    triangleNormalCamera = TriangleNormalCameraField()
    tnc = triangleNormalCamera
    triangleNormalCameraX = triangleNormalCamera.triangleNormalCameraX
    tnx = triangleNormalCameraX
    triangleNormalCameraY = triangleNormalCamera.triangleNormalCameraY
    tny = triangleNormalCameraY
    triangleNormalCameraZ = triangleNormalCamera.triangleNormalCameraZ
    tnz = triangleNormalCameraZ

    pointCamera = PointCameraField()
    pc = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    normalCamera = NormalCameraField()
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    tangentUCamera = TangentUCameraField()
    utan = tangentUCamera
    tangentUCameraX = tangentUCamera.tangentUCameraX
    utnx = tangentUCameraX
    tangentUCameraY = tangentUCamera.tangentUCameraY
    utny = tangentUCameraY
    tangentUCameraZ = tangentUCamera.tangentUCameraZ
    utnz = tangentUCameraZ

    lightDataArray = LightDataArrayField(multi=True)
    ltd = lightDataArray

    # TODO: lightDataArray.lightDirectionX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightDirectionY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightDirectionZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightIntensityR (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightIntensityG (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightIntensityB (attributeType=None, dataType=None) は未対応のため手動で追加してください

    hardwareShader = HardwareShaderField()
    hws = hardwareShader
    hardwareShaderR = hardwareShader.hardwareShaderR
    hwr = hardwareShaderR
    hardwareShaderG = hardwareShader.hardwareShaderG
    hwg = hardwareShaderG
    hardwareShaderB = hardwareShader.hardwareShaderB
    hwb = hardwareShaderB

    aiUserOptions = DataStringField()
    ai_user_options = aiUserOptions

    aiSubsurfaceType = AiSubsurfaceTypeEnumField()
    ai_subsurface_type = aiSubsurfaceType

    aiTransmitAovs = BoolField()
    ai_transmit_aovs = aiTransmitAovs

    aiDielectricPriority = LongField()
    ai_dielectric_priority = aiDielectricPriority

    aiEnableMatte = BoolField()
    ai_enable_matte = aiEnableMatte

    aiMatteColor = AiMatteColorField()
    ai_matte_color = aiMatteColor
    aiMatteColorR = aiMatteColor.aiMatteColorR
    ai_matte_colorr = aiMatteColorR
    aiMatteColorG = aiMatteColor.aiMatteColorG
    ai_matte_colorg = aiMatteColorG
    aiMatteColorB = aiMatteColor.aiMatteColorB
    ai_matte_colorb = aiMatteColorB

    aiMatteColorA = FloatField()
    ai_matte_color_a = aiMatteColorA

    aiAovId1 = DataStringField()
    ai_aov_id1 = aiAovId1

    aiId1 = AiId1Field()
    ai_id1 = aiId1
    aiId1R = aiId1.aiId1R
    ai_id1r = aiId1R
    aiId1G = aiId1.aiId1G
    ai_id1g = aiId1G
    aiId1B = aiId1.aiId1B
    ai_id1b = aiId1B

    aiAovId2 = DataStringField()
    ai_aov_id2 = aiAovId2

    aiId2 = AiId2Field()
    ai_id2 = aiId2
    aiId2R = aiId2.aiId2R
    ai_id2r = aiId2R
    aiId2G = aiId2.aiId2G
    ai_id2g = aiId2G
    aiId2B = aiId2.aiId2B
    ai_id2b = aiId2B

    aiAovId3 = DataStringField()
    ai_aov_id3 = aiAovId3

    aiId3 = AiId3Field()
    ai_id3 = aiId3
    aiId3R = aiId3.aiId3R
    ai_id3r = aiId3R
    aiId3G = aiId3.aiId3G
    ai_id3g = aiId3G
    aiId3B = aiId3.aiId3B
    ai_id3b = aiId3B

    aiAovId4 = DataStringField()
    ai_aov_id4 = aiAovId4

    aiId4 = AiId4Field()
    ai_id4 = aiId4
    aiId4R = aiId4.aiId4R
    ai_id4r = aiId4R
    aiId4G = aiId4.aiId4G
    ai_id4g = aiId4G
    aiId4B = aiId4.aiId4B
    ai_id4b = aiId4B

    aiAovId5 = DataStringField()
    ai_aov_id5 = aiAovId5

    aiId5 = AiId5Field()
    ai_id5 = aiId5
    aiId5R = aiId5.aiId5R
    ai_id5r = aiId5R
    aiId5G = aiId5.aiId5G
    ai_id5g = aiId5G
    aiId5B = aiId5.aiId5B
    ai_id5b = aiId5B

    aiAovId6 = DataStringField()
    ai_aov_id6 = aiAovId6

    aiId6 = AiId6Field()
    ai_id6 = aiId6
    aiId6R = aiId6.aiId6R
    ai_id6r = aiId6R
    aiId6G = aiId6.aiId6G
    ai_id6g = aiId6G
    aiId6B = aiId6.aiId6B
    ai_id6b = aiId6B

    aiAovId7 = DataStringField()
    ai_aov_id7 = aiAovId7

    aiId7 = AiId7Field()
    ai_id7 = aiId7
    aiId7R = aiId7.aiId7R
    ai_id7r = aiId7R
    aiId7G = aiId7.aiId7G
    ai_id7g = aiId7G
    aiId7B = aiId7.aiId7B
    ai_id7b = aiId7B

    aiAovId8 = DataStringField()
    ai_aov_id8 = aiAovId8

    aiId8 = AiId8Field()
    ai_id8 = aiId8
    aiId8R = aiId8.aiId8R
    ai_id8r = aiId8R
    aiId8G = aiId8.aiId8G
    ai_id8g = aiId8G
    aiId8B = aiId8.aiId8B
    ai_id8b = aiId8B

    aiCaustics = BoolField()
    ai_caustics = aiCaustics

    aiExitToBackground = BoolField()
    ai_exit_to_background = aiExitToBackground

    aiInternalReflections = BoolField()
    ai_internal_reflections = aiInternalReflections

    aiIndirectDiffuse = FloatField()
    ai_indirect_diffuse = aiIndirectDiffuse

    aiIndirectSpecular = FloatField()
    ai_indirect_specular = aiIndirectSpecular
