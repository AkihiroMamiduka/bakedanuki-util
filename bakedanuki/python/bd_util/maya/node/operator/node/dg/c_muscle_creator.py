# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.c_muscle_creator import (
    AttachDataField,
    ControlDataField,
    JiggleFrameField,
    LinearDataField,
    NurbsDataField,
    OutAttachDataField,
    OutDrivenField,
    OutLinearDataField,
    PoseStateField,
)
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class CMuscleCreator(DG):
    __slots__ = ()

    NODE_TYPE = "cMuscleCreator"

    nurbsData = NurbsDataField()
    ndata = nurbsData
    startPointA = nurbsData.startPointA
    spa = startPointA
    startPointB = nurbsData.startPointB
    spb = startPointB
    endPointA = nurbsData.endPointA
    epa = endPointA
    endPointB = nurbsData.endPointB
    epb = endPointB
    startParent = nurbsData.startParent
    spm = startParent
    endParent = nurbsData.endParent
    epm = endParent
    MODEL = nurbsData.MODEL
    lblmdl = MODEL
    crossSections = nurbsData.crossSections
    csec = crossSections
    sides = nurbsData.sides
    sid = sides
    tolerance = nurbsData.tolerance
    tol = tolerance
    upAxis = nurbsData.upAxis
    uax = upAxis
    flatCrossSections = nurbsData.flatCrossSections
    fltcrs = flatCrossSections
    showControls = nurbsData.showControls
    shcont = showControls
    showRestMovers = nurbsData.showRestMovers
    shrsm = showRestMovers
    showSquashMovers = nurbsData.showSquashMovers
    shsqm = showSquashMovers
    showStretchMovers = nurbsData.showStretchMovers
    shstm = showStretchMovers
    SQUASH_STRETCH = nurbsData.SQUASH_STRETCH
    lblsqst = SQUASH_STRETCH
    basedOn = nurbsData.basedOn
    sqstbo = basedOn
    interpMode = nurbsData.interpMode
    intmod = interpMode
    poseUses = nurbsData.poseUses
    pous = poseUses
    poseReadAxis = nurbsData.poseReadAxis
    psredax = poseReadAxis
    poseUseTwist = nurbsData.poseUseTwist
    psustw = poseUseTwist
    msgAnimCurveSq = nurbsData.msgAnimCurveSq
    msgacsq = msgAnimCurveSq
    animCurveOutputSq = nurbsData.animCurveOutputSq
    acoutsq = animCurveOutputSq
    msgAnimCurveSt = nurbsData.msgAnimCurveSt
    msgacst = msgAnimCurveSt
    animCurveOutputSt = nurbsData.animCurveOutputSt
    acoutst = animCurveOutputSt
    defWidthStart = nurbsData.defWidthStart
    defwidst = defWidthStart
    defWidthEnd = nurbsData.defWidthEnd
    defwided = defWidthEnd
    lenDefault = nurbsData.lenDefault
    lendef = lenDefault
    lenSquash = nurbsData.lenSquash
    lensq = lenSquash
    lenStretch = nurbsData.lenStretch
    lenst = lenStretch
    autoRotate = nurbsData.autoRotate
    arot = autoRotate
    autoWiden = nurbsData.autoWiden
    awid = autoWiden
    dampenOnSquash = nurbsData.dampenOnSquash
    dmpsq = dampenOnSquash
    dampenOnStretch = nurbsData.dampenOnStretch
    dmpst = dampenOnStretch
    manualSqSt = nurbsData.manualSqSt
    msqst = manualSqSt
    linearAutoSquash = nurbsData.linearAutoSquash
    lnatsq = linearAutoSquash
    linearAutoStretch = nurbsData.linearAutoStretch
    lnatst = linearAutoStretch
    userScale = nurbsData.userScale
    usc = userScale
    gravityStrength = nurbsData.gravityStrength
    gravstr = gravityStrength
    gravityJiggle = nurbsData.gravityJiggle
    gravjig = gravityJiggle
    gravityCycle = nurbsData.gravityCycle
    gravcyc = gravityCycle
    gravityX = nurbsData.gravityX
    gravx = gravityX
    gravityY = nurbsData.gravityY
    gravy = gravityY
    gravityZ = nurbsData.gravityZ
    gravz = gravityZ
    JIGGLE = nurbsData.JIGGLE
    lbljig = JIGGLE
    resetFrame = nurbsData.resetFrame
    rf = resetFrame

    jiggleFrame = JiggleFrameField(multi=True)
    jfrm = jiggleFrame

    poseState = PoseStateField()
    pstate = poseState
    poseDefault = poseState.poseDefault
    pd = poseDefault
    poseDefaultStored = poseState.poseDefaultStored
    pds = poseDefaultStored
    poseSquash = poseState.poseSquash
    psq = poseSquash
    poseSquashStored = poseState.poseSquashStored
    psqs = poseSquashStored
    poseStretch = poseState.poseStretch
    pst = poseStretch
    poseStretchStored = poseState.poseStretchStored
    psts = poseStretchStored

    inTime = DoubleField(default_value=0.0)
    it = inTime

    controlData = ControlDataField(multi=True)
    cdata = controlData

    linearData = LinearDataField(multi=True)
    ldata = linearData

    attachData = AttachDataField(multi=True)
    atdata = attachData

    outNurbs = DataNurbsSurfaceField()
    onrb = outNurbs

    outLength = DoubleField(default_value=0.0)
    olen = outLength

    outLinearData = OutLinearDataField(multi=True)
    oldat = outLinearData

    outLinearTranslateX = DoubleField()
    oltx = outLinearTranslateX

    outLinearTranslateY = DoubleField()
    olty = outLinearTranslateY

    outLinearTranslateZ = DoubleField()
    oltz = outLinearTranslateZ

    outLinearRotateX = DoubleField()
    olrx = outLinearRotateX

    outLinearRotateY = DoubleField()
    olry = outLinearRotateY

    outLinearRotateZ = DoubleField()
    olrz = outLinearRotateZ

    outAttachData = OutAttachDataField(multi=True)
    oadat = outAttachData

    outAttachTranslateX = DoubleField()
    oatx = outAttachTranslateX

    outAttachTranslateY = DoubleField()
    oaty = outAttachTranslateY

    outAttachTranslateZ = DoubleField()
    oatz = outAttachTranslateZ

    outAttachRotateX = DoubleField()
    oarx = outAttachRotateX

    outAttachRotateY = DoubleField()
    oary = outAttachRotateY

    outAttachRotateZ = DoubleField()
    oarz = outAttachRotateZ

    outDriven = OutDrivenField(default_value=(0.0, 0.0))
    odrvn = outDriven
    outDrivenSquash = outDriven.outDrivenSquash
    odsq = outDrivenSquash
    outDrivenStretch = outDriven.outDrivenStretch
    odst = outDrivenStretch
