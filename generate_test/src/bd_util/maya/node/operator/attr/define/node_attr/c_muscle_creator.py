# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.matrix import MatrixField
from ..std.at.message import MessageField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.dt.nurbs_curve import DataNurbsCurveField


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

    MODEL = EnumField()
    lblmdl = MODEL

    crossSections = LongField()
    csec = crossSections

    sides = LongField()
    sid = sides

    tolerance = LongField()
    tol = tolerance

    upAxis = EnumField()
    uax = upAxis

    flatCrossSections = BoolField()
    fltcrs = flatCrossSections

    showControls = BoolField()
    shcont = showControls

    showRestMovers = BoolField()
    shrsm = showRestMovers

    showSquashMovers = BoolField()
    shsqm = showSquashMovers

    showStretchMovers = BoolField()
    shstm = showStretchMovers

    SQUASH_STRETCH = EnumField()
    lblsqst = SQUASH_STRETCH

    basedOn = EnumField()
    sqstbo = basedOn

    interpMode = EnumField()
    intmod = interpMode

    poseUses = EnumField()
    pous = poseUses

    poseReadAxis = EnumField()
    psredax = poseReadAxis

    poseUseTwist = BoolField()
    psustw = poseUseTwist

    msgAnimCurveSq = MessageField()
    msgacsq = msgAnimCurveSq

    animCurveOutputSq = DoubleField()
    acoutsq = animCurveOutputSq

    msgAnimCurveSt = MessageField()
    msgacst = msgAnimCurveSt

    animCurveOutputSt = DoubleField()
    acoutst = animCurveOutputSt

    defWidthStart = DoubleField()
    defwidst = defWidthStart

    defWidthEnd = DoubleField()
    defwided = defWidthEnd

    lenDefault = DoubleField()
    lendef = lenDefault

    lenSquash = DoubleField()
    lensq = lenSquash

    lenStretch = DoubleField()
    lenst = lenStretch

    autoRotate = DoubleField()
    arot = autoRotate

    autoWiden = DoubleField()
    awid = autoWiden

    dampenOnSquash = DoubleField()
    dmpsq = dampenOnSquash

    dampenOnStretch = DoubleField()
    dmpst = dampenOnStretch

    manualSqSt = DoubleField()
    msqst = manualSqSt

    linearAutoSquash = DoubleField()
    lnatsq = linearAutoSquash

    linearAutoStretch = DoubleField()
    lnatst = linearAutoStretch

    userScale = DoubleField()
    usc = userScale

    gravityStrength = DoubleField()
    gravstr = gravityStrength

    gravityJiggle = DoubleField()
    gravjig = gravityJiggle

    gravityCycle = DoubleField()
    gravcyc = gravityCycle

    gravityX = DoubleField()
    gravx = gravityX

    gravityY = DoubleField()
    gravy = gravityY

    gravityZ = DoubleField()
    gravz = gravityZ

    JIGGLE = EnumField()
    lbljig = JIGGLE

    resetFrame = DoubleField()
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

    MODEL = EnumField()
    lblmdl = MODEL

    crossSections = LongField()
    csec = crossSections

    sides = LongField()
    sid = sides

    tolerance = LongField()
    tol = tolerance

    upAxis = EnumField()
    uax = upAxis

    flatCrossSections = BoolField()
    fltcrs = flatCrossSections

    showControls = BoolField()
    shcont = showControls

    showRestMovers = BoolField()
    shrsm = showRestMovers

    showSquashMovers = BoolField()
    shsqm = showSquashMovers

    showStretchMovers = BoolField()
    shstm = showStretchMovers

    SQUASH_STRETCH = EnumField()
    lblsqst = SQUASH_STRETCH

    basedOn = EnumField()
    sqstbo = basedOn

    interpMode = EnumField()
    intmod = interpMode

    poseUses = EnumField()
    pous = poseUses

    poseReadAxis = EnumField()
    psredax = poseReadAxis

    poseUseTwist = BoolField()
    psustw = poseUseTwist

    msgAnimCurveSq = MessageField()
    msgacsq = msgAnimCurveSq

    animCurveOutputSq = DoubleField()
    acoutsq = animCurveOutputSq

    msgAnimCurveSt = MessageField()
    msgacst = msgAnimCurveSt

    animCurveOutputSt = DoubleField()
    acoutst = animCurveOutputSt

    defWidthStart = DoubleField()
    defwidst = defWidthStart

    defWidthEnd = DoubleField()
    defwided = defWidthEnd

    lenDefault = DoubleField()
    lendef = lenDefault

    lenSquash = DoubleField()
    lensq = lenSquash

    lenStretch = DoubleField()
    lenst = lenStretch

    autoRotate = DoubleField()
    arot = autoRotate

    autoWiden = DoubleField()
    awid = autoWiden

    dampenOnSquash = DoubleField()
    dmpsq = dampenOnSquash

    dampenOnStretch = DoubleField()
    dmpst = dampenOnStretch

    manualSqSt = DoubleField()
    msqst = manualSqSt

    linearAutoSquash = DoubleField()
    lnatsq = linearAutoSquash

    linearAutoStretch = DoubleField()
    lnatst = linearAutoStretch

    userScale = DoubleField()
    usc = userScale

    gravityStrength = DoubleField()
    gravstr = gravityStrength

    gravityJiggle = DoubleField()
    gravjig = gravityJiggle

    gravityCycle = DoubleField()
    gravcyc = gravityCycle

    gravityX = DoubleField()
    gravx = gravityX

    gravityY = DoubleField()
    gravy = gravityY

    gravityZ = DoubleField()
    gravz = gravityZ

    JIGGLE = EnumField()
    lbljig = JIGGLE

    resetFrame = DoubleField()
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

    MODEL = EnumField()
    lblmdl = MODEL

    crossSections = LongField()
    csec = crossSections

    sides = LongField()
    sid = sides

    tolerance = LongField()
    tol = tolerance

    upAxis = EnumField()
    uax = upAxis

    flatCrossSections = BoolField()
    fltcrs = flatCrossSections

    showControls = BoolField()
    shcont = showControls

    showRestMovers = BoolField()
    shrsm = showRestMovers

    showSquashMovers = BoolField()
    shsqm = showSquashMovers

    showStretchMovers = BoolField()
    shstm = showStretchMovers

    SQUASH_STRETCH = EnumField()
    lblsqst = SQUASH_STRETCH

    basedOn = EnumField()
    sqstbo = basedOn

    interpMode = EnumField()
    intmod = interpMode

    poseUses = EnumField()
    pous = poseUses

    poseReadAxis = EnumField()
    psredax = poseReadAxis

    poseUseTwist = BoolField()
    psustw = poseUseTwist

    msgAnimCurveSq = MessageField()
    msgacsq = msgAnimCurveSq

    animCurveOutputSq = DoubleField()
    acoutsq = animCurveOutputSq

    msgAnimCurveSt = MessageField()
    msgacst = msgAnimCurveSt

    animCurveOutputSt = DoubleField()
    acoutst = animCurveOutputSt

    defWidthStart = DoubleField()
    defwidst = defWidthStart

    defWidthEnd = DoubleField()
    defwided = defWidthEnd

    lenDefault = DoubleField()
    lendef = lenDefault

    lenSquash = DoubleField()
    lensq = lenSquash

    lenStretch = DoubleField()
    lenst = lenStretch

    autoRotate = DoubleField()
    arot = autoRotate

    autoWiden = DoubleField()
    awid = autoWiden

    dampenOnSquash = DoubleField()
    dmpsq = dampenOnSquash

    dampenOnStretch = DoubleField()
    dmpst = dampenOnStretch

    manualSqSt = DoubleField()
    msqst = manualSqSt

    linearAutoSquash = DoubleField()
    lnatsq = linearAutoSquash

    linearAutoStretch = DoubleField()
    lnatst = linearAutoStretch

    userScale = DoubleField()
    usc = userScale

    gravityStrength = DoubleField()
    gravstr = gravityStrength

    gravityJiggle = DoubleField()
    gravjig = gravityJiggle

    gravityCycle = DoubleField()
    gravcyc = gravityCycle

    gravityX = DoubleField()
    gravx = gravityX

    gravityY = DoubleField()
    gravy = gravityY

    gravityZ = DoubleField()
    gravz = gravityZ

    JIGGLE = EnumField()
    lbljig = JIGGLE

    resetFrame = DoubleField()
    rf = resetFrame


class JiggleFramePlugOperator(
    CompoundPlugOperator["JiggleFrameAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("force", "frc"),
    )

    force = CompoundField()
    frc = force


class JiggleFrameAttrOperator(
    CompoundAttrOperator[JiggleFramePlugOperator]
):
    __slots__ = ()

    force = CompoundField()
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

    poseDefaultStored = BoolField()
    pds = poseDefaultStored

    poseSquash = MatrixField()
    psq = poseSquash

    poseSquashStored = BoolField()
    psqs = poseSquashStored

    poseStretch = MatrixField()
    pst = poseStretch

    poseStretchStored = BoolField()
    psts = poseStretchStored


class PoseStateAttrOperator(
    CompoundAttrOperator[PoseStatePlugOperator]
):
    __slots__ = ()

    poseDefault = MatrixField()
    pd = poseDefault

    poseDefaultStored = BoolField()
    pds = poseDefaultStored

    poseSquash = MatrixField()
    psq = poseSquash

    poseSquashStored = BoolField()
    psqs = poseSquashStored

    poseStretch = MatrixField()
    pst = poseStretch

    poseStretchStored = BoolField()
    psts = poseStretchStored


class PoseStateField(
    CompoundField[PoseStateAttrOperator, PoseStatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PoseStateAttrOperator
    PLUG_CLS = PoseStatePlugOperator

    poseDefault = MatrixField()
    pd = poseDefault

    poseDefaultStored = BoolField()
    pds = poseDefaultStored

    poseSquash = MatrixField()
    psq = poseSquash

    poseSquashStored = BoolField()
    psqs = poseSquashStored

    poseStretch = MatrixField()
    pst = poseStretch

    poseStretchStored = BoolField()
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

    jiggle = DoubleField()
    jig = jiggle

    cycle = DoubleField()
    cyc = cycle

    rest = DoubleField()
    rst = rest

    jiggleX = DoubleField()
    jigx = jiggleX

    jiggleY = DoubleField()
    jigy = jiggleY

    jiggleZ = DoubleField()
    jigz = jiggleZ

    jiggleImpact = DoubleField()
    jigimp = jiggleImpact

    jiggleImpactStart = DoubleField()
    jigimps = jiggleImpactStart

    jiggleImpactStop = DoubleField()
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

    jiggle = DoubleField()
    jig = jiggle

    cycle = DoubleField()
    cyc = cycle

    rest = DoubleField()
    rst = rest

    jiggleX = DoubleField()
    jigx = jiggleX

    jiggleY = DoubleField()
    jigy = jiggleY

    jiggleZ = DoubleField()
    jigz = jiggleZ

    jiggleImpact = DoubleField()
    jigimp = jiggleImpact

    jiggleImpactStart = DoubleField()
    jigimps = jiggleImpactStart

    jiggleImpactStop = DoubleField()
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

    uValue = DoubleField()
    uval = uValue


class LinearDataAttrOperator(
    CompoundAttrOperator[LinearDataPlugOperator]
):
    __slots__ = ()

    linearMatrix = MatrixField()
    lmat = linearMatrix

    uValue = DoubleField()
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

    gravityMult = DoubleField()
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

    gravityMult = DoubleField()
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

    outLinearTranslate = CompoundField()
    olt = outLinearTranslate

    outLinearRotate = CompoundField()
    olr = outLinearRotate


class OutLinearDataAttrOperator(
    CompoundAttrOperator[OutLinearDataPlugOperator]
):
    __slots__ = ()

    outLinearTranslate = CompoundField()
    olt = outLinearTranslate

    outLinearRotate = CompoundField()
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

    outAttachTranslate = CompoundField()
    oat = outAttachTranslate

    outAttachRotate = CompoundField()
    oar = outAttachRotate


class OutAttachDataAttrOperator(
    CompoundAttrOperator[OutAttachDataPlugOperator]
):
    __slots__ = ()

    outAttachTranslate = CompoundField()
    oat = outAttachTranslate

    outAttachRotate = CompoundField()
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

    outDrivenSquash = DoubleField()
    odsq = outDrivenSquash

    outDrivenStretch = DoubleField()
    odst = outDrivenStretch


class OutDrivenAttrOperator(
    CompoundAttrOperator[OutDrivenPlugOperator]
):
    __slots__ = ()

    outDrivenSquash = DoubleField()
    odsq = outDrivenSquash

    outDrivenStretch = DoubleField()
    odst = outDrivenStretch


class OutDrivenField(
    CompoundField[OutDrivenAttrOperator, OutDrivenPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutDrivenAttrOperator
    PLUG_CLS = OutDrivenPlugOperator

    outDrivenSquash = DoubleField()
    odsq = outDrivenSquash

    outDrivenStretch = DoubleField()
    odst = outDrivenStretch
