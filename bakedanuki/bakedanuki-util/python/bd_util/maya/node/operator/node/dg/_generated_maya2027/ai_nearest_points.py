# coding: utf-8
from .._core import DG
from ....attr.define.node_attr_maya2027.ai_nearest_points import (
    OutColorField,
    Out_rgbField,
    Out_vec2Field,
    Out_vecField,
    PositionField,
    QueryPositionField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)
from ....attr.define.std.dt.string import DataStringField


class PointcloudModeEnumPlugOperator(
    EnumPlugOperator["PointcloudModeEnumAttrOperator"]
):
    __slots__ = ()

    FILE = 0
    NODE = 1


class PointcloudModeEnumAttrOperator(
    EnumAttrOperator[PointcloudModeEnumPlugOperator]
):
    __slots__ = ()

    FILE = 0
    NODE = 1

    NAME_MAP = {
        FILE: "file",
        NODE: "node",
    }


class PointcloudModeEnumField(
    EnumField[PointcloudModeEnumAttrOperator, PointcloudModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointcloudModeEnumAttrOperator
    PLUG_CLS = PointcloudModeEnumPlugOperator


class GeneratedAiNearestPoints(DG):
    __slots__ = ()

    NODE_TYPE = "aiNearestPoints"

    count = LongField(default_value=0, writable=False)

    distance = FloatField(default_value=0.0, writable=False)

    position = PositionField(default_value=(0.0, 0.0, 0.0), writable=False)
    positionX = position.positionX
    positionx = positionX
    positionY = position.positionY
    positiony = positionY
    positionZ = position.positionZ
    positionz = positionZ

    out_float = FloatField(default_value=0.0, writable=False)

    out_rgb = Out_rgbField(default_value=(0.0, 0.0, 0.0), writable=False)
    out_rgbR = out_rgb.out_rgbR
    out_rgbr = out_rgbR
    out_rgbG = out_rgb.out_rgbG
    out_rgbg = out_rgbG
    out_rgbB = out_rgb.out_rgbB
    out_rgbb = out_rgbB

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

    out_vec = Out_vecField(default_value=(0.0, 0.0, 0.0), writable=False)
    out_vecX = out_vec.out_vecX
    out_vecx = out_vecX
    out_vecY = out_vec.out_vecY
    out_vecy = out_vecY
    out_vecZ = out_vec.out_vecZ
    out_vecz = out_vecZ

    out_vec2 = Out_vec2Field(default_value=(0.0, 0.0), writable=False)
    out_vec2X = out_vec2.out_vec2X
    out_vec2x = out_vec2X
    out_vec2Y = out_vec2.out_vec2Y
    out_vec2y = out_vec2Y

    maxPoints = LongField(default_value=1)
    max_points = maxPoints

    searchRadius = DoubleLinearField(default_value=1.0, min_value=0.0)
    search_radius = searchRadius

    pointcloudMode = PointcloudModeEnumField(default_value=0)
    pointcloud_mode = pointcloudMode

    pointcloudFile = DataStringField()
    pointcloud_file = pointcloudFile

    pointcloudGrid = DataStringField()
    pointcloud_grid = pointcloudGrid

    pointcloudNode = MessageField()
    pointcloud_node = pointcloudNode

    queryPosition = QueryPositionField(default_value=(0.0, 0.0, 0.0))
    query_position = queryPosition
    queryPositionX = queryPosition.queryPositionX
    query_positionx = queryPositionX
    queryPositionY = queryPosition.queryPositionY
    query_positiony = queryPositionY
    queryPositionZ = queryPosition.queryPositionZ
    query_positionz = queryPositionZ

    outputAttribute = DataStringField()
    output_attribute = outputAttribute

    averageByMax = BoolField(default_value=False)
    average_by_max = averageByMax

    normalizeDistance = BoolField(default_value=False)
    normalize_distance = normalizeDistance

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    frame = LongField(default_value=0, category="arnold")

    useFrameExtension = BoolField(default_value=False, category="arnold")
