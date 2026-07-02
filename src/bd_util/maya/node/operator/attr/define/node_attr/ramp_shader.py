# coding: utf-8

from ..std.at.addr import AddrField
from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.light_data import (
    LightDataAttrOperator,
    LightDataPlugOperator,
    LightDataField,
)
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class Color_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Color_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class Color_InterpEnumField(
    EnumField[Color_InterpEnumAttrOperator, Color_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Color_InterpEnumAttrOperator
    PLUG_CLS = Color_InterpEnumPlugOperator


class Transparency_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Transparency_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class Transparency_InterpEnumField(
    EnumField[Transparency_InterpEnumAttrOperator, Transparency_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Transparency_InterpEnumAttrOperator
    PLUG_CLS = Transparency_InterpEnumPlugOperator


class Incandescence_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Incandescence_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class Incandescence_InterpEnumField(
    EnumField[Incandescence_InterpEnumAttrOperator, Incandescence_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Incandescence_InterpEnumAttrOperator
    PLUG_CLS = Incandescence_InterpEnumPlugOperator


class SpecularRollOff_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class SpecularRollOff_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class SpecularRollOff_InterpEnumField(
    EnumField[SpecularRollOff_InterpEnumAttrOperator, SpecularRollOff_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularRollOff_InterpEnumAttrOperator
    PLUG_CLS = SpecularRollOff_InterpEnumPlugOperator


class SpecularColor_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class SpecularColor_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class SpecularColor_InterpEnumField(
    EnumField[SpecularColor_InterpEnumAttrOperator, SpecularColor_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularColor_InterpEnumAttrOperator
    PLUG_CLS = SpecularColor_InterpEnumPlugOperator


class Reflectivity_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Reflectivity_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class Reflectivity_InterpEnumField(
    EnumField[Reflectivity_InterpEnumAttrOperator, Reflectivity_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Reflectivity_InterpEnumAttrOperator
    PLUG_CLS = Reflectivity_InterpEnumPlugOperator


class Environment_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Environment_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class Environment_InterpEnumField(
    EnumField[Environment_InterpEnumAttrOperator, Environment_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Environment_InterpEnumAttrOperator
    PLUG_CLS = Environment_InterpEnumPlugOperator


class RayDirectionPlugOperator(
    Float3CompoundBasePlugOperator["RayDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rayDirectionX", "rdx"),
        ("rayDirectionY", "rdy"),
        ("rayDirectionZ", "rdz"),
    )

    rayDirectionX = FloatField()
    rdx = rayDirectionX

    rayDirectionY = FloatField()
    rdy = rayDirectionY

    rayDirectionZ = FloatField()
    rdz = rayDirectionZ


class RayDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[RayDirectionPlugOperator]
):
    __slots__ = ()

    rayDirectionX = FloatField()
    rdx = rayDirectionX

    rayDirectionY = FloatField()
    rdy = rayDirectionY

    rayDirectionZ = FloatField()
    rdz = rayDirectionZ


class RayDirectionField(
    Float3CompoundBaseField[RayDirectionAttrOperator, RayDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RayDirectionAttrOperator
    PLUG_CLS = RayDirectionPlugOperator

    rayDirectionX = FloatField()
    rdx = rayDirectionX

    rayDirectionY = FloatField()
    rdy = rayDirectionY

    rayDirectionZ = FloatField()
    rdz = rayDirectionZ


class ColorPlugOperator(
    CompoundPlugOperator["ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("color_Position", "clrp"),
        ("color_Color", "clrc"),
        ("color_Interp", "clri"),
    )

    color_Position = FloatField()
    clrp = color_Position

    color_Color = Float3Field()
    clrc = color_Color

    color_Interp = Color_InterpEnumField()
    clri = color_Interp


class ColorAttrOperator(
    CompoundAttrOperator[ColorPlugOperator]
):
    __slots__ = ()

    color_Position = FloatField()
    clrp = color_Position

    color_Color = Float3Field()
    clrc = color_Color

    color_Interp = Color_InterpEnumField()
    clri = color_Interp


class ColorField(
    CompoundField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator


class ShadowColorPlugOperator(
    Float3CompoundBasePlugOperator["ShadowColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shadowColorR", "shr"),
        ("shadowColorG", "shg"),
        ("shadowColorB", "shb"),
    )

    shadowColorR = FloatField()
    shr = shadowColorR

    shadowColorG = FloatField()
    shg = shadowColorG

    shadowColorB = FloatField()
    shb = shadowColorB


class ShadowColorAttrOperator(
    Float3CompoundBaseAttrOperator[ShadowColorPlugOperator]
):
    __slots__ = ()

    shadowColorR = FloatField()
    shr = shadowColorR

    shadowColorG = FloatField()
    shg = shadowColorG

    shadowColorB = FloatField()
    shb = shadowColorB


class ShadowColorField(
    Float3CompoundBaseField[ShadowColorAttrOperator, ShadowColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShadowColorAttrOperator
    PLUG_CLS = ShadowColorPlugOperator

    shadowColorR = FloatField()
    shr = shadowColorR

    shadowColorG = FloatField()
    shg = shadowColorG

    shadowColorB = FloatField()
    shb = shadowColorB


class TransparencyPlugOperator(
    CompoundPlugOperator["TransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transparency_Position", "itp"),
        ("transparency_Color", "itc"),
        ("transparency_Interp", "iti"),
    )

    transparency_Position = FloatField()
    itp = transparency_Position

    transparency_Color = Float3Field()
    itc = transparency_Color

    transparency_Interp = Transparency_InterpEnumField()
    iti = transparency_Interp


class TransparencyAttrOperator(
    CompoundAttrOperator[TransparencyPlugOperator]
):
    __slots__ = ()

    transparency_Position = FloatField()
    itp = transparency_Position

    transparency_Color = Float3Field()
    itc = transparency_Color

    transparency_Interp = Transparency_InterpEnumField()
    iti = transparency_Interp


class TransparencyField(
    CompoundField[TransparencyAttrOperator, TransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencyAttrOperator
    PLUG_CLS = TransparencyPlugOperator


class AmbientColorPlugOperator(
    Float3CompoundBasePlugOperator["AmbientColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ambientColorR", "acr"),
        ("ambientColorG", "acg"),
        ("ambientColorB", "acb"),
    )

    ambientColorR = FloatField()
    acr = ambientColorR

    ambientColorG = FloatField()
    acg = ambientColorG

    ambientColorB = FloatField()
    acb = ambientColorB


class AmbientColorAttrOperator(
    Float3CompoundBaseAttrOperator[AmbientColorPlugOperator]
):
    __slots__ = ()

    ambientColorR = FloatField()
    acr = ambientColorR

    ambientColorG = FloatField()
    acg = ambientColorG

    ambientColorB = FloatField()
    acb = ambientColorB


class AmbientColorField(
    Float3CompoundBaseField[AmbientColorAttrOperator, AmbientColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AmbientColorAttrOperator
    PLUG_CLS = AmbientColorPlugOperator

    ambientColorR = FloatField()
    acr = ambientColorR

    ambientColorG = FloatField()
    acg = ambientColorG

    ambientColorB = FloatField()
    acb = ambientColorB


class IncandescencePlugOperator(
    CompoundPlugOperator["IncandescenceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("incandescence_Position", "icp"),
        ("incandescence_Color", "icc"),
        ("incandescence_Interp", "ici"),
    )

    incandescence_Position = FloatField()
    icp = incandescence_Position

    incandescence_Color = Float3Field()
    icc = incandescence_Color

    incandescence_Interp = Incandescence_InterpEnumField()
    ici = incandescence_Interp


class IncandescenceAttrOperator(
    CompoundAttrOperator[IncandescencePlugOperator]
):
    __slots__ = ()

    incandescence_Position = FloatField()
    icp = incandescence_Position

    incandescence_Color = Float3Field()
    icc = incandescence_Color

    incandescence_Interp = Incandescence_InterpEnumField()
    ici = incandescence_Interp


class IncandescenceField(
    CompoundField[IncandescenceAttrOperator, IncandescencePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IncandescenceAttrOperator
    PLUG_CLS = IncandescencePlugOperator


class SpecularRollOffPlugOperator(
    CompoundPlugOperator["SpecularRollOffAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularRollOff_Position", "srop"),
        ("specularRollOff_FloatValue", "srofv"),
        ("specularRollOff_Interp", "sroi"),
    )

    specularRollOff_Position = FloatField()
    srop = specularRollOff_Position

    specularRollOff_FloatValue = FloatField()
    srofv = specularRollOff_FloatValue

    specularRollOff_Interp = SpecularRollOff_InterpEnumField()
    sroi = specularRollOff_Interp


class SpecularRollOffAttrOperator(
    CompoundAttrOperator[SpecularRollOffPlugOperator]
):
    __slots__ = ()

    specularRollOff_Position = FloatField()
    srop = specularRollOff_Position

    specularRollOff_FloatValue = FloatField()
    srofv = specularRollOff_FloatValue

    specularRollOff_Interp = SpecularRollOff_InterpEnumField()
    sroi = specularRollOff_Interp


class SpecularRollOffField(
    CompoundField[SpecularRollOffAttrOperator, SpecularRollOffPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularRollOffAttrOperator
    PLUG_CLS = SpecularRollOffPlugOperator


class SpecularColorPlugOperator(
    CompoundPlugOperator["SpecularColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularColor_Position", "scp"),
        ("specularColor_Color", "scc"),
        ("specularColor_Interp", "sci"),
    )

    specularColor_Position = FloatField()
    scp = specularColor_Position

    specularColor_Color = Float3Field()
    scc = specularColor_Color

    specularColor_Interp = SpecularColor_InterpEnumField()
    sci = specularColor_Interp


class SpecularColorAttrOperator(
    CompoundAttrOperator[SpecularColorPlugOperator]
):
    __slots__ = ()

    specularColor_Position = FloatField()
    scp = specularColor_Position

    specularColor_Color = Float3Field()
    scc = specularColor_Color

    specularColor_Interp = SpecularColor_InterpEnumField()
    sci = specularColor_Interp


class SpecularColorField(
    CompoundField[SpecularColorAttrOperator, SpecularColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularColorAttrOperator
    PLUG_CLS = SpecularColorPlugOperator


class ReflectivityPlugOperator(
    CompoundPlugOperator["ReflectivityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("reflectivity_Position", "rflp"),
        ("reflectivity_FloatValue", "rflfv"),
        ("reflectivity_Interp", "rfli"),
    )

    reflectivity_Position = FloatField()
    rflp = reflectivity_Position

    reflectivity_FloatValue = FloatField()
    rflfv = reflectivity_FloatValue

    reflectivity_Interp = Reflectivity_InterpEnumField()
    rfli = reflectivity_Interp


class ReflectivityAttrOperator(
    CompoundAttrOperator[ReflectivityPlugOperator]
):
    __slots__ = ()

    reflectivity_Position = FloatField()
    rflp = reflectivity_Position

    reflectivity_FloatValue = FloatField()
    rflfv = reflectivity_FloatValue

    reflectivity_Interp = Reflectivity_InterpEnumField()
    rfli = reflectivity_Interp


class ReflectivityField(
    CompoundField[ReflectivityAttrOperator, ReflectivityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ReflectivityAttrOperator
    PLUG_CLS = ReflectivityPlugOperator


class EnvironmentPlugOperator(
    CompoundPlugOperator["EnvironmentAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("environment_Position", "envp"),
        ("environment_Color", "envc"),
        ("environment_Interp", "envi"),
    )

    environment_Position = FloatField()
    envp = environment_Position

    environment_Color = Float3Field()
    envc = environment_Color

    environment_Interp = Environment_InterpEnumField()
    envi = environment_Interp


class EnvironmentAttrOperator(
    CompoundAttrOperator[EnvironmentPlugOperator]
):
    __slots__ = ()

    environment_Position = FloatField()
    envp = environment_Position

    environment_Color = Float3Field()
    envc = environment_Color

    environment_Interp = Environment_InterpEnumField()
    envi = environment_Interp


class EnvironmentField(
    CompoundField[EnvironmentAttrOperator, EnvironmentPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EnvironmentAttrOperator
    PLUG_CLS = EnvironmentPlugOperator


class ReflectedColorPlugOperator(
    Float3CompoundBasePlugOperator["ReflectedColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("reflectedColorR", "rr"),
        ("reflectedColorG", "rg"),
        ("reflectedColorB", "rb"),
    )

    reflectedColorR = FloatField()
    rr = reflectedColorR

    reflectedColorG = FloatField()
    rg = reflectedColorG

    reflectedColorB = FloatField()
    rb = reflectedColorB


class ReflectedColorAttrOperator(
    Float3CompoundBaseAttrOperator[ReflectedColorPlugOperator]
):
    __slots__ = ()

    reflectedColorR = FloatField()
    rr = reflectedColorR

    reflectedColorG = FloatField()
    rg = reflectedColorG

    reflectedColorB = FloatField()
    rb = reflectedColorB


class ReflectedColorField(
    Float3CompoundBaseField[ReflectedColorAttrOperator, ReflectedColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ReflectedColorAttrOperator
    PLUG_CLS = ReflectedColorPlugOperator

    reflectedColorR = FloatField()
    rr = reflectedColorR

    reflectedColorG = FloatField()
    rg = reflectedColorG

    reflectedColorB = FloatField()
    rb = reflectedColorB


class TriangleNormalCameraPlugOperator(
    Float3CompoundBasePlugOperator["TriangleNormalCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("triangleNormalCameraX", "tnx"),
        ("triangleNormalCameraY", "tny"),
        ("triangleNormalCameraZ", "tnz"),
    )

    triangleNormalCameraX = FloatField()
    tnx = triangleNormalCameraX

    triangleNormalCameraY = FloatField()
    tny = triangleNormalCameraY

    triangleNormalCameraZ = FloatField()
    tnz = triangleNormalCameraZ


class TriangleNormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[TriangleNormalCameraPlugOperator]
):
    __slots__ = ()

    triangleNormalCameraX = FloatField()
    tnx = triangleNormalCameraX

    triangleNormalCameraY = FloatField()
    tny = triangleNormalCameraY

    triangleNormalCameraZ = FloatField()
    tnz = triangleNormalCameraZ


class TriangleNormalCameraField(
    Float3CompoundBaseField[TriangleNormalCameraAttrOperator, TriangleNormalCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TriangleNormalCameraAttrOperator
    PLUG_CLS = TriangleNormalCameraPlugOperator

    triangleNormalCameraX = FloatField()
    tnx = triangleNormalCameraX

    triangleNormalCameraY = FloatField()
    tny = triangleNormalCameraY

    triangleNormalCameraZ = FloatField()
    tnz = triangleNormalCameraZ


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


class OutGlowColorPlugOperator(
    Float3CompoundBasePlugOperator["OutGlowColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outGlowColorR", "ogr"),
        ("outGlowColorG", "ogg"),
        ("outGlowColorB", "ogb"),
    )

    outGlowColorR = FloatField()
    ogr = outGlowColorR

    outGlowColorG = FloatField()
    ogg = outGlowColorG

    outGlowColorB = FloatField()
    ogb = outGlowColorB


class OutGlowColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutGlowColorPlugOperator]
):
    __slots__ = ()

    outGlowColorR = FloatField()
    ogr = outGlowColorR

    outGlowColorG = FloatField()
    ogg = outGlowColorG

    outGlowColorB = FloatField()
    ogb = outGlowColorB


class OutGlowColorField(
    Float3CompoundBaseField[OutGlowColorAttrOperator, OutGlowColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutGlowColorAttrOperator
    PLUG_CLS = OutGlowColorPlugOperator

    outGlowColorR = FloatField()
    ogr = outGlowColorR

    outGlowColorG = FloatField()
    ogg = outGlowColorG

    outGlowColorB = FloatField()
    ogb = outGlowColorB


class PointCameraPlugOperator(
    Float3CompoundBasePlugOperator["PointCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointCameraX", "px"),
        ("pointCameraY", "py"),
        ("pointCameraZ", "pz"),
    )

    pointCameraX = FloatField()
    px = pointCameraX

    pointCameraY = FloatField()
    py = pointCameraY

    pointCameraZ = FloatField()
    pz = pointCameraZ


class PointCameraAttrOperator(
    Float3CompoundBaseAttrOperator[PointCameraPlugOperator]
):
    __slots__ = ()

    pointCameraX = FloatField()
    px = pointCameraX

    pointCameraY = FloatField()
    py = pointCameraY

    pointCameraZ = FloatField()
    pz = pointCameraZ


class PointCameraField(
    Float3CompoundBaseField[PointCameraAttrOperator, PointCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointCameraAttrOperator
    PLUG_CLS = PointCameraPlugOperator

    pointCameraX = FloatField()
    px = pointCameraX

    pointCameraY = FloatField()
    py = pointCameraY

    pointCameraZ = FloatField()
    pz = pointCameraZ


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


class LightDataArrayPlugOperator(
    LightDataPlugOperator["LightDataArrayAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightDirection", "ld"),
        ("lightIntensity", "li"),
        ("lightAmbient", "la"),
        ("lightDiffuse", "ldf"),
        ("lightSpecular", "ls"),
        ("lightShadowFraction", "lsf"),
        ("preShadowIntensity", "psi"),
        ("lightBlindData", "lbd"),
    )

    lightDirection = Float3Field()
    ld = lightDirection

    lightIntensity = Float3Field()
    li = lightIntensity

    lightAmbient = BoolField()
    la = lightAmbient

    lightDiffuse = BoolField()
    ldf = lightDiffuse

    lightSpecular = BoolField()
    ls = lightSpecular

    lightShadowFraction = FloatField()
    lsf = lightShadowFraction

    preShadowIntensity = FloatField()
    psi = preShadowIntensity

    lightBlindData = AddrField()
    lbd = lightBlindData


class LightDataArrayAttrOperator(
    LightDataAttrOperator[LightDataArrayPlugOperator]
):
    __slots__ = ()

    lightDirection = Float3Field()
    ld = lightDirection

    lightIntensity = Float3Field()
    li = lightIntensity

    lightAmbient = BoolField()
    la = lightAmbient

    lightDiffuse = BoolField()
    ldf = lightDiffuse

    lightSpecular = BoolField()
    ls = lightSpecular

    lightShadowFraction = FloatField()
    lsf = lightShadowFraction

    preShadowIntensity = FloatField()
    psi = preShadowIntensity

    lightBlindData = AddrField()
    lbd = lightBlindData


class LightDataArrayField(
    LightDataField[LightDataArrayAttrOperator, LightDataArrayPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightDataArrayAttrOperator
    PLUG_CLS = LightDataArrayPlugOperator


class OutMatteOpacityPlugOperator(
    Float3CompoundBasePlugOperator["OutMatteOpacityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outMatteOpacityR", "omor"),
        ("outMatteOpacityG", "omog"),
        ("outMatteOpacityB", "omob"),
    )

    outMatteOpacityR = FloatField()
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField()
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField()
    omob = outMatteOpacityB


class OutMatteOpacityAttrOperator(
    Float3CompoundBaseAttrOperator[OutMatteOpacityPlugOperator]
):
    __slots__ = ()

    outMatteOpacityR = FloatField()
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField()
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField()
    omob = outMatteOpacityB


class OutMatteOpacityField(
    Float3CompoundBaseField[OutMatteOpacityAttrOperator, OutMatteOpacityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutMatteOpacityAttrOperator
    PLUG_CLS = OutMatteOpacityPlugOperator

    outMatteOpacityR = FloatField()
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField()
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField()
    omob = outMatteOpacityB
