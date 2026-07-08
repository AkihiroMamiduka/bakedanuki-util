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


class GroundAlbedoPlugOperator(
    Float3CompoundBasePlugOperator["GroundAlbedoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("groundAlbedoR", "ground_albedor"),
        ("groundAlbedoG", "ground_albedog"),
        ("groundAlbedoB", "ground_albedob"),
    )

    groundAlbedoR = FloatField(default_value=0.10000000149011612)
    ground_albedor = groundAlbedoR

    groundAlbedoG = FloatField(default_value=0.10000000149011612)
    ground_albedog = groundAlbedoG

    groundAlbedoB = FloatField(default_value=0.10000000149011612)
    ground_albedob = groundAlbedoB


class GroundAlbedoAttrOperator(
    Float3CompoundBaseAttrOperator[GroundAlbedoPlugOperator]
):
    __slots__ = ()

    groundAlbedoR = FloatField(default_value=0.10000000149011612)
    ground_albedor = groundAlbedoR

    groundAlbedoG = FloatField(default_value=0.10000000149011612)
    ground_albedog = groundAlbedoG

    groundAlbedoB = FloatField(default_value=0.10000000149011612)
    ground_albedob = groundAlbedoB


class GroundAlbedoField(
    Float3CompoundBaseField[GroundAlbedoAttrOperator, GroundAlbedoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GroundAlbedoAttrOperator
    PLUG_CLS = GroundAlbedoPlugOperator

    groundAlbedoR = FloatField(default_value=0.10000000149011612)
    ground_albedor = groundAlbedoR

    groundAlbedoG = FloatField(default_value=0.10000000149011612)
    ground_albedog = groundAlbedoG

    groundAlbedoB = FloatField(default_value=0.10000000149011612)
    ground_albedob = groundAlbedoB


class SunDirectionPlugOperator(
    Float3CompoundBasePlugOperator["SunDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sunDirectionX", "sun_directionx"),
        ("sunDirectionY", "sun_directiony"),
        ("sunDirectionZ", "sun_directionz"),
    )

    sunDirectionX = FloatField(default_value=0.0)
    sun_directionx = sunDirectionX

    sunDirectionY = FloatField(default_value=1.0)
    sun_directiony = sunDirectionY

    sunDirectionZ = FloatField(default_value=0.0)
    sun_directionz = sunDirectionZ


class SunDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[SunDirectionPlugOperator]
):
    __slots__ = ()

    sunDirectionX = FloatField(default_value=0.0)
    sun_directionx = sunDirectionX

    sunDirectionY = FloatField(default_value=1.0)
    sun_directiony = sunDirectionY

    sunDirectionZ = FloatField(default_value=0.0)
    sun_directionz = sunDirectionZ


class SunDirectionField(
    Float3CompoundBaseField[SunDirectionAttrOperator, SunDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SunDirectionAttrOperator
    PLUG_CLS = SunDirectionPlugOperator

    sunDirectionX = FloatField(default_value=0.0)
    sun_directionx = sunDirectionX

    sunDirectionY = FloatField(default_value=1.0)
    sun_directiony = sunDirectionY

    sunDirectionZ = FloatField(default_value=0.0)
    sun_directionz = sunDirectionZ


class SunTintPlugOperator(
    Float3CompoundBasePlugOperator["SunTintAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sunTintR", "sun_tintr"),
        ("sunTintG", "sun_tintg"),
        ("sunTintB", "sun_tintb"),
    )

    sunTintR = FloatField(default_value=1.0)
    sun_tintr = sunTintR

    sunTintG = FloatField(default_value=1.0)
    sun_tintg = sunTintG

    sunTintB = FloatField(default_value=1.0)
    sun_tintb = sunTintB


class SunTintAttrOperator(
    Float3CompoundBaseAttrOperator[SunTintPlugOperator]
):
    __slots__ = ()

    sunTintR = FloatField(default_value=1.0)
    sun_tintr = sunTintR

    sunTintG = FloatField(default_value=1.0)
    sun_tintg = sunTintG

    sunTintB = FloatField(default_value=1.0)
    sun_tintb = sunTintB


class SunTintField(
    Float3CompoundBaseField[SunTintAttrOperator, SunTintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SunTintAttrOperator
    PLUG_CLS = SunTintPlugOperator

    sunTintR = FloatField(default_value=1.0)
    sun_tintr = sunTintR

    sunTintG = FloatField(default_value=1.0)
    sun_tintg = sunTintG

    sunTintB = FloatField(default_value=1.0)
    sun_tintb = sunTintB


class SkyTintPlugOperator(
    Float3CompoundBasePlugOperator["SkyTintAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("skyTintR", "sky_tintr"),
        ("skyTintG", "sky_tintg"),
        ("skyTintB", "sky_tintb"),
    )

    skyTintR = FloatField(default_value=1.0)
    sky_tintr = skyTintR

    skyTintG = FloatField(default_value=1.0)
    sky_tintg = skyTintG

    skyTintB = FloatField(default_value=1.0)
    sky_tintb = skyTintB


class SkyTintAttrOperator(
    Float3CompoundBaseAttrOperator[SkyTintPlugOperator]
):
    __slots__ = ()

    skyTintR = FloatField(default_value=1.0)
    sky_tintr = skyTintR

    skyTintG = FloatField(default_value=1.0)
    sky_tintg = skyTintG

    skyTintB = FloatField(default_value=1.0)
    sky_tintb = skyTintB


class SkyTintField(
    Float3CompoundBaseField[SkyTintAttrOperator, SkyTintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SkyTintAttrOperator
    PLUG_CLS = SkyTintPlugOperator

    skyTintR = FloatField(default_value=1.0)
    sky_tintr = skyTintR

    skyTintG = FloatField(default_value=1.0)
    sky_tintg = skyTintG

    skyTintB = FloatField(default_value=1.0)
    sky_tintb = skyTintB


class XPlugOperator(
    Float3CompoundBasePlugOperator["XAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("XX", "Xx"),
        ("XY", "Xy"),
        ("XZ", "Xz"),
    )

    XX = FloatField(default_value=1.0)
    Xx = XX

    XY = FloatField(default_value=0.0)
    Xy = XY

    XZ = FloatField(default_value=0.0)
    Xz = XZ


class XAttrOperator(
    Float3CompoundBaseAttrOperator[XPlugOperator]
):
    __slots__ = ()

    XX = FloatField(default_value=1.0)
    Xx = XX

    XY = FloatField(default_value=0.0)
    Xy = XY

    XZ = FloatField(default_value=0.0)
    Xz = XZ


class XField(
    Float3CompoundBaseField[XAttrOperator, XPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = XAttrOperator
    PLUG_CLS = XPlugOperator

    XX = FloatField(default_value=1.0)
    Xx = XX

    XY = FloatField(default_value=0.0)
    Xy = XY

    XZ = FloatField(default_value=0.0)
    Xz = XZ


class YPlugOperator(
    Float3CompoundBasePlugOperator["YAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("YX", "Yx"),
        ("YY", "Yy"),
        ("YZ", "Yz"),
    )

    YX = FloatField(default_value=0.0)
    Yx = YX

    YY = FloatField(default_value=1.0)
    Yy = YY

    YZ = FloatField(default_value=0.0)
    Yz = YZ


class YAttrOperator(
    Float3CompoundBaseAttrOperator[YPlugOperator]
):
    __slots__ = ()

    YX = FloatField(default_value=0.0)
    Yx = YX

    YY = FloatField(default_value=1.0)
    Yy = YY

    YZ = FloatField(default_value=0.0)
    Yz = YZ


class YField(
    Float3CompoundBaseField[YAttrOperator, YPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = YAttrOperator
    PLUG_CLS = YPlugOperator

    YX = FloatField(default_value=0.0)
    Yx = YX

    YY = FloatField(default_value=1.0)
    Yy = YY

    YZ = FloatField(default_value=0.0)
    Yz = YZ


class ZPlugOperator(
    Float3CompoundBasePlugOperator["ZAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ZX", "Zx"),
        ("ZY", "Zy"),
        ("ZZ", "Zz"),
    )

    ZX = FloatField(default_value=0.0)
    Zx = ZX

    ZY = FloatField(default_value=0.0)
    Zy = ZY

    ZZ = FloatField(default_value=1.0)
    Zz = ZZ


class ZAttrOperator(
    Float3CompoundBaseAttrOperator[ZPlugOperator]
):
    __slots__ = ()

    ZX = FloatField(default_value=0.0)
    Zx = ZX

    ZY = FloatField(default_value=0.0)
    Zy = ZY

    ZZ = FloatField(default_value=1.0)
    Zz = ZZ


class ZField(
    Float3CompoundBaseField[ZAttrOperator, ZPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ZAttrOperator
    PLUG_CLS = ZPlugOperator

    ZX = FloatField(default_value=0.0)
    Zx = ZX

    ZY = FloatField(default_value=0.0)
    Zy = ZY

    ZZ = FloatField(default_value=1.0)
    Zz = ZZ
