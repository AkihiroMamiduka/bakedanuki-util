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


class PassthroughPlugOperator(
    Float3CompoundBasePlugOperator["PassthroughAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("passthroughR", "passthroughr"),
        ("passthroughG", "passthroughg"),
        ("passthroughB", "passthroughb"),
    )

    passthroughR = FloatField()
    passthroughr = passthroughR

    passthroughG = FloatField()
    passthroughg = passthroughG

    passthroughB = FloatField()
    passthroughb = passthroughB


class PassthroughAttrOperator(
    Float3CompoundBaseAttrOperator[PassthroughPlugOperator]
):
    __slots__ = ()

    passthroughR = FloatField()
    passthroughr = passthroughR

    passthroughG = FloatField()
    passthroughg = passthroughG

    passthroughB = FloatField()
    passthroughb = passthroughB


class PassthroughField(
    Float3CompoundBaseField[PassthroughAttrOperator, PassthroughPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PassthroughAttrOperator
    PLUG_CLS = PassthroughPlugOperator

    passthroughR = FloatField()
    passthroughr = passthroughR

    passthroughG = FloatField()
    passthroughg = passthroughG

    passthroughB = FloatField()
    passthroughb = passthroughB


class Eval1PlugOperator(
    Float3CompoundBasePlugOperator["Eval1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval1R", "eval1r"),
        ("eval1G", "eval1g"),
        ("eval1B", "eval1b"),
    )

    eval1R = FloatField()
    eval1r = eval1R

    eval1G = FloatField()
    eval1g = eval1G

    eval1B = FloatField()
    eval1b = eval1B


class Eval1AttrOperator(
    Float3CompoundBaseAttrOperator[Eval1PlugOperator]
):
    __slots__ = ()

    eval1R = FloatField()
    eval1r = eval1R

    eval1G = FloatField()
    eval1g = eval1G

    eval1B = FloatField()
    eval1b = eval1B


class Eval1Field(
    Float3CompoundBaseField[Eval1AttrOperator, Eval1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval1AttrOperator
    PLUG_CLS = Eval1PlugOperator

    eval1R = FloatField()
    eval1r = eval1R

    eval1G = FloatField()
    eval1g = eval1G

    eval1B = FloatField()
    eval1b = eval1B


class Eval2PlugOperator(
    Float3CompoundBasePlugOperator["Eval2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval2R", "eval2r"),
        ("eval2G", "eval2g"),
        ("eval2B", "eval2b"),
    )

    eval2R = FloatField()
    eval2r = eval2R

    eval2G = FloatField()
    eval2g = eval2G

    eval2B = FloatField()
    eval2b = eval2B


class Eval2AttrOperator(
    Float3CompoundBaseAttrOperator[Eval2PlugOperator]
):
    __slots__ = ()

    eval2R = FloatField()
    eval2r = eval2R

    eval2G = FloatField()
    eval2g = eval2G

    eval2B = FloatField()
    eval2b = eval2B


class Eval2Field(
    Float3CompoundBaseField[Eval2AttrOperator, Eval2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval2AttrOperator
    PLUG_CLS = Eval2PlugOperator

    eval2R = FloatField()
    eval2r = eval2R

    eval2G = FloatField()
    eval2g = eval2G

    eval2B = FloatField()
    eval2b = eval2B


class Eval3PlugOperator(
    Float3CompoundBasePlugOperator["Eval3AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval3R", "eval3r"),
        ("eval3G", "eval3g"),
        ("eval3B", "eval3b"),
    )

    eval3R = FloatField()
    eval3r = eval3R

    eval3G = FloatField()
    eval3g = eval3G

    eval3B = FloatField()
    eval3b = eval3B


class Eval3AttrOperator(
    Float3CompoundBaseAttrOperator[Eval3PlugOperator]
):
    __slots__ = ()

    eval3R = FloatField()
    eval3r = eval3R

    eval3G = FloatField()
    eval3g = eval3G

    eval3B = FloatField()
    eval3b = eval3B


class Eval3Field(
    Float3CompoundBaseField[Eval3AttrOperator, Eval3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval3AttrOperator
    PLUG_CLS = Eval3PlugOperator

    eval3R = FloatField()
    eval3r = eval3R

    eval3G = FloatField()
    eval3g = eval3G

    eval3B = FloatField()
    eval3b = eval3B


class Eval4PlugOperator(
    Float3CompoundBasePlugOperator["Eval4AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval4R", "eval4r"),
        ("eval4G", "eval4g"),
        ("eval4B", "eval4b"),
    )

    eval4R = FloatField()
    eval4r = eval4R

    eval4G = FloatField()
    eval4g = eval4G

    eval4B = FloatField()
    eval4b = eval4B


class Eval4AttrOperator(
    Float3CompoundBaseAttrOperator[Eval4PlugOperator]
):
    __slots__ = ()

    eval4R = FloatField()
    eval4r = eval4R

    eval4G = FloatField()
    eval4g = eval4G

    eval4B = FloatField()
    eval4b = eval4B


class Eval4Field(
    Float3CompoundBaseField[Eval4AttrOperator, Eval4PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval4AttrOperator
    PLUG_CLS = Eval4PlugOperator

    eval4R = FloatField()
    eval4r = eval4R

    eval4G = FloatField()
    eval4g = eval4G

    eval4B = FloatField()
    eval4b = eval4B


class Eval5PlugOperator(
    Float3CompoundBasePlugOperator["Eval5AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval5R", "eval5r"),
        ("eval5G", "eval5g"),
        ("eval5B", "eval5b"),
    )

    eval5R = FloatField()
    eval5r = eval5R

    eval5G = FloatField()
    eval5g = eval5G

    eval5B = FloatField()
    eval5b = eval5B


class Eval5AttrOperator(
    Float3CompoundBaseAttrOperator[Eval5PlugOperator]
):
    __slots__ = ()

    eval5R = FloatField()
    eval5r = eval5R

    eval5G = FloatField()
    eval5g = eval5G

    eval5B = FloatField()
    eval5b = eval5B


class Eval5Field(
    Float3CompoundBaseField[Eval5AttrOperator, Eval5PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval5AttrOperator
    PLUG_CLS = Eval5PlugOperator

    eval5R = FloatField()
    eval5r = eval5R

    eval5G = FloatField()
    eval5g = eval5G

    eval5B = FloatField()
    eval5b = eval5B


class Eval6PlugOperator(
    Float3CompoundBasePlugOperator["Eval6AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval6R", "eval6r"),
        ("eval6G", "eval6g"),
        ("eval6B", "eval6b"),
    )

    eval6R = FloatField()
    eval6r = eval6R

    eval6G = FloatField()
    eval6g = eval6G

    eval6B = FloatField()
    eval6b = eval6B


class Eval6AttrOperator(
    Float3CompoundBaseAttrOperator[Eval6PlugOperator]
):
    __slots__ = ()

    eval6R = FloatField()
    eval6r = eval6R

    eval6G = FloatField()
    eval6g = eval6G

    eval6B = FloatField()
    eval6b = eval6B


class Eval6Field(
    Float3CompoundBaseField[Eval6AttrOperator, Eval6PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval6AttrOperator
    PLUG_CLS = Eval6PlugOperator

    eval6R = FloatField()
    eval6r = eval6R

    eval6G = FloatField()
    eval6g = eval6G

    eval6B = FloatField()
    eval6b = eval6B


class Eval7PlugOperator(
    Float3CompoundBasePlugOperator["Eval7AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval7R", "eval7r"),
        ("eval7G", "eval7g"),
        ("eval7B", "eval7b"),
    )

    eval7R = FloatField()
    eval7r = eval7R

    eval7G = FloatField()
    eval7g = eval7G

    eval7B = FloatField()
    eval7b = eval7B


class Eval7AttrOperator(
    Float3CompoundBaseAttrOperator[Eval7PlugOperator]
):
    __slots__ = ()

    eval7R = FloatField()
    eval7r = eval7R

    eval7G = FloatField()
    eval7g = eval7G

    eval7B = FloatField()
    eval7b = eval7B


class Eval7Field(
    Float3CompoundBaseField[Eval7AttrOperator, Eval7PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval7AttrOperator
    PLUG_CLS = Eval7PlugOperator

    eval7R = FloatField()
    eval7r = eval7R

    eval7G = FloatField()
    eval7g = eval7G

    eval7B = FloatField()
    eval7b = eval7B


class Eval8PlugOperator(
    Float3CompoundBasePlugOperator["Eval8AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval8R", "eval8r"),
        ("eval8G", "eval8g"),
        ("eval8B", "eval8b"),
    )

    eval8R = FloatField()
    eval8r = eval8R

    eval8G = FloatField()
    eval8g = eval8G

    eval8B = FloatField()
    eval8b = eval8B


class Eval8AttrOperator(
    Float3CompoundBaseAttrOperator[Eval8PlugOperator]
):
    __slots__ = ()

    eval8R = FloatField()
    eval8r = eval8R

    eval8G = FloatField()
    eval8g = eval8G

    eval8B = FloatField()
    eval8b = eval8B


class Eval8Field(
    Float3CompoundBaseField[Eval8AttrOperator, Eval8PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval8AttrOperator
    PLUG_CLS = Eval8PlugOperator

    eval8R = FloatField()
    eval8r = eval8R

    eval8G = FloatField()
    eval8g = eval8G

    eval8B = FloatField()
    eval8b = eval8B


class Eval9PlugOperator(
    Float3CompoundBasePlugOperator["Eval9AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval9R", "eval9r"),
        ("eval9G", "eval9g"),
        ("eval9B", "eval9b"),
    )

    eval9R = FloatField()
    eval9r = eval9R

    eval9G = FloatField()
    eval9g = eval9G

    eval9B = FloatField()
    eval9b = eval9B


class Eval9AttrOperator(
    Float3CompoundBaseAttrOperator[Eval9PlugOperator]
):
    __slots__ = ()

    eval9R = FloatField()
    eval9r = eval9R

    eval9G = FloatField()
    eval9g = eval9G

    eval9B = FloatField()
    eval9b = eval9B


class Eval9Field(
    Float3CompoundBaseField[Eval9AttrOperator, Eval9PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval9AttrOperator
    PLUG_CLS = Eval9PlugOperator

    eval9R = FloatField()
    eval9r = eval9R

    eval9G = FloatField()
    eval9g = eval9G

    eval9B = FloatField()
    eval9b = eval9B


class Eval10PlugOperator(
    Float3CompoundBasePlugOperator["Eval10AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval10R", "eval10r"),
        ("eval10G", "eval10g"),
        ("eval10B", "eval10b"),
    )

    eval10R = FloatField()
    eval10r = eval10R

    eval10G = FloatField()
    eval10g = eval10G

    eval10B = FloatField()
    eval10b = eval10B


class Eval10AttrOperator(
    Float3CompoundBaseAttrOperator[Eval10PlugOperator]
):
    __slots__ = ()

    eval10R = FloatField()
    eval10r = eval10R

    eval10G = FloatField()
    eval10g = eval10G

    eval10B = FloatField()
    eval10b = eval10B


class Eval10Field(
    Float3CompoundBaseField[Eval10AttrOperator, Eval10PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval10AttrOperator
    PLUG_CLS = Eval10PlugOperator

    eval10R = FloatField()
    eval10r = eval10R

    eval10G = FloatField()
    eval10g = eval10G

    eval10B = FloatField()
    eval10b = eval10B


class Eval11PlugOperator(
    Float3CompoundBasePlugOperator["Eval11AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval11R", "eval11r"),
        ("eval11G", "eval11g"),
        ("eval11B", "eval11b"),
    )

    eval11R = FloatField()
    eval11r = eval11R

    eval11G = FloatField()
    eval11g = eval11G

    eval11B = FloatField()
    eval11b = eval11B


class Eval11AttrOperator(
    Float3CompoundBaseAttrOperator[Eval11PlugOperator]
):
    __slots__ = ()

    eval11R = FloatField()
    eval11r = eval11R

    eval11G = FloatField()
    eval11g = eval11G

    eval11B = FloatField()
    eval11b = eval11B


class Eval11Field(
    Float3CompoundBaseField[Eval11AttrOperator, Eval11PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval11AttrOperator
    PLUG_CLS = Eval11PlugOperator

    eval11R = FloatField()
    eval11r = eval11R

    eval11G = FloatField()
    eval11g = eval11G

    eval11B = FloatField()
    eval11b = eval11B


class Eval12PlugOperator(
    Float3CompoundBasePlugOperator["Eval12AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval12R", "eval12r"),
        ("eval12G", "eval12g"),
        ("eval12B", "eval12b"),
    )

    eval12R = FloatField()
    eval12r = eval12R

    eval12G = FloatField()
    eval12g = eval12G

    eval12B = FloatField()
    eval12b = eval12B


class Eval12AttrOperator(
    Float3CompoundBaseAttrOperator[Eval12PlugOperator]
):
    __slots__ = ()

    eval12R = FloatField()
    eval12r = eval12R

    eval12G = FloatField()
    eval12g = eval12G

    eval12B = FloatField()
    eval12b = eval12B


class Eval12Field(
    Float3CompoundBaseField[Eval12AttrOperator, Eval12PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval12AttrOperator
    PLUG_CLS = Eval12PlugOperator

    eval12R = FloatField()
    eval12r = eval12R

    eval12G = FloatField()
    eval12g = eval12G

    eval12B = FloatField()
    eval12b = eval12B


class Eval13PlugOperator(
    Float3CompoundBasePlugOperator["Eval13AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval13R", "eval13r"),
        ("eval13G", "eval13g"),
        ("eval13B", "eval13b"),
    )

    eval13R = FloatField()
    eval13r = eval13R

    eval13G = FloatField()
    eval13g = eval13G

    eval13B = FloatField()
    eval13b = eval13B


class Eval13AttrOperator(
    Float3CompoundBaseAttrOperator[Eval13PlugOperator]
):
    __slots__ = ()

    eval13R = FloatField()
    eval13r = eval13R

    eval13G = FloatField()
    eval13g = eval13G

    eval13B = FloatField()
    eval13b = eval13B


class Eval13Field(
    Float3CompoundBaseField[Eval13AttrOperator, Eval13PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval13AttrOperator
    PLUG_CLS = Eval13PlugOperator

    eval13R = FloatField()
    eval13r = eval13R

    eval13G = FloatField()
    eval13g = eval13G

    eval13B = FloatField()
    eval13b = eval13B


class Eval14PlugOperator(
    Float3CompoundBasePlugOperator["Eval14AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval14R", "eval14r"),
        ("eval14G", "eval14g"),
        ("eval14B", "eval14b"),
    )

    eval14R = FloatField()
    eval14r = eval14R

    eval14G = FloatField()
    eval14g = eval14G

    eval14B = FloatField()
    eval14b = eval14B


class Eval14AttrOperator(
    Float3CompoundBaseAttrOperator[Eval14PlugOperator]
):
    __slots__ = ()

    eval14R = FloatField()
    eval14r = eval14R

    eval14G = FloatField()
    eval14g = eval14G

    eval14B = FloatField()
    eval14b = eval14B


class Eval14Field(
    Float3CompoundBaseField[Eval14AttrOperator, Eval14PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval14AttrOperator
    PLUG_CLS = Eval14PlugOperator

    eval14R = FloatField()
    eval14r = eval14R

    eval14G = FloatField()
    eval14g = eval14G

    eval14B = FloatField()
    eval14b = eval14B


class Eval15PlugOperator(
    Float3CompoundBasePlugOperator["Eval15AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval15R", "eval15r"),
        ("eval15G", "eval15g"),
        ("eval15B", "eval15b"),
    )

    eval15R = FloatField()
    eval15r = eval15R

    eval15G = FloatField()
    eval15g = eval15G

    eval15B = FloatField()
    eval15b = eval15B


class Eval15AttrOperator(
    Float3CompoundBaseAttrOperator[Eval15PlugOperator]
):
    __slots__ = ()

    eval15R = FloatField()
    eval15r = eval15R

    eval15G = FloatField()
    eval15g = eval15G

    eval15B = FloatField()
    eval15b = eval15B


class Eval15Field(
    Float3CompoundBaseField[Eval15AttrOperator, Eval15PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval15AttrOperator
    PLUG_CLS = Eval15PlugOperator

    eval15R = FloatField()
    eval15r = eval15R

    eval15G = FloatField()
    eval15g = eval15G

    eval15B = FloatField()
    eval15b = eval15B


class Eval16PlugOperator(
    Float3CompoundBasePlugOperator["Eval16AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval16R", "eval16r"),
        ("eval16G", "eval16g"),
        ("eval16B", "eval16b"),
    )

    eval16R = FloatField()
    eval16r = eval16R

    eval16G = FloatField()
    eval16g = eval16G

    eval16B = FloatField()
    eval16b = eval16B


class Eval16AttrOperator(
    Float3CompoundBaseAttrOperator[Eval16PlugOperator]
):
    __slots__ = ()

    eval16R = FloatField()
    eval16r = eval16R

    eval16G = FloatField()
    eval16g = eval16G

    eval16B = FloatField()
    eval16b = eval16B


class Eval16Field(
    Float3CompoundBaseField[Eval16AttrOperator, Eval16PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval16AttrOperator
    PLUG_CLS = Eval16PlugOperator

    eval16R = FloatField()
    eval16r = eval16R

    eval16G = FloatField()
    eval16g = eval16G

    eval16B = FloatField()
    eval16b = eval16B


class Eval17PlugOperator(
    Float3CompoundBasePlugOperator["Eval17AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval17R", "eval17r"),
        ("eval17G", "eval17g"),
        ("eval17B", "eval17b"),
    )

    eval17R = FloatField()
    eval17r = eval17R

    eval17G = FloatField()
    eval17g = eval17G

    eval17B = FloatField()
    eval17b = eval17B


class Eval17AttrOperator(
    Float3CompoundBaseAttrOperator[Eval17PlugOperator]
):
    __slots__ = ()

    eval17R = FloatField()
    eval17r = eval17R

    eval17G = FloatField()
    eval17g = eval17G

    eval17B = FloatField()
    eval17b = eval17B


class Eval17Field(
    Float3CompoundBaseField[Eval17AttrOperator, Eval17PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval17AttrOperator
    PLUG_CLS = Eval17PlugOperator

    eval17R = FloatField()
    eval17r = eval17R

    eval17G = FloatField()
    eval17g = eval17G

    eval17B = FloatField()
    eval17b = eval17B


class Eval18PlugOperator(
    Float3CompoundBasePlugOperator["Eval18AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval18R", "eval18r"),
        ("eval18G", "eval18g"),
        ("eval18B", "eval18b"),
    )

    eval18R = FloatField()
    eval18r = eval18R

    eval18G = FloatField()
    eval18g = eval18G

    eval18B = FloatField()
    eval18b = eval18B


class Eval18AttrOperator(
    Float3CompoundBaseAttrOperator[Eval18PlugOperator]
):
    __slots__ = ()

    eval18R = FloatField()
    eval18r = eval18R

    eval18G = FloatField()
    eval18g = eval18G

    eval18B = FloatField()
    eval18b = eval18B


class Eval18Field(
    Float3CompoundBaseField[Eval18AttrOperator, Eval18PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval18AttrOperator
    PLUG_CLS = Eval18PlugOperator

    eval18R = FloatField()
    eval18r = eval18R

    eval18G = FloatField()
    eval18g = eval18G

    eval18B = FloatField()
    eval18b = eval18B


class Eval19PlugOperator(
    Float3CompoundBasePlugOperator["Eval19AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval19R", "eval19r"),
        ("eval19G", "eval19g"),
        ("eval19B", "eval19b"),
    )

    eval19R = FloatField()
    eval19r = eval19R

    eval19G = FloatField()
    eval19g = eval19G

    eval19B = FloatField()
    eval19b = eval19B


class Eval19AttrOperator(
    Float3CompoundBaseAttrOperator[Eval19PlugOperator]
):
    __slots__ = ()

    eval19R = FloatField()
    eval19r = eval19R

    eval19G = FloatField()
    eval19g = eval19G

    eval19B = FloatField()
    eval19b = eval19B


class Eval19Field(
    Float3CompoundBaseField[Eval19AttrOperator, Eval19PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval19AttrOperator
    PLUG_CLS = Eval19PlugOperator

    eval19R = FloatField()
    eval19r = eval19R

    eval19G = FloatField()
    eval19g = eval19G

    eval19B = FloatField()
    eval19b = eval19B


class Eval20PlugOperator(
    Float3CompoundBasePlugOperator["Eval20AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eval20R", "eval20r"),
        ("eval20G", "eval20g"),
        ("eval20B", "eval20b"),
    )

    eval20R = FloatField()
    eval20r = eval20R

    eval20G = FloatField()
    eval20g = eval20G

    eval20B = FloatField()
    eval20b = eval20B


class Eval20AttrOperator(
    Float3CompoundBaseAttrOperator[Eval20PlugOperator]
):
    __slots__ = ()

    eval20R = FloatField()
    eval20r = eval20R

    eval20G = FloatField()
    eval20g = eval20G

    eval20B = FloatField()
    eval20b = eval20B


class Eval20Field(
    Float3CompoundBaseField[Eval20AttrOperator, Eval20PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Eval20AttrOperator
    PLUG_CLS = Eval20PlugOperator

    eval20R = FloatField()
    eval20r = eval20R

    eval20G = FloatField()
    eval20g = eval20G

    eval20B = FloatField()
    eval20b = eval20B


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
