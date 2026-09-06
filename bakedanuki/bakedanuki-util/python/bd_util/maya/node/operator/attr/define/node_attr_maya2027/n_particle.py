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
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.unit.time import TimeField
from ..std.at.typed import TypedField
from ..std.dt.double_array import DataDoubleArrayField
from ..std.dt.string import DataStringField
from ..std.dt.string_array import DataStringArrayField
from ..std.dt.vector_array import DataVectorArrayField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
)


class FieldScale_fieldScale_InterpEnumPlugOperator(
    EnumPlugOperator["FieldScale_fieldScale_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class FieldScale_fieldScale_InterpEnumAttrOperator(
    EnumAttrOperator[FieldScale_fieldScale_InterpEnumPlugOperator]
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


class FieldScale_fieldScale_InterpEnumField(
    EnumField[
        FieldScale_fieldScale_InterpEnumAttrOperator,
        FieldScale_fieldScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = FieldScale_fieldScale_InterpEnumAttrOperator
    PLUG_CLS = FieldScale_fieldScale_InterpEnumPlugOperator


class PointFieldDropoff_pointFieldDropoff_InterpEnumPlugOperator(
    EnumPlugOperator[
        "PointFieldDropoff_pointFieldDropoff_InterpEnumAttrOperator"
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class PointFieldDropoff_pointFieldDropoff_InterpEnumAttrOperator(
    EnumAttrOperator[
        PointFieldDropoff_pointFieldDropoff_InterpEnumPlugOperator
    ]
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


class PointFieldDropoff_pointFieldDropoff_InterpEnumField(
    EnumField[
        PointFieldDropoff_pointFieldDropoff_InterpEnumAttrOperator,
        PointFieldDropoff_pointFieldDropoff_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = PointFieldDropoff_pointFieldDropoff_InterpEnumAttrOperator
    PLUG_CLS = PointFieldDropoff_pointFieldDropoff_InterpEnumPlugOperator


class ViscosityScale_viscosityScale_InterpEnumPlugOperator(
    EnumPlugOperator["ViscosityScale_viscosityScale_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ViscosityScale_viscosityScale_InterpEnumAttrOperator(
    EnumAttrOperator[ViscosityScale_viscosityScale_InterpEnumPlugOperator]
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


class ViscosityScale_viscosityScale_InterpEnumField(
    EnumField[
        ViscosityScale_viscosityScale_InterpEnumAttrOperator,
        ViscosityScale_viscosityScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ViscosityScale_viscosityScale_InterpEnumAttrOperator
    PLUG_CLS = ViscosityScale_viscosityScale_InterpEnumPlugOperator


class SurfaceTensionScale_surfaceTensionScale_InterpEnumPlugOperator(
    EnumPlugOperator[
        "SurfaceTensionScale_surfaceTensionScale_InterpEnumAttrOperator"
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class SurfaceTensionScale_surfaceTensionScale_InterpEnumAttrOperator(
    EnumAttrOperator[
        SurfaceTensionScale_surfaceTensionScale_InterpEnumPlugOperator
    ]
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


class SurfaceTensionScale_surfaceTensionScale_InterpEnumField(
    EnumField[
        SurfaceTensionScale_surfaceTensionScale_InterpEnumAttrOperator,
        SurfaceTensionScale_surfaceTensionScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = SurfaceTensionScale_surfaceTensionScale_InterpEnumAttrOperator
    PLUG_CLS = SurfaceTensionScale_surfaceTensionScale_InterpEnumPlugOperator


class RadiusScale_radiusScale_InterpEnumPlugOperator(
    EnumPlugOperator["RadiusScale_radiusScale_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class RadiusScale_radiusScale_InterpEnumAttrOperator(
    EnumAttrOperator[RadiusScale_radiusScale_InterpEnumPlugOperator]
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


class RadiusScale_radiusScale_InterpEnumField(
    EnumField[
        RadiusScale_radiusScale_InterpEnumAttrOperator,
        RadiusScale_radiusScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = RadiusScale_radiusScale_InterpEnumAttrOperator
    PLUG_CLS = RadiusScale_radiusScale_InterpEnumPlugOperator


class MassScale_massScale_InterpEnumPlugOperator(
    EnumPlugOperator["MassScale_massScale_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class MassScale_massScale_InterpEnumAttrOperator(
    EnumAttrOperator[MassScale_massScale_InterpEnumPlugOperator]
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


class MassScale_massScale_InterpEnumField(
    EnumField[
        MassScale_massScale_InterpEnumAttrOperator,
        MassScale_massScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = MassScale_massScale_InterpEnumAttrOperator
    PLUG_CLS = MassScale_massScale_InterpEnumPlugOperator


class PointFieldScale_pointFieldScale_InterpEnumPlugOperator(
    EnumPlugOperator["PointFieldScale_pointFieldScale_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class PointFieldScale_pointFieldScale_InterpEnumAttrOperator(
    EnumAttrOperator[PointFieldScale_pointFieldScale_InterpEnumPlugOperator]
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


class PointFieldScale_pointFieldScale_InterpEnumField(
    EnumField[
        PointFieldScale_pointFieldScale_InterpEnumAttrOperator,
        PointFieldScale_pointFieldScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = PointFieldScale_pointFieldScale_InterpEnumAttrOperator
    PLUG_CLS = PointFieldScale_pointFieldScale_InterpEnumPlugOperator


class FrictionScale_frictionScale_InterpEnumPlugOperator(
    EnumPlugOperator["FrictionScale_frictionScale_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class FrictionScale_frictionScale_InterpEnumAttrOperator(
    EnumAttrOperator[FrictionScale_frictionScale_InterpEnumPlugOperator]
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


class FrictionScale_frictionScale_InterpEnumField(
    EnumField[
        FrictionScale_frictionScale_InterpEnumAttrOperator,
        FrictionScale_frictionScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = FrictionScale_frictionScale_InterpEnumAttrOperator
    PLUG_CLS = FrictionScale_frictionScale_InterpEnumPlugOperator


class StickinessScale_stickinessScale_InterpEnumPlugOperator(
    EnumPlugOperator["StickinessScale_stickinessScale_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class StickinessScale_stickinessScale_InterpEnumAttrOperator(
    EnumAttrOperator[StickinessScale_stickinessScale_InterpEnumPlugOperator]
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


class StickinessScale_stickinessScale_InterpEnumField(
    EnumField[
        StickinessScale_stickinessScale_InterpEnumAttrOperator,
        StickinessScale_stickinessScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = StickinessScale_stickinessScale_InterpEnumAttrOperator
    PLUG_CLS = StickinessScale_stickinessScale_InterpEnumPlugOperator


class CollideStrengthScale_collideStrengthScale_InterpEnumPlugOperator(
    EnumPlugOperator[
        "CollideStrengthScale_collideStrengthScale_InterpEnumAttrOperator"
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CollideStrengthScale_collideStrengthScale_InterpEnumAttrOperator(
    EnumAttrOperator[
        CollideStrengthScale_collideStrengthScale_InterpEnumPlugOperator
    ]
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


class CollideStrengthScale_collideStrengthScale_InterpEnumField(
    EnumField[
        CollideStrengthScale_collideStrengthScale_InterpEnumAttrOperator,
        CollideStrengthScale_collideStrengthScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollideStrengthScale_collideStrengthScale_InterpEnumAttrOperator
    PLUG_CLS = CollideStrengthScale_collideStrengthScale_InterpEnumPlugOperator


class BounceScale_bounceScale_InterpEnumPlugOperator(
    EnumPlugOperator["BounceScale_bounceScale_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class BounceScale_bounceScale_InterpEnumAttrOperator(
    EnumAttrOperator[BounceScale_bounceScale_InterpEnumPlugOperator]
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


class BounceScale_bounceScale_InterpEnumField(
    EnumField[
        BounceScale_bounceScale_InterpEnumAttrOperator,
        BounceScale_bounceScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = BounceScale_bounceScale_InterpEnumAttrOperator
    PLUG_CLS = BounceScale_bounceScale_InterpEnumPlugOperator


class OpacityScale_opacityScale_InterpEnumPlugOperator(
    EnumPlugOperator["OpacityScale_opacityScale_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class OpacityScale_opacityScale_InterpEnumAttrOperator(
    EnumAttrOperator[OpacityScale_opacityScale_InterpEnumPlugOperator]
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


class OpacityScale_opacityScale_InterpEnumField(
    EnumField[
        OpacityScale_opacityScale_InterpEnumAttrOperator,
        OpacityScale_opacityScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = OpacityScale_opacityScale_InterpEnumAttrOperator
    PLUG_CLS = OpacityScale_opacityScale_InterpEnumPlugOperator


class Color_color_InterpEnumPlugOperator(
    EnumPlugOperator["Color_color_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Color_color_InterpEnumAttrOperator(
    EnumAttrOperator[Color_color_InterpEnumPlugOperator]
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


class Color_color_InterpEnumField(
    EnumField[
        Color_color_InterpEnumAttrOperator, Color_color_InterpEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Color_color_InterpEnumAttrOperator
    PLUG_CLS = Color_color_InterpEnumPlugOperator


class Incandescence_incandescence_InterpEnumPlugOperator(
    EnumPlugOperator["Incandescence_incandescence_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Incandescence_incandescence_InterpEnumAttrOperator(
    EnumAttrOperator[Incandescence_incandescence_InterpEnumPlugOperator]
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


class Incandescence_incandescence_InterpEnumField(
    EnumField[
        Incandescence_incandescence_InterpEnumAttrOperator,
        Incandescence_incandescence_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Incandescence_incandescence_InterpEnumAttrOperator
    PLUG_CLS = Incandescence_incandescence_InterpEnumPlugOperator


class CompInstObjGroups_compObjectGroupsPlugOperator(
    CompoundPlugOperator["CompInstObjGroups_compObjectGroupsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("compObjectGrpCompList", "cgcl"),
        ("compObjectGroupId", "cgid"),
    )

    compObjectGrpCompList = TypedField()
    cgcl = compObjectGrpCompList

    compObjectGroupId = LongField(default_value=0)
    cgid = compObjectGroupId


class CompInstObjGroups_compObjectGroupsAttrOperator(
    CompoundAttrOperator[CompInstObjGroups_compObjectGroupsPlugOperator]
):
    __slots__ = ()

    compObjectGrpCompList = TypedField()
    cgcl = compObjectGrpCompList

    compObjectGroupId = LongField(default_value=0)
    cgid = compObjectGroupId


class CompInstObjGroups_compObjectGroupsField(
    CompoundField[
        CompInstObjGroups_compObjectGroupsAttrOperator,
        CompInstObjGroups_compObjectGroupsPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CompInstObjGroups_compObjectGroupsAttrOperator
    PLUG_CLS = CompInstObjGroups_compObjectGroupsPlugOperator


class Color_color_ColorPlugOperator(
    Float3CompoundBasePlugOperator["Color_color_ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("color_ColorR", "clcr"),
        ("color_ColorG", "clcg"),
        ("color_ColorB", "clcb"),
    )

    color_ColorR = FloatField(default_value=0.0)
    clcr = color_ColorR

    color_ColorG = FloatField(default_value=0.0)
    clcg = color_ColorG

    color_ColorB = FloatField(default_value=0.0)
    clcb = color_ColorB


class Color_color_ColorAttrOperator(
    Float3CompoundBaseAttrOperator[Color_color_ColorPlugOperator]
):
    __slots__ = ()

    color_ColorR = FloatField(default_value=0.0)
    clcr = color_ColorR

    color_ColorG = FloatField(default_value=0.0)
    clcg = color_ColorG

    color_ColorB = FloatField(default_value=0.0)
    clcb = color_ColorB


class Color_color_ColorField(
    Float3CompoundBaseField[
        Color_color_ColorAttrOperator, Color_color_ColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Color_color_ColorAttrOperator
    PLUG_CLS = Color_color_ColorPlugOperator

    color_ColorR = FloatField(default_value=0.0)
    clcr = color_ColorR

    color_ColorG = FloatField(default_value=0.0)
    clcg = color_ColorG

    color_ColorB = FloatField(default_value=0.0)
    clcb = color_ColorB


class Incandescence_incandescence_ColorPlugOperator(
    Float3CompoundBasePlugOperator[
        "Incandescence_incandescence_ColorAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("incandescence_ColorR", "incacr"),
        ("incandescence_ColorG", "incacg"),
        ("incandescence_ColorB", "incacb"),
    )

    incandescence_ColorR = FloatField(default_value=0.0)
    incacr = incandescence_ColorR

    incandescence_ColorG = FloatField(default_value=0.0)
    incacg = incandescence_ColorG

    incandescence_ColorB = FloatField(default_value=0.0)
    incacb = incandescence_ColorB


class Incandescence_incandescence_ColorAttrOperator(
    Float3CompoundBaseAttrOperator[
        Incandescence_incandescence_ColorPlugOperator
    ]
):
    __slots__ = ()

    incandescence_ColorR = FloatField(default_value=0.0)
    incacr = incandescence_ColorR

    incandescence_ColorG = FloatField(default_value=0.0)
    incacg = incandescence_ColorG

    incandescence_ColorB = FloatField(default_value=0.0)
    incacb = incandescence_ColorB


class Incandescence_incandescence_ColorField(
    Float3CompoundBaseField[
        Incandescence_incandescence_ColorAttrOperator,
        Incandescence_incandescence_ColorPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Incandescence_incandescence_ColorAttrOperator
    PLUG_CLS = Incandescence_incandescence_ColorPlugOperator

    incandescence_ColorR = FloatField(default_value=0.0)
    incacr = incandescence_ColorR

    incandescence_ColorG = FloatField(default_value=0.0)
    incacg = incandescence_ColorG

    incandescence_ColorB = FloatField(default_value=0.0)
    incacb = incandescence_ColorB


class CompInstObjGroupsPlugOperator(
    CompoundPlugOperator["CompInstObjGroupsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("compObjectGroups", "cog"),)

    compObjectGroups = CompInstObjGroups_compObjectGroupsField(multi=True)
    cog = compObjectGroups


class CompInstObjGroupsAttrOperator(
    CompoundAttrOperator[CompInstObjGroupsPlugOperator]
):
    __slots__ = ()

    compObjectGroups = CompInstObjGroups_compObjectGroupsField(multi=True)
    cog = compObjectGroups


class CompInstObjGroupsField(
    CompoundField[CompInstObjGroupsAttrOperator, CompInstObjGroupsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompInstObjGroupsAttrOperator
    PLUG_CLS = CompInstObjGroupsPlugOperator


class ComponentTagsPlugOperator(
    CompoundPlugOperator["ComponentTagsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("componentTagName", "gtagnm"),
        ("componentTagContents", "gtagcmp"),
    )

    componentTagName = DataStringField()
    gtagnm = componentTagName

    componentTagContents = TypedField()
    gtagcmp = componentTagContents


class ComponentTagsAttrOperator(
    CompoundAttrOperator[ComponentTagsPlugOperator]
):
    __slots__ = ()

    componentTagName = DataStringField()
    gtagnm = componentTagName

    componentTagContents = TypedField()
    gtagcmp = componentTagContents


class ComponentTagsField(
    CompoundField[ComponentTagsAttrOperator, ComponentTagsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ComponentTagsAttrOperator
    PLUG_CLS = ComponentTagsPlugOperator


class CentroidPlugOperator(
    Double3CompoundBasePlugOperator["CentroidAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("centroidX", "ctdx"),
        ("centroidY", "ctdy"),
        ("centroidZ", "ctdz"),
    )

    centroidX = DoubleField(default_value=0.0, writable=False)
    ctdx = centroidX

    centroidY = DoubleField(default_value=0.0, writable=False)
    ctdy = centroidY

    centroidZ = DoubleField(default_value=0.0, writable=False)
    ctdz = centroidZ


class CentroidAttrOperator(
    Double3CompoundBaseAttrOperator[CentroidPlugOperator]
):
    __slots__ = ()

    centroidX = DoubleField(default_value=0.0, writable=False)
    ctdx = centroidX

    centroidY = DoubleField(default_value=0.0, writable=False)
    ctdy = centroidY

    centroidZ = DoubleField(default_value=0.0, writable=False)
    ctdz = centroidZ


class CentroidField(
    Double3CompoundBaseField[CentroidAttrOperator, CentroidPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CentroidAttrOperator
    PLUG_CLS = CentroidPlugOperator

    centroidX = DoubleField(default_value=0.0, writable=False)
    ctdx = centroidX

    centroidY = DoubleField(default_value=0.0, writable=False)
    ctdy = centroidY

    centroidZ = DoubleField(default_value=0.0, writable=False)
    ctdz = centroidZ


class WorldCentroidPlugOperator(
    Double3CompoundBasePlugOperator["WorldCentroidAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldCentroidX", "wctx"),
        ("worldCentroidY", "wcty"),
        ("worldCentroidZ", "wctz"),
    )

    worldCentroidX = DoubleField(default_value=0.0, writable=False)
    wctx = worldCentroidX

    worldCentroidY = DoubleField(default_value=0.0, writable=False)
    wcty = worldCentroidY

    worldCentroidZ = DoubleField(default_value=0.0, writable=False)
    wctz = worldCentroidZ


class WorldCentroidAttrOperator(
    Double3CompoundBaseAttrOperator[WorldCentroidPlugOperator]
):
    __slots__ = ()

    worldCentroidX = DoubleField(default_value=0.0, writable=False)
    wctx = worldCentroidX

    worldCentroidY = DoubleField(default_value=0.0, writable=False)
    wcty = worldCentroidY

    worldCentroidZ = DoubleField(default_value=0.0, writable=False)
    wctz = worldCentroidZ


class WorldCentroidField(
    Double3CompoundBaseField[
        WorldCentroidAttrOperator, WorldCentroidPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = WorldCentroidAttrOperator
    PLUG_CLS = WorldCentroidPlugOperator

    worldCentroidX = DoubleField(default_value=0.0, writable=False)
    wctx = worldCentroidX

    worldCentroidY = DoubleField(default_value=0.0, writable=False)
    wcty = worldCentroidY

    worldCentroidZ = DoubleField(default_value=0.0, writable=False)
    wctz = worldCentroidZ


class CachedWorldCentroidPlugOperator(
    Double3CompoundBasePlugOperator["CachedWorldCentroidAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cachedWorldCentroidX", "cwcx"),
        ("cachedWorldCentroidY", "cwcy"),
        ("cachedWorldCentroidZ", "cwcz"),
    )

    cachedWorldCentroidX = DoubleField(default_value=0.0, writable=False)
    cwcx = cachedWorldCentroidX

    cachedWorldCentroidY = DoubleField(default_value=0.0, writable=False)
    cwcy = cachedWorldCentroidY

    cachedWorldCentroidZ = DoubleField(default_value=0.0, writable=False)
    cwcz = cachedWorldCentroidZ


class CachedWorldCentroidAttrOperator(
    Double3CompoundBaseAttrOperator[CachedWorldCentroidPlugOperator]
):
    __slots__ = ()

    cachedWorldCentroidX = DoubleField(default_value=0.0, writable=False)
    cwcx = cachedWorldCentroidX

    cachedWorldCentroidY = DoubleField(default_value=0.0, writable=False)
    cwcy = cachedWorldCentroidY

    cachedWorldCentroidZ = DoubleField(default_value=0.0, writable=False)
    cwcz = cachedWorldCentroidZ


class CachedWorldCentroidField(
    Double3CompoundBaseField[
        CachedWorldCentroidAttrOperator, CachedWorldCentroidPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CachedWorldCentroidAttrOperator
    PLUG_CLS = CachedWorldCentroidPlugOperator

    cachedWorldCentroidX = DoubleField(default_value=0.0, writable=False)
    cwcx = cachedWorldCentroidX

    cachedWorldCentroidY = DoubleField(default_value=0.0, writable=False)
    cwcy = cachedWorldCentroidY

    cachedWorldCentroidZ = DoubleField(default_value=0.0, writable=False)
    cwcz = cachedWorldCentroidZ


class IdMappingPlugOperator(CompoundPlugOperator["IdMappingAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sortedId", "sid"),
        ("idIndex", "idix"),
    )

    sortedId = TypedField(writable=False)
    sid = sortedId

    idIndex = TypedField(writable=False)
    idix = idIndex


class IdMappingAttrOperator(CompoundAttrOperator[IdMappingPlugOperator]):
    __slots__ = ()

    sortedId = TypedField(writable=False)
    sid = sortedId

    idIndex = TypedField(writable=False)
    idix = idIndex


class IdMappingField(
    CompoundField[IdMappingAttrOperator, IdMappingPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IdMappingAttrOperator
    PLUG_CLS = IdMappingPlugOperator

    sortedId = TypedField(writable=False)
    sid = sortedId

    idIndex = TypedField(writable=False)
    idix = idIndex


class RandStatePlugOperator(
    Long3CompoundBasePlugOperator["RandStateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("randStateX", "rstx"),
        ("randStateY", "rsty"),
        ("randStateZ", "rstz"),
    )

    randStateX = LongField(default_value=0)
    rstx = randStateX

    randStateY = LongField(default_value=0)
    rsty = randStateY

    randStateZ = LongField(default_value=0)
    rstz = randStateZ


class RandStateAttrOperator(
    Long3CompoundBaseAttrOperator[RandStatePlugOperator]
):
    __slots__ = ()

    randStateX = LongField(default_value=0)
    rstx = randStateX

    randStateY = LongField(default_value=0)
    rsty = randStateY

    randStateZ = LongField(default_value=0)
    rstz = randStateZ


class RandStateField(
    Long3CompoundBaseField[RandStateAttrOperator, RandStatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RandStateAttrOperator
    PLUG_CLS = RandStatePlugOperator

    randStateX = LongField(default_value=0)
    rstx = randStateX

    randStateY = LongField(default_value=0)
    rsty = randStateY

    randStateZ = LongField(default_value=0)
    rstz = randStateZ


class FieldDataPlugOperator(CompoundPlugOperator["FieldDataAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fieldDataPosition", "fdp"),
        ("fieldDataVelocity", "fdv"),
        ("fieldDataMass", "fdm"),
        ("fieldDataDeltaTime", "fdt"),
    )

    fieldDataPosition = DataVectorArrayField(writable=False)
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField(writable=False)
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField(writable=False)
    fdm = fieldDataMass

    fieldDataDeltaTime = TimeField(default_value=0.0, writable=False)
    fdt = fieldDataDeltaTime


class FieldDataAttrOperator(CompoundAttrOperator[FieldDataPlugOperator]):
    __slots__ = ()

    fieldDataPosition = DataVectorArrayField(writable=False)
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField(writable=False)
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField(writable=False)
    fdm = fieldDataMass

    fieldDataDeltaTime = TimeField(default_value=0.0, writable=False)
    fdt = fieldDataDeltaTime


class FieldDataField(
    CompoundField[FieldDataAttrOperator, FieldDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FieldDataAttrOperator
    PLUG_CLS = FieldDataPlugOperator

    fieldDataPosition = DataVectorArrayField(writable=False)
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField(writable=False)
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField(writable=False)
    fdm = fieldDataMass

    fieldDataDeltaTime = TimeField(default_value=0.0, writable=False)
    fdt = fieldDataDeltaTime


class EmitterDataPlugOperator(CompoundPlugOperator["EmitterDataAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("emitterDataPosition", "edp"),
        ("emitterDataVelocity", "edv"),
        ("emitterDataDeltaTime", "edt"),
    )

    emitterDataPosition = DataVectorArrayField(writable=False)
    edp = emitterDataPosition

    emitterDataVelocity = DataVectorArrayField(writable=False)
    edv = emitterDataVelocity

    emitterDataDeltaTime = TimeField(default_value=0.0, writable=False)
    edt = emitterDataDeltaTime


class EmitterDataAttrOperator(CompoundAttrOperator[EmitterDataPlugOperator]):
    __slots__ = ()

    emitterDataPosition = DataVectorArrayField(writable=False)
    edp = emitterDataPosition

    emitterDataVelocity = DataVectorArrayField(writable=False)
    edv = emitterDataVelocity

    emitterDataDeltaTime = TimeField(default_value=0.0, writable=False)
    edt = emitterDataDeltaTime


class EmitterDataField(
    CompoundField[EmitterDataAttrOperator, EmitterDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmitterDataAttrOperator
    PLUG_CLS = EmitterDataPlugOperator

    emitterDataPosition = DataVectorArrayField(writable=False)
    edp = emitterDataPosition

    emitterDataVelocity = DataVectorArrayField(writable=False)
    edv = emitterDataVelocity

    emitterDataDeltaTime = TimeField(default_value=0.0, writable=False)
    edt = emitterDataDeltaTime


class CollisionDataPlugOperator(
    CompoundPlugOperator["CollisionDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionGeometry", "cge"),
        ("collisionResilience", "crs"),
        ("collisionFriction", "cfr"),
        ("collisionOffset", "cof"),
    )

    collisionGeometry = TypedField(multi=True)
    cge = collisionGeometry

    collisionResilience = DoubleField(multi=True, default_value=0.0)
    crs = collisionResilience

    collisionFriction = DoubleField(multi=True, default_value=0.0)
    cfr = collisionFriction

    collisionOffset = DoubleField(multi=True, default_value=0.01)
    cof = collisionOffset


class CollisionDataAttrOperator(
    CompoundAttrOperator[CollisionDataPlugOperator]
):
    __slots__ = ()

    collisionGeometry = TypedField(multi=True)
    cge = collisionGeometry

    collisionResilience = DoubleField(multi=True, default_value=0.0)
    crs = collisionResilience

    collisionFriction = DoubleField(multi=True, default_value=0.0)
    cfr = collisionFriction

    collisionOffset = DoubleField(multi=True, default_value=0.01)
    cof = collisionOffset


class CollisionDataField(
    CompoundField[CollisionDataAttrOperator, CollisionDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollisionDataAttrOperator
    PLUG_CLS = CollisionDataPlugOperator

    collisionGeometry = TypedField(multi=True)
    cge = collisionGeometry

    collisionResilience = DoubleField(multi=True, default_value=0.0)
    crs = collisionResilience

    collisionFriction = DoubleField(multi=True, default_value=0.0)
    cfr = collisionFriction

    collisionOffset = DoubleField(multi=True, default_value=0.01)
    cof = collisionOffset


class EventRandStatePlugOperator(
    Long3CompoundBasePlugOperator["EventRandStateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eventRandStateX", "ersx"),
        ("eventRandStateY", "ersy"),
        ("eventRandStateZ", "ersz"),
    )

    eventRandStateX = LongField(default_value=0)
    ersx = eventRandStateX

    eventRandStateY = LongField(default_value=0)
    ersy = eventRandStateY

    eventRandStateZ = LongField(default_value=0)
    ersz = eventRandStateZ


class EventRandStateAttrOperator(
    Long3CompoundBaseAttrOperator[EventRandStatePlugOperator]
):
    __slots__ = ()

    eventRandStateX = LongField(default_value=0)
    ersx = eventRandStateX

    eventRandStateY = LongField(default_value=0)
    ersy = eventRandStateY

    eventRandStateZ = LongField(default_value=0)
    ersz = eventRandStateZ


class EventRandStateField(
    Long3CompoundBaseField[
        EventRandStateAttrOperator, EventRandStatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = EventRandStateAttrOperator
    PLUG_CLS = EventRandStatePlugOperator

    eventRandStateX = LongField(default_value=0)
    ersx = eventRandStateX

    eventRandStateY = LongField(default_value=0)
    ersy = eventRandStateY

    eventRandStateZ = LongField(default_value=0)
    ersz = eventRandStateZ


class InstanceDataPlugOperator(
    CompoundPlugOperator["InstanceDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("instanceAttributeMapping", "iam"),
        ("instancePointData", "ipd"),
    )

    instanceAttributeMapping = DataStringArrayField()
    iam = instanceAttributeMapping

    instancePointData = TypedField()
    ipd = instancePointData


class InstanceDataAttrOperator(CompoundAttrOperator[InstanceDataPlugOperator]):
    __slots__ = ()

    instanceAttributeMapping = DataStringArrayField()
    iam = instanceAttributeMapping

    instancePointData = TypedField()
    ipd = instancePointData


class InstanceDataField(
    CompoundField[InstanceDataAttrOperator, InstanceDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InstanceDataAttrOperator
    PLUG_CLS = InstanceDataPlugOperator


class LocalForcePlugOperator(
    Float3CompoundBasePlugOperator["LocalForceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localForceX", "lfcx"),
        ("localForceY", "lfcy"),
        ("localForceZ", "lfcz"),
    )

    localForceX = FloatField(default_value=0.0)
    lfcx = localForceX

    localForceY = FloatField(default_value=0.0)
    lfcy = localForceY

    localForceZ = FloatField(default_value=0.0)
    lfcz = localForceZ


class LocalForceAttrOperator(
    Float3CompoundBaseAttrOperator[LocalForcePlugOperator]
):
    __slots__ = ()

    localForceX = FloatField(default_value=0.0)
    lfcx = localForceX

    localForceY = FloatField(default_value=0.0)
    lfcy = localForceY

    localForceZ = FloatField(default_value=0.0)
    lfcz = localForceZ


class LocalForceField(
    Float3CompoundBaseField[LocalForceAttrOperator, LocalForcePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LocalForceAttrOperator
    PLUG_CLS = LocalForcePlugOperator

    localForceX = FloatField(default_value=0.0)
    lfcx = localForceX

    localForceY = FloatField(default_value=0.0)
    lfcy = localForceY

    localForceZ = FloatField(default_value=0.0)
    lfcz = localForceZ


class LocalWindPlugOperator(
    Float3CompoundBasePlugOperator["LocalWindAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localWindX", "lwnx"),
        ("localWindY", "lwny"),
        ("localWindZ", "lwnz"),
    )

    localWindX = FloatField(default_value=0.0)
    lwnx = localWindX

    localWindY = FloatField(default_value=0.0)
    lwny = localWindY

    localWindZ = FloatField(default_value=0.0)
    lwnz = localWindZ


class LocalWindAttrOperator(
    Float3CompoundBaseAttrOperator[LocalWindPlugOperator]
):
    __slots__ = ()

    localWindX = FloatField(default_value=0.0)
    lwnx = localWindX

    localWindY = FloatField(default_value=0.0)
    lwny = localWindY

    localWindZ = FloatField(default_value=0.0)
    lwnz = localWindZ


class LocalWindField(
    Float3CompoundBaseField[LocalWindAttrOperator, LocalWindPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LocalWindAttrOperator
    PLUG_CLS = LocalWindPlugOperator

    localWindX = FloatField(default_value=0.0)
    lwnx = localWindX

    localWindY = FloatField(default_value=0.0)
    lwny = localWindY

    localWindZ = FloatField(default_value=0.0)
    lwnz = localWindZ


class FieldScalePlugOperator(CompoundPlugOperator["FieldScaleAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fieldScale_Position", "fscp"),
        ("fieldScale_FloatValue", "fscfv"),
        ("fieldScale_Interp", "fsci"),
    )

    fieldScale_Position = FloatField(default_value=0.0)
    fscp = fieldScale_Position

    fieldScale_FloatValue = FloatField(default_value=0.0)
    fscfv = fieldScale_FloatValue

    fieldScale_Interp = FieldScale_fieldScale_InterpEnumField(default_value=0)
    fsci = fieldScale_Interp


class FieldScaleAttrOperator(CompoundAttrOperator[FieldScalePlugOperator]):
    __slots__ = ()

    fieldScale_Position = FloatField(default_value=0.0)
    fscp = fieldScale_Position

    fieldScale_FloatValue = FloatField(default_value=0.0)
    fscfv = fieldScale_FloatValue

    fieldScale_Interp = FieldScale_fieldScale_InterpEnumField(default_value=0)
    fsci = fieldScale_Interp


class FieldScaleField(
    CompoundField[FieldScaleAttrOperator, FieldScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FieldScaleAttrOperator
    PLUG_CLS = FieldScalePlugOperator


class PointFieldDropoffPlugOperator(
    CompoundPlugOperator["PointFieldDropoffAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointFieldDropoff_Position", "pfdop"),
        ("pointFieldDropoff_FloatValue", "pfdofv"),
        ("pointFieldDropoff_Interp", "pfdoi"),
    )

    pointFieldDropoff_Position = FloatField(default_value=0.0)
    pfdop = pointFieldDropoff_Position

    pointFieldDropoff_FloatValue = FloatField(default_value=0.0)
    pfdofv = pointFieldDropoff_FloatValue

    pointFieldDropoff_Interp = (
        PointFieldDropoff_pointFieldDropoff_InterpEnumField(default_value=0)
    )
    pfdoi = pointFieldDropoff_Interp


class PointFieldDropoffAttrOperator(
    CompoundAttrOperator[PointFieldDropoffPlugOperator]
):
    __slots__ = ()

    pointFieldDropoff_Position = FloatField(default_value=0.0)
    pfdop = pointFieldDropoff_Position

    pointFieldDropoff_FloatValue = FloatField(default_value=0.0)
    pfdofv = pointFieldDropoff_FloatValue

    pointFieldDropoff_Interp = (
        PointFieldDropoff_pointFieldDropoff_InterpEnumField(default_value=0)
    )
    pfdoi = pointFieldDropoff_Interp


class PointFieldDropoffField(
    CompoundField[PointFieldDropoffAttrOperator, PointFieldDropoffPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointFieldDropoffAttrOperator
    PLUG_CLS = PointFieldDropoffPlugOperator


class DisplayColorPlugOperator(
    Float3CompoundBasePlugOperator["DisplayColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("displayColorR", "dcr"),
        ("displayColorG", "dcg"),
        ("displayColorB", "dcb"),
    )

    displayColorR = FloatField(default_value=1.0)
    dcr = displayColorR

    displayColorG = FloatField(default_value=0.800000011920929)
    dcg = displayColorG

    displayColorB = FloatField(default_value=0.0)
    dcb = displayColorB


class DisplayColorAttrOperator(
    Float3CompoundBaseAttrOperator[DisplayColorPlugOperator]
):
    __slots__ = ()

    displayColorR = FloatField(default_value=1.0)
    dcr = displayColorR

    displayColorG = FloatField(default_value=0.800000011920929)
    dcg = displayColorG

    displayColorB = FloatField(default_value=0.0)
    dcb = displayColorB


class DisplayColorField(
    Float3CompoundBaseField[DisplayColorAttrOperator, DisplayColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplayColorAttrOperator
    PLUG_CLS = DisplayColorPlugOperator

    displayColorR = FloatField(default_value=1.0)
    dcr = displayColorR

    displayColorG = FloatField(default_value=0.800000011920929)
    dcg = displayColorG

    displayColorB = FloatField(default_value=0.0)
    dcb = displayColorB


class ViscosityScalePlugOperator(
    CompoundPlugOperator["ViscosityScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("viscosityScale_Position", "vsscp"),
        ("viscosityScale_FloatValue", "vsscfv"),
        ("viscosityScale_Interp", "vssci"),
    )

    viscosityScale_Position = FloatField(default_value=0.0)
    vsscp = viscosityScale_Position

    viscosityScale_FloatValue = FloatField(default_value=0.0)
    vsscfv = viscosityScale_FloatValue

    viscosityScale_Interp = ViscosityScale_viscosityScale_InterpEnumField(
        default_value=0
    )
    vssci = viscosityScale_Interp


class ViscosityScaleAttrOperator(
    CompoundAttrOperator[ViscosityScalePlugOperator]
):
    __slots__ = ()

    viscosityScale_Position = FloatField(default_value=0.0)
    vsscp = viscosityScale_Position

    viscosityScale_FloatValue = FloatField(default_value=0.0)
    vsscfv = viscosityScale_FloatValue

    viscosityScale_Interp = ViscosityScale_viscosityScale_InterpEnumField(
        default_value=0
    )
    vssci = viscosityScale_Interp


class ViscosityScaleField(
    CompoundField[ViscosityScaleAttrOperator, ViscosityScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ViscosityScaleAttrOperator
    PLUG_CLS = ViscosityScalePlugOperator


class SurfaceTensionScalePlugOperator(
    CompoundPlugOperator["SurfaceTensionScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("surfaceTensionScale_Position", "stnsp"),
        ("surfaceTensionScale_FloatValue", "stnsfv"),
        ("surfaceTensionScale_Interp", "stnsi"),
    )

    surfaceTensionScale_Position = FloatField(default_value=0.0)
    stnsp = surfaceTensionScale_Position

    surfaceTensionScale_FloatValue = FloatField(default_value=0.0)
    stnsfv = surfaceTensionScale_FloatValue

    surfaceTensionScale_Interp = (
        SurfaceTensionScale_surfaceTensionScale_InterpEnumField(
            default_value=0
        )
    )
    stnsi = surfaceTensionScale_Interp


class SurfaceTensionScaleAttrOperator(
    CompoundAttrOperator[SurfaceTensionScalePlugOperator]
):
    __slots__ = ()

    surfaceTensionScale_Position = FloatField(default_value=0.0)
    stnsp = surfaceTensionScale_Position

    surfaceTensionScale_FloatValue = FloatField(default_value=0.0)
    stnsfv = surfaceTensionScale_FloatValue

    surfaceTensionScale_Interp = (
        SurfaceTensionScale_surfaceTensionScale_InterpEnumField(
            default_value=0
        )
    )
    stnsi = surfaceTensionScale_Interp


class SurfaceTensionScaleField(
    CompoundField[
        SurfaceTensionScaleAttrOperator, SurfaceTensionScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SurfaceTensionScaleAttrOperator
    PLUG_CLS = SurfaceTensionScalePlugOperator


class RadiusScalePlugOperator(CompoundPlugOperator["RadiusScaleAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("radiusScale_Position", "rdcp"),
        ("radiusScale_FloatValue", "rdcfv"),
        ("radiusScale_Interp", "rdci"),
    )

    radiusScale_Position = FloatField(default_value=0.0)
    rdcp = radiusScale_Position

    radiusScale_FloatValue = FloatField(default_value=0.0)
    rdcfv = radiusScale_FloatValue

    radiusScale_Interp = RadiusScale_radiusScale_InterpEnumField(
        default_value=0
    )
    rdci = radiusScale_Interp


class RadiusScaleAttrOperator(CompoundAttrOperator[RadiusScalePlugOperator]):
    __slots__ = ()

    radiusScale_Position = FloatField(default_value=0.0)
    rdcp = radiusScale_Position

    radiusScale_FloatValue = FloatField(default_value=0.0)
    rdcfv = radiusScale_FloatValue

    radiusScale_Interp = RadiusScale_radiusScale_InterpEnumField(
        default_value=0
    )
    rdci = radiusScale_Interp


class RadiusScaleField(
    CompoundField[RadiusScaleAttrOperator, RadiusScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RadiusScaleAttrOperator
    PLUG_CLS = RadiusScalePlugOperator


class MassScalePlugOperator(CompoundPlugOperator["MassScaleAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("massScale_Position", "msscp"),
        ("massScale_FloatValue", "msscfv"),
        ("massScale_Interp", "mssci"),
    )

    massScale_Position = FloatField(default_value=0.0)
    msscp = massScale_Position

    massScale_FloatValue = FloatField(default_value=0.0)
    msscfv = massScale_FloatValue

    massScale_Interp = MassScale_massScale_InterpEnumField(default_value=0)
    mssci = massScale_Interp


class MassScaleAttrOperator(CompoundAttrOperator[MassScalePlugOperator]):
    __slots__ = ()

    massScale_Position = FloatField(default_value=0.0)
    msscp = massScale_Position

    massScale_FloatValue = FloatField(default_value=0.0)
    msscfv = massScale_FloatValue

    massScale_Interp = MassScale_massScale_InterpEnumField(default_value=0)
    mssci = massScale_Interp


class MassScaleField(
    CompoundField[MassScaleAttrOperator, MassScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MassScaleAttrOperator
    PLUG_CLS = MassScalePlugOperator


class PointFieldScalePlugOperator(
    CompoundPlugOperator["PointFieldScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointFieldScale_Position", "pfscp"),
        ("pointFieldScale_FloatValue", "pfscfv"),
        ("pointFieldScale_Interp", "pfsci"),
    )

    pointFieldScale_Position = FloatField(default_value=0.0)
    pfscp = pointFieldScale_Position

    pointFieldScale_FloatValue = FloatField(default_value=0.0)
    pfscfv = pointFieldScale_FloatValue

    pointFieldScale_Interp = PointFieldScale_pointFieldScale_InterpEnumField(
        default_value=0
    )
    pfsci = pointFieldScale_Interp


class PointFieldScaleAttrOperator(
    CompoundAttrOperator[PointFieldScalePlugOperator]
):
    __slots__ = ()

    pointFieldScale_Position = FloatField(default_value=0.0)
    pfscp = pointFieldScale_Position

    pointFieldScale_FloatValue = FloatField(default_value=0.0)
    pfscfv = pointFieldScale_FloatValue

    pointFieldScale_Interp = PointFieldScale_pointFieldScale_InterpEnumField(
        default_value=0
    )
    pfsci = pointFieldScale_Interp


class PointFieldScaleField(
    CompoundField[PointFieldScaleAttrOperator, PointFieldScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointFieldScaleAttrOperator
    PLUG_CLS = PointFieldScalePlugOperator


class FrictionScalePlugOperator(
    CompoundPlugOperator["FrictionScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("frictionScale_Position", "frscp"),
        ("frictionScale_FloatValue", "frscfv"),
        ("frictionScale_Interp", "frsci"),
    )

    frictionScale_Position = FloatField(default_value=0.0)
    frscp = frictionScale_Position

    frictionScale_FloatValue = FloatField(default_value=0.0)
    frscfv = frictionScale_FloatValue

    frictionScale_Interp = FrictionScale_frictionScale_InterpEnumField(
        default_value=0
    )
    frsci = frictionScale_Interp


class FrictionScaleAttrOperator(
    CompoundAttrOperator[FrictionScalePlugOperator]
):
    __slots__ = ()

    frictionScale_Position = FloatField(default_value=0.0)
    frscp = frictionScale_Position

    frictionScale_FloatValue = FloatField(default_value=0.0)
    frscfv = frictionScale_FloatValue

    frictionScale_Interp = FrictionScale_frictionScale_InterpEnumField(
        default_value=0
    )
    frsci = frictionScale_Interp


class FrictionScaleField(
    CompoundField[FrictionScaleAttrOperator, FrictionScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FrictionScaleAttrOperator
    PLUG_CLS = FrictionScalePlugOperator


class StickinessScalePlugOperator(
    CompoundPlugOperator["StickinessScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("stickinessScale_Position", "stscp"),
        ("stickinessScale_FloatValue", "stscfv"),
        ("stickinessScale_Interp", "stsci"),
    )

    stickinessScale_Position = FloatField(default_value=0.0)
    stscp = stickinessScale_Position

    stickinessScale_FloatValue = FloatField(default_value=0.0)
    stscfv = stickinessScale_FloatValue

    stickinessScale_Interp = StickinessScale_stickinessScale_InterpEnumField(
        default_value=0
    )
    stsci = stickinessScale_Interp


class StickinessScaleAttrOperator(
    CompoundAttrOperator[StickinessScalePlugOperator]
):
    __slots__ = ()

    stickinessScale_Position = FloatField(default_value=0.0)
    stscp = stickinessScale_Position

    stickinessScale_FloatValue = FloatField(default_value=0.0)
    stscfv = stickinessScale_FloatValue

    stickinessScale_Interp = StickinessScale_stickinessScale_InterpEnumField(
        default_value=0
    )
    stsci = stickinessScale_Interp


class StickinessScaleField(
    CompoundField[StickinessScaleAttrOperator, StickinessScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StickinessScaleAttrOperator
    PLUG_CLS = StickinessScalePlugOperator


class CollideStrengthScalePlugOperator(
    CompoundPlugOperator["CollideStrengthScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collideStrengthScale_Position", "clscp"),
        ("collideStrengthScale_FloatValue", "clscfv"),
        ("collideStrengthScale_Interp", "clsci"),
    )

    collideStrengthScale_Position = FloatField(default_value=0.0)
    clscp = collideStrengthScale_Position

    collideStrengthScale_FloatValue = FloatField(default_value=0.0)
    clscfv = collideStrengthScale_FloatValue

    collideStrengthScale_Interp = (
        CollideStrengthScale_collideStrengthScale_InterpEnumField(
            default_value=0
        )
    )
    clsci = collideStrengthScale_Interp


class CollideStrengthScaleAttrOperator(
    CompoundAttrOperator[CollideStrengthScalePlugOperator]
):
    __slots__ = ()

    collideStrengthScale_Position = FloatField(default_value=0.0)
    clscp = collideStrengthScale_Position

    collideStrengthScale_FloatValue = FloatField(default_value=0.0)
    clscfv = collideStrengthScale_FloatValue

    collideStrengthScale_Interp = (
        CollideStrengthScale_collideStrengthScale_InterpEnumField(
            default_value=0
        )
    )
    clsci = collideStrengthScale_Interp


class CollideStrengthScaleField(
    CompoundField[
        CollideStrengthScaleAttrOperator, CollideStrengthScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CollideStrengthScaleAttrOperator
    PLUG_CLS = CollideStrengthScalePlugOperator


class BounceScalePlugOperator(CompoundPlugOperator["BounceScaleAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("bounceScale_Position", "boscp"),
        ("bounceScale_FloatValue", "boscfv"),
        ("bounceScale_Interp", "bosci"),
    )

    bounceScale_Position = FloatField(default_value=0.0)
    boscp = bounceScale_Position

    bounceScale_FloatValue = FloatField(default_value=0.0)
    boscfv = bounceScale_FloatValue

    bounceScale_Interp = BounceScale_bounceScale_InterpEnumField(
        default_value=0
    )
    bosci = bounceScale_Interp


class BounceScaleAttrOperator(CompoundAttrOperator[BounceScalePlugOperator]):
    __slots__ = ()

    bounceScale_Position = FloatField(default_value=0.0)
    boscp = bounceScale_Position

    bounceScale_FloatValue = FloatField(default_value=0.0)
    boscfv = bounceScale_FloatValue

    bounceScale_Interp = BounceScale_bounceScale_InterpEnumField(
        default_value=0
    )
    bosci = bounceScale_Interp


class BounceScaleField(
    CompoundField[BounceScaleAttrOperator, BounceScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BounceScaleAttrOperator
    PLUG_CLS = BounceScalePlugOperator


class OpacityScalePlugOperator(
    CompoundPlugOperator["OpacityScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("opacityScale_Position", "opcp"),
        ("opacityScale_FloatValue", "opcfv"),
        ("opacityScale_Interp", "opci"),
    )

    opacityScale_Position = FloatField(default_value=0.0)
    opcp = opacityScale_Position

    opacityScale_FloatValue = FloatField(default_value=0.0)
    opcfv = opacityScale_FloatValue

    opacityScale_Interp = OpacityScale_opacityScale_InterpEnumField(
        default_value=0
    )
    opci = opacityScale_Interp


class OpacityScaleAttrOperator(CompoundAttrOperator[OpacityScalePlugOperator]):
    __slots__ = ()

    opacityScale_Position = FloatField(default_value=0.0)
    opcp = opacityScale_Position

    opacityScale_FloatValue = FloatField(default_value=0.0)
    opcfv = opacityScale_FloatValue

    opacityScale_Interp = OpacityScale_opacityScale_InterpEnumField(
        default_value=0
    )
    opci = opacityScale_Interp


class OpacityScaleField(
    CompoundField[OpacityScaleAttrOperator, OpacityScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OpacityScaleAttrOperator
    PLUG_CLS = OpacityScalePlugOperator


class ColorPlugOperator(CompoundPlugOperator["ColorAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("color_Position", "clp"),
        ("color_Color", "clc"),
        ("color_Interp", "cli"),
    )

    color_Position = FloatField(default_value=0.0)
    clp = color_Position

    color_Color = Color_color_ColorField(default_value=(0.0, 0.0, 0.0))
    clc = color_Color

    color_Interp = Color_color_InterpEnumField(default_value=0)
    cli = color_Interp


class ColorAttrOperator(CompoundAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    color_Position = FloatField(default_value=0.0)
    clp = color_Position

    color_Color = Color_color_ColorField(default_value=(0.0, 0.0, 0.0))
    clc = color_Color

    color_Interp = Color_color_InterpEnumField(default_value=0)
    cli = color_Interp


class ColorField(CompoundField[ColorAttrOperator, ColorPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator


class IncandescencePlugOperator(
    CompoundPlugOperator["IncandescenceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("incandescence_Position", "incap"),
        ("incandescence_Color", "incac"),
        ("incandescence_Interp", "incai"),
    )

    incandescence_Position = FloatField(default_value=0.0)
    incap = incandescence_Position

    incandescence_Color = Incandescence_incandescence_ColorField(
        default_value=(0.0, 0.0, 0.0)
    )
    incac = incandescence_Color

    incandescence_Interp = Incandescence_incandescence_InterpEnumField(
        default_value=0
    )
    incai = incandescence_Interp


class IncandescenceAttrOperator(
    CompoundAttrOperator[IncandescencePlugOperator]
):
    __slots__ = ()

    incandescence_Position = FloatField(default_value=0.0)
    incap = incandescence_Position

    incandescence_Color = Incandescence_incandescence_ColorField(
        default_value=(0.0, 0.0, 0.0)
    )
    incac = incandescence_Color

    incandescence_Interp = Incandescence_incandescence_InterpEnumField(
        default_value=0
    )
    incai = incandescence_Interp


class IncandescenceField(
    CompoundField[IncandescenceAttrOperator, IncandescencePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IncandescenceAttrOperator
    PLUG_CLS = IncandescencePlugOperator
