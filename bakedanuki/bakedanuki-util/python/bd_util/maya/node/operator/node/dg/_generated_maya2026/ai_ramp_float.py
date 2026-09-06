# coding: utf-8
from .._core import DG
from ....attr.define.node_attr_maya2026.ai_ramp_float import (
    EndField,
    OutTransparencyField,
    RampField,
    StartField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)
from ....attr.define.std.dt.string import DataStringField


class TypeEnumPlugOperator(EnumPlugOperator["TypeEnumAttrOperator"]):
    __slots__ = ()

    CUSTOM = 0
    U = 1
    V = 2
    DIAGONAL = 3
    RADIAL = 4
    CIRCULAR = 5
    BOX = 6
    TIME = 7
    _3D_LINEAR = 8
    _3D_SPHERICAL = 9
    _3D_CYLINDRICAL = 10


class TypeEnumAttrOperator(EnumAttrOperator[TypeEnumPlugOperator]):
    __slots__ = ()

    CUSTOM = 0
    U = 1
    V = 2
    DIAGONAL = 3
    RADIAL = 4
    CIRCULAR = 5
    BOX = 6
    TIME = 7
    _3D_LINEAR = 8
    _3D_SPHERICAL = 9
    _3D_CYLINDRICAL = 10

    NAME_MAP = {
        CUSTOM: "custom",
        U: "u",
        V: "v",
        DIAGONAL: "diagonal",
        RADIAL: "radial",
        CIRCULAR: "circular",
        BOX: "box",
        TIME: "time",
        _3D_LINEAR: "3d_linear",
        _3D_SPHERICAL: "3d_spherical",
        _3D_CYLINDRICAL: "3d_cylindrical",
    }


class TypeEnumField(EnumField[TypeEnumAttrOperator, TypeEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = TypeEnumAttrOperator
    PLUG_CLS = TypeEnumPlugOperator


class WrapEnumPlugOperator(EnumPlugOperator["WrapEnumAttrOperator"]):
    __slots__ = ()

    PERIODIC = 0
    CLAMP = 1
    MIRROR = 2


class WrapEnumAttrOperator(EnumAttrOperator[WrapEnumPlugOperator]):
    __slots__ = ()

    PERIODIC = 0
    CLAMP = 1
    MIRROR = 2

    NAME_MAP = {
        PERIODIC: "periodic",
        CLAMP: "clamp",
        MIRROR: "mirror",
    }


class WrapEnumField(EnumField[WrapEnumAttrOperator, WrapEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = WrapEnumAttrOperator
    PLUG_CLS = WrapEnumPlugOperator


class UseImplicitUvsEnumPlugOperator(
    EnumPlugOperator["UseImplicitUvsEnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    ON = 1
    CURVES_ONLY = 2


class UseImplicitUvsEnumAttrOperator(
    EnumAttrOperator[UseImplicitUvsEnumPlugOperator]
):
    __slots__ = ()

    OFF = 0
    ON = 1
    CURVES_ONLY = 2

    NAME_MAP = {
        OFF: "off",
        ON: "on",
        CURVES_ONLY: "curves_only",
    }


class UseImplicitUvsEnumField(
    EnumField[UseImplicitUvsEnumAttrOperator, UseImplicitUvsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UseImplicitUvsEnumAttrOperator
    PLUG_CLS = UseImplicitUvsEnumPlugOperator


class CoordSpaceEnumPlugOperator(
    EnumPlugOperator["CoordSpaceEnumAttrOperator"]
):
    __slots__ = ()

    WORLD = 0
    OBJECT = 1


class CoordSpaceEnumAttrOperator(EnumAttrOperator[CoordSpaceEnumPlugOperator]):
    __slots__ = ()

    WORLD = 0
    OBJECT = 1

    NAME_MAP = {
        WORLD: "world",
        OBJECT: "object",
    }


class CoordSpaceEnumField(
    EnumField[CoordSpaceEnumAttrOperator, CoordSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoordSpaceEnumAttrOperator
    PLUG_CLS = CoordSpaceEnumPlugOperator


class GeneratedAiRampFloat(DG):
    __slots__ = ()

    NODE_TYPE = "aiRampFloat"

    outValue = FloatField(default_value=0.0, writable=False)
    out = outValue

    outTransparency = OutTransparencyField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    type = TypeEnumField(default_value=2)

    input = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    wrap = WrapEnumField(default_value=1)

    offset = FloatField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )

    offsetScale = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    offset_scale = offsetScale

    uvset = DataStringField()

    useImplicitUvs = UseImplicitUvsEnumField(default_value=0)
    use_implicit_uvs = useImplicitUvs

    wrapUvs = BoolField(default_value=False)
    wrap_uvs = wrapUvs

    start = StartField(default_value=(0.0, 0.0, 0.0))
    startX = start.startX
    startx = startX
    startY = start.startY
    starty = startY
    startZ = start.startZ
    startz = startZ

    end = EndField(default_value=(1.0, 1.0, 1.0))
    endX = end.endX
    endx = endX
    endY = end.endY
    endy = endY
    endZ = end.endZ
    endz = endZ

    radius = DoubleLinearField(default_value=1.0)

    coordSpace = CoordSpaceEnumField(default_value=1)
    coord_space = coordSpace

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    ramp = RampField(
        multi=True, default_value=(0.0, 0.0, 1), category="arnold"
    )
    aiRamp = ramp
