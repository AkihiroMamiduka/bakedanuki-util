# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class LeafCurl_InterpEnumPlugOperator(EnumPlugOperator["LeafCurl_InterpEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class LeafCurl_InterpEnumAttrOperator(EnumAttrOperator[LeafCurl_InterpEnumPlugOperator]):
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


class LeafCurl_InterpEnumField(
    EnumField[LeafCurl_InterpEnumAttrOperator, LeafCurl_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafCurl_InterpEnumAttrOperator
    PLUG_CLS = LeafCurl_InterpEnumPlugOperator


class PetalCurl_InterpEnumPlugOperator(EnumPlugOperator["PetalCurl_InterpEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class PetalCurl_InterpEnumAttrOperator(EnumAttrOperator[PetalCurl_InterpEnumPlugOperator]):
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


class PetalCurl_InterpEnumField(
    EnumField[PetalCurl_InterpEnumAttrOperator, PetalCurl_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PetalCurl_InterpEnumAttrOperator
    PLUG_CLS = PetalCurl_InterpEnumPlugOperator


class WidthScale_InterpEnumPlugOperator(EnumPlugOperator["WidthScale_InterpEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class WidthScale_InterpEnumAttrOperator(EnumAttrOperator[WidthScale_InterpEnumPlugOperator]):
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


class WidthScale_InterpEnumField(
    EnumField[WidthScale_InterpEnumAttrOperator, WidthScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WidthScale_InterpEnumAttrOperator
    PLUG_CLS = WidthScale_InterpEnumPlugOperator


class LeafWidthScale_InterpEnumPlugOperator(EnumPlugOperator["LeafWidthScale_InterpEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class LeafWidthScale_InterpEnumAttrOperator(EnumAttrOperator[LeafWidthScale_InterpEnumPlugOperator]):
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


class LeafWidthScale_InterpEnumField(
    EnumField[LeafWidthScale_InterpEnumAttrOperator, LeafWidthScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafWidthScale_InterpEnumAttrOperator
    PLUG_CLS = LeafWidthScale_InterpEnumPlugOperator


class PetalWidthScale_InterpEnumPlugOperator(EnumPlugOperator["PetalWidthScale_InterpEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class PetalWidthScale_InterpEnumAttrOperator(EnumAttrOperator[PetalWidthScale_InterpEnumPlugOperator]):
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


class PetalWidthScale_InterpEnumField(
    EnumField[PetalWidthScale_InterpEnumAttrOperator, PetalWidthScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PetalWidthScale_InterpEnumAttrOperator
    PLUG_CLS = PetalWidthScale_InterpEnumPlugOperator


class TwigLengthScale_InterpEnumPlugOperator(EnumPlugOperator["TwigLengthScale_InterpEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class TwigLengthScale_InterpEnumAttrOperator(EnumAttrOperator[TwigLengthScale_InterpEnumPlugOperator]):
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


class TwigLengthScale_InterpEnumField(
    EnumField[TwigLengthScale_InterpEnumAttrOperator, TwigLengthScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TwigLengthScale_InterpEnumAttrOperator
    PLUG_CLS = TwigLengthScale_InterpEnumPlugOperator


class Environment_InterpEnumPlugOperator(EnumPlugOperator["Environment_InterpEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Environment_InterpEnumAttrOperator(EnumAttrOperator[Environment_InterpEnumPlugOperator]):
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


class ReflectionRolloff_InterpEnumPlugOperator(EnumPlugOperator["ReflectionRolloff_InterpEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ReflectionRolloff_InterpEnumAttrOperator(EnumAttrOperator[ReflectionRolloff_InterpEnumPlugOperator]):
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


class ReflectionRolloff_InterpEnumField(
    EnumField[ReflectionRolloff_InterpEnumAttrOperator, ReflectionRolloff_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ReflectionRolloff_InterpEnumAttrOperator
    PLUG_CLS = ReflectionRolloff_InterpEnumPlugOperator


class Color1PlugOperator(
    Float3CompoundBasePlugOperator["Color1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("color1R", "c1r"),
        ("color1G", "c1g"),
        ("color1B", "c1b"),
    )

    color1R = FloatField(default_value=0.0)
    c1r = color1R

    color1G = FloatField(default_value=0.0)
    c1g = color1G

    color1B = FloatField(default_value=0.0)
    c1b = color1B


class Color1AttrOperator(
    Float3CompoundBaseAttrOperator[Color1PlugOperator]
):
    __slots__ = ()

    color1R = FloatField(default_value=0.0)
    c1r = color1R

    color1G = FloatField(default_value=0.0)
    c1g = color1G

    color1B = FloatField(default_value=0.0)
    c1b = color1B


class Color1Field(
    Float3CompoundBaseField[Color1AttrOperator, Color1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Color1AttrOperator
    PLUG_CLS = Color1PlugOperator

    color1R = FloatField(default_value=0.0)
    c1r = color1R

    color1G = FloatField(default_value=0.0)
    c1g = color1G

    color1B = FloatField(default_value=0.0)
    c1b = color1B


class Color2PlugOperator(
    Float3CompoundBasePlugOperator["Color2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("color2R", "c2r"),
        ("color2G", "c2g"),
        ("color2B", "c2b"),
    )

    color2R = FloatField(default_value=1.0)
    c2r = color2R

    color2G = FloatField(default_value=1.0)
    c2g = color2G

    color2B = FloatField(default_value=1.0)
    c2b = color2B


class Color2AttrOperator(
    Float3CompoundBaseAttrOperator[Color2PlugOperator]
):
    __slots__ = ()

    color2R = FloatField(default_value=1.0)
    c2r = color2R

    color2G = FloatField(default_value=1.0)
    c2g = color2G

    color2B = FloatField(default_value=1.0)
    c2b = color2B


class Color2Field(
    Float3CompoundBaseField[Color2AttrOperator, Color2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Color2AttrOperator
    PLUG_CLS = Color2PlugOperator

    color2R = FloatField(default_value=1.0)
    c2r = color2R

    color2G = FloatField(default_value=1.0)
    c2g = color2G

    color2B = FloatField(default_value=1.0)
    c2b = color2B


class Transparency1PlugOperator(
    Float3CompoundBasePlugOperator["Transparency1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transparency1R", "t1r"),
        ("transparency1G", "t1g"),
        ("transparency1B", "t1b"),
    )

    transparency1R = FloatField(default_value=0.0)
    t1r = transparency1R

    transparency1G = FloatField(default_value=0.0)
    t1g = transparency1G

    transparency1B = FloatField(default_value=0.0)
    t1b = transparency1B


class Transparency1AttrOperator(
    Float3CompoundBaseAttrOperator[Transparency1PlugOperator]
):
    __slots__ = ()

    transparency1R = FloatField(default_value=0.0)
    t1r = transparency1R

    transparency1G = FloatField(default_value=0.0)
    t1g = transparency1G

    transparency1B = FloatField(default_value=0.0)
    t1b = transparency1B


class Transparency1Field(
    Float3CompoundBaseField[Transparency1AttrOperator, Transparency1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Transparency1AttrOperator
    PLUG_CLS = Transparency1PlugOperator

    transparency1R = FloatField(default_value=0.0)
    t1r = transparency1R

    transparency1G = FloatField(default_value=0.0)
    t1g = transparency1G

    transparency1B = FloatField(default_value=0.0)
    t1b = transparency1B


class Transparency2PlugOperator(
    Float3CompoundBasePlugOperator["Transparency2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transparency2R", "t2r"),
        ("transparency2G", "t2g"),
        ("transparency2B", "t2b"),
    )

    transparency2R = FloatField(default_value=0.0)
    t2r = transparency2R

    transparency2G = FloatField(default_value=0.0)
    t2g = transparency2G

    transparency2B = FloatField(default_value=0.0)
    t2b = transparency2B


class Transparency2AttrOperator(
    Float3CompoundBaseAttrOperator[Transparency2PlugOperator]
):
    __slots__ = ()

    transparency2R = FloatField(default_value=0.0)
    t2r = transparency2R

    transparency2G = FloatField(default_value=0.0)
    t2g = transparency2G

    transparency2B = FloatField(default_value=0.0)
    t2b = transparency2B


class Transparency2Field(
    Float3CompoundBaseField[Transparency2AttrOperator, Transparency2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Transparency2AttrOperator
    PLUG_CLS = Transparency2PlugOperator

    transparency2R = FloatField(default_value=0.0)
    t2r = transparency2R

    transparency2G = FloatField(default_value=0.0)
    t2g = transparency2G

    transparency2B = FloatField(default_value=0.0)
    t2b = transparency2B


class Incandescence1PlugOperator(
    Float3CompoundBasePlugOperator["Incandescence1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("incandescence1R", "i1r"),
        ("incandescence1G", "i1g"),
        ("incandescence1B", "i1b"),
    )

    incandescence1R = FloatField(default_value=0.0)
    i1r = incandescence1R

    incandescence1G = FloatField(default_value=0.0)
    i1g = incandescence1G

    incandescence1B = FloatField(default_value=0.0)
    i1b = incandescence1B


class Incandescence1AttrOperator(
    Float3CompoundBaseAttrOperator[Incandescence1PlugOperator]
):
    __slots__ = ()

    incandescence1R = FloatField(default_value=0.0)
    i1r = incandescence1R

    incandescence1G = FloatField(default_value=0.0)
    i1g = incandescence1G

    incandescence1B = FloatField(default_value=0.0)
    i1b = incandescence1B


class Incandescence1Field(
    Float3CompoundBaseField[Incandescence1AttrOperator, Incandescence1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Incandescence1AttrOperator
    PLUG_CLS = Incandescence1PlugOperator

    incandescence1R = FloatField(default_value=0.0)
    i1r = incandescence1R

    incandescence1G = FloatField(default_value=0.0)
    i1g = incandescence1G

    incandescence1B = FloatField(default_value=0.0)
    i1b = incandescence1B


class Incandescence2PlugOperator(
    Float3CompoundBasePlugOperator["Incandescence2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("incandescence2R", "i2r"),
        ("incandescence2G", "i2g"),
        ("incandescence2B", "i2b"),
    )

    incandescence2R = FloatField(default_value=0.0)
    i2r = incandescence2R

    incandescence2G = FloatField(default_value=0.0)
    i2g = incandescence2G

    incandescence2B = FloatField(default_value=0.0)
    i2b = incandescence2B


class Incandescence2AttrOperator(
    Float3CompoundBaseAttrOperator[Incandescence2PlugOperator]
):
    __slots__ = ()

    incandescence2R = FloatField(default_value=0.0)
    i2r = incandescence2R

    incandescence2G = FloatField(default_value=0.0)
    i2g = incandescence2G

    incandescence2B = FloatField(default_value=0.0)
    i2b = incandescence2B


class Incandescence2Field(
    Float3CompoundBaseField[Incandescence2AttrOperator, Incandescence2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Incandescence2AttrOperator
    PLUG_CLS = Incandescence2PlugOperator

    incandescence2R = FloatField(default_value=0.0)
    i2r = incandescence2R

    incandescence2G = FloatField(default_value=0.0)
    i2g = incandescence2G

    incandescence2B = FloatField(default_value=0.0)
    i2b = incandescence2B


class SpecularColorPlugOperator(
    Float3CompoundBasePlugOperator["SpecularColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularColorR", "spr"),
        ("specularColorG", "spg"),
        ("specularColorB", "spb"),
    )

    specularColorR = FloatField(default_value=1.0)
    spr = specularColorR

    specularColorG = FloatField(default_value=1.0)
    spg = specularColorG

    specularColorB = FloatField(default_value=1.0)
    spb = specularColorB


class SpecularColorAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularColorPlugOperator]
):
    __slots__ = ()

    specularColorR = FloatField(default_value=1.0)
    spr = specularColorR

    specularColorG = FloatField(default_value=1.0)
    spg = specularColorG

    specularColorB = FloatField(default_value=1.0)
    spb = specularColorB


class SpecularColorField(
    Float3CompoundBaseField[SpecularColorAttrOperator, SpecularColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularColorAttrOperator
    PLUG_CLS = SpecularColorPlugOperator

    specularColorR = FloatField(default_value=1.0)
    spr = specularColorR

    specularColorG = FloatField(default_value=1.0)
    spg = specularColorG

    specularColorB = FloatField(default_value=1.0)
    spb = specularColorB


class GlowColorPlugOperator(
    Float3CompoundBasePlugOperator["GlowColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("glowColorR", "glr"),
        ("glowColorG", "glg"),
        ("glowColorB", "glb"),
    )

    glowColorR = FloatField(default_value=0.5)
    glr = glowColorR

    glowColorG = FloatField(default_value=0.5)
    glg = glowColorG

    glowColorB = FloatField(default_value=0.5)
    glb = glowColorB


class GlowColorAttrOperator(
    Float3CompoundBaseAttrOperator[GlowColorPlugOperator]
):
    __slots__ = ()

    glowColorR = FloatField(default_value=0.5)
    glr = glowColorR

    glowColorG = FloatField(default_value=0.5)
    glg = glowColorG

    glowColorB = FloatField(default_value=0.5)
    glb = glowColorB


class GlowColorField(
    Float3CompoundBaseField[GlowColorAttrOperator, GlowColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GlowColorAttrOperator
    PLUG_CLS = GlowColorPlugOperator

    glowColorR = FloatField(default_value=0.5)
    glr = glowColorR

    glowColorG = FloatField(default_value=0.5)
    glg = glowColorG

    glowColorB = FloatField(default_value=0.5)
    glb = glowColorB


class LightDirectionPlugOperator(
    Double3CompoundBasePlugOperator["LightDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightDirectionX", "ldx"),
        ("lightDirectionY", "ldy"),
        ("lightDirectionZ", "ldz"),
    )

    lightDirectionX = DoubleField(default_value=0.5)
    ldx = lightDirectionX

    lightDirectionY = DoubleField(default_value=0.5)
    ldy = lightDirectionY

    lightDirectionZ = DoubleField(default_value=-0.5)
    ldz = lightDirectionZ


class LightDirectionAttrOperator(
    Double3CompoundBaseAttrOperator[LightDirectionPlugOperator]
):
    __slots__ = ()

    lightDirectionX = DoubleField(default_value=0.5)
    ldx = lightDirectionX

    lightDirectionY = DoubleField(default_value=0.5)
    ldy = lightDirectionY

    lightDirectionZ = DoubleField(default_value=-0.5)
    ldz = lightDirectionZ


class LightDirectionField(
    Double3CompoundBaseField[LightDirectionAttrOperator, LightDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightDirectionAttrOperator
    PLUG_CLS = LightDirectionPlugOperator

    lightDirectionX = DoubleField(default_value=0.5)
    ldx = lightDirectionX

    lightDirectionY = DoubleField(default_value=0.5)
    ldy = lightDirectionY

    lightDirectionZ = DoubleField(default_value=-0.5)
    ldz = lightDirectionZ


class UniformForcePlugOperator(
    Double3CompoundBasePlugOperator["UniformForceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uniformForceX", "ufx"),
        ("uniformForceY", "ufy"),
        ("uniformForceZ", "ufz"),
    )

    uniformForceX = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    ufx = uniformForceX

    uniformForceY = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    ufy = uniformForceY

    uniformForceZ = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    ufz = uniformForceZ


class UniformForceAttrOperator(
    Double3CompoundBaseAttrOperator[UniformForcePlugOperator]
):
    __slots__ = ()

    uniformForceX = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    ufx = uniformForceX

    uniformForceY = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    ufy = uniformForceY

    uniformForceZ = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    ufz = uniformForceZ


class UniformForceField(
    Double3CompoundBaseField[UniformForceAttrOperator, UniformForcePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UniformForceAttrOperator
    PLUG_CLS = UniformForcePlugOperator

    uniformForceX = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    ufx = uniformForceX

    uniformForceY = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    ufy = uniformForceY

    uniformForceZ = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    ufz = uniformForceZ


class TurbulenceOffsetPlugOperator(
    Double3CompoundBasePlugOperator["TurbulenceOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("turbulenceOffsetX", "trx"),
        ("turbulenceOffsetY", "try"),
        ("turbulenceOffsetZ", "trz"),
    )

    turbulenceOffsetX = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    trx = turbulenceOffsetX

    turbulenceOffsetY = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    try_ = turbulenceOffsetY

    turbulenceOffsetZ = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    trz = turbulenceOffsetZ


class TurbulenceOffsetAttrOperator(
    Double3CompoundBaseAttrOperator[TurbulenceOffsetPlugOperator]
):
    __slots__ = ()

    turbulenceOffsetX = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    trx = turbulenceOffsetX

    turbulenceOffsetY = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    try_ = turbulenceOffsetY

    turbulenceOffsetZ = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    trz = turbulenceOffsetZ


class TurbulenceOffsetField(
    Double3CompoundBaseField[TurbulenceOffsetAttrOperator, TurbulenceOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TurbulenceOffsetAttrOperator
    PLUG_CLS = TurbulenceOffsetPlugOperator

    turbulenceOffsetX = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    trx = turbulenceOffsetX

    turbulenceOffsetY = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    try_ = turbulenceOffsetY

    turbulenceOffsetZ = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    trz = turbulenceOffsetZ


class SunDirectionPlugOperator(
    Double3CompoundBasePlugOperator["SunDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sunDirectionX", "sndx"),
        ("sunDirectionY", "sndy"),
        ("sunDirectionZ", "sndz"),
    )

    sunDirectionX = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    sndx = sunDirectionX

    sunDirectionY = DoubleField(default_value=1.0, soft_min_value=-1.0, soft_max_value=1.0)
    sndy = sunDirectionY

    sunDirectionZ = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    sndz = sunDirectionZ


class SunDirectionAttrOperator(
    Double3CompoundBaseAttrOperator[SunDirectionPlugOperator]
):
    __slots__ = ()

    sunDirectionX = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    sndx = sunDirectionX

    sunDirectionY = DoubleField(default_value=1.0, soft_min_value=-1.0, soft_max_value=1.0)
    sndy = sunDirectionY

    sunDirectionZ = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    sndz = sunDirectionZ


class SunDirectionField(
    Double3CompoundBaseField[SunDirectionAttrOperator, SunDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SunDirectionAttrOperator
    PLUG_CLS = SunDirectionPlugOperator

    sunDirectionX = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    sndx = sunDirectionX

    sunDirectionY = DoubleField(default_value=1.0, soft_min_value=-1.0, soft_max_value=1.0)
    sndy = sunDirectionY

    sunDirectionZ = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    sndz = sunDirectionZ


class LeafCurlPlugOperator(
    CompoundPlugOperator["LeafCurlAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("leafCurl_Position", "lclp"),
        ("leafCurl_FloatValue", "lclfv"),
        ("leafCurl_Interp", "lcli"),
    )

    leafCurl_Position = FloatField(default_value=0.0)
    lclp = leafCurl_Position

    leafCurl_FloatValue = FloatField(default_value=0.0)
    lclfv = leafCurl_FloatValue

    leafCurl_Interp = LeafCurl_InterpEnumField(default_value=0)
    lcli = leafCurl_Interp


class LeafCurlAttrOperator(
    CompoundAttrOperator[LeafCurlPlugOperator]
):
    __slots__ = ()

    leafCurl_Position = FloatField(default_value=0.0)
    lclp = leafCurl_Position

    leafCurl_FloatValue = FloatField(default_value=0.0)
    lclfv = leafCurl_FloatValue

    leafCurl_Interp = LeafCurl_InterpEnumField(default_value=0)
    lcli = leafCurl_Interp


class LeafCurlField(
    CompoundField[LeafCurlAttrOperator, LeafCurlPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafCurlAttrOperator
    PLUG_CLS = LeafCurlPlugOperator


class LeafColor1PlugOperator(
    Float3CompoundBasePlugOperator["LeafColor1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("leafColor1R", "lr1"),
        ("leafColor1G", "lg1"),
        ("leafColor1B", "lb1"),
    )

    leafColor1R = FloatField(default_value=0.20000000298023224)
    lr1 = leafColor1R

    leafColor1G = FloatField(default_value=0.6000000238418579)
    lg1 = leafColor1G

    leafColor1B = FloatField(default_value=0.30000001192092896)
    lb1 = leafColor1B


class LeafColor1AttrOperator(
    Float3CompoundBaseAttrOperator[LeafColor1PlugOperator]
):
    __slots__ = ()

    leafColor1R = FloatField(default_value=0.20000000298023224)
    lr1 = leafColor1R

    leafColor1G = FloatField(default_value=0.6000000238418579)
    lg1 = leafColor1G

    leafColor1B = FloatField(default_value=0.30000001192092896)
    lb1 = leafColor1B


class LeafColor1Field(
    Float3CompoundBaseField[LeafColor1AttrOperator, LeafColor1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafColor1AttrOperator
    PLUG_CLS = LeafColor1PlugOperator

    leafColor1R = FloatField(default_value=0.20000000298023224)
    lr1 = leafColor1R

    leafColor1G = FloatField(default_value=0.6000000238418579)
    lg1 = leafColor1G

    leafColor1B = FloatField(default_value=0.30000001192092896)
    lb1 = leafColor1B


class LeafColor2PlugOperator(
    Float3CompoundBasePlugOperator["LeafColor2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("leafColor2R", "lr2"),
        ("leafColor2G", "lg2"),
        ("leafColor2B", "lb2"),
    )

    leafColor2R = FloatField(default_value=0.4000000059604645)
    lr2 = leafColor2R

    leafColor2G = FloatField(default_value=0.6000000238418579)
    lg2 = leafColor2G

    leafColor2B = FloatField(default_value=0.30000001192092896)
    lb2 = leafColor2B


class LeafColor2AttrOperator(
    Float3CompoundBaseAttrOperator[LeafColor2PlugOperator]
):
    __slots__ = ()

    leafColor2R = FloatField(default_value=0.4000000059604645)
    lr2 = leafColor2R

    leafColor2G = FloatField(default_value=0.6000000238418579)
    lg2 = leafColor2G

    leafColor2B = FloatField(default_value=0.30000001192092896)
    lb2 = leafColor2B


class LeafColor2Field(
    Float3CompoundBaseField[LeafColor2AttrOperator, LeafColor2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafColor2AttrOperator
    PLUG_CLS = LeafColor2PlugOperator

    leafColor2R = FloatField(default_value=0.4000000059604645)
    lr2 = leafColor2R

    leafColor2G = FloatField(default_value=0.6000000238418579)
    lg2 = leafColor2G

    leafColor2B = FloatField(default_value=0.30000001192092896)
    lb2 = leafColor2B


class BudColorPlugOperator(
    Float3CompoundBasePlugOperator["BudColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("budColorR", "bur"),
        ("budColorG", "bug"),
        ("budColorB", "bub"),
    )

    budColorR = FloatField(default_value=0.4000000059604645)
    bur = budColorR

    budColorG = FloatField(default_value=0.800000011920929)
    bug = budColorG

    budColorB = FloatField(default_value=0.20000000298023224)
    bub = budColorB


class BudColorAttrOperator(
    Float3CompoundBaseAttrOperator[BudColorPlugOperator]
):
    __slots__ = ()

    budColorR = FloatField(default_value=0.4000000059604645)
    bur = budColorR

    budColorG = FloatField(default_value=0.800000011920929)
    bug = budColorG

    budColorB = FloatField(default_value=0.20000000298023224)
    bub = budColorB


class BudColorField(
    Float3CompoundBaseField[BudColorAttrOperator, BudColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BudColorAttrOperator
    PLUG_CLS = BudColorPlugOperator

    budColorR = FloatField(default_value=0.4000000059604645)
    bur = budColorR

    budColorG = FloatField(default_value=0.800000011920929)
    bug = budColorG

    budColorB = FloatField(default_value=0.20000000298023224)
    bub = budColorB


class PetalCurlPlugOperator(
    CompoundPlugOperator["PetalCurlAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("petalCurl_Position", "pclp"),
        ("petalCurl_FloatValue", "pclfv"),
        ("petalCurl_Interp", "pcli"),
    )

    petalCurl_Position = FloatField(default_value=0.0)
    pclp = petalCurl_Position

    petalCurl_FloatValue = FloatField(default_value=0.0)
    pclfv = petalCurl_FloatValue

    petalCurl_Interp = PetalCurl_InterpEnumField(default_value=0)
    pcli = petalCurl_Interp


class PetalCurlAttrOperator(
    CompoundAttrOperator[PetalCurlPlugOperator]
):
    __slots__ = ()

    petalCurl_Position = FloatField(default_value=0.0)
    pclp = petalCurl_Position

    petalCurl_FloatValue = FloatField(default_value=0.0)
    pclfv = petalCurl_FloatValue

    petalCurl_Interp = PetalCurl_InterpEnumField(default_value=0)
    pcli = petalCurl_Interp


class PetalCurlField(
    CompoundField[PetalCurlAttrOperator, PetalCurlPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PetalCurlAttrOperator
    PLUG_CLS = PetalCurlPlugOperator


class PetalColor1PlugOperator(
    Float3CompoundBasePlugOperator["PetalColor1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("petalColor1R", "pr1"),
        ("petalColor1G", "pg1"),
        ("petalColor1B", "pb1"),
    )

    petalColor1R = FloatField(default_value=0.800000011920929)
    pr1 = petalColor1R

    petalColor1G = FloatField(default_value=0.20000000298023224)
    pg1 = petalColor1G

    petalColor1B = FloatField(default_value=0.10000000149011612)
    pb1 = petalColor1B


class PetalColor1AttrOperator(
    Float3CompoundBaseAttrOperator[PetalColor1PlugOperator]
):
    __slots__ = ()

    petalColor1R = FloatField(default_value=0.800000011920929)
    pr1 = petalColor1R

    petalColor1G = FloatField(default_value=0.20000000298023224)
    pg1 = petalColor1G

    petalColor1B = FloatField(default_value=0.10000000149011612)
    pb1 = petalColor1B


class PetalColor1Field(
    Float3CompoundBaseField[PetalColor1AttrOperator, PetalColor1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PetalColor1AttrOperator
    PLUG_CLS = PetalColor1PlugOperator

    petalColor1R = FloatField(default_value=0.800000011920929)
    pr1 = petalColor1R

    petalColor1G = FloatField(default_value=0.20000000298023224)
    pg1 = petalColor1G

    petalColor1B = FloatField(default_value=0.10000000149011612)
    pb1 = petalColor1B


class PetalColor2PlugOperator(
    Float3CompoundBasePlugOperator["PetalColor2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("petalColor2R", "pr2"),
        ("petalColor2G", "pg2"),
        ("petalColor2B", "pb2"),
    )

    petalColor2R = FloatField(default_value=1.0)
    pr2 = petalColor2R

    petalColor2G = FloatField(default_value=1.0)
    pg2 = petalColor2G

    petalColor2B = FloatField(default_value=1.0)
    pb2 = petalColor2B


class PetalColor2AttrOperator(
    Float3CompoundBaseAttrOperator[PetalColor2PlugOperator]
):
    __slots__ = ()

    petalColor2R = FloatField(default_value=1.0)
    pr2 = petalColor2R

    petalColor2G = FloatField(default_value=1.0)
    pg2 = petalColor2G

    petalColor2B = FloatField(default_value=1.0)
    pb2 = petalColor2B


class PetalColor2Field(
    Float3CompoundBaseField[PetalColor2AttrOperator, PetalColor2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PetalColor2AttrOperator
    PLUG_CLS = PetalColor2PlugOperator

    petalColor2R = FloatField(default_value=1.0)
    pr2 = petalColor2R

    petalColor2G = FloatField(default_value=1.0)
    pg2 = petalColor2G

    petalColor2B = FloatField(default_value=1.0)
    pb2 = petalColor2B


class TexColor1PlugOperator(
    Float3CompoundBasePlugOperator["TexColor1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("texColor1R", "x1r"),
        ("texColor1G", "x1g"),
        ("texColor1B", "x1b"),
    )

    texColor1R = FloatField(default_value=1.0)
    x1r = texColor1R

    texColor1G = FloatField(default_value=1.0)
    x1g = texColor1G

    texColor1B = FloatField(default_value=1.0)
    x1b = texColor1B


class TexColor1AttrOperator(
    Float3CompoundBaseAttrOperator[TexColor1PlugOperator]
):
    __slots__ = ()

    texColor1R = FloatField(default_value=1.0)
    x1r = texColor1R

    texColor1G = FloatField(default_value=1.0)
    x1g = texColor1G

    texColor1B = FloatField(default_value=1.0)
    x1b = texColor1B


class TexColor1Field(
    Float3CompoundBaseField[TexColor1AttrOperator, TexColor1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TexColor1AttrOperator
    PLUG_CLS = TexColor1PlugOperator

    texColor1R = FloatField(default_value=1.0)
    x1r = texColor1R

    texColor1G = FloatField(default_value=1.0)
    x1g = texColor1G

    texColor1B = FloatField(default_value=1.0)
    x1b = texColor1B


class TexColor2PlugOperator(
    Float3CompoundBasePlugOperator["TexColor2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("texColor2R", "x2r"),
        ("texColor2G", "x2g"),
        ("texColor2B", "x2b"),
    )

    texColor2R = FloatField(default_value=0.0)
    x2r = texColor2R

    texColor2G = FloatField(default_value=0.0)
    x2g = texColor2G

    texColor2B = FloatField(default_value=0.0)
    x2b = texColor2B


class TexColor2AttrOperator(
    Float3CompoundBaseAttrOperator[TexColor2PlugOperator]
):
    __slots__ = ()

    texColor2R = FloatField(default_value=0.0)
    x2r = texColor2R

    texColor2G = FloatField(default_value=0.0)
    x2g = texColor2G

    texColor2B = FloatField(default_value=0.0)
    x2b = texColor2B


class TexColor2Field(
    Float3CompoundBaseField[TexColor2AttrOperator, TexColor2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TexColor2AttrOperator
    PLUG_CLS = TexColor2PlugOperator

    texColor2R = FloatField(default_value=0.0)
    x2r = texColor2R

    texColor2G = FloatField(default_value=0.0)
    x2g = texColor2G

    texColor2B = FloatField(default_value=0.0)
    x2b = texColor2B


class WidthScalePlugOperator(
    CompoundPlugOperator["WidthScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("widthScale_Position", "wscp"),
        ("widthScale_FloatValue", "wscfv"),
        ("widthScale_Interp", "wsci"),
    )

    widthScale_Position = FloatField(default_value=0.0)
    wscp = widthScale_Position

    widthScale_FloatValue = FloatField(default_value=0.0)
    wscfv = widthScale_FloatValue

    widthScale_Interp = WidthScale_InterpEnumField(default_value=0)
    wsci = widthScale_Interp


class WidthScaleAttrOperator(
    CompoundAttrOperator[WidthScalePlugOperator]
):
    __slots__ = ()

    widthScale_Position = FloatField(default_value=0.0)
    wscp = widthScale_Position

    widthScale_FloatValue = FloatField(default_value=0.0)
    wscfv = widthScale_FloatValue

    widthScale_Interp = WidthScale_InterpEnumField(default_value=0)
    wsci = widthScale_Interp


class WidthScaleField(
    CompoundField[WidthScaleAttrOperator, WidthScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WidthScaleAttrOperator
    PLUG_CLS = WidthScalePlugOperator


class LeafWidthScalePlugOperator(
    CompoundPlugOperator["LeafWidthScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("leafWidthScale_Position", "lwsp"),
        ("leafWidthScale_FloatValue", "lwsfv"),
        ("leafWidthScale_Interp", "lwsi"),
    )

    leafWidthScale_Position = FloatField(default_value=0.0)
    lwsp = leafWidthScale_Position

    leafWidthScale_FloatValue = FloatField(default_value=0.0)
    lwsfv = leafWidthScale_FloatValue

    leafWidthScale_Interp = LeafWidthScale_InterpEnumField(default_value=0)
    lwsi = leafWidthScale_Interp


class LeafWidthScaleAttrOperator(
    CompoundAttrOperator[LeafWidthScalePlugOperator]
):
    __slots__ = ()

    leafWidthScale_Position = FloatField(default_value=0.0)
    lwsp = leafWidthScale_Position

    leafWidthScale_FloatValue = FloatField(default_value=0.0)
    lwsfv = leafWidthScale_FloatValue

    leafWidthScale_Interp = LeafWidthScale_InterpEnumField(default_value=0)
    lwsi = leafWidthScale_Interp


class LeafWidthScaleField(
    CompoundField[LeafWidthScaleAttrOperator, LeafWidthScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafWidthScaleAttrOperator
    PLUG_CLS = LeafWidthScalePlugOperator


class PetalWidthScalePlugOperator(
    CompoundPlugOperator["PetalWidthScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("petalWidthScale_Position", "pwsp"),
        ("petalWidthScale_FloatValue", "pwsfv"),
        ("petalWidthScale_Interp", "pwsi"),
    )

    petalWidthScale_Position = FloatField(default_value=0.0)
    pwsp = petalWidthScale_Position

    petalWidthScale_FloatValue = FloatField(default_value=0.0)
    pwsfv = petalWidthScale_FloatValue

    petalWidthScale_Interp = PetalWidthScale_InterpEnumField(default_value=0)
    pwsi = petalWidthScale_Interp


class PetalWidthScaleAttrOperator(
    CompoundAttrOperator[PetalWidthScalePlugOperator]
):
    __slots__ = ()

    petalWidthScale_Position = FloatField(default_value=0.0)
    pwsp = petalWidthScale_Position

    petalWidthScale_FloatValue = FloatField(default_value=0.0)
    pwsfv = petalWidthScale_FloatValue

    petalWidthScale_Interp = PetalWidthScale_InterpEnumField(default_value=0)
    pwsi = petalWidthScale_Interp


class PetalWidthScaleField(
    CompoundField[PetalWidthScaleAttrOperator, PetalWidthScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PetalWidthScaleAttrOperator
    PLUG_CLS = PetalWidthScalePlugOperator


class TwigLengthScalePlugOperator(
    CompoundPlugOperator["TwigLengthScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("twigLengthScale_Position", "tlsp"),
        ("twigLengthScale_FloatValue", "tlsfv"),
        ("twigLengthScale_Interp", "tlsi"),
    )

    twigLengthScale_Position = FloatField(default_value=0.0)
    tlsp = twigLengthScale_Position

    twigLengthScale_FloatValue = FloatField(default_value=0.0)
    tlsfv = twigLengthScale_FloatValue

    twigLengthScale_Interp = TwigLengthScale_InterpEnumField(default_value=0)
    tlsi = twigLengthScale_Interp


class TwigLengthScaleAttrOperator(
    CompoundAttrOperator[TwigLengthScalePlugOperator]
):
    __slots__ = ()

    twigLengthScale_Position = FloatField(default_value=0.0)
    tlsp = twigLengthScale_Position

    twigLengthScale_FloatValue = FloatField(default_value=0.0)
    tlsfv = twigLengthScale_FloatValue

    twigLengthScale_Interp = TwigLengthScale_InterpEnumField(default_value=0)
    tlsi = twigLengthScale_Interp


class TwigLengthScaleField(
    CompoundField[TwigLengthScaleAttrOperator, TwigLengthScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TwigLengthScaleAttrOperator
    PLUG_CLS = TwigLengthScalePlugOperator


class ThornBaseColorPlugOperator(
    Float3CompoundBasePlugOperator["ThornBaseColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("thornBaseColorR", "tbcr"),
        ("thornBaseColorG", "tbcg"),
        ("thornBaseColorB", "tbcb"),
    )

    thornBaseColorR = FloatField(default_value=0.5)
    tbcr = thornBaseColorR

    thornBaseColorG = FloatField(default_value=0.5)
    tbcg = thornBaseColorG

    thornBaseColorB = FloatField(default_value=0.5)
    tbcb = thornBaseColorB


class ThornBaseColorAttrOperator(
    Float3CompoundBaseAttrOperator[ThornBaseColorPlugOperator]
):
    __slots__ = ()

    thornBaseColorR = FloatField(default_value=0.5)
    tbcr = thornBaseColorR

    thornBaseColorG = FloatField(default_value=0.5)
    tbcg = thornBaseColorG

    thornBaseColorB = FloatField(default_value=0.5)
    tbcb = thornBaseColorB


class ThornBaseColorField(
    Float3CompoundBaseField[ThornBaseColorAttrOperator, ThornBaseColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ThornBaseColorAttrOperator
    PLUG_CLS = ThornBaseColorPlugOperator

    thornBaseColorR = FloatField(default_value=0.5)
    tbcr = thornBaseColorR

    thornBaseColorG = FloatField(default_value=0.5)
    tbcg = thornBaseColorG

    thornBaseColorB = FloatField(default_value=0.5)
    tbcb = thornBaseColorB


class ThornTipColorPlugOperator(
    Float3CompoundBasePlugOperator["ThornTipColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("thornTipColorR", "ttcr"),
        ("thornTipColorG", "ttcg"),
        ("thornTipColorB", "ttcb"),
    )

    thornTipColorR = FloatField(default_value=0.5)
    ttcr = thornTipColorR

    thornTipColorG = FloatField(default_value=0.5)
    ttcg = thornTipColorG

    thornTipColorB = FloatField(default_value=0.5)
    ttcb = thornTipColorB


class ThornTipColorAttrOperator(
    Float3CompoundBaseAttrOperator[ThornTipColorPlugOperator]
):
    __slots__ = ()

    thornTipColorR = FloatField(default_value=0.5)
    ttcr = thornTipColorR

    thornTipColorG = FloatField(default_value=0.5)
    ttcg = thornTipColorG

    thornTipColorB = FloatField(default_value=0.5)
    ttcb = thornTipColorB


class ThornTipColorField(
    Float3CompoundBaseField[ThornTipColorAttrOperator, ThornTipColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ThornTipColorAttrOperator
    PLUG_CLS = ThornTipColorPlugOperator

    thornTipColorR = FloatField(default_value=0.5)
    ttcr = thornTipColorR

    thornTipColorG = FloatField(default_value=0.5)
    ttcg = thornTipColorG

    thornTipColorB = FloatField(default_value=0.5)
    ttcb = thornTipColorB


class EnvironmentPlugOperator(
    CompoundPlugOperator["EnvironmentAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("environment_Position", "envp"),
        ("environment_Color", "envc"),
        ("environment_Interp", "envi"),
    )

    environment_Position = FloatField(default_value=0.0)
    envp = environment_Position

    environment_Color = Float3Field(default_value=(0.0, 0.0, 0.0))
    envc = environment_Color

    environment_Interp = Environment_InterpEnumField(default_value=0)
    envi = environment_Interp


class EnvironmentAttrOperator(
    CompoundAttrOperator[EnvironmentPlugOperator]
):
    __slots__ = ()

    environment_Position = FloatField(default_value=0.0)
    envp = environment_Position

    environment_Color = Float3Field(default_value=(0.0, 0.0, 0.0))
    envc = environment_Color

    environment_Interp = Environment_InterpEnumField(default_value=0)
    envi = environment_Interp


class EnvironmentField(
    CompoundField[EnvironmentAttrOperator, EnvironmentPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EnvironmentAttrOperator
    PLUG_CLS = EnvironmentPlugOperator


class ReflectionRolloffPlugOperator(
    CompoundPlugOperator["ReflectionRolloffAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("reflectionRolloff_Position", "rrop"),
        ("reflectionRolloff_FloatValue", "rrofv"),
        ("reflectionRolloff_Interp", "rroi"),
    )

    reflectionRolloff_Position = FloatField(default_value=0.0)
    rrop = reflectionRolloff_Position

    reflectionRolloff_FloatValue = FloatField(default_value=0.0)
    rrofv = reflectionRolloff_FloatValue

    reflectionRolloff_Interp = ReflectionRolloff_InterpEnumField(default_value=0)
    rroi = reflectionRolloff_Interp


class ReflectionRolloffAttrOperator(
    CompoundAttrOperator[ReflectionRolloffPlugOperator]
):
    __slots__ = ()

    reflectionRolloff_Position = FloatField(default_value=0.0)
    rrop = reflectionRolloff_Position

    reflectionRolloff_FloatValue = FloatField(default_value=0.0)
    rrofv = reflectionRolloff_FloatValue

    reflectionRolloff_Interp = ReflectionRolloff_InterpEnumField(default_value=0)
    rroi = reflectionRolloff_Interp


class ReflectionRolloffField(
    CompoundField[ReflectionRolloffAttrOperator, ReflectionRolloffPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ReflectionRolloffAttrOperator
    PLUG_CLS = ReflectionRolloffPlugOperator
