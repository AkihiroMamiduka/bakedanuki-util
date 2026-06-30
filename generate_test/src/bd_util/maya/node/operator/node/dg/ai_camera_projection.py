# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_camera_projection import (
    OffscreenColorField,
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
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


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


class AiCameraProjection(DG):
    __slots__ = ()

    NODE_TYPE = "aiCameraProjection"

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

    offscreenColorA = FloatField()
    offscreen_colora = offscreenColorA

    offscreenColor = OffscreenColorField()
    offscreen_color = offscreenColor
    offscreenColorR = offscreenColor.offscreenColorR
    offscreen_colorr = offscreenColorR
    offscreenColorG = offscreenColor.offscreenColorG
    offscreen_colorg = offscreenColorG
    offscreenColorB = offscreenColor.offscreenColorB
    offscreen_colorb = offscreenColorB

    mask = FloatField()

    camera = MessageField()

    aspectRatio = FloatField()
    aspect_ratio = aspectRatio

    frontFacing = BoolField()
    front_facing = frontFacing

    backFacing = BoolField()
    back_facing = backFacing

    useShadingNormal = BoolField()
    use_shading_normal = useShadingNormal

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
