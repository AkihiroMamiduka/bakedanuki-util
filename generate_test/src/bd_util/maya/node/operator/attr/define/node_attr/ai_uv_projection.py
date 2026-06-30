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


class ProjectionColorPlugOperator(
    Float3CompoundBasePlugOperator["ProjectionColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("projectionColorR", "projection_colorr"),
        ("projectionColorG", "projection_colorg"),
        ("projectionColorB", "projection_colorb"),
    )

    projectionColorR = FloatField()
    projection_colorr = projectionColorR

    projectionColorG = FloatField()
    projection_colorg = projectionColorG

    projectionColorB = FloatField()
    projection_colorb = projectionColorB


class ProjectionColorAttrOperator(
    Float3CompoundBaseAttrOperator[ProjectionColorPlugOperator]
):
    __slots__ = ()

    projectionColorR = FloatField()
    projection_colorr = projectionColorR

    projectionColorG = FloatField()
    projection_colorg = projectionColorG

    projectionColorB = FloatField()
    projection_colorb = projectionColorB


class ProjectionColorField(
    Float3CompoundBaseField[ProjectionColorAttrOperator, ProjectionColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ProjectionColorAttrOperator
    PLUG_CLS = ProjectionColorPlugOperator

    projectionColorR = FloatField()
    projection_colorr = projectionColorR

    projectionColorG = FloatField()
    projection_colorg = projectionColorG

    projectionColorB = FloatField()
    projection_colorb = projectionColorB


class PPlugOperator(
    Float3CompoundBasePlugOperator["PAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("PX", "Px"),
        ("PY", "Py"),
        ("PZ", "Pz"),
    )

    PX = FloatField()
    Px = PX

    PY = FloatField()
    Py = PY

    PZ = FloatField()
    Pz = PZ


class PAttrOperator(
    Float3CompoundBaseAttrOperator[PPlugOperator]
):
    __slots__ = ()

    PX = FloatField()
    Px = PX

    PY = FloatField()
    Py = PY

    PZ = FloatField()
    Pz = PZ


class PField(
    Float3CompoundBaseField[PAttrOperator, PPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PAttrOperator
    PLUG_CLS = PPlugOperator

    PX = FloatField()
    Px = PX

    PY = FloatField()
    Py = PY

    PZ = FloatField()
    Pz = PZ


class DefaultColorPlugOperator(
    Float3CompoundBasePlugOperator["DefaultColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("defaultColorR", "default_colorr"),
        ("defaultColorG", "default_colorg"),
        ("defaultColorB", "default_colorb"),
    )

    defaultColorR = FloatField()
    default_colorr = defaultColorR

    defaultColorG = FloatField()
    default_colorg = defaultColorG

    defaultColorB = FloatField()
    default_colorb = defaultColorB


class DefaultColorAttrOperator(
    Float3CompoundBaseAttrOperator[DefaultColorPlugOperator]
):
    __slots__ = ()

    defaultColorR = FloatField()
    default_colorr = defaultColorR

    defaultColorG = FloatField()
    default_colorg = defaultColorG

    defaultColorB = FloatField()
    default_colorb = defaultColorB


class DefaultColorField(
    Float3CompoundBaseField[DefaultColorAttrOperator, DefaultColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DefaultColorAttrOperator
    PLUG_CLS = DefaultColorPlugOperator

    defaultColorR = FloatField()
    default_colorr = defaultColorR

    defaultColorG = FloatField()
    default_colorg = defaultColorG

    defaultColorB = FloatField()
    default_colorb = defaultColorB
