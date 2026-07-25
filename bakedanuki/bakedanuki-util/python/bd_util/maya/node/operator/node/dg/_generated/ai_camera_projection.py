# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_camera_projection import (
    OffscreenColorField,
    OutColorField,
    OutTransparencyField,
    PField,
    ProjectionColorField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


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


class _GeneratedAiCameraProjection(DG):
    __slots__ = ()

    NODE_TYPE = "aiCameraProjection"

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

    offscreenColorA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    offscreen_colora = offscreenColorA

    offscreenColor = OffscreenColorField(default_value=(0.0, 0.0, 0.0))
    offscreen_color = offscreenColor
    offscreenColorR = offscreenColor.offscreenColorR
    offscreen_colorr = offscreenColorR
    offscreenColorG = offscreenColor.offscreenColorG
    offscreen_colorg = offscreenColorG
    offscreenColorB = offscreenColor.offscreenColorB
    offscreen_colorb = offscreenColorB

    mask = FloatField(default_value=1.0, min_value=0.0, max_value=1.0, soft_max_value=1.0)

    camera = MessageField()

    aspectRatio = FloatField(default_value=1.3329999446868896, min_value=9.999999747378752e-05, soft_max_value=3.0)
    aspect_ratio = aspectRatio

    frontFacing = BoolField(default_value=True)
    front_facing = frontFacing

    backFacing = BoolField(default_value=True)
    back_facing = backFacing

    useShadingNormal = BoolField(default_value=False)
    use_shading_normal = useShadingNormal

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
