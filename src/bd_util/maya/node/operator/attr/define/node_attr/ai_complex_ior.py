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


class ReflectivityPlugOperator(
    Float3CompoundBasePlugOperator["ReflectivityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("reflectivityR", "reflectivityr"),
        ("reflectivityG", "reflectivityg"),
        ("reflectivityB", "reflectivityb"),
    )

    reflectivityR = FloatField()
    reflectivityr = reflectivityR

    reflectivityG = FloatField()
    reflectivityg = reflectivityG

    reflectivityB = FloatField()
    reflectivityb = reflectivityB


class ReflectivityAttrOperator(
    Float3CompoundBaseAttrOperator[ReflectivityPlugOperator]
):
    __slots__ = ()

    reflectivityR = FloatField()
    reflectivityr = reflectivityR

    reflectivityG = FloatField()
    reflectivityg = reflectivityG

    reflectivityB = FloatField()
    reflectivityb = reflectivityB


class ReflectivityField(
    Float3CompoundBaseField[ReflectivityAttrOperator, ReflectivityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ReflectivityAttrOperator
    PLUG_CLS = ReflectivityPlugOperator

    reflectivityR = FloatField()
    reflectivityr = reflectivityR

    reflectivityG = FloatField()
    reflectivityg = reflectivityG

    reflectivityB = FloatField()
    reflectivityb = reflectivityB


class EdgetintPlugOperator(
    Float3CompoundBasePlugOperator["EdgetintAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("edgetintR", "edgetintr"),
        ("edgetintG", "edgetintg"),
        ("edgetintB", "edgetintb"),
    )

    edgetintR = FloatField()
    edgetintr = edgetintR

    edgetintG = FloatField()
    edgetintg = edgetintG

    edgetintB = FloatField()
    edgetintb = edgetintB


class EdgetintAttrOperator(
    Float3CompoundBaseAttrOperator[EdgetintPlugOperator]
):
    __slots__ = ()

    edgetintR = FloatField()
    edgetintr = edgetintR

    edgetintG = FloatField()
    edgetintg = edgetintG

    edgetintB = FloatField()
    edgetintb = edgetintB


class EdgetintField(
    Float3CompoundBaseField[EdgetintAttrOperator, EdgetintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EdgetintAttrOperator
    PLUG_CLS = EdgetintPlugOperator

    edgetintR = FloatField()
    edgetintr = edgetintR

    edgetintG = FloatField()
    edgetintg = edgetintG

    edgetintB = FloatField()
    edgetintb = edgetintB


class NPlugOperator(
    Float3CompoundBasePlugOperator["NAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("nX", "nx"),
        ("nY", "ny"),
        ("nZ", "nz"),
    )

    nX = FloatField()
    nx = nX

    nY = FloatField()
    ny = nY

    nZ = FloatField()
    nz = nZ


class NAttrOperator(
    Float3CompoundBaseAttrOperator[NPlugOperator]
):
    __slots__ = ()

    nX = FloatField()
    nx = nX

    nY = FloatField()
    ny = nY

    nZ = FloatField()
    nz = nZ


class NField(
    Float3CompoundBaseField[NAttrOperator, NPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NAttrOperator
    PLUG_CLS = NPlugOperator

    nX = FloatField()
    nx = nX

    nY = FloatField()
    ny = nY

    nZ = FloatField()
    nz = nZ


class KPlugOperator(
    Float3CompoundBasePlugOperator["KAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("kX", "kx"),
        ("kY", "ky"),
        ("kZ", "kz"),
    )

    kX = FloatField()
    kx = kX

    kY = FloatField()
    ky = kY

    kZ = FloatField()
    kz = kZ


class KAttrOperator(
    Float3CompoundBaseAttrOperator[KPlugOperator]
):
    __slots__ = ()

    kX = FloatField()
    kx = kX

    kY = FloatField()
    ky = kY

    kZ = FloatField()
    kz = kZ


class KField(
    Float3CompoundBaseField[KAttrOperator, KPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KAttrOperator
    PLUG_CLS = KPlugOperator

    kX = FloatField()
    kx = kX

    kY = FloatField()
    ky = kY

    kZ = FloatField()
    kz = kZ
