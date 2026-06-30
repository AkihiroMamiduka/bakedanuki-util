# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_skin import (
    DeepScatterColorField,
    MidScatterColorField,
    NormalField,
    OpacityColorField,
    OutColorField,
    OutTransparencyField,
    ShallowScatterColorField,
    SheenColorField,
    SpecularColorField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiSkin(DG):
    __slots__ = ()

    NODE_TYPE = "aiSkin"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField()
    outa = outAlpha

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    sssWeight = FloatField()
    sss_weight = sssWeight

    shallowScatterColor = ShallowScatterColorField()
    shallow_scatter_color = shallowScatterColor
    shallowScatterColorR = shallowScatterColor.shallowScatterColorR
    shallow_scatter_colorr = shallowScatterColorR
    shallowScatterColorG = shallowScatterColor.shallowScatterColorG
    shallow_scatter_colorg = shallowScatterColorG
    shallowScatterColorB = shallowScatterColor.shallowScatterColorB
    shallow_scatter_colorb = shallowScatterColorB

    shallowScatterWeight = FloatField()
    shallow_scatter_weight = shallowScatterWeight

    shallowScatterRadius = FloatField()
    shallow_scatter_radius = shallowScatterRadius

    midScatterColor = MidScatterColorField()
    mid_scatter_color = midScatterColor
    midScatterColorR = midScatterColor.midScatterColorR
    mid_scatter_colorr = midScatterColorR
    midScatterColorG = midScatterColor.midScatterColorG
    mid_scatter_colorg = midScatterColorG
    midScatterColorB = midScatterColor.midScatterColorB
    mid_scatter_colorb = midScatterColorB

    midScatterWeight = FloatField()
    mid_scatter_weight = midScatterWeight

    midScatterRadius = FloatField()
    mid_scatter_radius = midScatterRadius

    deepScatterColor = DeepScatterColorField()
    deep_scatter_color = deepScatterColor
    deepScatterColorR = deepScatterColor.deepScatterColorR
    deep_scatter_colorr = deepScatterColorR
    deepScatterColorG = deepScatterColor.deepScatterColorG
    deep_scatter_colorg = deepScatterColorG
    deepScatterColorB = deepScatterColor.deepScatterColorB
    deep_scatter_colorb = deepScatterColorB

    deepScatterWeight = FloatField()
    deep_scatter_weight = deepScatterWeight

    deepScatterRadius = FloatField()
    deep_scatter_radius = deepScatterRadius

    specularColor = SpecularColorField()
    specular_color = specularColor
    specularColorR = specularColor.specularColorR
    specular_colorr = specularColorR
    specularColorG = specularColor.specularColorG
    specular_colorg = specularColorG
    specularColorB = specularColor.specularColorB
    specular_colorb = specularColorB

    specularWeight = FloatField()
    specular_weight = specularWeight

    specularRoughness = FloatField()
    specular_roughness = specularRoughness

    specularIor = FloatField()
    specular_ior = specularIor

    sheenColor = SheenColorField()
    sheen_color = sheenColor
    sheenColorR = sheenColor.sheenColorR
    sheen_colorr = sheenColorR
    sheenColorG = sheenColor.sheenColorG
    sheen_colorg = sheenColorG
    sheenColorB = sheenColor.sheenColorB
    sheen_colorb = sheenColorB

    sheenWeight = FloatField()
    sheen_weight = sheenWeight

    sheenRoughness = FloatField()
    sheen_roughness = sheenRoughness

    sheenIor = FloatField()
    sheen_ior = sheenIor

    globalSssRadiusMultiplier = FloatField()
    global_sss_radius_multiplier = globalSssRadiusMultiplier

    specularInSecondaryRays = BoolField()
    specular_in_secondary_rays = specularInSecondaryRays

    fresnelAffectSss = BoolField()
    fresnel_affect_sss = fresnelAffectSss

    opacity = FloatField()

    opacityColor = OpacityColorField()
    opacity_color = opacityColor
    opacityColorR = opacityColor.opacityColorR
    opacity_colorr = opacityColorR
    opacityColorG = opacityColor.opacityColorG
    opacity_colorg = opacityColorG
    opacityColorB = opacityColor.opacityColorB
    opacity_colorb = opacityColorB

    normal = NormalField()
    normalX = normal.normalX
    normalx = normalX
    normalY = normal.normalY
    normaly = normalY
    normalZ = normal.normalZ
    normalz = normalZ
