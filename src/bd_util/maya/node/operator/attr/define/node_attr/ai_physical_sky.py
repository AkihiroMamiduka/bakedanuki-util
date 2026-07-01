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


class GroundAlbedoPlugOperator(
    Float3CompoundBasePlugOperator["GroundAlbedoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("groundAlbedoR", "ground_albedor"),
        ("groundAlbedoG", "ground_albedog"),
        ("groundAlbedoB", "ground_albedob"),
    )

    groundAlbedoR = FloatField()
    ground_albedor = groundAlbedoR

    groundAlbedoG = FloatField()
    ground_albedog = groundAlbedoG

    groundAlbedoB = FloatField()
    ground_albedob = groundAlbedoB


class GroundAlbedoAttrOperator(
    Float3CompoundBaseAttrOperator[GroundAlbedoPlugOperator]
):
    __slots__ = ()

    groundAlbedoR = FloatField()
    ground_albedor = groundAlbedoR

    groundAlbedoG = FloatField()
    ground_albedog = groundAlbedoG

    groundAlbedoB = FloatField()
    ground_albedob = groundAlbedoB


class GroundAlbedoField(
    Float3CompoundBaseField[GroundAlbedoAttrOperator, GroundAlbedoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GroundAlbedoAttrOperator
    PLUG_CLS = GroundAlbedoPlugOperator

    groundAlbedoR = FloatField()
    ground_albedor = groundAlbedoR

    groundAlbedoG = FloatField()
    ground_albedog = groundAlbedoG

    groundAlbedoB = FloatField()
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

    sunDirectionX = FloatField()
    sun_directionx = sunDirectionX

    sunDirectionY = FloatField()
    sun_directiony = sunDirectionY

    sunDirectionZ = FloatField()
    sun_directionz = sunDirectionZ


class SunDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[SunDirectionPlugOperator]
):
    __slots__ = ()

    sunDirectionX = FloatField()
    sun_directionx = sunDirectionX

    sunDirectionY = FloatField()
    sun_directiony = sunDirectionY

    sunDirectionZ = FloatField()
    sun_directionz = sunDirectionZ


class SunDirectionField(
    Float3CompoundBaseField[SunDirectionAttrOperator, SunDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SunDirectionAttrOperator
    PLUG_CLS = SunDirectionPlugOperator

    sunDirectionX = FloatField()
    sun_directionx = sunDirectionX

    sunDirectionY = FloatField()
    sun_directiony = sunDirectionY

    sunDirectionZ = FloatField()
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

    sunTintR = FloatField()
    sun_tintr = sunTintR

    sunTintG = FloatField()
    sun_tintg = sunTintG

    sunTintB = FloatField()
    sun_tintb = sunTintB


class SunTintAttrOperator(
    Float3CompoundBaseAttrOperator[SunTintPlugOperator]
):
    __slots__ = ()

    sunTintR = FloatField()
    sun_tintr = sunTintR

    sunTintG = FloatField()
    sun_tintg = sunTintG

    sunTintB = FloatField()
    sun_tintb = sunTintB


class SunTintField(
    Float3CompoundBaseField[SunTintAttrOperator, SunTintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SunTintAttrOperator
    PLUG_CLS = SunTintPlugOperator

    sunTintR = FloatField()
    sun_tintr = sunTintR

    sunTintG = FloatField()
    sun_tintg = sunTintG

    sunTintB = FloatField()
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

    skyTintR = FloatField()
    sky_tintr = skyTintR

    skyTintG = FloatField()
    sky_tintg = skyTintG

    skyTintB = FloatField()
    sky_tintb = skyTintB


class SkyTintAttrOperator(
    Float3CompoundBaseAttrOperator[SkyTintPlugOperator]
):
    __slots__ = ()

    skyTintR = FloatField()
    sky_tintr = skyTintR

    skyTintG = FloatField()
    sky_tintg = skyTintG

    skyTintB = FloatField()
    sky_tintb = skyTintB


class SkyTintField(
    Float3CompoundBaseField[SkyTintAttrOperator, SkyTintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SkyTintAttrOperator
    PLUG_CLS = SkyTintPlugOperator

    skyTintR = FloatField()
    sky_tintr = skyTintR

    skyTintG = FloatField()
    sky_tintg = skyTintG

    skyTintB = FloatField()
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

    XX = FloatField()
    Xx = XX

    XY = FloatField()
    Xy = XY

    XZ = FloatField()
    Xz = XZ


class XAttrOperator(
    Float3CompoundBaseAttrOperator[XPlugOperator]
):
    __slots__ = ()

    XX = FloatField()
    Xx = XX

    XY = FloatField()
    Xy = XY

    XZ = FloatField()
    Xz = XZ


class XField(
    Float3CompoundBaseField[XAttrOperator, XPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = XAttrOperator
    PLUG_CLS = XPlugOperator

    XX = FloatField()
    Xx = XX

    XY = FloatField()
    Xy = XY

    XZ = FloatField()
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

    YX = FloatField()
    Yx = YX

    YY = FloatField()
    Yy = YY

    YZ = FloatField()
    Yz = YZ


class YAttrOperator(
    Float3CompoundBaseAttrOperator[YPlugOperator]
):
    __slots__ = ()

    YX = FloatField()
    Yx = YX

    YY = FloatField()
    Yy = YY

    YZ = FloatField()
    Yz = YZ


class YField(
    Float3CompoundBaseField[YAttrOperator, YPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = YAttrOperator
    PLUG_CLS = YPlugOperator

    YX = FloatField()
    Yx = YX

    YY = FloatField()
    Yy = YY

    YZ = FloatField()
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

    ZX = FloatField()
    Zx = ZX

    ZY = FloatField()
    Zy = ZY

    ZZ = FloatField()
    Zz = ZZ


class ZAttrOperator(
    Float3CompoundBaseAttrOperator[ZPlugOperator]
):
    __slots__ = ()

    ZX = FloatField()
    Zx = ZX

    ZY = FloatField()
    Zy = ZY

    ZZ = FloatField()
    Zz = ZZ


class ZField(
    Float3CompoundBaseField[ZAttrOperator, ZPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ZAttrOperator
    PLUG_CLS = ZPlugOperator

    ZX = FloatField()
    Zx = ZX

    ZY = FloatField()
    Zy = ZY

    ZZ = FloatField()
    Zz = ZZ
