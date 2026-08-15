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
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.at.scalar.unit.range.float_linear import FloatLinearField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
    Double2CompoundBaseAttrOperator,
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseField,
    FloatLinear3CompoundBaseAttrOperator,
    FloatLinear3CompoundBasePlugOperator,
    FloatLinear3CompoundBaseField,
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
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


class ColorPerVertex_vertexColor_vertexFaceColor_vertexFaceColorRGBPlugOperator(
    Float3CompoundBasePlugOperator[
        "ColorPerVertex_vertexColor_vertexFaceColor_vertexFaceColorRGBAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexFaceColorR", "vfcr"),
        ("vertexFaceColorG", "vfcg"),
        ("vertexFaceColorB", "vfcb"),
    )

    vertexFaceColorR = FloatField(default_value=0.0, max_value=1.0)
    vfcr = vertexFaceColorR

    vertexFaceColorG = FloatField(default_value=0.0, max_value=1.0)
    vfcg = vertexFaceColorG

    vertexFaceColorB = FloatField(default_value=0.0, max_value=1.0)
    vfcb = vertexFaceColorB


class ColorPerVertex_vertexColor_vertexFaceColor_vertexFaceColorRGBAttrOperator(
    Float3CompoundBaseAttrOperator[
        ColorPerVertex_vertexColor_vertexFaceColor_vertexFaceColorRGBPlugOperator
    ]
):
    __slots__ = ()

    vertexFaceColorR = FloatField(default_value=0.0, max_value=1.0)
    vfcr = vertexFaceColorR

    vertexFaceColorG = FloatField(default_value=0.0, max_value=1.0)
    vfcg = vertexFaceColorG

    vertexFaceColorB = FloatField(default_value=0.0, max_value=1.0)
    vfcb = vertexFaceColorB


class ColorPerVertex_vertexColor_vertexFaceColor_vertexFaceColorRGBField(
    Float3CompoundBaseField[
        ColorPerVertex_vertexColor_vertexFaceColor_vertexFaceColorRGBAttrOperator,
        ColorPerVertex_vertexColor_vertexFaceColor_vertexFaceColorRGBPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ColorPerVertex_vertexColor_vertexFaceColor_vertexFaceColorRGBAttrOperator
    PLUG_CLS = ColorPerVertex_vertexColor_vertexFaceColor_vertexFaceColorRGBPlugOperator

    vertexFaceColorR = FloatField(default_value=0.0, max_value=1.0)
    vfcr = vertexFaceColorR

    vertexFaceColorG = FloatField(default_value=0.0, max_value=1.0)
    vfcg = vertexFaceColorG

    vertexFaceColorB = FloatField(default_value=0.0, max_value=1.0)
    vfcb = vertexFaceColorB


class NormalPerVertex_vertexNormal_vertexFaceNormal_vertexFaceNormalXYZPlugOperator(
    Float3CompoundBasePlugOperator[
        "NormalPerVertex_vertexNormal_vertexFaceNormal_vertexFaceNormalXYZAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexFaceNormalX", "vfnx"),
        ("vertexFaceNormalY", "vfny"),
        ("vertexFaceNormalZ", "vfnz"),
    )

    vertexFaceNormalX = FloatField(default_value=1.0000000200408773e20)
    vfnx = vertexFaceNormalX

    vertexFaceNormalY = FloatField(default_value=1.0000000200408773e20)
    vfny = vertexFaceNormalY

    vertexFaceNormalZ = FloatField(default_value=1.0000000200408773e20)
    vfnz = vertexFaceNormalZ


class NormalPerVertex_vertexNormal_vertexFaceNormal_vertexFaceNormalXYZAttrOperator(
    Float3CompoundBaseAttrOperator[
        NormalPerVertex_vertexNormal_vertexFaceNormal_vertexFaceNormalXYZPlugOperator
    ]
):
    __slots__ = ()

    vertexFaceNormalX = FloatField(default_value=1.0000000200408773e20)
    vfnx = vertexFaceNormalX

    vertexFaceNormalY = FloatField(default_value=1.0000000200408773e20)
    vfny = vertexFaceNormalY

    vertexFaceNormalZ = FloatField(default_value=1.0000000200408773e20)
    vfnz = vertexFaceNormalZ


class NormalPerVertex_vertexNormal_vertexFaceNormal_vertexFaceNormalXYZField(
    Float3CompoundBaseField[
        NormalPerVertex_vertexNormal_vertexFaceNormal_vertexFaceNormalXYZAttrOperator,
        NormalPerVertex_vertexNormal_vertexFaceNormal_vertexFaceNormalXYZPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = NormalPerVertex_vertexNormal_vertexFaceNormal_vertexFaceNormalXYZAttrOperator
    PLUG_CLS = NormalPerVertex_vertexNormal_vertexFaceNormal_vertexFaceNormalXYZPlugOperator

    vertexFaceNormalX = FloatField(default_value=1.0000000200408773e20)
    vfnx = vertexFaceNormalX

    vertexFaceNormalY = FloatField(default_value=1.0000000200408773e20)
    vfny = vertexFaceNormalY

    vertexFaceNormalZ = FloatField(default_value=1.0000000200408773e20)
    vfnz = vertexFaceNormalZ


class ColorPerVertex_vertexColor_vertexColorRGBPlugOperator(
    Float3CompoundBasePlugOperator[
        "ColorPerVertex_vertexColor_vertexColorRGBAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexColorR", "vxcr"),
        ("vertexColorG", "vxcg"),
        ("vertexColorB", "vxcb"),
    )

    vertexColorR = FloatField(default_value=0.0)
    vxcr = vertexColorR

    vertexColorG = FloatField(default_value=0.0)
    vxcg = vertexColorG

    vertexColorB = FloatField(default_value=0.0)
    vxcb = vertexColorB


class ColorPerVertex_vertexColor_vertexColorRGBAttrOperator(
    Float3CompoundBaseAttrOperator[
        ColorPerVertex_vertexColor_vertexColorRGBPlugOperator
    ]
):
    __slots__ = ()

    vertexColorR = FloatField(default_value=0.0)
    vxcr = vertexColorR

    vertexColorG = FloatField(default_value=0.0)
    vxcg = vertexColorG

    vertexColorB = FloatField(default_value=0.0)
    vxcb = vertexColorB


class ColorPerVertex_vertexColor_vertexColorRGBField(
    Float3CompoundBaseField[
        ColorPerVertex_vertexColor_vertexColorRGBAttrOperator,
        ColorPerVertex_vertexColor_vertexColorRGBPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ColorPerVertex_vertexColor_vertexColorRGBAttrOperator
    PLUG_CLS = ColorPerVertex_vertexColor_vertexColorRGBPlugOperator

    vertexColorR = FloatField(default_value=0.0)
    vxcr = vertexColorR

    vertexColorG = FloatField(default_value=0.0)
    vxcg = vertexColorG

    vertexColorB = FloatField(default_value=0.0)
    vxcb = vertexColorB


class ColorPerVertex_vertexColor_vertexFaceColorPlugOperator(
    CompoundPlugOperator[
        "ColorPerVertex_vertexColor_vertexFaceColorAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexFaceColorRGB", "frgb"),
        ("vertexFaceAlpha", "vfal"),
    )

    vertexFaceColorRGB = (
        ColorPerVertex_vertexColor_vertexFaceColor_vertexFaceColorRGBField(
            default_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0)
        )
    )
    frgb = vertexFaceColorRGB

    vertexFaceAlpha = FloatField(default_value=1.0, max_value=1.0)
    vfal = vertexFaceAlpha


class ColorPerVertex_vertexColor_vertexFaceColorAttrOperator(
    CompoundAttrOperator[
        ColorPerVertex_vertexColor_vertexFaceColorPlugOperator
    ]
):
    __slots__ = ()

    vertexFaceColorRGB = (
        ColorPerVertex_vertexColor_vertexFaceColor_vertexFaceColorRGBField(
            default_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0)
        )
    )
    frgb = vertexFaceColorRGB

    vertexFaceAlpha = FloatField(default_value=1.0, max_value=1.0)
    vfal = vertexFaceAlpha


class ColorPerVertex_vertexColor_vertexFaceColorField(
    CompoundField[
        ColorPerVertex_vertexColor_vertexFaceColorAttrOperator,
        ColorPerVertex_vertexColor_vertexFaceColorPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ColorPerVertex_vertexColor_vertexFaceColorAttrOperator
    PLUG_CLS = ColorPerVertex_vertexColor_vertexFaceColorPlugOperator


class NormalPerVertex_vertexNormal_vertexNormalXYZPlugOperator(
    Float3CompoundBasePlugOperator[
        "NormalPerVertex_vertexNormal_vertexNormalXYZAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexNormalX", "vxnx"),
        ("vertexNormalY", "vxny"),
        ("vertexNormalZ", "vxnz"),
    )

    vertexNormalX = FloatField(default_value=1.0000000200408773e20)
    vxnx = vertexNormalX

    vertexNormalY = FloatField(default_value=1.0000000200408773e20)
    vxny = vertexNormalY

    vertexNormalZ = FloatField(default_value=1.0000000200408773e20)
    vxnz = vertexNormalZ


class NormalPerVertex_vertexNormal_vertexNormalXYZAttrOperator(
    Float3CompoundBaseAttrOperator[
        NormalPerVertex_vertexNormal_vertexNormalXYZPlugOperator
    ]
):
    __slots__ = ()

    vertexNormalX = FloatField(default_value=1.0000000200408773e20)
    vxnx = vertexNormalX

    vertexNormalY = FloatField(default_value=1.0000000200408773e20)
    vxny = vertexNormalY

    vertexNormalZ = FloatField(default_value=1.0000000200408773e20)
    vxnz = vertexNormalZ


class NormalPerVertex_vertexNormal_vertexNormalXYZField(
    Float3CompoundBaseField[
        NormalPerVertex_vertexNormal_vertexNormalXYZAttrOperator,
        NormalPerVertex_vertexNormal_vertexNormalXYZPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = NormalPerVertex_vertexNormal_vertexNormalXYZAttrOperator
    PLUG_CLS = NormalPerVertex_vertexNormal_vertexNormalXYZPlugOperator

    vertexNormalX = FloatField(default_value=1.0000000200408773e20)
    vxnx = vertexNormalX

    vertexNormalY = FloatField(default_value=1.0000000200408773e20)
    vxny = vertexNormalY

    vertexNormalZ = FloatField(default_value=1.0000000200408773e20)
    vxnz = vertexNormalZ


class NormalPerVertex_vertexNormal_vertexFaceNormalPlugOperator(
    CompoundPlugOperator[
        "NormalPerVertex_vertexNormal_vertexFaceNormalAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("vertexFaceNormalXYZ", "fnxy"),)

    vertexFaceNormalXYZ = (
        NormalPerVertex_vertexNormal_vertexFaceNormal_vertexFaceNormalXYZField(
            default_value=(
                1.0000000200408773e20,
                1.0000000200408773e20,
                1.0000000200408773e20,
            )
        )
    )
    fnxy = vertexFaceNormalXYZ


class NormalPerVertex_vertexNormal_vertexFaceNormalAttrOperator(
    CompoundAttrOperator[
        NormalPerVertex_vertexNormal_vertexFaceNormalPlugOperator
    ]
):
    __slots__ = ()

    vertexFaceNormalXYZ = (
        NormalPerVertex_vertexNormal_vertexFaceNormal_vertexFaceNormalXYZField(
            default_value=(
                1.0000000200408773e20,
                1.0000000200408773e20,
                1.0000000200408773e20,
            )
        )
    )
    fnxy = vertexFaceNormalXYZ


class NormalPerVertex_vertexNormal_vertexFaceNormalField(
    CompoundField[
        NormalPerVertex_vertexNormal_vertexFaceNormalAttrOperator,
        NormalPerVertex_vertexNormal_vertexFaceNormalPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = NormalPerVertex_vertexNormal_vertexFaceNormalAttrOperator
    PLUG_CLS = NormalPerVertex_vertexNormal_vertexFaceNormalPlugOperator


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


class ColorPerVertex_vertexColorPlugOperator(
    CompoundPlugOperator["ColorPerVertex_vertexColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexColorRGB", "vrgb"),
        ("vertexAlpha", "vxal"),
        ("vertexFaceColor", "vfcl"),
    )

    vertexColorRGB = ColorPerVertex_vertexColor_vertexColorRGBField(
        default_value=(0.0, 0.0, 0.0)
    )
    vrgb = vertexColorRGB

    vertexAlpha = FloatField(default_value=1.0, max_value=1.0)
    vxal = vertexAlpha

    vertexFaceColor = ColorPerVertex_vertexColor_vertexFaceColorField(
        multi=True
    )
    vfcl = vertexFaceColor


class ColorPerVertex_vertexColorAttrOperator(
    CompoundAttrOperator[ColorPerVertex_vertexColorPlugOperator]
):
    __slots__ = ()

    vertexColorRGB = ColorPerVertex_vertexColor_vertexColorRGBField(
        default_value=(0.0, 0.0, 0.0)
    )
    vrgb = vertexColorRGB

    vertexAlpha = FloatField(default_value=1.0, max_value=1.0)
    vxal = vertexAlpha

    vertexFaceColor = ColorPerVertex_vertexColor_vertexFaceColorField(
        multi=True
    )
    vfcl = vertexFaceColor


class ColorPerVertex_vertexColorField(
    CompoundField[
        ColorPerVertex_vertexColorAttrOperator,
        ColorPerVertex_vertexColorPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ColorPerVertex_vertexColorAttrOperator
    PLUG_CLS = ColorPerVertex_vertexColorPlugOperator


class NormalPerVertex_vertexNormalPlugOperator(
    CompoundPlugOperator["NormalPerVertex_vertexNormalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexNormalXYZ", "nxyz"),
        ("vertexFaceNormal", "vfnl"),
    )

    vertexNormalXYZ = NormalPerVertex_vertexNormal_vertexNormalXYZField(
        default_value=(
            1.0000000200408773e20,
            1.0000000200408773e20,
            1.0000000200408773e20,
        )
    )
    nxyz = vertexNormalXYZ

    vertexFaceNormal = NormalPerVertex_vertexNormal_vertexFaceNormalField(
        multi=True
    )
    vfnl = vertexFaceNormal


class NormalPerVertex_vertexNormalAttrOperator(
    CompoundAttrOperator[NormalPerVertex_vertexNormalPlugOperator]
):
    __slots__ = ()

    vertexNormalXYZ = NormalPerVertex_vertexNormal_vertexNormalXYZField(
        default_value=(
            1.0000000200408773e20,
            1.0000000200408773e20,
            1.0000000200408773e20,
        )
    )
    nxyz = vertexNormalXYZ

    vertexFaceNormal = NormalPerVertex_vertexNormal_vertexFaceNormalField(
        multi=True
    )
    vfnl = vertexFaceNormal


class NormalPerVertex_vertexNormalField(
    CompoundField[
        NormalPerVertex_vertexNormalAttrOperator,
        NormalPerVertex_vertexNormalPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = NormalPerVertex_vertexNormalAttrOperator
    PLUG_CLS = NormalPerVertex_vertexNormalPlugOperator


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


class SmoothOffsetPlugOperator(
    Float3CompoundBasePlugOperator["SmoothOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sofx", "sx"),
        ("sofy", "sy"),
        ("sofz", "sz"),
    )

    sofx = FloatField(default_value=0.0)
    sx = sofx

    sofy = FloatField(default_value=0.0)
    sy = sofy

    sofz = FloatField(default_value=0.0)
    sz = sofz


class SmoothOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[SmoothOffsetPlugOperator]
):
    __slots__ = ()

    sofx = FloatField(default_value=0.0)
    sx = sofx

    sofy = FloatField(default_value=0.0)
    sy = sofy

    sofz = FloatField(default_value=0.0)
    sz = sofz


class SmoothOffsetField(
    Float3CompoundBaseField[SmoothOffsetAttrOperator, SmoothOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SmoothOffsetAttrOperator
    PLUG_CLS = SmoothOffsetPlugOperator

    sofx = FloatField(default_value=0.0)
    sx = sofx

    sofy = FloatField(default_value=0.0)
    sy = sofy

    sofz = FloatField(default_value=0.0)
    sz = sofz


class PntsPlugOperator(
    FloatLinear3CompoundBasePlugOperator["PntsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pntx", "px"),
        ("pnty", "py"),
        ("pntz", "pz"),
    )

    pntx = FloatLinearField(default_value=0.0)
    px = pntx

    pnty = FloatLinearField(default_value=0.0)
    py = pnty

    pntz = FloatLinearField(default_value=0.0)
    pz = pntz


class PntsAttrOperator(FloatLinear3CompoundBaseAttrOperator[PntsPlugOperator]):
    __slots__ = ()

    pntx = FloatLinearField(default_value=0.0)
    px = pntx

    pnty = FloatLinearField(default_value=0.0)
    py = pnty

    pntz = FloatLinearField(default_value=0.0)
    pz = pntz


class PntsField(
    FloatLinear3CompoundBaseField[PntsAttrOperator, PntsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PntsAttrOperator
    PLUG_CLS = PntsPlugOperator


class VrtsPlugOperator(Float3CompoundBasePlugOperator["VrtsAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vrtx", "vx"),
        ("vrty", "vy"),
        ("vrtz", "vz"),
    )

    vrtx = FloatField(default_value=0.0)
    vx = vrtx

    vrty = FloatField(default_value=0.0)
    vy = vrty

    vrtz = FloatField(default_value=0.0)
    vz = vrtz


class VrtsAttrOperator(Float3CompoundBaseAttrOperator[VrtsPlugOperator]):
    __slots__ = ()

    vrtx = FloatField(default_value=0.0)
    vx = vrtx

    vrty = FloatField(default_value=0.0)
    vy = vrty

    vrtz = FloatField(default_value=0.0)
    vz = vrtz


class VrtsField(Float3CompoundBaseField[VrtsAttrOperator, VrtsPlugOperator]):
    __slots__ = ()

    ATTR_CLS = VrtsAttrOperator
    PLUG_CLS = VrtsPlugOperator


class EdgePlugOperator(Long3CompoundBasePlugOperator["EdgeAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("edg1", "e1"),
        ("edg2", "e2"),
        ("edgh", "eh"),
    )

    edg1 = LongField(default_value=0)
    e1 = edg1

    edg2 = LongField(default_value=0)
    e2 = edg2

    edgh = LongField(default_value=0)
    eh = edgh


class EdgeAttrOperator(Long3CompoundBaseAttrOperator[EdgePlugOperator]):
    __slots__ = ()

    edg1 = LongField(default_value=0)
    e1 = edg1

    edg2 = LongField(default_value=0)
    e2 = edg2

    edgh = LongField(default_value=0)
    eh = edgh


class EdgeField(Long3CompoundBaseField[EdgeAttrOperator, EdgePlugOperator]):
    __slots__ = ()

    ATTR_CLS = EdgeAttrOperator
    PLUG_CLS = EdgePlugOperator


class UvptPlugOperator(Float2CompoundBasePlugOperator["UvptAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvpx", "ux"),
        ("uvpy", "uy"),
    )

    uvpx = FloatField(default_value=0.0)
    ux = uvpx

    uvpy = FloatField(default_value=0.0)
    uy = uvpy


class UvptAttrOperator(Float2CompoundBaseAttrOperator[UvptPlugOperator]):
    __slots__ = ()

    uvpx = FloatField(default_value=0.0)
    ux = uvpx

    uvpy = FloatField(default_value=0.0)
    uy = uvpy


class UvptField(Float2CompoundBaseField[UvptAttrOperator, UvptPlugOperator]):
    __slots__ = ()

    ATTR_CLS = UvptAttrOperator
    PLUG_CLS = UvptPlugOperator


class ColorsPlugOperator(CompoundPlugOperator["ColorsAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "clrr"),
        ("colorG", "clrg"),
        ("colorB", "clrb"),
        ("colorA", "clra"),
    )

    colorR = FloatField(default_value=0.0)
    clrr = colorR

    colorG = FloatField(default_value=0.0)
    clrg = colorG

    colorB = FloatField(default_value=0.0)
    clrb = colorB

    colorA = FloatField(default_value=0.0)
    clra = colorA


class ColorsAttrOperator(CompoundAttrOperator[ColorsPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=0.0)
    clrr = colorR

    colorG = FloatField(default_value=0.0)
    clrg = colorG

    colorB = FloatField(default_value=0.0)
    clrb = colorB

    colorA = FloatField(default_value=0.0)
    clra = colorA


class ColorsField(CompoundField[ColorsAttrOperator, ColorsPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ColorsAttrOperator
    PLUG_CLS = ColorsPlugOperator


class NormalsPlugOperator(
    Float3CompoundBasePlugOperator["NormalsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalx", "nx"),
        ("normaly", "ny"),
        ("normalz", "nz"),
    )

    normalx = FloatField(default_value=1.0000000200408773e20)
    nx = normalx

    normaly = FloatField(default_value=1.0000000200408773e20)
    ny = normaly

    normalz = FloatField(default_value=1.0000000200408773e20)
    nz = normalz


class NormalsAttrOperator(Float3CompoundBaseAttrOperator[NormalsPlugOperator]):
    __slots__ = ()

    normalx = FloatField(default_value=1.0000000200408773e20)
    nx = normalx

    normaly = FloatField(default_value=1.0000000200408773e20)
    ny = normaly

    normalz = FloatField(default_value=1.0000000200408773e20)
    nz = normalz


class NormalsField(
    Float3CompoundBaseField[NormalsAttrOperator, NormalsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalsAttrOperator
    PLUG_CLS = NormalsPlugOperator


class ColorPerVertexPlugOperator(
    CompoundPlugOperator["ColorPerVertexAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("vertexColor", "vclr"),)

    vertexColor = ColorPerVertex_vertexColorField(multi=True)
    vclr = vertexColor


class ColorPerVertexAttrOperator(
    CompoundAttrOperator[ColorPerVertexPlugOperator]
):
    __slots__ = ()

    vertexColor = ColorPerVertex_vertexColorField(multi=True)
    vclr = vertexColor


class ColorPerVertexField(
    CompoundField[ColorPerVertexAttrOperator, ColorPerVertexPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorPerVertexAttrOperator
    PLUG_CLS = ColorPerVertexPlugOperator

    vertexColor = ColorPerVertex_vertexColorField(multi=True)
    vclr = vertexColor


class NormalPerVertexPlugOperator(
    CompoundPlugOperator["NormalPerVertexAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("vertexNormal", "vn"),)

    vertexNormal = NormalPerVertex_vertexNormalField(multi=True)
    vn = vertexNormal


class NormalPerVertexAttrOperator(
    CompoundAttrOperator[NormalPerVertexPlugOperator]
):
    __slots__ = ()

    vertexNormal = NormalPerVertex_vertexNormalField(multi=True)
    vn = vertexNormal


class NormalPerVertexField(
    CompoundField[NormalPerVertexAttrOperator, NormalPerVertexPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalPerVertexAttrOperator
    PLUG_CLS = NormalPerVertexPlugOperator

    vertexNormal = NormalPerVertex_vertexNormalField(multi=True)
    vn = vertexNormal


class AiShadowColorPlugOperator(
    Float3CompoundBasePlugOperator["AiShadowColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiShadowColorR", "ai_shadow_colorr"),
        ("aiShadowColorG", "ai_shadow_colorg"),
        ("aiShadowColorB", "ai_shadow_colorb"),
    )

    aiShadowColorR = FloatField(default_value=0.0)
    ai_shadow_colorr = aiShadowColorR

    aiShadowColorG = FloatField(default_value=0.0)
    ai_shadow_colorg = aiShadowColorG

    aiShadowColorB = FloatField(default_value=0.0)
    ai_shadow_colorb = aiShadowColorB


class AiShadowColorAttrOperator(
    Float3CompoundBaseAttrOperator[AiShadowColorPlugOperator]
):
    __slots__ = ()

    aiShadowColorR = FloatField(default_value=0.0)
    ai_shadow_colorr = aiShadowColorR

    aiShadowColorG = FloatField(default_value=0.0)
    ai_shadow_colorg = aiShadowColorG

    aiShadowColorB = FloatField(default_value=0.0)
    ai_shadow_colorb = aiShadowColorB


class AiShadowColorField(
    Float3CompoundBaseField[
        AiShadowColorAttrOperator, AiShadowColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiShadowColorAttrOperator
    PLUG_CLS = AiShadowColorPlugOperator

    aiShadowColorR = FloatField(default_value=0.0)
    ai_shadow_colorr = aiShadowColorR

    aiShadowColorG = FloatField(default_value=0.0)
    ai_shadow_colorg = aiShadowColorG

    aiShadowColorB = FloatField(default_value=0.0)
    ai_shadow_colorb = aiShadowColorB


class ColorPlugOperator(Float3CompoundBasePlugOperator["ColorAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorRed", "scr"),
        ("colorGreen", "scg"),
        ("colorBlue", "scb"),
    )

    colorRed = FloatField(default_value=1.0)
    scr = colorRed

    colorGreen = FloatField(default_value=1.0)
    scg = colorGreen

    colorBlue = FloatField(default_value=1.0)
    scb = colorBlue


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorRed = FloatField(default_value=1.0)
    scr = colorRed

    colorGreen = FloatField(default_value=1.0)
    scg = colorGreen

    colorBlue = FloatField(default_value=1.0)
    scb = colorBlue


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorRed = FloatField(default_value=1.0)
    scr = colorRed

    colorGreen = FloatField(default_value=1.0)
    scg = colorGreen

    colorBlue = FloatField(default_value=1.0)
    scb = colorBlue
