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

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField()
    outa = outAlpha

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    projectionColorA = FloatField()
    projection_colora = projectionColorA

    projectionColor = ProjectionColorField()
    projection_color = projectionColor
    projectionColorR = projectionColor.projectionColorR
    projection_colorr = projectionColorR
    projectionColorG = projectionColor.projectionColorG
    projection_colorg = projectionColorG
    projectionColorB = projectionColor.projectionColorB
    projection_colorb = projectionColorB

    projectionType = ProjectionTypeEnumField()
    projection_type = projectionType

    coordSpace = CoordSpaceEnumField()
    coord_space = coordSpace

    prefName = DataStringField()
    pref_name = prefName

    P = PField()
    PX = P.PX
    Px = PX
    PY = P.PY
    Py = PY
    PZ = P.PZ
    Pz = PZ

    uAngle = FloatField()
    u_angle = uAngle

    vAngle = FloatField()
    v_angle = vAngle

    clamp = BoolField()

    defaultColorA = FloatField()
    default_colora = defaultColorA

    defaultColor = DefaultColorField()
    default_color = defaultColor
    defaultColorR = defaultColor.defaultColorR
    default_colorr = defaultColorR
    defaultColorG = defaultColor.defaultColorG
    default_colorg = defaultColorG
    defaultColorB = defaultColor.defaultColorB
    default_colorb = defaultColorB

    placementMatrix = FltMatrixField()
    matrix = placementMatrix
