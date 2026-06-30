# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class InputsPlugOperator(
    CompoundPlugOperator["InputsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("color", "c"),
        ("transparency", "t"),
        ("glowColor", "g"),
    )

    color = Float3Field()
    c = color

    transparency = Float3Field()
    t = transparency

    glowColor = Float3Field()
    g = glowColor


class InputsAttrOperator(
    CompoundAttrOperator[InputsPlugOperator]
):
    __slots__ = ()

    color = Float3Field()
    c = color

    transparency = Float3Field()
    t = transparency

    glowColor = Float3Field()
    g = glowColor


class InputsField(
    CompoundField[InputsAttrOperator, InputsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputsAttrOperator
    PLUG_CLS = InputsPlugOperator


class HardwareColorPlugOperator(
    Float3CompoundBasePlugOperator["HardwareColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hardwareColorR", "hcr"),
        ("hardwareColorG", "hcg"),
        ("hardwareColorB", "hcb"),
    )

    hardwareColorR = FloatField()
    hcr = hardwareColorR

    hardwareColorG = FloatField()
    hcg = hardwareColorG

    hardwareColorB = FloatField()
    hcb = hardwareColorB


class HardwareColorAttrOperator(
    Float3CompoundBaseAttrOperator[HardwareColorPlugOperator]
):
    __slots__ = ()

    hardwareColorR = FloatField()
    hcr = hardwareColorR

    hardwareColorG = FloatField()
    hcg = hardwareColorG

    hardwareColorB = FloatField()
    hcb = hardwareColorB


class HardwareColorField(
    Float3CompoundBaseField[HardwareColorAttrOperator, HardwareColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HardwareColorAttrOperator
    PLUG_CLS = HardwareColorPlugOperator

    hardwareColorR = FloatField()
    hcr = hardwareColorR

    hardwareColorG = FloatField()
    hcg = hardwareColorG

    hardwareColorB = FloatField()
    hcb = hardwareColorB


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


class OutGlowColorPlugOperator(
    Float3CompoundBasePlugOperator["OutGlowColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outGlowColorR", "ogr"),
        ("outGlowColorG", "ogg"),
        ("outGlowColorB", "ogb"),
    )

    outGlowColorR = FloatField()
    ogr = outGlowColorR

    outGlowColorG = FloatField()
    ogg = outGlowColorG

    outGlowColorB = FloatField()
    ogb = outGlowColorB


class OutGlowColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutGlowColorPlugOperator]
):
    __slots__ = ()

    outGlowColorR = FloatField()
    ogr = outGlowColorR

    outGlowColorG = FloatField()
    ogg = outGlowColorG

    outGlowColorB = FloatField()
    ogb = outGlowColorB


class OutGlowColorField(
    Float3CompoundBaseField[OutGlowColorAttrOperator, OutGlowColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutGlowColorAttrOperator
    PLUG_CLS = OutGlowColorPlugOperator

    outGlowColorR = FloatField()
    ogr = outGlowColorR

    outGlowColorG = FloatField()
    ogg = outGlowColorG

    outGlowColorB = FloatField()
    ogb = outGlowColorB


class OutMatteOpacityPlugOperator(
    Float3CompoundBasePlugOperator["OutMatteOpacityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outMatteOpacityR", "omor"),
        ("outMatteOpacityG", "omog"),
        ("outMatteOpacityB", "omob"),
    )

    outMatteOpacityR = FloatField()
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField()
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField()
    omob = outMatteOpacityB


class OutMatteOpacityAttrOperator(
    Float3CompoundBaseAttrOperator[OutMatteOpacityPlugOperator]
):
    __slots__ = ()

    outMatteOpacityR = FloatField()
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField()
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField()
    omob = outMatteOpacityB


class OutMatteOpacityField(
    Float3CompoundBaseField[OutMatteOpacityAttrOperator, OutMatteOpacityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutMatteOpacityAttrOperator
    PLUG_CLS = OutMatteOpacityPlugOperator

    outMatteOpacityR = FloatField()
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField()
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField()
    omob = outMatteOpacityB
