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


class ShallowScatterColorPlugOperator(
    Float3CompoundBasePlugOperator["ShallowScatterColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shallowScatterColorR", "shallow_scatter_colorr"),
        ("shallowScatterColorG", "shallow_scatter_colorg"),
        ("shallowScatterColorB", "shallow_scatter_colorb"),
    )

    shallowScatterColorR = FloatField()
    shallow_scatter_colorr = shallowScatterColorR

    shallowScatterColorG = FloatField()
    shallow_scatter_colorg = shallowScatterColorG

    shallowScatterColorB = FloatField()
    shallow_scatter_colorb = shallowScatterColorB


class ShallowScatterColorAttrOperator(
    Float3CompoundBaseAttrOperator[ShallowScatterColorPlugOperator]
):
    __slots__ = ()

    shallowScatterColorR = FloatField()
    shallow_scatter_colorr = shallowScatterColorR

    shallowScatterColorG = FloatField()
    shallow_scatter_colorg = shallowScatterColorG

    shallowScatterColorB = FloatField()
    shallow_scatter_colorb = shallowScatterColorB


class ShallowScatterColorField(
    Float3CompoundBaseField[ShallowScatterColorAttrOperator, ShallowScatterColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShallowScatterColorAttrOperator
    PLUG_CLS = ShallowScatterColorPlugOperator

    shallowScatterColorR = FloatField()
    shallow_scatter_colorr = shallowScatterColorR

    shallowScatterColorG = FloatField()
    shallow_scatter_colorg = shallowScatterColorG

    shallowScatterColorB = FloatField()
    shallow_scatter_colorb = shallowScatterColorB


class MidScatterColorPlugOperator(
    Float3CompoundBasePlugOperator["MidScatterColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("midScatterColorR", "mid_scatter_colorr"),
        ("midScatterColorG", "mid_scatter_colorg"),
        ("midScatterColorB", "mid_scatter_colorb"),
    )

    midScatterColorR = FloatField()
    mid_scatter_colorr = midScatterColorR

    midScatterColorG = FloatField()
    mid_scatter_colorg = midScatterColorG

    midScatterColorB = FloatField()
    mid_scatter_colorb = midScatterColorB


class MidScatterColorAttrOperator(
    Float3CompoundBaseAttrOperator[MidScatterColorPlugOperator]
):
    __slots__ = ()

    midScatterColorR = FloatField()
    mid_scatter_colorr = midScatterColorR

    midScatterColorG = FloatField()
    mid_scatter_colorg = midScatterColorG

    midScatterColorB = FloatField()
    mid_scatter_colorb = midScatterColorB


class MidScatterColorField(
    Float3CompoundBaseField[MidScatterColorAttrOperator, MidScatterColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MidScatterColorAttrOperator
    PLUG_CLS = MidScatterColorPlugOperator

    midScatterColorR = FloatField()
    mid_scatter_colorr = midScatterColorR

    midScatterColorG = FloatField()
    mid_scatter_colorg = midScatterColorG

    midScatterColorB = FloatField()
    mid_scatter_colorb = midScatterColorB


class DeepScatterColorPlugOperator(
    Float3CompoundBasePlugOperator["DeepScatterColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("deepScatterColorR", "deep_scatter_colorr"),
        ("deepScatterColorG", "deep_scatter_colorg"),
        ("deepScatterColorB", "deep_scatter_colorb"),
    )

    deepScatterColorR = FloatField()
    deep_scatter_colorr = deepScatterColorR

    deepScatterColorG = FloatField()
    deep_scatter_colorg = deepScatterColorG

    deepScatterColorB = FloatField()
    deep_scatter_colorb = deepScatterColorB


class DeepScatterColorAttrOperator(
    Float3CompoundBaseAttrOperator[DeepScatterColorPlugOperator]
):
    __slots__ = ()

    deepScatterColorR = FloatField()
    deep_scatter_colorr = deepScatterColorR

    deepScatterColorG = FloatField()
    deep_scatter_colorg = deepScatterColorG

    deepScatterColorB = FloatField()
    deep_scatter_colorb = deepScatterColorB


class DeepScatterColorField(
    Float3CompoundBaseField[DeepScatterColorAttrOperator, DeepScatterColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DeepScatterColorAttrOperator
    PLUG_CLS = DeepScatterColorPlugOperator

    deepScatterColorR = FloatField()
    deep_scatter_colorr = deepScatterColorR

    deepScatterColorG = FloatField()
    deep_scatter_colorg = deepScatterColorG

    deepScatterColorB = FloatField()
    deep_scatter_colorb = deepScatterColorB


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


class OpacityColorPlugOperator(
    Float3CompoundBasePlugOperator["OpacityColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("opacityColorR", "opacity_colorr"),
        ("opacityColorG", "opacity_colorg"),
        ("opacityColorB", "opacity_colorb"),
    )

    opacityColorR = FloatField()
    opacity_colorr = opacityColorR

    opacityColorG = FloatField()
    opacity_colorg = opacityColorG

    opacityColorB = FloatField()
    opacity_colorb = opacityColorB


class OpacityColorAttrOperator(
    Float3CompoundBaseAttrOperator[OpacityColorPlugOperator]
):
    __slots__ = ()

    opacityColorR = FloatField()
    opacity_colorr = opacityColorR

    opacityColorG = FloatField()
    opacity_colorg = opacityColorG

    opacityColorB = FloatField()
    opacity_colorb = opacityColorB


class OpacityColorField(
    Float3CompoundBaseField[OpacityColorAttrOperator, OpacityColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OpacityColorAttrOperator
    PLUG_CLS = OpacityColorPlugOperator

    opacityColorR = FloatField()
    opacity_colorr = opacityColorR

    opacityColorG = FloatField()
    opacity_colorg = opacityColorG

    opacityColorB = FloatField()
    opacity_colorb = opacityColorB


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
