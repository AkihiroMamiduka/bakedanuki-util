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
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.numeric.range.short import ShortField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.at.scalar.unit.time import TimeField
from ..std.at.typed import TypedField
from ..std.dt.double_array import DataDoubleArrayField
from ..std.dt.string import DataStringField
from ..std.dt.vector_array import DataVectorArrayField
from ..custom import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
    Double2CompoundBaseAttrOperator,
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseField,
)


class ColorSet_representationEnumPlugOperator(
    EnumPlugOperator["ColorSet_representationEnumAttrOperator"]
):
    __slots__ = ()

    A = 1
    LA = 2
    RGB = 3
    RGBA = 4


class ColorSet_representationEnumAttrOperator(
    EnumAttrOperator[ColorSet_representationEnumPlugOperator]
):
    __slots__ = ()

    A = 1
    LA = 2
    RGB = 3
    RGBA = 4

    NAME_MAP = {
        A: "A",
        LA: "LA",
        RGB: "RGB",
        RGBA: "RGBA",
    }


class ColorSet_representationEnumField(
    EnumField[
        ColorSet_representationEnumAttrOperator,
        ColorSet_representationEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ColorSet_representationEnumAttrOperator
    PLUG_CLS = ColorSet_representationEnumPlugOperator


class CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumPlugOperator(
    EnumPlugOperator[
        "CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumAttrOperator"
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumAttrOperator(
    EnumAttrOperator[
        CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumPlugOperator
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


class CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumField(
    EnumField[
        CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumAttrOperator,
        CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumAttrOperator
    PLUG_CLS = CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumPlugOperator


class CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumPlugOperator(
    EnumPlugOperator[
        "CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumAttrOperator"
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumAttrOperator(
    EnumAttrOperator[
        CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumPlugOperator
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


class CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumField(
    EnumField[
        CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumAttrOperator,
        CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumAttrOperator
    PLUG_CLS = CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumPlugOperator


class CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumPlugOperator(
    EnumPlugOperator[
        "CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumAttrOperator"
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumAttrOperator(
    EnumAttrOperator[
        CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumPlugOperator
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


class CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumField(
    EnumField[
        CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumAttrOperator,
        CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumAttrOperator
    PLUG_CLS = CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumPlugOperator


class CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumPlugOperator(
    EnumPlugOperator[
        "CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumAttrOperator"
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumAttrOperator(
    EnumAttrOperator[
        CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumPlugOperator
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


class CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumField(
    EnumField[
        CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumAttrOperator,
        CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumAttrOperator
    PLUG_CLS = CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumPlugOperator


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


class Opacity_opacity_InterpEnumPlugOperator(
    EnumPlugOperator["Opacity_opacity_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Opacity_opacity_InterpEnumAttrOperator(
    EnumAttrOperator[Opacity_opacity_InterpEnumPlugOperator]
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


class Opacity_opacity_InterpEnumField(
    EnumField[
        Opacity_opacity_InterpEnumAttrOperator,
        Opacity_opacity_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Opacity_opacity_InterpEnumAttrOperator
    PLUG_CLS = Opacity_opacity_InterpEnumPlugOperator


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


class Environment_environment_InterpEnumPlugOperator(
    EnumPlugOperator["Environment_environment_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Environment_environment_InterpEnumAttrOperator(
    EnumAttrOperator[Environment_environment_InterpEnumPlugOperator]
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


class Environment_environment_InterpEnumField(
    EnumField[
        Environment_environment_InterpEnumAttrOperator,
        Environment_environment_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Environment_environment_InterpEnumAttrOperator
    PLUG_CLS = Environment_environment_InterpEnumPlugOperator


class FieldList_fieldFunction_fieldFunction_InmapPlugOperator(
    CompoundPlugOperator[
        "FieldList_fieldFunction_fieldFunction_InmapAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fieldFunction_InmapTo", "frfit"),
        ("fieldFunction_InmapFrom", "frfif"),
    )

    fieldFunction_InmapTo = ShortField(default_value=0)
    frfit = fieldFunction_InmapTo

    fieldFunction_InmapFrom = ShortField(default_value=0)
    frfif = fieldFunction_InmapFrom


class FieldList_fieldFunction_fieldFunction_InmapAttrOperator(
    CompoundAttrOperator[
        FieldList_fieldFunction_fieldFunction_InmapPlugOperator
    ]
):
    __slots__ = ()

    fieldFunction_InmapTo = ShortField(default_value=0)
    frfit = fieldFunction_InmapTo

    fieldFunction_InmapFrom = ShortField(default_value=0)
    frfif = fieldFunction_InmapFrom


class FieldList_fieldFunction_fieldFunction_InmapField(
    CompoundField[
        FieldList_fieldFunction_fieldFunction_InmapAttrOperator,
        FieldList_fieldFunction_fieldFunction_InmapPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = FieldList_fieldFunction_fieldFunction_InmapAttrOperator
    PLUG_CLS = FieldList_fieldFunction_fieldFunction_InmapPlugOperator


class FieldList_fieldFunction_fieldFunction_OutmapPlugOperator(
    CompoundPlugOperator[
        "FieldList_fieldFunction_fieldFunction_OutmapAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fieldFunction_OutmapTo", "frfot"),
        ("fieldFunction_OutmapFrom", "frfof"),
    )

    fieldFunction_OutmapTo = ShortField(default_value=0)
    frfot = fieldFunction_OutmapTo

    fieldFunction_OutmapFrom = ShortField(default_value=0)
    frfof = fieldFunction_OutmapFrom


class FieldList_fieldFunction_fieldFunction_OutmapAttrOperator(
    CompoundAttrOperator[
        FieldList_fieldFunction_fieldFunction_OutmapPlugOperator
    ]
):
    __slots__ = ()

    fieldFunction_OutmapTo = ShortField(default_value=0)
    frfot = fieldFunction_OutmapTo

    fieldFunction_OutmapFrom = ShortField(default_value=0)
    frfof = fieldFunction_OutmapFrom


class FieldList_fieldFunction_fieldFunction_OutmapField(
    CompoundField[
        FieldList_fieldFunction_fieldFunction_OutmapAttrOperator,
        FieldList_fieldFunction_fieldFunction_OutmapPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = FieldList_fieldFunction_fieldFunction_OutmapAttrOperator
    PLUG_CLS = FieldList_fieldFunction_fieldFunction_OutmapPlugOperator


class EmissionList_emissionFunction_emissionFunction_InmapPlugOperator(
    CompoundPlugOperator[
        "EmissionList_emissionFunction_emissionFunction_InmapAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("emissionFunction_InmapTo", "emfit"),
        ("emissionFunction_InmapFrom", "emfif"),
    )

    emissionFunction_InmapTo = ShortField(default_value=0)
    emfit = emissionFunction_InmapTo

    emissionFunction_InmapFrom = ShortField(default_value=0)
    emfif = emissionFunction_InmapFrom


class EmissionList_emissionFunction_emissionFunction_InmapAttrOperator(
    CompoundAttrOperator[
        EmissionList_emissionFunction_emissionFunction_InmapPlugOperator
    ]
):
    __slots__ = ()

    emissionFunction_InmapTo = ShortField(default_value=0)
    emfit = emissionFunction_InmapTo

    emissionFunction_InmapFrom = ShortField(default_value=0)
    emfif = emissionFunction_InmapFrom


class EmissionList_emissionFunction_emissionFunction_InmapField(
    CompoundField[
        EmissionList_emissionFunction_emissionFunction_InmapAttrOperator,
        EmissionList_emissionFunction_emissionFunction_InmapPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = EmissionList_emissionFunction_emissionFunction_InmapAttrOperator
    PLUG_CLS = EmissionList_emissionFunction_emissionFunction_InmapPlugOperator


class EmissionList_emissionFunction_emissionFunction_OutmapPlugOperator(
    CompoundPlugOperator[
        "EmissionList_emissionFunction_emissionFunction_OutmapAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("emissionFunction_OutmapTo", "emfot"),
        ("emissionFunction_OutmapFrom", "emfof"),
    )

    emissionFunction_OutmapTo = ShortField(default_value=0)
    emfot = emissionFunction_OutmapTo

    emissionFunction_OutmapFrom = ShortField(default_value=0)
    emfof = emissionFunction_OutmapFrom


class EmissionList_emissionFunction_emissionFunction_OutmapAttrOperator(
    CompoundAttrOperator[
        EmissionList_emissionFunction_emissionFunction_OutmapPlugOperator
    ]
):
    __slots__ = ()

    emissionFunction_OutmapTo = ShortField(default_value=0)
    emfot = emissionFunction_OutmapTo

    emissionFunction_OutmapFrom = ShortField(default_value=0)
    emfof = emissionFunction_OutmapFrom


class EmissionList_emissionFunction_emissionFunction_OutmapField(
    CompoundField[
        EmissionList_emissionFunction_emissionFunction_OutmapAttrOperator,
        EmissionList_emissionFunction_emissionFunction_OutmapPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = (
        EmissionList_emissionFunction_emissionFunction_OutmapAttrOperator
    )
    PLUG_CLS = (
        EmissionList_emissionFunction_emissionFunction_OutmapPlugOperator
    )


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


class UvSet_uvSetPointsPlugOperator(
    Float2CompoundBasePlugOperator["UvSet_uvSetPointsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvSetPointsU", "uvpu"),
        ("uvSetPointsV", "uvpv"),
    )

    uvSetPointsU = FloatField(default_value=0.0)
    uvpu = uvSetPointsU

    uvSetPointsV = FloatField(default_value=0.0)
    uvpv = uvSetPointsV


class UvSet_uvSetPointsAttrOperator(
    Float2CompoundBaseAttrOperator[UvSet_uvSetPointsPlugOperator]
):
    __slots__ = ()

    uvSetPointsU = FloatField(default_value=0.0)
    uvpu = uvSetPointsU

    uvSetPointsV = FloatField(default_value=0.0)
    uvpv = uvSetPointsV


class UvSet_uvSetPointsField(
    Float2CompoundBaseField[
        UvSet_uvSetPointsAttrOperator, UvSet_uvSetPointsPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = UvSet_uvSetPointsAttrOperator
    PLUG_CLS = UvSet_uvSetPointsPlugOperator


class ColorSet_colorSetPointsPlugOperator(
    CompoundPlugOperator["ColorSet_colorSetPointsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorSetPointsR", "clpr"),
        ("colorSetPointsG", "clpg"),
        ("colorSetPointsB", "clpb"),
        ("colorSetPointsA", "clpa"),
    )

    colorSetPointsR = FloatField(default_value=0.0)
    clpr = colorSetPointsR

    colorSetPointsG = FloatField(default_value=0.0)
    clpg = colorSetPointsG

    colorSetPointsB = FloatField(default_value=0.0)
    clpb = colorSetPointsB

    colorSetPointsA = FloatField(default_value=0.0)
    clpa = colorSetPointsA


class ColorSet_colorSetPointsAttrOperator(
    CompoundAttrOperator[ColorSet_colorSetPointsPlugOperator]
):
    __slots__ = ()

    colorSetPointsR = FloatField(default_value=0.0)
    clpr = colorSetPointsR

    colorSetPointsG = FloatField(default_value=0.0)
    clpg = colorSetPointsG

    colorSetPointsB = FloatField(default_value=0.0)
    clpb = colorSetPointsB

    colorSetPointsA = FloatField(default_value=0.0)
    clpa = colorSetPointsA


class ColorSet_colorSetPointsField(
    CompoundField[
        ColorSet_colorSetPointsAttrOperator,
        ColorSet_colorSetPointsPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ColorSet_colorSetPointsAttrOperator
    PLUG_CLS = ColorSet_colorSetPointsPlugOperator


class FieldList_fieldFunctionPlugOperator(
    CompoundPlugOperator["FieldList_fieldFunctionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fieldFunction_Hidden", "frfh"),
        ("fieldFunction_Raw", "frfr"),
        ("fieldFunction_Inmap", "frfi"),
        ("fieldFunction_Outmap", "frfo"),
    )

    fieldFunction_Hidden = TypedField()
    frfh = fieldFunction_Hidden

    fieldFunction_Raw = TypedField()
    frfr = fieldFunction_Raw

    fieldFunction_Inmap = FieldList_fieldFunction_fieldFunction_InmapField(
        multi=True, default_value=(0.0, 0.0)
    )
    frfi = fieldFunction_Inmap

    fieldFunction_Outmap = FieldList_fieldFunction_fieldFunction_OutmapField(
        multi=True, default_value=(0.0, 0.0)
    )
    frfo = fieldFunction_Outmap


class FieldList_fieldFunctionAttrOperator(
    CompoundAttrOperator[FieldList_fieldFunctionPlugOperator]
):
    __slots__ = ()

    fieldFunction_Hidden = TypedField()
    frfh = fieldFunction_Hidden

    fieldFunction_Raw = TypedField()
    frfr = fieldFunction_Raw

    fieldFunction_Inmap = FieldList_fieldFunction_fieldFunction_InmapField(
        multi=True, default_value=(0.0, 0.0)
    )
    frfi = fieldFunction_Inmap

    fieldFunction_Outmap = FieldList_fieldFunction_fieldFunction_OutmapField(
        multi=True, default_value=(0.0, 0.0)
    )
    frfo = fieldFunction_Outmap


class FieldList_fieldFunctionField(
    CompoundField[
        FieldList_fieldFunctionAttrOperator,
        FieldList_fieldFunctionPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = FieldList_fieldFunctionAttrOperator
    PLUG_CLS = FieldList_fieldFunctionPlugOperator

    fieldFunction_Hidden = TypedField()
    frfh = fieldFunction_Hidden

    fieldFunction_Raw = TypedField()
    frfr = fieldFunction_Raw

    fieldFunction_Inmap = FieldList_fieldFunction_fieldFunction_InmapField(
        multi=True, default_value=(0.0, 0.0)
    )
    frfi = fieldFunction_Inmap

    fieldFunction_Outmap = FieldList_fieldFunction_fieldFunction_OutmapField(
        multi=True, default_value=(0.0, 0.0)
    )
    frfo = fieldFunction_Outmap


class EmissionList_emissionFunctionPlugOperator(
    CompoundPlugOperator["EmissionList_emissionFunctionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("emissionFunction_Hidden", "emfh"),
        ("emissionFunction_Raw", "emfr"),
        ("emissionFunction_Inmap", "emfi"),
        ("emissionFunction_Outmap", "emfo"),
    )

    emissionFunction_Hidden = TypedField()
    emfh = emissionFunction_Hidden

    emissionFunction_Raw = TypedField()
    emfr = emissionFunction_Raw

    emissionFunction_Inmap = (
        EmissionList_emissionFunction_emissionFunction_InmapField(
            multi=True, default_value=(0.0, 0.0)
        )
    )
    emfi = emissionFunction_Inmap

    emissionFunction_Outmap = (
        EmissionList_emissionFunction_emissionFunction_OutmapField(
            multi=True, default_value=(0.0, 0.0)
        )
    )
    emfo = emissionFunction_Outmap


class EmissionList_emissionFunctionAttrOperator(
    CompoundAttrOperator[EmissionList_emissionFunctionPlugOperator]
):
    __slots__ = ()

    emissionFunction_Hidden = TypedField()
    emfh = emissionFunction_Hidden

    emissionFunction_Raw = TypedField()
    emfr = emissionFunction_Raw

    emissionFunction_Inmap = (
        EmissionList_emissionFunction_emissionFunction_InmapField(
            multi=True, default_value=(0.0, 0.0)
        )
    )
    emfi = emissionFunction_Inmap

    emissionFunction_Outmap = (
        EmissionList_emissionFunction_emissionFunction_OutmapField(
            multi=True, default_value=(0.0, 0.0)
        )
    )
    emfo = emissionFunction_Outmap


class EmissionList_emissionFunctionField(
    CompoundField[
        EmissionList_emissionFunctionAttrOperator,
        EmissionList_emissionFunctionPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = EmissionList_emissionFunctionAttrOperator
    PLUG_CLS = EmissionList_emissionFunctionPlugOperator

    emissionFunction_Hidden = TypedField()
    emfh = emissionFunction_Hidden

    emissionFunction_Raw = TypedField()
    emfr = emissionFunction_Raw

    emissionFunction_Inmap = (
        EmissionList_emissionFunction_emissionFunction_InmapField(
            multi=True, default_value=(0.0, 0.0)
        )
    )
    emfi = emissionFunction_Inmap

    emissionFunction_Outmap = (
        EmissionList_emissionFunction_emissionFunction_OutmapField(
            multi=True, default_value=(0.0, 0.0)
        )
    )
    emfo = emissionFunction_Outmap


class LightDataArray_lightDirectionPlugOperator(
    Float3CompoundBasePlugOperator["LightDataArray_lightDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightDirectionX", "ldx"),
        ("lightDirectionY", "ldy"),
        ("lightDirectionZ", "ldz"),
    )

    lightDirectionX = FloatField(default_value=1.0, readable=False)
    ldx = lightDirectionX

    lightDirectionY = FloatField(default_value=1.0, readable=False)
    ldy = lightDirectionY

    lightDirectionZ = FloatField(default_value=1.0, readable=False)
    ldz = lightDirectionZ


class LightDataArray_lightDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[LightDataArray_lightDirectionPlugOperator]
):
    __slots__ = ()

    lightDirectionX = FloatField(default_value=1.0, readable=False)
    ldx = lightDirectionX

    lightDirectionY = FloatField(default_value=1.0, readable=False)
    ldy = lightDirectionY

    lightDirectionZ = FloatField(default_value=1.0, readable=False)
    ldz = lightDirectionZ


class LightDataArray_lightDirectionField(
    Float3CompoundBaseField[
        LightDataArray_lightDirectionAttrOperator,
        LightDataArray_lightDirectionPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = LightDataArray_lightDirectionAttrOperator
    PLUG_CLS = LightDataArray_lightDirectionPlugOperator

    lightDirectionX = FloatField(default_value=1.0, readable=False)
    ldx = lightDirectionX

    lightDirectionY = FloatField(default_value=1.0, readable=False)
    ldy = lightDirectionY

    lightDirectionZ = FloatField(default_value=1.0, readable=False)
    ldz = lightDirectionZ


class LightDataArray_lightIntensityPlugOperator(
    Float3CompoundBasePlugOperator["LightDataArray_lightIntensityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightIntensityR", "lir"),
        ("lightIntensityG", "lig"),
        ("lightIntensityB", "lib"),
    )

    lightIntensityR = FloatField(default_value=1.0, readable=False)
    lir = lightIntensityR

    lightIntensityG = FloatField(default_value=1.0, readable=False)
    lig = lightIntensityG

    lightIntensityB = FloatField(default_value=1.0, readable=False)
    lib = lightIntensityB


class LightDataArray_lightIntensityAttrOperator(
    Float3CompoundBaseAttrOperator[LightDataArray_lightIntensityPlugOperator]
):
    __slots__ = ()

    lightIntensityR = FloatField(default_value=1.0, readable=False)
    lir = lightIntensityR

    lightIntensityG = FloatField(default_value=1.0, readable=False)
    lig = lightIntensityG

    lightIntensityB = FloatField(default_value=1.0, readable=False)
    lib = lightIntensityB


class LightDataArray_lightIntensityField(
    Float3CompoundBaseField[
        LightDataArray_lightIntensityAttrOperator,
        LightDataArray_lightIntensityPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = LightDataArray_lightIntensityAttrOperator
    PLUG_CLS = LightDataArray_lightIntensityPlugOperator

    lightIntensityR = FloatField(default_value=1.0, readable=False)
    lir = lightIntensityR

    lightIntensityG = FloatField(default_value=1.0, readable=False)
    lig = lightIntensityG

    lightIntensityB = FloatField(default_value=1.0, readable=False)
    lib = lightIntensityB


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
        ("incandescence_ColorR", "icr"),
        ("incandescence_ColorG", "icg"),
        ("incandescence_ColorB", "icb"),
    )

    incandescence_ColorR = FloatField(default_value=0.0)
    icr = incandescence_ColorR

    incandescence_ColorG = FloatField(default_value=0.0)
    icg = incandescence_ColorG

    incandescence_ColorB = FloatField(default_value=0.0)
    icb = incandescence_ColorB


class Incandescence_incandescence_ColorAttrOperator(
    Float3CompoundBaseAttrOperator[
        Incandescence_incandescence_ColorPlugOperator
    ]
):
    __slots__ = ()

    incandescence_ColorR = FloatField(default_value=0.0)
    icr = incandescence_ColorR

    incandescence_ColorG = FloatField(default_value=0.0)
    icg = incandescence_ColorG

    incandescence_ColorB = FloatField(default_value=0.0)
    icb = incandescence_ColorB


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
    icr = incandescence_ColorR

    incandescence_ColorG = FloatField(default_value=0.0)
    icg = incandescence_ColorG

    incandescence_ColorB = FloatField(default_value=0.0)
    icb = incandescence_ColorB


class Environment_environment_ColorPlugOperator(
    Float3CompoundBasePlugOperator["Environment_environment_ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("environment_ColorR", "envcr"),
        ("environment_ColorG", "envcg"),
        ("environment_ColorB", "envcb"),
    )

    environment_ColorR = FloatField(default_value=0.0)
    envcr = environment_ColorR

    environment_ColorG = FloatField(default_value=0.0)
    envcg = environment_ColorG

    environment_ColorB = FloatField(default_value=0.0)
    envcb = environment_ColorB


class Environment_environment_ColorAttrOperator(
    Float3CompoundBaseAttrOperator[Environment_environment_ColorPlugOperator]
):
    __slots__ = ()

    environment_ColorR = FloatField(default_value=0.0)
    envcr = environment_ColorR

    environment_ColorG = FloatField(default_value=0.0)
    envcg = environment_ColorG

    environment_ColorB = FloatField(default_value=0.0)
    envcb = environment_ColorB


class Environment_environment_ColorField(
    Float3CompoundBaseField[
        Environment_environment_ColorAttrOperator,
        Environment_environment_ColorPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Environment_environment_ColorAttrOperator
    PLUG_CLS = Environment_environment_ColorPlugOperator

    environment_ColorR = FloatField(default_value=0.0)
    envcr = environment_ColorR

    environment_ColorG = FloatField(default_value=0.0)
    envcg = environment_ColorG

    environment_ColorB = FloatField(default_value=0.0)
    envcb = environment_ColorB


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


class ControlPointsPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ControlPointsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("xValue", "xv"),
        ("yValue", "yv"),
        ("zValue", "zv"),
    )

    xValue = DoubleLinearField(default_value=0.0)
    xv = xValue

    yValue = DoubleLinearField(default_value=0.0)
    yv = yValue

    zValue = DoubleLinearField(default_value=0.0)
    zv = zValue


class ControlPointsAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ControlPointsPlugOperator]
):
    __slots__ = ()

    xValue = DoubleLinearField(default_value=0.0)
    xv = xValue

    yValue = DoubleLinearField(default_value=0.0)
    yv = yValue

    zValue = DoubleLinearField(default_value=0.0)
    zv = zValue


class ControlPointsField(
    DoubleLinear3CompoundBaseField[
        ControlPointsAttrOperator, ControlPointsPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ControlPointsAttrOperator
    PLUG_CLS = ControlPointsPlugOperator


class UvPivotPlugOperator(
    Double2CompoundBasePlugOperator["UvPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvPivotX", "pvx"),
        ("uvPivotY", "pvy"),
    )

    uvPivotX = DoubleField(default_value=0.0)
    pvx = uvPivotX

    uvPivotY = DoubleField(default_value=0.0)
    pvy = uvPivotY


class UvPivotAttrOperator(
    Double2CompoundBaseAttrOperator[UvPivotPlugOperator]
):
    __slots__ = ()

    uvPivotX = DoubleField(default_value=0.0)
    pvx = uvPivotX

    uvPivotY = DoubleField(default_value=0.0)
    pvy = uvPivotY


class UvPivotField(
    Double2CompoundBaseField[UvPivotAttrOperator, UvPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvPivotAttrOperator
    PLUG_CLS = UvPivotPlugOperator

    uvPivotX = DoubleField(default_value=0.0)
    pvx = uvPivotX

    uvPivotY = DoubleField(default_value=0.0)
    pvy = uvPivotY


class UvSetPlugOperator(CompoundPlugOperator["UvSetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvSetName", "uvsn"),
        ("uvSetPoints", "uvsp"),
        ("uvSetTweakLocation", "uvtw"),
    )

    uvSetName = DataStringField()
    uvsn = uvSetName

    uvSetPoints = UvSet_uvSetPointsField(multi=True, default_value=(0.0, 0.0))
    uvsp = uvSetPoints

    uvSetTweakLocation = TypedField(readable=False)
    uvtw = uvSetTweakLocation


class UvSetAttrOperator(CompoundAttrOperator[UvSetPlugOperator]):
    __slots__ = ()

    uvSetName = DataStringField()
    uvsn = uvSetName

    uvSetPoints = UvSet_uvSetPointsField(multi=True, default_value=(0.0, 0.0))
    uvsp = uvSetPoints

    uvSetTweakLocation = TypedField(readable=False)
    uvtw = uvSetTweakLocation


class UvSetField(CompoundField[UvSetAttrOperator, UvSetPlugOperator]):
    __slots__ = ()

    ATTR_CLS = UvSetAttrOperator
    PLUG_CLS = UvSetPlugOperator


class ColorSetPlugOperator(CompoundPlugOperator["ColorSetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorName", "clsn"),
        ("clamped", "clam"),
        ("representation", "rprt"),
        ("colorSetPoints", "clsp"),
    )

    colorName = DataStringField()
    clsn = colorName

    clamped = BoolField(default_value=False)
    clam = clamped

    representation = ColorSet_representationEnumField(default_value=4)
    rprt = representation

    colorSetPoints = ColorSet_colorSetPointsField(
        multi=True, default_value=(0.0, 0.0, 0.0, 0.0)
    )
    clsp = colorSetPoints


class ColorSetAttrOperator(CompoundAttrOperator[ColorSetPlugOperator]):
    __slots__ = ()

    colorName = DataStringField()
    clsn = colorName

    clamped = BoolField(default_value=False)
    clam = clamped

    representation = ColorSet_representationEnumField(default_value=4)
    rprt = representation

    colorSetPoints = ColorSet_colorSetPointsField(
        multi=True, default_value=(0.0, 0.0, 0.0, 0.0)
    )
    clsp = colorSetPoints


class ColorSetField(CompoundField[ColorSetAttrOperator, ColorSetPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ColorSetAttrOperator
    PLUG_CLS = ColorSetPlugOperator


class BoundingBoxScalePlugOperator(
    Float3CompoundBasePlugOperator["BoundingBoxScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("boundingBoxScaleX", "bscx"),
        ("boundingBoxScaleY", "bscy"),
        ("boundingBoxScaleZ", "bscz"),
    )

    boundingBoxScaleX = FloatField(default_value=1.5, min_value=1.0)
    bscx = boundingBoxScaleX

    boundingBoxScaleY = FloatField(default_value=1.5, min_value=1.0)
    bscy = boundingBoxScaleY

    boundingBoxScaleZ = FloatField(default_value=1.5, min_value=1.0)
    bscz = boundingBoxScaleZ


class BoundingBoxScaleAttrOperator(
    Float3CompoundBaseAttrOperator[BoundingBoxScalePlugOperator]
):
    __slots__ = ()

    boundingBoxScaleX = FloatField(default_value=1.5, min_value=1.0)
    bscx = boundingBoxScaleX

    boundingBoxScaleY = FloatField(default_value=1.5, min_value=1.0)
    bscy = boundingBoxScaleY

    boundingBoxScaleZ = FloatField(default_value=1.5, min_value=1.0)
    bscz = boundingBoxScaleZ


class BoundingBoxScaleField(
    Float3CompoundBaseField[
        BoundingBoxScaleAttrOperator, BoundingBoxScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = BoundingBoxScaleAttrOperator
    PLUG_CLS = BoundingBoxScalePlugOperator

    boundingBoxScaleX = FloatField(default_value=1.5, min_value=1.0)
    bscx = boundingBoxScaleX

    boundingBoxScaleY = FloatField(default_value=1.5, min_value=1.0)
    bscy = boundingBoxScaleY

    boundingBoxScaleZ = FloatField(default_value=1.5, min_value=1.0)
    bscz = boundingBoxScaleZ


class CollisionOffsetVelocityIncrementPlugOperator(
    CompoundPlugOperator["CollisionOffsetVelocityIncrementAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionOffsetVelocityIncrement_Position", "covip"),
        ("collisionOffsetVelocityIncrement_FloatValue", "covifv"),
        ("collisionOffsetVelocityIncrement_Interp", "covii"),
    )

    collisionOffsetVelocityIncrement_Position = FloatField(default_value=0.0)
    covip = collisionOffsetVelocityIncrement_Position

    collisionOffsetVelocityIncrement_FloatValue = FloatField(default_value=0.0)
    covifv = collisionOffsetVelocityIncrement_FloatValue

    collisionOffsetVelocityIncrement_Interp = CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumField(
        default_value=0
    )
    covii = collisionOffsetVelocityIncrement_Interp


class CollisionOffsetVelocityIncrementAttrOperator(
    CompoundAttrOperator[CollisionOffsetVelocityIncrementPlugOperator]
):
    __slots__ = ()

    collisionOffsetVelocityIncrement_Position = FloatField(default_value=0.0)
    covip = collisionOffsetVelocityIncrement_Position

    collisionOffsetVelocityIncrement_FloatValue = FloatField(default_value=0.0)
    covifv = collisionOffsetVelocityIncrement_FloatValue

    collisionOffsetVelocityIncrement_Interp = CollisionOffsetVelocityIncrement_collisionOffsetVelocityIncrement_InterpEnumField(
        default_value=0
    )
    covii = collisionOffsetVelocityIncrement_Interp


class CollisionOffsetVelocityIncrementField(
    CompoundField[
        CollisionOffsetVelocityIncrementAttrOperator,
        CollisionOffsetVelocityIncrementPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionOffsetVelocityIncrementAttrOperator
    PLUG_CLS = CollisionOffsetVelocityIncrementPlugOperator


class CollisionDepthVelocityIncrementPlugOperator(
    CompoundPlugOperator["CollisionDepthVelocityIncrementAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionDepthVelocityIncrement_Position", "cdvip"),
        ("collisionDepthVelocityIncrement_FloatValue", "cdvifv"),
        ("collisionDepthVelocityIncrement_Interp", "cdvii"),
    )

    collisionDepthVelocityIncrement_Position = FloatField(default_value=0.0)
    cdvip = collisionDepthVelocityIncrement_Position

    collisionDepthVelocityIncrement_FloatValue = FloatField(default_value=0.0)
    cdvifv = collisionDepthVelocityIncrement_FloatValue

    collisionDepthVelocityIncrement_Interp = CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumField(
        default_value=0
    )
    cdvii = collisionDepthVelocityIncrement_Interp


class CollisionDepthVelocityIncrementAttrOperator(
    CompoundAttrOperator[CollisionDepthVelocityIncrementPlugOperator]
):
    __slots__ = ()

    collisionDepthVelocityIncrement_Position = FloatField(default_value=0.0)
    cdvip = collisionDepthVelocityIncrement_Position

    collisionDepthVelocityIncrement_FloatValue = FloatField(default_value=0.0)
    cdvifv = collisionDepthVelocityIncrement_FloatValue

    collisionDepthVelocityIncrement_Interp = CollisionDepthVelocityIncrement_collisionDepthVelocityIncrement_InterpEnumField(
        default_value=0
    )
    cdvii = collisionDepthVelocityIncrement_Interp


class CollisionDepthVelocityIncrementField(
    CompoundField[
        CollisionDepthVelocityIncrementAttrOperator,
        CollisionDepthVelocityIncrementPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionDepthVelocityIncrementAttrOperator
    PLUG_CLS = CollisionDepthVelocityIncrementPlugOperator


class CollisionOffsetVelocityMultiplierPlugOperator(
    CompoundPlugOperator["CollisionOffsetVelocityMultiplierAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionOffsetVelocityMultiplier_Position", "covmp"),
        ("collisionOffsetVelocityMultiplier_FloatValue", "covmfv"),
        ("collisionOffsetVelocityMultiplier_Interp", "covmi"),
    )

    collisionOffsetVelocityMultiplier_Position = FloatField(default_value=0.0)
    covmp = collisionOffsetVelocityMultiplier_Position

    collisionOffsetVelocityMultiplier_FloatValue = FloatField(
        default_value=0.0
    )
    covmfv = collisionOffsetVelocityMultiplier_FloatValue

    collisionOffsetVelocityMultiplier_Interp = CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumField(
        default_value=0
    )
    covmi = collisionOffsetVelocityMultiplier_Interp


class CollisionOffsetVelocityMultiplierAttrOperator(
    CompoundAttrOperator[CollisionOffsetVelocityMultiplierPlugOperator]
):
    __slots__ = ()

    collisionOffsetVelocityMultiplier_Position = FloatField(default_value=0.0)
    covmp = collisionOffsetVelocityMultiplier_Position

    collisionOffsetVelocityMultiplier_FloatValue = FloatField(
        default_value=0.0
    )
    covmfv = collisionOffsetVelocityMultiplier_FloatValue

    collisionOffsetVelocityMultiplier_Interp = CollisionOffsetVelocityMultiplier_collisionOffsetVelocityMultiplier_InterpEnumField(
        default_value=0
    )
    covmi = collisionOffsetVelocityMultiplier_Interp


class CollisionOffsetVelocityMultiplierField(
    CompoundField[
        CollisionOffsetVelocityMultiplierAttrOperator,
        CollisionOffsetVelocityMultiplierPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionOffsetVelocityMultiplierAttrOperator
    PLUG_CLS = CollisionOffsetVelocityMultiplierPlugOperator


class CollisionDepthVelocityMultiplierPlugOperator(
    CompoundPlugOperator["CollisionDepthVelocityMultiplierAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionDepthVelocityMultiplier_Position", "cdvmp"),
        ("collisionDepthVelocityMultiplier_FloatValue", "cdvmfv"),
        ("collisionDepthVelocityMultiplier_Interp", "cdvmi"),
    )

    collisionDepthVelocityMultiplier_Position = FloatField(default_value=0.0)
    cdvmp = collisionDepthVelocityMultiplier_Position

    collisionDepthVelocityMultiplier_FloatValue = FloatField(default_value=0.0)
    cdvmfv = collisionDepthVelocityMultiplier_FloatValue

    collisionDepthVelocityMultiplier_Interp = CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumField(
        default_value=0
    )
    cdvmi = collisionDepthVelocityMultiplier_Interp


class CollisionDepthVelocityMultiplierAttrOperator(
    CompoundAttrOperator[CollisionDepthVelocityMultiplierPlugOperator]
):
    __slots__ = ()

    collisionDepthVelocityMultiplier_Position = FloatField(default_value=0.0)
    cdvmp = collisionDepthVelocityMultiplier_Position

    collisionDepthVelocityMultiplier_FloatValue = FloatField(default_value=0.0)
    cdvmfv = collisionDepthVelocityMultiplier_FloatValue

    collisionDepthVelocityMultiplier_Interp = CollisionDepthVelocityMultiplier_collisionDepthVelocityMultiplier_InterpEnumField(
        default_value=0
    )
    cdvmi = collisionDepthVelocityMultiplier_Interp


class CollisionDepthVelocityMultiplierField(
    CompoundField[
        CollisionDepthVelocityMultiplierAttrOperator,
        CollisionDepthVelocityMultiplierPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionDepthVelocityMultiplierAttrOperator
    PLUG_CLS = CollisionDepthVelocityMultiplierPlugOperator


class ResolutionPlugOperator(CompoundPlugOperator["ResolutionAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("resolutionW", "rw"),
        ("resolutionH", "rh"),
        ("resolutionD", "rd"),
    )

    resolutionW = LongField(default_value=10, min_value=3)
    rw = resolutionW

    resolutionH = LongField(default_value=10, min_value=3)
    rh = resolutionH

    resolutionD = LongField(default_value=10, min_value=1)
    rd = resolutionD


class ResolutionAttrOperator(CompoundAttrOperator[ResolutionPlugOperator]):
    __slots__ = ()

    resolutionW = LongField(default_value=10, min_value=3)
    rw = resolutionW

    resolutionH = LongField(default_value=10, min_value=3)
    rh = resolutionH

    resolutionD = LongField(default_value=10, min_value=1)
    rd = resolutionD


class ResolutionField(
    CompoundField[ResolutionAttrOperator, ResolutionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ResolutionAttrOperator
    PLUG_CLS = ResolutionPlugOperator

    resolutionW = LongField(default_value=10, min_value=3)
    rw = resolutionW

    resolutionH = LongField(default_value=10, min_value=3)
    rh = resolutionH

    resolutionD = LongField(default_value=10, min_value=1)
    rd = resolutionD


class DimensionsPlugOperator(CompoundPlugOperator["DimensionsAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dimensionsW", "dw"),
        ("dimensionsH", "dh"),
        ("dimensionsD", "dd"),
    )

    dimensionsW = DoubleField(default_value=3.0, min_value=1e-05)
    dw = dimensionsW

    dimensionsH = DoubleField(default_value=3.0, min_value=1e-05)
    dh = dimensionsH

    dimensionsD = DoubleField(default_value=3.0, min_value=1e-05)
    dd = dimensionsD


class DimensionsAttrOperator(CompoundAttrOperator[DimensionsPlugOperator]):
    __slots__ = ()

    dimensionsW = DoubleField(default_value=3.0, min_value=1e-05)
    dw = dimensionsW

    dimensionsH = DoubleField(default_value=3.0, min_value=1e-05)
    dh = dimensionsH

    dimensionsD = DoubleField(default_value=3.0, min_value=1e-05)
    dd = dimensionsD


class DimensionsField(
    CompoundField[DimensionsAttrOperator, DimensionsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DimensionsAttrOperator
    PLUG_CLS = DimensionsPlugOperator

    dimensionsW = DoubleField(default_value=3.0, min_value=1e-05)
    dw = dimensionsW

    dimensionsH = DoubleField(default_value=3.0, min_value=1e-05)
    dh = dimensionsH

    dimensionsD = DoubleField(default_value=3.0, min_value=1e-05)
    dd = dimensionsD


class DynamicOffsetPlugOperator(
    CompoundPlugOperator["DynamicOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dynamicOffsetX", "dofx"),
        ("dynamicOffsetY", "dofy"),
        ("dynamicOffsetZ", "dofz"),
    )

    dynamicOffsetX = DoubleField(default_value=0.0)
    dofx = dynamicOffsetX

    dynamicOffsetY = DoubleField(default_value=0.0)
    dofy = dynamicOffsetY

    dynamicOffsetZ = DoubleField(default_value=0.0)
    dofz = dynamicOffsetZ


class DynamicOffsetAttrOperator(
    CompoundAttrOperator[DynamicOffsetPlugOperator]
):
    __slots__ = ()

    dynamicOffsetX = DoubleField(default_value=0.0)
    dofx = dynamicOffsetX

    dynamicOffsetY = DoubleField(default_value=0.0)
    dofy = dynamicOffsetY

    dynamicOffsetZ = DoubleField(default_value=0.0)
    dofz = dynamicOffsetZ


class DynamicOffsetField(
    CompoundField[DynamicOffsetAttrOperator, DynamicOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DynamicOffsetAttrOperator
    PLUG_CLS = DynamicOffsetPlugOperator

    dynamicOffsetX = DoubleField(default_value=0.0)
    dofx = dynamicOffsetX

    dynamicOffsetY = DoubleField(default_value=0.0)
    dofy = dynamicOffsetY

    dynamicOffsetZ = DoubleField(default_value=0.0)
    dofz = dynamicOffsetZ


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


class FieldListPlugOperator(CompoundPlugOperator["FieldListAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("fieldFunction", "frf"),)

    fieldFunction = FieldList_fieldFunctionField()
    frf = fieldFunction


class FieldListAttrOperator(CompoundAttrOperator[FieldListPlugOperator]):
    __slots__ = ()

    fieldFunction = FieldList_fieldFunctionField()
    frf = fieldFunction


class FieldListField(
    CompoundField[FieldListAttrOperator, FieldListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FieldListAttrOperator
    PLUG_CLS = FieldListPlugOperator


class EmissionListPlugOperator(
    CompoundPlugOperator["EmissionListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("emissionFunction", "emf"),)

    emissionFunction = EmissionList_emissionFunctionField()
    emf = emissionFunction


class EmissionListAttrOperator(CompoundAttrOperator[EmissionListPlugOperator]):
    __slots__ = ()

    emissionFunction = EmissionList_emissionFunctionField()
    emf = emissionFunction


class EmissionListField(
    CompoundField[EmissionListAttrOperator, EmissionListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmissionListAttrOperator
    PLUG_CLS = EmissionListPlugOperator


class SubVolumeCenterPlugOperator(
    CompoundPlugOperator["SubVolumeCenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("subVolumeCenterW", "scw"),
        ("subVolumeCenterH", "sch"),
        ("subVolumeCenterD", "scd"),
    )

    subVolumeCenterW = LongField(default_value=-1, min_value=-1)
    scw = subVolumeCenterW

    subVolumeCenterH = LongField(default_value=-1, min_value=-1)
    sch = subVolumeCenterH

    subVolumeCenterD = LongField(default_value=-1, min_value=-1)
    scd = subVolumeCenterD


class SubVolumeCenterAttrOperator(
    CompoundAttrOperator[SubVolumeCenterPlugOperator]
):
    __slots__ = ()

    subVolumeCenterW = LongField(default_value=-1, min_value=-1)
    scw = subVolumeCenterW

    subVolumeCenterH = LongField(default_value=-1, min_value=-1)
    sch = subVolumeCenterH

    subVolumeCenterD = LongField(default_value=-1, min_value=-1)
    scd = subVolumeCenterD


class SubVolumeCenterField(
    CompoundField[SubVolumeCenterAttrOperator, SubVolumeCenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SubVolumeCenterAttrOperator
    PLUG_CLS = SubVolumeCenterPlugOperator

    subVolumeCenterW = LongField(default_value=-1, min_value=-1)
    scw = subVolumeCenterW

    subVolumeCenterH = LongField(default_value=-1, min_value=-1)
    sch = subVolumeCenterH

    subVolumeCenterD = LongField(default_value=-1, min_value=-1)
    scd = subVolumeCenterD


class SubVolumeSizePlugOperator(
    CompoundPlugOperator["SubVolumeSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("subVolumeSizeW", "ssw"),
        ("subVolumeSizeH", "ssh"),
        ("subVolumeSizeD", "ssd"),
    )

    subVolumeSizeW = LongField(default_value=-1, min_value=-1)
    ssw = subVolumeSizeW

    subVolumeSizeH = LongField(default_value=-1, min_value=-1)
    ssh = subVolumeSizeH

    subVolumeSizeD = LongField(default_value=-1, min_value=-1)
    ssd = subVolumeSizeD


class SubVolumeSizeAttrOperator(
    CompoundAttrOperator[SubVolumeSizePlugOperator]
):
    __slots__ = ()

    subVolumeSizeW = LongField(default_value=-1, min_value=-1)
    ssw = subVolumeSizeW

    subVolumeSizeH = LongField(default_value=-1, min_value=-1)
    ssh = subVolumeSizeH

    subVolumeSizeD = LongField(default_value=-1, min_value=-1)
    ssd = subVolumeSizeD


class SubVolumeSizeField(
    CompoundField[SubVolumeSizeAttrOperator, SubVolumeSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SubVolumeSizeAttrOperator
    PLUG_CLS = SubVolumeSizePlugOperator

    subVolumeSizeW = LongField(default_value=-1, min_value=-1)
    ssw = subVolumeSizeW

    subVolumeSizeH = LongField(default_value=-1, min_value=-1)
    ssh = subVolumeSizeH

    subVolumeSizeD = LongField(default_value=-1, min_value=-1)
    ssd = subVolumeSizeD


class VelocityScalePlugOperator(
    Float3CompoundBasePlugOperator["VelocityScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("velocityScaleX", "vsx"),
        ("velocityScaleY", "vsy"),
        ("velocityScaleZ", "vsz"),
    )

    velocityScaleX = FloatField(default_value=1.0)
    vsx = velocityScaleX

    velocityScaleY = FloatField(default_value=1.0)
    vsy = velocityScaleY

    velocityScaleZ = FloatField(default_value=1.0)
    vsz = velocityScaleZ


class VelocityScaleAttrOperator(
    Float3CompoundBaseAttrOperator[VelocityScalePlugOperator]
):
    __slots__ = ()

    velocityScaleX = FloatField(default_value=1.0)
    vsx = velocityScaleX

    velocityScaleY = FloatField(default_value=1.0)
    vsy = velocityScaleY

    velocityScaleZ = FloatField(default_value=1.0)
    vsz = velocityScaleZ


class VelocityScaleField(
    Float3CompoundBaseField[
        VelocityScaleAttrOperator, VelocityScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = VelocityScaleAttrOperator
    PLUG_CLS = VelocityScalePlugOperator

    velocityScaleX = FloatField(default_value=1.0)
    vsx = velocityScaleX

    velocityScaleY = FloatField(default_value=1.0)
    vsy = velocityScaleY

    velocityScaleZ = FloatField(default_value=1.0)
    vsz = velocityScaleZ


class LightColorPlugOperator(
    Float3CompoundBasePlugOperator["LightColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightColorR", "lcor"),
        ("lightColorG", "lcog"),
        ("lightColorB", "lcob"),
    )

    lightColorR = FloatField(default_value=1.0)
    lcor = lightColorR

    lightColorG = FloatField(default_value=1.0)
    lcog = lightColorG

    lightColorB = FloatField(default_value=1.0)
    lcob = lightColorB


class LightColorAttrOperator(
    Float3CompoundBaseAttrOperator[LightColorPlugOperator]
):
    __slots__ = ()

    lightColorR = FloatField(default_value=1.0)
    lcor = lightColorR

    lightColorG = FloatField(default_value=1.0)
    lcog = lightColorG

    lightColorB = FloatField(default_value=1.0)
    lcob = lightColorB


class LightColorField(
    Float3CompoundBaseField[LightColorAttrOperator, LightColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightColorAttrOperator
    PLUG_CLS = LightColorPlugOperator

    lightColorR = FloatField(default_value=1.0)
    lcor = lightColorR

    lightColorG = FloatField(default_value=1.0)
    lcog = lightColorG

    lightColorB = FloatField(default_value=1.0)
    lcob = lightColorB


class InputDataPlugOperator(CompoundPlugOperator["InputDataAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputPositions", "inp"),
        ("inputVelocities", "inv"),
        ("inputMass", "inm"),
        ("deltaTime", "dt"),
    )

    inputPositions = DataVectorArrayField()
    inp = inputPositions

    inputVelocities = DataVectorArrayField()
    inv = inputVelocities

    inputMass = DataDoubleArrayField()
    inm = inputMass

    deltaTime = TimeField(default_value=0.0)
    dt = deltaTime


class InputDataAttrOperator(CompoundAttrOperator[InputDataPlugOperator]):
    __slots__ = ()

    inputPositions = DataVectorArrayField()
    inp = inputPositions

    inputVelocities = DataVectorArrayField()
    inv = inputVelocities

    inputMass = DataDoubleArrayField()
    inm = inputMass

    deltaTime = TimeField(default_value=0.0)
    dt = deltaTime


class InputDataField(
    CompoundField[InputDataAttrOperator, InputDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputDataAttrOperator
    PLUG_CLS = InputDataPlugOperator


class FilterSizePlugOperator(
    Float3CompoundBasePlugOperator["FilterSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("filterSizeX", "fsx"),
        ("filterSizeY", "fsy"),
        ("filterSizeZ", "fsz"),
    )

    filterSizeX = FloatField(default_value=0.0, readable=False)
    fsx = filterSizeX

    filterSizeY = FloatField(default_value=0.0, readable=False)
    fsy = filterSizeY

    filterSizeZ = FloatField(default_value=0.0, readable=False)
    fsz = filterSizeZ


class FilterSizeAttrOperator(
    Float3CompoundBaseAttrOperator[FilterSizePlugOperator]
):
    __slots__ = ()

    filterSizeX = FloatField(default_value=0.0, readable=False)
    fsx = filterSizeX

    filterSizeY = FloatField(default_value=0.0, readable=False)
    fsy = filterSizeY

    filterSizeZ = FloatField(default_value=0.0, readable=False)
    fsz = filterSizeZ


class FilterSizeField(
    Float3CompoundBaseField[FilterSizeAttrOperator, FilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FilterSizeAttrOperator
    PLUG_CLS = FilterSizePlugOperator

    filterSizeX = FloatField(default_value=0.0, readable=False)
    fsx = filterSizeX

    filterSizeY = FloatField(default_value=0.0, readable=False)
    fsy = filterSizeY

    filterSizeZ = FloatField(default_value=0.0, readable=False)
    fsz = filterSizeZ


class PointWorldPlugOperator(
    Float3CompoundBasePlugOperator["PointWorldAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointWorldX", "pwx"),
        ("pointWorldY", "pwy"),
        ("pointWorldZ", "pwz"),
    )

    pointWorldX = FloatField(default_value=0.0)
    pwx = pointWorldX

    pointWorldY = FloatField(default_value=0.0)
    pwy = pointWorldY

    pointWorldZ = FloatField(default_value=0.0)
    pwz = pointWorldZ


class PointWorldAttrOperator(
    Float3CompoundBaseAttrOperator[PointWorldPlugOperator]
):
    __slots__ = ()

    pointWorldX = FloatField(default_value=0.0)
    pwx = pointWorldX

    pointWorldY = FloatField(default_value=0.0)
    pwy = pointWorldY

    pointWorldZ = FloatField(default_value=0.0)
    pwz = pointWorldZ


class PointWorldField(
    Float3CompoundBaseField[PointWorldAttrOperator, PointWorldPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointWorldAttrOperator
    PLUG_CLS = PointWorldPlugOperator

    pointWorldX = FloatField(default_value=0.0)
    pwx = pointWorldX

    pointWorldY = FloatField(default_value=0.0)
    pwy = pointWorldY

    pointWorldZ = FloatField(default_value=0.0)
    pwz = pointWorldZ


class FarPointWorldPlugOperator(
    Float3CompoundBasePlugOperator["FarPointWorldAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("farPointWorldX", "fwx"),
        ("farPointWorldY", "fwy"),
        ("farPointWorldZ", "fwz"),
    )

    farPointWorldX = FloatField(default_value=1.0)
    fwx = farPointWorldX

    farPointWorldY = FloatField(default_value=1.0)
    fwy = farPointWorldY

    farPointWorldZ = FloatField(default_value=1.0)
    fwz = farPointWorldZ


class FarPointWorldAttrOperator(
    Float3CompoundBaseAttrOperator[FarPointWorldPlugOperator]
):
    __slots__ = ()

    farPointWorldX = FloatField(default_value=1.0)
    fwx = farPointWorldX

    farPointWorldY = FloatField(default_value=1.0)
    fwy = farPointWorldY

    farPointWorldZ = FloatField(default_value=1.0)
    fwz = farPointWorldZ


class FarPointWorldField(
    Float3CompoundBaseField[
        FarPointWorldAttrOperator, FarPointWorldPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = FarPointWorldAttrOperator
    PLUG_CLS = FarPointWorldPlugOperator

    farPointWorldX = FloatField(default_value=1.0)
    fwx = farPointWorldX

    farPointWorldY = FloatField(default_value=1.0)
    fwy = farPointWorldY

    farPointWorldZ = FloatField(default_value=1.0)
    fwz = farPointWorldZ


class PointObjPlugOperator(
    Float3CompoundBasePlugOperator["PointObjAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointObjX", "pox"),
        ("pointObjY", "poy"),
        ("pointObjZ", "poz"),
    )

    pointObjX = FloatField(default_value=0.0)
    pox = pointObjX

    pointObjY = FloatField(default_value=0.0)
    poy = pointObjY

    pointObjZ = FloatField(default_value=0.0)
    poz = pointObjZ


class PointObjAttrOperator(
    Float3CompoundBaseAttrOperator[PointObjPlugOperator]
):
    __slots__ = ()

    pointObjX = FloatField(default_value=0.0)
    pox = pointObjX

    pointObjY = FloatField(default_value=0.0)
    poy = pointObjY

    pointObjZ = FloatField(default_value=0.0)
    poz = pointObjZ


class PointObjField(
    Float3CompoundBaseField[PointObjAttrOperator, PointObjPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointObjAttrOperator
    PLUG_CLS = PointObjPlugOperator

    pointObjX = FloatField(default_value=0.0)
    pox = pointObjX

    pointObjY = FloatField(default_value=0.0)
    poy = pointObjY

    pointObjZ = FloatField(default_value=0.0)
    poz = pointObjZ


class FarPointObjPlugOperator(
    Float3CompoundBasePlugOperator["FarPointObjAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("farPointObjectX", "fox"),
        ("farPointObjectY", "foy"),
        ("farPointObjectZ", "foz"),
    )

    farPointObjectX = FloatField(default_value=1.0)
    fox = farPointObjectX

    farPointObjectY = FloatField(default_value=1.0)
    foy = farPointObjectY

    farPointObjectZ = FloatField(default_value=1.0)
    foz = farPointObjectZ


class FarPointObjAttrOperator(
    Float3CompoundBaseAttrOperator[FarPointObjPlugOperator]
):
    __slots__ = ()

    farPointObjectX = FloatField(default_value=1.0)
    fox = farPointObjectX

    farPointObjectY = FloatField(default_value=1.0)
    foy = farPointObjectY

    farPointObjectZ = FloatField(default_value=1.0)
    foz = farPointObjectZ


class FarPointObjField(
    Float3CompoundBaseField[FarPointObjAttrOperator, FarPointObjPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FarPointObjAttrOperator
    PLUG_CLS = FarPointObjPlugOperator

    farPointObjectX = FloatField(default_value=1.0)
    fox = farPointObjectX

    farPointObjectY = FloatField(default_value=1.0)
    foy = farPointObjectY

    farPointObjectZ = FloatField(default_value=1.0)
    foz = farPointObjectZ


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

    lightDirection = LightDataArray_lightDirectionField(
        default_value=(1.0, 1.0, 1.0), readable=False
    )
    ld = lightDirection

    lightIntensity = LightDataArray_lightIntensityField(
        default_value=(1.0, 1.0, 1.0), readable=False
    )
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

    lightDirection = LightDataArray_lightDirectionField(
        default_value=(1.0, 1.0, 1.0), readable=False
    )
    ld = lightDirection

    lightIntensity = LightDataArray_lightIntensityField(
        default_value=(1.0, 1.0, 1.0), readable=False
    )
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


class OpacityPlugOperator(CompoundPlugOperator["OpacityAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("opacity_Position", "opap"),
        ("opacity_FloatValue", "opafv"),
        ("opacity_Interp", "opai"),
    )

    opacity_Position = FloatField(default_value=0.0)
    opap = opacity_Position

    opacity_FloatValue = FloatField(default_value=0.0)
    opafv = opacity_FloatValue

    opacity_Interp = Opacity_opacity_InterpEnumField(default_value=0)
    opai = opacity_Interp


class OpacityAttrOperator(CompoundAttrOperator[OpacityPlugOperator]):
    __slots__ = ()

    opacity_Position = FloatField(default_value=0.0)
    opap = opacity_Position

    opacity_FloatValue = FloatField(default_value=0.0)
    opafv = opacity_FloatValue

    opacity_Interp = Opacity_opacity_InterpEnumField(default_value=0)
    opai = opacity_Interp


class OpacityField(CompoundField[OpacityAttrOperator, OpacityPlugOperator]):
    __slots__ = ()

    ATTR_CLS = OpacityAttrOperator
    PLUG_CLS = OpacityPlugOperator


class TransparencyPlugOperator(
    Float3CompoundBasePlugOperator["TransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transparencyR", "tr"),
        ("transparencyG", "tg"),
        ("transparencyB", "tb"),
    )

    transparencyR = FloatField(default_value=0.25)
    tr = transparencyR

    transparencyG = FloatField(default_value=0.25)
    tg = transparencyG

    transparencyB = FloatField(default_value=0.25)
    tb = transparencyB


class TransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[TransparencyPlugOperator]
):
    __slots__ = ()

    transparencyR = FloatField(default_value=0.25)
    tr = transparencyR

    transparencyG = FloatField(default_value=0.25)
    tg = transparencyG

    transparencyB = FloatField(default_value=0.25)
    tb = transparencyB


class TransparencyField(
    Float3CompoundBaseField[TransparencyAttrOperator, TransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencyAttrOperator
    PLUG_CLS = TransparencyPlugOperator

    transparencyR = FloatField(default_value=0.25)
    tr = transparencyR

    transparencyG = FloatField(default_value=0.25)
    tg = transparencyG

    transparencyB = FloatField(default_value=0.25)
    tb = transparencyB


class FluidLightColorPlugOperator(
    Float3CompoundBasePlugOperator["FluidLightColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fluidLightColorR", "flir"),
        ("fluidLightColorG", "flig"),
        ("fluidLightColorB", "flib"),
    )

    fluidLightColorR = FloatField(default_value=1.0)
    flir = fluidLightColorR

    fluidLightColorG = FloatField(default_value=1.0)
    flig = fluidLightColorG

    fluidLightColorB = FloatField(default_value=1.0)
    flib = fluidLightColorB


class FluidLightColorAttrOperator(
    Float3CompoundBaseAttrOperator[FluidLightColorPlugOperator]
):
    __slots__ = ()

    fluidLightColorR = FloatField(default_value=1.0)
    flir = fluidLightColorR

    fluidLightColorG = FloatField(default_value=1.0)
    flig = fluidLightColorG

    fluidLightColorB = FloatField(default_value=1.0)
    flib = fluidLightColorB


class FluidLightColorField(
    Float3CompoundBaseField[
        FluidLightColorAttrOperator, FluidLightColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = FluidLightColorAttrOperator
    PLUG_CLS = FluidLightColorPlugOperator

    fluidLightColorR = FloatField(default_value=1.0)
    flir = fluidLightColorR

    fluidLightColorG = FloatField(default_value=1.0)
    flig = fluidLightColorG

    fluidLightColorB = FloatField(default_value=1.0)
    flib = fluidLightColorB


class AmbientColorPlugOperator(
    Float3CompoundBasePlugOperator["AmbientColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ambientColorR", "ambr"),
        ("ambientColorG", "ambg"),
        ("ambientColorB", "ambb"),
    )

    ambientColorR = FloatField(default_value=0.5)
    ambr = ambientColorR

    ambientColorG = FloatField(default_value=0.699999988079071)
    ambg = ambientColorG

    ambientColorB = FloatField(default_value=1.0)
    ambb = ambientColorB


class AmbientColorAttrOperator(
    Float3CompoundBaseAttrOperator[AmbientColorPlugOperator]
):
    __slots__ = ()

    ambientColorR = FloatField(default_value=0.5)
    ambr = ambientColorR

    ambientColorG = FloatField(default_value=0.699999988079071)
    ambg = ambientColorG

    ambientColorB = FloatField(default_value=1.0)
    ambb = ambientColorB


class AmbientColorField(
    Float3CompoundBaseField[AmbientColorAttrOperator, AmbientColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AmbientColorAttrOperator
    PLUG_CLS = AmbientColorPlugOperator

    ambientColorR = FloatField(default_value=0.5)
    ambr = ambientColorR

    ambientColorG = FloatField(default_value=0.699999988079071)
    ambg = ambientColorG

    ambientColorB = FloatField(default_value=1.0)
    ambb = ambientColorB


class IncandescencePlugOperator(
    CompoundPlugOperator["IncandescenceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("incandescence_Position", "ip"),
        ("incandescence_Color", "ic"),
        ("incandescence_Interp", "ii"),
    )

    incandescence_Position = FloatField(default_value=0.0)
    ip = incandescence_Position

    incandescence_Color = Incandescence_incandescence_ColorField(
        default_value=(0.0, 0.0, 0.0)
    )
    ic = incandescence_Color

    incandescence_Interp = Incandescence_incandescence_InterpEnumField(
        default_value=0
    )
    ii = incandescence_Interp


class IncandescenceAttrOperator(
    CompoundAttrOperator[IncandescencePlugOperator]
):
    __slots__ = ()

    incandescence_Position = FloatField(default_value=0.0)
    ip = incandescence_Position

    incandescence_Color = Incandescence_incandescence_ColorField(
        default_value=(0.0, 0.0, 0.0)
    )
    ic = incandescence_Color

    incandescence_Interp = Incandescence_incandescence_InterpEnumField(
        default_value=0
    )
    ii = incandescence_Interp


class IncandescenceField(
    CompoundField[IncandescenceAttrOperator, IncandescencePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IncandescenceAttrOperator
    PLUG_CLS = IncandescencePlugOperator


class SpecularColorPlugOperator(
    Float3CompoundBasePlugOperator["SpecularColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularColorR", "spr"),
        ("specularColorG", "spg"),
        ("specularColorB", "spb"),
    )

    specularColorR = FloatField(default_value=0.0)
    spr = specularColorR

    specularColorG = FloatField(default_value=0.0)
    spg = specularColorG

    specularColorB = FloatField(default_value=0.0)
    spb = specularColorB


class SpecularColorAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularColorPlugOperator]
):
    __slots__ = ()

    specularColorR = FloatField(default_value=0.0)
    spr = specularColorR

    specularColorG = FloatField(default_value=0.0)
    spg = specularColorG

    specularColorB = FloatField(default_value=0.0)
    spb = specularColorB


class SpecularColorField(
    Float3CompoundBaseField[
        SpecularColorAttrOperator, SpecularColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SpecularColorAttrOperator
    PLUG_CLS = SpecularColorPlugOperator

    specularColorR = FloatField(default_value=0.0)
    spr = specularColorR

    specularColorG = FloatField(default_value=0.0)
    spg = specularColorG

    specularColorB = FloatField(default_value=0.0)
    spb = specularColorB


class EnvironmentPlugOperator(CompoundPlugOperator["EnvironmentAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("environment_Position", "envp"),
        ("environment_Color", "envc"),
        ("environment_Interp", "envi"),
    )

    environment_Position = FloatField(default_value=0.0)
    envp = environment_Position

    environment_Color = Environment_environment_ColorField(
        default_value=(0.0, 0.0, 0.0)
    )
    envc = environment_Color

    environment_Interp = Environment_environment_InterpEnumField(
        default_value=0
    )
    envi = environment_Interp


class EnvironmentAttrOperator(CompoundAttrOperator[EnvironmentPlugOperator]):
    __slots__ = ()

    environment_Position = FloatField(default_value=0.0)
    envp = environment_Position

    environment_Color = Environment_environment_ColorField(
        default_value=(0.0, 0.0, 0.0)
    )
    envc = environment_Color

    environment_Interp = Environment_environment_InterpEnumField(
        default_value=0
    )
    envi = environment_Interp


class EnvironmentField(
    CompoundField[EnvironmentAttrOperator, EnvironmentPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EnvironmentAttrOperator
    PLUG_CLS = EnvironmentPlugOperator


class PointLightPlugOperator(
    Float3CompoundBasePlugOperator["PointLightAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointLightX", "polx"),
        ("pointLightY", "poly"),
        ("pointLightZ", "polz"),
    )

    pointLightX = FloatField(default_value=0.0)
    polx = pointLightX

    pointLightY = FloatField(default_value=0.0)
    poly = pointLightY

    pointLightZ = FloatField(default_value=0.0)
    polz = pointLightZ


class PointLightAttrOperator(
    Float3CompoundBaseAttrOperator[PointLightPlugOperator]
):
    __slots__ = ()

    pointLightX = FloatField(default_value=0.0)
    polx = pointLightX

    pointLightY = FloatField(default_value=0.0)
    poly = pointLightY

    pointLightZ = FloatField(default_value=0.0)
    polz = pointLightZ


class PointLightField(
    Float3CompoundBaseField[PointLightAttrOperator, PointLightPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointLightAttrOperator
    PLUG_CLS = PointLightPlugOperator

    pointLightX = FloatField(default_value=0.0)
    polx = pointLightX

    pointLightY = FloatField(default_value=0.0)
    poly = pointLightY

    pointLightZ = FloatField(default_value=0.0)
    polz = pointLightZ


class DirectionalLightPlugOperator(
    Float3CompoundBasePlugOperator["DirectionalLightAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("directionalLightX", "dlx"),
        ("directionalLightY", "dly"),
        ("directionalLightZ", "dlz"),
    )

    directionalLightX = FloatField(default_value=0.5)
    dlx = directionalLightX

    directionalLightY = FloatField(default_value=0.800000011920929)
    dly = directionalLightY

    directionalLightZ = FloatField(default_value=0.5)
    dlz = directionalLightZ


class DirectionalLightAttrOperator(
    Float3CompoundBaseAttrOperator[DirectionalLightPlugOperator]
):
    __slots__ = ()

    directionalLightX = FloatField(default_value=0.5)
    dlx = directionalLightX

    directionalLightY = FloatField(default_value=0.800000011920929)
    dly = directionalLightY

    directionalLightZ = FloatField(default_value=0.5)
    dlz = directionalLightZ


class DirectionalLightField(
    Float3CompoundBaseField[
        DirectionalLightAttrOperator, DirectionalLightPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DirectionalLightAttrOperator
    PLUG_CLS = DirectionalLightPlugOperator

    directionalLightX = FloatField(default_value=0.5)
    dlx = directionalLightX

    directionalLightY = FloatField(default_value=0.800000011920929)
    dly = directionalLightY

    directionalLightZ = FloatField(default_value=0.5)
    dlz = directionalLightZ


class TextureScalePlugOperator(
    Float3CompoundBasePlugOperator["TextureScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("textureScaleX", "tscx"),
        ("textureScaleY", "tscy"),
        ("textureScaleZ", "tscz"),
    )

    textureScaleX = FloatField(default_value=1.0, min_value=0.0)
    tscx = textureScaleX

    textureScaleY = FloatField(default_value=1.0, min_value=0.0)
    tscy = textureScaleY

    textureScaleZ = FloatField(default_value=1.0, min_value=0.0)
    tscz = textureScaleZ


class TextureScaleAttrOperator(
    Float3CompoundBaseAttrOperator[TextureScalePlugOperator]
):
    __slots__ = ()

    textureScaleX = FloatField(default_value=1.0, min_value=0.0)
    tscx = textureScaleX

    textureScaleY = FloatField(default_value=1.0, min_value=0.0)
    tscy = textureScaleY

    textureScaleZ = FloatField(default_value=1.0, min_value=0.0)
    tscz = textureScaleZ


class TextureScaleField(
    Float3CompoundBaseField[TextureScaleAttrOperator, TextureScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TextureScaleAttrOperator
    PLUG_CLS = TextureScalePlugOperator

    textureScaleX = FloatField(default_value=1.0, min_value=0.0)
    tscx = textureScaleX

    textureScaleY = FloatField(default_value=1.0, min_value=0.0)
    tscy = textureScaleY

    textureScaleZ = FloatField(default_value=1.0, min_value=0.0)
    tscz = textureScaleZ


class TextureOriginPlugOperator(
    Float3CompoundBasePlugOperator["TextureOriginAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("textureOriginX", "torx"),
        ("textureOriginY", "tory"),
        ("textureOriginZ", "torz"),
    )

    textureOriginX = FloatField(
        default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0
    )
    torx = textureOriginX

    textureOriginY = FloatField(
        default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0
    )
    tory = textureOriginY

    textureOriginZ = FloatField(
        default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0
    )
    torz = textureOriginZ


class TextureOriginAttrOperator(
    Float3CompoundBaseAttrOperator[TextureOriginPlugOperator]
):
    __slots__ = ()

    textureOriginX = FloatField(
        default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0
    )
    torx = textureOriginX

    textureOriginY = FloatField(
        default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0
    )
    tory = textureOriginY

    textureOriginZ = FloatField(
        default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0
    )
    torz = textureOriginZ


class TextureOriginField(
    Float3CompoundBaseField[
        TextureOriginAttrOperator, TextureOriginPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = TextureOriginAttrOperator
    PLUG_CLS = TextureOriginPlugOperator

    textureOriginX = FloatField(
        default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0
    )
    torx = textureOriginX

    textureOriginY = FloatField(
        default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0
    )
    tory = textureOriginY

    textureOriginZ = FloatField(
        default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0
    )
    torz = textureOriginZ


class TextureRotatePlugOperator(
    Float3CompoundBasePlugOperator["TextureRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("textureRotateX", "trtx"),
        ("textureRotateY", "trty"),
        ("textureRotateZ", "trtz"),
    )

    textureRotateX = FloatField(default_value=0.0)
    trtx = textureRotateX

    textureRotateY = FloatField(default_value=0.0)
    trty = textureRotateY

    textureRotateZ = FloatField(default_value=0.0)
    trtz = textureRotateZ


class TextureRotateAttrOperator(
    Float3CompoundBaseAttrOperator[TextureRotatePlugOperator]
):
    __slots__ = ()

    textureRotateX = FloatField(default_value=0.0)
    trtx = textureRotateX

    textureRotateY = FloatField(default_value=0.0)
    trty = textureRotateY

    textureRotateZ = FloatField(default_value=0.0)
    trtz = textureRotateZ


class TextureRotateField(
    Float3CompoundBaseField[
        TextureRotateAttrOperator, TextureRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = TextureRotateAttrOperator
    PLUG_CLS = TextureRotatePlugOperator

    textureRotateX = FloatField(default_value=0.0)
    trtx = textureRotateX

    textureRotateY = FloatField(default_value=0.0)
    trty = textureRotateY

    textureRotateZ = FloatField(default_value=0.0)
    trtz = textureRotateZ


class ImplodeCenterPlugOperator(
    Float3CompoundBasePlugOperator["ImplodeCenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("implodeCenterX", "imx"),
        ("implodeCenterY", "imy"),
        ("implodeCenterZ", "imz"),
    )

    implodeCenterX = FloatField(default_value=0.0)
    imx = implodeCenterX

    implodeCenterY = FloatField(default_value=0.0)
    imy = implodeCenterY

    implodeCenterZ = FloatField(default_value=0.0)
    imz = implodeCenterZ


class ImplodeCenterAttrOperator(
    Float3CompoundBaseAttrOperator[ImplodeCenterPlugOperator]
):
    __slots__ = ()

    implodeCenterX = FloatField(default_value=0.0)
    imx = implodeCenterX

    implodeCenterY = FloatField(default_value=0.0)
    imy = implodeCenterY

    implodeCenterZ = FloatField(default_value=0.0)
    imz = implodeCenterZ


class ImplodeCenterField(
    Float3CompoundBaseField[
        ImplodeCenterAttrOperator, ImplodeCenterPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ImplodeCenterAttrOperator
    PLUG_CLS = ImplodeCenterPlugOperator

    implodeCenterX = FloatField(default_value=0.0)
    imx = implodeCenterX

    implodeCenterY = FloatField(default_value=0.0)
    imy = implodeCenterY

    implodeCenterZ = FloatField(default_value=0.0)
    imz = implodeCenterZ


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


class CollisionDataPlugOperator(
    CompoundPlugOperator["CollisionDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionGeometry", "cge"),
        ("collisionResilience", "crs"),
        ("collisionFriction", "cfr"),
    )

    collisionGeometry = TypedField(multi=True, readable=False)
    cge = collisionGeometry

    collisionResilience = DoubleField(
        multi=True, default_value=0.0, readable=False
    )
    crs = collisionResilience

    collisionFriction = DoubleField(
        multi=True, default_value=0.0, readable=False
    )
    cfr = collisionFriction


class CollisionDataAttrOperator(
    CompoundAttrOperator[CollisionDataPlugOperator]
):
    __slots__ = ()

    collisionGeometry = TypedField(multi=True, readable=False)
    cge = collisionGeometry

    collisionResilience = DoubleField(
        multi=True, default_value=0.0, readable=False
    )
    crs = collisionResilience

    collisionFriction = DoubleField(
        multi=True, default_value=0.0, readable=False
    )
    cfr = collisionFriction


class CollisionDataField(
    CompoundField[CollisionDataAttrOperator, CollisionDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollisionDataAttrOperator
    PLUG_CLS = CollisionDataPlugOperator

    collisionGeometry = TypedField(multi=True, readable=False)
    cge = collisionGeometry

    collisionResilience = DoubleField(
        multi=True, default_value=0.0, readable=False
    )
    crs = collisionResilience

    collisionFriction = DoubleField(
        multi=True, default_value=0.0, readable=False
    )
    cfr = collisionFriction


class UvCoordPlugOperator(
    Float2CompoundBasePlugOperator["UvCoordAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uCoord", "uvu"),
        ("vCoord", "uvv"),
    )

    uCoord = FloatField(default_value=0.0)
    uvu = uCoord

    vCoord = FloatField(default_value=0.0)
    uvv = vCoord


class UvCoordAttrOperator(Float2CompoundBaseAttrOperator[UvCoordPlugOperator]):
    __slots__ = ()

    uCoord = FloatField(default_value=0.0)
    uvu = uCoord

    vCoord = FloatField(default_value=0.0)
    uvv = vCoord


class UvCoordField(
    Float2CompoundBaseField[UvCoordAttrOperator, UvCoordPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvCoordAttrOperator
    PLUG_CLS = UvCoordPlugOperator

    uCoord = FloatField(default_value=0.0)
    uvu = uCoord

    vCoord = FloatField(default_value=0.0)
    uvv = vCoord


class UvFilterSizePlugOperator(
    Float2CompoundBasePlugOperator["UvFilterSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvFilterSizeX", "uvfsx"),
        ("uvFilterSizeY", "uvfsy"),
    )

    uvFilterSizeX = FloatField(default_value=0.0)
    uvfsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    uvfsy = uvFilterSizeY


class UvFilterSizeAttrOperator(
    Float2CompoundBaseAttrOperator[UvFilterSizePlugOperator]
):
    __slots__ = ()

    uvFilterSizeX = FloatField(default_value=0.0)
    uvfsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    uvfsy = uvFilterSizeY


class UvFilterSizeField(
    Float2CompoundBaseField[UvFilterSizeAttrOperator, UvFilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvFilterSizeAttrOperator
    PLUG_CLS = UvFilterSizePlugOperator

    uvFilterSizeX = FloatField(default_value=0.0)
    uvfsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    uvfsy = uvFilterSizeY


class OutUVPlugOperator(Float2CompoundBasePlugOperator["OutUVAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outU", "ou"),
        ("outV", "ov"),
    )

    outU = FloatField(default_value=0.0, writable=False)
    ou = outU

    outV = FloatField(default_value=0.0, writable=False)
    ov = outV


class OutUVAttrOperator(Float2CompoundBaseAttrOperator[OutUVPlugOperator]):
    __slots__ = ()

    outU = FloatField(default_value=0.0, writable=False)
    ou = outU

    outV = FloatField(default_value=0.0, writable=False)
    ov = outV


class OutUVField(
    Float2CompoundBaseField[OutUVAttrOperator, OutUVPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutUVAttrOperator
    PLUG_CLS = OutUVPlugOperator

    outU = FloatField(default_value=0.0, writable=False)
    ou = outU

    outV = FloatField(default_value=0.0, writable=False)
    ov = outV


class DefaultColorPlugOperator(
    Float3CompoundBasePlugOperator["DefaultColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("defaultColorR", "dcr"),
        ("defaultColorG", "dcg"),
        ("defaultColorB", "dcb"),
    )

    defaultColorR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcr = defaultColorR

    defaultColorG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcg = defaultColorG

    defaultColorB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcb = defaultColorB


class DefaultColorAttrOperator(
    Float3CompoundBaseAttrOperator[DefaultColorPlugOperator]
):
    __slots__ = ()

    defaultColorR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcr = defaultColorR

    defaultColorG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcg = defaultColorG

    defaultColorB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcb = defaultColorB


class DefaultColorField(
    Float3CompoundBaseField[DefaultColorAttrOperator, DefaultColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DefaultColorAttrOperator
    PLUG_CLS = DefaultColorPlugOperator

    defaultColorR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcr = defaultColorR

    defaultColorG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcg = defaultColorG

    defaultColorB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcb = defaultColorB


class AiVolumeTexturePlugOperator(
    Float3CompoundBasePlugOperator["AiVolumeTextureAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiVolumeTextureR", "ai_volume_texturer"),
        ("aiVolumeTextureG", "ai_volume_textureg"),
        ("aiVolumeTextureB", "ai_volume_textureb"),
    )

    aiVolumeTextureR = FloatField(default_value=1.0)
    ai_volume_texturer = aiVolumeTextureR

    aiVolumeTextureG = FloatField(default_value=0.0)
    ai_volume_textureg = aiVolumeTextureG

    aiVolumeTextureB = FloatField(default_value=0.0)
    ai_volume_textureb = aiVolumeTextureB


class AiVolumeTextureAttrOperator(
    Float3CompoundBaseAttrOperator[AiVolumeTexturePlugOperator]
):
    __slots__ = ()

    aiVolumeTextureR = FloatField(default_value=1.0)
    ai_volume_texturer = aiVolumeTextureR

    aiVolumeTextureG = FloatField(default_value=0.0)
    ai_volume_textureg = aiVolumeTextureG

    aiVolumeTextureB = FloatField(default_value=0.0)
    ai_volume_textureb = aiVolumeTextureB


class AiVolumeTextureField(
    Float3CompoundBaseField[
        AiVolumeTextureAttrOperator, AiVolumeTexturePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiVolumeTextureAttrOperator
    PLUG_CLS = AiVolumeTexturePlugOperator

    aiVolumeTextureR = FloatField(default_value=1.0)
    ai_volume_texturer = aiVolumeTextureR

    aiVolumeTextureG = FloatField(default_value=0.0)
    ai_volume_textureg = aiVolumeTextureG

    aiVolumeTextureB = FloatField(default_value=0.0)
    ai_volume_textureb = aiVolumeTextureB
