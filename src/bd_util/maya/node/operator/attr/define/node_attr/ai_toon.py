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


class MaskColorPlugOperator(
    Float3CompoundBasePlugOperator["MaskColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maskColorR", "mask_colorr"),
        ("maskColorG", "mask_colorg"),
        ("maskColorB", "mask_colorb"),
    )

    maskColorR = FloatField()
    mask_colorr = maskColorR

    maskColorG = FloatField()
    mask_colorg = maskColorG

    maskColorB = FloatField()
    mask_colorb = maskColorB


class MaskColorAttrOperator(
    Float3CompoundBaseAttrOperator[MaskColorPlugOperator]
):
    __slots__ = ()

    maskColorR = FloatField()
    mask_colorr = maskColorR

    maskColorG = FloatField()
    mask_colorg = maskColorG

    maskColorB = FloatField()
    mask_colorb = maskColorB


class MaskColorField(
    Float3CompoundBaseField[MaskColorAttrOperator, MaskColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaskColorAttrOperator
    PLUG_CLS = MaskColorPlugOperator

    maskColorR = FloatField()
    mask_colorr = maskColorR

    maskColorG = FloatField()
    mask_colorg = maskColorG

    maskColorB = FloatField()
    mask_colorb = maskColorB


class EdgeColorPlugOperator(
    Float3CompoundBasePlugOperator["EdgeColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("edgeColorR", "edge_colorr"),
        ("edgeColorG", "edge_colorg"),
        ("edgeColorB", "edge_colorb"),
    )

    edgeColorR = FloatField()
    edge_colorr = edgeColorR

    edgeColorG = FloatField()
    edge_colorg = edgeColorG

    edgeColorB = FloatField()
    edge_colorb = edgeColorB


class EdgeColorAttrOperator(
    Float3CompoundBaseAttrOperator[EdgeColorPlugOperator]
):
    __slots__ = ()

    edgeColorR = FloatField()
    edge_colorr = edgeColorR

    edgeColorG = FloatField()
    edge_colorg = edgeColorG

    edgeColorB = FloatField()
    edge_colorb = edgeColorB


class EdgeColorField(
    Float3CompoundBaseField[EdgeColorAttrOperator, EdgeColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EdgeColorAttrOperator
    PLUG_CLS = EdgeColorPlugOperator

    edgeColorR = FloatField()
    edge_colorr = edgeColorR

    edgeColorG = FloatField()
    edge_colorg = edgeColorG

    edgeColorB = FloatField()
    edge_colorb = edgeColorB


class EdgeTonemapPlugOperator(
    Float3CompoundBasePlugOperator["EdgeTonemapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("edgeTonemapR", "edge_tonemapr"),
        ("edgeTonemapG", "edge_tonemapg"),
        ("edgeTonemapB", "edge_tonemapb"),
    )

    edgeTonemapR = FloatField()
    edge_tonemapr = edgeTonemapR

    edgeTonemapG = FloatField()
    edge_tonemapg = edgeTonemapG

    edgeTonemapB = FloatField()
    edge_tonemapb = edgeTonemapB


class EdgeTonemapAttrOperator(
    Float3CompoundBaseAttrOperator[EdgeTonemapPlugOperator]
):
    __slots__ = ()

    edgeTonemapR = FloatField()
    edge_tonemapr = edgeTonemapR

    edgeTonemapG = FloatField()
    edge_tonemapg = edgeTonemapG

    edgeTonemapB = FloatField()
    edge_tonemapb = edgeTonemapB


class EdgeTonemapField(
    Float3CompoundBaseField[EdgeTonemapAttrOperator, EdgeTonemapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EdgeTonemapAttrOperator
    PLUG_CLS = EdgeTonemapPlugOperator

    edgeTonemapR = FloatField()
    edge_tonemapr = edgeTonemapR

    edgeTonemapG = FloatField()
    edge_tonemapg = edgeTonemapG

    edgeTonemapB = FloatField()
    edge_tonemapb = edgeTonemapB


class SilhouetteColorPlugOperator(
    Float3CompoundBasePlugOperator["SilhouetteColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("silhouetteColorR", "silhouette_colorr"),
        ("silhouetteColorG", "silhouette_colorg"),
        ("silhouetteColorB", "silhouette_colorb"),
    )

    silhouetteColorR = FloatField()
    silhouette_colorr = silhouetteColorR

    silhouetteColorG = FloatField()
    silhouette_colorg = silhouetteColorG

    silhouetteColorB = FloatField()
    silhouette_colorb = silhouetteColorB


class SilhouetteColorAttrOperator(
    Float3CompoundBaseAttrOperator[SilhouetteColorPlugOperator]
):
    __slots__ = ()

    silhouetteColorR = FloatField()
    silhouette_colorr = silhouetteColorR

    silhouetteColorG = FloatField()
    silhouette_colorg = silhouetteColorG

    silhouetteColorB = FloatField()
    silhouette_colorb = silhouetteColorB


class SilhouetteColorField(
    Float3CompoundBaseField[SilhouetteColorAttrOperator, SilhouetteColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SilhouetteColorAttrOperator
    PLUG_CLS = SilhouetteColorPlugOperator

    silhouetteColorR = FloatField()
    silhouette_colorr = silhouetteColorR

    silhouetteColorG = FloatField()
    silhouette_colorg = silhouetteColorG

    silhouetteColorB = FloatField()
    silhouette_colorb = silhouetteColorB


class SilhouetteTonemapPlugOperator(
    Float3CompoundBasePlugOperator["SilhouetteTonemapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("silhouetteTonemapR", "silhouette_tonemapr"),
        ("silhouetteTonemapG", "silhouette_tonemapg"),
        ("silhouetteTonemapB", "silhouette_tonemapb"),
    )

    silhouetteTonemapR = FloatField()
    silhouette_tonemapr = silhouetteTonemapR

    silhouetteTonemapG = FloatField()
    silhouette_tonemapg = silhouetteTonemapG

    silhouetteTonemapB = FloatField()
    silhouette_tonemapb = silhouetteTonemapB


class SilhouetteTonemapAttrOperator(
    Float3CompoundBaseAttrOperator[SilhouetteTonemapPlugOperator]
):
    __slots__ = ()

    silhouetteTonemapR = FloatField()
    silhouette_tonemapr = silhouetteTonemapR

    silhouetteTonemapG = FloatField()
    silhouette_tonemapg = silhouetteTonemapG

    silhouetteTonemapB = FloatField()
    silhouette_tonemapb = silhouetteTonemapB


class SilhouetteTonemapField(
    Float3CompoundBaseField[SilhouetteTonemapAttrOperator, SilhouetteTonemapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SilhouetteTonemapAttrOperator
    PLUG_CLS = SilhouetteTonemapPlugOperator

    silhouetteTonemapR = FloatField()
    silhouette_tonemapr = silhouetteTonemapR

    silhouetteTonemapG = FloatField()
    silhouette_tonemapg = silhouetteTonemapG

    silhouetteTonemapB = FloatField()
    silhouette_tonemapb = silhouetteTonemapB


class BaseColorPlugOperator(
    Float3CompoundBasePlugOperator["BaseColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("baseColorR", "base_colorr"),
        ("baseColorG", "base_colorg"),
        ("baseColorB", "base_colorb"),
    )

    baseColorR = FloatField()
    base_colorr = baseColorR

    baseColorG = FloatField()
    base_colorg = baseColorG

    baseColorB = FloatField()
    base_colorb = baseColorB


class BaseColorAttrOperator(
    Float3CompoundBaseAttrOperator[BaseColorPlugOperator]
):
    __slots__ = ()

    baseColorR = FloatField()
    base_colorr = baseColorR

    baseColorG = FloatField()
    base_colorg = baseColorG

    baseColorB = FloatField()
    base_colorb = baseColorB


class BaseColorField(
    Float3CompoundBaseField[BaseColorAttrOperator, BaseColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BaseColorAttrOperator
    PLUG_CLS = BaseColorPlugOperator

    baseColorR = FloatField()
    base_colorr = baseColorR

    baseColorG = FloatField()
    base_colorg = baseColorG

    baseColorB = FloatField()
    base_colorb = baseColorB


class BaseTonemapPlugOperator(
    Float3CompoundBasePlugOperator["BaseTonemapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("baseTonemapR", "base_tonemapr"),
        ("baseTonemapG", "base_tonemapg"),
        ("baseTonemapB", "base_tonemapb"),
    )

    baseTonemapR = FloatField()
    base_tonemapr = baseTonemapR

    baseTonemapG = FloatField()
    base_tonemapg = baseTonemapG

    baseTonemapB = FloatField()
    base_tonemapb = baseTonemapB


class BaseTonemapAttrOperator(
    Float3CompoundBaseAttrOperator[BaseTonemapPlugOperator]
):
    __slots__ = ()

    baseTonemapR = FloatField()
    base_tonemapr = baseTonemapR

    baseTonemapG = FloatField()
    base_tonemapg = baseTonemapG

    baseTonemapB = FloatField()
    base_tonemapb = baseTonemapB


class BaseTonemapField(
    Float3CompoundBaseField[BaseTonemapAttrOperator, BaseTonemapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BaseTonemapAttrOperator
    PLUG_CLS = BaseTonemapPlugOperator

    baseTonemapR = FloatField()
    base_tonemapr = baseTonemapR

    baseTonemapG = FloatField()
    base_tonemapg = baseTonemapG

    baseTonemapB = FloatField()
    base_tonemapb = baseTonemapB


class SpecularColorPlugOperator(
    Float3CompoundBasePlugOperator["SpecularColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularColorR", "specular_colorr"),
        ("specularColorG", "specular_colorg"),
        ("specularColorB", "specular_colorb"),
    )

    specularColorR = FloatField()
    specular_colorr = specularColorR

    specularColorG = FloatField()
    specular_colorg = specularColorG

    specularColorB = FloatField()
    specular_colorb = specularColorB


class SpecularColorAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularColorPlugOperator]
):
    __slots__ = ()

    specularColorR = FloatField()
    specular_colorr = specularColorR

    specularColorG = FloatField()
    specular_colorg = specularColorG

    specularColorB = FloatField()
    specular_colorb = specularColorB


class SpecularColorField(
    Float3CompoundBaseField[SpecularColorAttrOperator, SpecularColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularColorAttrOperator
    PLUG_CLS = SpecularColorPlugOperator

    specularColorR = FloatField()
    specular_colorr = specularColorR

    specularColorG = FloatField()
    specular_colorg = specularColorG

    specularColorB = FloatField()
    specular_colorb = specularColorB


class SpecularTonemapPlugOperator(
    Float3CompoundBasePlugOperator["SpecularTonemapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularTonemapR", "specular_tonemapr"),
        ("specularTonemapG", "specular_tonemapg"),
        ("specularTonemapB", "specular_tonemapb"),
    )

    specularTonemapR = FloatField()
    specular_tonemapr = specularTonemapR

    specularTonemapG = FloatField()
    specular_tonemapg = specularTonemapG

    specularTonemapB = FloatField()
    specular_tonemapb = specularTonemapB


class SpecularTonemapAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularTonemapPlugOperator]
):
    __slots__ = ()

    specularTonemapR = FloatField()
    specular_tonemapr = specularTonemapR

    specularTonemapG = FloatField()
    specular_tonemapg = specularTonemapG

    specularTonemapB = FloatField()
    specular_tonemapb = specularTonemapB


class SpecularTonemapField(
    Float3CompoundBaseField[SpecularTonemapAttrOperator, SpecularTonemapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularTonemapAttrOperator
    PLUG_CLS = SpecularTonemapPlugOperator

    specularTonemapR = FloatField()
    specular_tonemapr = specularTonemapR

    specularTonemapG = FloatField()
    specular_tonemapg = specularTonemapG

    specularTonemapB = FloatField()
    specular_tonemapb = specularTonemapB


class HighlightColorPlugOperator(
    Float3CompoundBasePlugOperator["HighlightColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("highlightColorR", "highlight_colorr"),
        ("highlightColorG", "highlight_colorg"),
        ("highlightColorB", "highlight_colorb"),
    )

    highlightColorR = FloatField()
    highlight_colorr = highlightColorR

    highlightColorG = FloatField()
    highlight_colorg = highlightColorG

    highlightColorB = FloatField()
    highlight_colorb = highlightColorB


class HighlightColorAttrOperator(
    Float3CompoundBaseAttrOperator[HighlightColorPlugOperator]
):
    __slots__ = ()

    highlightColorR = FloatField()
    highlight_colorr = highlightColorR

    highlightColorG = FloatField()
    highlight_colorg = highlightColorG

    highlightColorB = FloatField()
    highlight_colorb = highlightColorB


class HighlightColorField(
    Float3CompoundBaseField[HighlightColorAttrOperator, HighlightColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HighlightColorAttrOperator
    PLUG_CLS = HighlightColorPlugOperator

    highlightColorR = FloatField()
    highlight_colorr = highlightColorR

    highlightColorG = FloatField()
    highlight_colorg = highlightColorG

    highlightColorB = FloatField()
    highlight_colorb = highlightColorB


class RimLightColorPlugOperator(
    Float3CompoundBasePlugOperator["RimLightColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rimLightColorR", "rim_light_colorr"),
        ("rimLightColorG", "rim_light_colorg"),
        ("rimLightColorB", "rim_light_colorb"),
    )

    rimLightColorR = FloatField()
    rim_light_colorr = rimLightColorR

    rimLightColorG = FloatField()
    rim_light_colorg = rimLightColorG

    rimLightColorB = FloatField()
    rim_light_colorb = rimLightColorB


class RimLightColorAttrOperator(
    Float3CompoundBaseAttrOperator[RimLightColorPlugOperator]
):
    __slots__ = ()

    rimLightColorR = FloatField()
    rim_light_colorr = rimLightColorR

    rimLightColorG = FloatField()
    rim_light_colorg = rimLightColorG

    rimLightColorB = FloatField()
    rim_light_colorb = rimLightColorB


class RimLightColorField(
    Float3CompoundBaseField[RimLightColorAttrOperator, RimLightColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RimLightColorAttrOperator
    PLUG_CLS = RimLightColorPlugOperator

    rimLightColorR = FloatField()
    rim_light_colorr = rimLightColorR

    rimLightColorG = FloatField()
    rim_light_colorg = rimLightColorG

    rimLightColorB = FloatField()
    rim_light_colorb = rimLightColorB


class TransmissionColorPlugOperator(
    Float3CompoundBasePlugOperator["TransmissionColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transmissionColorR", "transmission_colorr"),
        ("transmissionColorG", "transmission_colorg"),
        ("transmissionColorB", "transmission_colorb"),
    )

    transmissionColorR = FloatField()
    transmission_colorr = transmissionColorR

    transmissionColorG = FloatField()
    transmission_colorg = transmissionColorG

    transmissionColorB = FloatField()
    transmission_colorb = transmissionColorB


class TransmissionColorAttrOperator(
    Float3CompoundBaseAttrOperator[TransmissionColorPlugOperator]
):
    __slots__ = ()

    transmissionColorR = FloatField()
    transmission_colorr = transmissionColorR

    transmissionColorG = FloatField()
    transmission_colorg = transmissionColorG

    transmissionColorB = FloatField()
    transmission_colorb = transmissionColorB


class TransmissionColorField(
    Float3CompoundBaseField[TransmissionColorAttrOperator, TransmissionColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransmissionColorAttrOperator
    PLUG_CLS = TransmissionColorPlugOperator

    transmissionColorR = FloatField()
    transmission_colorr = transmissionColorR

    transmissionColorG = FloatField()
    transmission_colorg = transmissionColorG

    transmissionColorB = FloatField()
    transmission_colorb = transmissionColorB


class SheenColorPlugOperator(
    Float3CompoundBasePlugOperator["SheenColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sheenColorR", "sheen_colorr"),
        ("sheenColorG", "sheen_colorg"),
        ("sheenColorB", "sheen_colorb"),
    )

    sheenColorR = FloatField()
    sheen_colorr = sheenColorR

    sheenColorG = FloatField()
    sheen_colorg = sheenColorG

    sheenColorB = FloatField()
    sheen_colorb = sheenColorB


class SheenColorAttrOperator(
    Float3CompoundBaseAttrOperator[SheenColorPlugOperator]
):
    __slots__ = ()

    sheenColorR = FloatField()
    sheen_colorr = sheenColorR

    sheenColorG = FloatField()
    sheen_colorg = sheenColorG

    sheenColorB = FloatField()
    sheen_colorb = sheenColorB


class SheenColorField(
    Float3CompoundBaseField[SheenColorAttrOperator, SheenColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SheenColorAttrOperator
    PLUG_CLS = SheenColorPlugOperator

    sheenColorR = FloatField()
    sheen_colorr = sheenColorR

    sheenColorG = FloatField()
    sheen_colorg = sheenColorG

    sheenColorB = FloatField()
    sheen_colorb = sheenColorB


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


class TangentPlugOperator(
    Float3CompoundBasePlugOperator["TangentAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tangentX", "tangentx"),
        ("tangentY", "tangenty"),
        ("tangentZ", "tangentz"),
    )

    tangentX = FloatField()
    tangentx = tangentX

    tangentY = FloatField()
    tangenty = tangentY

    tangentZ = FloatField()
    tangentz = tangentZ


class TangentAttrOperator(
    Float3CompoundBaseAttrOperator[TangentPlugOperator]
):
    __slots__ = ()

    tangentX = FloatField()
    tangentx = tangentX

    tangentY = FloatField()
    tangenty = tangentY

    tangentZ = FloatField()
    tangentz = tangentZ


class TangentField(
    Float3CompoundBaseField[TangentAttrOperator, TangentPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentAttrOperator
    PLUG_CLS = TangentPlugOperator

    tangentX = FloatField()
    tangentx = tangentX

    tangentY = FloatField()
    tangenty = tangentY

    tangentZ = FloatField()
    tangentz = tangentZ
