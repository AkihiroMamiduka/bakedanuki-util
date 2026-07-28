# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
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

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
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


class ProjectionColorPlugOperator(
    Float3CompoundBasePlugOperator["ProjectionColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("projectionColorR", "projection_colorr"),
        ("projectionColorG", "projection_colorg"),
        ("projectionColorB", "projection_colorb"),
    )

    projectionColorR = FloatField(default_value=1.0)
    projection_colorr = projectionColorR

    projectionColorG = FloatField(default_value=1.0)
    projection_colorg = projectionColorG

    projectionColorB = FloatField(default_value=1.0)
    projection_colorb = projectionColorB


class ProjectionColorAttrOperator(
    Float3CompoundBaseAttrOperator[ProjectionColorPlugOperator]
):
    __slots__ = ()

    projectionColorR = FloatField(default_value=1.0)
    projection_colorr = projectionColorR

    projectionColorG = FloatField(default_value=1.0)
    projection_colorg = projectionColorG

    projectionColorB = FloatField(default_value=1.0)
    projection_colorb = projectionColorB


class ProjectionColorField(
    Float3CompoundBaseField[
        ProjectionColorAttrOperator, ProjectionColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ProjectionColorAttrOperator
    PLUG_CLS = ProjectionColorPlugOperator

    projectionColorR = FloatField(default_value=1.0)
    projection_colorr = projectionColorR

    projectionColorG = FloatField(default_value=1.0)
    projection_colorg = projectionColorG

    projectionColorB = FloatField(default_value=1.0)
    projection_colorb = projectionColorB


class PPlugOperator(Float3CompoundBasePlugOperator["PAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("PX", "Px"),
        ("PY", "Py"),
        ("PZ", "Pz"),
    )

    PX = FloatField(default_value=0.0)
    Px = PX

    PY = FloatField(default_value=0.0)
    Py = PY

    PZ = FloatField(default_value=0.0)
    Pz = PZ


class PAttrOperator(Float3CompoundBaseAttrOperator[PPlugOperator]):
    __slots__ = ()

    PX = FloatField(default_value=0.0)
    Px = PX

    PY = FloatField(default_value=0.0)
    Py = PY

    PZ = FloatField(default_value=0.0)
    Pz = PZ


class PField(Float3CompoundBaseField[PAttrOperator, PPlugOperator]):
    __slots__ = ()

    ATTR_CLS = PAttrOperator
    PLUG_CLS = PPlugOperator

    PX = FloatField(default_value=0.0)
    Px = PX

    PY = FloatField(default_value=0.0)
    Py = PY

    PZ = FloatField(default_value=0.0)
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

    defaultColorR = FloatField(default_value=0.0)
    default_colorr = defaultColorR

    defaultColorG = FloatField(default_value=0.0)
    default_colorg = defaultColorG

    defaultColorB = FloatField(default_value=0.0)
    default_colorb = defaultColorB


class DefaultColorAttrOperator(
    Float3CompoundBaseAttrOperator[DefaultColorPlugOperator]
):
    __slots__ = ()

    defaultColorR = FloatField(default_value=0.0)
    default_colorr = defaultColorR

    defaultColorG = FloatField(default_value=0.0)
    default_colorg = defaultColorG

    defaultColorB = FloatField(default_value=0.0)
    default_colorb = defaultColorB


class DefaultColorField(
    Float3CompoundBaseField[DefaultColorAttrOperator, DefaultColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DefaultColorAttrOperator
    PLUG_CLS = DefaultColorPlugOperator

    defaultColorR = FloatField(default_value=0.0)
    default_colorr = defaultColorR

    defaultColorG = FloatField(default_value=0.0)
    default_colorg = defaultColorG

    defaultColorB = FloatField(default_value=0.0)
    default_colorb = defaultColorB
