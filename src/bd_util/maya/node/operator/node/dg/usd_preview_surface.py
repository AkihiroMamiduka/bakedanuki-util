# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.usd_preview_surface import (
    DiffuseColorField,
    EmissiveColorField,
    NormalField,
    OutColorField,
    OutTransparencyField,
    SpecularColorField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class UsdPreviewSurface(DG):
    __slots__ = ()

    NODE_TYPE = "usdPreviewSurface"

    clearcoat = FloatField()
    cc = clearcoat

    clearcoatRoughness = FloatField()
    ccr = clearcoatRoughness

    diffuseColor = DiffuseColorField()
    dc = diffuseColor
    diffuseColorR = diffuseColor.diffuseColorR
    dcr = diffuseColorR
    diffuseColorG = diffuseColor.diffuseColorG
    dcg = diffuseColorG
    diffuseColorB = diffuseColor.diffuseColorB
    dcb = diffuseColorB

    displacement = FloatField()
    dsp = displacement

    emissiveColor = EmissiveColorField()
    ec = emissiveColor
    emissiveColorR = emissiveColor.emissiveColorR
    ecr = emissiveColorR
    emissiveColorG = emissiveColor.emissiveColorG
    ecg = emissiveColorG
    emissiveColorB = emissiveColor.emissiveColorB
    ecb = emissiveColorB

    ior = FloatField()

    metallic = FloatField()
    mtl = metallic

    normal = NormalField()
    nrm = normal
    normal0 = normal.normal0
    nrm0 = normal0
    normal1 = normal.normal1
    nrm1 = normal1
    normal2 = normal.normal2
    nrm2 = normal2

    occlusion = FloatField()
    ocl = occlusion

    opacity = FloatField()
    opc = opacity

    opacityThreshold = FloatField()
    opt = opacityThreshold

    roughness = FloatField()
    rgh = roughness

    specularColor = SpecularColorField()
    spc = specularColor
    specularColorR = specularColor.specularColorR
    spcr = specularColorR
    specularColorG = specularColor.specularColorG
    spcg = specularColorG
    specularColorB = specularColor.specularColorB
    spcb = specularColorB

    useSpecularWorkflow = BoolField()
    usw = useSpecularWorkflow

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

    outTransparencyOn = FloatField()
    oto = outTransparencyOn
