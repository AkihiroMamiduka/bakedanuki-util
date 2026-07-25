# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.usd_preview_surface import (
    DiffuseColorField,
    EmissiveColorField,
    NormalField,
    OutColorField,
    OutTransparencyField,
    SpecularColorField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class _GeneratedUsdPreviewSurface(DG):
    __slots__ = ()

    NODE_TYPE = "usdPreviewSurface"

    clearcoat = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    cc = clearcoat

    clearcoatRoughness = FloatField(default_value=0.009999999776482582, min_value=0.001, soft_min_value=0.001, soft_max_value=1.0)
    ccr = clearcoatRoughness

    diffuseColor = DiffuseColorField(default_value=(0.18000000715255737, 0.18000000715255737, 0.18000000715255737))
    dc = diffuseColor
    diffuseColorR = diffuseColor.diffuseColorR
    dcr = diffuseColorR
    diffuseColorG = diffuseColor.diffuseColorG
    dcg = diffuseColorG
    diffuseColorB = diffuseColor.diffuseColorB
    dcb = diffuseColorB

    displacement = FloatField(default_value=0.0)
    dsp = displacement

    emissiveColor = EmissiveColorField(default_value=(0.0, 0.0, 0.0))
    ec = emissiveColor
    emissiveColorR = emissiveColor.emissiveColorR
    ecr = emissiveColorR
    emissiveColorG = emissiveColor.emissiveColorG
    ecg = emissiveColorG
    emissiveColorB = emissiveColor.emissiveColorB
    ecb = emissiveColorB

    ior = FloatField(default_value=1.5)

    metallic = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mtl = metallic

    normal = NormalField(default_value=(0.0, 1.0, 0.0))
    nrm = normal
    normal0 = normal.normal0
    nrm0 = normal0
    normal1 = normal.normal1
    nrm1 = normal1
    normal2 = normal.normal2
    nrm2 = normal2

    occlusion = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    ocl = occlusion

    opacity = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    opc = opacity

    opacityThreshold = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    opt = opacityThreshold

    roughness = FloatField(default_value=0.5, min_value=0.001, soft_min_value=0.001, soft_max_value=1.0)
    rgh = roughness

    specularColor = SpecularColorField(default_value=(0.0, 0.0, 0.0))
    spc = specularColor
    specularColorR = specularColor.specularColorR
    spcr = specularColorR
    specularColorG = specularColor.specularColorG
    spcg = specularColorG
    specularColorB = specularColor.specularColorB
    spcb = specularColorB

    useSpecularWorkflow = BoolField(default_value=False)
    usw = useSpecularWorkflow

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

    outTransparencyOn = FloatField(default_value=0.0, writable=False)
    oto = outTransparencyOn
