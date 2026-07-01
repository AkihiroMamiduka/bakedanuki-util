# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_ray_switch import (
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
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class AiRaySwitch(DG):
    __slots__ = ()

    NODE_TYPE = "aiRaySwitch"

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

    cameraA = FloatField()
    cameraa = cameraA

    camera = CameraField()
    cameraR = camera.cameraR
    camerar = cameraR
    cameraG = camera.cameraG
    camerag = cameraG
    cameraB = camera.cameraB
    camerab = cameraB

    shadowA = FloatField()
    shadowa = shadowA

    shadow = ShadowField()
    shadowR = shadow.shadowR
    shadowr = shadowR
    shadowG = shadow.shadowG
    shadowg = shadowG
    shadowB = shadow.shadowB
    shadowb = shadowB

    diffuseReflectionA = FloatField()
    diffuse_reflectiona = diffuseReflectionA

    diffuseReflection = DiffuseReflectionField()
    diffuse_reflection = diffuseReflection
    diffuseReflectionR = diffuseReflection.diffuseReflectionR
    diffuse_reflectionr = diffuseReflectionR
    diffuseReflectionG = diffuseReflection.diffuseReflectionG
    diffuse_reflectiong = diffuseReflectionG
    diffuseReflectionB = diffuseReflection.diffuseReflectionB
    diffuse_reflectionb = diffuseReflectionB

    diffuseTransmissionA = FloatField()
    diffuse_transmissiona = diffuseTransmissionA

    diffuseTransmission = DiffuseTransmissionField()
    diffuse_transmission = diffuseTransmission
    diffuseTransmissionR = diffuseTransmission.diffuseTransmissionR
    diffuse_transmissionr = diffuseTransmissionR
    diffuseTransmissionG = diffuseTransmission.diffuseTransmissionG
    diffuse_transmissiong = diffuseTransmissionG
    diffuseTransmissionB = diffuseTransmission.diffuseTransmissionB
    diffuse_transmissionb = diffuseTransmissionB

    specularReflectionA = FloatField()
    specular_reflectiona = specularReflectionA

    specularReflection = SpecularReflectionField()
    specular_reflection = specularReflection
    specularReflectionR = specularReflection.specularReflectionR
    specular_reflectionr = specularReflectionR
    specularReflectionG = specularReflection.specularReflectionG
    specular_reflectiong = specularReflectionG
    specularReflectionB = specularReflection.specularReflectionB
    specular_reflectionb = specularReflectionB

    specularTransmissionA = FloatField()
    specular_transmissiona = specularTransmissionA

    specularTransmission = SpecularTransmissionField()
    specular_transmission = specularTransmission
    specularTransmissionR = specularTransmission.specularTransmissionR
    specular_transmissionr = specularTransmissionR
    specularTransmissionG = specularTransmission.specularTransmissionG
    specular_transmissiong = specularTransmissionG
    specularTransmissionB = specularTransmission.specularTransmissionB
    specular_transmissionb = specularTransmissionB

    volumeA = FloatField()
    volumea = volumeA

    volume = VolumeField()
    volumeR = volume.volumeR
    volumer = volumeR
    volumeG = volume.volumeG
    volumeg = volumeG
    volumeB = volume.volumeB
    volumeb = volumeB

    aiUserOptions = DataStringField()
    ai_user_options = aiUserOptions
