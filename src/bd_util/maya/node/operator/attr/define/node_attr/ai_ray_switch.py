# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "outr"),
        ("outColorG", "outg"),
        ("outColorB", "outb"),
    )

    outColorR = FloatField()
    outr = outColorR

    outColorG = FloatField()
    outg = outColorG

    outColorB = FloatField()
    outb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField()
    outr = outColorR

    outColorG = FloatField()
    outg = outColorG

    outColorB = FloatField()
    outb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField()
    outr = outColorR

    outColorG = FloatField()
    outg = outColorG

    outColorB = FloatField()
    outb = outColorB


class OutTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["OutTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTransparencyR", "otr"),
        ("outTransparencyG", "otg"),
        ("outTransparencyB", "otb"),
    )

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class NormalCameraPlugOperator(
    Float3CompoundBasePlugOperator["NormalCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalCameraX", "nx"),
        ("normalCameraY", "ny"),
        ("normalCameraZ", "nz"),
    )

    normalCameraX = FloatField()
    nx = normalCameraX

    normalCameraY = FloatField()
    ny = normalCameraY

    normalCameraZ = FloatField()
    nz = normalCameraZ


class NormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[NormalCameraPlugOperator]
):
    __slots__ = ()

    normalCameraX = FloatField()
    nx = normalCameraX

    normalCameraY = FloatField()
    ny = normalCameraY

    normalCameraZ = FloatField()
    nz = normalCameraZ


class NormalCameraField(
    Float3CompoundBaseField[NormalCameraAttrOperator, NormalCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalCameraAttrOperator
    PLUG_CLS = NormalCameraPlugOperator

    normalCameraX = FloatField()
    nx = normalCameraX

    normalCameraY = FloatField()
    ny = normalCameraY

    normalCameraZ = FloatField()
    nz = normalCameraZ


class HardwareColorPlugOperator(
    Float3CompoundBasePlugOperator["HardwareColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hardwareColorR", "hwcr"),
        ("hardwareColorG", "hwcg"),
        ("hardwareColorB", "hwcb"),
    )

    hardwareColorR = FloatField()
    hwcr = hardwareColorR

    hardwareColorG = FloatField()
    hwcg = hardwareColorG

    hardwareColorB = FloatField()
    hwcb = hardwareColorB


class HardwareColorAttrOperator(
    Float3CompoundBaseAttrOperator[HardwareColorPlugOperator]
):
    __slots__ = ()

    hardwareColorR = FloatField()
    hwcr = hardwareColorR

    hardwareColorG = FloatField()
    hwcg = hardwareColorG

    hardwareColorB = FloatField()
    hwcb = hardwareColorB


class HardwareColorField(
    Float3CompoundBaseField[HardwareColorAttrOperator, HardwareColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HardwareColorAttrOperator
    PLUG_CLS = HardwareColorPlugOperator

    hardwareColorR = FloatField()
    hwcr = hardwareColorR

    hardwareColorG = FloatField()
    hwcg = hardwareColorG

    hardwareColorB = FloatField()
    hwcb = hardwareColorB


class CameraPlugOperator(
    Float3CompoundBasePlugOperator["CameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cameraR", "camerar"),
        ("cameraG", "camerag"),
        ("cameraB", "camerab"),
    )

    cameraR = FloatField()
    camerar = cameraR

    cameraG = FloatField()
    camerag = cameraG

    cameraB = FloatField()
    camerab = cameraB


class CameraAttrOperator(
    Float3CompoundBaseAttrOperator[CameraPlugOperator]
):
    __slots__ = ()

    cameraR = FloatField()
    camerar = cameraR

    cameraG = FloatField()
    camerag = cameraG

    cameraB = FloatField()
    camerab = cameraB


class CameraField(
    Float3CompoundBaseField[CameraAttrOperator, CameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CameraAttrOperator
    PLUG_CLS = CameraPlugOperator

    cameraR = FloatField()
    camerar = cameraR

    cameraG = FloatField()
    camerag = cameraG

    cameraB = FloatField()
    camerab = cameraB


class ShadowPlugOperator(
    Float3CompoundBasePlugOperator["ShadowAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shadowR", "shadowr"),
        ("shadowG", "shadowg"),
        ("shadowB", "shadowb"),
    )

    shadowR = FloatField()
    shadowr = shadowR

    shadowG = FloatField()
    shadowg = shadowG

    shadowB = FloatField()
    shadowb = shadowB


class ShadowAttrOperator(
    Float3CompoundBaseAttrOperator[ShadowPlugOperator]
):
    __slots__ = ()

    shadowR = FloatField()
    shadowr = shadowR

    shadowG = FloatField()
    shadowg = shadowG

    shadowB = FloatField()
    shadowb = shadowB


class ShadowField(
    Float3CompoundBaseField[ShadowAttrOperator, ShadowPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShadowAttrOperator
    PLUG_CLS = ShadowPlugOperator

    shadowR = FloatField()
    shadowr = shadowR

    shadowG = FloatField()
    shadowg = shadowG

    shadowB = FloatField()
    shadowb = shadowB


class DiffuseReflectionPlugOperator(
    Float3CompoundBasePlugOperator["DiffuseReflectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("diffuseReflectionR", "diffuse_reflectionr"),
        ("diffuseReflectionG", "diffuse_reflectiong"),
        ("diffuseReflectionB", "diffuse_reflectionb"),
    )

    diffuseReflectionR = FloatField()
    diffuse_reflectionr = diffuseReflectionR

    diffuseReflectionG = FloatField()
    diffuse_reflectiong = diffuseReflectionG

    diffuseReflectionB = FloatField()
    diffuse_reflectionb = diffuseReflectionB


class DiffuseReflectionAttrOperator(
    Float3CompoundBaseAttrOperator[DiffuseReflectionPlugOperator]
):
    __slots__ = ()

    diffuseReflectionR = FloatField()
    diffuse_reflectionr = diffuseReflectionR

    diffuseReflectionG = FloatField()
    diffuse_reflectiong = diffuseReflectionG

    diffuseReflectionB = FloatField()
    diffuse_reflectionb = diffuseReflectionB


class DiffuseReflectionField(
    Float3CompoundBaseField[DiffuseReflectionAttrOperator, DiffuseReflectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DiffuseReflectionAttrOperator
    PLUG_CLS = DiffuseReflectionPlugOperator

    diffuseReflectionR = FloatField()
    diffuse_reflectionr = diffuseReflectionR

    diffuseReflectionG = FloatField()
    diffuse_reflectiong = diffuseReflectionG

    diffuseReflectionB = FloatField()
    diffuse_reflectionb = diffuseReflectionB


class DiffuseTransmissionPlugOperator(
    Float3CompoundBasePlugOperator["DiffuseTransmissionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("diffuseTransmissionR", "diffuse_transmissionr"),
        ("diffuseTransmissionG", "diffuse_transmissiong"),
        ("diffuseTransmissionB", "diffuse_transmissionb"),
    )

    diffuseTransmissionR = FloatField()
    diffuse_transmissionr = diffuseTransmissionR

    diffuseTransmissionG = FloatField()
    diffuse_transmissiong = diffuseTransmissionG

    diffuseTransmissionB = FloatField()
    diffuse_transmissionb = diffuseTransmissionB


class DiffuseTransmissionAttrOperator(
    Float3CompoundBaseAttrOperator[DiffuseTransmissionPlugOperator]
):
    __slots__ = ()

    diffuseTransmissionR = FloatField()
    diffuse_transmissionr = diffuseTransmissionR

    diffuseTransmissionG = FloatField()
    diffuse_transmissiong = diffuseTransmissionG

    diffuseTransmissionB = FloatField()
    diffuse_transmissionb = diffuseTransmissionB


class DiffuseTransmissionField(
    Float3CompoundBaseField[DiffuseTransmissionAttrOperator, DiffuseTransmissionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DiffuseTransmissionAttrOperator
    PLUG_CLS = DiffuseTransmissionPlugOperator

    diffuseTransmissionR = FloatField()
    diffuse_transmissionr = diffuseTransmissionR

    diffuseTransmissionG = FloatField()
    diffuse_transmissiong = diffuseTransmissionG

    diffuseTransmissionB = FloatField()
    diffuse_transmissionb = diffuseTransmissionB


class SpecularReflectionPlugOperator(
    Float3CompoundBasePlugOperator["SpecularReflectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularReflectionR", "specular_reflectionr"),
        ("specularReflectionG", "specular_reflectiong"),
        ("specularReflectionB", "specular_reflectionb"),
    )

    specularReflectionR = FloatField()
    specular_reflectionr = specularReflectionR

    specularReflectionG = FloatField()
    specular_reflectiong = specularReflectionG

    specularReflectionB = FloatField()
    specular_reflectionb = specularReflectionB


class SpecularReflectionAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularReflectionPlugOperator]
):
    __slots__ = ()

    specularReflectionR = FloatField()
    specular_reflectionr = specularReflectionR

    specularReflectionG = FloatField()
    specular_reflectiong = specularReflectionG

    specularReflectionB = FloatField()
    specular_reflectionb = specularReflectionB


class SpecularReflectionField(
    Float3CompoundBaseField[SpecularReflectionAttrOperator, SpecularReflectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularReflectionAttrOperator
    PLUG_CLS = SpecularReflectionPlugOperator

    specularReflectionR = FloatField()
    specular_reflectionr = specularReflectionR

    specularReflectionG = FloatField()
    specular_reflectiong = specularReflectionG

    specularReflectionB = FloatField()
    specular_reflectionb = specularReflectionB


class SpecularTransmissionPlugOperator(
    Float3CompoundBasePlugOperator["SpecularTransmissionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularTransmissionR", "specular_transmissionr"),
        ("specularTransmissionG", "specular_transmissiong"),
        ("specularTransmissionB", "specular_transmissionb"),
    )

    specularTransmissionR = FloatField()
    specular_transmissionr = specularTransmissionR

    specularTransmissionG = FloatField()
    specular_transmissiong = specularTransmissionG

    specularTransmissionB = FloatField()
    specular_transmissionb = specularTransmissionB


class SpecularTransmissionAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularTransmissionPlugOperator]
):
    __slots__ = ()

    specularTransmissionR = FloatField()
    specular_transmissionr = specularTransmissionR

    specularTransmissionG = FloatField()
    specular_transmissiong = specularTransmissionG

    specularTransmissionB = FloatField()
    specular_transmissionb = specularTransmissionB


class SpecularTransmissionField(
    Float3CompoundBaseField[SpecularTransmissionAttrOperator, SpecularTransmissionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularTransmissionAttrOperator
    PLUG_CLS = SpecularTransmissionPlugOperator

    specularTransmissionR = FloatField()
    specular_transmissionr = specularTransmissionR

    specularTransmissionG = FloatField()
    specular_transmissiong = specularTransmissionG

    specularTransmissionB = FloatField()
    specular_transmissionb = specularTransmissionB


class VolumePlugOperator(
    Float3CompoundBasePlugOperator["VolumeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("volumeR", "volumer"),
        ("volumeG", "volumeg"),
        ("volumeB", "volumeb"),
    )

    volumeR = FloatField()
    volumer = volumeR

    volumeG = FloatField()
    volumeg = volumeG

    volumeB = FloatField()
    volumeb = volumeB


class VolumeAttrOperator(
    Float3CompoundBaseAttrOperator[VolumePlugOperator]
):
    __slots__ = ()

    volumeR = FloatField()
    volumer = volumeR

    volumeG = FloatField()
    volumeg = volumeG

    volumeB = FloatField()
    volumeb = volumeB


class VolumeField(
    Float3CompoundBaseField[VolumeAttrOperator, VolumePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VolumeAttrOperator
    PLUG_CLS = VolumePlugOperator

    volumeR = FloatField()
    volumer = volumeR

    volumeG = FloatField()
    volumeg = volumeG

    volumeB = FloatField()
    volumeb = volumeB
