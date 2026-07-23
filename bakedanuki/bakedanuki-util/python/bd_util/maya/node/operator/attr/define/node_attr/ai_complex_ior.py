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
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
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


class ReflectivityPlugOperator(
    Float3CompoundBasePlugOperator["ReflectivityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("reflectivityR", "reflectivityr"),
        ("reflectivityG", "reflectivityg"),
        ("reflectivityB", "reflectivityb"),
    )

    reflectivityR = FloatField(default_value=0.9259520173072815)
    reflectivityr = reflectivityR

    reflectivityG = FloatField(default_value=0.7208870053291321)
    reflectivityg = reflectivityG

    reflectivityB = FloatField(default_value=0.5041540265083313)
    reflectivityb = reflectivityB


class ReflectivityAttrOperator(
    Float3CompoundBaseAttrOperator[ReflectivityPlugOperator]
):
    __slots__ = ()

    reflectivityR = FloatField(default_value=0.9259520173072815)
    reflectivityr = reflectivityR

    reflectivityG = FloatField(default_value=0.7208870053291321)
    reflectivityg = reflectivityG

    reflectivityB = FloatField(default_value=0.5041540265083313)
    reflectivityb = reflectivityB


class ReflectivityField(
    Float3CompoundBaseField[ReflectivityAttrOperator, ReflectivityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ReflectivityAttrOperator
    PLUG_CLS = ReflectivityPlugOperator

    reflectivityR = FloatField(default_value=0.9259520173072815)
    reflectivityr = reflectivityR

    reflectivityG = FloatField(default_value=0.7208870053291321)
    reflectivityg = reflectivityG

    reflectivityB = FloatField(default_value=0.5041540265083313)
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

    edgetintR = FloatField(default_value=0.995523989200592)
    edgetintr = edgetintR

    edgetintG = FloatField(default_value=0.957414984703064)
    edgetintg = edgetintG

    edgetintB = FloatField(default_value=0.8227760195732117)
    edgetintb = edgetintB


class EdgetintAttrOperator(
    Float3CompoundBaseAttrOperator[EdgetintPlugOperator]
):
    __slots__ = ()

    edgetintR = FloatField(default_value=0.995523989200592)
    edgetintr = edgetintR

    edgetintG = FloatField(default_value=0.957414984703064)
    edgetintg = edgetintG

    edgetintB = FloatField(default_value=0.8227760195732117)
    edgetintb = edgetintB


class EdgetintField(
    Float3CompoundBaseField[EdgetintAttrOperator, EdgetintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EdgetintAttrOperator
    PLUG_CLS = EdgetintPlugOperator

    edgetintR = FloatField(default_value=0.995523989200592)
    edgetintr = edgetintR

    edgetintG = FloatField(default_value=0.957414984703064)
    edgetintg = edgetintG

    edgetintB = FloatField(default_value=0.8227760195732117)
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

    nX = FloatField(default_value=0.27105000615119934)
    nx = nX

    nY = FloatField(default_value=0.6769300103187561)
    ny = nY

    nZ = FloatField(default_value=1.3164000511169434)
    nz = nZ


class NAttrOperator(
    Float3CompoundBaseAttrOperator[NPlugOperator]
):
    __slots__ = ()

    nX = FloatField(default_value=0.27105000615119934)
    nx = nX

    nY = FloatField(default_value=0.6769300103187561)
    ny = nY

    nZ = FloatField(default_value=1.3164000511169434)
    nz = nZ


class NField(
    Float3CompoundBaseField[NAttrOperator, NPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NAttrOperator
    PLUG_CLS = NPlugOperator

    nX = FloatField(default_value=0.27105000615119934)
    nx = nX

    nY = FloatField(default_value=0.6769300103187561)
    ny = nY

    nZ = FloatField(default_value=1.3164000511169434)
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

    kX = FloatField(default_value=3.6092000007629395)
    kx = kX

    kY = FloatField(default_value=2.6247000694274902)
    ky = kY

    kZ = FloatField(default_value=2.292099952697754)
    kz = kZ


class KAttrOperator(
    Float3CompoundBaseAttrOperator[KPlugOperator]
):
    __slots__ = ()

    kX = FloatField(default_value=3.6092000007629395)
    kx = kX

    kY = FloatField(default_value=2.6247000694274902)
    ky = kY

    kZ = FloatField(default_value=2.292099952697754)
    kz = kZ


class KField(
    Float3CompoundBaseField[KAttrOperator, KPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KAttrOperator
    PLUG_CLS = KPlugOperator

    kX = FloatField(default_value=3.6092000007629395)
    kx = kX

    kY = FloatField(default_value=2.6247000694274902)
    ky = kY

    kZ = FloatField(default_value=2.292099952697754)
    kz = kZ
