# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..custom import (
    Double2CompoundBaseAttrOperator,
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseField,
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)


class PostProjection_filmRollControl_filmRollOrderEnumPlugOperator(
    EnumPlugOperator[
        "PostProjection_filmRollControl_filmRollOrderEnumAttrOperator"
    ]
):
    __slots__ = ()

    ROTATE_MINUS_TRANSLATE = 0
    TRANSLATE_MINUS_ROTATE = 1


class PostProjection_filmRollControl_filmRollOrderEnumAttrOperator(
    EnumAttrOperator[
        PostProjection_filmRollControl_filmRollOrderEnumPlugOperator
    ]
):
    __slots__ = ()

    ROTATE_MINUS_TRANSLATE = 0
    TRANSLATE_MINUS_ROTATE = 1

    NAME_MAP = {
        ROTATE_MINUS_TRANSLATE: "Rotate-Translate",
        TRANSLATE_MINUS_ROTATE: "Translate-Rotate",
    }


class PostProjection_filmRollControl_filmRollOrderEnumField(
    EnumField[
        PostProjection_filmRollControl_filmRollOrderEnumAttrOperator,
        PostProjection_filmRollControl_filmRollOrderEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = PostProjection_filmRollControl_filmRollOrderEnumAttrOperator
    PLUG_CLS = PostProjection_filmRollControl_filmRollOrderEnumPlugOperator


class PostProjection_filmRollControl_filmRollPivotPlugOperator(
    Double2CompoundBasePlugOperator[
        "PostProjection_filmRollControl_filmRollPivotAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("horizontalRollPivot", "hrp"),
        ("verticalRollPivot", "vrp"),
    )

    horizontalRollPivot = DoubleField(default_value=0.0)
    hrp = horizontalRollPivot

    verticalRollPivot = DoubleField(default_value=0.0)
    vrp = verticalRollPivot


class PostProjection_filmRollControl_filmRollPivotAttrOperator(
    Double2CompoundBaseAttrOperator[
        PostProjection_filmRollControl_filmRollPivotPlugOperator
    ]
):
    __slots__ = ()

    horizontalRollPivot = DoubleField(default_value=0.0)
    hrp = horizontalRollPivot

    verticalRollPivot = DoubleField(default_value=0.0)
    vrp = verticalRollPivot


class PostProjection_filmRollControl_filmRollPivotField(
    Double2CompoundBaseField[
        PostProjection_filmRollControl_filmRollPivotAttrOperator,
        PostProjection_filmRollControl_filmRollPivotPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = PostProjection_filmRollControl_filmRollPivotAttrOperator
    PLUG_CLS = PostProjection_filmRollControl_filmRollPivotPlugOperator

    horizontalRollPivot = DoubleField(default_value=0.0)
    hrp = horizontalRollPivot

    verticalRollPivot = DoubleField(default_value=0.0)
    vrp = verticalRollPivot


class PostProjection_filmTranslatePlugOperator(
    Double2CompoundBasePlugOperator["PostProjection_filmTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("filmTranslateH", "fth"),
        ("filmTranslateV", "ftv"),
    )

    filmTranslateH = DoubleField(default_value=0.0)
    fth = filmTranslateH

    filmTranslateV = DoubleField(default_value=0.0)
    ftv = filmTranslateV


class PostProjection_filmTranslateAttrOperator(
    Double2CompoundBaseAttrOperator[PostProjection_filmTranslatePlugOperator]
):
    __slots__ = ()

    filmTranslateH = DoubleField(default_value=0.0)
    fth = filmTranslateH

    filmTranslateV = DoubleField(default_value=0.0)
    ftv = filmTranslateV


class PostProjection_filmTranslateField(
    Double2CompoundBaseField[
        PostProjection_filmTranslateAttrOperator,
        PostProjection_filmTranslatePlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = PostProjection_filmTranslateAttrOperator
    PLUG_CLS = PostProjection_filmTranslatePlugOperator

    filmTranslateH = DoubleField(default_value=0.0)
    fth = filmTranslateH

    filmTranslateV = DoubleField(default_value=0.0)
    ftv = filmTranslateV


class PostProjection_filmRollControlPlugOperator(
    CompoundPlugOperator["PostProjection_filmRollControlAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("filmRollPivot", "frp"),
        ("filmRollValue", "frv"),
        ("filmRollOrder", "fro"),
    )

    filmRollPivot = PostProjection_filmRollControl_filmRollPivotField(
        default_value=(0.0, 0.0)
    )
    frp = filmRollPivot

    filmRollValue = DoubleAngleField(default_value=0.0)
    frv = filmRollValue

    filmRollOrder = PostProjection_filmRollControl_filmRollOrderEnumField(
        default_value=0
    )
    fro = filmRollOrder


class PostProjection_filmRollControlAttrOperator(
    CompoundAttrOperator[PostProjection_filmRollControlPlugOperator]
):
    __slots__ = ()

    filmRollPivot = PostProjection_filmRollControl_filmRollPivotField(
        default_value=(0.0, 0.0)
    )
    frp = filmRollPivot

    filmRollValue = DoubleAngleField(default_value=0.0)
    frv = filmRollValue

    filmRollOrder = PostProjection_filmRollControl_filmRollOrderEnumField(
        default_value=0
    )
    fro = filmRollOrder


class PostProjection_filmRollControlField(
    CompoundField[
        PostProjection_filmRollControlAttrOperator,
        PostProjection_filmRollControlPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = PostProjection_filmRollControlAttrOperator
    PLUG_CLS = PostProjection_filmRollControlPlugOperator

    filmRollPivot = PostProjection_filmRollControl_filmRollPivotField(
        default_value=(0.0, 0.0)
    )
    frp = filmRollPivot

    filmRollValue = DoubleAngleField(default_value=0.0)
    frv = filmRollValue

    filmRollOrder = PostProjection_filmRollControl_filmRollOrderEnumField(
        default_value=0
    )
    fro = filmRollOrder


class CameraAperturePlugOperator(
    Double2CompoundBasePlugOperator["CameraApertureAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("horizontalFilmAperture", "hfa"),
        ("verticalFilmAperture", "vfa"),
    )

    horizontalFilmAperture = DoubleField(
        default_value=1.4173200000000001,
        min_value=3.9370000000000004e-05,
        max_value=1200.0,
        soft_min_value=0.1,
        soft_max_value=10.0,
    )
    hfa = horizontalFilmAperture

    verticalFilmAperture = DoubleField(
        default_value=0.94488,
        min_value=3.9370000000000004e-05,
        max_value=1200.0,
        soft_min_value=0.1,
        soft_max_value=10.0,
    )
    vfa = verticalFilmAperture


class CameraApertureAttrOperator(
    Double2CompoundBaseAttrOperator[CameraAperturePlugOperator]
):
    __slots__ = ()

    horizontalFilmAperture = DoubleField(
        default_value=1.4173200000000001,
        min_value=3.9370000000000004e-05,
        max_value=1200.0,
        soft_min_value=0.1,
        soft_max_value=10.0,
    )
    hfa = horizontalFilmAperture

    verticalFilmAperture = DoubleField(
        default_value=0.94488,
        min_value=3.9370000000000004e-05,
        max_value=1200.0,
        soft_min_value=0.1,
        soft_max_value=10.0,
    )
    vfa = verticalFilmAperture


class CameraApertureField(
    Double2CompoundBaseField[
        CameraApertureAttrOperator, CameraAperturePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CameraApertureAttrOperator
    PLUG_CLS = CameraAperturePlugOperator

    horizontalFilmAperture = DoubleField(
        default_value=1.4173200000000001,
        min_value=3.9370000000000004e-05,
        max_value=1200.0,
        soft_min_value=0.1,
        soft_max_value=10.0,
    )
    hfa = horizontalFilmAperture

    verticalFilmAperture = DoubleField(
        default_value=0.94488,
        min_value=3.9370000000000004e-05,
        max_value=1200.0,
        soft_min_value=0.1,
        soft_max_value=10.0,
    )
    vfa = verticalFilmAperture


class FilmOffsetPlugOperator(
    Double2CompoundBasePlugOperator["FilmOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("horizontalFilmOffset", "hfo"),
        ("verticalFilmOffset", "vfo"),
    )

    horizontalFilmOffset = DoubleField(default_value=0.0)
    hfo = horizontalFilmOffset

    verticalFilmOffset = DoubleField(default_value=0.0)
    vfo = verticalFilmOffset


class FilmOffsetAttrOperator(
    Double2CompoundBaseAttrOperator[FilmOffsetPlugOperator]
):
    __slots__ = ()

    horizontalFilmOffset = DoubleField(default_value=0.0)
    hfo = horizontalFilmOffset

    verticalFilmOffset = DoubleField(default_value=0.0)
    vfo = verticalFilmOffset


class FilmOffsetField(
    Double2CompoundBaseField[FilmOffsetAttrOperator, FilmOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FilmOffsetAttrOperator
    PLUG_CLS = FilmOffsetPlugOperator

    horizontalFilmOffset = DoubleField(default_value=0.0)
    hfo = horizontalFilmOffset

    verticalFilmOffset = DoubleField(default_value=0.0)
    vfo = verticalFilmOffset


class ShakePlugOperator(Double2CompoundBasePlugOperator["ShakeAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("horizontalShake", "hs"),
        ("verticalShake", "vs"),
    )

    horizontalShake = DoubleField(default_value=0.0)
    hs = horizontalShake

    verticalShake = DoubleField(default_value=0.0)
    vs = verticalShake


class ShakeAttrOperator(Double2CompoundBaseAttrOperator[ShakePlugOperator]):
    __slots__ = ()

    horizontalShake = DoubleField(default_value=0.0)
    hs = horizontalShake

    verticalShake = DoubleField(default_value=0.0)
    vs = verticalShake


class ShakeField(
    Double2CompoundBaseField[ShakeAttrOperator, ShakePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShakeAttrOperator
    PLUG_CLS = ShakePlugOperator

    horizontalShake = DoubleField(default_value=0.0)
    hs = horizontalShake

    verticalShake = DoubleField(default_value=0.0)
    vs = verticalShake


class PostProjectionPlugOperator(
    CompoundPlugOperator["PostProjectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("preScale", "psc"),
        ("filmTranslate", "ct"),
        ("filmRollControl", "frc"),
        ("postScale", "ptsc"),
    )

    preScale = DoubleField(default_value=1.0, min_value=1e-10)
    psc = preScale

    filmTranslate = PostProjection_filmTranslateField(default_value=(0.0, 0.0))
    ct = filmTranslate

    filmRollControl = PostProjection_filmRollControlField()
    frc = filmRollControl

    postScale = DoubleField(default_value=1.0, min_value=1e-10)
    ptsc = postScale


class PostProjectionAttrOperator(
    CompoundAttrOperator[PostProjectionPlugOperator]
):
    __slots__ = ()

    preScale = DoubleField(default_value=1.0, min_value=1e-10)
    psc = preScale

    filmTranslate = PostProjection_filmTranslateField(default_value=(0.0, 0.0))
    ct = filmTranslate

    filmRollControl = PostProjection_filmRollControlField()
    frc = filmRollControl

    postScale = DoubleField(default_value=1.0, min_value=1e-10)
    ptsc = postScale


class PostProjectionField(
    CompoundField[PostProjectionAttrOperator, PostProjectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PostProjectionAttrOperator
    PLUG_CLS = PostProjectionPlugOperator

    preScale = DoubleField(default_value=1.0, min_value=1e-10)
    psc = preScale

    filmTranslate = PostProjection_filmTranslateField(default_value=(0.0, 0.0))
    ct = filmTranslate

    filmRollControl = PostProjection_filmRollControlField()
    frc = filmRollControl

    postScale = DoubleField(default_value=1.0, min_value=1e-10)
    ptsc = postScale


class PanPlugOperator(Double2CompoundBasePlugOperator["PanAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("horizontalPan", "hpn"),
        ("verticalPan", "vpn"),
    )

    horizontalPan = DoubleField(default_value=0.0)
    hpn = horizontalPan

    verticalPan = DoubleField(default_value=0.0)
    vpn = verticalPan


class PanAttrOperator(Double2CompoundBaseAttrOperator[PanPlugOperator]):
    __slots__ = ()

    horizontalPan = DoubleField(default_value=0.0)
    hpn = horizontalPan

    verticalPan = DoubleField(default_value=0.0)
    vpn = verticalPan


class PanField(Double2CompoundBaseField[PanAttrOperator, PanPlugOperator]):
    __slots__ = ()

    ATTR_CLS = PanAttrOperator
    PLUG_CLS = PanPlugOperator

    horizontalPan = DoubleField(default_value=0.0)
    hpn = horizontalPan

    verticalPan = DoubleField(default_value=0.0)
    vpn = verticalPan


class TumblePivotPlugOperator(
    Double3CompoundBasePlugOperator["TumblePivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tumblePivotX", "tpx"),
        ("tumblePivotY", "tpy"),
        ("tumblePivotZ", "tpz"),
    )

    tumblePivotX = DoubleField(default_value=0.0)
    tpx = tumblePivotX

    tumblePivotY = DoubleField(default_value=0.0)
    tpy = tumblePivotY

    tumblePivotZ = DoubleField(default_value=0.0)
    tpz = tumblePivotZ


class TumblePivotAttrOperator(
    Double3CompoundBaseAttrOperator[TumblePivotPlugOperator]
):
    __slots__ = ()

    tumblePivotX = DoubleField(default_value=0.0)
    tpx = tumblePivotX

    tumblePivotY = DoubleField(default_value=0.0)
    tpy = tumblePivotY

    tumblePivotZ = DoubleField(default_value=0.0)
    tpz = tumblePivotZ


class TumblePivotField(
    Double3CompoundBaseField[TumblePivotAttrOperator, TumblePivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TumblePivotAttrOperator
    PLUG_CLS = TumblePivotPlugOperator

    tumblePivotX = DoubleField(default_value=0.0)
    tpx = tumblePivotX

    tumblePivotY = DoubleField(default_value=0.0)
    tpy = tumblePivotY

    tumblePivotZ = DoubleField(default_value=0.0)
    tpz = tumblePivotZ


class DisplayGateMaskColorPlugOperator(
    Float3CompoundBasePlugOperator["DisplayGateMaskColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("displayGateMaskColorR", "dgcr"),
        ("displayGateMaskColorG", "dgcg"),
        ("displayGateMaskColorB", "dgcb"),
    )

    displayGateMaskColorR = FloatField(default_value=0.5)
    dgcr = displayGateMaskColorR

    displayGateMaskColorG = FloatField(default_value=0.5)
    dgcg = displayGateMaskColorG

    displayGateMaskColorB = FloatField(default_value=0.5)
    dgcb = displayGateMaskColorB


class DisplayGateMaskColorAttrOperator(
    Float3CompoundBaseAttrOperator[DisplayGateMaskColorPlugOperator]
):
    __slots__ = ()

    displayGateMaskColorR = FloatField(default_value=0.5)
    dgcr = displayGateMaskColorR

    displayGateMaskColorG = FloatField(default_value=0.5)
    dgcg = displayGateMaskColorG

    displayGateMaskColorB = FloatField(default_value=0.5)
    dgcb = displayGateMaskColorB


class DisplayGateMaskColorField(
    Float3CompoundBaseField[
        DisplayGateMaskColorAttrOperator, DisplayGateMaskColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DisplayGateMaskColorAttrOperator
    PLUG_CLS = DisplayGateMaskColorPlugOperator

    displayGateMaskColorR = FloatField(default_value=0.5)
    dgcr = displayGateMaskColorR

    displayGateMaskColorG = FloatField(default_value=0.5)
    dgcg = displayGateMaskColorG

    displayGateMaskColorB = FloatField(default_value=0.5)
    dgcb = displayGateMaskColorB


class BackgroundColorPlugOperator(
    Float3CompoundBasePlugOperator["BackgroundColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("backgroundColorR", "colr"),
        ("backgroundColorG", "colg"),
        ("backgroundColorB", "colb"),
    )

    backgroundColorR = FloatField(default_value=0.0)
    colr = backgroundColorR

    backgroundColorG = FloatField(default_value=0.0)
    colg = backgroundColorG

    backgroundColorB = FloatField(default_value=0.0)
    colb = backgroundColorB


class BackgroundColorAttrOperator(
    Float3CompoundBaseAttrOperator[BackgroundColorPlugOperator]
):
    __slots__ = ()

    backgroundColorR = FloatField(default_value=0.0)
    colr = backgroundColorR

    backgroundColorG = FloatField(default_value=0.0)
    colg = backgroundColorG

    backgroundColorB = FloatField(default_value=0.0)
    colb = backgroundColorB


class BackgroundColorField(
    Float3CompoundBaseField[
        BackgroundColorAttrOperator, BackgroundColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = BackgroundColorAttrOperator
    PLUG_CLS = BackgroundColorPlugOperator

    backgroundColorR = FloatField(default_value=0.0)
    colr = backgroundColorR

    backgroundColorG = FloatField(default_value=0.0)
    colg = backgroundColorG

    backgroundColorB = FloatField(default_value=0.0)
    colb = backgroundColorB


class AiPositionPlugOperator(
    Float3CompoundBasePlugOperator["AiPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiPositionX", "ai_positionx"),
        ("aiPositionY", "ai_positiony"),
        ("aiPositionZ", "ai_positionz"),
    )

    aiPositionX = FloatField(default_value=0.0)
    ai_positionx = aiPositionX

    aiPositionY = FloatField(default_value=0.0)
    ai_positiony = aiPositionY

    aiPositionZ = FloatField(default_value=0.0)
    ai_positionz = aiPositionZ


class AiPositionAttrOperator(
    Float3CompoundBaseAttrOperator[AiPositionPlugOperator]
):
    __slots__ = ()

    aiPositionX = FloatField(default_value=0.0)
    ai_positionx = aiPositionX

    aiPositionY = FloatField(default_value=0.0)
    ai_positiony = aiPositionY

    aiPositionZ = FloatField(default_value=0.0)
    ai_positionz = aiPositionZ


class AiPositionField(
    Float3CompoundBaseField[AiPositionAttrOperator, AiPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiPositionAttrOperator
    PLUG_CLS = AiPositionPlugOperator


class AiLookAtPlugOperator(
    Float3CompoundBasePlugOperator["AiLookAtAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiLookAtX", "ai_look_atx"),
        ("aiLookAtY", "ai_look_aty"),
        ("aiLookAtZ", "ai_look_atz"),
    )

    aiLookAtX = FloatField(default_value=0.0)
    ai_look_atx = aiLookAtX

    aiLookAtY = FloatField(default_value=0.0)
    ai_look_aty = aiLookAtY

    aiLookAtZ = FloatField(default_value=-1.0)
    ai_look_atz = aiLookAtZ


class AiLookAtAttrOperator(
    Float3CompoundBaseAttrOperator[AiLookAtPlugOperator]
):
    __slots__ = ()

    aiLookAtX = FloatField(default_value=0.0)
    ai_look_atx = aiLookAtX

    aiLookAtY = FloatField(default_value=0.0)
    ai_look_aty = aiLookAtY

    aiLookAtZ = FloatField(default_value=-1.0)
    ai_look_atz = aiLookAtZ


class AiLookAtField(
    Float3CompoundBaseField[AiLookAtAttrOperator, AiLookAtPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiLookAtAttrOperator
    PLUG_CLS = AiLookAtPlugOperator


class AiUpPlugOperator(Float3CompoundBasePlugOperator["AiUpAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiUpX", "ai_upx"),
        ("aiUpY", "ai_upy"),
        ("aiUpZ", "ai_upz"),
    )

    aiUpX = FloatField(default_value=0.0)
    ai_upx = aiUpX

    aiUpY = FloatField(default_value=1.0)
    ai_upy = aiUpY

    aiUpZ = FloatField(default_value=0.0)
    ai_upz = aiUpZ


class AiUpAttrOperator(Float3CompoundBaseAttrOperator[AiUpPlugOperator]):
    __slots__ = ()

    aiUpX = FloatField(default_value=0.0)
    ai_upx = aiUpX

    aiUpY = FloatField(default_value=1.0)
    ai_upy = aiUpY

    aiUpZ = FloatField(default_value=0.0)
    ai_upz = aiUpZ


class AiUpField(Float3CompoundBaseField[AiUpAttrOperator, AiUpPlugOperator]):
    __slots__ = ()

    ATTR_CLS = AiUpAttrOperator
    PLUG_CLS = AiUpPlugOperator


class AiScreenWindowMinPlugOperator(
    Float2CompoundBasePlugOperator["AiScreenWindowMinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiScreenWindowMinX", "ai_screen_window_minx"),
        ("aiScreenWindowMinY", "ai_screen_window_miny"),
    )

    aiScreenWindowMinX = FloatField(default_value=-1.0)
    ai_screen_window_minx = aiScreenWindowMinX

    aiScreenWindowMinY = FloatField(default_value=-1.0)
    ai_screen_window_miny = aiScreenWindowMinY


class AiScreenWindowMinAttrOperator(
    Float2CompoundBaseAttrOperator[AiScreenWindowMinPlugOperator]
):
    __slots__ = ()

    aiScreenWindowMinX = FloatField(default_value=-1.0)
    ai_screen_window_minx = aiScreenWindowMinX

    aiScreenWindowMinY = FloatField(default_value=-1.0)
    ai_screen_window_miny = aiScreenWindowMinY


class AiScreenWindowMinField(
    Float2CompoundBaseField[
        AiScreenWindowMinAttrOperator, AiScreenWindowMinPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiScreenWindowMinAttrOperator
    PLUG_CLS = AiScreenWindowMinPlugOperator


class AiScreenWindowMaxPlugOperator(
    Float2CompoundBasePlugOperator["AiScreenWindowMaxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiScreenWindowMaxX", "ai_screen_window_maxx"),
        ("aiScreenWindowMaxY", "ai_screen_window_maxy"),
    )

    aiScreenWindowMaxX = FloatField(default_value=1.0)
    ai_screen_window_maxx = aiScreenWindowMaxX

    aiScreenWindowMaxY = FloatField(default_value=1.0)
    ai_screen_window_maxy = aiScreenWindowMaxY


class AiScreenWindowMaxAttrOperator(
    Float2CompoundBaseAttrOperator[AiScreenWindowMaxPlugOperator]
):
    __slots__ = ()

    aiScreenWindowMaxX = FloatField(default_value=1.0)
    ai_screen_window_maxx = aiScreenWindowMaxX

    aiScreenWindowMaxY = FloatField(default_value=1.0)
    ai_screen_window_maxy = aiScreenWindowMaxY


class AiScreenWindowMaxField(
    Float2CompoundBaseField[
        AiScreenWindowMaxAttrOperator, AiScreenWindowMaxPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiScreenWindowMaxAttrOperator
    PLUG_CLS = AiScreenWindowMaxPlugOperator


class AiShutterCurvePlugOperator(
    Float2CompoundBasePlugOperator["AiShutterCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiShutterCurveX", "ai_shutter_curvex"),
        ("aiShutterCurveY", "ai_shutter_curvey"),
    )

    aiShutterCurveX = FloatField(default_value=float("nan"))
    ai_shutter_curvex = aiShutterCurveX

    aiShutterCurveY = FloatField(default_value=8.617985555597625e-43)
    ai_shutter_curvey = aiShutterCurveY


class AiShutterCurveAttrOperator(
    Float2CompoundBaseAttrOperator[AiShutterCurvePlugOperator]
):
    __slots__ = ()

    aiShutterCurveX = FloatField(default_value=float("nan"))
    ai_shutter_curvex = aiShutterCurveX

    aiShutterCurveY = FloatField(default_value=8.617985555597625e-43)
    ai_shutter_curvey = aiShutterCurveY


class AiShutterCurveField(
    Float2CompoundBaseField[
        AiShutterCurveAttrOperator, AiShutterCurvePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiShutterCurveAttrOperator
    PLUG_CLS = AiShutterCurvePlugOperator


class AiRayOriginPlugOperator(
    Float3CompoundBasePlugOperator["AiRayOriginAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiRayOriginX", "ai_ray_originx"),
        ("aiRayOriginY", "ai_ray_originy"),
        ("aiRayOriginZ", "ai_ray_originz"),
    )

    aiRayOriginX = FloatField(default_value=0.0)
    ai_ray_originx = aiRayOriginX

    aiRayOriginY = FloatField(default_value=0.0)
    ai_ray_originy = aiRayOriginY

    aiRayOriginZ = FloatField(default_value=0.0)
    ai_ray_originz = aiRayOriginZ


class AiRayOriginAttrOperator(
    Float3CompoundBaseAttrOperator[AiRayOriginPlugOperator]
):
    __slots__ = ()

    aiRayOriginX = FloatField(default_value=0.0)
    ai_ray_originx = aiRayOriginX

    aiRayOriginY = FloatField(default_value=0.0)
    ai_ray_originy = aiRayOriginY

    aiRayOriginZ = FloatField(default_value=0.0)
    ai_ray_originz = aiRayOriginZ


class AiRayOriginField(
    Float3CompoundBaseField[AiRayOriginAttrOperator, AiRayOriginPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiRayOriginAttrOperator
    PLUG_CLS = AiRayOriginPlugOperator

    aiRayOriginX = FloatField(default_value=0.0)
    ai_ray_originx = aiRayOriginX

    aiRayOriginY = FloatField(default_value=0.0)
    ai_ray_originy = aiRayOriginY

    aiRayOriginZ = FloatField(default_value=0.0)
    ai_ray_originz = aiRayOriginZ


class AiRayDirectionPlugOperator(
    Float3CompoundBasePlugOperator["AiRayDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiRayDirectionX", "ai_ray_directionx"),
        ("aiRayDirectionY", "ai_ray_directiony"),
        ("aiRayDirectionZ", "ai_ray_directionz"),
    )

    aiRayDirectionX = FloatField(default_value=0.0)
    ai_ray_directionx = aiRayDirectionX

    aiRayDirectionY = FloatField(default_value=0.0)
    ai_ray_directiony = aiRayDirectionY

    aiRayDirectionZ = FloatField(default_value=0.0)
    ai_ray_directionz = aiRayDirectionZ


class AiRayDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[AiRayDirectionPlugOperator]
):
    __slots__ = ()

    aiRayDirectionX = FloatField(default_value=0.0)
    ai_ray_directionx = aiRayDirectionX

    aiRayDirectionY = FloatField(default_value=0.0)
    ai_ray_directiony = aiRayDirectionY

    aiRayDirectionZ = FloatField(default_value=0.0)
    ai_ray_directionz = aiRayDirectionZ


class AiRayDirectionField(
    Float3CompoundBaseField[
        AiRayDirectionAttrOperator, AiRayDirectionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiRayDirectionAttrOperator
    PLUG_CLS = AiRayDirectionPlugOperator

    aiRayDirectionX = FloatField(default_value=0.0)
    ai_ray_directionx = aiRayDirectionX

    aiRayDirectionY = FloatField(default_value=0.0)
    ai_ray_directiony = aiRayDirectionY

    aiRayDirectionZ = FloatField(default_value=0.0)
    ai_ray_directionz = aiRayDirectionZ


class AiUvRemapPlugOperator(
    Float3CompoundBasePlugOperator["AiUvRemapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiUvRemapR", "ai_uv_remapr"),
        ("aiUvRemapG", "ai_uv_remapg"),
        ("aiUvRemapB", "ai_uv_remapb"),
    )

    aiUvRemapR = FloatField(default_value=0.0)
    ai_uv_remapr = aiUvRemapR

    aiUvRemapG = FloatField(default_value=0.0)
    ai_uv_remapg = aiUvRemapG

    aiUvRemapB = FloatField(default_value=0.0)
    ai_uv_remapb = aiUvRemapB


class AiUvRemapAttrOperator(
    Float3CompoundBaseAttrOperator[AiUvRemapPlugOperator]
):
    __slots__ = ()

    aiUvRemapR = FloatField(default_value=0.0)
    ai_uv_remapr = aiUvRemapR

    aiUvRemapG = FloatField(default_value=0.0)
    ai_uv_remapg = aiUvRemapG

    aiUvRemapB = FloatField(default_value=0.0)
    ai_uv_remapb = aiUvRemapB


class AiUvRemapField(
    Float3CompoundBaseField[AiUvRemapAttrOperator, AiUvRemapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiUvRemapAttrOperator
    PLUG_CLS = AiUvRemapPlugOperator

    aiUvRemapR = FloatField(default_value=0.0)
    ai_uv_remapr = aiUvRemapR

    aiUvRemapG = FloatField(default_value=0.0)
    ai_uv_remapg = aiUvRemapG

    aiUvRemapB = FloatField(default_value=0.0)
    ai_uv_remapb = aiUvRemapB


class AiLensTiltAnglePlugOperator(
    Float2CompoundBasePlugOperator["AiLensTiltAngleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiLensTiltAngleX", "ai_lens_tilt_anglex"),
        ("aiLensTiltAngleY", "ai_lens_tilt_angley"),
    )

    aiLensTiltAngleX = FloatField(default_value=0.0)
    ai_lens_tilt_anglex = aiLensTiltAngleX

    aiLensTiltAngleY = FloatField(default_value=0.0)
    ai_lens_tilt_angley = aiLensTiltAngleY


class AiLensTiltAngleAttrOperator(
    Float2CompoundBaseAttrOperator[AiLensTiltAnglePlugOperator]
):
    __slots__ = ()

    aiLensTiltAngleX = FloatField(default_value=0.0)
    ai_lens_tilt_anglex = aiLensTiltAngleX

    aiLensTiltAngleY = FloatField(default_value=0.0)
    ai_lens_tilt_angley = aiLensTiltAngleY


class AiLensTiltAngleField(
    Float2CompoundBaseField[
        AiLensTiltAngleAttrOperator, AiLensTiltAnglePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiLensTiltAngleAttrOperator
    PLUG_CLS = AiLensTiltAnglePlugOperator

    aiLensTiltAngleX = FloatField(default_value=0.0)
    ai_lens_tilt_anglex = aiLensTiltAngleX

    aiLensTiltAngleY = FloatField(default_value=0.0)
    ai_lens_tilt_angley = aiLensTiltAngleY


class AiLensShiftPlugOperator(
    Float2CompoundBasePlugOperator["AiLensShiftAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiLensShiftX", "ai_lens_shiftx"),
        ("aiLensShiftY", "ai_lens_shifty"),
    )

    aiLensShiftX = FloatField(default_value=0.0)
    ai_lens_shiftx = aiLensShiftX

    aiLensShiftY = FloatField(default_value=0.0)
    ai_lens_shifty = aiLensShiftY


class AiLensShiftAttrOperator(
    Float2CompoundBaseAttrOperator[AiLensShiftPlugOperator]
):
    __slots__ = ()

    aiLensShiftX = FloatField(default_value=0.0)
    ai_lens_shiftx = aiLensShiftX

    aiLensShiftY = FloatField(default_value=0.0)
    ai_lens_shifty = aiLensShiftY


class AiLensShiftField(
    Float2CompoundBaseField[AiLensShiftAttrOperator, AiLensShiftPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiLensShiftAttrOperator
    PLUG_CLS = AiLensShiftPlugOperator

    aiLensShiftX = FloatField(default_value=0.0)
    ai_lens_shiftx = aiLensShiftX

    aiLensShiftY = FloatField(default_value=0.0)
    ai_lens_shifty = aiLensShiftY
