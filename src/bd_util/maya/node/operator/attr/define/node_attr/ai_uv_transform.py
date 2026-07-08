# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "outr"),
        ("outColorG", "outg"),
        ("outColorB", "outb"),
    )

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["OutTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTransparencyR", "otr"),
        ("outTransparencyG", "otg"),
        ("outTransparencyB", "otb"),
    )

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class PassthroughPlugOperator(
    Float3CompoundBasePlugOperator["PassthroughAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("passthroughR", "passthroughr"),
        ("passthroughG", "passthroughg"),
        ("passthroughB", "passthroughb"),
    )

    passthroughR = FloatField(default_value=0.0)
    passthroughr = passthroughR

    passthroughG = FloatField(default_value=0.0)
    passthroughg = passthroughG

    passthroughB = FloatField(default_value=0.0)
    passthroughb = passthroughB


class PassthroughAttrOperator(
    Float3CompoundBaseAttrOperator[PassthroughPlugOperator]
):
    __slots__ = ()

    passthroughR = FloatField(default_value=0.0)
    passthroughr = passthroughR

    passthroughG = FloatField(default_value=0.0)
    passthroughg = passthroughG

    passthroughB = FloatField(default_value=0.0)
    passthroughb = passthroughB


class PassthroughField(
    Float3CompoundBaseField[PassthroughAttrOperator, PassthroughPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PassthroughAttrOperator
    PLUG_CLS = PassthroughPlugOperator

    passthroughR = FloatField(default_value=0.0)
    passthroughr = passthroughR

    passthroughG = FloatField(default_value=0.0)
    passthroughg = passthroughG

    passthroughB = FloatField(default_value=0.0)
    passthroughb = passthroughB


class UvcoordsPlugOperator(
    Float3CompoundBasePlugOperator["UvcoordsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvcoordsX", "uvcoordsx"),
        ("uvcoordsY", "uvcoordsy"),
        ("uvcoordsZ", "uvcoordsz"),
    )

    uvcoordsX = FloatField(default_value=0.0)
    uvcoordsx = uvcoordsX

    uvcoordsY = FloatField(default_value=0.0)
    uvcoordsy = uvcoordsY

    uvcoordsZ = FloatField(default_value=0.0)
    uvcoordsz = uvcoordsZ


class UvcoordsAttrOperator(
    Float3CompoundBaseAttrOperator[UvcoordsPlugOperator]
):
    __slots__ = ()

    uvcoordsX = FloatField(default_value=0.0)
    uvcoordsx = uvcoordsX

    uvcoordsY = FloatField(default_value=0.0)
    uvcoordsy = uvcoordsY

    uvcoordsZ = FloatField(default_value=0.0)
    uvcoordsz = uvcoordsZ


class UvcoordsField(
    Float3CompoundBaseField[UvcoordsAttrOperator, UvcoordsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvcoordsAttrOperator
    PLUG_CLS = UvcoordsPlugOperator

    uvcoordsX = FloatField(default_value=0.0)
    uvcoordsx = uvcoordsX

    uvcoordsY = FloatField(default_value=0.0)
    uvcoordsy = uvcoordsY

    uvcoordsZ = FloatField(default_value=0.0)
    uvcoordsz = uvcoordsZ


class CoveragePlugOperator(
    Float2CompoundBasePlugOperator["CoverageAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("coverageX", "coveragex"),
        ("coverageY", "coveragey"),
    )

    coverageX = FloatField(default_value=1.0)
    coveragex = coverageX

    coverageY = FloatField(default_value=1.0)
    coveragey = coverageY


class CoverageAttrOperator(
    Float2CompoundBaseAttrOperator[CoveragePlugOperator]
):
    __slots__ = ()

    coverageX = FloatField(default_value=1.0)
    coveragex = coverageX

    coverageY = FloatField(default_value=1.0)
    coveragey = coverageY


class CoverageField(
    Float2CompoundBaseField[CoverageAttrOperator, CoveragePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoverageAttrOperator
    PLUG_CLS = CoveragePlugOperator

    coverageX = FloatField(default_value=1.0)
    coveragex = coverageX

    coverageY = FloatField(default_value=1.0)
    coveragey = coverageY


class ScaleFramePlugOperator(
    Float2CompoundBasePlugOperator["ScaleFrameAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleFrameX", "scale_framex"),
        ("scaleFrameY", "scale_framey"),
    )

    scaleFrameX = FloatField(default_value=1.0)
    scale_framex = scaleFrameX

    scaleFrameY = FloatField(default_value=1.0)
    scale_framey = scaleFrameY


class ScaleFrameAttrOperator(
    Float2CompoundBaseAttrOperator[ScaleFramePlugOperator]
):
    __slots__ = ()

    scaleFrameX = FloatField(default_value=1.0)
    scale_framex = scaleFrameX

    scaleFrameY = FloatField(default_value=1.0)
    scale_framey = scaleFrameY


class ScaleFrameField(
    Float2CompoundBaseField[ScaleFrameAttrOperator, ScaleFramePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleFrameAttrOperator
    PLUG_CLS = ScaleFramePlugOperator

    scaleFrameX = FloatField(default_value=1.0)
    scale_framex = scaleFrameX

    scaleFrameY = FloatField(default_value=1.0)
    scale_framey = scaleFrameY


class TranslateFramePlugOperator(
    Float2CompoundBasePlugOperator["TranslateFrameAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("translateFrameX", "translate_framex"),
        ("translateFrameY", "translate_framey"),
    )

    translateFrameX = FloatField(default_value=0.0)
    translate_framex = translateFrameX

    translateFrameY = FloatField(default_value=0.0)
    translate_framey = translateFrameY


class TranslateFrameAttrOperator(
    Float2CompoundBaseAttrOperator[TranslateFramePlugOperator]
):
    __slots__ = ()

    translateFrameX = FloatField(default_value=0.0)
    translate_framex = translateFrameX

    translateFrameY = FloatField(default_value=0.0)
    translate_framey = translateFrameY


class TranslateFrameField(
    Float2CompoundBaseField[TranslateFrameAttrOperator, TranslateFramePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateFrameAttrOperator
    PLUG_CLS = TranslateFramePlugOperator

    translateFrameX = FloatField(default_value=0.0)
    translate_framex = translateFrameX

    translateFrameY = FloatField(default_value=0.0)
    translate_framey = translateFrameY


class PivotFramePlugOperator(
    Float2CompoundBasePlugOperator["PivotFrameAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pivotFrameX", "pivot_framex"),
        ("pivotFrameY", "pivot_framey"),
    )

    pivotFrameX = FloatField(default_value=0.5)
    pivot_framex = pivotFrameX

    pivotFrameY = FloatField(default_value=0.5)
    pivot_framey = pivotFrameY


class PivotFrameAttrOperator(
    Float2CompoundBaseAttrOperator[PivotFramePlugOperator]
):
    __slots__ = ()

    pivotFrameX = FloatField(default_value=0.5)
    pivot_framex = pivotFrameX

    pivotFrameY = FloatField(default_value=0.5)
    pivot_framey = pivotFrameY


class PivotFrameField(
    Float2CompoundBaseField[PivotFrameAttrOperator, PivotFramePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PivotFrameAttrOperator
    PLUG_CLS = PivotFramePlugOperator

    pivotFrameX = FloatField(default_value=0.5)
    pivot_framex = pivotFrameX

    pivotFrameY = FloatField(default_value=0.5)
    pivot_framey = pivotFrameY


class WrapFrameColorPlugOperator(
    Float3CompoundBasePlugOperator["WrapFrameColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("wrapFrameColorR", "wrap_frame_colorr"),
        ("wrapFrameColorG", "wrap_frame_colorg"),
        ("wrapFrameColorB", "wrap_frame_colorb"),
    )

    wrapFrameColorR = FloatField(default_value=0.0)
    wrap_frame_colorr = wrapFrameColorR

    wrapFrameColorG = FloatField(default_value=0.0)
    wrap_frame_colorg = wrapFrameColorG

    wrapFrameColorB = FloatField(default_value=0.0)
    wrap_frame_colorb = wrapFrameColorB


class WrapFrameColorAttrOperator(
    Float3CompoundBaseAttrOperator[WrapFrameColorPlugOperator]
):
    __slots__ = ()

    wrapFrameColorR = FloatField(default_value=0.0)
    wrap_frame_colorr = wrapFrameColorR

    wrapFrameColorG = FloatField(default_value=0.0)
    wrap_frame_colorg = wrapFrameColorG

    wrapFrameColorB = FloatField(default_value=0.0)
    wrap_frame_colorb = wrapFrameColorB


class WrapFrameColorField(
    Float3CompoundBaseField[WrapFrameColorAttrOperator, WrapFrameColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WrapFrameColorAttrOperator
    PLUG_CLS = WrapFrameColorPlugOperator

    wrapFrameColorR = FloatField(default_value=0.0)
    wrap_frame_colorr = wrapFrameColorR

    wrapFrameColorG = FloatField(default_value=0.0)
    wrap_frame_colorg = wrapFrameColorG

    wrapFrameColorB = FloatField(default_value=0.0)
    wrap_frame_colorb = wrapFrameColorB


class RepeatPlugOperator(
    Float2CompoundBasePlugOperator["RepeatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("repeatX", "repeatx"),
        ("repeatY", "repeaty"),
    )

    repeatX = FloatField(default_value=1.0)
    repeatx = repeatX

    repeatY = FloatField(default_value=1.0)
    repeaty = repeatY


class RepeatAttrOperator(
    Float2CompoundBaseAttrOperator[RepeatPlugOperator]
):
    __slots__ = ()

    repeatX = FloatField(default_value=1.0)
    repeatx = repeatX

    repeatY = FloatField(default_value=1.0)
    repeaty = repeatY


class RepeatField(
    Float2CompoundBaseField[RepeatAttrOperator, RepeatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RepeatAttrOperator
    PLUG_CLS = RepeatPlugOperator

    repeatX = FloatField(default_value=1.0)
    repeatx = repeatX

    repeatY = FloatField(default_value=1.0)
    repeaty = repeatY


class OffsetPlugOperator(
    Float2CompoundBasePlugOperator["OffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetX", "offsetx"),
        ("offsetY", "offsety"),
    )

    offsetX = FloatField(default_value=0.0)
    offsetx = offsetX

    offsetY = FloatField(default_value=0.0)
    offsety = offsetY


class OffsetAttrOperator(
    Float2CompoundBaseAttrOperator[OffsetPlugOperator]
):
    __slots__ = ()

    offsetX = FloatField(default_value=0.0)
    offsetx = offsetX

    offsetY = FloatField(default_value=0.0)
    offsety = offsetY


class OffsetField(
    Float2CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetX = FloatField(default_value=0.0)
    offsetx = offsetX

    offsetY = FloatField(default_value=0.0)
    offsety = offsetY


class PivotPlugOperator(
    Float2CompoundBasePlugOperator["PivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pivotX", "pivotx"),
        ("pivotY", "pivoty"),
    )

    pivotX = FloatField(default_value=0.5)
    pivotx = pivotX

    pivotY = FloatField(default_value=0.5)
    pivoty = pivotY


class PivotAttrOperator(
    Float2CompoundBaseAttrOperator[PivotPlugOperator]
):
    __slots__ = ()

    pivotX = FloatField(default_value=0.5)
    pivotx = pivotX

    pivotY = FloatField(default_value=0.5)
    pivoty = pivotY


class PivotField(
    Float2CompoundBaseField[PivotAttrOperator, PivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PivotAttrOperator
    PLUG_CLS = PivotPlugOperator

    pivotX = FloatField(default_value=0.5)
    pivotx = pivotX

    pivotY = FloatField(default_value=0.5)
    pivoty = pivotY


class NoisePlugOperator(
    Float2CompoundBasePlugOperator["NoiseAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("noiseX", "noisex"),
        ("noiseY", "noisey"),
    )

    noiseX = FloatField(default_value=0.0)
    noisex = noiseX

    noiseY = FloatField(default_value=0.0)
    noisey = noiseY


class NoiseAttrOperator(
    Float2CompoundBaseAttrOperator[NoisePlugOperator]
):
    __slots__ = ()

    noiseX = FloatField(default_value=0.0)
    noisex = noiseX

    noiseY = FloatField(default_value=0.0)
    noisey = noiseY


class NoiseField(
    Float2CompoundBaseField[NoiseAttrOperator, NoisePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NoiseAttrOperator
    PLUG_CLS = NoisePlugOperator

    noiseX = FloatField(default_value=0.0)
    noisex = noiseX

    noiseY = FloatField(default_value=0.0)
    noisey = noiseY
