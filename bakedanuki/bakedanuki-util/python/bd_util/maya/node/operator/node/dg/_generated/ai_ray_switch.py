# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_ray_switch import (
    CameraField,
    DiffuseReflectionField,
    DiffuseTransmissionField,
    HardwareColorField,
    NormalCameraField,
    OutColorField,
    OutTransparencyField,
    ShadowField,
    SpecularReflectionField,
    SpecularTransmissionField,
    VolumeField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class GeneratedAiRaySwitch(DG):
    __slots__ = ()

    NODE_TYPE = "aiRaySwitch"

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

    cameraA = FloatField(default_value=4.591634678053128e-41, min_value=0.0, max_value=1.0)
    cameraa = cameraA

    camera = CameraField(default_value=(0.0, 0.0, 0.0))
    cameraR = camera.cameraR
    camerar = cameraR
    cameraG = camera.cameraG
    camerag = cameraG
    cameraB = camera.cameraB
    camerab = cameraB

    shadowA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    shadowa = shadowA

    shadow = ShadowField(default_value=(0.0, 0.0, 0.0))
    shadowR = shadow.shadowR
    shadowr = shadowR
    shadowG = shadow.shadowG
    shadowg = shadowG
    shadowB = shadow.shadowB
    shadowb = shadowB

    diffuseReflectionA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    diffuse_reflectiona = diffuseReflectionA

    diffuseReflection = DiffuseReflectionField(default_value=(0.0, 0.0, 0.0))
    diffuse_reflection = diffuseReflection
    diffuseReflectionR = diffuseReflection.diffuseReflectionR
    diffuse_reflectionr = diffuseReflectionR
    diffuseReflectionG = diffuseReflection.diffuseReflectionG
    diffuse_reflectiong = diffuseReflectionG
    diffuseReflectionB = diffuseReflection.diffuseReflectionB
    diffuse_reflectionb = diffuseReflectionB

    diffuseTransmissionA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    diffuse_transmissiona = diffuseTransmissionA

    diffuseTransmission = DiffuseTransmissionField(default_value=(0.0, 0.0, 0.0))
    diffuse_transmission = diffuseTransmission
    diffuseTransmissionR = diffuseTransmission.diffuseTransmissionR
    diffuse_transmissionr = diffuseTransmissionR
    diffuseTransmissionG = diffuseTransmission.diffuseTransmissionG
    diffuse_transmissiong = diffuseTransmissionG
    diffuseTransmissionB = diffuseTransmission.diffuseTransmissionB
    diffuse_transmissionb = diffuseTransmissionB

    specularReflectionA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    specular_reflectiona = specularReflectionA

    specularReflection = SpecularReflectionField(default_value=(0.0, 0.0, 0.0))
    specular_reflection = specularReflection
    specularReflectionR = specularReflection.specularReflectionR
    specular_reflectionr = specularReflectionR
    specularReflectionG = specularReflection.specularReflectionG
    specular_reflectiong = specularReflectionG
    specularReflectionB = specularReflection.specularReflectionB
    specular_reflectionb = specularReflectionB

    specularTransmissionA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    specular_transmissiona = specularTransmissionA

    specularTransmission = SpecularTransmissionField(default_value=(0.0, 0.0, 0.0))
    specular_transmission = specularTransmission
    specularTransmissionR = specularTransmission.specularTransmissionR
    specular_transmissionr = specularTransmissionR
    specularTransmissionG = specularTransmission.specularTransmissionG
    specular_transmissiong = specularTransmissionG
    specularTransmissionB = specularTransmission.specularTransmissionB
    specular_transmissionb = specularTransmissionB

    volumeA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    volumea = volumeA

    volume = VolumeField(default_value=(0.0, 0.0, 0.0))
    volumeR = volume.volumeR
    volumer = volumeR
    volumeG = volume.volumeG
    volumeg = volumeG
    volumeB = volume.volumeB
    volumeb = volumeB

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions
