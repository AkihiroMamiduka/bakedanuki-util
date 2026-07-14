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

    outColor = OutColorField(default_value=(0.5, 0.5, 0.5), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.5, 0.5, 0.5), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    normalCamera = NormalCameraField(default_value=(0.0, 0.0, 0.0))
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    hardwareColor = HardwareColorField(default_value=(0.5, 0.5, 0.5))
    hwc = hardwareColor
    hardwareColorR = hardwareColor.hardwareColorR
    hwcr = hardwareColorR
    hardwareColorG = hardwareColor.hardwareColorG
    hwcg = hardwareColorG
    hardwareColorB = hardwareColor.hardwareColorB
    hwcb = hardwareColorB

    maskColor = MaskColorField(default_value=(0.0, 0.0, 0.0))
    mask_color = maskColor
    maskColorR = maskColor.maskColorR
    mask_colorr = maskColorR
    maskColorG = maskColor.maskColorG
    mask_colorg = maskColorG
    maskColorB = maskColor.maskColorB
    mask_colorb = maskColorB

    edgeColor = EdgeColorField(default_value=(0.0, 0.0, 0.0))
    edge_color = edgeColor
    edgeColorR = edgeColor.edgeColorR
    edge_colorr = edgeColorR
    edgeColorG = edgeColor.edgeColorG
    edge_colorg = edgeColorG
    edgeColorB = edgeColor.edgeColorB
    edge_colorb = edgeColorB

    edgeTonemap = EdgeTonemapField(default_value=(1.0, 1.0, 1.0))
    edge_tonemap = edgeTonemap
    edgeTonemapR = edgeTonemap.edgeTonemapR
    edge_tonemapr = edgeTonemapR
    edgeTonemapG = edgeTonemap.edgeTonemapG
    edge_tonemapg = edgeTonemapG
    edgeTonemapB = edgeTonemap.edgeTonemapB
    edge_tonemapb = edgeTonemapB

    edgeOpacity = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    edge_opacity = edgeOpacity

    edgeWidthScale = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    edge_width_scale = edgeWidthScale

    silhouetteColor = SilhouetteColorField(default_value=(0.0, 0.0, 0.0))
    silhouette_color = silhouetteColor
    silhouetteColorR = silhouetteColor.silhouetteColorR
    silhouette_colorr = silhouetteColorR
    silhouetteColorG = silhouetteColor.silhouetteColorG
    silhouette_colorg = silhouetteColorG
    silhouetteColorB = silhouetteColor.silhouetteColorB
    silhouette_colorb = silhouetteColorB

    silhouetteTonemap = SilhouetteTonemapField(default_value=(1.0, 1.0, 1.0))
    silhouette_tonemap = silhouetteTonemap
    silhouetteTonemapR = silhouetteTonemap.silhouetteTonemapR
    silhouette_tonemapr = silhouetteTonemapR
    silhouetteTonemapG = silhouetteTonemap.silhouetteTonemapG
    silhouette_tonemapg = silhouetteTonemapG
    silhouetteTonemapB = silhouetteTonemap.silhouetteTonemapB
    silhouette_tonemapb = silhouetteTonemapB

    silhouetteOpacity = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    silhouette_opacity = silhouetteOpacity

    silhouetteWidthScale = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    silhouette_width_scale = silhouetteWidthScale

    priority = LongField(default_value=0)

    enableSilhouette = BoolField(default_value=False)
    enable_silhouette = enableSilhouette

    ignoreThroughput = BoolField(default_value=False)
    ignore_throughput = ignoreThroughput

    enable = BoolField(default_value=True)

    idDifference = BoolField(default_value=True)
    id_difference = idDifference

    shaderDifference = BoolField(default_value=True)
    shader_difference = shaderDifference

    uvThreshold = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    uv_threshold = uvThreshold

    angleThreshold = FloatField(default_value=180.0, min_value=0.0, max_value=180.0)
    angle_threshold = angleThreshold

    normalType = NormalTypeEnumField(default_value=0)
    normal_type = normalType

    base = FloatField(default_value=0.800000011920929, min_value=0.0, max_value=1.0)

    baseColor = BaseColorField(default_value=(1.0, 1.0, 1.0))
    base_color = baseColor
    baseColorR = baseColor.baseColorR
    base_colorr = baseColorR
    baseColorG = baseColor.baseColorG
    base_colorg = baseColorG
    baseColorB = baseColor.baseColorB
    base_colorb = baseColorB

    baseTonemap = BaseTonemapField(default_value=(1.0, 1.0, 1.0))
    base_tonemap = baseTonemap
    baseTonemapR = baseTonemap.baseTonemapR
    base_tonemapr = baseTonemapR
    baseTonemapG = baseTonemap.baseTonemapG
    base_tonemapg = baseTonemapG
    baseTonemapB = baseTonemap.baseTonemapB
    base_tonemapb = baseTonemapB

    specular = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    specularColor = SpecularColorField(default_value=(1.0, 1.0, 1.0))
    specular_color = specularColor
    specularColorR = specularColor.specularColorR
    specular_colorr = specularColorR
    specularColorG = specularColor.specularColorG
    specular_colorg = specularColorG
    specularColorB = specularColor.specularColorB
    specular_colorb = specularColorB

    specularRoughness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    specular_roughness = specularRoughness

    specularAnisotropy = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    specular_anisotropy = specularAnisotropy

    specularRotation = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    specular_rotation = specularRotation

    specularTonemap = SpecularTonemapField(default_value=(1.0, 1.0, 1.0))
    specular_tonemap = specularTonemap
    specularTonemapR = specularTonemap.specularTonemapR
    specular_tonemapr = specularTonemapR
    specularTonemapG = specularTonemap.specularTonemapG
    specular_tonemapg = specularTonemapG
    specularTonemapB = specularTonemap.specularTonemapB
    specular_tonemapb = specularTonemapB

    lights = DataStringField()

    highlightColor = HighlightColorField(default_value=(1.0, 1.0, 1.0))
    highlight_color = highlightColor
    highlightColorR = highlightColor.highlightColorR
    highlight_colorr = highlightColorR
    highlightColorG = highlightColor.highlightColorG
    highlight_colorg = highlightColorG
    highlightColorB = highlightColor.highlightColorB
    highlight_colorb = highlightColorB

    highlightSize = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    highlight_size = highlightSize

    aovHighlight = DataStringField()
    aov_highlight = aovHighlight

    rimLight = DataStringField()
    rim_light = rimLight

    rimLightColor = RimLightColorField(default_value=(0.0, 0.0, 0.0))
    rim_light_color = rimLightColor
    rimLightColorR = rimLightColor.rimLightColorR
    rim_light_colorr = rimLightColorR
    rimLightColorG = rimLightColor.rimLightColorG
    rim_light_colorg = rimLightColorG
    rimLightColorB = rimLightColor.rimLightColorB
    rim_light_colorb = rimLightColorB

    rimLightWidth = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    rim_light_width = rimLightWidth

    rimLightTint = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rim_light_tint = rimLightTint

    aovRimLight = DataStringField()
    aov_rim_light = aovRimLight

    transmission = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    transmissionColor = TransmissionColorField(default_value=(1.0, 1.0, 1.0))
    transmission_color = transmissionColor
    transmissionColorR = transmissionColor.transmissionColorR
    transmission_colorr = transmissionColorR
    transmissionColorG = transmissionColor.transmissionColorG
    transmission_colorg = transmissionColorG
    transmissionColorB = transmissionColor.transmissionColorB
    transmission_colorb = transmissionColorB

    transmissionRoughness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    transmission_roughness = transmissionRoughness

    transmissionAnisotropy = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    transmission_anisotropy = transmissionAnisotropy

    transmissionRotation = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    transmission_rotation = transmissionRotation

    sheen = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    sheenColor = SheenColorField(default_value=(1.0, 1.0, 1.0))
    sheen_color = sheenColor
    sheenColorR = sheenColor.sheenColorR
    sheen_colorr = sheenColorR
    sheenColorG = sheenColor.sheenColorG
    sheen_colorg = sheenColorG
    sheenColorB = sheenColor.sheenColorB
    sheen_colorb = sheenColorB

    sheenRoughness = FloatField(default_value=0.30000001192092896, min_value=0.0, max_value=1.0)
    sheen_roughness = sheenRoughness

    emission = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)

    emissionColor = EmissionColorField(default_value=(1.0, 1.0, 1.0))
    emission_color = emissionColor
    emissionColorR = emissionColor.emissionColorR
    emission_colorr = emissionColorR
    emissionColorG = emissionColor.emissionColorG
    emission_colorg = emissionColorG
    emissionColorB = emissionColor.emissionColorB
    emission_colorb = emissionColorB

    IOR = FloatField(default_value=1.5199999809265137, min_value=0.0, soft_max_value=3.0)

    normal = NormalField(default_value=(0.0, 0.0, 0.0))
    normalX = normal.normalX
    normalx = normalX
    normalY = normal.normalY
    normaly = normalY
    normalZ = normal.normalZ
    normalz = normalZ

    tangent = TangentField(default_value=(0.0, 0.0, 0.0))
    tangentX = tangent.tangentX
    tangentx = tangentX
    tangentY = tangent.tangentY
    tangenty = tangentY
    tangentZ = tangent.tangentZ
    tangentz = tangentZ

    indirectDiffuse = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    indirect_diffuse = indirectDiffuse

    indirectSpecular = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    indirect_specular = indirectSpecular

    bumpMode = BumpModeEnumField(default_value=0)
    bump_mode = bumpMode

    energyConserving = BoolField(default_value=True)
    energy_conserving = energyConserving

    userId = BoolField(default_value=False)
    user_id = userId

    aovPrefix = DataStringField()
    aov_prefix = aovPrefix
