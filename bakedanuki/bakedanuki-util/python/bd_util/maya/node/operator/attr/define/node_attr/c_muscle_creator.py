# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.matrix import MatrixField
from ..std.at.message import MessageField
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.dt.nurbs_curve import DataNurbsCurveField


class MODELEnumPlugOperator(EnumPlugOperator["MODELEnumAttrOperator"]):
    __slots__ = ()

    MINUS = 0


class MODELEnumAttrOperator(EnumAttrOperator[MODELEnumPlugOperator]):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class MODELEnumField(
    EnumField[MODELEnumAttrOperator, MODELEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MODELEnumAttrOperator
    PLUG_CLS = MODELEnumPlugOperator


class UpAxisEnumPlugOperator(EnumPlugOperator["UpAxisEnumAttrOperator"]):
    __slots__ = ()

    X_MINUS_AXIS = 0
    Z_MINUS_AXIS = 1


class UpAxisEnumAttrOperator(EnumAttrOperator[UpAxisEnumPlugOperator]):
    __slots__ = ()

    X_MINUS_AXIS = 0
    Z_MINUS_AXIS = 1

    NAME_MAP = {
        X_MINUS_AXIS: "X-Axis",
        Z_MINUS_AXIS: "Z-Axis",
    }


class UpAxisEnumField(
    EnumField[UpAxisEnumAttrOperator, UpAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UpAxisEnumAttrOperator
    PLUG_CLS = UpAxisEnumPlugOperator


class SQUASH_STRETCHEnumPlugOperator(EnumPlugOperator["SQUASH_STRETCHEnumAttrOperator"]):
    __slots__ = ()

    MINUS = 0


class SQUASH_STRETCHEnumAttrOperator(EnumAttrOperator[SQUASH_STRETCHEnumPlugOperator]):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class SQUASH_STRETCHEnumField(
    EnumField[SQUASH_STRETCHEnumAttrOperator, SQUASH_STRETCHEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SQUASH_STRETCHEnumAttrOperator
    PLUG_CLS = SQUASH_STRETCHEnumPlugOperator


class BasedOnEnumPlugOperator(EnumPlugOperator["BasedOnEnumAttrOperator"]):
    __slots__ = ()

    LENGTH = 0
    POSE = 1
    POSE_OR_LENGTH = 2


class BasedOnEnumAttrOperator(EnumAttrOperator[BasedOnEnumPlugOperator]):
    __slots__ = ()

    LENGTH = 0
    POSE = 1
    POSE_OR_LENGTH = 2

    NAME_MAP = {
        LENGTH: "length",
        POSE: "pose",
        POSE_OR_LENGTH: "pose or length",
    }


class BasedOnEnumField(
    EnumField[BasedOnEnumAttrOperator, BasedOnEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BasedOnEnumAttrOperator
    PLUG_CLS = BasedOnEnumPlugOperator


class InterpModeEnumPlugOperator(EnumPlugOperator["InterpModeEnumAttrOperator"]):
    __slots__ = ()

    LINEAR = 0
    SMOOTH_MINUS_STEP = 1
    ANIMCURVE = 2


class InterpModeEnumAttrOperator(EnumAttrOperator[InterpModeEnumPlugOperator]):
    __slots__ = ()

    LINEAR = 0
    SMOOTH_MINUS_STEP = 1
    ANIMCURVE = 2

    NAME_MAP = {
        LINEAR: "linear",
        SMOOTH_MINUS_STEP: "smooth-step",
        ANIMCURVE: "animCurve",
    }


class InterpModeEnumField(
    EnumField[InterpModeEnumAttrOperator, InterpModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InterpModeEnumAttrOperator
    PLUG_CLS = InterpModeEnumPlugOperator


class PoseUsesEnumPlugOperator(EnumPlugOperator["PoseUsesEnumAttrOperator"]):
    __slots__ = ()

    ANGLE = 0
    POSITION = 1
    ANGLE_AND_POSITION = 2


class PoseUsesEnumAttrOperator(EnumAttrOperator[PoseUsesEnumPlugOperator]):
    __slots__ = ()

    ANGLE = 0
    POSITION = 1
    ANGLE_AND_POSITION = 2

    NAME_MAP = {
        ANGLE: "angle",
        POSITION: "position",
        ANGLE_AND_POSITION: "angle and position",
    }


class PoseUsesEnumField(
    EnumField[PoseUsesEnumAttrOperator, PoseUsesEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PoseUsesEnumAttrOperator
    PLUG_CLS = PoseUsesEnumPlugOperator


class PoseReadAxisEnumPlugOperator(EnumPlugOperator["PoseReadAxisEnumAttrOperator"]):
    __slots__ = ()

    X_MINUS_AXIS = 0
    Y_MINUS_AXIS = 1
    Z_MINUS_AXIS = 2


class PoseReadAxisEnumAttrOperator(EnumAttrOperator[PoseReadAxisEnumPlugOperator]):
    __slots__ = ()

    X_MINUS_AXIS = 0
    Y_MINUS_AXIS = 1
    Z_MINUS_AXIS = 2

    NAME_MAP = {
        X_MINUS_AXIS: "X-Axis",
        Y_MINUS_AXIS: "Y-Axis",
        Z_MINUS_AXIS: "Z-Axis",
    }


class PoseReadAxisEnumField(
    EnumField[PoseReadAxisEnumAttrOperator, PoseReadAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PoseReadAxisEnumAttrOperator
    PLUG_CLS = PoseReadAxisEnumPlugOperator


class JIGGLEEnumPlugOperator(EnumPlugOperator["JIGGLEEnumAttrOperator"]):
    __slots__ = ()

    MINUS = 0


class JIGGLEEnumAttrOperator(EnumAttrOperator[JIGGLEEnumPlugOperator]):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class JIGGLEEnumField(
    EnumField[JIGGLEEnumAttrOperator, JIGGLEEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = JIGGLEEnumAttrOperator
    PLUG_CLS = JIGGLEEnumPlugOperator


class NurbsDataPlugOperator(
    CompoundPlugOperator["NurbsDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("startPointA", "spa"),
        ("startPointB", "spb"),
        ("endPointA", "epa"),
        ("endPointB", "epb"),
        ("startParent", "spm"),
        ("endParent", "epm"),
        ("MODEL", "lblmdl"),
        ("crossSections", "csec"),
        ("sides", "sid"),
        ("tolerance", "tol"),
        ("upAxis", "uax"),
        ("flatCrossSections", "fltcrs"),
        ("showControls", "shcont"),
        ("showRestMovers", "shrsm"),
        ("showSquashMovers", "shsqm"),
        ("showStretchMovers", "shstm"),
        ("SQUASH_STRETCH", "lblsqst"),
        ("basedOn", "sqstbo"),
        ("interpMode", "intmod"),
        ("poseUses", "pous"),
        ("poseReadAxis", "psredax"),
        ("poseUseTwist", "psustw"),
        ("msgAnimCurveSq", "msgacsq"),
        ("animCurveOutputSq", "acoutsq"),
        ("msgAnimCurveSt", "msgacst"),
        ("animCurveOutputSt", "acoutst"),
        ("defWidthStart", "defwidst"),
        ("defWidthEnd", "defwided"),
        ("lenDefault", "lendef"),
        ("lenSquash", "lensq"),
        ("lenStretch", "lenst"),
        ("autoRotate", "arot"),
        ("autoWiden", "awid"),
        ("dampenOnSquash", "dmpsq"),
        ("dampenOnStretch", "dmpst"),
        ("manualSqSt", "msqst"),
        ("linearAutoSquash", "lnatsq"),
        ("linearAutoStretch", "lnatst"),
        ("userScale", "usc"),
        ("gravityStrength", "gravstr"),
        ("gravityJiggle", "gravjig"),
        ("gravityCycle", "gravcyc"),
        ("gravityX", "gravx"),
        ("gravityY", "gravy"),
        ("gravityZ", "gravz"),
        ("JIGGLE", "lbljig"),
        ("resetFrame", "rf"),
    )

    startPointA = MatrixField()
    spa = startPointA

    startPointB = MatrixField()
    spb = startPointB

    endPointA = MatrixField()
    epa = endPointA

    endPointB = MatrixField()
    epb = endPointB

    startParent = MatrixField()
    spm = startParent

    endParent = MatrixField()
    epm = endParent

    MODEL = MODELEnumField(default_value=0)
    lblmdl = MODEL

    crossSections = LongField(default_value=7, min_value=1)
    csec = crossSections

    sides = LongField(default_value=8, min_value=3)
    sid = sides

    tolerance = LongField(default_value=24, min_value=2)
    tol = tolerance

    upAxis = UpAxisEnumField(default_value=0)
    uax = upAxis

    flatCrossSections = BoolField(default_value=False)
    fltcrs = flatCrossSections

    showControls = BoolField(default_value=True)
    shcont = showControls

    showRestMovers = BoolField(default_value=True)
    shrsm = showRestMovers

    showSquashMovers = BoolField(default_value=True)
    shsqm = showSquashMovers

    showStretchMovers = BoolField(default_value=True)
    shstm = showStretchMovers

    SQUASH_STRETCH = SQUASH_STRETCHEnumField(default_value=0)
    lblsqst = SQUASH_STRETCH

    basedOn = BasedOnEnumField(default_value=2)
    sqstbo = basedOn

    interpMode = InterpModeEnumField(default_value=0)
    intmod = interpMode

    poseUses = PoseUsesEnumField(default_value=2)
    pous = poseUses

    poseReadAxis = PoseReadAxisEnumField(default_value=1)
    psredax = poseReadAxis

    poseUseTwist = BoolField(default_value=False)
    psustw = poseUseTwist

    msgAnimCurveSq = MessageField()
    msgacsq = msgAnimCurveSq

    animCurveOutputSq = DoubleField(default_value=1.0)
    acoutsq = animCurveOutputSq

    msgAnimCurveSt = MessageField()
    msgacst = msgAnimCurveSt

    animCurveOutputSt = DoubleField(default_value=1.0)
    acoutst = animCurveOutputSt

    defWidthStart = DoubleField(default_value=1.0, min_value=0.0)
    defwidst = defWidthStart

    defWidthEnd = DoubleField(default_value=1.0, min_value=0.0)
    defwided = defWidthEnd

    lenDefault = DoubleField(default_value=1.0, min_value=0.0)
    lendef = lenDefault

    lenSquash = DoubleField(default_value=0.5, min_value=0.0)
    lensq = lenSquash

    lenStretch = DoubleField(default_value=2.0, min_value=0.0)
    lenst = lenStretch

    autoRotate = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    arot = autoRotate

    autoWiden = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    awid = autoWiden

    dampenOnSquash = DoubleField(default_value=0.75, min_value=0.0, max_value=1.0)
    dmpsq = dampenOnSquash

    dampenOnStretch = DoubleField(default_value=0.75, min_value=0.0, max_value=1.0)
    dmpst = dampenOnStretch

    manualSqSt = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    msqst = manualSqSt

    linearAutoSquash = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    lnatsq = linearAutoSquash

    linearAutoStretch = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    lnatst = linearAutoStretch

    userScale = DoubleField(default_value=1.0)
    usc = userScale

    gravityStrength = DoubleField(default_value=0.0, min_value=0.0)
    gravstr = gravityStrength

    gravityJiggle = DoubleField(default_value=0.0, min_value=0.0)
    gravjig = gravityJiggle

    gravityCycle = DoubleField(default_value=0.0, min_value=0.0)
    gravcyc = gravityCycle

    gravityX = DoubleField(default_value=0.0)
    gravx = gravityX

    gravityY = DoubleField(default_value=-1.0)
    gravy = gravityY

    gravityZ = DoubleField(default_value=0.0)
    gravz = gravityZ

    JIGGLE = JIGGLEEnumField(default_value=0)
    lbljig = JIGGLE

    resetFrame = DoubleField(default_value=0.0, min_value=-1024.0)
    rf = resetFrame


class NurbsDataAttrOperator(
    CompoundAttrOperator[NurbsDataPlugOperator]
):
    __slots__ = ()

    startPointA = MatrixField()
    spa = startPointA

    startPointB = MatrixField()
    spb = startPointB

    endPointA = MatrixField()
    epa = endPointA

    endPointB = MatrixField()
    epb = endPointB

    startParent = MatrixField()
    spm = startParent

    endParent = MatrixField()
    epm = endParent

    MODEL = MODELEnumField(default_value=0)
    lblmdl = MODEL

    crossSections = LongField(default_value=7, min_value=1)
    csec = crossSections

    sides = LongField(default_value=8, min_value=3)
    sid = sides

    tolerance = LongField(default_value=24, min_value=2)
    tol = tolerance

    upAxis = UpAxisEnumField(default_value=0)
    uax = upAxis

    flatCrossSections = BoolField(default_value=False)
    fltcrs = flatCrossSections

    showControls = BoolField(default_value=True)
    shcont = showControls

    showRestMovers = BoolField(default_value=True)
    shrsm = showRestMovers

    showSquashMovers = BoolField(default_value=True)
    shsqm = showSquashMovers

    showStretchMovers = BoolField(default_value=True)
    shstm = showStretchMovers

    SQUASH_STRETCH = SQUASH_STRETCHEnumField(default_value=0)
    lblsqst = SQUASH_STRETCH

    basedOn = BasedOnEnumField(default_value=2)
    sqstbo = basedOn

    interpMode = InterpModeEnumField(default_value=0)
    intmod = interpMode

    poseUses = PoseUsesEnumField(default_value=2)
    pous = poseUses

    poseReadAxis = PoseReadAxisEnumField(default_value=1)
    psredax = poseReadAxis

    poseUseTwist = BoolField(default_value=False)
    psustw = poseUseTwist

    msgAnimCurveSq = MessageField()
    msgacsq = msgAnimCurveSq

    animCurveOutputSq = DoubleField(default_value=1.0)
    acoutsq = animCurveOutputSq

    msgAnimCurveSt = MessageField()
    msgacst = msgAnimCurveSt

    animCurveOutputSt = DoubleField(default_value=1.0)
    acoutst = animCurveOutputSt

    defWidthStart = DoubleField(default_value=1.0, min_value=0.0)
    defwidst = defWidthStart

    defWidthEnd = DoubleField(default_value=1.0, min_value=0.0)
    defwided = defWidthEnd

    lenDefault = DoubleField(default_value=1.0, min_value=0.0)
    lendef = lenDefault

    lenSquash = DoubleField(default_value=0.5, min_value=0.0)
    lensq = lenSquash

    lenStretch = DoubleField(default_value=2.0, min_value=0.0)
    lenst = lenStretch

    autoRotate = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    arot = autoRotate

    autoWiden = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    awid = autoWiden

    dampenOnSquash = DoubleField(default_value=0.75, min_value=0.0, max_value=1.0)
    dmpsq = dampenOnSquash

    dampenOnStretch = DoubleField(default_value=0.75, min_value=0.0, max_value=1.0)
    dmpst = dampenOnStretch

    manualSqSt = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    msqst = manualSqSt

    linearAutoSquash = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    lnatsq = linearAutoSquash

    linearAutoStretch = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    lnatst = linearAutoStretch

    userScale = DoubleField(default_value=1.0)
    usc = userScale

    gravityStrength = DoubleField(default_value=0.0, min_value=0.0)
    gravstr = gravityStrength

    gravityJiggle = DoubleField(default_value=0.0, min_value=0.0)
    gravjig = gravityJiggle

    gravityCycle = DoubleField(default_value=0.0, min_value=0.0)
    gravcyc = gravityCycle

    gravityX = DoubleField(default_value=0.0)
    gravx = gravityX

    gravityY = DoubleField(default_value=-1.0)
    gravy = gravityY

    gravityZ = DoubleField(default_value=0.0)
    gravz = gravityZ

    JIGGLE = JIGGLEEnumField(default_value=0)
    lbljig = JIGGLE

    resetFrame = DoubleField(default_value=0.0, min_value=-1024.0)
    rf = resetFrame


class NurbsDataField(
    CompoundField[NurbsDataAttrOperator, NurbsDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NurbsDataAttrOperator
    PLUG_CLS = NurbsDataPlugOperator

    startPointA = MatrixField()
    spa = startPointA

    startPointB = MatrixField()
    spb = startPointB

    endPointA = MatrixField()
    epa = endPointA

    endPointB = MatrixField()
    epb = endPointB

    startParent = MatrixField()
    spm = startParent

    endParent = MatrixField()
    epm = endParent

    MODEL = MODELEnumField(default_value=0)
    lblmdl = MODEL

    crossSections = LongField(default_value=7, min_value=1)
    csec = crossSections

    sides = LongField(default_value=8, min_value=3)
    sid = sides

    tolerance = LongField(default_value=24, min_value=2)
    tol = tolerance

    upAxis = UpAxisEnumField(default_value=0)
    uax = upAxis

    flatCrossSections = BoolField(default_value=False)
    fltcrs = flatCrossSections

    showControls = BoolField(default_value=True)
    shcont = showControls

    showRestMovers = BoolField(default_value=True)
    shrsm = showRestMovers

    showSquashMovers = BoolField(default_value=True)
    shsqm = showSquashMovers

    showStretchMovers = BoolField(default_value=True)
    shstm = showStretchMovers

    SQUASH_STRETCH = SQUASH_STRETCHEnumField(default_value=0)
    lblsqst = SQUASH_STRETCH

    basedOn = BasedOnEnumField(default_value=2)
    sqstbo = basedOn

    interpMode = InterpModeEnumField(default_value=0)
    intmod = interpMode

    poseUses = PoseUsesEnumField(default_value=2)
    pous = poseUses

    poseReadAxis = PoseReadAxisEnumField(default_value=1)
    psredax = poseReadAxis

    poseUseTwist = BoolField(default_value=False)
    psustw = poseUseTwist

    msgAnimCurveSq = MessageField()
    msgacsq = msgAnimCurveSq

    animCurveOutputSq = DoubleField(default_value=1.0)
    acoutsq = animCurveOutputSq

    msgAnimCurveSt = MessageField()
    msgacst = msgAnimCurveSt

    animCurveOutputSt = DoubleField(default_value=1.0)
    acoutst = animCurveOutputSt

    defWidthStart = DoubleField(default_value=1.0, min_value=0.0)
    defwidst = defWidthStart

    defWidthEnd = DoubleField(default_value=1.0, min_value=0.0)
    defwided = defWidthEnd

    lenDefault = DoubleField(default_value=1.0, min_value=0.0)
    lendef = lenDefault

    lenSquash = DoubleField(default_value=0.5, min_value=0.0)
    lensq = lenSquash

    lenStretch = DoubleField(default_value=2.0, min_value=0.0)
    lenst = lenStretch

    autoRotate = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    arot = autoRotate

    autoWiden = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    awid = autoWiden

    dampenOnSquash = DoubleField(default_value=0.75, min_value=0.0, max_value=1.0)
    dmpsq = dampenOnSquash

    dampenOnStretch = DoubleField(default_value=0.75, min_value=0.0, max_value=1.0)
    dmpst = dampenOnStretch

    manualSqSt = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    msqst = manualSqSt

    linearAutoSquash = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    lnatsq = linearAutoSquash

    linearAutoStretch = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    lnatst = linearAutoStretch

    userScale = DoubleField(default_value=1.0)
    usc = userScale

    gravityStrength = DoubleField(default_value=0.0, min_value=0.0)
    gravstr = gravityStrength

    gravityJiggle = DoubleField(default_value=0.0, min_value=0.0)
    gravjig = gravityJiggle

    gravityCycle = DoubleField(default_value=0.0, min_value=0.0)
    gravcyc = gravityCycle

    gravityX = DoubleField(default_value=0.0)
    gravx = gravityX

    gravityY = DoubleField(default_value=-1.0)
    gravy = gravityY

    gravityZ = DoubleField(default_value=0.0)
    gravz = gravityZ

    JIGGLE = JIGGLEEnumField(default_value=0)
    lbljig = JIGGLE

    resetFrame = DoubleField(default_value=0.0, min_value=-1024.0)
    rf = resetFrame


class JiggleFramePlugOperator(
    CompoundPlugOperator["JiggleFrameAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("force", "frc"),
    )

    force = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    frc = force


class JiggleFrameAttrOperator(
    CompoundAttrOperator[JiggleFramePlugOperator]
):
    __slots__ = ()

    force = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    frc = force


class JiggleFrameField(
    CompoundField[JiggleFrameAttrOperator, JiggleFramePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = JiggleFrameAttrOperator
    PLUG_CLS = JiggleFramePlugOperator


class PoseStatePlugOperator(
    CompoundPlugOperator["PoseStateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("poseDefault", "pd"),
        ("poseDefaultStored", "pds"),
        ("poseSquash", "psq"),
        ("poseSquashStored", "psqs"),
        ("poseStretch", "pst"),
        ("poseStretchStored", "psts"),
    )

    poseDefault = MatrixField()
    pd = poseDefault

    poseDefaultStored = BoolField(default_value=False)
    pds = poseDefaultStored

    poseSquash = MatrixField()
    psq = poseSquash

    poseSquashStored = BoolField(default_value=False)
    psqs = poseSquashStored

    poseStretch = MatrixField()
    pst = poseStretch

    poseStretchStored = BoolField(default_value=False)
    psts = poseStretchStored


class PoseStateAttrOperator(
    CompoundAttrOperator[PoseStatePlugOperator]
):
    __slots__ = ()

    poseDefault = MatrixField()
    pd = poseDefault

    poseDefaultStored = BoolField(default_value=False)
    pds = poseDefaultStored

    poseSquash = MatrixField()
    psq = poseSquash

    poseSquashStored = BoolField(default_value=False)
    psqs = poseSquashStored

    poseStretch = MatrixField()
    pst = poseStretch

    poseStretchStored = BoolField(default_value=False)
    psts = poseStretchStored


class PoseStateField(
    CompoundField[PoseStateAttrOperator, PoseStatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PoseStateAttrOperator
    PLUG_CLS = PoseStatePlugOperator

    poseDefault = MatrixField()
    pd = poseDefault

    poseDefaultStored = BoolField(default_value=False)
    pds = poseDefaultStored

    poseSquash = MatrixField()
    psq = poseSquash

    poseSquashStored = BoolField(default_value=False)
    psqs = poseSquashStored

    poseStretch = MatrixField()
    pst = poseStretch

    poseStretchStored = BoolField(default_value=False)
    psts = poseStretchStored


class ControlDataPlugOperator(
    CompoundPlugOperator["ControlDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("insertMatrix", "imat"),
        ("jiggle", "jig"),
        ("cycle", "cyc"),
        ("rest", "rst"),
        ("jiggleX", "jigx"),
        ("jiggleY", "jigy"),
        ("jiggleZ", "jigz"),
        ("jiggleImpact", "jigimp"),
        ("jiggleImpactStart", "jigimps"),
        ("jiggleImpactStop", "jigimpp"),
        ("curveRest", "crvrs"),
        ("curveSq", "crvsq"),
        ("curveSt", "crvst"),
    )

    insertMatrix = MatrixField()
    imat = insertMatrix

    jiggle = DoubleField(default_value=0.0)
    jig = jiggle

    cycle = DoubleField(default_value=10.0, min_value=1.0)
    cyc = cycle

    rest = DoubleField(default_value=24.0, min_value=1.0)
    rst = rest

    jiggleX = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    jigx = jiggleX

    jiggleY = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    jigy = jiggleY

    jiggleZ = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    jigz = jiggleZ

    jiggleImpact = DoubleField(default_value=0.0)
    jigimp = jiggleImpact

    jiggleImpactStart = DoubleField(default_value=0.1, min_value=0.0)
    jigimps = jiggleImpactStart

    jiggleImpactStop = DoubleField(default_value=0.1, min_value=0.0)
    jigimpp = jiggleImpactStop

    curveRest = DataNurbsCurveField()
    crvrs = curveRest

    curveSq = DataNurbsCurveField()
    crvsq = curveSq

    curveSt = DataNurbsCurveField()
    crvst = curveSt


class ControlDataAttrOperator(
    CompoundAttrOperator[ControlDataPlugOperator]
):
    __slots__ = ()

    insertMatrix = MatrixField()
    imat = insertMatrix

    jiggle = DoubleField(default_value=0.0)
    jig = jiggle

    cycle = DoubleField(default_value=10.0, min_value=1.0)
    cyc = cycle

    rest = DoubleField(default_value=24.0, min_value=1.0)
    rst = rest

    jiggleX = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    jigx = jiggleX

    jiggleY = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    jigy = jiggleY

    jiggleZ = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    jigz = jiggleZ

    jiggleImpact = DoubleField(default_value=0.0)
    jigimp = jiggleImpact

    jiggleImpactStart = DoubleField(default_value=0.1, min_value=0.0)
    jigimps = jiggleImpactStart

    jiggleImpactStop = DoubleField(default_value=0.1, min_value=0.0)
    jigimpp = jiggleImpactStop

    curveRest = DataNurbsCurveField()
    crvrs = curveRest

    curveSq = DataNurbsCurveField()
    crvsq = curveSq

    curveSt = DataNurbsCurveField()
    crvst = curveSt


class ControlDataField(
    CompoundField[ControlDataAttrOperator, ControlDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ControlDataAttrOperator
    PLUG_CLS = ControlDataPlugOperator


class LinearDataPlugOperator(
    CompoundPlugOperator["LinearDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("linearMatrix", "lmat"),
        ("uValue", "uval"),
    )

    linearMatrix = MatrixField()
    lmat = linearMatrix

    uValue = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    uval = uValue


class LinearDataAttrOperator(
    CompoundAttrOperator[LinearDataPlugOperator]
):
    __slots__ = ()

    linearMatrix = MatrixField()
    lmat = linearMatrix

    uValue = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    uval = uValue


class LinearDataField(
    CompoundField[LinearDataAttrOperator, LinearDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LinearDataAttrOperator
    PLUG_CLS = LinearDataPlugOperator


class AttachDataPlugOperator(
    CompoundPlugOperator["AttachDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("attachMatrix", "amat"),
        ("attachMatrixSq", "amatsq"),
        ("attachMatrixSt", "amatst"),
        ("gravityMult", "grvmul"),
    )

    attachMatrix = MatrixField()
    amat = attachMatrix

    attachMatrixSq = MatrixField()
    amatsq = attachMatrixSq

    attachMatrixSt = MatrixField()
    amatst = attachMatrixSt

    gravityMult = DoubleField(default_value=1.0, min_value=0.0)
    grvmul = gravityMult


class AttachDataAttrOperator(
    CompoundAttrOperator[AttachDataPlugOperator]
):
    __slots__ = ()

    attachMatrix = MatrixField()
    amat = attachMatrix

    attachMatrixSq = MatrixField()
    amatsq = attachMatrixSq

    attachMatrixSt = MatrixField()
    amatst = attachMatrixSt

    gravityMult = DoubleField(default_value=1.0, min_value=0.0)
    grvmul = gravityMult


class AttachDataField(
    CompoundField[AttachDataAttrOperator, AttachDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttachDataAttrOperator
    PLUG_CLS = AttachDataPlugOperator


class OutLinearDataPlugOperator(
    CompoundPlugOperator["OutLinearDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outLinearTranslate", "olt"),
        ("outLinearRotate", "olr"),
    )

    outLinearTranslate = CompoundField(default_value=(0.0, 0.0, 0.0))
    olt = outLinearTranslate

    outLinearRotate = CompoundField(default_value=(0.0, 0.0, 0.0))
    olr = outLinearRotate


class OutLinearDataAttrOperator(
    CompoundAttrOperator[OutLinearDataPlugOperator]
):
    __slots__ = ()

    outLinearTranslate = CompoundField(default_value=(0.0, 0.0, 0.0))
    olt = outLinearTranslate

    outLinearRotate = CompoundField(default_value=(0.0, 0.0, 0.0))
    olr = outLinearRotate


class OutLinearDataField(
    CompoundField[OutLinearDataAttrOperator, OutLinearDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutLinearDataAttrOperator
    PLUG_CLS = OutLinearDataPlugOperator


class OutAttachDataPlugOperator(
    CompoundPlugOperator["OutAttachDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outAttachTranslate", "oat"),
        ("outAttachRotate", "oar"),
    )

    outAttachTranslate = CompoundField(default_value=(0.0, 0.0, 0.0))
    oat = outAttachTranslate

    outAttachRotate = CompoundField(default_value=(0.0, 0.0, 0.0))
    oar = outAttachRotate


class OutAttachDataAttrOperator(
    CompoundAttrOperator[OutAttachDataPlugOperator]
):
    __slots__ = ()

    outAttachTranslate = CompoundField(default_value=(0.0, 0.0, 0.0))
    oat = outAttachTranslate

    outAttachRotate = CompoundField(default_value=(0.0, 0.0, 0.0))
    oar = outAttachRotate


class OutAttachDataField(
    CompoundField[OutAttachDataAttrOperator, OutAttachDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutAttachDataAttrOperator
    PLUG_CLS = OutAttachDataPlugOperator


class OutDrivenPlugOperator(
    CompoundPlugOperator["OutDrivenAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outDrivenSquash", "odsq"),
        ("outDrivenStretch", "odst"),
    )

    outDrivenSquash = DoubleField(default_value=0.0)
    odsq = outDrivenSquash

    outDrivenStretch = DoubleField(default_value=0.0)
    odst = outDrivenStretch


class OutDrivenAttrOperator(
    CompoundAttrOperator[OutDrivenPlugOperator]
):
    __slots__ = ()

    outDrivenSquash = DoubleField(default_value=0.0)
    odsq = outDrivenSquash

    outDrivenStretch = DoubleField(default_value=0.0)
    odst = outDrivenStretch


class OutDrivenField(
    CompoundField[OutDrivenAttrOperator, OutDrivenPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutDrivenAttrOperator
    PLUG_CLS = OutDrivenPlugOperator

    outDrivenSquash = DoubleField(default_value=0.0)
    odsq = outDrivenSquash

    outDrivenStretch = DoubleField(default_value=0.0)
    odst = outDrivenStretch
