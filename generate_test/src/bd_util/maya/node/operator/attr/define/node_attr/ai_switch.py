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


class Input0PlugOperator(
    Float3CompoundBasePlugOperator["Input0AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input0R", "input0r"),
        ("input0G", "input0g"),
        ("input0B", "input0b"),
    )

    input0R = FloatField()
    input0r = input0R

    input0G = FloatField()
    input0g = input0G

    input0B = FloatField()
    input0b = input0B


class Input0AttrOperator(
    Float3CompoundBaseAttrOperator[Input0PlugOperator]
):
    __slots__ = ()

    input0R = FloatField()
    input0r = input0R

    input0G = FloatField()
    input0g = input0G

    input0B = FloatField()
    input0b = input0B


class Input0Field(
    Float3CompoundBaseField[Input0AttrOperator, Input0PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input0AttrOperator
    PLUG_CLS = Input0PlugOperator

    input0R = FloatField()
    input0r = input0R

    input0G = FloatField()
    input0g = input0G

    input0B = FloatField()
    input0b = input0B


class Input1PlugOperator(
    Float3CompoundBasePlugOperator["Input1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input1R", "input1r"),
        ("input1G", "input1g"),
        ("input1B", "input1b"),
    )

    input1R = FloatField()
    input1r = input1R

    input1G = FloatField()
    input1g = input1G

    input1B = FloatField()
    input1b = input1B


class Input1AttrOperator(
    Float3CompoundBaseAttrOperator[Input1PlugOperator]
):
    __slots__ = ()

    input1R = FloatField()
    input1r = input1R

    input1G = FloatField()
    input1g = input1G

    input1B = FloatField()
    input1b = input1B


class Input1Field(
    Float3CompoundBaseField[Input1AttrOperator, Input1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input1AttrOperator
    PLUG_CLS = Input1PlugOperator

    input1R = FloatField()
    input1r = input1R

    input1G = FloatField()
    input1g = input1G

    input1B = FloatField()
    input1b = input1B


class Input2PlugOperator(
    Float3CompoundBasePlugOperator["Input2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input2R", "input2r"),
        ("input2G", "input2g"),
        ("input2B", "input2b"),
    )

    input2R = FloatField()
    input2r = input2R

    input2G = FloatField()
    input2g = input2G

    input2B = FloatField()
    input2b = input2B


class Input2AttrOperator(
    Float3CompoundBaseAttrOperator[Input2PlugOperator]
):
    __slots__ = ()

    input2R = FloatField()
    input2r = input2R

    input2G = FloatField()
    input2g = input2G

    input2B = FloatField()
    input2b = input2B


class Input2Field(
    Float3CompoundBaseField[Input2AttrOperator, Input2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input2AttrOperator
    PLUG_CLS = Input2PlugOperator

    input2R = FloatField()
    input2r = input2R

    input2G = FloatField()
    input2g = input2G

    input2B = FloatField()
    input2b = input2B


class Input3PlugOperator(
    Float3CompoundBasePlugOperator["Input3AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input3R", "input3r"),
        ("input3G", "input3g"),
        ("input3B", "input3b"),
    )

    input3R = FloatField()
    input3r = input3R

    input3G = FloatField()
    input3g = input3G

    input3B = FloatField()
    input3b = input3B


class Input3AttrOperator(
    Float3CompoundBaseAttrOperator[Input3PlugOperator]
):
    __slots__ = ()

    input3R = FloatField()
    input3r = input3R

    input3G = FloatField()
    input3g = input3G

    input3B = FloatField()
    input3b = input3B


class Input3Field(
    Float3CompoundBaseField[Input3AttrOperator, Input3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input3AttrOperator
    PLUG_CLS = Input3PlugOperator

    input3R = FloatField()
    input3r = input3R

    input3G = FloatField()
    input3g = input3G

    input3B = FloatField()
    input3b = input3B


class Input4PlugOperator(
    Float3CompoundBasePlugOperator["Input4AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input4R", "input4r"),
        ("input4G", "input4g"),
        ("input4B", "input4b"),
    )

    input4R = FloatField()
    input4r = input4R

    input4G = FloatField()
    input4g = input4G

    input4B = FloatField()
    input4b = input4B


class Input4AttrOperator(
    Float3CompoundBaseAttrOperator[Input4PlugOperator]
):
    __slots__ = ()

    input4R = FloatField()
    input4r = input4R

    input4G = FloatField()
    input4g = input4G

    input4B = FloatField()
    input4b = input4B


class Input4Field(
    Float3CompoundBaseField[Input4AttrOperator, Input4PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input4AttrOperator
    PLUG_CLS = Input4PlugOperator

    input4R = FloatField()
    input4r = input4R

    input4G = FloatField()
    input4g = input4G

    input4B = FloatField()
    input4b = input4B


class Input5PlugOperator(
    Float3CompoundBasePlugOperator["Input5AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input5R", "input5r"),
        ("input5G", "input5g"),
        ("input5B", "input5b"),
    )

    input5R = FloatField()
    input5r = input5R

    input5G = FloatField()
    input5g = input5G

    input5B = FloatField()
    input5b = input5B


class Input5AttrOperator(
    Float3CompoundBaseAttrOperator[Input5PlugOperator]
):
    __slots__ = ()

    input5R = FloatField()
    input5r = input5R

    input5G = FloatField()
    input5g = input5G

    input5B = FloatField()
    input5b = input5B


class Input5Field(
    Float3CompoundBaseField[Input5AttrOperator, Input5PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input5AttrOperator
    PLUG_CLS = Input5PlugOperator

    input5R = FloatField()
    input5r = input5R

    input5G = FloatField()
    input5g = input5G

    input5B = FloatField()
    input5b = input5B


class Input6PlugOperator(
    Float3CompoundBasePlugOperator["Input6AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input6R", "input6r"),
        ("input6G", "input6g"),
        ("input6B", "input6b"),
    )

    input6R = FloatField()
    input6r = input6R

    input6G = FloatField()
    input6g = input6G

    input6B = FloatField()
    input6b = input6B


class Input6AttrOperator(
    Float3CompoundBaseAttrOperator[Input6PlugOperator]
):
    __slots__ = ()

    input6R = FloatField()
    input6r = input6R

    input6G = FloatField()
    input6g = input6G

    input6B = FloatField()
    input6b = input6B


class Input6Field(
    Float3CompoundBaseField[Input6AttrOperator, Input6PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input6AttrOperator
    PLUG_CLS = Input6PlugOperator

    input6R = FloatField()
    input6r = input6R

    input6G = FloatField()
    input6g = input6G

    input6B = FloatField()
    input6b = input6B


class Input7PlugOperator(
    Float3CompoundBasePlugOperator["Input7AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input7R", "input7r"),
        ("input7G", "input7g"),
        ("input7B", "input7b"),
    )

    input7R = FloatField()
    input7r = input7R

    input7G = FloatField()
    input7g = input7G

    input7B = FloatField()
    input7b = input7B


class Input7AttrOperator(
    Float3CompoundBaseAttrOperator[Input7PlugOperator]
):
    __slots__ = ()

    input7R = FloatField()
    input7r = input7R

    input7G = FloatField()
    input7g = input7G

    input7B = FloatField()
    input7b = input7B


class Input7Field(
    Float3CompoundBaseField[Input7AttrOperator, Input7PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input7AttrOperator
    PLUG_CLS = Input7PlugOperator

    input7R = FloatField()
    input7r = input7R

    input7G = FloatField()
    input7g = input7G

    input7B = FloatField()
    input7b = input7B


class Input8PlugOperator(
    Float3CompoundBasePlugOperator["Input8AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input8R", "input8r"),
        ("input8G", "input8g"),
        ("input8B", "input8b"),
    )

    input8R = FloatField()
    input8r = input8R

    input8G = FloatField()
    input8g = input8G

    input8B = FloatField()
    input8b = input8B


class Input8AttrOperator(
    Float3CompoundBaseAttrOperator[Input8PlugOperator]
):
    __slots__ = ()

    input8R = FloatField()
    input8r = input8R

    input8G = FloatField()
    input8g = input8G

    input8B = FloatField()
    input8b = input8B


class Input8Field(
    Float3CompoundBaseField[Input8AttrOperator, Input8PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input8AttrOperator
    PLUG_CLS = Input8PlugOperator

    input8R = FloatField()
    input8r = input8R

    input8G = FloatField()
    input8g = input8G

    input8B = FloatField()
    input8b = input8B


class Input9PlugOperator(
    Float3CompoundBasePlugOperator["Input9AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input9R", "input9r"),
        ("input9G", "input9g"),
        ("input9B", "input9b"),
    )

    input9R = FloatField()
    input9r = input9R

    input9G = FloatField()
    input9g = input9G

    input9B = FloatField()
    input9b = input9B


class Input9AttrOperator(
    Float3CompoundBaseAttrOperator[Input9PlugOperator]
):
    __slots__ = ()

    input9R = FloatField()
    input9r = input9R

    input9G = FloatField()
    input9g = input9G

    input9B = FloatField()
    input9b = input9B


class Input9Field(
    Float3CompoundBaseField[Input9AttrOperator, Input9PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input9AttrOperator
    PLUG_CLS = Input9PlugOperator

    input9R = FloatField()
    input9r = input9R

    input9G = FloatField()
    input9g = input9G

    input9B = FloatField()
    input9b = input9B


class Input10PlugOperator(
    Float3CompoundBasePlugOperator["Input10AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input10R", "input10r"),
        ("input10G", "input10g"),
        ("input10B", "input10b"),
    )

    input10R = FloatField()
    input10r = input10R

    input10G = FloatField()
    input10g = input10G

    input10B = FloatField()
    input10b = input10B


class Input10AttrOperator(
    Float3CompoundBaseAttrOperator[Input10PlugOperator]
):
    __slots__ = ()

    input10R = FloatField()
    input10r = input10R

    input10G = FloatField()
    input10g = input10G

    input10B = FloatField()
    input10b = input10B


class Input10Field(
    Float3CompoundBaseField[Input10AttrOperator, Input10PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input10AttrOperator
    PLUG_CLS = Input10PlugOperator

    input10R = FloatField()
    input10r = input10R

    input10G = FloatField()
    input10g = input10G

    input10B = FloatField()
    input10b = input10B


class Input11PlugOperator(
    Float3CompoundBasePlugOperator["Input11AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input11R", "input11r"),
        ("input11G", "input11g"),
        ("input11B", "input11b"),
    )

    input11R = FloatField()
    input11r = input11R

    input11G = FloatField()
    input11g = input11G

    input11B = FloatField()
    input11b = input11B


class Input11AttrOperator(
    Float3CompoundBaseAttrOperator[Input11PlugOperator]
):
    __slots__ = ()

    input11R = FloatField()
    input11r = input11R

    input11G = FloatField()
    input11g = input11G

    input11B = FloatField()
    input11b = input11B


class Input11Field(
    Float3CompoundBaseField[Input11AttrOperator, Input11PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input11AttrOperator
    PLUG_CLS = Input11PlugOperator

    input11R = FloatField()
    input11r = input11R

    input11G = FloatField()
    input11g = input11G

    input11B = FloatField()
    input11b = input11B


class Input12PlugOperator(
    Float3CompoundBasePlugOperator["Input12AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input12R", "input12r"),
        ("input12G", "input12g"),
        ("input12B", "input12b"),
    )

    input12R = FloatField()
    input12r = input12R

    input12G = FloatField()
    input12g = input12G

    input12B = FloatField()
    input12b = input12B


class Input12AttrOperator(
    Float3CompoundBaseAttrOperator[Input12PlugOperator]
):
    __slots__ = ()

    input12R = FloatField()
    input12r = input12R

    input12G = FloatField()
    input12g = input12G

    input12B = FloatField()
    input12b = input12B


class Input12Field(
    Float3CompoundBaseField[Input12AttrOperator, Input12PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input12AttrOperator
    PLUG_CLS = Input12PlugOperator

    input12R = FloatField()
    input12r = input12R

    input12G = FloatField()
    input12g = input12G

    input12B = FloatField()
    input12b = input12B


class Input13PlugOperator(
    Float3CompoundBasePlugOperator["Input13AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input13R", "input13r"),
        ("input13G", "input13g"),
        ("input13B", "input13b"),
    )

    input13R = FloatField()
    input13r = input13R

    input13G = FloatField()
    input13g = input13G

    input13B = FloatField()
    input13b = input13B


class Input13AttrOperator(
    Float3CompoundBaseAttrOperator[Input13PlugOperator]
):
    __slots__ = ()

    input13R = FloatField()
    input13r = input13R

    input13G = FloatField()
    input13g = input13G

    input13B = FloatField()
    input13b = input13B


class Input13Field(
    Float3CompoundBaseField[Input13AttrOperator, Input13PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input13AttrOperator
    PLUG_CLS = Input13PlugOperator

    input13R = FloatField()
    input13r = input13R

    input13G = FloatField()
    input13g = input13G

    input13B = FloatField()
    input13b = input13B


class Input14PlugOperator(
    Float3CompoundBasePlugOperator["Input14AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input14R", "input14r"),
        ("input14G", "input14g"),
        ("input14B", "input14b"),
    )

    input14R = FloatField()
    input14r = input14R

    input14G = FloatField()
    input14g = input14G

    input14B = FloatField()
    input14b = input14B


class Input14AttrOperator(
    Float3CompoundBaseAttrOperator[Input14PlugOperator]
):
    __slots__ = ()

    input14R = FloatField()
    input14r = input14R

    input14G = FloatField()
    input14g = input14G

    input14B = FloatField()
    input14b = input14B


class Input14Field(
    Float3CompoundBaseField[Input14AttrOperator, Input14PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input14AttrOperator
    PLUG_CLS = Input14PlugOperator

    input14R = FloatField()
    input14r = input14R

    input14G = FloatField()
    input14g = input14G

    input14B = FloatField()
    input14b = input14B


class Input15PlugOperator(
    Float3CompoundBasePlugOperator["Input15AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input15R", "input15r"),
        ("input15G", "input15g"),
        ("input15B", "input15b"),
    )

    input15R = FloatField()
    input15r = input15R

    input15G = FloatField()
    input15g = input15G

    input15B = FloatField()
    input15b = input15B


class Input15AttrOperator(
    Float3CompoundBaseAttrOperator[Input15PlugOperator]
):
    __slots__ = ()

    input15R = FloatField()
    input15r = input15R

    input15G = FloatField()
    input15g = input15G

    input15B = FloatField()
    input15b = input15B


class Input15Field(
    Float3CompoundBaseField[Input15AttrOperator, Input15PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input15AttrOperator
    PLUG_CLS = Input15PlugOperator

    input15R = FloatField()
    input15r = input15R

    input15G = FloatField()
    input15g = input15G

    input15B = FloatField()
    input15b = input15B


class Input16PlugOperator(
    Float3CompoundBasePlugOperator["Input16AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input16R", "input16r"),
        ("input16G", "input16g"),
        ("input16B", "input16b"),
    )

    input16R = FloatField()
    input16r = input16R

    input16G = FloatField()
    input16g = input16G

    input16B = FloatField()
    input16b = input16B


class Input16AttrOperator(
    Float3CompoundBaseAttrOperator[Input16PlugOperator]
):
    __slots__ = ()

    input16R = FloatField()
    input16r = input16R

    input16G = FloatField()
    input16g = input16G

    input16B = FloatField()
    input16b = input16B


class Input16Field(
    Float3CompoundBaseField[Input16AttrOperator, Input16PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input16AttrOperator
    PLUG_CLS = Input16PlugOperator

    input16R = FloatField()
    input16r = input16R

    input16G = FloatField()
    input16g = input16G

    input16B = FloatField()
    input16b = input16B


class Input17PlugOperator(
    Float3CompoundBasePlugOperator["Input17AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input17R", "input17r"),
        ("input17G", "input17g"),
        ("input17B", "input17b"),
    )

    input17R = FloatField()
    input17r = input17R

    input17G = FloatField()
    input17g = input17G

    input17B = FloatField()
    input17b = input17B


class Input17AttrOperator(
    Float3CompoundBaseAttrOperator[Input17PlugOperator]
):
    __slots__ = ()

    input17R = FloatField()
    input17r = input17R

    input17G = FloatField()
    input17g = input17G

    input17B = FloatField()
    input17b = input17B


class Input17Field(
    Float3CompoundBaseField[Input17AttrOperator, Input17PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input17AttrOperator
    PLUG_CLS = Input17PlugOperator

    input17R = FloatField()
    input17r = input17R

    input17G = FloatField()
    input17g = input17G

    input17B = FloatField()
    input17b = input17B


class Input18PlugOperator(
    Float3CompoundBasePlugOperator["Input18AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input18R", "input18r"),
        ("input18G", "input18g"),
        ("input18B", "input18b"),
    )

    input18R = FloatField()
    input18r = input18R

    input18G = FloatField()
    input18g = input18G

    input18B = FloatField()
    input18b = input18B


class Input18AttrOperator(
    Float3CompoundBaseAttrOperator[Input18PlugOperator]
):
    __slots__ = ()

    input18R = FloatField()
    input18r = input18R

    input18G = FloatField()
    input18g = input18G

    input18B = FloatField()
    input18b = input18B


class Input18Field(
    Float3CompoundBaseField[Input18AttrOperator, Input18PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input18AttrOperator
    PLUG_CLS = Input18PlugOperator

    input18R = FloatField()
    input18r = input18R

    input18G = FloatField()
    input18g = input18G

    input18B = FloatField()
    input18b = input18B


class Input19PlugOperator(
    Float3CompoundBasePlugOperator["Input19AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input19R", "input19r"),
        ("input19G", "input19g"),
        ("input19B", "input19b"),
    )

    input19R = FloatField()
    input19r = input19R

    input19G = FloatField()
    input19g = input19G

    input19B = FloatField()
    input19b = input19B


class Input19AttrOperator(
    Float3CompoundBaseAttrOperator[Input19PlugOperator]
):
    __slots__ = ()

    input19R = FloatField()
    input19r = input19R

    input19G = FloatField()
    input19g = input19G

    input19B = FloatField()
    input19b = input19B


class Input19Field(
    Float3CompoundBaseField[Input19AttrOperator, Input19PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input19AttrOperator
    PLUG_CLS = Input19PlugOperator

    input19R = FloatField()
    input19r = input19R

    input19G = FloatField()
    input19g = input19G

    input19B = FloatField()
    input19b = input19B
