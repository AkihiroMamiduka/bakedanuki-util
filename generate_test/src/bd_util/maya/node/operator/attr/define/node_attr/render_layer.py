# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.generic import GenericField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.byte import ByteField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.numeric_scalar_range.short import ShortField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)
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


class OutSizePlugOperator(
    Float2CompoundBasePlugOperator["OutSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outSizeX", "osx"),
        ("outSizeY", "osy"),
    )

    outSizeX = FloatField()
    osx = outSizeX

    outSizeY = FloatField()
    osy = outSizeY


class OutSizeAttrOperator(
    Float2CompoundBaseAttrOperator[OutSizePlugOperator]
):
    __slots__ = ()

    outSizeX = FloatField()
    osx = outSizeX

    outSizeY = FloatField()
    osy = outSizeY


class OutSizeField(
    Float2CompoundBaseField[OutSizeAttrOperator, OutSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutSizeAttrOperator
    PLUG_CLS = OutSizePlugOperator

    outSizeX = FloatField()
    osx = outSizeX

    outSizeY = FloatField()
    osy = outSizeY


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


class RenderInfoPlugOperator(
    CompoundPlugOperator["RenderInfoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("identification", "rlid"),
        ("renderable", "rndr"),
        ("drawColor", "c"),
    )

    identification = ShortField()
    rlid = identification

    renderable = BoolField()
    rndr = renderable

    drawColor = ByteField()
    c = drawColor


class RenderInfoAttrOperator(
    CompoundAttrOperator[RenderInfoPlugOperator]
):
    __slots__ = ()

    identification = ShortField()
    rlid = identification

    renderable = BoolField()
    rndr = renderable

    drawColor = ByteField()
    c = drawColor


class RenderInfoField(
    CompoundField[RenderInfoAttrOperator, RenderInfoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RenderInfoAttrOperator
    PLUG_CLS = RenderInfoPlugOperator

    identification = ShortField()
    rlid = identification

    renderable = BoolField()
    rndr = renderable

    drawColor = ByteField()
    c = drawColor


class RenderPassInfoPlugOperator(
    CompoundPlugOperator["RenderPassInfoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("beauty", "b"),
        ("color", "cp"),
        ("ambient", "am"),
        ("diffuse", "di"),
        ("specular", "sp"),
        ("shadow", "s"),
    )

    beauty = BoolField()
    b = beauty

    color = BoolField()
    cp = color

    ambient = BoolField()
    am = ambient

    diffuse = BoolField()
    di = diffuse

    specular = BoolField()
    sp = specular

    shadow = BoolField()
    s = shadow


class RenderPassInfoAttrOperator(
    CompoundAttrOperator[RenderPassInfoPlugOperator]
):
    __slots__ = ()

    beauty = BoolField()
    b = beauty

    color = BoolField()
    cp = color

    ambient = BoolField()
    am = ambient

    diffuse = BoolField()
    di = diffuse

    specular = BoolField()
    sp = specular

    shadow = BoolField()
    s = shadow


class RenderPassInfoField(
    CompoundField[RenderPassInfoAttrOperator, RenderPassInfoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RenderPassInfoAttrOperator
    PLUG_CLS = RenderPassInfoPlugOperator

    beauty = BoolField()
    b = beauty

    color = BoolField()
    cp = color

    ambient = BoolField()
    am = ambient

    diffuse = BoolField()
    di = diffuse

    specular = BoolField()
    sp = specular

    shadow = BoolField()
    s = shadow


class AdjustmentsPlugOperator(
    CompoundPlugOperator["AdjustmentsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("plug", "plg"),
        ("value", "val"),
    )

    plug = GenericField()
    plg = plug

    value = GenericField()
    val = value


class AdjustmentsAttrOperator(
    CompoundAttrOperator[AdjustmentsPlugOperator]
):
    __slots__ = ()

    plug = GenericField()
    plg = plug

    value = GenericField()
    val = value


class AdjustmentsField(
    CompoundField[AdjustmentsAttrOperator, AdjustmentsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AdjustmentsAttrOperator
    PLUG_CLS = AdjustmentsPlugOperator


class OutAdjustmentsPlugOperator(
    CompoundPlugOperator["OutAdjustmentsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outPlug", "opg"),
        ("outValue", "ovl"),
        ("outId", "oaid"),
    )

    outPlug = GenericField()
    opg = outPlug

    outValue = GenericField()
    ovl = outValue

    outId = LongField()
    oaid = outId


class OutAdjustmentsAttrOperator(
    CompoundAttrOperator[OutAdjustmentsPlugOperator]
):
    __slots__ = ()

    outPlug = GenericField()
    opg = outPlug

    outValue = GenericField()
    ovl = outValue

    outId = LongField()
    oaid = outId


class OutAdjustmentsField(
    CompoundField[OutAdjustmentsAttrOperator, OutAdjustmentsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutAdjustmentsAttrOperator
    PLUG_CLS = OutAdjustmentsPlugOperator
