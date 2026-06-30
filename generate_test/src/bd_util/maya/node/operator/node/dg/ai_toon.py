# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_toon import (
    BaseColorField,
    BaseTonemapField,
    EdgeColorField,
    EdgeTonemapField,
    EmissionColorField,
    HardwareColorField,
    HighlightColorField,
    MaskColorField,
    NormalCameraField,
    NormalField,
    OutColorField,
    OutTransparencyField,
    RimLightColorField,
    SheenColorField,
    SilhouetteColorField,
    SilhouetteTonemapField,
    SpecularColorField,
    SpecularTonemapField,
    TangentField,
    TransmissionColorField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class NormalTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SHADING_NORMAL = 0
    SMOOTHED_NORMAL = 1
    GEOMETRIC_NORMAL = 2


class NormalTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SHADING_NORMAL = 0
    SMOOTHED_NORMAL = 1
    GEOMETRIC_NORMAL = 2

    NAME_MAP = {
        SHADING_NORMAL: "shading normal",
        SMOOTHED_NORMAL: "smoothed normal",
        GEOMETRIC_NORMAL: "geometric normal",
    }


class NormalTypeEnumField(
    EnumField[NormalTypeEnumAttrOperator, NormalTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalTypeEnumAttrOperator
    PLUG_CLS = NormalTypeEnumPlugOperator


class BumpModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BOTH = 0
    DIFFUSE = 1
    SPECULAR = 2


class BumpModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BOTH = 0
    DIFFUSE = 1
    SPECULAR = 2

    NAME_MAP = {
        BOTH: "both",
        DIFFUSE: "diffuse",
        SPECULAR: "specular",
    }


class BumpModeEnumField(
    EnumField[BumpModeEnumAttrOperator, BumpModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BumpModeEnumAttrOperator
    PLUG_CLS = BumpModeEnumPlugOperator


class AiToon(DG):
    __slots__ = ()

    NODE_TYPE = "aiToon"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    normalCamera = NormalCameraField()
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    hardwareColor = HardwareColorField()
    hwc = hardwareColor
    hardwareColorR = hardwareColor.hardwareColorR
    hwcr = hardwareColorR
    hardwareColorG = hardwareColor.hardwareColorG
    hwcg = hardwareColorG
    hardwareColorB = hardwareColor.hardwareColorB
    hwcb = hardwareColorB

    maskColor = MaskColorField()
    mask_color = maskColor
    maskColorR = maskColor.maskColorR
    mask_colorr = maskColorR
    maskColorG = maskColor.maskColorG
    mask_colorg = maskColorG
    maskColorB = maskColor.maskColorB
    mask_colorb = maskColorB

    edgeColor = EdgeColorField()
    edge_color = edgeColor
    edgeColorR = edgeColor.edgeColorR
    edge_colorr = edgeColorR
    edgeColorG = edgeColor.edgeColorG
    edge_colorg = edgeColorG
    edgeColorB = edgeColor.edgeColorB
    edge_colorb = edgeColorB

    edgeTonemap = EdgeTonemapField()
    edge_tonemap = edgeTonemap
    edgeTonemapR = edgeTonemap.edgeTonemapR
    edge_tonemapr = edgeTonemapR
    edgeTonemapG = edgeTonemap.edgeTonemapG
    edge_tonemapg = edgeTonemapG
    edgeTonemapB = edgeTonemap.edgeTonemapB
    edge_tonemapb = edgeTonemapB

    edgeOpacity = FloatField()
    edge_opacity = edgeOpacity

    edgeWidthScale = FloatField()
    edge_width_scale = edgeWidthScale

    silhouetteColor = SilhouetteColorField()
    silhouette_color = silhouetteColor
    silhouetteColorR = silhouetteColor.silhouetteColorR
    silhouette_colorr = silhouetteColorR
    silhouetteColorG = silhouetteColor.silhouetteColorG
    silhouette_colorg = silhouetteColorG
    silhouetteColorB = silhouetteColor.silhouetteColorB
    silhouette_colorb = silhouetteColorB

    silhouetteTonemap = SilhouetteTonemapField()
    silhouette_tonemap = silhouetteTonemap
    silhouetteTonemapR = silhouetteTonemap.silhouetteTonemapR
    silhouette_tonemapr = silhouetteTonemapR
    silhouetteTonemapG = silhouetteTonemap.silhouetteTonemapG
    silhouette_tonemapg = silhouetteTonemapG
    silhouetteTonemapB = silhouetteTonemap.silhouetteTonemapB
    silhouette_tonemapb = silhouetteTonemapB

    silhouetteOpacity = FloatField()
    silhouette_opacity = silhouetteOpacity

    silhouetteWidthScale = FloatField()
    silhouette_width_scale = silhouetteWidthScale

    priority = LongField()

    enableSilhouette = BoolField()
    enable_silhouette = enableSilhouette

    ignoreThroughput = BoolField()
    ignore_throughput = ignoreThroughput

    enable = BoolField()

    idDifference = BoolField()
    id_difference = idDifference

    shaderDifference = BoolField()
    shader_difference = shaderDifference

    uvThreshold = FloatField()
    uv_threshold = uvThreshold

    angleThreshold = FloatField()
    angle_threshold = angleThreshold

    normalType = NormalTypeEnumField()
    normal_type = normalType

    base = FloatField()

    baseColor = BaseColorField()
    base_color = baseColor
    baseColorR = baseColor.baseColorR
    base_colorr = baseColorR
    baseColorG = baseColor.baseColorG
    base_colorg = baseColorG
    baseColorB = baseColor.baseColorB
    base_colorb = baseColorB

    baseTonemap = BaseTonemapField()
    base_tonemap = baseTonemap
    baseTonemapR = baseTonemap.baseTonemapR
    base_tonemapr = baseTonemapR
    baseTonemapG = baseTonemap.baseTonemapG
    base_tonemapg = baseTonemapG
    baseTonemapB = baseTonemap.baseTonemapB
    base_tonemapb = baseTonemapB

    specular = FloatField()

    specularColor = SpecularColorField()
    specular_color = specularColor
    specularColorR = specularColor.specularColorR
    specular_colorr = specularColorR
    specularColorG = specularColor.specularColorG
    specular_colorg = specularColorG
    specularColorB = specularColor.specularColorB
    specular_colorb = specularColorB

    specularRoughness = FloatField()
    specular_roughness = specularRoughness

    specularAnisotropy = FloatField()
    specular_anisotropy = specularAnisotropy

    specularRotation = FloatField()
    specular_rotation = specularRotation

    specularTonemap = SpecularTonemapField()
    specular_tonemap = specularTonemap
    specularTonemapR = specularTonemap.specularTonemapR
    specular_tonemapr = specularTonemapR
    specularTonemapG = specularTonemap.specularTonemapG
    specular_tonemapg = specularTonemapG
    specularTonemapB = specularTonemap.specularTonemapB
    specular_tonemapb = specularTonemapB

    lights = DataStringField()

    highlightColor = HighlightColorField()
    highlight_color = highlightColor
    highlightColorR = highlightColor.highlightColorR
    highlight_colorr = highlightColorR
    highlightColorG = highlightColor.highlightColorG
    highlight_colorg = highlightColorG
    highlightColorB = highlightColor.highlightColorB
    highlight_colorb = highlightColorB

    highlightSize = FloatField()
    highlight_size = highlightSize

    aovHighlight = DataStringField()
    aov_highlight = aovHighlight

    rimLight = DataStringField()
    rim_light = rimLight

    rimLightColor = RimLightColorField()
    rim_light_color = rimLightColor
    rimLightColorR = rimLightColor.rimLightColorR
    rim_light_colorr = rimLightColorR
    rimLightColorG = rimLightColor.rimLightColorG
    rim_light_colorg = rimLightColorG
    rimLightColorB = rimLightColor.rimLightColorB
    rim_light_colorb = rimLightColorB

    rimLightWidth = FloatField()
    rim_light_width = rimLightWidth

    rimLightTint = FloatField()
    rim_light_tint = rimLightTint

    aovRimLight = DataStringField()
    aov_rim_light = aovRimLight

    transmission = FloatField()

    transmissionColor = TransmissionColorField()
    transmission_color = transmissionColor
    transmissionColorR = transmissionColor.transmissionColorR
    transmission_colorr = transmissionColorR
    transmissionColorG = transmissionColor.transmissionColorG
    transmission_colorg = transmissionColorG
    transmissionColorB = transmissionColor.transmissionColorB
    transmission_colorb = transmissionColorB

    transmissionRoughness = FloatField()
    transmission_roughness = transmissionRoughness

    transmissionAnisotropy = FloatField()
    transmission_anisotropy = transmissionAnisotropy

    transmissionRotation = FloatField()
    transmission_rotation = transmissionRotation

    sheen = FloatField()

    sheenColor = SheenColorField()
    sheen_color = sheenColor
    sheenColorR = sheenColor.sheenColorR
    sheen_colorr = sheenColorR
    sheenColorG = sheenColor.sheenColorG
    sheen_colorg = sheenColorG
    sheenColorB = sheenColor.sheenColorB
    sheen_colorb = sheenColorB

    sheenRoughness = FloatField()
    sheen_roughness = sheenRoughness

    emission = FloatField()

    emissionColor = EmissionColorField()
    emission_color = emissionColor
    emissionColorR = emissionColor.emissionColorR
    emission_colorr = emissionColorR
    emissionColorG = emissionColor.emissionColorG
    emission_colorg = emissionColorG
    emissionColorB = emissionColor.emissionColorB
    emission_colorb = emissionColorB

    IOR = FloatField()

    normal = NormalField()
    normalX = normal.normalX
    normalx = normalX
    normalY = normal.normalY
    normaly = normalY
    normalZ = normal.normalZ
    normalz = normalZ

    tangent = TangentField()
    tangentX = tangent.tangentX
    tangentx = tangentX
    tangentY = tangent.tangentY
    tangenty = tangentY
    tangentZ = tangent.tangentZ
    tangentz = tangentZ

    indirectDiffuse = FloatField()
    indirect_diffuse = indirectDiffuse

    indirectSpecular = FloatField()
    indirect_specular = indirectSpecular

    bumpMode = BumpModeEnumField()
    bump_mode = bumpMode

    energyConserving = BoolField()
    energy_conserving = energyConserving

    userId = BoolField()
    user_id = userId

    aovPrefix = DataStringField()
    aov_prefix = aovPrefix
