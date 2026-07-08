# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_uv_projection import (
    DefaultColorField,
    OutColorField,
    OutTransparencyField,
    PField,
    ProjectionColorField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class ProjectionTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PLANAR = 0
    SPHERICAL = 1
    CYLINDRICAL = 2
    BALL = 3
    CUBIC = 4
    SHRINK_WRAP = 5


class ProjectionTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PLANAR = 0
    SPHERICAL = 1
    CYLINDRICAL = 2
    BALL = 3
    CUBIC = 4
    SHRINK_WRAP = 5

    NAME_MAP = {
        PLANAR: "planar",
        SPHERICAL: "spherical",
        CYLINDRICAL: "cylindrical",
        BALL: "ball",
        CUBIC: "cubic",
        SHRINK_WRAP: "shrink_wrap",
    }


class ProjectionTypeEnumField(
    EnumField[ProjectionTypeEnumAttrOperator, ProjectionTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ProjectionTypeEnumAttrOperator
    PLUG_CLS = ProjectionTypeEnumPlugOperator


class CoordSpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 0
    OBJECT = 1
    PREF = 2


class CoordSpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 0
    OBJECT = 1
    PREF = 2

    NAME_MAP = {
        WORLD: "world",
        OBJECT: "object",
        PREF: "Pref",
    }


class CoordSpaceEnumField(
    EnumField[CoordSpaceEnumAttrOperator, CoordSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoordSpaceEnumAttrOperator
    PLUG_CLS = CoordSpaceEnumPlugOperator


class AiUvProjection(DG):
    __slots__ = ()

    NODE_TYPE = "aiUvProjection"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    outa = outAlpha

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    projectionColorA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    projection_colora = projectionColorA

    projectionColor = ProjectionColorField(default_value=(1.0, 1.0, 1.0))
    projection_color = projectionColor
    projectionColorR = projectionColor.projectionColorR
    projection_colorr = projectionColorR
    projectionColorG = projectionColor.projectionColorG
    projection_colorg = projectionColorG
    projectionColorB = projectionColor.projectionColorB
    projection_colorb = projectionColorB

    projectionType = ProjectionTypeEnumField(default_value=0)
    projection_type = projectionType

    coordSpace = CoordSpaceEnumField(default_value=0)
    coord_space = coordSpace

    prefName = DataStringField()
    pref_name = prefName

    P = PField(default_value=(0.0, 0.0, 0.0))
    PX = P.PX
    Px = PX
    PY = P.PY
    Py = PY
    PZ = P.PZ
    Pz = PZ

    uAngle = FloatField(default_value=180.0, soft_min_value=0.0, soft_max_value=360.0)
    u_angle = uAngle

    vAngle = FloatField(default_value=90.0, soft_min_value=0.0, soft_max_value=360.0)
    v_angle = vAngle

    clamp = BoolField(default_value=False)

    defaultColorA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    default_colora = defaultColorA

    defaultColor = DefaultColorField(default_value=(0.0, 0.0, 0.0))
    default_color = defaultColor
    defaultColorR = defaultColor.defaultColorR
    default_colorr = defaultColorR
    defaultColorG = defaultColor.defaultColorG
    default_colorg = defaultColorG
    defaultColorB = defaultColor.defaultColorB
    default_colorb = defaultColorB

    placementMatrix = FltMatrixField()
    matrix = placementMatrix
