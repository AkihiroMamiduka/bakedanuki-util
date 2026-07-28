# coding: utf-8

from ..std.at.addr import AddrField
from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.light_data import (
    LightDataAttrOperator,
    LightDataPlugOperator,
    LightDataField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    Float3Field,
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)


class Environment_InterpEnumPlugOperator(
    EnumPlugOperator["Environment_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Environment_InterpEnumAttrOperator(
    EnumAttrOperator[Environment_InterpEnumPlugOperator]
):
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
    EnumField[
        Environment_InterpEnumAttrOperator, Environment_InterpEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Environment_InterpEnumAttrOperator
    PLUG_CLS = Environment_InterpEnumPlugOperator


class WaveHeight_InterpEnumPlugOperator(
    EnumPlugOperator["WaveHeight_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class WaveHeight_InterpEnumAttrOperator(
    EnumAttrOperator[WaveHeight_InterpEnumPlugOperator]
):
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


class WaveHeight_InterpEnumField(
    EnumField[
        WaveHeight_InterpEnumAttrOperator, WaveHeight_InterpEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = WaveHeight_InterpEnumAttrOperator
    PLUG_CLS = WaveHeight_InterpEnumPlugOperator


class WaveTurbulence_InterpEnumPlugOperator(
    EnumPlugOperator["WaveTurbulence_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class WaveTurbulence_InterpEnumAttrOperator(
    EnumAttrOperator[WaveTurbulence_InterpEnumPlugOperator]
):
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


class WaveTurbulence_InterpEnumField(
    EnumField[
        WaveTurbulence_InterpEnumAttrOperator,
        WaveTurbulence_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = WaveTurbulence_InterpEnumAttrOperator
    PLUG_CLS = WaveTurbulence_InterpEnumPlugOperator


class WavePeaking_InterpEnumPlugOperator(
    EnumPlugOperator["WavePeaking_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class WavePeaking_InterpEnumAttrOperator(
    EnumAttrOperator[WavePeaking_InterpEnumPlugOperator]
):
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


class WavePeaking_InterpEnumField(
    EnumField[
        WavePeaking_InterpEnumAttrOperator, WavePeaking_InterpEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = WavePeaking_InterpEnumAttrOperator
    PLUG_CLS = WavePeaking_InterpEnumPlugOperator


class RayDirectionPlugOperator(
    Float3CompoundBasePlugOperator["RayDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rayDirectionX", "rdx"),
        ("rayDirectionY", "rdy"),
        ("rayDirectionZ", "rdz"),
    )

    rayDirectionX = FloatField(default_value=0.0, readable=False)
    rdx = rayDirectionX

    rayDirectionY = FloatField(default_value=0.0, readable=False)
    rdy = rayDirectionY

    rayDirectionZ = FloatField(default_value=1.0, readable=False)
    rdz = rayDirectionZ


class RayDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[RayDirectionPlugOperator]
):
    __slots__ = ()

    rayDirectionX = FloatField(default_value=0.0, readable=False)
    rdx = rayDirectionX

    rayDirectionY = FloatField(default_value=0.0, readable=False)
    rdy = rayDirectionY

    rayDirectionZ = FloatField(default_value=1.0, readable=False)
    rdz = rayDirectionZ


class RayDirectionField(
    Float3CompoundBaseField[RayDirectionAttrOperator, RayDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RayDirectionAttrOperator
    PLUG_CLS = RayDirectionPlugOperator

    rayDirectionX = FloatField(default_value=0.0, readable=False)
    rdx = rayDirectionX

    rayDirectionY = FloatField(default_value=0.0, readable=False)
    rdy = rayDirectionY

    rayDirectionZ = FloatField(default_value=1.0, readable=False)
    rdz = rayDirectionZ


class WaterColorPlugOperator(
    Float3CompoundBasePlugOperator["WaterColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("waterColorR", "wcr"),
        ("waterColorG", "wcg"),
        ("waterColorB", "wcb"),
    )

    waterColorR = FloatField(default_value=0.0)
    wcr = waterColorR

    waterColorG = FloatField(default_value=0.36000001430511475)
    wcg = waterColorG

    waterColorB = FloatField(default_value=0.4000000059604645)
    wcb = waterColorB


class WaterColorAttrOperator(
    Float3CompoundBaseAttrOperator[WaterColorPlugOperator]
):
    __slots__ = ()

    waterColorR = FloatField(default_value=0.0)
    wcr = waterColorR

    waterColorG = FloatField(default_value=0.36000001430511475)
    wcg = waterColorG

    waterColorB = FloatField(default_value=0.4000000059604645)
    wcb = waterColorB


class WaterColorField(
    Float3CompoundBaseField[WaterColorAttrOperator, WaterColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WaterColorAttrOperator
    PLUG_CLS = WaterColorPlugOperator

    waterColorR = FloatField(default_value=0.0)
    wcr = waterColorR

    waterColorG = FloatField(default_value=0.36000001430511475)
    wcg = waterColorG

    waterColorB = FloatField(default_value=0.4000000059604645)
    wcb = waterColorB


class TransparencyPlugOperator(
    Float3CompoundBasePlugOperator["TransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transparencyR", "itr"),
        ("transparencyG", "itg"),
        ("transparencyB", "itb"),
    )

    transparencyR = FloatField(default_value=0.0)
    itr = transparencyR

    transparencyG = FloatField(default_value=0.0)
    itg = transparencyG

    transparencyB = FloatField(default_value=0.0)
    itb = transparencyB


class TransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[TransparencyPlugOperator]
):
    __slots__ = ()

    transparencyR = FloatField(default_value=0.0)
    itr = transparencyR

    transparencyG = FloatField(default_value=0.0)
    itg = transparencyG

    transparencyB = FloatField(default_value=0.0)
    itb = transparencyB


class TransparencyField(
    Float3CompoundBaseField[TransparencyAttrOperator, TransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencyAttrOperator
    PLUG_CLS = TransparencyPlugOperator

    transparencyR = FloatField(default_value=0.0)
    itr = transparencyR

    transparencyG = FloatField(default_value=0.0)
    itg = transparencyG

    transparencyB = FloatField(default_value=0.0)
    itb = transparencyB


class AmbientColorPlugOperator(
    Float3CompoundBasePlugOperator["AmbientColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ambientColorR", "acr"),
        ("ambientColorG", "acg"),
        ("ambientColorB", "acb"),
    )

    ambientColorR = FloatField(default_value=0.0)
    acr = ambientColorR

    ambientColorG = FloatField(default_value=0.0)
    acg = ambientColorG

    ambientColorB = FloatField(default_value=0.0)
    acb = ambientColorB


class AmbientColorAttrOperator(
    Float3CompoundBaseAttrOperator[AmbientColorPlugOperator]
):
    __slots__ = ()

    ambientColorR = FloatField(default_value=0.0)
    acr = ambientColorR

    ambientColorG = FloatField(default_value=0.0)
    acg = ambientColorG

    ambientColorB = FloatField(default_value=0.0)
    acb = ambientColorB


class AmbientColorField(
    Float3CompoundBaseField[AmbientColorAttrOperator, AmbientColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AmbientColorAttrOperator
    PLUG_CLS = AmbientColorPlugOperator

    ambientColorR = FloatField(default_value=0.0)
    acr = ambientColorR

    ambientColorG = FloatField(default_value=0.0)
    acg = ambientColorG

    ambientColorB = FloatField(default_value=0.0)
    acb = ambientColorB


class IncandescencePlugOperator(
    Float3CompoundBasePlugOperator["IncandescenceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("incandescenceR", "ir"),
        ("incandescenceG", "ig"),
        ("incandescenceB", "ib"),
    )

    incandescenceR = FloatField(default_value=0.0)
    ir = incandescenceR

    incandescenceG = FloatField(default_value=0.0)
    ig = incandescenceG

    incandescenceB = FloatField(default_value=0.0)
    ib = incandescenceB


class IncandescenceAttrOperator(
    Float3CompoundBaseAttrOperator[IncandescencePlugOperator]
):
    __slots__ = ()

    incandescenceR = FloatField(default_value=0.0)
    ir = incandescenceR

    incandescenceG = FloatField(default_value=0.0)
    ig = incandescenceG

    incandescenceB = FloatField(default_value=0.0)
    ib = incandescenceB


class IncandescenceField(
    Float3CompoundBaseField[
        IncandescenceAttrOperator, IncandescencePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = IncandescenceAttrOperator
    PLUG_CLS = IncandescencePlugOperator

    incandescenceR = FloatField(default_value=0.0)
    ir = incandescenceR

    incandescenceG = FloatField(default_value=0.0)
    ig = incandescenceG

    incandescenceB = FloatField(default_value=0.0)
    ib = incandescenceB


class SpecularColorPlugOperator(
    Float3CompoundBasePlugOperator["SpecularColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularColorR", "sr"),
        ("specularColorG", "sg"),
        ("specularColorB", "sb"),
    )

    specularColorR = FloatField(default_value=1.0)
    sr = specularColorR

    specularColorG = FloatField(default_value=1.0)
    sg = specularColorG

    specularColorB = FloatField(default_value=1.0)
    sb = specularColorB


class SpecularColorAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularColorPlugOperator]
):
    __slots__ = ()

    specularColorR = FloatField(default_value=1.0)
    sr = specularColorR

    specularColorG = FloatField(default_value=1.0)
    sg = specularColorG

    specularColorB = FloatField(default_value=1.0)
    sb = specularColorB


class SpecularColorField(
    Float3CompoundBaseField[
        SpecularColorAttrOperator, SpecularColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SpecularColorAttrOperator
    PLUG_CLS = SpecularColorPlugOperator

    specularColorR = FloatField(default_value=1.0)
    sr = specularColorR

    specularColorG = FloatField(default_value=1.0)
    sg = specularColorG

    specularColorB = FloatField(default_value=1.0)
    sb = specularColorB


class EnvironmentPlugOperator(CompoundPlugOperator["EnvironmentAttrOperator"]):
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


class EnvironmentAttrOperator(CompoundAttrOperator[EnvironmentPlugOperator]):
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


class ReflectedColorPlugOperator(
    Float3CompoundBasePlugOperator["ReflectedColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("reflectedColorR", "rr"),
        ("reflectedColorG", "rg"),
        ("reflectedColorB", "rb"),
    )

    reflectedColorR = FloatField(default_value=0.0)
    rr = reflectedColorR

    reflectedColorG = FloatField(default_value=0.0)
    rg = reflectedColorG

    reflectedColorB = FloatField(default_value=0.0)
    rb = reflectedColorB


class ReflectedColorAttrOperator(
    Float3CompoundBaseAttrOperator[ReflectedColorPlugOperator]
):
    __slots__ = ()

    reflectedColorR = FloatField(default_value=0.0)
    rr = reflectedColorR

    reflectedColorG = FloatField(default_value=0.0)
    rg = reflectedColorG

    reflectedColorB = FloatField(default_value=0.0)
    rb = reflectedColorB


class ReflectedColorField(
    Float3CompoundBaseField[
        ReflectedColorAttrOperator, ReflectedColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ReflectedColorAttrOperator
    PLUG_CLS = ReflectedColorPlugOperator

    reflectedColorR = FloatField(default_value=0.0)
    rr = reflectedColorR

    reflectedColorG = FloatField(default_value=0.0)
    rg = reflectedColorG

    reflectedColorB = FloatField(default_value=0.0)
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

    triangleNormalCameraX = FloatField(default_value=0.0)
    tnx = triangleNormalCameraX

    triangleNormalCameraY = FloatField(default_value=1.0)
    tny = triangleNormalCameraY

    triangleNormalCameraZ = FloatField(default_value=0.0)
    tnz = triangleNormalCameraZ


class TriangleNormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[TriangleNormalCameraPlugOperator]
):
    __slots__ = ()

    triangleNormalCameraX = FloatField(default_value=0.0)
    tnx = triangleNormalCameraX

    triangleNormalCameraY = FloatField(default_value=1.0)
    tny = triangleNormalCameraY

    triangleNormalCameraZ = FloatField(default_value=0.0)
    tnz = triangleNormalCameraZ


class TriangleNormalCameraField(
    Float3CompoundBaseField[
        TriangleNormalCameraAttrOperator, TriangleNormalCameraPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = TriangleNormalCameraAttrOperator
    PLUG_CLS = TriangleNormalCameraPlugOperator

    triangleNormalCameraX = FloatField(default_value=0.0)
    tnx = triangleNormalCameraX

    triangleNormalCameraY = FloatField(default_value=1.0)
    tny = triangleNormalCameraY

    triangleNormalCameraZ = FloatField(default_value=0.0)
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


class OutGlowColorPlugOperator(
    Float3CompoundBasePlugOperator["OutGlowColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outGlowColorR", "ogr"),
        ("outGlowColorG", "ogg"),
        ("outGlowColorB", "ogb"),
    )

    outGlowColorR = FloatField(default_value=0.0, writable=False)
    ogr = outGlowColorR

    outGlowColorG = FloatField(default_value=0.0, writable=False)
    ogg = outGlowColorG

    outGlowColorB = FloatField(default_value=0.0, writable=False)
    ogb = outGlowColorB


class OutGlowColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutGlowColorPlugOperator]
):
    __slots__ = ()

    outGlowColorR = FloatField(default_value=0.0, writable=False)
    ogr = outGlowColorR

    outGlowColorG = FloatField(default_value=0.0, writable=False)
    ogg = outGlowColorG

    outGlowColorB = FloatField(default_value=0.0, writable=False)
    ogb = outGlowColorB


class OutGlowColorField(
    Float3CompoundBaseField[OutGlowColorAttrOperator, OutGlowColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutGlowColorAttrOperator
    PLUG_CLS = OutGlowColorPlugOperator

    outGlowColorR = FloatField(default_value=0.0, writable=False)
    ogr = outGlowColorR

    outGlowColorG = FloatField(default_value=0.0, writable=False)
    ogg = outGlowColorG

    outGlowColorB = FloatField(default_value=0.0, writable=False)
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

    pointCameraX = FloatField(default_value=1.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=1.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=1.0)
    pz = pointCameraZ


class PointCameraAttrOperator(
    Float3CompoundBaseAttrOperator[PointCameraPlugOperator]
):
    __slots__ = ()

    pointCameraX = FloatField(default_value=1.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=1.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=1.0)
    pz = pointCameraZ


class PointCameraField(
    Float3CompoundBaseField[PointCameraAttrOperator, PointCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointCameraAttrOperator
    PLUG_CLS = PointCameraPlugOperator

    pointCameraX = FloatField(default_value=1.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=1.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=1.0)
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

    normalCameraX = FloatField(default_value=1.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=1.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
    nz = normalCameraZ


class NormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[NormalCameraPlugOperator]
):
    __slots__ = ()

    normalCameraX = FloatField(default_value=1.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=1.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
    nz = normalCameraZ


class NormalCameraField(
    Float3CompoundBaseField[NormalCameraAttrOperator, NormalCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalCameraAttrOperator
    PLUG_CLS = NormalCameraPlugOperator

    normalCameraX = FloatField(default_value=1.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=1.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
    nz = normalCameraZ


class FilterSizePlugOperator(
    Float3CompoundBasePlugOperator["FilterSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("filterSizeX", "fsx"),
        ("filterSizeY", "fsy"),
        ("filterSizeZ", "fsz"),
    )

    filterSizeX = FloatField(default_value=0.0)
    fsx = filterSizeX

    filterSizeY = FloatField(default_value=0.0)
    fsy = filterSizeY

    filterSizeZ = FloatField(default_value=0.0)
    fsz = filterSizeZ


class FilterSizeAttrOperator(
    Float3CompoundBaseAttrOperator[FilterSizePlugOperator]
):
    __slots__ = ()

    filterSizeX = FloatField(default_value=0.0)
    fsx = filterSizeX

    filterSizeY = FloatField(default_value=0.0)
    fsy = filterSizeY

    filterSizeZ = FloatField(default_value=0.0)
    fsz = filterSizeZ


class FilterSizeField(
    Float3CompoundBaseField[FilterSizeAttrOperator, FilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FilterSizeAttrOperator
    PLUG_CLS = FilterSizePlugOperator

    filterSizeX = FloatField(default_value=0.0)
    fsx = filterSizeX

    filterSizeY = FloatField(default_value=0.0)
    fsy = filterSizeY

    filterSizeZ = FloatField(default_value=0.0)
    fsz = filterSizeZ


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

    lightDirection = Float3Field(default_value=(1.0, 1.0, 1.0), readable=False)
    ld = lightDirection

    lightIntensity = Float3Field(default_value=(1.0, 1.0, 1.0), readable=False)
    li = lightIntensity

    lightAmbient = BoolField(default_value=True, readable=False)
    la = lightAmbient

    lightDiffuse = BoolField(default_value=True, readable=False)
    ldf = lightDiffuse

    lightSpecular = BoolField(default_value=False, readable=False)
    ls = lightSpecular

    lightShadowFraction = FloatField(default_value=0.0, readable=False)
    lsf = lightShadowFraction

    preShadowIntensity = FloatField(default_value=0.0, readable=False)
    psi = preShadowIntensity

    lightBlindData = AddrField(default_value=0.0, readable=False)
    lbd = lightBlindData


class LightDataArrayAttrOperator(
    LightDataAttrOperator[LightDataArrayPlugOperator]
):
    __slots__ = ()

    lightDirection = Float3Field(default_value=(1.0, 1.0, 1.0), readable=False)
    ld = lightDirection

    lightIntensity = Float3Field(default_value=(1.0, 1.0, 1.0), readable=False)
    li = lightIntensity

    lightAmbient = BoolField(default_value=True, readable=False)
    la = lightAmbient

    lightDiffuse = BoolField(default_value=True, readable=False)
    ldf = lightDiffuse

    lightSpecular = BoolField(default_value=False, readable=False)
    ls = lightSpecular

    lightShadowFraction = FloatField(default_value=0.0, readable=False)
    lsf = lightShadowFraction

    preShadowIntensity = FloatField(default_value=0.0, readable=False)
    psi = preShadowIntensity

    lightBlindData = AddrField(default_value=0.0, readable=False)
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

    outMatteOpacityR = FloatField(default_value=0.0, writable=False)
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField(default_value=0.0, writable=False)
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField(default_value=0.0, writable=False)
    omob = outMatteOpacityB


class OutMatteOpacityAttrOperator(
    Float3CompoundBaseAttrOperator[OutMatteOpacityPlugOperator]
):
    __slots__ = ()

    outMatteOpacityR = FloatField(default_value=0.0, writable=False)
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField(default_value=0.0, writable=False)
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField(default_value=0.0, writable=False)
    omob = outMatteOpacityB


class OutMatteOpacityField(
    Float3CompoundBaseField[
        OutMatteOpacityAttrOperator, OutMatteOpacityPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutMatteOpacityAttrOperator
    PLUG_CLS = OutMatteOpacityPlugOperator

    outMatteOpacityR = FloatField(default_value=0.0, writable=False)
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField(default_value=0.0, writable=False)
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField(default_value=0.0, writable=False)
    omob = outMatteOpacityB


class WindUVPlugOperator(Float2CompoundBasePlugOperator["WindUVAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("windU", "wiu"),
        ("windV", "wiv"),
    )

    windU = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)
    wiu = windU

    windV = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    wiv = windV


class WindUVAttrOperator(Float2CompoundBaseAttrOperator[WindUVPlugOperator]):
    __slots__ = ()

    windU = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)
    wiu = windU

    windV = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    wiv = windV


class WindUVField(
    Float2CompoundBaseField[WindUVAttrOperator, WindUVPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WindUVAttrOperator
    PLUG_CLS = WindUVPlugOperator

    windU = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)
    wiu = windU

    windV = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    wiv = windV


class WaveHeightPlugOperator(CompoundPlugOperator["WaveHeightAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("waveHeight_Position", "whp"),
        ("waveHeight_FloatValue", "whfv"),
        ("waveHeight_Interp", "whi"),
    )

    waveHeight_Position = FloatField(default_value=0.0)
    whp = waveHeight_Position

    waveHeight_FloatValue = FloatField(default_value=0.0)
    whfv = waveHeight_FloatValue

    waveHeight_Interp = WaveHeight_InterpEnumField(default_value=0)
    whi = waveHeight_Interp


class WaveHeightAttrOperator(CompoundAttrOperator[WaveHeightPlugOperator]):
    __slots__ = ()

    waveHeight_Position = FloatField(default_value=0.0)
    whp = waveHeight_Position

    waveHeight_FloatValue = FloatField(default_value=0.0)
    whfv = waveHeight_FloatValue

    waveHeight_Interp = WaveHeight_InterpEnumField(default_value=0)
    whi = waveHeight_Interp


class WaveHeightField(
    CompoundField[WaveHeightAttrOperator, WaveHeightPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WaveHeightAttrOperator
    PLUG_CLS = WaveHeightPlugOperator


class WaveTurbulencePlugOperator(
    CompoundPlugOperator["WaveTurbulenceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("waveTurbulence_Position", "wtbp"),
        ("waveTurbulence_FloatValue", "wtbfv"),
        ("waveTurbulence_Interp", "wtbi"),
    )

    waveTurbulence_Position = FloatField(default_value=0.0)
    wtbp = waveTurbulence_Position

    waveTurbulence_FloatValue = FloatField(default_value=0.0)
    wtbfv = waveTurbulence_FloatValue

    waveTurbulence_Interp = WaveTurbulence_InterpEnumField(default_value=0)
    wtbi = waveTurbulence_Interp


class WaveTurbulenceAttrOperator(
    CompoundAttrOperator[WaveTurbulencePlugOperator]
):
    __slots__ = ()

    waveTurbulence_Position = FloatField(default_value=0.0)
    wtbp = waveTurbulence_Position

    waveTurbulence_FloatValue = FloatField(default_value=0.0)
    wtbfv = waveTurbulence_FloatValue

    waveTurbulence_Interp = WaveTurbulence_InterpEnumField(default_value=0)
    wtbi = waveTurbulence_Interp


class WaveTurbulenceField(
    CompoundField[WaveTurbulenceAttrOperator, WaveTurbulencePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WaveTurbulenceAttrOperator
    PLUG_CLS = WaveTurbulencePlugOperator


class WavePeakingPlugOperator(CompoundPlugOperator["WavePeakingAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("wavePeaking_Position", "wpp"),
        ("wavePeaking_FloatValue", "wpfv"),
        ("wavePeaking_Interp", "wpi"),
    )

    wavePeaking_Position = FloatField(default_value=0.0)
    wpp = wavePeaking_Position

    wavePeaking_FloatValue = FloatField(default_value=0.0)
    wpfv = wavePeaking_FloatValue

    wavePeaking_Interp = WavePeaking_InterpEnumField(default_value=0)
    wpi = wavePeaking_Interp


class WavePeakingAttrOperator(CompoundAttrOperator[WavePeakingPlugOperator]):
    __slots__ = ()

    wavePeaking_Position = FloatField(default_value=0.0)
    wpp = wavePeaking_Position

    wavePeaking_FloatValue = FloatField(default_value=0.0)
    wpfv = wavePeaking_FloatValue

    wavePeaking_Interp = WavePeaking_InterpEnumField(default_value=0)
    wpi = wavePeaking_Interp


class WavePeakingField(
    CompoundField[WavePeakingAttrOperator, WavePeakingPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WavePeakingAttrOperator
    PLUG_CLS = WavePeakingPlugOperator


class FoamColorPlugOperator(
    Float3CompoundBasePlugOperator["FoamColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("foamColorR", "fcr"),
        ("foamColorG", "fcg"),
        ("foamColorB", "fcb"),
    )

    foamColorR = FloatField(default_value=1.0)
    fcr = foamColorR

    foamColorG = FloatField(default_value=1.0)
    fcg = foamColorG

    foamColorB = FloatField(default_value=1.0)
    fcb = foamColorB


class FoamColorAttrOperator(
    Float3CompoundBaseAttrOperator[FoamColorPlugOperator]
):
    __slots__ = ()

    foamColorR = FloatField(default_value=1.0)
    fcr = foamColorR

    foamColorG = FloatField(default_value=1.0)
    fcg = foamColorG

    foamColorB = FloatField(default_value=1.0)
    fcb = foamColorB


class FoamColorField(
    Float3CompoundBaseField[FoamColorAttrOperator, FoamColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FoamColorAttrOperator
    PLUG_CLS = FoamColorPlugOperator

    foamColorR = FloatField(default_value=1.0)
    fcr = foamColorR

    foamColorG = FloatField(default_value=1.0)
    fcg = foamColorG

    foamColorB = FloatField(default_value=1.0)
    fcb = foamColorB


class RefPointCameraPlugOperator(
    Float3CompoundBasePlugOperator["RefPointCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("refPointCameraX", "rcx"),
        ("refPointCameraY", "rcy"),
        ("refPointCameraZ", "rcz"),
    )

    refPointCameraX = FloatField(default_value=0.0)
    rcx = refPointCameraX

    refPointCameraY = FloatField(default_value=0.0)
    rcy = refPointCameraY

    refPointCameraZ = FloatField(default_value=0.0)
    rcz = refPointCameraZ


class RefPointCameraAttrOperator(
    Float3CompoundBaseAttrOperator[RefPointCameraPlugOperator]
):
    __slots__ = ()

    refPointCameraX = FloatField(default_value=0.0)
    rcx = refPointCameraX

    refPointCameraY = FloatField(default_value=0.0)
    rcy = refPointCameraY

    refPointCameraZ = FloatField(default_value=0.0)
    rcz = refPointCameraZ


class RefPointCameraField(
    Float3CompoundBaseField[
        RefPointCameraAttrOperator, RefPointCameraPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RefPointCameraAttrOperator
    PLUG_CLS = RefPointCameraPlugOperator

    refPointCameraX = FloatField(default_value=0.0)
    rcx = refPointCameraX

    refPointCameraY = FloatField(default_value=0.0)
    rcy = refPointCameraY

    refPointCameraZ = FloatField(default_value=0.0)
    rcz = refPointCameraZ
