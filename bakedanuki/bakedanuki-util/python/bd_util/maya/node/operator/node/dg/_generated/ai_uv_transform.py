# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_uv_transform import (
    CoverageField,
    NoiseField,
    OffsetField,
    OutColorField,
    OutTransparencyField,
    PassthroughField,
    PivotField,
    PivotFrameField,
    RepeatField,
    ScaleFrameField,
    TranslateFrameField,
    UvcoordsField,
    WrapFrameColorField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class UnitEnumPlugOperator(EnumPlugOperator["UnitEnumAttrOperator"]):
    __slots__ = ()

    RADIANS = 0
    DEGREES = 1
    NORMALIZED = 2


class UnitEnumAttrOperator(EnumAttrOperator[UnitEnumPlugOperator]):
    __slots__ = ()

    RADIANS = 0
    DEGREES = 1
    NORMALIZED = 2

    NAME_MAP = {
        RADIANS: "radians",
        DEGREES: "degrees",
        NORMALIZED: "normalized",
    }


class UnitEnumField(
    EnumField[UnitEnumAttrOperator, UnitEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UnitEnumAttrOperator
    PLUG_CLS = UnitEnumPlugOperator


class WrapFrameUEnumPlugOperator(EnumPlugOperator["WrapFrameUEnumAttrOperator"]):
    __slots__ = ()

    PERIODIC = 0
    COLOR = 1
    CLAMP = 2
    MIRROR = 3
    NONE = 4


class WrapFrameUEnumAttrOperator(EnumAttrOperator[WrapFrameUEnumPlugOperator]):
    __slots__ = ()

    PERIODIC = 0
    COLOR = 1
    CLAMP = 2
    MIRROR = 3
    NONE = 4

    NAME_MAP = {
        PERIODIC: "periodic",
        COLOR: "color",
        CLAMP: "clamp",
        MIRROR: "mirror",
        NONE: "none",
    }


class WrapFrameUEnumField(
    EnumField[WrapFrameUEnumAttrOperator, WrapFrameUEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WrapFrameUEnumAttrOperator
    PLUG_CLS = WrapFrameUEnumPlugOperator


class WrapFrameVEnumPlugOperator(EnumPlugOperator["WrapFrameVEnumAttrOperator"]):
    __slots__ = ()

    PERIODIC = 0
    COLOR = 1
    CLAMP = 2
    MIRROR = 3
    NONE = 4


class WrapFrameVEnumAttrOperator(EnumAttrOperator[WrapFrameVEnumPlugOperator]):
    __slots__ = ()

    PERIODIC = 0
    COLOR = 1
    CLAMP = 2
    MIRROR = 3
    NONE = 4

    NAME_MAP = {
        PERIODIC: "periodic",
        COLOR: "color",
        CLAMP: "clamp",
        MIRROR: "mirror",
        NONE: "none",
    }


class WrapFrameVEnumField(
    EnumField[WrapFrameVEnumAttrOperator, WrapFrameVEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WrapFrameVEnumAttrOperator
    PLUG_CLS = WrapFrameVEnumPlugOperator


class GeneratedAiUvTransform(DG):
    __slots__ = ()

    NODE_TYPE = "aiUvTransform"

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

    passthroughA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    passthrougha = passthroughA

    passthrough = PassthroughField(default_value=(0.0, 0.0, 0.0))
    passthroughR = passthrough.passthroughR
    passthroughr = passthroughR
    passthroughG = passthrough.passthroughG
    passthroughg = passthroughG
    passthroughB = passthrough.passthroughB
    passthroughb = passthroughB

    unit = UnitEnumField(default_value=1)

    uvcoords = UvcoordsField(default_value=(0.0, 0.0, 0.0))
    uvcoordsX = uvcoords.uvcoordsX
    uvcoordsx = uvcoordsX
    uvcoordsY = uvcoords.uvcoordsY
    uvcoordsy = uvcoordsY
    uvcoordsZ = uvcoords.uvcoordsZ
    uvcoordsz = uvcoordsZ

    uvset = DataStringField()

    coverage = CoverageField(default_value=(1.0, 1.0))
    coverageX = coverage.coverageX
    coveragex = coverageX
    coverageY = coverage.coverageY
    coveragey = coverageY

    scaleFrame = ScaleFrameField(default_value=(1.0, 1.0))
    scale_frame = scaleFrame
    scaleFrameX = scaleFrame.scaleFrameX
    scale_framex = scaleFrameX
    scaleFrameY = scaleFrame.scaleFrameY
    scale_framey = scaleFrameY

    translateFrame = TranslateFrameField(default_value=(0.0, 0.0))
    translate_frame = translateFrame
    translateFrameX = translateFrame.translateFrameX
    translate_framex = translateFrameX
    translateFrameY = translateFrame.translateFrameY
    translate_framey = translateFrameY

    rotateFrame = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=360.0)
    rotate_frame = rotateFrame

    pivotFrame = PivotFrameField(default_value=(0.5, 0.5))
    pivot_frame = pivotFrame
    pivotFrameX = pivotFrame.pivotFrameX
    pivot_framex = pivotFrameX
    pivotFrameY = pivotFrame.pivotFrameY
    pivot_framey = pivotFrameY

    wrapFrameU = WrapFrameUEnumField(default_value=0)
    wrap_frame_u = wrapFrameU

    wrapFrameV = WrapFrameVEnumField(default_value=0)
    wrap_frame_v = wrapFrameV

    wrapFrameColorA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    wrap_frame_colora = wrapFrameColorA

    wrapFrameColor = WrapFrameColorField(default_value=(0.0, 0.0, 0.0))
    wrap_frame_color = wrapFrameColor
    wrapFrameColorR = wrapFrameColor.wrapFrameColorR
    wrap_frame_colorr = wrapFrameColorR
    wrapFrameColorG = wrapFrameColor.wrapFrameColorG
    wrap_frame_colorg = wrapFrameColorG
    wrapFrameColorB = wrapFrameColor.wrapFrameColorB
    wrap_frame_colorb = wrapFrameColorB

    repeat = RepeatField(default_value=(1.0, 1.0))
    repeatX = repeat.repeatX
    repeatx = repeatX
    repeatY = repeat.repeatY
    repeaty = repeatY

    offset = OffsetField(default_value=(0.0, 0.0))
    offsetX = offset.offsetX
    offsetx = offsetX
    offsetY = offset.offsetY
    offsety = offsetY

    rotate = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=360.0)

    pivot = PivotField(default_value=(0.5, 0.5))
    pivotX = pivot.pivotX
    pivotx = pivotX
    pivotY = pivot.pivotY
    pivoty = pivotY

    noise = NoiseField(default_value=(0.0, 0.0))
    noiseX = noise.noiseX
    noisex = noiseX
    noiseY = noise.noiseY
    noisey = noiseY

    mirrorU = BoolField(default_value=False)
    mirror_u = mirrorU

    mirrorV = BoolField(default_value=False)
    mirror_v = mirrorV

    flipU = BoolField(default_value=False)
    flip_u = flipU

    flipV = BoolField(default_value=False)
    flip_v = flipV

    swapUv = BoolField(default_value=False)
    swap_uv = swapUv

    stagger = BoolField(default_value=False)

    wset = DataStringField()

    uvwMatrix = FltMatrixField()
    uvw_matrix = uvwMatrix
