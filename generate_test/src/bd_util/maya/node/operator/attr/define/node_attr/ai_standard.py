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


class AiMatteColorPlugOperator(
    Float3CompoundBasePlugOperator["AiMatteColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiMatteColorR", "ai_matte_colorr"),
        ("aiMatteColorG", "ai_matte_colorg"),
        ("aiMatteColorB", "ai_matte_colorb"),
    )

    aiMatteColorR = FloatField()
    ai_matte_colorr = aiMatteColorR

    aiMatteColorG = FloatField()
    ai_matte_colorg = aiMatteColorG

    aiMatteColorB = FloatField()
    ai_matte_colorb = aiMatteColorB


class AiMatteColorAttrOperator(
    Float3CompoundBaseAttrOperator[AiMatteColorPlugOperator]
):
    __slots__ = ()

    aiMatteColorR = FloatField()
    ai_matte_colorr = aiMatteColorR

    aiMatteColorG = FloatField()
    ai_matte_colorg = aiMatteColorG

    aiMatteColorB = FloatField()
    ai_matte_colorb = aiMatteColorB


class AiMatteColorField(
    Float3CompoundBaseField[AiMatteColorAttrOperator, AiMatteColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiMatteColorAttrOperator
    PLUG_CLS = AiMatteColorPlugOperator

    aiMatteColorR = FloatField()
    ai_matte_colorr = aiMatteColorR

    aiMatteColorG = FloatField()
    ai_matte_colorg = aiMatteColorG

    aiMatteColorB = FloatField()
    ai_matte_colorb = aiMatteColorB


class KdColorPlugOperator(
    Float3CompoundBasePlugOperator["KdColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("KdColorR", "Kd_colorr"),
        ("KdColorG", "Kd_colorg"),
        ("KdColorB", "Kd_colorb"),
    )

    KdColorR = FloatField()
    Kd_colorr = KdColorR

    KdColorG = FloatField()
    Kd_colorg = KdColorG

    KdColorB = FloatField()
    Kd_colorb = KdColorB


class KdColorAttrOperator(
    Float3CompoundBaseAttrOperator[KdColorPlugOperator]
):
    __slots__ = ()

    KdColorR = FloatField()
    Kd_colorr = KdColorR

    KdColorG = FloatField()
    Kd_colorg = KdColorG

    KdColorB = FloatField()
    Kd_colorb = KdColorB


class KdColorField(
    Float3CompoundBaseField[KdColorAttrOperator, KdColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KdColorAttrOperator
    PLUG_CLS = KdColorPlugOperator

    KdColorR = FloatField()
    Kd_colorr = KdColorR

    KdColorG = FloatField()
    Kd_colorg = KdColorG

    KdColorB = FloatField()
    Kd_colorb = KdColorB


class KsColorPlugOperator(
    Float3CompoundBasePlugOperator["KsColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("KsColorR", "Ks_colorr"),
        ("KsColorG", "Ks_colorg"),
        ("KsColorB", "Ks_colorb"),
    )

    KsColorR = FloatField()
    Ks_colorr = KsColorR

    KsColorG = FloatField()
    Ks_colorg = KsColorG

    KsColorB = FloatField()
    Ks_colorb = KsColorB


class KsColorAttrOperator(
    Float3CompoundBaseAttrOperator[KsColorPlugOperator]
):
    __slots__ = ()

    KsColorR = FloatField()
    Ks_colorr = KsColorR

    KsColorG = FloatField()
    Ks_colorg = KsColorG

    KsColorB = FloatField()
    Ks_colorb = KsColorB


class KsColorField(
    Float3CompoundBaseField[KsColorAttrOperator, KsColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KsColorAttrOperator
    PLUG_CLS = KsColorPlugOperator

    KsColorR = FloatField()
    Ks_colorr = KsColorR

    KsColorG = FloatField()
    Ks_colorg = KsColorG

    KsColorB = FloatField()
    Ks_colorb = KsColorB


class KrColorPlugOperator(
    Float3CompoundBasePlugOperator["KrColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("KrColorR", "Kr_colorr"),
        ("KrColorG", "Kr_colorg"),
        ("KrColorB", "Kr_colorb"),
    )

    KrColorR = FloatField()
    Kr_colorr = KrColorR

    KrColorG = FloatField()
    Kr_colorg = KrColorG

    KrColorB = FloatField()
    Kr_colorb = KrColorB


class KrColorAttrOperator(
    Float3CompoundBaseAttrOperator[KrColorPlugOperator]
):
    __slots__ = ()

    KrColorR = FloatField()
    Kr_colorr = KrColorR

    KrColorG = FloatField()
    Kr_colorg = KrColorG

    KrColorB = FloatField()
    Kr_colorb = KrColorB


class KrColorField(
    Float3CompoundBaseField[KrColorAttrOperator, KrColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KrColorAttrOperator
    PLUG_CLS = KrColorPlugOperator

    KrColorR = FloatField()
    Kr_colorr = KrColorR

    KrColorG = FloatField()
    Kr_colorg = KrColorG

    KrColorB = FloatField()
    Kr_colorb = KrColorB


class ReflectionExitColorPlugOperator(
    Float3CompoundBasePlugOperator["ReflectionExitColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("reflectionExitColorR", "reflection_exit_colorr"),
        ("reflectionExitColorG", "reflection_exit_colorg"),
        ("reflectionExitColorB", "reflection_exit_colorb"),
    )

    reflectionExitColorR = FloatField()
    reflection_exit_colorr = reflectionExitColorR

    reflectionExitColorG = FloatField()
    reflection_exit_colorg = reflectionExitColorG

    reflectionExitColorB = FloatField()
    reflection_exit_colorb = reflectionExitColorB


class ReflectionExitColorAttrOperator(
    Float3CompoundBaseAttrOperator[ReflectionExitColorPlugOperator]
):
    __slots__ = ()

    reflectionExitColorR = FloatField()
    reflection_exit_colorr = reflectionExitColorR

    reflectionExitColorG = FloatField()
    reflection_exit_colorg = reflectionExitColorG

    reflectionExitColorB = FloatField()
    reflection_exit_colorb = reflectionExitColorB


class ReflectionExitColorField(
    Float3CompoundBaseField[ReflectionExitColorAttrOperator, ReflectionExitColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ReflectionExitColorAttrOperator
    PLUG_CLS = ReflectionExitColorPlugOperator

    reflectionExitColorR = FloatField()
    reflection_exit_colorr = reflectionExitColorR

    reflectionExitColorG = FloatField()
    reflection_exit_colorg = reflectionExitColorG

    reflectionExitColorB = FloatField()
    reflection_exit_colorb = reflectionExitColorB


class KtColorPlugOperator(
    Float3CompoundBasePlugOperator["KtColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("KtColorR", "Kt_colorr"),
        ("KtColorG", "Kt_colorg"),
        ("KtColorB", "Kt_colorb"),
    )

    KtColorR = FloatField()
    Kt_colorr = KtColorR

    KtColorG = FloatField()
    Kt_colorg = KtColorG

    KtColorB = FloatField()
    Kt_colorb = KtColorB


class KtColorAttrOperator(
    Float3CompoundBaseAttrOperator[KtColorPlugOperator]
):
    __slots__ = ()

    KtColorR = FloatField()
    Kt_colorr = KtColorR

    KtColorG = FloatField()
    Kt_colorg = KtColorG

    KtColorB = FloatField()
    Kt_colorb = KtColorB


class KtColorField(
    Float3CompoundBaseField[KtColorAttrOperator, KtColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KtColorAttrOperator
    PLUG_CLS = KtColorPlugOperator

    KtColorR = FloatField()
    Kt_colorr = KtColorR

    KtColorG = FloatField()
    Kt_colorg = KtColorG

    KtColorB = FloatField()
    Kt_colorb = KtColorB


class TransmittancePlugOperator(
    Float3CompoundBasePlugOperator["TransmittanceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transmittanceR", "transmittancer"),
        ("transmittanceG", "transmittanceg"),
        ("transmittanceB", "transmittanceb"),
    )

    transmittanceR = FloatField()
    transmittancer = transmittanceR

    transmittanceG = FloatField()
    transmittanceg = transmittanceG

    transmittanceB = FloatField()
    transmittanceb = transmittanceB


class TransmittanceAttrOperator(
    Float3CompoundBaseAttrOperator[TransmittancePlugOperator]
):
    __slots__ = ()

    transmittanceR = FloatField()
    transmittancer = transmittanceR

    transmittanceG = FloatField()
    transmittanceg = transmittanceG

    transmittanceB = FloatField()
    transmittanceb = transmittanceB


class TransmittanceField(
    Float3CompoundBaseField[TransmittanceAttrOperator, TransmittancePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransmittanceAttrOperator
    PLUG_CLS = TransmittancePlugOperator

    transmittanceR = FloatField()
    transmittancer = transmittanceR

    transmittanceG = FloatField()
    transmittanceg = transmittanceG

    transmittanceB = FloatField()
    transmittanceb = transmittanceB


class RefractionExitColorPlugOperator(
    Float3CompoundBasePlugOperator["RefractionExitColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("refractionExitColorR", "refraction_exit_colorr"),
        ("refractionExitColorG", "refraction_exit_colorg"),
        ("refractionExitColorB", "refraction_exit_colorb"),
    )

    refractionExitColorR = FloatField()
    refraction_exit_colorr = refractionExitColorR

    refractionExitColorG = FloatField()
    refraction_exit_colorg = refractionExitColorG

    refractionExitColorB = FloatField()
    refraction_exit_colorb = refractionExitColorB


class RefractionExitColorAttrOperator(
    Float3CompoundBaseAttrOperator[RefractionExitColorPlugOperator]
):
    __slots__ = ()

    refractionExitColorR = FloatField()
    refraction_exit_colorr = refractionExitColorR

    refractionExitColorG = FloatField()
    refraction_exit_colorg = refractionExitColorG

    refractionExitColorB = FloatField()
    refraction_exit_colorb = refractionExitColorB


class RefractionExitColorField(
    Float3CompoundBaseField[RefractionExitColorAttrOperator, RefractionExitColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RefractionExitColorAttrOperator
    PLUG_CLS = RefractionExitColorPlugOperator

    refractionExitColorR = FloatField()
    refraction_exit_colorr = refractionExitColorR

    refractionExitColorG = FloatField()
    refraction_exit_colorg = refractionExitColorG

    refractionExitColorB = FloatField()
    refraction_exit_colorb = refractionExitColorB


class EmissionColorPlugOperator(
    Float3CompoundBasePlugOperator["EmissionColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("emissionColorR", "emission_colorr"),
        ("emissionColorG", "emission_colorg"),
        ("emissionColorB", "emission_colorb"),
    )

    emissionColorR = FloatField()
    emission_colorr = emissionColorR

    emissionColorG = FloatField()
    emission_colorg = emissionColorG

    emissionColorB = FloatField()
    emission_colorb = emissionColorB


class EmissionColorAttrOperator(
    Float3CompoundBaseAttrOperator[EmissionColorPlugOperator]
):
    __slots__ = ()

    emissionColorR = FloatField()
    emission_colorr = emissionColorR

    emissionColorG = FloatField()
    emission_colorg = emissionColorG

    emissionColorB = FloatField()
    emission_colorb = emissionColorB


class EmissionColorField(
    Float3CompoundBaseField[EmissionColorAttrOperator, EmissionColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmissionColorAttrOperator
    PLUG_CLS = EmissionColorPlugOperator

    emissionColorR = FloatField()
    emission_colorr = emissionColorR

    emissionColorG = FloatField()
    emission_colorg = emissionColorG

    emissionColorB = FloatField()
    emission_colorb = emissionColorB


class KsssColorPlugOperator(
    Float3CompoundBasePlugOperator["KsssColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("KsssColorR", "Ksss_colorr"),
        ("KsssColorG", "Ksss_colorg"),
        ("KsssColorB", "Ksss_colorb"),
    )

    KsssColorR = FloatField()
    Ksss_colorr = KsssColorR

    KsssColorG = FloatField()
    Ksss_colorg = KsssColorG

    KsssColorB = FloatField()
    Ksss_colorb = KsssColorB


class KsssColorAttrOperator(
    Float3CompoundBaseAttrOperator[KsssColorPlugOperator]
):
    __slots__ = ()

    KsssColorR = FloatField()
    Ksss_colorr = KsssColorR

    KsssColorG = FloatField()
    Ksss_colorg = KsssColorG

    KsssColorB = FloatField()
    Ksss_colorb = KsssColorB


class KsssColorField(
    Float3CompoundBaseField[KsssColorAttrOperator, KsssColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KsssColorAttrOperator
    PLUG_CLS = KsssColorPlugOperator

    KsssColorR = FloatField()
    Ksss_colorr = KsssColorR

    KsssColorG = FloatField()
    Ksss_colorg = KsssColorG

    KsssColorB = FloatField()
    Ksss_colorb = KsssColorB


class SssRadiusPlugOperator(
    Float3CompoundBasePlugOperator["SssRadiusAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sssRadiusR", "sss_radiusr"),
        ("sssRadiusG", "sss_radiusg"),
        ("sssRadiusB", "sss_radiusb"),
    )

    sssRadiusR = FloatField()
    sss_radiusr = sssRadiusR

    sssRadiusG = FloatField()
    sss_radiusg = sssRadiusG

    sssRadiusB = FloatField()
    sss_radiusb = sssRadiusB


class SssRadiusAttrOperator(
    Float3CompoundBaseAttrOperator[SssRadiusPlugOperator]
):
    __slots__ = ()

    sssRadiusR = FloatField()
    sss_radiusr = sssRadiusR

    sssRadiusG = FloatField()
    sss_radiusg = sssRadiusG

    sssRadiusB = FloatField()
    sss_radiusb = sssRadiusB


class SssRadiusField(
    Float3CompoundBaseField[SssRadiusAttrOperator, SssRadiusPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SssRadiusAttrOperator
    PLUG_CLS = SssRadiusPlugOperator

    sssRadiusR = FloatField()
    sss_radiusr = sssRadiusR

    sssRadiusG = FloatField()
    sss_radiusg = sssRadiusG

    sssRadiusB = FloatField()
    sss_radiusb = sssRadiusB


class OpacityPlugOperator(
    Float3CompoundBasePlugOperator["OpacityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("opacityR", "opacityr"),
        ("opacityG", "opacityg"),
        ("opacityB", "opacityb"),
    )

    opacityR = FloatField()
    opacityr = opacityR

    opacityG = FloatField()
    opacityg = opacityG

    opacityB = FloatField()
    opacityb = opacityB


class OpacityAttrOperator(
    Float3CompoundBaseAttrOperator[OpacityPlugOperator]
):
    __slots__ = ()

    opacityR = FloatField()
    opacityr = opacityR

    opacityG = FloatField()
    opacityg = opacityG

    opacityB = FloatField()
    opacityb = opacityB


class OpacityField(
    Float3CompoundBaseField[OpacityAttrOperator, OpacityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OpacityAttrOperator
    PLUG_CLS = OpacityPlugOperator

    opacityR = FloatField()
    opacityr = opacityR

    opacityG = FloatField()
    opacityg = opacityG

    opacityB = FloatField()
    opacityb = opacityB


class NormalPlugOperator(
    Float3CompoundBasePlugOperator["NormalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalX", "normalx"),
        ("normalY", "normaly"),
        ("normalZ", "normalz"),
    )

    normalX = FloatField()
    normalx = normalX

    normalY = FloatField()
    normaly = normalY

    normalZ = FloatField()
    normalz = normalZ


class NormalAttrOperator(
    Float3CompoundBaseAttrOperator[NormalPlugOperator]
):
    __slots__ = ()

    normalX = FloatField()
    normalx = normalX

    normalY = FloatField()
    normaly = normalY

    normalZ = FloatField()
    normalz = normalZ


class NormalField(
    Float3CompoundBaseField[NormalAttrOperator, NormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalAttrOperator
    PLUG_CLS = NormalPlugOperator

    normalX = FloatField()
    normalx = normalX

    normalY = FloatField()
    normaly = normalY

    normalZ = FloatField()
    normalz = normalZ
