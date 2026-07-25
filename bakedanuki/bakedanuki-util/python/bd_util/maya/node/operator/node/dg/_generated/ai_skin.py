# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_skin import (
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
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class _GeneratedAiSkin(DG):
    __slots__ = ()

    NODE_TYPE = "aiSkin"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    outa = outAlpha

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    sssWeight = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    sss_weight = sssWeight

    shallowScatterColor = ShallowScatterColorField(default_value=(1.0, 0.9089999794960022, 0.7689999938011169))
    shallow_scatter_color = shallowScatterColor
    shallowScatterColorR = shallowScatterColor.shallowScatterColorR
    shallow_scatter_colorr = shallowScatterColorR
    shallowScatterColorG = shallowScatterColor.shallowScatterColorG
    shallow_scatter_colorg = shallowScatterColorG
    shallowScatterColorB = shallowScatterColor.shallowScatterColorB
    shallow_scatter_colorb = shallowScatterColorB

    shallowScatterWeight = FloatField(default_value=0.5, min_value=0.0, soft_max_value=1.0)
    shallow_scatter_weight = shallowScatterWeight

    shallowScatterRadius = FloatField(default_value=0.15000000596046448, min_value=0.0, soft_max_value=1.0)
    shallow_scatter_radius = shallowScatterRadius

    midScatterColor = MidScatterColorField(default_value=(0.9490000009536743, 0.7139999866485596, 0.5600000023841858))
    mid_scatter_color = midScatterColor
    midScatterColorR = midScatterColor.midScatterColorR
    mid_scatter_colorr = midScatterColorR
    midScatterColorG = midScatterColor.midScatterColorG
    mid_scatter_colorg = midScatterColorG
    midScatterColorB = midScatterColor.midScatterColorB
    mid_scatter_colorb = midScatterColorB

    midScatterWeight = FloatField(default_value=0.25, min_value=0.0, soft_max_value=1.0)
    mid_scatter_weight = midScatterWeight

    midScatterRadius = FloatField(default_value=0.25, min_value=0.0, soft_max_value=1.0)
    mid_scatter_radius = midScatterRadius

    deepScatterColor = DeepScatterColorField(default_value=(0.699999988079071, 0.10000000149011612, 0.10000000149011612))
    deep_scatter_color = deepScatterColor
    deepScatterColorR = deepScatterColor.deepScatterColorR
    deep_scatter_colorr = deepScatterColorR
    deepScatterColorG = deepScatterColor.deepScatterColorG
    deep_scatter_colorg = deepScatterColorG
    deepScatterColorB = deepScatterColor.deepScatterColorB
    deep_scatter_colorb = deepScatterColorB

    deepScatterWeight = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    deep_scatter_weight = deepScatterWeight

    deepScatterRadius = FloatField(default_value=0.6000000238418579, min_value=0.0, soft_max_value=1.0)
    deep_scatter_radius = deepScatterRadius

    specularColor = SpecularColorField(default_value=(1.0, 1.0, 1.0))
    specular_color = specularColor
    specularColorR = specularColor.specularColorR
    specular_colorr = specularColorR
    specularColorG = specularColor.specularColorG
    specular_colorg = specularColorG
    specularColorB = specularColor.specularColorB
    specular_colorb = specularColorB

    specularWeight = FloatField(default_value=0.800000011920929, min_value=0.0, max_value=1.0)
    specular_weight = specularWeight

    specularRoughness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    specular_roughness = specularRoughness

    specularIor = FloatField(default_value=1.440000057220459, min_value=0.0, soft_min_value=1.0, soft_max_value=5.0)
    specular_ior = specularIor

    sheenColor = SheenColorField(default_value=(1.0, 1.0, 1.0))
    sheen_color = sheenColor
    sheenColorR = sheenColor.sheenColorR
    sheen_colorr = sheenColorR
    sheenColorG = sheenColor.sheenColorG
    sheen_colorg = sheenColorG
    sheenColorB = sheenColor.sheenColorB
    sheen_colorb = sheenColorB

    sheenWeight = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    sheen_weight = sheenWeight

    sheenRoughness = FloatField(default_value=0.3499999940395355, min_value=0.0, max_value=1.0)
    sheen_roughness = sheenRoughness

    sheenIor = FloatField(default_value=1.440000057220459, min_value=0.0, soft_min_value=1.0, soft_max_value=5.0)
    sheen_ior = sheenIor

    globalSssRadiusMultiplier = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=20.0)
    global_sss_radius_multiplier = globalSssRadiusMultiplier

    specularInSecondaryRays = BoolField(default_value=False)
    specular_in_secondary_rays = specularInSecondaryRays

    fresnelAffectSss = BoolField(default_value=True)
    fresnel_affect_sss = fresnelAffectSss

    opacity = FloatField(default_value=1.0)

    opacityColor = OpacityColorField(default_value=(1.0, 1.0, 1.0))
    opacity_color = opacityColor
    opacityColorR = opacityColor.opacityColorR
    opacity_colorr = opacityColorR
    opacityColorG = opacityColor.opacityColorG
    opacity_colorg = opacityColorG
    opacityColorB = opacityColor.opacityColorB
    opacity_colorb = opacityColorB

    normal = NormalField(default_value=(0.0, 1.0, 0.0))
    normalX = normal.normalX
    normalx = normalX
    normalY = normal.normalY
    normaly = normalY
    normalZ = normal.normalZ
    normalz = normalZ
