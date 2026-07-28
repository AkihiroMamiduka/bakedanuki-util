# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
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

    outColorR = FloatField(default_value=0.5, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.5, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.5, writable=False)
    outb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.5, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.5, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.5, writable=False)
    outb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.5, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.5, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.5, writable=False)
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

    outTransparencyR = FloatField(default_value=0.5, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.5, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.5, writable=False)
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField(default_value=0.5, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.5, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.5, writable=False)
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[
        OutTransparencyAttrOperator, OutTransparencyPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField(default_value=0.5, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.5, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.5, writable=False)
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

    normalCameraX = FloatField(default_value=0.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=0.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=0.0)
    nz = normalCameraZ


class NormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[NormalCameraPlugOperator]
):
    __slots__ = ()

    normalCameraX = FloatField(default_value=0.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=0.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=0.0)
    nz = normalCameraZ


class NormalCameraField(
    Float3CompoundBaseField[NormalCameraAttrOperator, NormalCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalCameraAttrOperator
    PLUG_CLS = NormalCameraPlugOperator

    normalCameraX = FloatField(default_value=0.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=0.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=0.0)
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

    hardwareColorR = FloatField(default_value=0.5)
    hwcr = hardwareColorR

    hardwareColorG = FloatField(default_value=0.5)
    hwcg = hardwareColorG

    hardwareColorB = FloatField(default_value=0.5)
    hwcb = hardwareColorB


class HardwareColorAttrOperator(
    Float3CompoundBaseAttrOperator[HardwareColorPlugOperator]
):
    __slots__ = ()

    hardwareColorR = FloatField(default_value=0.5)
    hwcr = hardwareColorR

    hardwareColorG = FloatField(default_value=0.5)
    hwcg = hardwareColorG

    hardwareColorB = FloatField(default_value=0.5)
    hwcb = hardwareColorB


class HardwareColorField(
    Float3CompoundBaseField[
        HardwareColorAttrOperator, HardwareColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = HardwareColorAttrOperator
    PLUG_CLS = HardwareColorPlugOperator

    hardwareColorR = FloatField(default_value=0.5)
    hwcr = hardwareColorR

    hardwareColorG = FloatField(default_value=0.5)
    hwcg = hardwareColorG

    hardwareColorB = FloatField(default_value=0.5)
    hwcb = hardwareColorB


class CameraPlugOperator(Float3CompoundBasePlugOperator["CameraAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cameraR", "camerar"),
        ("cameraG", "camerag"),
        ("cameraB", "camerab"),
    )

    cameraR = FloatField(default_value=0.0)
    camerar = cameraR

    cameraG = FloatField(default_value=0.0)
    camerag = cameraG

    cameraB = FloatField(default_value=0.0)
    camerab = cameraB


class CameraAttrOperator(Float3CompoundBaseAttrOperator[CameraPlugOperator]):
    __slots__ = ()

    cameraR = FloatField(default_value=0.0)
    camerar = cameraR

    cameraG = FloatField(default_value=0.0)
    camerag = cameraG

    cameraB = FloatField(default_value=0.0)
    camerab = cameraB


class CameraField(
    Float3CompoundBaseField[CameraAttrOperator, CameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CameraAttrOperator
    PLUG_CLS = CameraPlugOperator

    cameraR = FloatField(default_value=0.0)
    camerar = cameraR

    cameraG = FloatField(default_value=0.0)
    camerag = cameraG

    cameraB = FloatField(default_value=0.0)
    camerab = cameraB


class ShadowPlugOperator(Float3CompoundBasePlugOperator["ShadowAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shadowR", "shadowr"),
        ("shadowG", "shadowg"),
        ("shadowB", "shadowb"),
    )

    shadowR = FloatField(default_value=0.0)
    shadowr = shadowR

    shadowG = FloatField(default_value=0.0)
    shadowg = shadowG

    shadowB = FloatField(default_value=0.0)
    shadowb = shadowB


class ShadowAttrOperator(Float3CompoundBaseAttrOperator[ShadowPlugOperator]):
    __slots__ = ()

    shadowR = FloatField(default_value=0.0)
    shadowr = shadowR

    shadowG = FloatField(default_value=0.0)
    shadowg = shadowG

    shadowB = FloatField(default_value=0.0)
    shadowb = shadowB


class ShadowField(
    Float3CompoundBaseField[ShadowAttrOperator, ShadowPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShadowAttrOperator
    PLUG_CLS = ShadowPlugOperator

    shadowR = FloatField(default_value=0.0)
    shadowr = shadowR

    shadowG = FloatField(default_value=0.0)
    shadowg = shadowG

    shadowB = FloatField(default_value=0.0)
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

    diffuseReflectionR = FloatField(default_value=0.0)
    diffuse_reflectionr = diffuseReflectionR

    diffuseReflectionG = FloatField(default_value=0.0)
    diffuse_reflectiong = diffuseReflectionG

    diffuseReflectionB = FloatField(default_value=0.0)
    diffuse_reflectionb = diffuseReflectionB


class DiffuseReflectionAttrOperator(
    Float3CompoundBaseAttrOperator[DiffuseReflectionPlugOperator]
):
    __slots__ = ()

    diffuseReflectionR = FloatField(default_value=0.0)
    diffuse_reflectionr = diffuseReflectionR

    diffuseReflectionG = FloatField(default_value=0.0)
    diffuse_reflectiong = diffuseReflectionG

    diffuseReflectionB = FloatField(default_value=0.0)
    diffuse_reflectionb = diffuseReflectionB


class DiffuseReflectionField(
    Float3CompoundBaseField[
        DiffuseReflectionAttrOperator, DiffuseReflectionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DiffuseReflectionAttrOperator
    PLUG_CLS = DiffuseReflectionPlugOperator

    diffuseReflectionR = FloatField(default_value=0.0)
    diffuse_reflectionr = diffuseReflectionR

    diffuseReflectionG = FloatField(default_value=0.0)
    diffuse_reflectiong = diffuseReflectionG

    diffuseReflectionB = FloatField(default_value=0.0)
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

    diffuseTransmissionR = FloatField(default_value=0.0)
    diffuse_transmissionr = diffuseTransmissionR

    diffuseTransmissionG = FloatField(default_value=0.0)
    diffuse_transmissiong = diffuseTransmissionG

    diffuseTransmissionB = FloatField(default_value=0.0)
    diffuse_transmissionb = diffuseTransmissionB


class DiffuseTransmissionAttrOperator(
    Float3CompoundBaseAttrOperator[DiffuseTransmissionPlugOperator]
):
    __slots__ = ()

    diffuseTransmissionR = FloatField(default_value=0.0)
    diffuse_transmissionr = diffuseTransmissionR

    diffuseTransmissionG = FloatField(default_value=0.0)
    diffuse_transmissiong = diffuseTransmissionG

    diffuseTransmissionB = FloatField(default_value=0.0)
    diffuse_transmissionb = diffuseTransmissionB


class DiffuseTransmissionField(
    Float3CompoundBaseField[
        DiffuseTransmissionAttrOperator, DiffuseTransmissionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DiffuseTransmissionAttrOperator
    PLUG_CLS = DiffuseTransmissionPlugOperator

    diffuseTransmissionR = FloatField(default_value=0.0)
    diffuse_transmissionr = diffuseTransmissionR

    diffuseTransmissionG = FloatField(default_value=0.0)
    diffuse_transmissiong = diffuseTransmissionG

    diffuseTransmissionB = FloatField(default_value=0.0)
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

    specularReflectionR = FloatField(default_value=0.0)
    specular_reflectionr = specularReflectionR

    specularReflectionG = FloatField(default_value=0.0)
    specular_reflectiong = specularReflectionG

    specularReflectionB = FloatField(default_value=0.0)
    specular_reflectionb = specularReflectionB


class SpecularReflectionAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularReflectionPlugOperator]
):
    __slots__ = ()

    specularReflectionR = FloatField(default_value=0.0)
    specular_reflectionr = specularReflectionR

    specularReflectionG = FloatField(default_value=0.0)
    specular_reflectiong = specularReflectionG

    specularReflectionB = FloatField(default_value=0.0)
    specular_reflectionb = specularReflectionB


class SpecularReflectionField(
    Float3CompoundBaseField[
        SpecularReflectionAttrOperator, SpecularReflectionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SpecularReflectionAttrOperator
    PLUG_CLS = SpecularReflectionPlugOperator

    specularReflectionR = FloatField(default_value=0.0)
    specular_reflectionr = specularReflectionR

    specularReflectionG = FloatField(default_value=0.0)
    specular_reflectiong = specularReflectionG

    specularReflectionB = FloatField(default_value=0.0)
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

    specularTransmissionR = FloatField(default_value=0.0)
    specular_transmissionr = specularTransmissionR

    specularTransmissionG = FloatField(default_value=0.0)
    specular_transmissiong = specularTransmissionG

    specularTransmissionB = FloatField(default_value=0.0)
    specular_transmissionb = specularTransmissionB


class SpecularTransmissionAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularTransmissionPlugOperator]
):
    __slots__ = ()

    specularTransmissionR = FloatField(default_value=0.0)
    specular_transmissionr = specularTransmissionR

    specularTransmissionG = FloatField(default_value=0.0)
    specular_transmissiong = specularTransmissionG

    specularTransmissionB = FloatField(default_value=0.0)
    specular_transmissionb = specularTransmissionB


class SpecularTransmissionField(
    Float3CompoundBaseField[
        SpecularTransmissionAttrOperator, SpecularTransmissionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SpecularTransmissionAttrOperator
    PLUG_CLS = SpecularTransmissionPlugOperator

    specularTransmissionR = FloatField(default_value=0.0)
    specular_transmissionr = specularTransmissionR

    specularTransmissionG = FloatField(default_value=0.0)
    specular_transmissiong = specularTransmissionG

    specularTransmissionB = FloatField(default_value=0.0)
    specular_transmissionb = specularTransmissionB


class VolumePlugOperator(Float3CompoundBasePlugOperator["VolumeAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("volumeR", "volumer"),
        ("volumeG", "volumeg"),
        ("volumeB", "volumeb"),
    )

    volumeR = FloatField(default_value=0.0)
    volumer = volumeR

    volumeG = FloatField(default_value=0.0)
    volumeg = volumeG

    volumeB = FloatField(default_value=0.0)
    volumeb = volumeB


class VolumeAttrOperator(Float3CompoundBaseAttrOperator[VolumePlugOperator]):
    __slots__ = ()

    volumeR = FloatField(default_value=0.0)
    volumer = volumeR

    volumeG = FloatField(default_value=0.0)
    volumeg = volumeG

    volumeB = FloatField(default_value=0.0)
    volumeb = volumeB


class VolumeField(
    Float3CompoundBaseField[VolumeAttrOperator, VolumePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VolumeAttrOperator
    PLUG_CLS = VolumePlugOperator

    volumeR = FloatField(default_value=0.0)
    volumer = volumeR

    volumeG = FloatField(default_value=0.0)
    volumeg = volumeG

    volumeB = FloatField(default_value=0.0)
    volumeb = volumeB
