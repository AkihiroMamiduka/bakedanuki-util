# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.generic import GenericField
from ..std.at.matrix import MatrixField
from ..std.at.message import MessageField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.long_compound.long3_compound._base import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
)


class CacheEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DISABLED = 0
    WRITE_MINUS_FILE = 1
    READ_MINUS_FILE = 2
    WRITE_MINUS_NODE = 3
    READ_MINUS_NODE = 4


class CacheEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DISABLED = 0
    WRITE_MINUS_FILE = 1
    READ_MINUS_FILE = 2
    WRITE_MINUS_NODE = 3
    READ_MINUS_NODE = 4

    NAME_MAP = {
        DISABLED: "disabled",
        WRITE_MINUS_FILE: "write-file",
        READ_MINUS_FILE: "read-file",
        WRITE_MINUS_NODE: "write-node",
        READ_MINUS_NODE: "read-node",
    }


class CacheEnumField(
    EnumField[CacheEnumAttrOperator, CacheEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CacheEnumAttrOperator
    PLUG_CLS = CacheEnumPlugOperator


class STICKYEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class STICKYEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class STICKYEnumField(
    EnumField[STICKYEnumAttrOperator, STICKYEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = STICKYEnumAttrOperator
    PLUG_CLS = STICKYEnumPlugOperator


class RelativeStickyEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    RELATIVE = 1


class RelativeStickyEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    RELATIVE = 1

    NAME_MAP = {
        OFF: "off",
        RELATIVE: "relative",
    }


class RelativeStickyEnumField(
    EnumField[RelativeStickyEnumAttrOperator, RelativeStickyEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RelativeStickyEnumAttrOperator
    PLUG_CLS = RelativeStickyEnumPlugOperator


class SLIDINGEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class SLIDINGEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class SLIDINGEnumField(
    EnumField[SLIDINGEnumAttrOperator, SLIDINGEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SLIDINGEnumAttrOperator
    PLUG_CLS = SLIDINGEnumPlugOperator


class QualityEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FULL = 0
    MEDIUM = 1
    LOW = 2


class QualityEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FULL = 0
    MEDIUM = 1
    LOW = 2

    NAME_MAP = {
        FULL: "Full",
        MEDIUM: "Medium",
        LOW: "Low",
    }


class QualityEnumField(
    EnumField[QualityEnumAttrOperator, QualityEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = QualityEnumAttrOperator
    PLUG_CLS = QualityEnumPlugOperator


class DISPLACEEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class DISPLACEEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class DISPLACEEnumField(
    EnumField[DISPLACEEnumAttrOperator, DISPLACEEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DISPLACEEnumAttrOperator
    PLUG_CLS = DISPLACEEnumPlugOperator


class FORCEEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class FORCEEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class FORCEEnumField(
    EnumField[FORCEEnumAttrOperator, FORCEEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FORCEEnumAttrOperator
    PLUG_CLS = FORCEEnumPlugOperator


class JIGGLEEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class JIGGLEEnumAttrOperator(EnumAttrOperator):
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


class RELAXEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class RELAXEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class RELAXEnumField(
    EnumField[RELAXEnumAttrOperator, RELAXEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RELAXEnumAttrOperator
    PLUG_CLS = RELAXEnumPlugOperator


class RelaxModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 0
    PULL = 1
    WRINKLE = 2


class RelaxModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 0
    PULL = 1
    WRINKLE = 2

    NAME_MAP = {
        NORMAL: "normal",
        PULL: "pull",
        WRINKLE: "wrinkle",
    }


class RelaxModeEnumField(
    EnumField[RelaxModeEnumAttrOperator, RelaxModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RelaxModeEnumAttrOperator
    PLUG_CLS = RelaxModeEnumPlugOperator


class SMOOTHEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class SMOOTHEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class SMOOTHEnumField(
    EnumField[SMOOTHEnumAttrOperator, SMOOTHEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SMOOTHEnumAttrOperator
    PLUG_CLS = SMOOTHEnumPlugOperator


class COLLISIONEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class COLLISIONEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class COLLISIONEnumField(
    EnumField[COLLISIONEnumAttrOperator, COLLISIONEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = COLLISIONEnumAttrOperator
    PLUG_CLS = COLLISIONEnumPlugOperator


class TypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    POLY = 0
    NURBS = 1
    CAPSULE = 2


class TypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    POLY = 0
    NURBS = 1
    CAPSULE = 2

    NAME_MAP = {
        POLY: "poly",
        NURBS: "nurbs",
        CAPSULE: "capsule",
    }


class TypeEnumField(
    EnumField[TypeEnumAttrOperator, TypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TypeEnumAttrOperator
    PLUG_CLS = TypeEnumPlugOperator


class CapsuleAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X_MINUS_AXIS = 0
    Y_MINUS_AXIS = 1
    Z_MINUS_AXIS = 2
    NEG_X_MINUS_AXIS = 3
    NEG_Y_MINUS_AXIS = 4
    NEG_Z_MINUS_AXIS = 5


class CapsuleAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X_MINUS_AXIS = 0
    Y_MINUS_AXIS = 1
    Z_MINUS_AXIS = 2
    NEG_X_MINUS_AXIS = 3
    NEG_Y_MINUS_AXIS = 4
    NEG_Z_MINUS_AXIS = 5

    NAME_MAP = {
        X_MINUS_AXIS: "X-Axis",
        Y_MINUS_AXIS: "Y-Axis",
        Z_MINUS_AXIS: "Z-Axis",
        NEG_X_MINUS_AXIS: "Neg X-Axis",
        NEG_Y_MINUS_AXIS: "Neg Y-Axis",
        NEG_Z_MINUS_AXIS: "Neg Z-Axis",
    }


class CapsuleAxisEnumField(
    EnumField[CapsuleAxisEnumAttrOperator, CapsuleAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CapsuleAxisEnumAttrOperator
    PLUG_CLS = CapsuleAxisEnumPlugOperator


class DirTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    VECTOR = 0
    RADIAL = 1


class DirTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    VECTOR = 0
    RADIAL = 1

    NAME_MAP = {
        VECTOR: "vector",
        RADIAL: "radial",
    }


class DirTypeEnumField(
    EnumField[DirTypeEnumAttrOperator, DirTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DirTypeEnumAttrOperator
    PLUG_CLS = DirTypeEnumPlugOperator


class DirAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X_MINUS_AXIS = 0
    Y_MINUS_AXIS = 1
    Z_MINUS_AXIS = 2
    NEG_X_MINUS_AXIS = 3
    NEG_Y_MINUS_AXIS = 4
    NEG_Z_MINUS_AXIS = 5


class DirAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X_MINUS_AXIS = 0
    Y_MINUS_AXIS = 1
    Z_MINUS_AXIS = 2
    NEG_X_MINUS_AXIS = 3
    NEG_Y_MINUS_AXIS = 4
    NEG_Z_MINUS_AXIS = 5

    NAME_MAP = {
        X_MINUS_AXIS: "X-Axis",
        Y_MINUS_AXIS: "Y-Axis",
        Z_MINUS_AXIS: "Z-Axis",
        NEG_X_MINUS_AXIS: "Neg X-Axis",
        NEG_Y_MINUS_AXIS: "Neg Y-Axis",
        NEG_Z_MINUS_AXIS: "Neg Z-Axis",
    }


class DirAxisEnumField(
    EnumField[DirAxisEnumAttrOperator, DirAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DirAxisEnumAttrOperator
    PLUG_CLS = DirAxisEnumPlugOperator


class ModeDispEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PLANAR = 0
    CYLINDRICAL = 1
    CURVES = 2


class ModeDispEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PLANAR = 0
    CYLINDRICAL = 1
    CURVES = 2

    NAME_MAP = {
        PLANAR: "planar",
        CYLINDRICAL: "cylindrical",
        CURVES: "curves",
    }


class ModeDispEnumField(
    EnumField[ModeDispEnumAttrOperator, ModeDispEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeDispEnumAttrOperator
    PLUG_CLS = ModeDispEnumPlugOperator


class PushModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 0
    GIZMO = 1


class PushModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 0
    GIZMO = 1

    NAME_MAP = {
        NORMAL: "normal",
        GIZMO: "gizmo",
    }


class PushModeEnumField(
    EnumField[PushModeEnumAttrOperator, PushModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PushModeEnumAttrOperator
    PLUG_CLS = PushModeEnumPlugOperator


class CombineModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MAX = 0
    ADD = 1


class CombineModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MAX = 0
    ADD = 1

    NAME_MAP = {
        MAX: "max",
        ADD: "add",
    }


class CombineModeEnumField(
    EnumField[CombineModeEnumAttrOperator, CombineModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CombineModeEnumAttrOperator
    PLUG_CLS = CombineModeEnumPlugOperator


class CollideModeSmartEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PLANE = 0
    MESH = 1


class CollideModeSmartEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PLANE = 0
    MESH = 1

    NAME_MAP = {
        PLANE: "plane",
        MESH: "mesh",
    }


class CollideModeSmartEnumField(
    EnumField[CollideModeSmartEnumAttrOperator, CollideModeSmartEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollideModeSmartEnumAttrOperator
    PLUG_CLS = CollideModeSmartEnumPlugOperator


class AxisSmartEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X_MINUS_AXIS = 0
    Y_MINUS_AXIS = 1
    Z_MINUS_AXIS = 2
    NEG_X_MINUS_AXIS = 3
    NEG_Y_MINUS_AXIS = 4
    NEG_Z_MINUS_AXIS = 5


class AxisSmartEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X_MINUS_AXIS = 0
    Y_MINUS_AXIS = 1
    Z_MINUS_AXIS = 2
    NEG_X_MINUS_AXIS = 3
    NEG_Y_MINUS_AXIS = 4
    NEG_Z_MINUS_AXIS = 5

    NAME_MAP = {
        X_MINUS_AXIS: "X-Axis",
        Y_MINUS_AXIS: "Y-Axis",
        Z_MINUS_AXIS: "Z-Axis",
        NEG_X_MINUS_AXIS: "Neg X-Axis",
        NEG_Y_MINUS_AXIS: "Neg Y-Axis",
        NEG_Z_MINUS_AXIS: "Neg Z-Axis",
    }


class AxisSmartEnumField(
    EnumField[AxisSmartEnumAttrOperator, AxisSmartEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisSmartEnumAttrOperator
    PLUG_CLS = AxisSmartEnumPlugOperator


class SMOOTH_PREEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class SMOOTH_PREEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class SMOOTH_PREEnumField(
    EnumField[SMOOTH_PREEnumAttrOperator, SMOOTH_PREEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SMOOTH_PREEnumAttrOperator
    PLUG_CLS = SMOOTH_PREEnumPlugOperator


class MOVEMENTEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class MOVEMENTEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class MOVEMENTEnumField(
    EnumField[MOVEMENTEnumAttrOperator, MOVEMENTEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MOVEMENTEnumAttrOperator
    PLUG_CLS = MOVEMENTEnumPlugOperator


class COLLISIONSMARTEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class COLLISIONSMARTEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class COLLISIONSMARTEnumField(
    EnumField[COLLISIONSMARTEnumAttrOperator, COLLISIONSMARTEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = COLLISIONSMARTEnumAttrOperator
    PLUG_CLS = COLLISIONSMARTEnumPlugOperator


class SMOOTH_POSTEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class SMOOTH_POSTEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class SMOOTH_POSTEnumField(
    EnumField[SMOOTH_POSTEnumAttrOperator, SMOOTH_POSTEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SMOOTH_POSTEnumAttrOperator
    PLUG_CLS = SMOOTH_POSTEnumPlugOperator


class InputPlugOperator(
    CompoundPlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputGeometry", "ig"),
        ("groupId", "gi"),
        ("componentTagExpression", "gtg"),
    )

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField()
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputAttrOperator(
    CompoundAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField()
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputField(
    CompoundField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator


class EnvelopeWeightsListPlugOperator(
    CompoundPlugOperator["EnvelopeWeightsListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("envelopeWeights", "owt"),
    )

    envelopeWeights = FloatField()
    owt = envelopeWeights


class EnvelopeWeightsListAttrOperator(
    CompoundAttrOperator[EnvelopeWeightsListPlugOperator]
):
    __slots__ = ()

    envelopeWeights = FloatField()
    owt = envelopeWeights


class EnvelopeWeightsListField(
    CompoundField[EnvelopeWeightsListAttrOperator, EnvelopeWeightsListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EnvelopeWeightsListAttrOperator
    PLUG_CLS = EnvelopeWeightsListPlugOperator


class FunctionPlugOperator(
    Long3CompoundBasePlugOperator["FunctionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fchild1", "f1"),
        ("fchild2", "f2"),
        ("fchild3", "f3"),
    )

    fchild1 = LongField()
    f1 = fchild1

    fchild2 = LongField()
    f2 = fchild2

    fchild3 = LongField()
    f3 = fchild3


class FunctionAttrOperator(
    Long3CompoundBaseAttrOperator[FunctionPlugOperator]
):
    __slots__ = ()

    fchild1 = LongField()
    f1 = fchild1

    fchild2 = LongField()
    f2 = fchild2

    fchild3 = LongField()
    f3 = fchild3


class FunctionField(
    Long3CompoundBaseField[FunctionAttrOperator, FunctionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FunctionAttrOperator
    PLUG_CLS = FunctionPlugOperator

    fchild1 = LongField()
    f1 = fchild1

    fchild2 = LongField()
    f2 = fchild2

    fchild3 = LongField()
    f3 = fchild3


class WeightListPlugOperator(
    CompoundPlugOperator["WeightListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weights", "wl.w"),
    )

    weights = FloatField()


class WeightListAttrOperator(
    CompoundAttrOperator[WeightListPlugOperator]
):
    __slots__ = ()

    weights = FloatField()


class WeightListField(
    CompoundField[WeightListAttrOperator, WeightListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListAttrOperator
    PLUG_CLS = WeightListPlugOperator


class UserDataPlugOperator(
    CompoundPlugOperator["UserDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inTime", "it"),
        ("cache", "cac"),
        ("cachePath", "cpath"),
        ("showWarnings", "swrn"),
        ("userScale", "usc"),
        ("STICKY", "LSTK"),
        ("enableSticky", "estk"),
        ("relativeSticky", "relstk"),
        ("forceNormalize", "frcnrm"),
        ("stickyA", "stka"),
        ("stickyB", "stkb"),
        ("stickyC", "stkc"),
        ("SLIDING", "LSLD"),
        ("enableSliding", "esld"),
        ("quality", "qlty"),
        ("shrinkWrap", "shr"),
        ("useBind", "ub"),
        ("allowNegFat", "anft"),
        ("DISPLACE", "LDSP"),
        ("enableDisplace", "edsp"),
        ("collisionDisplace", "clldsp"),
        ("FORCE", "LFRC"),
        ("enableForce", "efrc"),
        ("gravityStrength", "gravstr"),
        ("gravityX", "gravx"),
        ("gravityY", "gravy"),
        ("gravityZ", "gravz"),
        ("windStrength", "windstr"),
        ("windDirX", "windx"),
        ("windDirY", "windy"),
        ("windDirZ", "windz"),
        ("windSpeed", "windspd"),
        ("windNoise", "windnos"),
        ("windNoiseScale", "windnscl"),
        ("windNoiseDirty", "winddrt"),
        ("JIGGLE", "LJIG"),
        ("enableJiggle", "ejig"),
        ("jiggleCollisions", "jigcol"),
        ("resetFrame", "rf"),
        ("jiggleMin", "jmin"),
        ("jiggleMax", "jmax"),
        ("cycleMin", "cmin"),
        ("cycleMax", "cmax"),
        ("restMin", "rmin"),
        ("restMax", "rmax"),
        ("RELAX", "LRLX"),
        ("enableRelax", "erlx"),
        ("relaxMode", "rmod"),
        ("relaxCollisions", "rcll"),
        ("relaxIterations", "ritr"),
        ("relaxStrength", "rstr"),
        ("wrinkleStrength", "wrstr"),
        ("relaxCompress", "rcmp"),
        ("relaxExpand", "rexp"),
        ("relaxFriction", "rfrc"),
        ("SMOOTH", "SMTH"),
        ("enableSmooth", "esmth"),
        ("smoothCollisions", "scll"),
        ("smoothIterations", "sitr"),
        ("smoothStrength", "sstr"),
        ("smoothCompress", "scmp"),
        ("smoothExpand", "sexp"),
        ("smoothHold", "shld"),
        ("COLLISION", "COLL"),
        ("smartCollision", "smrtcll"),
        ("selfCollision", "slfcll"),
        ("selfTolerance", "slftol"),
        ("selfFalloff", "slffal"),
        ("selfVolumize", "slfvol"),
        ("selfBlurIterations", "slfblrit"),
        ("selfRelaxIterations", "slfrxi"),
        ("selfRelaxStrength", "slfrxstr"),
        ("selfSmoothIterations", "slfsmi"),
        ("selfSmoothStrength", "slfsmstr"),
        ("selfSmoothHold", "slfhld"),
    )

    inTime = DoubleField()
    it = inTime

    cache = CacheEnumField()
    cac = cache

    cachePath = DataStringField()
    cpath = cachePath

    showWarnings = BoolField()
    swrn = showWarnings

    userScale = CompoundField()
    usc = userScale

    STICKY = STICKYEnumField()
    LSTK = STICKY

    enableSticky = BoolField()
    estk = enableSticky

    relativeSticky = RelativeStickyEnumField()
    relstk = relativeSticky

    forceNormalize = BoolField()
    frcnrm = forceNormalize

    stickyA = DoubleField()
    stka = stickyA

    stickyB = DoubleField()
    stkb = stickyB

    stickyC = DoubleField()
    stkc = stickyC

    SLIDING = SLIDINGEnumField()
    LSLD = SLIDING

    enableSliding = BoolField()
    esld = enableSliding

    quality = QualityEnumField()
    qlty = quality

    shrinkWrap = BoolField()
    shr = shrinkWrap

    useBind = BoolField()
    ub = useBind

    allowNegFat = BoolField()
    anft = allowNegFat

    DISPLACE = DISPLACEEnumField()
    LDSP = DISPLACE

    enableDisplace = BoolField()
    edsp = enableDisplace

    collisionDisplace = BoolField()
    clldsp = collisionDisplace

    FORCE = FORCEEnumField()
    LFRC = FORCE

    enableForce = BoolField()
    efrc = enableForce

    gravityStrength = DoubleField()
    gravstr = gravityStrength

    gravityX = DoubleField()
    gravx = gravityX

    gravityY = DoubleField()
    gravy = gravityY

    gravityZ = DoubleField()
    gravz = gravityZ

    windStrength = DoubleField()
    windstr = windStrength

    windDirX = DoubleField()
    windx = windDirX

    windDirY = DoubleField()
    windy = windDirY

    windDirZ = DoubleField()
    windz = windDirZ

    windSpeed = DoubleField()
    windspd = windSpeed

    windNoise = DoubleField()
    windnos = windNoise

    windNoiseScale = DoubleField()
    windnscl = windNoiseScale

    windNoiseDirty = LongField()
    winddrt = windNoiseDirty

    JIGGLE = JIGGLEEnumField()
    LJIG = JIGGLE

    enableJiggle = BoolField()
    ejig = enableJiggle

    jiggleCollisions = BoolField()
    jigcol = jiggleCollisions

    resetFrame = DoubleField()
    rf = resetFrame

    jiggleMin = DoubleField()
    jmin = jiggleMin

    jiggleMax = DoubleField()
    jmax = jiggleMax

    cycleMin = DoubleField()
    cmin = cycleMin

    cycleMax = DoubleField()
    cmax = cycleMax

    restMin = DoubleField()
    rmin = restMin

    restMax = DoubleField()
    rmax = restMax

    RELAX = RELAXEnumField()
    LRLX = RELAX

    enableRelax = BoolField()
    erlx = enableRelax

    relaxMode = RelaxModeEnumField()
    rmod = relaxMode

    relaxCollisions = BoolField()
    rcll = relaxCollisions

    relaxIterations = LongField()
    ritr = relaxIterations

    relaxStrength = DoubleField()
    rstr = relaxStrength

    wrinkleStrength = DoubleField()
    wrstr = wrinkleStrength

    relaxCompress = DoubleField()
    rcmp = relaxCompress

    relaxExpand = DoubleField()
    rexp = relaxExpand

    relaxFriction = DoubleField()
    rfrc = relaxFriction

    SMOOTH = SMOOTHEnumField()
    SMTH = SMOOTH

    enableSmooth = BoolField()
    esmth = enableSmooth

    smoothCollisions = BoolField()
    scll = smoothCollisions

    smoothIterations = LongField()
    sitr = smoothIterations

    smoothStrength = DoubleField()
    sstr = smoothStrength

    smoothCompress = DoubleField()
    scmp = smoothCompress

    smoothExpand = DoubleField()
    sexp = smoothExpand

    smoothHold = DoubleField()
    shld = smoothHold

    COLLISION = COLLISIONEnumField()
    COLL = COLLISION

    smartCollision = BoolField()
    smrtcll = smartCollision

    selfCollision = BoolField()
    slfcll = selfCollision

    selfTolerance = DoubleField()
    slftol = selfTolerance

    selfFalloff = DoubleField()
    slffal = selfFalloff

    selfVolumize = DoubleField()
    slfvol = selfVolumize

    selfBlurIterations = LongField()
    slfblrit = selfBlurIterations

    selfRelaxIterations = LongField()
    slfrxi = selfRelaxIterations

    selfRelaxStrength = DoubleField()
    slfrxstr = selfRelaxStrength

    selfSmoothIterations = LongField()
    slfsmi = selfSmoothIterations

    selfSmoothStrength = DoubleField()
    slfsmstr = selfSmoothStrength

    selfSmoothHold = DoubleField()
    slfhld = selfSmoothHold


class UserDataAttrOperator(
    CompoundAttrOperator[UserDataPlugOperator]
):
    __slots__ = ()

    inTime = DoubleField()
    it = inTime

    cache = CacheEnumField()
    cac = cache

    cachePath = DataStringField()
    cpath = cachePath

    showWarnings = BoolField()
    swrn = showWarnings

    userScale = CompoundField()
    usc = userScale

    STICKY = STICKYEnumField()
    LSTK = STICKY

    enableSticky = BoolField()
    estk = enableSticky

    relativeSticky = RelativeStickyEnumField()
    relstk = relativeSticky

    forceNormalize = BoolField()
    frcnrm = forceNormalize

    stickyA = DoubleField()
    stka = stickyA

    stickyB = DoubleField()
    stkb = stickyB

    stickyC = DoubleField()
    stkc = stickyC

    SLIDING = SLIDINGEnumField()
    LSLD = SLIDING

    enableSliding = BoolField()
    esld = enableSliding

    quality = QualityEnumField()
    qlty = quality

    shrinkWrap = BoolField()
    shr = shrinkWrap

    useBind = BoolField()
    ub = useBind

    allowNegFat = BoolField()
    anft = allowNegFat

    DISPLACE = DISPLACEEnumField()
    LDSP = DISPLACE

    enableDisplace = BoolField()
    edsp = enableDisplace

    collisionDisplace = BoolField()
    clldsp = collisionDisplace

    FORCE = FORCEEnumField()
    LFRC = FORCE

    enableForce = BoolField()
    efrc = enableForce

    gravityStrength = DoubleField()
    gravstr = gravityStrength

    gravityX = DoubleField()
    gravx = gravityX

    gravityY = DoubleField()
    gravy = gravityY

    gravityZ = DoubleField()
    gravz = gravityZ

    windStrength = DoubleField()
    windstr = windStrength

    windDirX = DoubleField()
    windx = windDirX

    windDirY = DoubleField()
    windy = windDirY

    windDirZ = DoubleField()
    windz = windDirZ

    windSpeed = DoubleField()
    windspd = windSpeed

    windNoise = DoubleField()
    windnos = windNoise

    windNoiseScale = DoubleField()
    windnscl = windNoiseScale

    windNoiseDirty = LongField()
    winddrt = windNoiseDirty

    JIGGLE = JIGGLEEnumField()
    LJIG = JIGGLE

    enableJiggle = BoolField()
    ejig = enableJiggle

    jiggleCollisions = BoolField()
    jigcol = jiggleCollisions

    resetFrame = DoubleField()
    rf = resetFrame

    jiggleMin = DoubleField()
    jmin = jiggleMin

    jiggleMax = DoubleField()
    jmax = jiggleMax

    cycleMin = DoubleField()
    cmin = cycleMin

    cycleMax = DoubleField()
    cmax = cycleMax

    restMin = DoubleField()
    rmin = restMin

    restMax = DoubleField()
    rmax = restMax

    RELAX = RELAXEnumField()
    LRLX = RELAX

    enableRelax = BoolField()
    erlx = enableRelax

    relaxMode = RelaxModeEnumField()
    rmod = relaxMode

    relaxCollisions = BoolField()
    rcll = relaxCollisions

    relaxIterations = LongField()
    ritr = relaxIterations

    relaxStrength = DoubleField()
    rstr = relaxStrength

    wrinkleStrength = DoubleField()
    wrstr = wrinkleStrength

    relaxCompress = DoubleField()
    rcmp = relaxCompress

    relaxExpand = DoubleField()
    rexp = relaxExpand

    relaxFriction = DoubleField()
    rfrc = relaxFriction

    SMOOTH = SMOOTHEnumField()
    SMTH = SMOOTH

    enableSmooth = BoolField()
    esmth = enableSmooth

    smoothCollisions = BoolField()
    scll = smoothCollisions

    smoothIterations = LongField()
    sitr = smoothIterations

    smoothStrength = DoubleField()
    sstr = smoothStrength

    smoothCompress = DoubleField()
    scmp = smoothCompress

    smoothExpand = DoubleField()
    sexp = smoothExpand

    smoothHold = DoubleField()
    shld = smoothHold

    COLLISION = COLLISIONEnumField()
    COLL = COLLISION

    smartCollision = BoolField()
    smrtcll = smartCollision

    selfCollision = BoolField()
    slfcll = selfCollision

    selfTolerance = DoubleField()
    slftol = selfTolerance

    selfFalloff = DoubleField()
    slffal = selfFalloff

    selfVolumize = DoubleField()
    slfvol = selfVolumize

    selfBlurIterations = LongField()
    slfblrit = selfBlurIterations

    selfRelaxIterations = LongField()
    slfrxi = selfRelaxIterations

    selfRelaxStrength = DoubleField()
    slfrxstr = selfRelaxStrength

    selfSmoothIterations = LongField()
    slfsmi = selfSmoothIterations

    selfSmoothStrength = DoubleField()
    slfsmstr = selfSmoothStrength

    selfSmoothHold = DoubleField()
    slfhld = selfSmoothHold


class UserDataField(
    CompoundField[UserDataAttrOperator, UserDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UserDataAttrOperator
    PLUG_CLS = UserDataPlugOperator

    inTime = DoubleField()
    it = inTime

    cache = CacheEnumField()
    cac = cache

    cachePath = DataStringField()
    cpath = cachePath

    showWarnings = BoolField()
    swrn = showWarnings

    userScale = CompoundField()
    usc = userScale

    STICKY = STICKYEnumField()
    LSTK = STICKY

    enableSticky = BoolField()
    estk = enableSticky

    relativeSticky = RelativeStickyEnumField()
    relstk = relativeSticky

    forceNormalize = BoolField()
    frcnrm = forceNormalize

    stickyA = DoubleField()
    stka = stickyA

    stickyB = DoubleField()
    stkb = stickyB

    stickyC = DoubleField()
    stkc = stickyC

    SLIDING = SLIDINGEnumField()
    LSLD = SLIDING

    enableSliding = BoolField()
    esld = enableSliding

    quality = QualityEnumField()
    qlty = quality

    shrinkWrap = BoolField()
    shr = shrinkWrap

    useBind = BoolField()
    ub = useBind

    allowNegFat = BoolField()
    anft = allowNegFat

    DISPLACE = DISPLACEEnumField()
    LDSP = DISPLACE

    enableDisplace = BoolField()
    edsp = enableDisplace

    collisionDisplace = BoolField()
    clldsp = collisionDisplace

    FORCE = FORCEEnumField()
    LFRC = FORCE

    enableForce = BoolField()
    efrc = enableForce

    gravityStrength = DoubleField()
    gravstr = gravityStrength

    gravityX = DoubleField()
    gravx = gravityX

    gravityY = DoubleField()
    gravy = gravityY

    gravityZ = DoubleField()
    gravz = gravityZ

    windStrength = DoubleField()
    windstr = windStrength

    windDirX = DoubleField()
    windx = windDirX

    windDirY = DoubleField()
    windy = windDirY

    windDirZ = DoubleField()
    windz = windDirZ

    windSpeed = DoubleField()
    windspd = windSpeed

    windNoise = DoubleField()
    windnos = windNoise

    windNoiseScale = DoubleField()
    windnscl = windNoiseScale

    windNoiseDirty = LongField()
    winddrt = windNoiseDirty

    JIGGLE = JIGGLEEnumField()
    LJIG = JIGGLE

    enableJiggle = BoolField()
    ejig = enableJiggle

    jiggleCollisions = BoolField()
    jigcol = jiggleCollisions

    resetFrame = DoubleField()
    rf = resetFrame

    jiggleMin = DoubleField()
    jmin = jiggleMin

    jiggleMax = DoubleField()
    jmax = jiggleMax

    cycleMin = DoubleField()
    cmin = cycleMin

    cycleMax = DoubleField()
    cmax = cycleMax

    restMin = DoubleField()
    rmin = restMin

    restMax = DoubleField()
    rmax = restMax

    RELAX = RELAXEnumField()
    LRLX = RELAX

    enableRelax = BoolField()
    erlx = enableRelax

    relaxMode = RelaxModeEnumField()
    rmod = relaxMode

    relaxCollisions = BoolField()
    rcll = relaxCollisions

    relaxIterations = LongField()
    ritr = relaxIterations

    relaxStrength = DoubleField()
    rstr = relaxStrength

    wrinkleStrength = DoubleField()
    wrstr = wrinkleStrength

    relaxCompress = DoubleField()
    rcmp = relaxCompress

    relaxExpand = DoubleField()
    rexp = relaxExpand

    relaxFriction = DoubleField()
    rfrc = relaxFriction

    SMOOTH = SMOOTHEnumField()
    SMTH = SMOOTH

    enableSmooth = BoolField()
    esmth = enableSmooth

    smoothCollisions = BoolField()
    scll = smoothCollisions

    smoothIterations = LongField()
    sitr = smoothIterations

    smoothStrength = DoubleField()
    sstr = smoothStrength

    smoothCompress = DoubleField()
    scmp = smoothCompress

    smoothExpand = DoubleField()
    sexp = smoothExpand

    smoothHold = DoubleField()
    shld = smoothHold

    COLLISION = COLLISIONEnumField()
    COLL = COLLISION

    smartCollision = BoolField()
    smrtcll = smartCollision

    selfCollision = BoolField()
    slfcll = selfCollision

    selfTolerance = DoubleField()
    slftol = selfTolerance

    selfFalloff = DoubleField()
    slffal = selfFalloff

    selfVolumize = DoubleField()
    slfvol = selfVolumize

    selfBlurIterations = LongField()
    slfblrit = selfBlurIterations

    selfRelaxIterations = LongField()
    slfrxi = selfRelaxIterations

    selfRelaxStrength = DoubleField()
    slfrxstr = selfRelaxStrength

    selfSmoothIterations = LongField()
    slfsmi = selfSmoothIterations

    selfSmoothStrength = DoubleField()
    slfsmstr = selfSmoothStrength

    selfSmoothHold = DoubleField()
    slfhld = selfSmoothHold


class MuscleDataPlugOperator(
    CompoundPlugOperator["MuscleDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldMatrixStart", "wms"),
        ("worldMatrixEnd", "wme"),
        ("worldMatrixStartBase", "wmsb"),
        ("worldMatrixEndBase", "wmeb"),
        ("meshIn", "mesh"),
        ("meshInBase", "meshb"),
        ("stickyStrength", "stkstr"),
        ("slidingStrength", "sldstr"),
        ("fat", "ft"),
        ("reverseNormals", "rn"),
        ("type", "typ"),
        ("radius", "rad"),
        ("length", "len"),
        ("capsuleAxis", "cax"),
        ("relative", "rel"),
        ("lockStickyWt", "lkst"),
        ("lockSlidingWt", "lksl"),
        ("affectSticky", "afstk"),
        ("affectSliding", "afsld"),
        ("userScaleMus", "uscmus"),
    )

    worldMatrixStart = MatrixField()
    wms = worldMatrixStart

    worldMatrixEnd = MatrixField()
    wme = worldMatrixEnd

    worldMatrixStartBase = MatrixField()
    wmsb = worldMatrixStartBase

    worldMatrixEndBase = MatrixField()
    wmeb = worldMatrixEndBase

    meshIn = GenericField()
    mesh = meshIn

    meshInBase = GenericField()
    meshb = meshInBase

    stickyStrength = DoubleField()
    stkstr = stickyStrength

    slidingStrength = DoubleField()
    sldstr = slidingStrength

    fat = DoubleField()
    ft = fat

    reverseNormals = BoolField()
    rn = reverseNormals

    type = TypeEnumField()
    typ = type

    radius = DoubleField()
    rad = radius

    length = DoubleField()
    len = length

    capsuleAxis = CapsuleAxisEnumField()
    cax = capsuleAxis

    relative = BoolField()
    rel = relative

    lockStickyWt = BoolField()
    lkst = lockStickyWt

    lockSlidingWt = BoolField()
    lksl = lockSlidingWt

    affectSticky = BoolField()
    afstk = affectSticky

    affectSliding = BoolField()
    afsld = affectSliding

    userScaleMus = CompoundField()
    uscmus = userScaleMus


class MuscleDataAttrOperator(
    CompoundAttrOperator[MuscleDataPlugOperator]
):
    __slots__ = ()

    worldMatrixStart = MatrixField()
    wms = worldMatrixStart

    worldMatrixEnd = MatrixField()
    wme = worldMatrixEnd

    worldMatrixStartBase = MatrixField()
    wmsb = worldMatrixStartBase

    worldMatrixEndBase = MatrixField()
    wmeb = worldMatrixEndBase

    meshIn = GenericField()
    mesh = meshIn

    meshInBase = GenericField()
    meshb = meshInBase

    stickyStrength = DoubleField()
    stkstr = stickyStrength

    slidingStrength = DoubleField()
    sldstr = slidingStrength

    fat = DoubleField()
    ft = fat

    reverseNormals = BoolField()
    rn = reverseNormals

    type = TypeEnumField()
    typ = type

    radius = DoubleField()
    rad = radius

    length = DoubleField()
    len = length

    capsuleAxis = CapsuleAxisEnumField()
    cax = capsuleAxis

    relative = BoolField()
    rel = relative

    lockStickyWt = BoolField()
    lkst = lockStickyWt

    lockSlidingWt = BoolField()
    lksl = lockSlidingWt

    affectSticky = BoolField()
    afstk = affectSticky

    affectSliding = BoolField()
    afsld = affectSliding

    userScaleMus = CompoundField()
    uscmus = userScaleMus


class MuscleDataField(
    CompoundField[MuscleDataAttrOperator, MuscleDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MuscleDataAttrOperator
    PLUG_CLS = MuscleDataPlugOperator


class DirDataPlugOperator(
    CompoundPlugOperator["DirDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldMatrixDir", "wmd"),
        ("strengthDir", "strd"),
        ("falloffInnerDir", "fid"),
        ("falloffOuterDir", "fod"),
        ("dirType", "dirtyp"),
        ("dirLength", "dirlen"),
        ("dirAxis", "dax"),
        ("lockDirWt", "lkdi"),
    )

    worldMatrixDir = MatrixField()
    wmd = worldMatrixDir

    strengthDir = DoubleField()
    strd = strengthDir

    falloffInnerDir = DoubleField()
    fid = falloffInnerDir

    falloffOuterDir = DoubleField()
    fod = falloffOuterDir

    dirType = DirTypeEnumField()
    dirtyp = dirType

    dirLength = DoubleField()
    dirlen = dirLength

    dirAxis = DirAxisEnumField()
    dax = dirAxis

    lockDirWt = BoolField()
    lkdi = lockDirWt


class DirDataAttrOperator(
    CompoundAttrOperator[DirDataPlugOperator]
):
    __slots__ = ()

    worldMatrixDir = MatrixField()
    wmd = worldMatrixDir

    strengthDir = DoubleField()
    strd = strengthDir

    falloffInnerDir = DoubleField()
    fid = falloffInnerDir

    falloffOuterDir = DoubleField()
    fod = falloffOuterDir

    dirType = DirTypeEnumField()
    dirtyp = dirType

    dirLength = DoubleField()
    dirlen = dirLength

    dirAxis = DirAxisEnumField()
    dax = dirAxis

    lockDirWt = BoolField()
    lkdi = lockDirWt


class DirDataField(
    CompoundField[DirDataAttrOperator, DirDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DirDataAttrOperator
    PLUG_CLS = DirDataPlugOperator


class DispDataPlugOperator(
    CompoundPlugOperator["DispDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldMatrixDisp", "wmdsp"),
        ("curves", "crv"),
        ("modeDisp", "mdd"),
        ("lengthDisp", "lend"),
        ("sizeRadiusDisp", "sizd"),
        ("amplitudeDisp", "ampd"),
        ("falloffDisp", "fald"),
        ("pushMode", "pmd"),
        ("combineMode", "cmd"),
        ("shader", "sha"),
    )

    worldMatrixDisp = MatrixField()
    wmdsp = worldMatrixDisp

    curves = GenericField()
    crv = curves

    modeDisp = ModeDispEnumField()
    mdd = modeDisp

    lengthDisp = FloatField()
    lend = lengthDisp

    sizeRadiusDisp = FloatField()
    sizd = sizeRadiusDisp

    amplitudeDisp = FloatField()
    ampd = amplitudeDisp

    falloffDisp = FloatField()
    fald = falloffDisp

    pushMode = PushModeEnumField()
    pmd = pushMode

    combineMode = CombineModeEnumField()
    cmd = combineMode

    shader = MessageField()
    sha = shader


class DispDataAttrOperator(
    CompoundAttrOperator[DispDataPlugOperator]
):
    __slots__ = ()

    worldMatrixDisp = MatrixField()
    wmdsp = worldMatrixDisp

    curves = GenericField()
    crv = curves

    modeDisp = ModeDispEnumField()
    mdd = modeDisp

    lengthDisp = FloatField()
    lend = lengthDisp

    sizeRadiusDisp = FloatField()
    sizd = sizeRadiusDisp

    amplitudeDisp = FloatField()
    ampd = amplitudeDisp

    falloffDisp = FloatField()
    fald = falloffDisp

    pushMode = PushModeEnumField()
    pmd = pushMode

    combineMode = CombineModeEnumField()
    cmd = combineMode

    shader = MessageField()
    sha = shader


class DispDataField(
    CompoundField[DispDataAttrOperator, DispDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DispDataAttrOperator
    PLUG_CLS = DispDataPlugOperator


class SmartCollideDataPlugOperator(
    CompoundPlugOperator["SmartCollideDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldMatrixASmart", "wmasmrt"),
        ("worldMatrixBSmart", "wmbsmrt"),
        ("worldMatrixASmartBase", "wmabsmrt"),
        ("worldMatrixBSmartBase", "wmbbsmrt"),
        ("worldMatrixPlaneSmart", "wmbplnsmrt"),
        ("worldMatrixPlaneSmartBase", "wmbplnbasesmrt"),
        ("enableSmart", "enasmrt"),
        ("collideModeSmart", "colmodsmrt"),
        ("axisSmart", "axsmrt"),
        ("triggerMin", "trgmin"),
        ("angleMinSmart", "angminsmrt"),
        ("angleMaxSmart", "angmaxsmrt"),
        ("biasSmart", "bissmrt"),
        ("biasAdjustSmart", "bisadjsmrt"),
        ("userScaleSmarr", "usrsclsmrt"),
        ("manualScaleSmarr", "mansclsmrt"),
        ("SMOOTH_PRE", "SMTHPRE"),
        ("smrtSmoothIterationsPre", "smrtsmipre"),
        ("smrtSmoothStrengthPre", "smrtsmstrpre"),
        ("smrtSmoothHoldPre", "smrthldpre"),
        ("MOVEMENT", "MOVE"),
        ("bulkASmart", "blkasmrt"),
        ("bulkBSmart", "blkbsmrt"),
        ("bulkAngularASmart", "blkaangsmrt"),
        ("bulkAngularBSmart", "blkangbsmrt"),
        ("bulkWidenASmart", "blkwidasmrt"),
        ("bulkWidenBSmart", "blkwidbsmrt"),
        ("slideSmartA", "sldasmrt"),
        ("slideSmartB", "sldbsmrt"),
        ("slideRearSmartA", "sldrerasmrt"),
        ("slideRearSmartB", "sldrerbsmrt"),
        ("slideAngularSmartA", "sldangasmrt"),
        ("slideAngularSmartB", "sldangbsmrt"),
        ("slideAngularRearSmartA", "sldangrerasmrt"),
        ("slideAngularRearSmartB", "sldangrerbsmrt"),
        ("wrinkleSmartA", "wrkasmrt"),
        ("wrinkleSmartB", "wrkbsmrt"),
        ("wrinkleSpreadSmart", "wrksprsmrt"),
        ("COLLISIONSMART", "COLLSMRT"),
        ("flattenSmartA", "fltasmrt"),
        ("flattenSmartB", "fltbsmrt"),
        ("rigidSmartA", "rigsmrta"),
        ("rigidSmartB", "rigsmrtb"),
        ("collisionBlurIterationsSmart", "colblritsmrt"),
        ("volumizeSmartA", "vlmasmrt"),
        ("volumizeSmartB", "vlmbsmrt"),
        ("volumizeOffsetSmartA", "vlmoffsmrt"),
        ("volumizePuffSmart", "vlmpufsmrt"),
        ("volumizeDistSmart", "vlmdsmrt"),
        ("volumizeFalloffSmart", "vlmfallsmrt"),
        ("SMOOTH_POST", "SMTHPST"),
        ("smrtSmoothIterationsPost", "smrtsmipst"),
        ("smrtSmoothStrengthPost", "smrtsmstrpst"),
        ("smrtSmoothHoldPost", "smrthldpst"),
        ("lockSmartWt", "lksmrt"),
    )

    worldMatrixASmart = MatrixField()
    wmasmrt = worldMatrixASmart

    worldMatrixBSmart = MatrixField()
    wmbsmrt = worldMatrixBSmart

    worldMatrixASmartBase = MatrixField()
    wmabsmrt = worldMatrixASmartBase

    worldMatrixBSmartBase = MatrixField()
    wmbbsmrt = worldMatrixBSmartBase

    worldMatrixPlaneSmart = MatrixField()
    wmbplnsmrt = worldMatrixPlaneSmart

    worldMatrixPlaneSmartBase = MatrixField()
    wmbplnbasesmrt = worldMatrixPlaneSmartBase

    enableSmart = BoolField()
    enasmrt = enableSmart

    collideModeSmart = CollideModeSmartEnumField()
    colmodsmrt = collideModeSmart

    axisSmart = AxisSmartEnumField()
    axsmrt = axisSmart

    triggerMin = DoubleField()
    trgmin = triggerMin

    angleMinSmart = DoubleField()
    angminsmrt = angleMinSmart

    angleMaxSmart = DoubleField()
    angmaxsmrt = angleMaxSmart

    biasSmart = DoubleField()
    bissmrt = biasSmart

    biasAdjustSmart = DoubleField()
    bisadjsmrt = biasAdjustSmart

    userScaleSmarr = DoubleField()
    usrsclsmrt = userScaleSmarr

    manualScaleSmarr = DoubleField()
    mansclsmrt = manualScaleSmarr

    SMOOTH_PRE = SMOOTH_PREEnumField()
    SMTHPRE = SMOOTH_PRE

    smrtSmoothIterationsPre = LongField()
    smrtsmipre = smrtSmoothIterationsPre

    smrtSmoothStrengthPre = DoubleField()
    smrtsmstrpre = smrtSmoothStrengthPre

    smrtSmoothHoldPre = DoubleField()
    smrthldpre = smrtSmoothHoldPre

    MOVEMENT = MOVEMENTEnumField()
    MOVE = MOVEMENT

    bulkASmart = DoubleField()
    blkasmrt = bulkASmart

    bulkBSmart = DoubleField()
    blkbsmrt = bulkBSmart

    bulkAngularASmart = DoubleField()
    blkaangsmrt = bulkAngularASmart

    bulkAngularBSmart = DoubleField()
    blkangbsmrt = bulkAngularBSmart

    bulkWidenASmart = DoubleField()
    blkwidasmrt = bulkWidenASmart

    bulkWidenBSmart = DoubleField()
    blkwidbsmrt = bulkWidenBSmart

    slideSmartA = DoubleField()
    sldasmrt = slideSmartA

    slideSmartB = DoubleField()
    sldbsmrt = slideSmartB

    slideRearSmartA = DoubleField()
    sldrerasmrt = slideRearSmartA

    slideRearSmartB = DoubleField()
    sldrerbsmrt = slideRearSmartB

    slideAngularSmartA = DoubleField()
    sldangasmrt = slideAngularSmartA

    slideAngularSmartB = DoubleField()
    sldangbsmrt = slideAngularSmartB

    slideAngularRearSmartA = DoubleField()
    sldangrerasmrt = slideAngularRearSmartA

    slideAngularRearSmartB = DoubleField()
    sldangrerbsmrt = slideAngularRearSmartB

    wrinkleSmartA = DoubleField()
    wrkasmrt = wrinkleSmartA

    wrinkleSmartB = DoubleField()
    wrkbsmrt = wrinkleSmartB

    wrinkleSpreadSmart = DoubleField()
    wrksprsmrt = wrinkleSpreadSmart

    COLLISIONSMART = COLLISIONSMARTEnumField()
    COLLSMRT = COLLISIONSMART

    flattenSmartA = DoubleField()
    fltasmrt = flattenSmartA

    flattenSmartB = DoubleField()
    fltbsmrt = flattenSmartB

    rigidSmartA = DoubleField()
    rigsmrta = rigidSmartA

    rigidSmartB = DoubleField()
    rigsmrtb = rigidSmartB

    collisionBlurIterationsSmart = LongField()
    colblritsmrt = collisionBlurIterationsSmart

    volumizeSmartA = DoubleField()
    vlmasmrt = volumizeSmartA

    volumizeSmartB = DoubleField()
    vlmbsmrt = volumizeSmartB

    volumizeOffsetSmartA = DoubleField()
    vlmoffsmrt = volumizeOffsetSmartA

    volumizePuffSmart = DoubleField()
    vlmpufsmrt = volumizePuffSmart

    volumizeDistSmart = DoubleField()
    vlmdsmrt = volumizeDistSmart

    volumizeFalloffSmart = DoubleField()
    vlmfallsmrt = volumizeFalloffSmart

    SMOOTH_POST = SMOOTH_POSTEnumField()
    SMTHPST = SMOOTH_POST

    smrtSmoothIterationsPost = LongField()
    smrtsmipst = smrtSmoothIterationsPost

    smrtSmoothStrengthPost = DoubleField()
    smrtsmstrpst = smrtSmoothStrengthPost

    smrtSmoothHoldPost = DoubleField()
    smrthldpst = smrtSmoothHoldPost

    lockSmartWt = BoolField()
    lksmrt = lockSmartWt


class SmartCollideDataAttrOperator(
    CompoundAttrOperator[SmartCollideDataPlugOperator]
):
    __slots__ = ()

    worldMatrixASmart = MatrixField()
    wmasmrt = worldMatrixASmart

    worldMatrixBSmart = MatrixField()
    wmbsmrt = worldMatrixBSmart

    worldMatrixASmartBase = MatrixField()
    wmabsmrt = worldMatrixASmartBase

    worldMatrixBSmartBase = MatrixField()
    wmbbsmrt = worldMatrixBSmartBase

    worldMatrixPlaneSmart = MatrixField()
    wmbplnsmrt = worldMatrixPlaneSmart

    worldMatrixPlaneSmartBase = MatrixField()
    wmbplnbasesmrt = worldMatrixPlaneSmartBase

    enableSmart = BoolField()
    enasmrt = enableSmart

    collideModeSmart = CollideModeSmartEnumField()
    colmodsmrt = collideModeSmart

    axisSmart = AxisSmartEnumField()
    axsmrt = axisSmart

    triggerMin = DoubleField()
    trgmin = triggerMin

    angleMinSmart = DoubleField()
    angminsmrt = angleMinSmart

    angleMaxSmart = DoubleField()
    angmaxsmrt = angleMaxSmart

    biasSmart = DoubleField()
    bissmrt = biasSmart

    biasAdjustSmart = DoubleField()
    bisadjsmrt = biasAdjustSmart

    userScaleSmarr = DoubleField()
    usrsclsmrt = userScaleSmarr

    manualScaleSmarr = DoubleField()
    mansclsmrt = manualScaleSmarr

    SMOOTH_PRE = SMOOTH_PREEnumField()
    SMTHPRE = SMOOTH_PRE

    smrtSmoothIterationsPre = LongField()
    smrtsmipre = smrtSmoothIterationsPre

    smrtSmoothStrengthPre = DoubleField()
    smrtsmstrpre = smrtSmoothStrengthPre

    smrtSmoothHoldPre = DoubleField()
    smrthldpre = smrtSmoothHoldPre

    MOVEMENT = MOVEMENTEnumField()
    MOVE = MOVEMENT

    bulkASmart = DoubleField()
    blkasmrt = bulkASmart

    bulkBSmart = DoubleField()
    blkbsmrt = bulkBSmart

    bulkAngularASmart = DoubleField()
    blkaangsmrt = bulkAngularASmart

    bulkAngularBSmart = DoubleField()
    blkangbsmrt = bulkAngularBSmart

    bulkWidenASmart = DoubleField()
    blkwidasmrt = bulkWidenASmart

    bulkWidenBSmart = DoubleField()
    blkwidbsmrt = bulkWidenBSmart

    slideSmartA = DoubleField()
    sldasmrt = slideSmartA

    slideSmartB = DoubleField()
    sldbsmrt = slideSmartB

    slideRearSmartA = DoubleField()
    sldrerasmrt = slideRearSmartA

    slideRearSmartB = DoubleField()
    sldrerbsmrt = slideRearSmartB

    slideAngularSmartA = DoubleField()
    sldangasmrt = slideAngularSmartA

    slideAngularSmartB = DoubleField()
    sldangbsmrt = slideAngularSmartB

    slideAngularRearSmartA = DoubleField()
    sldangrerasmrt = slideAngularRearSmartA

    slideAngularRearSmartB = DoubleField()
    sldangrerbsmrt = slideAngularRearSmartB

    wrinkleSmartA = DoubleField()
    wrkasmrt = wrinkleSmartA

    wrinkleSmartB = DoubleField()
    wrkbsmrt = wrinkleSmartB

    wrinkleSpreadSmart = DoubleField()
    wrksprsmrt = wrinkleSpreadSmart

    COLLISIONSMART = COLLISIONSMARTEnumField()
    COLLSMRT = COLLISIONSMART

    flattenSmartA = DoubleField()
    fltasmrt = flattenSmartA

    flattenSmartB = DoubleField()
    fltbsmrt = flattenSmartB

    rigidSmartA = DoubleField()
    rigsmrta = rigidSmartA

    rigidSmartB = DoubleField()
    rigsmrtb = rigidSmartB

    collisionBlurIterationsSmart = LongField()
    colblritsmrt = collisionBlurIterationsSmart

    volumizeSmartA = DoubleField()
    vlmasmrt = volumizeSmartA

    volumizeSmartB = DoubleField()
    vlmbsmrt = volumizeSmartB

    volumizeOffsetSmartA = DoubleField()
    vlmoffsmrt = volumizeOffsetSmartA

    volumizePuffSmart = DoubleField()
    vlmpufsmrt = volumizePuffSmart

    volumizeDistSmart = DoubleField()
    vlmdsmrt = volumizeDistSmart

    volumizeFalloffSmart = DoubleField()
    vlmfallsmrt = volumizeFalloffSmart

    SMOOTH_POST = SMOOTH_POSTEnumField()
    SMTHPST = SMOOTH_POST

    smrtSmoothIterationsPost = LongField()
    smrtsmipst = smrtSmoothIterationsPost

    smrtSmoothStrengthPost = DoubleField()
    smrtsmstrpst = smrtSmoothStrengthPost

    smrtSmoothHoldPost = DoubleField()
    smrthldpst = smrtSmoothHoldPost

    lockSmartWt = BoolField()
    lksmrt = lockSmartWt


class SmartCollideDataField(
    CompoundField[SmartCollideDataAttrOperator, SmartCollideDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SmartCollideDataAttrOperator
    PLUG_CLS = SmartCollideDataPlugOperator


class SelfCollideDataPlugOperator(
    CompoundPlugOperator["SelfCollideDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("selfName", "slfnam"),
        ("selfPtsA", "slfpta"),
        ("selfPtsB", "slfptb"),
    )

    selfName = DataStringField()
    slfnam = selfName

    selfPtsA = LongField()
    slfpta = selfPtsA

    selfPtsB = LongField()
    slfptb = selfPtsB


class SelfCollideDataAttrOperator(
    CompoundAttrOperator[SelfCollideDataPlugOperator]
):
    __slots__ = ()

    selfName = DataStringField()
    slfnam = selfName

    selfPtsA = LongField()
    slfpta = selfPtsA

    selfPtsB = LongField()
    slfptb = selfPtsB


class SelfCollideDataField(
    CompoundField[SelfCollideDataAttrOperator, SelfCollideDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SelfCollideDataAttrOperator
    PLUG_CLS = SelfCollideDataPlugOperator


class RelaxDataPlugOperator(
    CompoundPlugOperator["RelaxDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("numStretch", "nstr"),
        ("numBend", "nbnd"),
        ("relaxSt", "relst"),
        ("relaxBd", "relbd"),
        ("numCons", "ncns"),
        ("numPts", "npts"),
        ("ptsBase", "ptsBS"),
        ("numTri", "ntri"),
        ("relaxTri", "reltri"),
    )

    numStretch = LongField()
    nstr = numStretch

    numBend = LongField()
    nbnd = numBend

    relaxSt = CompoundField()
    relst = relaxSt

    relaxBd = CompoundField()
    relbd = relaxBd

    numCons = DoubleField()
    ncns = numCons

    numPts = LongField()
    npts = numPts

    ptsBase = CompoundField()
    ptsBS = ptsBase

    numTri = LongField()
    ntri = numTri

    relaxTri = CompoundField()
    reltri = relaxTri


class RelaxDataAttrOperator(
    CompoundAttrOperator[RelaxDataPlugOperator]
):
    __slots__ = ()

    numStretch = LongField()
    nstr = numStretch

    numBend = LongField()
    nbnd = numBend

    relaxSt = CompoundField()
    relst = relaxSt

    relaxBd = CompoundField()
    relbd = relaxBd

    numCons = DoubleField()
    ncns = numCons

    numPts = LongField()
    npts = numPts

    ptsBase = CompoundField()
    ptsBS = ptsBase

    numTri = LongField()
    ntri = numTri

    relaxTri = CompoundField()
    reltri = relaxTri


class RelaxDataField(
    CompoundField[RelaxDataAttrOperator, RelaxDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RelaxDataAttrOperator
    PLUG_CLS = RelaxDataPlugOperator

    numStretch = LongField()
    nstr = numStretch

    numBend = LongField()
    nbnd = numBend

    relaxSt = CompoundField()
    relst = relaxSt

    relaxBd = CompoundField()
    relbd = relaxBd

    numCons = DoubleField()
    ncns = numCons

    numPts = LongField()
    npts = numPts

    ptsBase = CompoundField()
    ptsBS = ptsBase

    numTri = LongField()
    ntri = numTri

    relaxTri = CompoundField()
    reltri = relaxTri


class RelativePointPlugOperator(
    CompoundPlugOperator["RelativePointAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("relativePointX", "relpx"),
        ("relativePointY", "relpy"),
        ("relativePointZ", "relpz"),
    )

    relativePointX = DoubleField()
    relpx = relativePointX

    relativePointY = DoubleField()
    relpy = relativePointY

    relativePointZ = DoubleField()
    relpz = relativePointZ


class RelativePointAttrOperator(
    CompoundAttrOperator[RelativePointPlugOperator]
):
    __slots__ = ()

    relativePointX = DoubleField()
    relpx = relativePointX

    relativePointY = DoubleField()
    relpy = relativePointY

    relativePointZ = DoubleField()
    relpz = relativePointZ


class RelativePointField(
    CompoundField[RelativePointAttrOperator, RelativePointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RelativePointAttrOperator
    PLUG_CLS = RelativePointPlugOperator


class SmoothDataPlugOperator(
    CompoundPlugOperator["SmoothDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("smoothEntry", "smte"),
        ("ptToPtEntry", "ptpe"),
    )

    smoothEntry = CompoundField()
    smte = smoothEntry

    ptToPtEntry = CompoundField()
    ptpe = ptToPtEntry


class SmoothDataAttrOperator(
    CompoundAttrOperator[SmoothDataPlugOperator]
):
    __slots__ = ()

    smoothEntry = CompoundField()
    smte = smoothEntry

    ptToPtEntry = CompoundField()
    ptpe = ptToPtEntry


class SmoothDataField(
    CompoundField[SmoothDataAttrOperator, SmoothDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SmoothDataAttrOperator
    PLUG_CLS = SmoothDataPlugOperator

    smoothEntry = CompoundField()
    smte = smoothEntry

    ptToPtEntry = CompoundField()
    ptpe = ptToPtEntry


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


class CacheFramePlugOperator(
    CompoundPlugOperator["CacheFrameAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cachePos", "cpos"),
    )

    cachePos = CompoundField()
    cpos = cachePos


class CacheFrameAttrOperator(
    CompoundAttrOperator[CacheFramePlugOperator]
):
    __slots__ = ()

    cachePos = CompoundField()
    cpos = cachePos


class CacheFrameField(
    CompoundField[CacheFrameAttrOperator, CacheFramePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CacheFrameAttrOperator
    PLUG_CLS = CacheFramePlugOperator


class WeightListMusPlugOperator(
    CompoundPlugOperator["WeightListMusAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weightsMus", "wtm"),
    )

    weightsMus = DoubleField()
    wtm = weightsMus


class WeightListMusAttrOperator(
    CompoundAttrOperator[WeightListMusPlugOperator]
):
    __slots__ = ()

    weightsMus = DoubleField()
    wtm = weightsMus


class WeightListMusField(
    CompoundField[WeightListMusAttrOperator, WeightListMusPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListMusAttrOperator
    PLUG_CLS = WeightListMusPlugOperator


class StickyWeightListMusPlugOperator(
    CompoundPlugOperator["StickyWeightListMusAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("stickyWeightsMus", "stkwtm"),
    )

    stickyWeightsMus = DoubleField()
    stkwtm = stickyWeightsMus


class StickyWeightListMusAttrOperator(
    CompoundAttrOperator[StickyWeightListMusPlugOperator]
):
    __slots__ = ()

    stickyWeightsMus = DoubleField()
    stkwtm = stickyWeightsMus


class StickyWeightListMusField(
    CompoundField[StickyWeightListMusAttrOperator, StickyWeightListMusPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StickyWeightListMusAttrOperator
    PLUG_CLS = StickyWeightListMusPlugOperator


class StickyWeightListMusBPlugOperator(
    CompoundPlugOperator["StickyWeightListMusBAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("stickyWeightsMusB", "stkwtmb"),
    )

    stickyWeightsMusB = DoubleField()
    stkwtmb = stickyWeightsMusB


class StickyWeightListMusBAttrOperator(
    CompoundAttrOperator[StickyWeightListMusBPlugOperator]
):
    __slots__ = ()

    stickyWeightsMusB = DoubleField()
    stkwtmb = stickyWeightsMusB


class StickyWeightListMusBField(
    CompoundField[StickyWeightListMusBAttrOperator, StickyWeightListMusBPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StickyWeightListMusBAttrOperator
    PLUG_CLS = StickyWeightListMusBPlugOperator


class StickyWeightListMusCPlugOperator(
    CompoundPlugOperator["StickyWeightListMusCAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("stickyWeightsMusC", "stkwtmc"),
    )

    stickyWeightsMusC = DoubleField()
    stkwtmc = stickyWeightsMusC


class StickyWeightListMusCAttrOperator(
    CompoundAttrOperator[StickyWeightListMusCPlugOperator]
):
    __slots__ = ()

    stickyWeightsMusC = DoubleField()
    stkwtmc = stickyWeightsMusC


class StickyWeightListMusCField(
    CompoundField[StickyWeightListMusCAttrOperator, StickyWeightListMusCPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StickyWeightListMusCAttrOperator
    PLUG_CLS = StickyWeightListMusCPlugOperator


class StickyListPlugOperator(
    CompoundPlugOperator["StickyListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("stickyData", "stkData"),
    )

    stickyData = CompoundField()
    stkData = stickyData


class StickyListAttrOperator(
    CompoundAttrOperator[StickyListPlugOperator]
):
    __slots__ = ()

    stickyData = CompoundField()
    stkData = stickyData


class StickyListField(
    CompoundField[StickyListAttrOperator, StickyListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StickyListAttrOperator
    PLUG_CLS = StickyListPlugOperator


class WeightListDirPlugOperator(
    CompoundPlugOperator["WeightListDirAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weightsDir", "wtd"),
    )

    weightsDir = DoubleField()
    wtd = weightsDir


class WeightListDirAttrOperator(
    CompoundAttrOperator[WeightListDirPlugOperator]
):
    __slots__ = ()

    weightsDir = DoubleField()
    wtd = weightsDir


class WeightListDirField(
    CompoundField[WeightListDirAttrOperator, WeightListDirPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListDirAttrOperator
    PLUG_CLS = WeightListDirPlugOperator


class WeightListSmartRegionAPlugOperator(
    CompoundPlugOperator["WeightListSmartRegionAAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weightsSmartRegionA", "wtsmrtrega"),
    )

    weightsSmartRegionA = DoubleField()
    wtsmrtrega = weightsSmartRegionA


class WeightListSmartRegionAAttrOperator(
    CompoundAttrOperator[WeightListSmartRegionAPlugOperator]
):
    __slots__ = ()

    weightsSmartRegionA = DoubleField()
    wtsmrtrega = weightsSmartRegionA


class WeightListSmartRegionAField(
    CompoundField[WeightListSmartRegionAAttrOperator, WeightListSmartRegionAPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartRegionAAttrOperator
    PLUG_CLS = WeightListSmartRegionAPlugOperator


class WeightListSmartRegionBPlugOperator(
    CompoundPlugOperator["WeightListSmartRegionBAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weightsSmartRegionB", "wtsmrtregb"),
    )

    weightsSmartRegionB = DoubleField()
    wtsmrtregb = weightsSmartRegionB


class WeightListSmartRegionBAttrOperator(
    CompoundAttrOperator[WeightListSmartRegionBPlugOperator]
):
    __slots__ = ()

    weightsSmartRegionB = DoubleField()
    wtsmrtregb = weightsSmartRegionB


class WeightListSmartRegionBField(
    CompoundField[WeightListSmartRegionBAttrOperator, WeightListSmartRegionBPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartRegionBAttrOperator
    PLUG_CLS = WeightListSmartRegionBPlugOperator


class WeightListSmartBulkPlugOperator(
    CompoundPlugOperator["WeightListSmartBulkAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weightsSmartBulk", "wtsmrtblk"),
    )

    weightsSmartBulk = DoubleField()
    wtsmrtblk = weightsSmartBulk


class WeightListSmartBulkAttrOperator(
    CompoundAttrOperator[WeightListSmartBulkPlugOperator]
):
    __slots__ = ()

    weightsSmartBulk = DoubleField()
    wtsmrtblk = weightsSmartBulk


class WeightListSmartBulkField(
    CompoundField[WeightListSmartBulkAttrOperator, WeightListSmartBulkPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartBulkAttrOperator
    PLUG_CLS = WeightListSmartBulkPlugOperator


class WeightListSmartBulkAngularPlugOperator(
    CompoundPlugOperator["WeightListSmartBulkAngularAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weightsSmartBulkAngular", "wtsmrtblkang"),
    )

    weightsSmartBulkAngular = DoubleField()
    wtsmrtblkang = weightsSmartBulkAngular


class WeightListSmartBulkAngularAttrOperator(
    CompoundAttrOperator[WeightListSmartBulkAngularPlugOperator]
):
    __slots__ = ()

    weightsSmartBulkAngular = DoubleField()
    wtsmrtblkang = weightsSmartBulkAngular


class WeightListSmartBulkAngularField(
    CompoundField[WeightListSmartBulkAngularAttrOperator, WeightListSmartBulkAngularPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartBulkAngularAttrOperator
    PLUG_CLS = WeightListSmartBulkAngularPlugOperator


class WeightListSmartBulkWidenPlugOperator(
    CompoundPlugOperator["WeightListSmartBulkWidenAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weightsSmartBulkWiden", "wtsmrtblkwid"),
    )

    weightsSmartBulkWiden = DoubleField()
    wtsmrtblkwid = weightsSmartBulkWiden


class WeightListSmartBulkWidenAttrOperator(
    CompoundAttrOperator[WeightListSmartBulkWidenPlugOperator]
):
    __slots__ = ()

    weightsSmartBulkWiden = DoubleField()
    wtsmrtblkwid = weightsSmartBulkWiden


class WeightListSmartBulkWidenField(
    CompoundField[WeightListSmartBulkWidenAttrOperator, WeightListSmartBulkWidenPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartBulkWidenAttrOperator
    PLUG_CLS = WeightListSmartBulkWidenPlugOperator


class WeightListSmartSlidePlugOperator(
    CompoundPlugOperator["WeightListSmartSlideAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weightsSmartSlide", "wtsmrtsld"),
    )

    weightsSmartSlide = DoubleField()
    wtsmrtsld = weightsSmartSlide


class WeightListSmartSlideAttrOperator(
    CompoundAttrOperator[WeightListSmartSlidePlugOperator]
):
    __slots__ = ()

    weightsSmartSlide = DoubleField()
    wtsmrtsld = weightsSmartSlide


class WeightListSmartSlideField(
    CompoundField[WeightListSmartSlideAttrOperator, WeightListSmartSlidePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartSlideAttrOperator
    PLUG_CLS = WeightListSmartSlidePlugOperator


class WeightListSmartSlideAngularPlugOperator(
    CompoundPlugOperator["WeightListSmartSlideAngularAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weightsSmartSlideAngular", "wtsmrtsldang"),
    )

    weightsSmartSlideAngular = DoubleField()
    wtsmrtsldang = weightsSmartSlideAngular


class WeightListSmartSlideAngularAttrOperator(
    CompoundAttrOperator[WeightListSmartSlideAngularPlugOperator]
):
    __slots__ = ()

    weightsSmartSlideAngular = DoubleField()
    wtsmrtsldang = weightsSmartSlideAngular


class WeightListSmartSlideAngularField(
    CompoundField[WeightListSmartSlideAngularAttrOperator, WeightListSmartSlideAngularPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartSlideAngularAttrOperator
    PLUG_CLS = WeightListSmartSlideAngularPlugOperator


class WeightListSmartSmoothPlugOperator(
    CompoundPlugOperator["WeightListSmartSmoothAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weightsSmartSmooth", "wtsmrtsmth"),
    )

    weightsSmartSmooth = DoubleField()
    wtsmrtsmth = weightsSmartSmooth


class WeightListSmartSmoothAttrOperator(
    CompoundAttrOperator[WeightListSmartSmoothPlugOperator]
):
    __slots__ = ()

    weightsSmartSmooth = DoubleField()
    wtsmrtsmth = weightsSmartSmooth


class WeightListSmartSmoothField(
    CompoundField[WeightListSmartSmoothAttrOperator, WeightListSmartSmoothPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartSmoothAttrOperator
    PLUG_CLS = WeightListSmartSmoothPlugOperator


class WeightListSmartWrinklePlugOperator(
    CompoundPlugOperator["WeightListSmartWrinkleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weightsSmartWrinkle", "wtsmrtwrk"),
    )

    weightsSmartWrinkle = DoubleField()
    wtsmrtwrk = weightsSmartWrinkle


class WeightListSmartWrinkleAttrOperator(
    CompoundAttrOperator[WeightListSmartWrinklePlugOperator]
):
    __slots__ = ()

    weightsSmartWrinkle = DoubleField()
    wtsmrtwrk = weightsSmartWrinkle


class WeightListSmartWrinkleField(
    CompoundField[WeightListSmartWrinkleAttrOperator, WeightListSmartWrinklePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartWrinkleAttrOperator
    PLUG_CLS = WeightListSmartWrinklePlugOperator


class WeightListSmartFlattenPlugOperator(
    CompoundPlugOperator["WeightListSmartFlattenAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weightsSmartFlatten", "wtsmrtflt"),
    )

    weightsSmartFlatten = DoubleField()
    wtsmrtflt = weightsSmartFlatten


class WeightListSmartFlattenAttrOperator(
    CompoundAttrOperator[WeightListSmartFlattenPlugOperator]
):
    __slots__ = ()

    weightsSmartFlatten = DoubleField()
    wtsmrtflt = weightsSmartFlatten


class WeightListSmartFlattenField(
    CompoundField[WeightListSmartFlattenAttrOperator, WeightListSmartFlattenPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartFlattenAttrOperator
    PLUG_CLS = WeightListSmartFlattenPlugOperator


class WeightListSmartVolumizePlugOperator(
    CompoundPlugOperator["WeightListSmartVolumizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weightsSmartVolumize", "wtsmrtvol"),
    )

    weightsSmartVolumize = DoubleField()
    wtsmrtvol = weightsSmartVolumize


class WeightListSmartVolumizeAttrOperator(
    CompoundAttrOperator[WeightListSmartVolumizePlugOperator]
):
    __slots__ = ()

    weightsSmartVolumize = DoubleField()
    wtsmrtvol = weightsSmartVolumize


class WeightListSmartVolumizeField(
    CompoundField[WeightListSmartVolumizeAttrOperator, WeightListSmartVolumizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartVolumizeAttrOperator
    PLUG_CLS = WeightListSmartVolumizePlugOperator
