# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.generic import GenericField
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.byte import ByteField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.numeric.range.short import ShortField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
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


class OutSizePlugOperator(
    Float2CompoundBasePlugOperator["OutSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outSizeX", "osx"),
        ("outSizeY", "osy"),
    )

    outSizeX = FloatField(default_value=0.0, writable=False)
    osx = outSizeX

    outSizeY = FloatField(default_value=0.0, writable=False)
    osy = outSizeY


class OutSizeAttrOperator(Float2CompoundBaseAttrOperator[OutSizePlugOperator]):
    __slots__ = ()

    outSizeX = FloatField(default_value=0.0, writable=False)
    osx = outSizeX

    outSizeY = FloatField(default_value=0.0, writable=False)
    osy = outSizeY


class OutSizeField(
    Float2CompoundBaseField[OutSizeAttrOperator, OutSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutSizeAttrOperator
    PLUG_CLS = OutSizePlugOperator

    outSizeX = FloatField(default_value=0.0, writable=False)
    osx = outSizeX

    outSizeY = FloatField(default_value=0.0, writable=False)
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
    Float3CompoundBaseField[
        OutTransparencyAttrOperator, OutTransparencyPlugOperator
    ]
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


class RenderInfoPlugOperator(CompoundPlugOperator["RenderInfoAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("identification", "rlid"),
        ("renderable", "rndr"),
        ("drawColor", "c"),
    )

    identification = ShortField(default_value=0)
    rlid = identification

    renderable = BoolField(default_value=True)
    rndr = renderable

    drawColor = ByteField(default_value=0, min_value=0, max_value=255)
    c = drawColor


class RenderInfoAttrOperator(CompoundAttrOperator[RenderInfoPlugOperator]):
    __slots__ = ()

    identification = ShortField(default_value=0)
    rlid = identification

    renderable = BoolField(default_value=True)
    rndr = renderable

    drawColor = ByteField(default_value=0, min_value=0, max_value=255)
    c = drawColor


class RenderInfoField(
    CompoundField[RenderInfoAttrOperator, RenderInfoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RenderInfoAttrOperator
    PLUG_CLS = RenderInfoPlugOperator

    identification = ShortField(default_value=0)
    rlid = identification

    renderable = BoolField(default_value=True)
    rndr = renderable

    drawColor = ByteField(default_value=0, min_value=0, max_value=255)
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

    beauty = BoolField(default_value=True)
    b = beauty

    color = BoolField(default_value=False)
    cp = color

    ambient = BoolField(default_value=False)
    am = ambient

    diffuse = BoolField(default_value=False)
    di = diffuse

    specular = BoolField(default_value=False)
    sp = specular

    shadow = BoolField(default_value=False)
    s = shadow


class RenderPassInfoAttrOperator(
    CompoundAttrOperator[RenderPassInfoPlugOperator]
):
    __slots__ = ()

    beauty = BoolField(default_value=True)
    b = beauty

    color = BoolField(default_value=False)
    cp = color

    ambient = BoolField(default_value=False)
    am = ambient

    diffuse = BoolField(default_value=False)
    di = diffuse

    specular = BoolField(default_value=False)
    sp = specular

    shadow = BoolField(default_value=False)
    s = shadow


class RenderPassInfoField(
    CompoundField[RenderPassInfoAttrOperator, RenderPassInfoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RenderPassInfoAttrOperator
    PLUG_CLS = RenderPassInfoPlugOperator

    beauty = BoolField(default_value=True)
    b = beauty

    color = BoolField(default_value=False)
    cp = color

    ambient = BoolField(default_value=False)
    am = ambient

    diffuse = BoolField(default_value=False)
    di = diffuse

    specular = BoolField(default_value=False)
    sp = specular

    shadow = BoolField(default_value=False)
    s = shadow


class AdjustmentsPlugOperator(CompoundPlugOperator["AdjustmentsAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("plug", "plg"),
        ("value", "val"),
    )

    plug = GenericField(readable=False)
    plg = plug

    value = GenericField()
    val = value


class AdjustmentsAttrOperator(CompoundAttrOperator[AdjustmentsPlugOperator]):
    __slots__ = ()

    plug = GenericField(readable=False)
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

    outPlug = GenericField(readable=False)
    opg = outPlug

    outValue = GenericField()
    ovl = outValue

    outId = LongField(default_value=-1)
    oaid = outId


class OutAdjustmentsAttrOperator(
    CompoundAttrOperator[OutAdjustmentsPlugOperator]
):
    __slots__ = ()

    outPlug = GenericField(readable=False)
    opg = outPlug

    outValue = GenericField()
    ovl = outValue

    outId = LongField(default_value=-1)
    oaid = outId


class OutAdjustmentsField(
    CompoundField[OutAdjustmentsAttrOperator, OutAdjustmentsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutAdjustmentsAttrOperator
    PLUG_CLS = OutAdjustmentsPlugOperator
