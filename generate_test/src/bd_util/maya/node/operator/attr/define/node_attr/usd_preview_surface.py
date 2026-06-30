# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
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

    diffuseColorR = FloatField()
    dcr = diffuseColorR

    diffuseColorG = FloatField()
    dcg = diffuseColorG

    diffuseColorB = FloatField()
    dcb = diffuseColorB


class DiffuseColorAttrOperator(
    Float3CompoundBaseAttrOperator[DiffuseColorPlugOperator]
):
    __slots__ = ()

    diffuseColorR = FloatField()
    dcr = diffuseColorR

    diffuseColorG = FloatField()
    dcg = diffuseColorG

    diffuseColorB = FloatField()
    dcb = diffuseColorB


class DiffuseColorField(
    Float3CompoundBaseField[DiffuseColorAttrOperator, DiffuseColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DiffuseColorAttrOperator
    PLUG_CLS = DiffuseColorPlugOperator

    diffuseColorR = FloatField()
    dcr = diffuseColorR

    diffuseColorG = FloatField()
    dcg = diffuseColorG

    diffuseColorB = FloatField()
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

    emissiveColorR = FloatField()
    ecr = emissiveColorR

    emissiveColorG = FloatField()
    ecg = emissiveColorG

    emissiveColorB = FloatField()
    ecb = emissiveColorB


class EmissiveColorAttrOperator(
    Float3CompoundBaseAttrOperator[EmissiveColorPlugOperator]
):
    __slots__ = ()

    emissiveColorR = FloatField()
    ecr = emissiveColorR

    emissiveColorG = FloatField()
    ecg = emissiveColorG

    emissiveColorB = FloatField()
    ecb = emissiveColorB


class EmissiveColorField(
    Float3CompoundBaseField[EmissiveColorAttrOperator, EmissiveColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmissiveColorAttrOperator
    PLUG_CLS = EmissiveColorPlugOperator

    emissiveColorR = FloatField()
    ecr = emissiveColorR

    emissiveColorG = FloatField()
    ecg = emissiveColorG

    emissiveColorB = FloatField()
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

    normal0 = FloatField()
    nrm0 = normal0

    normal1 = FloatField()
    nrm1 = normal1

    normal2 = FloatField()
    nrm2 = normal2


class NormalAttrOperator(
    Float3CompoundBaseAttrOperator[NormalPlugOperator]
):
    __slots__ = ()

    normal0 = FloatField()
    nrm0 = normal0

    normal1 = FloatField()
    nrm1 = normal1

    normal2 = FloatField()
    nrm2 = normal2


class NormalField(
    Float3CompoundBaseField[NormalAttrOperator, NormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalAttrOperator
    PLUG_CLS = NormalPlugOperator

    normal0 = FloatField()
    nrm0 = normal0

    normal1 = FloatField()
    nrm1 = normal1

    normal2 = FloatField()
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

    specularColorR = FloatField()
    spcr = specularColorR

    specularColorG = FloatField()
    spcg = specularColorG

    specularColorB = FloatField()
    spcb = specularColorB


class SpecularColorAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularColorPlugOperator]
):
    __slots__ = ()

    specularColorR = FloatField()
    spcr = specularColorR

    specularColorG = FloatField()
    spcg = specularColorG

    specularColorB = FloatField()
    spcb = specularColorB


class SpecularColorField(
    Float3CompoundBaseField[SpecularColorAttrOperator, SpecularColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularColorAttrOperator
    PLUG_CLS = SpecularColorPlugOperator

    specularColorR = FloatField()
    spcr = specularColorR

    specularColorG = FloatField()
    spcg = specularColorG

    specularColorB = FloatField()
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
