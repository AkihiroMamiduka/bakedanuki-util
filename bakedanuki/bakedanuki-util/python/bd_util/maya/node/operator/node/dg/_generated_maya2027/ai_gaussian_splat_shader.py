# coding: utf-8
from .._core import DG
from ....attr.define.node_attr_maya2027.ai_gaussian_splat_shader import (
    DiffuseTintField,
    EmissionTintField,
    HardwareColorField,
    NormalCameraField,
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class GeneratedAiGaussianSplatShader(DG):
    __slots__ = ()

    NODE_TYPE = "aiGaussianSplatShader"

    outColor = OutColorField(default_value=(0.5, 0.5, 0.5), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    outa = outAlpha

    outTransparency = OutTransparencyField(
        default_value=(0.5, 0.5, 0.5), writable=False
    )
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

    emissionWeight = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    emission_weight = emissionWeight

    emissionTint = EmissionTintField(default_value=(1.0, 1.0, 1.0))
    emission_tint = emissionTint
    emissionTintR = emissionTint.emissionTintR
    emission_tintr = emissionTintR
    emissionTintG = emissionTint.emissionTintG
    emission_tintg = emissionTintG
    emissionTintB = emissionTint.emissionTintB
    emission_tintb = emissionTintB

    diffuseWeight = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    diffuse_weight = diffuseWeight

    diffuseTint = DiffuseTintField(default_value=(1.0, 1.0, 1.0))
    diffuse_tint = diffuseTint
    diffuseTintR = diffuseTint.diffuseTintR
    diffuse_tintr = diffuseTintR
    diffuseTintG = diffuseTint.diffuseTintG
    diffuse_tintg = diffuseTintG
    diffuseTintB = diffuseTint.diffuseTintB
    diffuse_tintb = diffuseTintB

    diffuseRoughness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    diffuse_roughness = diffuseRoughness
