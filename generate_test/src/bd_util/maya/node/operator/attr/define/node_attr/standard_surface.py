# coding: utf-8

from ..std.at.addr import AddrField
from ..std.at.light_data import (
    LightDataAttrOperator,
    LightDataPlugOperator,
    LightDataField,
)
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "ocr"),
        ("outColorG", "ocg"),
        ("outColorB", "ocb"),
    )

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


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


class BaseColorPlugOperator(
    Float3CompoundBasePlugOperator["BaseColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("baseColorR", "bcr"),
        ("baseColorG", "bcg"),
        ("baseColorB", "bcb"),
    )

    baseColorR = FloatField()
    bcr = baseColorR

    baseColorG = FloatField()
    bcg = baseColorG

    baseColorB = FloatField()
    bcb = baseColorB


class BaseColorAttrOperator(
    Float3CompoundBaseAttrOperator[BaseColorPlugOperator]
):
    __slots__ = ()

    baseColorR = FloatField()
    bcr = baseColorR

    baseColorG = FloatField()
    bcg = baseColorG

    baseColorB = FloatField()
    bcb = baseColorB


class BaseColorField(
    Float3CompoundBaseField[BaseColorAttrOperator, BaseColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BaseColorAttrOperator
    PLUG_CLS = BaseColorPlugOperator

    baseColorR = FloatField()
    bcr = baseColorR

    baseColorG = FloatField()
    bcg = baseColorG

    baseColorB = FloatField()
    bcb = baseColorB


class SpecularColorPlugOperator(
    Float3CompoundBasePlugOperator["SpecularColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularColorR", "scr"),
        ("specularColorG", "scg"),
        ("specularColorB", "spb"),
    )

    specularColorR = FloatField()
    scr = specularColorR

    specularColorG = FloatField()
    scg = specularColorG

    specularColorB = FloatField()
    spb = specularColorB


class SpecularColorAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularColorPlugOperator]
):
    __slots__ = ()

    specularColorR = FloatField()
    scr = specularColorR

    specularColorG = FloatField()
    scg = specularColorG

    specularColorB = FloatField()
    spb = specularColorB


class SpecularColorField(
    Float3CompoundBaseField[SpecularColorAttrOperator, SpecularColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularColorAttrOperator
    PLUG_CLS = SpecularColorPlugOperator

    specularColorR = FloatField()
    scr = specularColorR

    specularColorG = FloatField()
    scg = specularColorG

    specularColorB = FloatField()
    spb = specularColorB


class TransmissionColorPlugOperator(
    Float3CompoundBasePlugOperator["TransmissionColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transmissionColorR", "trcr"),
        ("transmissionColorG", "trcg"),
        ("transmissionColorB", "trcb"),
    )

    transmissionColorR = FloatField()
    trcr = transmissionColorR

    transmissionColorG = FloatField()
    trcg = transmissionColorG

    transmissionColorB = FloatField()
    trcb = transmissionColorB


class TransmissionColorAttrOperator(
    Float3CompoundBaseAttrOperator[TransmissionColorPlugOperator]
):
    __slots__ = ()

    transmissionColorR = FloatField()
    trcr = transmissionColorR

    transmissionColorG = FloatField()
    trcg = transmissionColorG

    transmissionColorB = FloatField()
    trcb = transmissionColorB


class TransmissionColorField(
    Float3CompoundBaseField[TransmissionColorAttrOperator, TransmissionColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransmissionColorAttrOperator
    PLUG_CLS = TransmissionColorPlugOperator

    transmissionColorR = FloatField()
    trcr = transmissionColorR

    transmissionColorG = FloatField()
    trcg = transmissionColorG

    transmissionColorB = FloatField()
    trcb = transmissionColorB


class TransmissionScatterPlugOperator(
    Float3CompoundBasePlugOperator["TransmissionScatterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transmissionScatterR", "tsr"),
        ("transmissionScatterG", "tsg"),
        ("transmissionScatterB", "tsb"),
    )

    transmissionScatterR = FloatField()
    tsr = transmissionScatterR

    transmissionScatterG = FloatField()
    tsg = transmissionScatterG

    transmissionScatterB = FloatField()
    tsb = transmissionScatterB


class TransmissionScatterAttrOperator(
    Float3CompoundBaseAttrOperator[TransmissionScatterPlugOperator]
):
    __slots__ = ()

    transmissionScatterR = FloatField()
    tsr = transmissionScatterR

    transmissionScatterG = FloatField()
    tsg = transmissionScatterG

    transmissionScatterB = FloatField()
    tsb = transmissionScatterB


class TransmissionScatterField(
    Float3CompoundBaseField[TransmissionScatterAttrOperator, TransmissionScatterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransmissionScatterAttrOperator
    PLUG_CLS = TransmissionScatterPlugOperator

    transmissionScatterR = FloatField()
    tsr = transmissionScatterR

    transmissionScatterG = FloatField()
    tsg = transmissionScatterG

    transmissionScatterB = FloatField()
    tsb = transmissionScatterB


class SubsurfaceColorPlugOperator(
    Float3CompoundBasePlugOperator["SubsurfaceColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("subsurfaceColorR", "subcr"),
        ("subsurfaceColorG", "subcg"),
        ("subsurfaceColorB", "subcb"),
    )

    subsurfaceColorR = FloatField()
    subcr = subsurfaceColorR

    subsurfaceColorG = FloatField()
    subcg = subsurfaceColorG

    subsurfaceColorB = FloatField()
    subcb = subsurfaceColorB


class SubsurfaceColorAttrOperator(
    Float3CompoundBaseAttrOperator[SubsurfaceColorPlugOperator]
):
    __slots__ = ()

    subsurfaceColorR = FloatField()
    subcr = subsurfaceColorR

    subsurfaceColorG = FloatField()
    subcg = subsurfaceColorG

    subsurfaceColorB = FloatField()
    subcb = subsurfaceColorB


class SubsurfaceColorField(
    Float3CompoundBaseField[SubsurfaceColorAttrOperator, SubsurfaceColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SubsurfaceColorAttrOperator
    PLUG_CLS = SubsurfaceColorPlugOperator

    subsurfaceColorR = FloatField()
    subcr = subsurfaceColorR

    subsurfaceColorG = FloatField()
    subcg = subsurfaceColorG

    subsurfaceColorB = FloatField()
    subcb = subsurfaceColorB


class SubsurfaceRadiusPlugOperator(
    Float3CompoundBasePlugOperator["SubsurfaceRadiusAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("subsurfaceRadiusR", "subrr"),
        ("subsurfaceRadiusG", "subrg"),
        ("subsurfaceRadiusB", "subrb"),
    )

    subsurfaceRadiusR = FloatField()
    subrr = subsurfaceRadiusR

    subsurfaceRadiusG = FloatField()
    subrg = subsurfaceRadiusG

    subsurfaceRadiusB = FloatField()
    subrb = subsurfaceRadiusB


class SubsurfaceRadiusAttrOperator(
    Float3CompoundBaseAttrOperator[SubsurfaceRadiusPlugOperator]
):
    __slots__ = ()

    subsurfaceRadiusR = FloatField()
    subrr = subsurfaceRadiusR

    subsurfaceRadiusG = FloatField()
    subrg = subsurfaceRadiusG

    subsurfaceRadiusB = FloatField()
    subrb = subsurfaceRadiusB


class SubsurfaceRadiusField(
    Float3CompoundBaseField[SubsurfaceRadiusAttrOperator, SubsurfaceRadiusPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SubsurfaceRadiusAttrOperator
    PLUG_CLS = SubsurfaceRadiusPlugOperator

    subsurfaceRadiusR = FloatField()
    subrr = subsurfaceRadiusR

    subsurfaceRadiusG = FloatField()
    subrg = subsurfaceRadiusG

    subsurfaceRadiusB = FloatField()
    subrb = subsurfaceRadiusB


class SheenColorPlugOperator(
    Float3CompoundBasePlugOperator["SheenColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sheenColorR", "shcr"),
        ("sheenColorG", "shcg"),
        ("sheenColorB", "shcb"),
    )

    sheenColorR = FloatField()
    shcr = sheenColorR

    sheenColorG = FloatField()
    shcg = sheenColorG

    sheenColorB = FloatField()
    shcb = sheenColorB


class SheenColorAttrOperator(
    Float3CompoundBaseAttrOperator[SheenColorPlugOperator]
):
    __slots__ = ()

    sheenColorR = FloatField()
    shcr = sheenColorR

    sheenColorG = FloatField()
    shcg = sheenColorG

    sheenColorB = FloatField()
    shcb = sheenColorB


class SheenColorField(
    Float3CompoundBaseField[SheenColorAttrOperator, SheenColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SheenColorAttrOperator
    PLUG_CLS = SheenColorPlugOperator

    sheenColorR = FloatField()
    shcr = sheenColorR

    sheenColorG = FloatField()
    shcg = sheenColorG

    sheenColorB = FloatField()
    shcb = sheenColorB


class CoatColorPlugOperator(
    Float3CompoundBasePlugOperator["CoatColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("coatColorR", "ctcr"),
        ("coatColorG", "ctcg"),
        ("coatColorB", "ctcb"),
    )

    coatColorR = FloatField()
    ctcr = coatColorR

    coatColorG = FloatField()
    ctcg = coatColorG

    coatColorB = FloatField()
    ctcb = coatColorB


class CoatColorAttrOperator(
    Float3CompoundBaseAttrOperator[CoatColorPlugOperator]
):
    __slots__ = ()

    coatColorR = FloatField()
    ctcr = coatColorR

    coatColorG = FloatField()
    ctcg = coatColorG

    coatColorB = FloatField()
    ctcb = coatColorB


class CoatColorField(
    Float3CompoundBaseField[CoatColorAttrOperator, CoatColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoatColorAttrOperator
    PLUG_CLS = CoatColorPlugOperator

    coatColorR = FloatField()
    ctcr = coatColorR

    coatColorG = FloatField()
    ctcg = coatColorG

    coatColorB = FloatField()
    ctcb = coatColorB


class CoatNormalPlugOperator(
    Float3CompoundBasePlugOperator["CoatNormalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("coatNormalX", "ctnx"),
        ("coatNormalY", "ctny"),
        ("coatNormalZ", "ctnz"),
    )

    coatNormalX = FloatField()
    ctnx = coatNormalX

    coatNormalY = FloatField()
    ctny = coatNormalY

    coatNormalZ = FloatField()
    ctnz = coatNormalZ


class CoatNormalAttrOperator(
    Float3CompoundBaseAttrOperator[CoatNormalPlugOperator]
):
    __slots__ = ()

    coatNormalX = FloatField()
    ctnx = coatNormalX

    coatNormalY = FloatField()
    ctny = coatNormalY

    coatNormalZ = FloatField()
    ctnz = coatNormalZ


class CoatNormalField(
    Float3CompoundBaseField[CoatNormalAttrOperator, CoatNormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoatNormalAttrOperator
    PLUG_CLS = CoatNormalPlugOperator

    coatNormalX = FloatField()
    ctnx = coatNormalX

    coatNormalY = FloatField()
    ctny = coatNormalY

    coatNormalZ = FloatField()
    ctnz = coatNormalZ


class EmissionColorPlugOperator(
    Float3CompoundBasePlugOperator["EmissionColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("emissionColorR", "ecr"),
        ("emissionColorG", "ecg"),
        ("emissionColorB", "ecb"),
    )

    emissionColorR = FloatField()
    ecr = emissionColorR

    emissionColorG = FloatField()
    ecg = emissionColorG

    emissionColorB = FloatField()
    ecb = emissionColorB


class EmissionColorAttrOperator(
    Float3CompoundBaseAttrOperator[EmissionColorPlugOperator]
):
    __slots__ = ()

    emissionColorR = FloatField()
    ecr = emissionColorR

    emissionColorG = FloatField()
    ecg = emissionColorG

    emissionColorB = FloatField()
    ecb = emissionColorB


class EmissionColorField(
    Float3CompoundBaseField[EmissionColorAttrOperator, EmissionColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmissionColorAttrOperator
    PLUG_CLS = EmissionColorPlugOperator

    emissionColorR = FloatField()
    ecr = emissionColorR

    emissionColorG = FloatField()
    ecg = emissionColorG

    emissionColorB = FloatField()
    ecb = emissionColorB


class OpacityPlugOperator(
    Float3CompoundBasePlugOperator["OpacityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("opacityR", "opr"),
        ("opacityG", "opg"),
        ("opacityB", "opb"),
    )

    opacityR = FloatField()
    opr = opacityR

    opacityG = FloatField()
    opg = opacityG

    opacityB = FloatField()
    opb = opacityB


class OpacityAttrOperator(
    Float3CompoundBaseAttrOperator[OpacityPlugOperator]
):
    __slots__ = ()

    opacityR = FloatField()
    opr = opacityR

    opacityG = FloatField()
    opg = opacityG

    opacityB = FloatField()
    opb = opacityB


class OpacityField(
    Float3CompoundBaseField[OpacityAttrOperator, OpacityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OpacityAttrOperator
    PLUG_CLS = OpacityPlugOperator

    opacityR = FloatField()
    opr = opacityR

    opacityG = FloatField()
    opg = opacityG

    opacityB = FloatField()
    opb = opacityB


class RayDirectionPlugOperator(
    Float3CompoundBasePlugOperator["RayDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rayDirectionX", "rdx"),
        ("rayDirectionY", "rdy"),
        ("rayDirectionZ", "rdz"),
    )

    rayDirectionX = FloatField()
    rdx = rayDirectionX

    rayDirectionY = FloatField()
    rdy = rayDirectionY

    rayDirectionZ = FloatField()
    rdz = rayDirectionZ


class RayDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[RayDirectionPlugOperator]
):
    __slots__ = ()

    rayDirectionX = FloatField()
    rdx = rayDirectionX

    rayDirectionY = FloatField()
    rdy = rayDirectionY

    rayDirectionZ = FloatField()
    rdz = rayDirectionZ


class RayDirectionField(
    Float3CompoundBaseField[RayDirectionAttrOperator, RayDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RayDirectionAttrOperator
    PLUG_CLS = RayDirectionPlugOperator

    rayDirectionX = FloatField()
    rdx = rayDirectionX

    rayDirectionY = FloatField()
    rdy = rayDirectionY

    rayDirectionZ = FloatField()
    rdz = rayDirectionZ


class TriangleNormalCameraPlugOperator(
    Float3CompoundBasePlugOperator["TriangleNormalCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("triangleNormalCameraX", "tnx"),
        ("triangleNormalCameraY", "tny"),
        ("triangleNormalCameraZ", "tnz"),
    )

    triangleNormalCameraX = FloatField()
    tnx = triangleNormalCameraX

    triangleNormalCameraY = FloatField()
    tny = triangleNormalCameraY

    triangleNormalCameraZ = FloatField()
    tnz = triangleNormalCameraZ


class TriangleNormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[TriangleNormalCameraPlugOperator]
):
    __slots__ = ()

    triangleNormalCameraX = FloatField()
    tnx = triangleNormalCameraX

    triangleNormalCameraY = FloatField()
    tny = triangleNormalCameraY

    triangleNormalCameraZ = FloatField()
    tnz = triangleNormalCameraZ


class TriangleNormalCameraField(
    Float3CompoundBaseField[TriangleNormalCameraAttrOperator, TriangleNormalCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TriangleNormalCameraAttrOperator
    PLUG_CLS = TriangleNormalCameraPlugOperator

    triangleNormalCameraX = FloatField()
    tnx = triangleNormalCameraX

    triangleNormalCameraY = FloatField()
    tny = triangleNormalCameraY

    triangleNormalCameraZ = FloatField()
    tnz = triangleNormalCameraZ


class PointCameraPlugOperator(
    Float3CompoundBasePlugOperator["PointCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointCameraX", "px"),
        ("pointCameraY", "py"),
        ("pointCameraZ", "pz"),
    )

    pointCameraX = FloatField()
    px = pointCameraX

    pointCameraY = FloatField()
    py = pointCameraY

    pointCameraZ = FloatField()
    pz = pointCameraZ


class PointCameraAttrOperator(
    Float3CompoundBaseAttrOperator[PointCameraPlugOperator]
):
    __slots__ = ()

    pointCameraX = FloatField()
    px = pointCameraX

    pointCameraY = FloatField()
    py = pointCameraY

    pointCameraZ = FloatField()
    pz = pointCameraZ


class PointCameraField(
    Float3CompoundBaseField[PointCameraAttrOperator, PointCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointCameraAttrOperator
    PLUG_CLS = PointCameraPlugOperator

    pointCameraX = FloatField()
    px = pointCameraX

    pointCameraY = FloatField()
    py = pointCameraY

    pointCameraZ = FloatField()
    pz = pointCameraZ


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


class TangentUCameraPlugOperator(
    Float3CompoundBasePlugOperator["TangentUCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tangentUCameraX", "utnx"),
        ("tangentUCameraY", "utny"),
        ("tangentUCameraZ", "utnz"),
    )

    tangentUCameraX = FloatField()
    utnx = tangentUCameraX

    tangentUCameraY = FloatField()
    utny = tangentUCameraY

    tangentUCameraZ = FloatField()
    utnz = tangentUCameraZ


class TangentUCameraAttrOperator(
    Float3CompoundBaseAttrOperator[TangentUCameraPlugOperator]
):
    __slots__ = ()

    tangentUCameraX = FloatField()
    utnx = tangentUCameraX

    tangentUCameraY = FloatField()
    utny = tangentUCameraY

    tangentUCameraZ = FloatField()
    utnz = tangentUCameraZ


class TangentUCameraField(
    Float3CompoundBaseField[TangentUCameraAttrOperator, TangentUCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentUCameraAttrOperator
    PLUG_CLS = TangentUCameraPlugOperator

    tangentUCameraX = FloatField()
    utnx = tangentUCameraX

    tangentUCameraY = FloatField()
    utny = tangentUCameraY

    tangentUCameraZ = FloatField()
    utnz = tangentUCameraZ


class LightDataArrayPlugOperator(
    LightDataPlugOperator["LightDataArrayAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightDirection", "ld"),
        ("lightIntensity", "li"),
        ("lightAmbient", "la"),
        ("lightDiffuse", "ldf"),
        ("lightSpecular", "ls"),
        ("lightShadowFraction", "lsf"),
        ("preShadowIntensity", "psi"),
        ("lightBlindData", "lbd"),
    )

    lightDirection = Float3Field()
    ld = lightDirection

    lightIntensity = Float3Field()
    li = lightIntensity

    lightAmbient = BoolField()
    la = lightAmbient

    lightDiffuse = BoolField()
    ldf = lightDiffuse

    lightSpecular = BoolField()
    ls = lightSpecular

    lightShadowFraction = FloatField()
    lsf = lightShadowFraction

    preShadowIntensity = FloatField()
    psi = preShadowIntensity

    lightBlindData = AddrField()
    lbd = lightBlindData


class LightDataArrayAttrOperator(
    LightDataAttrOperator[LightDataArrayPlugOperator]
):
    __slots__ = ()

    lightDirection = Float3Field()
    ld = lightDirection

    lightIntensity = Float3Field()
    li = lightIntensity

    lightAmbient = BoolField()
    la = lightAmbient

    lightDiffuse = BoolField()
    ldf = lightDiffuse

    lightSpecular = BoolField()
    ls = lightSpecular

    lightShadowFraction = FloatField()
    lsf = lightShadowFraction

    preShadowIntensity = FloatField()
    psi = preShadowIntensity

    lightBlindData = AddrField()
    lbd = lightBlindData


class LightDataArrayField(
    LightDataField[LightDataArrayAttrOperator, LightDataArrayPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightDataArrayAttrOperator
    PLUG_CLS = LightDataArrayPlugOperator


class HardwareShaderPlugOperator(
    Float3CompoundBasePlugOperator["HardwareShaderAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hardwareShaderR", "hwr"),
        ("hardwareShaderG", "hwg"),
        ("hardwareShaderB", "hwb"),
    )

    hardwareShaderR = FloatField()
    hwr = hardwareShaderR

    hardwareShaderG = FloatField()
    hwg = hardwareShaderG

    hardwareShaderB = FloatField()
    hwb = hardwareShaderB


class HardwareShaderAttrOperator(
    Float3CompoundBaseAttrOperator[HardwareShaderPlugOperator]
):
    __slots__ = ()

    hardwareShaderR = FloatField()
    hwr = hardwareShaderR

    hardwareShaderG = FloatField()
    hwg = hardwareShaderG

    hardwareShaderB = FloatField()
    hwb = hardwareShaderB


class HardwareShaderField(
    Float3CompoundBaseField[HardwareShaderAttrOperator, HardwareShaderPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HardwareShaderAttrOperator
    PLUG_CLS = HardwareShaderPlugOperator

    hardwareShaderR = FloatField()
    hwr = hardwareShaderR

    hardwareShaderG = FloatField()
    hwg = hardwareShaderG

    hardwareShaderB = FloatField()
    hwb = hardwareShaderB


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


class AiId1PlugOperator(
    Float3CompoundBasePlugOperator["AiId1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiId1R", "ai_id1r"),
        ("aiId1G", "ai_id1g"),
        ("aiId1B", "ai_id1b"),
    )

    aiId1R = FloatField()
    ai_id1r = aiId1R

    aiId1G = FloatField()
    ai_id1g = aiId1G

    aiId1B = FloatField()
    ai_id1b = aiId1B


class AiId1AttrOperator(
    Float3CompoundBaseAttrOperator[AiId1PlugOperator]
):
    __slots__ = ()

    aiId1R = FloatField()
    ai_id1r = aiId1R

    aiId1G = FloatField()
    ai_id1g = aiId1G

    aiId1B = FloatField()
    ai_id1b = aiId1B


class AiId1Field(
    Float3CompoundBaseField[AiId1AttrOperator, AiId1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiId1AttrOperator
    PLUG_CLS = AiId1PlugOperator

    aiId1R = FloatField()
    ai_id1r = aiId1R

    aiId1G = FloatField()
    ai_id1g = aiId1G

    aiId1B = FloatField()
    ai_id1b = aiId1B


class AiId2PlugOperator(
    Float3CompoundBasePlugOperator["AiId2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiId2R", "ai_id2r"),
        ("aiId2G", "ai_id2g"),
        ("aiId2B", "ai_id2b"),
    )

    aiId2R = FloatField()
    ai_id2r = aiId2R

    aiId2G = FloatField()
    ai_id2g = aiId2G

    aiId2B = FloatField()
    ai_id2b = aiId2B


class AiId2AttrOperator(
    Float3CompoundBaseAttrOperator[AiId2PlugOperator]
):
    __slots__ = ()

    aiId2R = FloatField()
    ai_id2r = aiId2R

    aiId2G = FloatField()
    ai_id2g = aiId2G

    aiId2B = FloatField()
    ai_id2b = aiId2B


class AiId2Field(
    Float3CompoundBaseField[AiId2AttrOperator, AiId2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiId2AttrOperator
    PLUG_CLS = AiId2PlugOperator

    aiId2R = FloatField()
    ai_id2r = aiId2R

    aiId2G = FloatField()
    ai_id2g = aiId2G

    aiId2B = FloatField()
    ai_id2b = aiId2B


class AiId3PlugOperator(
    Float3CompoundBasePlugOperator["AiId3AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiId3R", "ai_id3r"),
        ("aiId3G", "ai_id3g"),
        ("aiId3B", "ai_id3b"),
    )

    aiId3R = FloatField()
    ai_id3r = aiId3R

    aiId3G = FloatField()
    ai_id3g = aiId3G

    aiId3B = FloatField()
    ai_id3b = aiId3B


class AiId3AttrOperator(
    Float3CompoundBaseAttrOperator[AiId3PlugOperator]
):
    __slots__ = ()

    aiId3R = FloatField()
    ai_id3r = aiId3R

    aiId3G = FloatField()
    ai_id3g = aiId3G

    aiId3B = FloatField()
    ai_id3b = aiId3B


class AiId3Field(
    Float3CompoundBaseField[AiId3AttrOperator, AiId3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiId3AttrOperator
    PLUG_CLS = AiId3PlugOperator

    aiId3R = FloatField()
    ai_id3r = aiId3R

    aiId3G = FloatField()
    ai_id3g = aiId3G

    aiId3B = FloatField()
    ai_id3b = aiId3B


class AiId4PlugOperator(
    Float3CompoundBasePlugOperator["AiId4AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiId4R", "ai_id4r"),
        ("aiId4G", "ai_id4g"),
        ("aiId4B", "ai_id4b"),
    )

    aiId4R = FloatField()
    ai_id4r = aiId4R

    aiId4G = FloatField()
    ai_id4g = aiId4G

    aiId4B = FloatField()
    ai_id4b = aiId4B


class AiId4AttrOperator(
    Float3CompoundBaseAttrOperator[AiId4PlugOperator]
):
    __slots__ = ()

    aiId4R = FloatField()
    ai_id4r = aiId4R

    aiId4G = FloatField()
    ai_id4g = aiId4G

    aiId4B = FloatField()
    ai_id4b = aiId4B


class AiId4Field(
    Float3CompoundBaseField[AiId4AttrOperator, AiId4PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiId4AttrOperator
    PLUG_CLS = AiId4PlugOperator

    aiId4R = FloatField()
    ai_id4r = aiId4R

    aiId4G = FloatField()
    ai_id4g = aiId4G

    aiId4B = FloatField()
    ai_id4b = aiId4B


class AiId5PlugOperator(
    Float3CompoundBasePlugOperator["AiId5AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiId5R", "ai_id5r"),
        ("aiId5G", "ai_id5g"),
        ("aiId5B", "ai_id5b"),
    )

    aiId5R = FloatField()
    ai_id5r = aiId5R

    aiId5G = FloatField()
    ai_id5g = aiId5G

    aiId5B = FloatField()
    ai_id5b = aiId5B


class AiId5AttrOperator(
    Float3CompoundBaseAttrOperator[AiId5PlugOperator]
):
    __slots__ = ()

    aiId5R = FloatField()
    ai_id5r = aiId5R

    aiId5G = FloatField()
    ai_id5g = aiId5G

    aiId5B = FloatField()
    ai_id5b = aiId5B


class AiId5Field(
    Float3CompoundBaseField[AiId5AttrOperator, AiId5PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiId5AttrOperator
    PLUG_CLS = AiId5PlugOperator

    aiId5R = FloatField()
    ai_id5r = aiId5R

    aiId5G = FloatField()
    ai_id5g = aiId5G

    aiId5B = FloatField()
    ai_id5b = aiId5B


class AiId6PlugOperator(
    Float3CompoundBasePlugOperator["AiId6AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiId6R", "ai_id6r"),
        ("aiId6G", "ai_id6g"),
        ("aiId6B", "ai_id6b"),
    )

    aiId6R = FloatField()
    ai_id6r = aiId6R

    aiId6G = FloatField()
    ai_id6g = aiId6G

    aiId6B = FloatField()
    ai_id6b = aiId6B


class AiId6AttrOperator(
    Float3CompoundBaseAttrOperator[AiId6PlugOperator]
):
    __slots__ = ()

    aiId6R = FloatField()
    ai_id6r = aiId6R

    aiId6G = FloatField()
    ai_id6g = aiId6G

    aiId6B = FloatField()
    ai_id6b = aiId6B


class AiId6Field(
    Float3CompoundBaseField[AiId6AttrOperator, AiId6PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiId6AttrOperator
    PLUG_CLS = AiId6PlugOperator

    aiId6R = FloatField()
    ai_id6r = aiId6R

    aiId6G = FloatField()
    ai_id6g = aiId6G

    aiId6B = FloatField()
    ai_id6b = aiId6B


class AiId7PlugOperator(
    Float3CompoundBasePlugOperator["AiId7AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiId7R", "ai_id7r"),
        ("aiId7G", "ai_id7g"),
        ("aiId7B", "ai_id7b"),
    )

    aiId7R = FloatField()
    ai_id7r = aiId7R

    aiId7G = FloatField()
    ai_id7g = aiId7G

    aiId7B = FloatField()
    ai_id7b = aiId7B


class AiId7AttrOperator(
    Float3CompoundBaseAttrOperator[AiId7PlugOperator]
):
    __slots__ = ()

    aiId7R = FloatField()
    ai_id7r = aiId7R

    aiId7G = FloatField()
    ai_id7g = aiId7G

    aiId7B = FloatField()
    ai_id7b = aiId7B


class AiId7Field(
    Float3CompoundBaseField[AiId7AttrOperator, AiId7PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiId7AttrOperator
    PLUG_CLS = AiId7PlugOperator

    aiId7R = FloatField()
    ai_id7r = aiId7R

    aiId7G = FloatField()
    ai_id7g = aiId7G

    aiId7B = FloatField()
    ai_id7b = aiId7B


class AiId8PlugOperator(
    Float3CompoundBasePlugOperator["AiId8AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiId8R", "ai_id8r"),
        ("aiId8G", "ai_id8g"),
        ("aiId8B", "ai_id8b"),
    )

    aiId8R = FloatField()
    ai_id8r = aiId8R

    aiId8G = FloatField()
    ai_id8g = aiId8G

    aiId8B = FloatField()
    ai_id8b = aiId8B


class AiId8AttrOperator(
    Float3CompoundBaseAttrOperator[AiId8PlugOperator]
):
    __slots__ = ()

    aiId8R = FloatField()
    ai_id8r = aiId8R

    aiId8G = FloatField()
    ai_id8g = aiId8G

    aiId8B = FloatField()
    ai_id8b = aiId8B


class AiId8Field(
    Float3CompoundBaseField[AiId8AttrOperator, AiId8PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiId8AttrOperator
    PLUG_CLS = AiId8PlugOperator

    aiId8R = FloatField()
    ai_id8r = aiId8R

    aiId8G = FloatField()
    ai_id8g = aiId8G

    aiId8B = FloatField()
    ai_id8b = aiId8B
