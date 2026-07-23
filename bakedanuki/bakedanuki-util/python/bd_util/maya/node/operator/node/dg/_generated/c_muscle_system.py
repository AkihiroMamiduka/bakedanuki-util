# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.c_muscle_system import (
    CacheFrameField,
    DirDataField,
    DispDataField,
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    JiggleFrameField,
    MuscleDataField,
    RelativePointField,
    RelaxDataField,
    SelfCollideDataField,
    SmartCollideDataField,
    SmoothDataField,
    StickyListField,
    StickyWeightListMusBField,
    StickyWeightListMusCField,
    StickyWeightListMusField,
    UserDataField,
    WeightListDirField,
    WeightListField,
    WeightListMusField,
    WeightListSmartBulkAngularField,
    WeightListSmartBulkField,
    WeightListSmartBulkWidenField,
    WeightListSmartFlattenField,
    WeightListSmartRegionAField,
    WeightListSmartRegionBField,
    WeightListSmartSlideAngularField,
    WeightListSmartSlideField,
    WeightListSmartSmoothField,
    WeightListSmartVolumizeField,
    WeightListSmartWrinkleField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField
from ....attr.define.std.at.typed import TypedField


class _GeneratedCMuscleSystem(DG):
    __slots__ = ()

    NODE_TYPE = "cMuscleSystem"

    input = InputField(multi=True)
    ip = input

    weightFunction = TypedField(multi=True)
    wfl = weightFunction

    outputGeometry = TypedField(multi=True, writable=False)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(multi=True, default_value=1.0, writable=False)
    ocw = envelopeWeightsList

    blockGPU = BoolField(default_value=False)
    bgp = blockGPU

    envelope = FloatField(default_value=1.0, min_value=-2.0, max_value=2.0, soft_min_value=0.0, soft_max_value=1.0)
    en = envelope

    function = FunctionField(default_value=(0, 0, 0), readable=False)
    f = function
    fchild1 = function.fchild1
    f1 = fchild1
    fchild2 = function.fchild2
    f2 = fchild2
    fchild3 = function.fchild3
    f3 = fchild3

    map64BitIndices = TypedField()
    map = map64BitIndices

    weightList = WeightListField(multi=True, default_value=1.0)
    wl = weightList

    userData = UserDataField()
    udata = userData
    inTime = userData.inTime
    it = inTime
    cache = userData.cache
    cac = cache
    cachePath = userData.cachePath
    cpath = cachePath
    showWarnings = userData.showWarnings
    swrn = showWarnings
    userScale = userData.userScale
    usc = userScale
    STICKY = userData.STICKY
    LSTK = STICKY
    enableSticky = userData.enableSticky
    estk = enableSticky
    relativeSticky = userData.relativeSticky
    relstk = relativeSticky
    forceNormalize = userData.forceNormalize
    frcnrm = forceNormalize
    stickyA = userData.stickyA
    stka = stickyA
    stickyB = userData.stickyB
    stkb = stickyB
    stickyC = userData.stickyC
    stkc = stickyC
    SLIDING = userData.SLIDING
    LSLD = SLIDING
    enableSliding = userData.enableSliding
    esld = enableSliding
    quality = userData.quality
    qlty = quality
    shrinkWrap = userData.shrinkWrap
    shr = shrinkWrap
    useBind = userData.useBind
    ub = useBind
    allowNegFat = userData.allowNegFat
    anft = allowNegFat
    DISPLACE = userData.DISPLACE
    LDSP = DISPLACE
    enableDisplace = userData.enableDisplace
    edsp = enableDisplace
    collisionDisplace = userData.collisionDisplace
    clldsp = collisionDisplace
    FORCE = userData.FORCE
    LFRC = FORCE
    enableForce = userData.enableForce
    efrc = enableForce
    gravityStrength = userData.gravityStrength
    gravstr = gravityStrength
    gravityX = userData.gravityX
    gravx = gravityX
    gravityY = userData.gravityY
    gravy = gravityY
    gravityZ = userData.gravityZ
    gravz = gravityZ
    windStrength = userData.windStrength
    windstr = windStrength
    windDirX = userData.windDirX
    windx = windDirX
    windDirY = userData.windDirY
    windy = windDirY
    windDirZ = userData.windDirZ
    windz = windDirZ
    windSpeed = userData.windSpeed
    windspd = windSpeed
    windNoise = userData.windNoise
    windnos = windNoise
    windNoiseScale = userData.windNoiseScale
    windnscl = windNoiseScale
    windNoiseDirty = userData.windNoiseDirty
    winddrt = windNoiseDirty
    JIGGLE = userData.JIGGLE
    LJIG = JIGGLE
    enableJiggle = userData.enableJiggle
    ejig = enableJiggle
    jiggleCollisions = userData.jiggleCollisions
    jigcol = jiggleCollisions
    resetFrame = userData.resetFrame
    rf = resetFrame
    jiggleMin = userData.jiggleMin
    jmin = jiggleMin
    jiggleMax = userData.jiggleMax
    jmax = jiggleMax
    cycleMin = userData.cycleMin
    cmin = cycleMin
    cycleMax = userData.cycleMax
    cmax = cycleMax
    restMin = userData.restMin
    rmin = restMin
    restMax = userData.restMax
    rmax = restMax
    RELAX = userData.RELAX
    LRLX = RELAX
    enableRelax = userData.enableRelax
    erlx = enableRelax
    relaxMode = userData.relaxMode
    rmod = relaxMode
    relaxCollisions = userData.relaxCollisions
    rcll = relaxCollisions
    relaxIterations = userData.relaxIterations
    ritr = relaxIterations
    relaxStrength = userData.relaxStrength
    rstr = relaxStrength
    wrinkleStrength = userData.wrinkleStrength
    wrstr = wrinkleStrength
    relaxCompress = userData.relaxCompress
    rcmp = relaxCompress
    relaxExpand = userData.relaxExpand
    rexp = relaxExpand
    relaxFriction = userData.relaxFriction
    rfrc = relaxFriction
    SMOOTH = userData.SMOOTH
    SMTH = SMOOTH
    enableSmooth = userData.enableSmooth
    esmth = enableSmooth
    smoothCollisions = userData.smoothCollisions
    scll = smoothCollisions
    smoothIterations = userData.smoothIterations
    sitr = smoothIterations
    smoothStrength = userData.smoothStrength
    sstr = smoothStrength
    smoothCompress = userData.smoothCompress
    scmp = smoothCompress
    smoothExpand = userData.smoothExpand
    sexp = smoothExpand
    smoothHold = userData.smoothHold
    shld = smoothHold
    COLLISION = userData.COLLISION
    COLL = COLLISION
    smartCollision = userData.smartCollision
    smrtcll = smartCollision
    selfCollision = userData.selfCollision
    slfcll = selfCollision
    selfTolerance = userData.selfTolerance
    slftol = selfTolerance
    selfFalloff = userData.selfFalloff
    slffal = selfFalloff
    selfVolumize = userData.selfVolumize
    slfvol = selfVolumize
    selfBlurIterations = userData.selfBlurIterations
    slfblrit = selfBlurIterations
    selfRelaxIterations = userData.selfRelaxIterations
    slfrxi = selfRelaxIterations
    selfRelaxStrength = userData.selfRelaxStrength
    slfrxstr = selfRelaxStrength
    selfSmoothIterations = userData.selfSmoothIterations
    slfsmi = selfSmoothIterations
    selfSmoothStrength = userData.selfSmoothStrength
    slfsmstr = selfSmoothStrength
    selfSmoothHold = userData.selfSmoothHold
    slfhld = selfSmoothHold

    muscleData = MuscleDataField(multi=True)
    data = muscleData

    userScaleMusX = DoubleField()
    usxmus = userScaleMusX

    userScaleMusY = DoubleField()
    usymus = userScaleMusY

    userScaleMusZ = DoubleField()
    uszmus = userScaleMusZ

    dirData = DirDataField(multi=True)
    ddata = dirData

    dispData = DispDataField(multi=True)
    dspdata = dispData

    smartCollideData = SmartCollideDataField(multi=True)
    scdata = smartCollideData

    selfCollideData = SelfCollideDataField(multi=True)
    slfdata = selfCollideData

    relaxData = RelaxDataField()
    reldata = relaxData
    numStretch = relaxData.numStretch
    nstr = numStretch
    numBend = relaxData.numBend
    nbnd = numBend
    relaxSt = relaxData.relaxSt
    relst = relaxSt
    relaxBd = relaxData.relaxBd
    relbd = relaxBd
    numCons = relaxData.numCons
    ncns = numCons
    numPts = relaxData.numPts
    npts = numPts
    ptsBase = relaxData.ptsBase
    ptsBS = ptsBase
    numTri = relaxData.numTri
    ntri = numTri
    relaxTri = relaxData.relaxTri
    reltri = relaxTri

    ptIdxASt = LongField()
    ptast = ptIdxASt

    ptIdxBSt = LongField()
    ptbst = ptIdxBSt

    restLenSt = DoubleField()
    rlenst = restLenSt

    ptIdxABd = LongField()
    ptabd = ptIdxABd

    ptIdxBBd = LongField()
    ptbbd = ptIdxBBd

    restLenBd = DoubleField()
    rlenbd = restLenBd

    ptsBaseX = DoubleField()
    ptsBSX = ptsBaseX

    ptsBaseY = DoubleField()
    ptsBSY = ptsBaseY

    ptsBaseZ = DoubleField()
    ptsBSZ = ptsBaseZ

    relaxTriIdxA = LongField()
    rtidxa = relaxTriIdxA

    relaxTriIdxB = LongField()
    rtidxb = relaxTriIdxB

    relaxTriIdxC = LongField()
    rtidxc = relaxTriIdxC

    relaxTriAdj = LongField()
    rtadj = relaxTriAdj

    relativePoint = RelativePointField(multi=True, default_value=(0.0, 0.0, 0.0))
    relpt = relativePoint

    smoothData = SmoothDataField()
    smtdata = smoothData
    smoothEntry = smoothData.smoothEntry
    smte = smoothEntry
    ptToPtEntry = smoothData.ptToPtEntry
    ptpe = ptToPtEntry

    smoothCon = LongField()
    smtc = smoothCon

    ptToPtCon = LongField()
    ptpc = ptToPtCon

    jiggle = DoubleField(multi=True, default_value=0.0, min_value=0.0, max_value=1.0)
    jig = jiggle

    cycle = DoubleField(multi=True, default_value=0.0, min_value=0.0, max_value=1.0)
    cyc = cycle

    rest = DoubleField(multi=True, default_value=0.0, min_value=0.0, max_value=1.0)
    rst = rest

    jiggleFrame = JiggleFrameField(multi=True)
    jfrm = jiggleFrame

    cacheFrame = CacheFrameField(multi=True)
    cfrm = cacheFrame

    wtChange = BoolField(default_value=False)
    wchg = wtChange

    wtChangeInternal = ShortField(default_value=0)
    wchgi = wtChangeInternal

    wtPointCount = LongField(default_value=0)
    wtptcnt = wtPointCount

    wtPointIndex = LongField(multi=True, default_value=0)
    wtptidx = wtPointIndex

    wtColChange = BoolField(default_value=False)
    wtcolchg = wtColChange

    wtForceUpdate = LongField(default_value=0)
    wtfrcupd = wtForceUpdate

    relaxChange = BoolField(default_value=False)
    rlxchg = relaxChange

    weightListMus = WeightListMusField(multi=True, default_value=0.0, min_value=0.0)
    wlm = weightListMus

    fatList = DoubleField(multi=True, default_value=0.0)
    fl = fatList

    stickyWeightListMus = StickyWeightListMusField(multi=True, default_value=0.0, min_value=0.0)
    stkwlm = stickyWeightListMus

    stickyWeightListMusB = StickyWeightListMusBField(multi=True, default_value=0.0, min_value=0.0)
    stkwlmb = stickyWeightListMusB

    stickyWeightListMusC = StickyWeightListMusCField(multi=True, default_value=0.0, min_value=0.0)
    stkwlmc = stickyWeightListMusC

    stickyList = StickyListField(multi=True)
    stklist = stickyList

    weightListDir = WeightListDirField(multi=True, default_value=0.0, min_value=0.0)
    wld = weightListDir

    weightListSmartRegionA = WeightListSmartRegionAField(multi=True, default_value=0.0, min_value=0.0)
    wlsmrtrega = weightListSmartRegionA

    weightListSmartRegionB = WeightListSmartRegionBField(multi=True, default_value=0.0, min_value=0.0)
    wlsmrtregb = weightListSmartRegionB

    weightListSmartBulk = WeightListSmartBulkField(multi=True, default_value=0.0, min_value=0.0)
    wlsmrtblk = weightListSmartBulk

    weightListSmartBulkAngular = WeightListSmartBulkAngularField(multi=True, default_value=0.0, min_value=0.0)
    wlsmrtblkang = weightListSmartBulkAngular

    weightListSmartBulkWiden = WeightListSmartBulkWidenField(multi=True, default_value=0.0, min_value=0.0)
    wlsmrtblkwid = weightListSmartBulkWiden

    weightListSmartSlide = WeightListSmartSlideField(multi=True, default_value=0.0, min_value=0.0)
    wlsmrtsld = weightListSmartSlide

    weightListSmartSlideAngular = WeightListSmartSlideAngularField(multi=True, default_value=0.0, min_value=0.0)
    wlsmrtsldang = weightListSmartSlideAngular

    weightListSmartSmooth = WeightListSmartSmoothField(multi=True, default_value=0.0, min_value=0.0)
    wlsmrtsmth = weightListSmartSmooth

    weightListSmartWrinkle = WeightListSmartWrinkleField(multi=True, default_value=0.0, min_value=0.0)
    wlsmrtwrk = weightListSmartWrinkle

    weightListSmartFlatten = WeightListSmartFlattenField(multi=True, default_value=0.0, min_value=0.0)
    wlsmrtflt = weightListSmartFlatten

    weightListSmartVolumize = WeightListSmartVolumizeField(multi=True, default_value=0.0, min_value=0.0)
    wlsmrtvol = weightListSmartVolumize

    weightsForce = DoubleField(multi=True, default_value=1.0)
    wtfrc = weightsForce

    weightsRelax = DoubleField(multi=True, default_value=1.0)
    wtrlx = weightsRelax

    weightsWrinkle = DoubleField(multi=True, default_value=0.0)
    wtwrk = weightsWrinkle

    weightsSmooth = DoubleField(multi=True, default_value=1.0)
    wtsmt = weightsSmooth

    weightsSmoothCompress = DoubleField(multi=True, default_value=1.0)
    wtsmtcmp = weightsSmoothCompress

    weightsSmoothExpand = DoubleField(multi=True, default_value=1.0)
    wtsmtexp = weightsSmoothExpand

    weightsSelfCollision = DoubleField(multi=True, default_value=1.0)
    wtsslfcol = weightsSelfCollision

    weightsSelfRigidity = DoubleField(multi=True, default_value=0.0)
    wtsslfrig = weightsSelfRigidity

    weightsSelfVolumize = DoubleField(multi=True, default_value=1.0)
    wtsslfvol = weightsSelfVolumize
