# coding: utf-8
from .._core import DG
from ....attr.define.node_attr_maya2027.ai_line import (
    BackgroundColorField,
    ColorField,
    OffsetField,
    OutColorField,
    Out_line_uvField,
    ShiftPerLayerField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class CoordinateSystemEnumPlugOperator(
    EnumPlugOperator["CoordinateSystemEnumAttrOperator"]
):
    __slots__ = ()

    CARTESIAN = 0
    CONCENTRIC_CIRCLES = 1
    POLAR = 2


class CoordinateSystemEnumAttrOperator(
    EnumAttrOperator[CoordinateSystemEnumPlugOperator]
):
    __slots__ = ()

    CARTESIAN = 0
    CONCENTRIC_CIRCLES = 1
    POLAR = 2

    NAME_MAP = {
        CARTESIAN: "cartesian",
        CONCENTRIC_CIRCLES: "concentric circles",
        POLAR: "polar",
    }


class CoordinateSystemEnumField(
    EnumField[
        CoordinateSystemEnumAttrOperator, CoordinateSystemEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CoordinateSystemEnumAttrOperator
    PLUG_CLS = CoordinateSystemEnumPlugOperator


class DecimateModeEnumPlugOperator(
    EnumPlugOperator["DecimateModeEnumAttrOperator"]
):
    __slots__ = ()

    RANDOM_LINE = 0
    RANDOM_LINE_AMP_LAYER = 1
    RANDOM_SEGMENT = 2
    RANDOM_SEGMENT_AMP_LAYER = 3
    CENTER_PRESERVING = 4
    SEQUENTIAL = 5


class DecimateModeEnumAttrOperator(
    EnumAttrOperator[DecimateModeEnumPlugOperator]
):
    __slots__ = ()

    RANDOM_LINE = 0
    RANDOM_LINE_AMP_LAYER = 1
    RANDOM_SEGMENT = 2
    RANDOM_SEGMENT_AMP_LAYER = 3
    CENTER_PRESERVING = 4
    SEQUENTIAL = 5

    NAME_MAP = {
        RANDOM_LINE: "random (line)",
        RANDOM_LINE_AMP_LAYER: "random (line & layer)",
        RANDOM_SEGMENT: "random (segment)",
        RANDOM_SEGMENT_AMP_LAYER: "random (segment & layer)",
        CENTER_PRESERVING: "center_preserving",
        SEQUENTIAL: "sequential",
    }


class DecimateModeEnumField(
    EnumField[DecimateModeEnumAttrOperator, DecimateModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DecimateModeEnumAttrOperator
    PLUG_CLS = DecimateModeEnumPlugOperator


class SmoothModeEnumPlugOperator(
    EnumPlugOperator["SmoothModeEnumAttrOperator"]
):
    __slots__ = ()

    BOTH_SIDES = 0
    PERIPHERAL = 1


class SmoothModeEnumAttrOperator(EnumAttrOperator[SmoothModeEnumPlugOperator]):
    __slots__ = ()

    BOTH_SIDES = 0
    PERIPHERAL = 1

    NAME_MAP = {
        BOTH_SIDES: "both_sides",
        PERIPHERAL: "peripheral",
    }


class SmoothModeEnumField(
    EnumField[SmoothModeEnumAttrOperator, SmoothModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SmoothModeEnumAttrOperator
    PLUG_CLS = SmoothModeEnumPlugOperator


class IntervalOffsetModeEnumPlugOperator(
    EnumPlugOperator["IntervalOffsetModeEnumAttrOperator"]
):
    __slots__ = ()

    CONSTANT = 0
    INTERLEAVE = 1
    RANDOM_LINE = 2
    RANDOM_SEGMENT = 3


class IntervalOffsetModeEnumAttrOperator(
    EnumAttrOperator[IntervalOffsetModeEnumPlugOperator]
):
    __slots__ = ()

    CONSTANT = 0
    INTERLEAVE = 1
    RANDOM_LINE = 2
    RANDOM_SEGMENT = 3

    NAME_MAP = {
        CONSTANT: "constant",
        INTERLEAVE: "interleave",
        RANDOM_LINE: "random (line)",
        RANDOM_SEGMENT: "random (segment)",
    }


class IntervalOffsetModeEnumField(
    EnumField[
        IntervalOffsetModeEnumAttrOperator, IntervalOffsetModeEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = IntervalOffsetModeEnumAttrOperator
    PLUG_CLS = IntervalOffsetModeEnumPlugOperator


class LineOffsetModeEnumPlugOperator(
    EnumPlugOperator["LineOffsetModeEnumAttrOperator"]
):
    __slots__ = ()

    CONSTANT = 0
    INTERLEAVE = 1
    RANDOM_LINE = 2
    RANDOM_SEGMENT = 3


class LineOffsetModeEnumAttrOperator(
    EnumAttrOperator[LineOffsetModeEnumPlugOperator]
):
    __slots__ = ()

    CONSTANT = 0
    INTERLEAVE = 1
    RANDOM_LINE = 2
    RANDOM_SEGMENT = 3

    NAME_MAP = {
        CONSTANT: "constant",
        INTERLEAVE: "interleave",
        RANDOM_LINE: "random (line)",
        RANDOM_SEGMENT: "random (segment)",
    }


class LineOffsetModeEnumField(
    EnumField[LineOffsetModeEnumAttrOperator, LineOffsetModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LineOffsetModeEnumAttrOperator
    PLUG_CLS = LineOffsetModeEnumPlugOperator


class StyleEnumPlugOperator(EnumPlugOperator["StyleEnumAttrOperator"]):
    __slots__ = ()

    SINE = 0
    TRIANGLE = 1
    HALF_ARC = 2
    QUAD_ARC = 3
    TRAPEZOID = 4


class StyleEnumAttrOperator(EnumAttrOperator[StyleEnumPlugOperator]):
    __slots__ = ()

    SINE = 0
    TRIANGLE = 1
    HALF_ARC = 2
    QUAD_ARC = 3
    TRAPEZOID = 4

    NAME_MAP = {
        SINE: "sine",
        TRIANGLE: "triangle",
        HALF_ARC: "half_arc",
        QUAD_ARC: "quad_arc",
        TRAPEZOID: "trapezoid",
    }


class StyleEnumField(EnumField[StyleEnumAttrOperator, StyleEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = StyleEnumAttrOperator
    PLUG_CLS = StyleEnumPlugOperator


class TipShapeEnumPlugOperator(EnumPlugOperator["TipShapeEnumAttrOperator"]):
    __slots__ = ()

    RECTANGLE = 0
    ELLIPTIC = 1
    TRIANGLE = 2
    CHISEL = 3


class TipShapeEnumAttrOperator(EnumAttrOperator[TipShapeEnumPlugOperator]):
    __slots__ = ()

    RECTANGLE = 0
    ELLIPTIC = 1
    TRIANGLE = 2
    CHISEL = 3

    NAME_MAP = {
        RECTANGLE: "rectangle",
        ELLIPTIC: "elliptic",
        TRIANGLE: "triangle",
        CHISEL: "chisel",
    }


class TipShapeEnumField(
    EnumField[TipShapeEnumAttrOperator, TipShapeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TipShapeEnumAttrOperator
    PLUG_CLS = TipShapeEnumPlugOperator


class BlendModeEnumPlugOperator(EnumPlugOperator["BlendModeEnumAttrOperator"]):
    __slots__ = ()

    ALPHA = 0
    AVERAGE = 1


class BlendModeEnumAttrOperator(EnumAttrOperator[BlendModeEnumPlugOperator]):
    __slots__ = ()

    ALPHA = 0
    AVERAGE = 1

    NAME_MAP = {
        ALPHA: "alpha",
        AVERAGE: "average",
    }


class BlendModeEnumField(
    EnumField[BlendModeEnumAttrOperator, BlendModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlendModeEnumAttrOperator
    PLUG_CLS = BlendModeEnumPlugOperator


class GeneratedAiLine(DG):
    __slots__ = ()

    NODE_TYPE = "aiLine"

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

    out_line_id = LongField(default_value=0, writable=False)

    out_segment_id = LongField(default_value=0, writable=False)

    out_line_uv = Out_line_uvField(default_value=(0.0, 0.0), writable=False)
    out_line_uvX = out_line_uv.out_line_uvX
    out_line_uvx = out_line_uvX
    out_line_uvY = out_line_uv.out_line_uvY
    out_line_uvy = out_line_uvY

    backgroundColorA = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    background_colora = backgroundColorA

    backgroundColor = BackgroundColorField(default_value=(1.0, 1.0, 1.0))
    background_color = backgroundColor
    backgroundColorR = backgroundColor.backgroundColorR
    background_colorr = backgroundColorR
    backgroundColorG = backgroundColor.backgroundColorG
    background_colorg = backgroundColorG
    backgroundColorB = backgroundColor.backgroundColorB
    background_colorb = backgroundColorB

    coordinateSystem = CoordinateSystemEnumField(default_value=0)
    coordinate_system = coordinateSystem

    numLines = LongField(default_value=4, min_value=1, soft_max_value=100)
    num_lines = numLines

    numSegments = LongField(default_value=1, min_value=1, soft_max_value=100)
    num_segments = numSegments

    colorA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    colora = colorA

    color = ColorField(default_value=(0.0, 0.0, 0.0))
    colorR = color.colorR
    colorr = colorR
    colorG = color.colorG
    colorg = colorG
    colorB = color.colorB
    colorb = colorB

    width = FloatField(default_value=0.25, min_value=0.0, max_value=1.0)

    length = FloatField(
        default_value=0.8999999761581421, min_value=0.0, max_value=1.0
    )

    interval = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=0.10000000149011612
    )

    decimateMode = DecimateModeEnumField(default_value=0)
    decimate_mode = decimateMode

    density = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    smoothMode = SmoothModeEnumField(default_value=0)
    smooth_mode = smoothMode

    smoothness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    intervalOffsetMode = IntervalOffsetModeEnumField(default_value=0)
    interval_offset_mode = intervalOffsetMode

    lineOffsetMode = LineOffsetModeEnumField(default_value=0)
    line_offset_mode = lineOffsetMode

    offset = OffsetField(default_value=(0.5, 0.5))
    offsetX = offset.offsetX
    offsetx = offsetX
    offsetY = offset.offsetY
    offsety = offsetY

    style = StyleEnumField(default_value=0)

    amplitude = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )

    frequency = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=10.0
    )

    phase = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    tipShape = TipShapeEnumField(default_value=0)
    tip_shape = tipShape

    tipRatio = FloatField(default_value=0.25, min_value=0.0, max_value=1.0)
    tip_ratio = tipRatio

    tipFade = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    tip_fade = tipFade

    tipBias = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    tip_bias = tipBias

    numLayers = LongField(default_value=1, min_value=1, max_value=16)
    num_layers = numLayers

    blendMode = BlendModeEnumField(default_value=0)
    blend_mode = blendMode

    shiftPerLayer = ShiftPerLayerField(default_value=(0.0, 0.0))
    shift_per_layer = shiftPerLayer
    shiftPerLayerX = shiftPerLayer.shiftPerLayerX
    shift_per_layerx = shiftPerLayerX
    shiftPerLayerY = shiftPerLayer.shiftPerLayerY
    shift_per_layery = shiftPerLayerY

    rotationPerLayer = FloatField(
        default_value=0.25, soft_min_value=0.0, soft_max_value=1.0
    )
    rotation_per_layer = rotationPerLayer

    skipTransform = BoolField(default_value=False)
    skip_transform = skipTransform
