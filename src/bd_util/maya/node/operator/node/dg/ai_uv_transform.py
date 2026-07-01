# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_uv_transform import (
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
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class UnitEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RADIANS = 0
    DEGREES = 1
    NORMALIZED = 2


class UnitEnumAttrOperator(EnumAttrOperator):
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


class WrapFrameUEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PERIODIC = 0
    COLOR = 1
    CLAMP = 2
    MIRROR = 3
    NONE = 4


class WrapFrameUEnumAttrOperator(EnumAttrOperator):
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


class WrapFrameVEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PERIODIC = 0
    COLOR = 1
    CLAMP = 2
    MIRROR = 3
    NONE = 4


class WrapFrameVEnumAttrOperator(EnumAttrOperator):
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


class AiUvTransform(DG):
    __slots__ = ()

    NODE_TYPE = "aiUvTransform"

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

    passthroughA = FloatField()
    passthrougha = passthroughA

    passthrough = PassthroughField()
    passthroughR = passthrough.passthroughR
    passthroughr = passthroughR
    passthroughG = passthrough.passthroughG
    passthroughg = passthroughG
    passthroughB = passthrough.passthroughB
    passthroughb = passthroughB

    unit = UnitEnumField()

    uvcoords = UvcoordsField()
    uvcoordsX = uvcoords.uvcoordsX
    uvcoordsx = uvcoordsX
    uvcoordsY = uvcoords.uvcoordsY
    uvcoordsy = uvcoordsY
    uvcoordsZ = uvcoords.uvcoordsZ
    uvcoordsz = uvcoordsZ

    uvset = DataStringField()

    coverage = CoverageField()
    coverageX = coverage.coverageX
    coveragex = coverageX
    coverageY = coverage.coverageY
    coveragey = coverageY

    scaleFrame = ScaleFrameField()
    scale_frame = scaleFrame
    scaleFrameX = scaleFrame.scaleFrameX
    scale_framex = scaleFrameX
    scaleFrameY = scaleFrame.scaleFrameY
    scale_framey = scaleFrameY

    translateFrame = TranslateFrameField()
    translate_frame = translateFrame
    translateFrameX = translateFrame.translateFrameX
    translate_framex = translateFrameX
    translateFrameY = translateFrame.translateFrameY
    translate_framey = translateFrameY

    rotateFrame = FloatField()
    rotate_frame = rotateFrame

    pivotFrame = PivotFrameField()
    pivot_frame = pivotFrame
    pivotFrameX = pivotFrame.pivotFrameX
    pivot_framex = pivotFrameX
    pivotFrameY = pivotFrame.pivotFrameY
    pivot_framey = pivotFrameY

    wrapFrameU = WrapFrameUEnumField()
    wrap_frame_u = wrapFrameU

    wrapFrameV = WrapFrameVEnumField()
    wrap_frame_v = wrapFrameV

    wrapFrameColorA = FloatField()
    wrap_frame_colora = wrapFrameColorA

    wrapFrameColor = WrapFrameColorField()
    wrap_frame_color = wrapFrameColor
    wrapFrameColorR = wrapFrameColor.wrapFrameColorR
    wrap_frame_colorr = wrapFrameColorR
    wrapFrameColorG = wrapFrameColor.wrapFrameColorG
    wrap_frame_colorg = wrapFrameColorG
    wrapFrameColorB = wrapFrameColor.wrapFrameColorB
    wrap_frame_colorb = wrapFrameColorB

    repeat = RepeatField()
    repeatX = repeat.repeatX
    repeatx = repeatX
    repeatY = repeat.repeatY
    repeaty = repeatY

    offset = OffsetField()
    offsetX = offset.offsetX
    offsetx = offsetX
    offsetY = offset.offsetY
    offsety = offsetY

    rotate = FloatField()

    pivot = PivotField()
    pivotX = pivot.pivotX
    pivotx = pivotX
    pivotY = pivot.pivotY
    pivoty = pivotY

    noise = NoiseField()
    noiseX = noise.noiseX
    noisex = noiseX
    noiseY = noise.noiseY
    noisey = noiseY

    mirrorU = BoolField()
    mirror_u = mirrorU

    mirrorV = BoolField()
    mirror_v = mirrorV

    flipU = BoolField()
    flip_u = flipU

    flipV = BoolField()
    flip_v = flipV

    swapUv = BoolField()
    swap_uv = swapUv

    stagger = BoolField()

    wset = DataStringField()

    uvwMatrix = FltMatrixField()
    uvw_matrix = uvwMatrix
