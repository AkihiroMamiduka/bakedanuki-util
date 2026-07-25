# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class DiffuseColorPlugOperator(
    Float3CompoundBasePlugOperator["DiffuseColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("diffuseColorR", "dcr"),
        ("diffuseColorG", "dcg"),
        ("diffuseColorB", "dcb"),
    )

    diffuseColorR = FloatField(default_value=0.18000000715255737)
    dcr = diffuseColorR

    diffuseColorG = FloatField(default_value=0.18000000715255737)
    dcg = diffuseColorG

    diffuseColorB = FloatField(default_value=0.18000000715255737)
    dcb = diffuseColorB


class DiffuseColorAttrOperator(
    Float3CompoundBaseAttrOperator[DiffuseColorPlugOperator]
):
    __slots__ = ()

    diffuseColorR = FloatField(default_value=0.18000000715255737)
    dcr = diffuseColorR

    diffuseColorG = FloatField(default_value=0.18000000715255737)
    dcg = diffuseColorG

    diffuseColorB = FloatField(default_value=0.18000000715255737)
    dcb = diffuseColorB


class DiffuseColorField(
    Float3CompoundBaseField[DiffuseColorAttrOperator, DiffuseColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DiffuseColorAttrOperator
    PLUG_CLS = DiffuseColorPlugOperator

    diffuseColorR = FloatField(default_value=0.18000000715255737)
    dcr = diffuseColorR

    diffuseColorG = FloatField(default_value=0.18000000715255737)
    dcg = diffuseColorG

    diffuseColorB = FloatField(default_value=0.18000000715255737)
    dcb = diffuseColorB


class EmissiveColorPlugOperator(
    Float3CompoundBasePlugOperator["EmissiveColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("emissiveColorR", "ecr"),
        ("emissiveColorG", "ecg"),
        ("emissiveColorB", "ecb"),
    )

    emissiveColorR = FloatField(default_value=0.0)
    ecr = emissiveColorR

    emissiveColorG = FloatField(default_value=0.0)
    ecg = emissiveColorG

    emissiveColorB = FloatField(default_value=0.0)
    ecb = emissiveColorB


class EmissiveColorAttrOperator(
    Float3CompoundBaseAttrOperator[EmissiveColorPlugOperator]
):
    __slots__ = ()

    emissiveColorR = FloatField(default_value=0.0)
    ecr = emissiveColorR

    emissiveColorG = FloatField(default_value=0.0)
    ecg = emissiveColorG

    emissiveColorB = FloatField(default_value=0.0)
    ecb = emissiveColorB


class EmissiveColorField(
    Float3CompoundBaseField[EmissiveColorAttrOperator, EmissiveColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmissiveColorAttrOperator
    PLUG_CLS = EmissiveColorPlugOperator

    emissiveColorR = FloatField(default_value=0.0)
    ecr = emissiveColorR

    emissiveColorG = FloatField(default_value=0.0)
    ecg = emissiveColorG

    emissiveColorB = FloatField(default_value=0.0)
    ecb = emissiveColorB


class NormalPlugOperator(
    Float3CompoundBasePlugOperator["NormalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normal0", "nrm0"),
        ("normal1", "nrm1"),
        ("normal2", "nrm2"),
    )

    normal0 = FloatField(default_value=0.0)
    nrm0 = normal0

    normal1 = FloatField(default_value=1.0)
    nrm1 = normal1

    normal2 = FloatField(default_value=0.0)
    nrm2 = normal2


class NormalAttrOperator(
    Float3CompoundBaseAttrOperator[NormalPlugOperator]
):
    __slots__ = ()

    normal0 = FloatField(default_value=0.0)
    nrm0 = normal0

    normal1 = FloatField(default_value=1.0)
    nrm1 = normal1

    normal2 = FloatField(default_value=0.0)
    nrm2 = normal2


class NormalField(
    Float3CompoundBaseField[NormalAttrOperator, NormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalAttrOperator
    PLUG_CLS = NormalPlugOperator

    normal0 = FloatField(default_value=0.0)
    nrm0 = normal0

    normal1 = FloatField(default_value=1.0)
    nrm1 = normal1

    normal2 = FloatField(default_value=0.0)
    nrm2 = normal2


class SpecularColorPlugOperator(
    Float3CompoundBasePlugOperator["SpecularColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularColorR", "spcr"),
        ("specularColorG", "spcg"),
        ("specularColorB", "spcb"),
    )

    specularColorR = FloatField(default_value=0.0)
    spcr = specularColorR

    specularColorG = FloatField(default_value=0.0)
    spcg = specularColorG

    specularColorB = FloatField(default_value=0.0)
    spcb = specularColorB


class SpecularColorAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularColorPlugOperator]
):
    __slots__ = ()

    specularColorR = FloatField(default_value=0.0)
    spcr = specularColorR

    specularColorG = FloatField(default_value=0.0)
    spcg = specularColorG

    specularColorB = FloatField(default_value=0.0)
    spcb = specularColorB


class SpecularColorField(
    Float3CompoundBaseField[SpecularColorAttrOperator, SpecularColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularColorAttrOperator
    PLUG_CLS = SpecularColorPlugOperator

    specularColorR = FloatField(default_value=0.0)
    spcr = specularColorR

    specularColorG = FloatField(default_value=0.0)
    spcg = specularColorG

    specularColorB = FloatField(default_value=0.0)
    spcb = specularColorB


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "ocr"),
        ("outColorG", "ocg"),
        ("outColorB", "ocb"),
    )

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
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

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB
