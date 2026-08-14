# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.generic import GenericField
from ..std.at.matrix import MatrixField
from ..std.at.message import MessageField
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
)


class CacheEnumPlugOperator(EnumPlugOperator["CacheEnumAttrOperator"]):
    __slots__ = ()

    DISABLED = 0
    WRITE_MINUS_FILE = 1
    READ_MINUS_FILE = 2
    WRITE_MINUS_NODE = 3
    READ_MINUS_NODE = 4


class CacheEnumAttrOperator(EnumAttrOperator[CacheEnumPlugOperator]):
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


class CacheEnumField(EnumField[CacheEnumAttrOperator, CacheEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = CacheEnumAttrOperator
    PLUG_CLS = CacheEnumPlugOperator


class STICKYEnumPlugOperator(EnumPlugOperator["STICKYEnumAttrOperator"]):
    __slots__ = ()

    MINUS = 0


class STICKYEnumAttrOperator(EnumAttrOperator[STICKYEnumPlugOperator]):
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


class RelativeStickyEnumPlugOperator(
    EnumPlugOperator["RelativeStickyEnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    RELATIVE = 1


class RelativeStickyEnumAttrOperator(
    EnumAttrOperator[RelativeStickyEnumPlugOperator]
):
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


class SLIDINGEnumPlugOperator(EnumPlugOperator["SLIDINGEnumAttrOperator"]):
    __slots__ = ()

    MINUS = 0


class SLIDINGEnumAttrOperator(EnumAttrOperator[SLIDINGEnumPlugOperator]):
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


class QualityEnumPlugOperator(EnumPlugOperator["QualityEnumAttrOperator"]):
    __slots__ = ()

    FULL = 0
    MEDIUM = 1
    LOW = 2


class QualityEnumAttrOperator(EnumAttrOperator[QualityEnumPlugOperator]):
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


class DISPLACEEnumPlugOperator(EnumPlugOperator["DISPLACEEnumAttrOperator"]):
    __slots__ = ()

    MINUS = 0


class DISPLACEEnumAttrOperator(EnumAttrOperator[DISPLACEEnumPlugOperator]):
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


class FORCEEnumPlugOperator(EnumPlugOperator["FORCEEnumAttrOperator"]):
    __slots__ = ()

    MINUS = 0


class FORCEEnumAttrOperator(EnumAttrOperator[FORCEEnumPlugOperator]):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class FORCEEnumField(EnumField[FORCEEnumAttrOperator, FORCEEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = FORCEEnumAttrOperator
    PLUG_CLS = FORCEEnumPlugOperator


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


class RELAXEnumPlugOperator(EnumPlugOperator["RELAXEnumAttrOperator"]):
    __slots__ = ()

    MINUS = 0


class RELAXEnumAttrOperator(EnumAttrOperator[RELAXEnumPlugOperator]):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class RELAXEnumField(EnumField[RELAXEnumAttrOperator, RELAXEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = RELAXEnumAttrOperator
    PLUG_CLS = RELAXEnumPlugOperator


class RelaxModeEnumPlugOperator(EnumPlugOperator["RelaxModeEnumAttrOperator"]):
    __slots__ = ()

    NORMAL = 0
    PULL = 1
    WRINKLE = 2


class RelaxModeEnumAttrOperator(EnumAttrOperator[RelaxModeEnumPlugOperator]):
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


class SMOOTHEnumPlugOperator(EnumPlugOperator["SMOOTHEnumAttrOperator"]):
    __slots__ = ()

    MINUS = 0


class SMOOTHEnumAttrOperator(EnumAttrOperator[SMOOTHEnumPlugOperator]):
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


class COLLISIONEnumPlugOperator(EnumPlugOperator["COLLISIONEnumAttrOperator"]):
    __slots__ = ()

    MINUS = 0


class COLLISIONEnumAttrOperator(EnumAttrOperator[COLLISIONEnumPlugOperator]):
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


class TypeEnumPlugOperator(EnumPlugOperator["TypeEnumAttrOperator"]):
    __slots__ = ()

    POLY = 0
    NURBS = 1
    CAPSULE = 2


class TypeEnumAttrOperator(EnumAttrOperator[TypeEnumPlugOperator]):
    __slots__ = ()

    POLY = 0
    NURBS = 1
    CAPSULE = 2

    NAME_MAP = {
        POLY: "poly",
        NURBS: "nurbs",
        CAPSULE: "capsule",
    }


class TypeEnumField(EnumField[TypeEnumAttrOperator, TypeEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = TypeEnumAttrOperator
    PLUG_CLS = TypeEnumPlugOperator


class CapsuleAxisEnumPlugOperator(
    EnumPlugOperator["CapsuleAxisEnumAttrOperator"]
):
    __slots__ = ()

    X_MINUS_AXIS = 0
    Y_MINUS_AXIS = 1
    Z_MINUS_AXIS = 2
    NEG_X_MINUS_AXIS = 3
    NEG_Y_MINUS_AXIS = 4
    NEG_Z_MINUS_AXIS = 5


class CapsuleAxisEnumAttrOperator(
    EnumAttrOperator[CapsuleAxisEnumPlugOperator]
):
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


class DirTypeEnumPlugOperator(EnumPlugOperator["DirTypeEnumAttrOperator"]):
    __slots__ = ()

    VECTOR = 0
    RADIAL = 1


class DirTypeEnumAttrOperator(EnumAttrOperator[DirTypeEnumPlugOperator]):
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


class DirAxisEnumPlugOperator(EnumPlugOperator["DirAxisEnumAttrOperator"]):
    __slots__ = ()

    X_MINUS_AXIS = 0
    Y_MINUS_AXIS = 1
    Z_MINUS_AXIS = 2
    NEG_X_MINUS_AXIS = 3
    NEG_Y_MINUS_AXIS = 4
    NEG_Z_MINUS_AXIS = 5


class DirAxisEnumAttrOperator(EnumAttrOperator[DirAxisEnumPlugOperator]):
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


class ModeDispEnumPlugOperator(EnumPlugOperator["ModeDispEnumAttrOperator"]):
    __slots__ = ()

    PLANAR = 0
    CYLINDRICAL = 1
    CURVES = 2


class ModeDispEnumAttrOperator(EnumAttrOperator[ModeDispEnumPlugOperator]):
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


class PushModeEnumPlugOperator(EnumPlugOperator["PushModeEnumAttrOperator"]):
    __slots__ = ()

    NORMAL = 0
    GIZMO = 1


class PushModeEnumAttrOperator(EnumAttrOperator[PushModeEnumPlugOperator]):
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


class CombineModeEnumPlugOperator(
    EnumPlugOperator["CombineModeEnumAttrOperator"]
):
    __slots__ = ()

    MAX = 0
    ADD = 1


class CombineModeEnumAttrOperator(
    EnumAttrOperator[CombineModeEnumPlugOperator]
):
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


class CollideModeSmartEnumPlugOperator(
    EnumPlugOperator["CollideModeSmartEnumAttrOperator"]
):
    __slots__ = ()

    PLANE = 0
    MESH = 1


class CollideModeSmartEnumAttrOperator(
    EnumAttrOperator[CollideModeSmartEnumPlugOperator]
):
    __slots__ = ()

    PLANE = 0
    MESH = 1

    NAME_MAP = {
        PLANE: "plane",
        MESH: "mesh",
    }


class CollideModeSmartEnumField(
    EnumField[
        CollideModeSmartEnumAttrOperator, CollideModeSmartEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CollideModeSmartEnumAttrOperator
    PLUG_CLS = CollideModeSmartEnumPlugOperator


class AxisSmartEnumPlugOperator(EnumPlugOperator["AxisSmartEnumAttrOperator"]):
    __slots__ = ()

    X_MINUS_AXIS = 0
    Y_MINUS_AXIS = 1
    Z_MINUS_AXIS = 2
    NEG_X_MINUS_AXIS = 3
    NEG_Y_MINUS_AXIS = 4
    NEG_Z_MINUS_AXIS = 5


class AxisSmartEnumAttrOperator(EnumAttrOperator[AxisSmartEnumPlugOperator]):
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


class SMOOTH_PREEnumPlugOperator(
    EnumPlugOperator["SMOOTH_PREEnumAttrOperator"]
):
    __slots__ = ()

    MINUS = 0


class SMOOTH_PREEnumAttrOperator(EnumAttrOperator[SMOOTH_PREEnumPlugOperator]):
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


class MOVEMENTEnumPlugOperator(EnumPlugOperator["MOVEMENTEnumAttrOperator"]):
    __slots__ = ()

    MINUS = 0


class MOVEMENTEnumAttrOperator(EnumAttrOperator[MOVEMENTEnumPlugOperator]):
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


class COLLISIONSMARTEnumPlugOperator(
    EnumPlugOperator["COLLISIONSMARTEnumAttrOperator"]
):
    __slots__ = ()

    MINUS = 0


class COLLISIONSMARTEnumAttrOperator(
    EnumAttrOperator[COLLISIONSMARTEnumPlugOperator]
):
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


class SMOOTH_POSTEnumPlugOperator(
    EnumPlugOperator["SMOOTH_POSTEnumAttrOperator"]
):
    __slots__ = ()

    MINUS = 0


class SMOOTH_POSTEnumAttrOperator(
    EnumAttrOperator[SMOOTH_POSTEnumPlugOperator]
):
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


class InputPlugOperator(CompoundPlugOperator["InputAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputGeometry", "ig"),
        ("groupId", "gi"),
        ("componentTagExpression", "gtg"),
    )

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField(default_value=0)
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputAttrOperator(CompoundAttrOperator[InputPlugOperator]):
    __slots__ = ()

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField(default_value=0)
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputField(CompoundField[InputAttrOperator, InputPlugOperator]):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator


class EnvelopeWeightsListPlugOperator(
    CompoundPlugOperator["EnvelopeWeightsListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("envelopeWeights", "owt"),)

    envelopeWeights = FloatField(multi=True, default_value=1.0, writable=False)
    owt = envelopeWeights


class EnvelopeWeightsListAttrOperator(
    CompoundAttrOperator[EnvelopeWeightsListPlugOperator]
):
    __slots__ = ()

    envelopeWeights = FloatField(multi=True, default_value=1.0, writable=False)
    owt = envelopeWeights


class EnvelopeWeightsListField(
    CompoundField[
        EnvelopeWeightsListAttrOperator, EnvelopeWeightsListPlugOperator
    ]
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

    fchild1 = LongField(default_value=0, readable=False)
    f1 = fchild1

    fchild2 = LongField(default_value=0, readable=False)
    f2 = fchild2

    fchild3 = LongField(default_value=0, readable=False)
    f3 = fchild3


class FunctionAttrOperator(
    Long3CompoundBaseAttrOperator[FunctionPlugOperator]
):
    __slots__ = ()

    fchild1 = LongField(default_value=0, readable=False)
    f1 = fchild1

    fchild2 = LongField(default_value=0, readable=False)
    f2 = fchild2

    fchild3 = LongField(default_value=0, readable=False)
    f3 = fchild3


class FunctionField(
    Long3CompoundBaseField[FunctionAttrOperator, FunctionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FunctionAttrOperator
    PLUG_CLS = FunctionPlugOperator

    fchild1 = LongField(default_value=0, readable=False)
    f1 = fchild1

    fchild2 = LongField(default_value=0, readable=False)
    f2 = fchild2

    fchild3 = LongField(default_value=0, readable=False)
    f3 = fchild3


class WeightListPlugOperator(CompoundPlugOperator["WeightListAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("weights", "wl.w"),)

    weights = FloatField(multi=True, default_value=1.0)


class WeightListAttrOperator(CompoundAttrOperator[WeightListPlugOperator]):
    __slots__ = ()

    weights = FloatField(multi=True, default_value=1.0)


class WeightListField(
    CompoundField[WeightListAttrOperator, WeightListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListAttrOperator
    PLUG_CLS = WeightListPlugOperator


class UserDataPlugOperator(CompoundPlugOperator["UserDataAttrOperator"]):
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

    inTime = DoubleField(default_value=0.0)
    it = inTime

    cache = CacheEnumField(default_value=0)
    cac = cache

    cachePath = DataStringField()
    cpath = cachePath

    showWarnings = BoolField(default_value=False)
    swrn = showWarnings

    userScale = CompoundField(default_value=(1.0, 1.0, 1.0))
    usc = userScale

    STICKY = STICKYEnumField(default_value=0)
    LSTK = STICKY

    enableSticky = BoolField(default_value=True)
    estk = enableSticky

    relativeSticky = RelativeStickyEnumField(default_value=0)
    relstk = relativeSticky

    forceNormalize = BoolField(default_value=False)
    frcnrm = forceNormalize

    stickyA = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    stka = stickyA

    stickyB = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    stkb = stickyB

    stickyC = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    stkc = stickyC

    SLIDING = SLIDINGEnumField(default_value=0)
    LSLD = SLIDING

    enableSliding = BoolField(default_value=False)
    esld = enableSliding

    quality = QualityEnumField(default_value=0)
    qlty = quality

    shrinkWrap = BoolField(default_value=False)
    shr = shrinkWrap

    useBind = BoolField(default_value=False)
    ub = useBind

    allowNegFat = BoolField(default_value=True)
    anft = allowNegFat

    DISPLACE = DISPLACEEnumField(default_value=0)
    LDSP = DISPLACE

    enableDisplace = BoolField(default_value=False)
    edsp = enableDisplace

    collisionDisplace = BoolField(default_value=True)
    clldsp = collisionDisplace

    FORCE = FORCEEnumField(default_value=0)
    LFRC = FORCE

    enableForce = BoolField(default_value=False)
    efrc = enableForce

    gravityStrength = DoubleField(default_value=1.0, min_value=0.0)
    gravstr = gravityStrength

    gravityX = DoubleField(default_value=0.0)
    gravx = gravityX

    gravityY = DoubleField(default_value=-1.0)
    gravy = gravityY

    gravityZ = DoubleField(default_value=0.0)
    gravz = gravityZ

    windStrength = DoubleField(default_value=0.0, min_value=0.0)
    windstr = windStrength

    windDirX = DoubleField(default_value=1.0)
    windx = windDirX

    windDirY = DoubleField(default_value=0.0)
    windy = windDirY

    windDirZ = DoubleField(default_value=0.0)
    windz = windDirZ

    windSpeed = DoubleField(default_value=1.0)
    windspd = windSpeed

    windNoise = DoubleField(default_value=1.0, min_value=0.0)
    windnos = windNoise

    windNoiseScale = DoubleField(default_value=1.0, min_value=0.0)
    windnscl = windNoiseScale

    windNoiseDirty = LongField(default_value=1, min_value=1, max_value=16)
    winddrt = windNoiseDirty

    JIGGLE = JIGGLEEnumField(default_value=0)
    LJIG = JIGGLE

    enableJiggle = BoolField(default_value=False)
    ejig = enableJiggle

    jiggleCollisions = BoolField(default_value=True)
    jigcol = jiggleCollisions

    resetFrame = DoubleField(default_value=0.0, min_value=-1024.0)
    rf = resetFrame

    jiggleMin = DoubleField(default_value=0.0)
    jmin = jiggleMin

    jiggleMax = DoubleField(default_value=0.5)
    jmax = jiggleMax

    cycleMin = DoubleField(default_value=8.0, min_value=1.0)
    cmin = cycleMin

    cycleMax = DoubleField(default_value=10.0, min_value=1.0)
    cmax = cycleMax

    restMin = DoubleField(default_value=12.0, min_value=1.0)
    rmin = restMin

    restMax = DoubleField(default_value=36.0, min_value=1.0)
    rmax = restMax

    RELAX = RELAXEnumField(default_value=0)
    LRLX = RELAX

    enableRelax = BoolField(default_value=False)
    erlx = enableRelax

    relaxMode = RelaxModeEnumField(default_value=2)
    rmod = relaxMode

    relaxCollisions = BoolField(default_value=True)
    rcll = relaxCollisions

    relaxIterations = LongField(default_value=8, min_value=1)
    ritr = relaxIterations

    relaxStrength = DoubleField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    rstr = relaxStrength

    wrinkleStrength = DoubleField(default_value=1.0, min_value=0.0)
    wrstr = wrinkleStrength

    relaxCompress = DoubleField(default_value=0.0, min_value=0.0)
    rcmp = relaxCompress

    relaxExpand = DoubleField(default_value=0.0, min_value=0.0)
    rexp = relaxExpand

    relaxFriction = DoubleField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    rfrc = relaxFriction

    SMOOTH = SMOOTHEnumField(default_value=0)
    SMTH = SMOOTH

    enableSmooth = BoolField(default_value=False)
    esmth = enableSmooth

    smoothCollisions = BoolField(default_value=True)
    scll = smoothCollisions

    smoothIterations = LongField(default_value=5, min_value=1)
    sitr = smoothIterations

    smoothStrength = DoubleField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    sstr = smoothStrength

    smoothCompress = DoubleField(default_value=0.0, min_value=0.0)
    scmp = smoothCompress

    smoothExpand = DoubleField(default_value=0.0, min_value=0.0)
    sexp = smoothExpand

    smoothHold = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    shld = smoothHold

    COLLISION = COLLISIONEnumField(default_value=0)
    COLL = COLLISION

    smartCollision = BoolField(default_value=False)
    smrtcll = smartCollision

    selfCollision = BoolField(default_value=False)
    slfcll = selfCollision

    selfTolerance = DoubleField(default_value=0.001, min_value=0.0)
    slftol = selfTolerance

    selfFalloff = DoubleField(default_value=1.0, min_value=0.0)
    slffal = selfFalloff

    selfVolumize = DoubleField(default_value=0.3, min_value=0.0)
    slfvol = selfVolumize

    selfBlurIterations = LongField(default_value=5, min_value=0)
    slfblrit = selfBlurIterations

    selfRelaxIterations = LongField(default_value=12, min_value=1)
    slfrxi = selfRelaxIterations

    selfRelaxStrength = DoubleField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    slfrxstr = selfRelaxStrength

    selfSmoothIterations = LongField(default_value=5, min_value=1)
    slfsmi = selfSmoothIterations

    selfSmoothStrength = DoubleField(
        default_value=0.3, min_value=0.0, max_value=1.0
    )
    slfsmstr = selfSmoothStrength

    selfSmoothHold = DoubleField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    slfhld = selfSmoothHold


class UserDataAttrOperator(CompoundAttrOperator[UserDataPlugOperator]):
    __slots__ = ()

    inTime = DoubleField(default_value=0.0)
    it = inTime

    cache = CacheEnumField(default_value=0)
    cac = cache

    cachePath = DataStringField()
    cpath = cachePath

    showWarnings = BoolField(default_value=False)
    swrn = showWarnings

    userScale = CompoundField(default_value=(1.0, 1.0, 1.0))
    usc = userScale

    STICKY = STICKYEnumField(default_value=0)
    LSTK = STICKY

    enableSticky = BoolField(default_value=True)
    estk = enableSticky

    relativeSticky = RelativeStickyEnumField(default_value=0)
    relstk = relativeSticky

    forceNormalize = BoolField(default_value=False)
    frcnrm = forceNormalize

    stickyA = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    stka = stickyA

    stickyB = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    stkb = stickyB

    stickyC = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    stkc = stickyC

    SLIDING = SLIDINGEnumField(default_value=0)
    LSLD = SLIDING

    enableSliding = BoolField(default_value=False)
    esld = enableSliding

    quality = QualityEnumField(default_value=0)
    qlty = quality

    shrinkWrap = BoolField(default_value=False)
    shr = shrinkWrap

    useBind = BoolField(default_value=False)
    ub = useBind

    allowNegFat = BoolField(default_value=True)
    anft = allowNegFat

    DISPLACE = DISPLACEEnumField(default_value=0)
    LDSP = DISPLACE

    enableDisplace = BoolField(default_value=False)
    edsp = enableDisplace

    collisionDisplace = BoolField(default_value=True)
    clldsp = collisionDisplace

    FORCE = FORCEEnumField(default_value=0)
    LFRC = FORCE

    enableForce = BoolField(default_value=False)
    efrc = enableForce

    gravityStrength = DoubleField(default_value=1.0, min_value=0.0)
    gravstr = gravityStrength

    gravityX = DoubleField(default_value=0.0)
    gravx = gravityX

    gravityY = DoubleField(default_value=-1.0)
    gravy = gravityY

    gravityZ = DoubleField(default_value=0.0)
    gravz = gravityZ

    windStrength = DoubleField(default_value=0.0, min_value=0.0)
    windstr = windStrength

    windDirX = DoubleField(default_value=1.0)
    windx = windDirX

    windDirY = DoubleField(default_value=0.0)
    windy = windDirY

    windDirZ = DoubleField(default_value=0.0)
    windz = windDirZ

    windSpeed = DoubleField(default_value=1.0)
    windspd = windSpeed

    windNoise = DoubleField(default_value=1.0, min_value=0.0)
    windnos = windNoise

    windNoiseScale = DoubleField(default_value=1.0, min_value=0.0)
    windnscl = windNoiseScale

    windNoiseDirty = LongField(default_value=1, min_value=1, max_value=16)
    winddrt = windNoiseDirty

    JIGGLE = JIGGLEEnumField(default_value=0)
    LJIG = JIGGLE

    enableJiggle = BoolField(default_value=False)
    ejig = enableJiggle

    jiggleCollisions = BoolField(default_value=True)
    jigcol = jiggleCollisions

    resetFrame = DoubleField(default_value=0.0, min_value=-1024.0)
    rf = resetFrame

    jiggleMin = DoubleField(default_value=0.0)
    jmin = jiggleMin

    jiggleMax = DoubleField(default_value=0.5)
    jmax = jiggleMax

    cycleMin = DoubleField(default_value=8.0, min_value=1.0)
    cmin = cycleMin

    cycleMax = DoubleField(default_value=10.0, min_value=1.0)
    cmax = cycleMax

    restMin = DoubleField(default_value=12.0, min_value=1.0)
    rmin = restMin

    restMax = DoubleField(default_value=36.0, min_value=1.0)
    rmax = restMax

    RELAX = RELAXEnumField(default_value=0)
    LRLX = RELAX

    enableRelax = BoolField(default_value=False)
    erlx = enableRelax

    relaxMode = RelaxModeEnumField(default_value=2)
    rmod = relaxMode

    relaxCollisions = BoolField(default_value=True)
    rcll = relaxCollisions

    relaxIterations = LongField(default_value=8, min_value=1)
    ritr = relaxIterations

    relaxStrength = DoubleField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    rstr = relaxStrength

    wrinkleStrength = DoubleField(default_value=1.0, min_value=0.0)
    wrstr = wrinkleStrength

    relaxCompress = DoubleField(default_value=0.0, min_value=0.0)
    rcmp = relaxCompress

    relaxExpand = DoubleField(default_value=0.0, min_value=0.0)
    rexp = relaxExpand

    relaxFriction = DoubleField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    rfrc = relaxFriction

    SMOOTH = SMOOTHEnumField(default_value=0)
    SMTH = SMOOTH

    enableSmooth = BoolField(default_value=False)
    esmth = enableSmooth

    smoothCollisions = BoolField(default_value=True)
    scll = smoothCollisions

    smoothIterations = LongField(default_value=5, min_value=1)
    sitr = smoothIterations

    smoothStrength = DoubleField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    sstr = smoothStrength

    smoothCompress = DoubleField(default_value=0.0, min_value=0.0)
    scmp = smoothCompress

    smoothExpand = DoubleField(default_value=0.0, min_value=0.0)
    sexp = smoothExpand

    smoothHold = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    shld = smoothHold

    COLLISION = COLLISIONEnumField(default_value=0)
    COLL = COLLISION

    smartCollision = BoolField(default_value=False)
    smrtcll = smartCollision

    selfCollision = BoolField(default_value=False)
    slfcll = selfCollision

    selfTolerance = DoubleField(default_value=0.001, min_value=0.0)
    slftol = selfTolerance

    selfFalloff = DoubleField(default_value=1.0, min_value=0.0)
    slffal = selfFalloff

    selfVolumize = DoubleField(default_value=0.3, min_value=0.0)
    slfvol = selfVolumize

    selfBlurIterations = LongField(default_value=5, min_value=0)
    slfblrit = selfBlurIterations

    selfRelaxIterations = LongField(default_value=12, min_value=1)
    slfrxi = selfRelaxIterations

    selfRelaxStrength = DoubleField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    slfrxstr = selfRelaxStrength

    selfSmoothIterations = LongField(default_value=5, min_value=1)
    slfsmi = selfSmoothIterations

    selfSmoothStrength = DoubleField(
        default_value=0.3, min_value=0.0, max_value=1.0
    )
    slfsmstr = selfSmoothStrength

    selfSmoothHold = DoubleField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    slfhld = selfSmoothHold


class UserDataField(CompoundField[UserDataAttrOperator, UserDataPlugOperator]):
    __slots__ = ()

    ATTR_CLS = UserDataAttrOperator
    PLUG_CLS = UserDataPlugOperator

    inTime = DoubleField(default_value=0.0)
    it = inTime

    cache = CacheEnumField(default_value=0)
    cac = cache

    cachePath = DataStringField()
    cpath = cachePath

    showWarnings = BoolField(default_value=False)
    swrn = showWarnings

    userScale = CompoundField(default_value=(1.0, 1.0, 1.0))
    usc = userScale

    STICKY = STICKYEnumField(default_value=0)
    LSTK = STICKY

    enableSticky = BoolField(default_value=True)
    estk = enableSticky

    relativeSticky = RelativeStickyEnumField(default_value=0)
    relstk = relativeSticky

    forceNormalize = BoolField(default_value=False)
    frcnrm = forceNormalize

    stickyA = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    stka = stickyA

    stickyB = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    stkb = stickyB

    stickyC = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    stkc = stickyC

    SLIDING = SLIDINGEnumField(default_value=0)
    LSLD = SLIDING

    enableSliding = BoolField(default_value=False)
    esld = enableSliding

    quality = QualityEnumField(default_value=0)
    qlty = quality

    shrinkWrap = BoolField(default_value=False)
    shr = shrinkWrap

    useBind = BoolField(default_value=False)
    ub = useBind

    allowNegFat = BoolField(default_value=True)
    anft = allowNegFat

    DISPLACE = DISPLACEEnumField(default_value=0)
    LDSP = DISPLACE

    enableDisplace = BoolField(default_value=False)
    edsp = enableDisplace

    collisionDisplace = BoolField(default_value=True)
    clldsp = collisionDisplace

    FORCE = FORCEEnumField(default_value=0)
    LFRC = FORCE

    enableForce = BoolField(default_value=False)
    efrc = enableForce

    gravityStrength = DoubleField(default_value=1.0, min_value=0.0)
    gravstr = gravityStrength

    gravityX = DoubleField(default_value=0.0)
    gravx = gravityX

    gravityY = DoubleField(default_value=-1.0)
    gravy = gravityY

    gravityZ = DoubleField(default_value=0.0)
    gravz = gravityZ

    windStrength = DoubleField(default_value=0.0, min_value=0.0)
    windstr = windStrength

    windDirX = DoubleField(default_value=1.0)
    windx = windDirX

    windDirY = DoubleField(default_value=0.0)
    windy = windDirY

    windDirZ = DoubleField(default_value=0.0)
    windz = windDirZ

    windSpeed = DoubleField(default_value=1.0)
    windspd = windSpeed

    windNoise = DoubleField(default_value=1.0, min_value=0.0)
    windnos = windNoise

    windNoiseScale = DoubleField(default_value=1.0, min_value=0.0)
    windnscl = windNoiseScale

    windNoiseDirty = LongField(default_value=1, min_value=1, max_value=16)
    winddrt = windNoiseDirty

    JIGGLE = JIGGLEEnumField(default_value=0)
    LJIG = JIGGLE

    enableJiggle = BoolField(default_value=False)
    ejig = enableJiggle

    jiggleCollisions = BoolField(default_value=True)
    jigcol = jiggleCollisions

    resetFrame = DoubleField(default_value=0.0, min_value=-1024.0)
    rf = resetFrame

    jiggleMin = DoubleField(default_value=0.0)
    jmin = jiggleMin

    jiggleMax = DoubleField(default_value=0.5)
    jmax = jiggleMax

    cycleMin = DoubleField(default_value=8.0, min_value=1.0)
    cmin = cycleMin

    cycleMax = DoubleField(default_value=10.0, min_value=1.0)
    cmax = cycleMax

    restMin = DoubleField(default_value=12.0, min_value=1.0)
    rmin = restMin

    restMax = DoubleField(default_value=36.0, min_value=1.0)
    rmax = restMax

    RELAX = RELAXEnumField(default_value=0)
    LRLX = RELAX

    enableRelax = BoolField(default_value=False)
    erlx = enableRelax

    relaxMode = RelaxModeEnumField(default_value=2)
    rmod = relaxMode

    relaxCollisions = BoolField(default_value=True)
    rcll = relaxCollisions

    relaxIterations = LongField(default_value=8, min_value=1)
    ritr = relaxIterations

    relaxStrength = DoubleField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    rstr = relaxStrength

    wrinkleStrength = DoubleField(default_value=1.0, min_value=0.0)
    wrstr = wrinkleStrength

    relaxCompress = DoubleField(default_value=0.0, min_value=0.0)
    rcmp = relaxCompress

    relaxExpand = DoubleField(default_value=0.0, min_value=0.0)
    rexp = relaxExpand

    relaxFriction = DoubleField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    rfrc = relaxFriction

    SMOOTH = SMOOTHEnumField(default_value=0)
    SMTH = SMOOTH

    enableSmooth = BoolField(default_value=False)
    esmth = enableSmooth

    smoothCollisions = BoolField(default_value=True)
    scll = smoothCollisions

    smoothIterations = LongField(default_value=5, min_value=1)
    sitr = smoothIterations

    smoothStrength = DoubleField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    sstr = smoothStrength

    smoothCompress = DoubleField(default_value=0.0, min_value=0.0)
    scmp = smoothCompress

    smoothExpand = DoubleField(default_value=0.0, min_value=0.0)
    sexp = smoothExpand

    smoothHold = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    shld = smoothHold

    COLLISION = COLLISIONEnumField(default_value=0)
    COLL = COLLISION

    smartCollision = BoolField(default_value=False)
    smrtcll = smartCollision

    selfCollision = BoolField(default_value=False)
    slfcll = selfCollision

    selfTolerance = DoubleField(default_value=0.001, min_value=0.0)
    slftol = selfTolerance

    selfFalloff = DoubleField(default_value=1.0, min_value=0.0)
    slffal = selfFalloff

    selfVolumize = DoubleField(default_value=0.3, min_value=0.0)
    slfvol = selfVolumize

    selfBlurIterations = LongField(default_value=5, min_value=0)
    slfblrit = selfBlurIterations

    selfRelaxIterations = LongField(default_value=12, min_value=1)
    slfrxi = selfRelaxIterations

    selfRelaxStrength = DoubleField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    slfrxstr = selfRelaxStrength

    selfSmoothIterations = LongField(default_value=5, min_value=1)
    slfsmi = selfSmoothIterations

    selfSmoothStrength = DoubleField(
        default_value=0.3, min_value=0.0, max_value=1.0
    )
    slfsmstr = selfSmoothStrength

    selfSmoothHold = DoubleField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    slfhld = selfSmoothHold


class MuscleDataPlugOperator(CompoundPlugOperator["MuscleDataAttrOperator"]):
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

    stickyStrength = DoubleField(default_value=1.0)
    stkstr = stickyStrength

    slidingStrength = DoubleField(default_value=1.0)
    sldstr = slidingStrength

    fat = DoubleField(default_value=0.1, min_value=0.0)
    ft = fat

    reverseNormals = BoolField(default_value=False)
    rn = reverseNormals

    type = TypeEnumField(default_value=0)
    typ = type

    radius = DoubleField(default_value=1.0, min_value=1e-10)
    rad = radius

    length = DoubleField(default_value=1.0)
    len = length

    capsuleAxis = CapsuleAxisEnumField(default_value=1)
    cax = capsuleAxis

    relative = BoolField(default_value=True)
    rel = relative

    lockStickyWt = BoolField(default_value=False)
    lkst = lockStickyWt

    lockSlidingWt = BoolField(default_value=False)
    lksl = lockSlidingWt

    affectSticky = BoolField(default_value=True)
    afstk = affectSticky

    affectSliding = BoolField(default_value=True)
    afsld = affectSliding

    userScaleMus = CompoundField(default_value=(1.0, 1.0, 1.0))
    uscmus = userScaleMus


class MuscleDataAttrOperator(CompoundAttrOperator[MuscleDataPlugOperator]):
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

    stickyStrength = DoubleField(default_value=1.0)
    stkstr = stickyStrength

    slidingStrength = DoubleField(default_value=1.0)
    sldstr = slidingStrength

    fat = DoubleField(default_value=0.1, min_value=0.0)
    ft = fat

    reverseNormals = BoolField(default_value=False)
    rn = reverseNormals

    type = TypeEnumField(default_value=0)
    typ = type

    radius = DoubleField(default_value=1.0, min_value=1e-10)
    rad = radius

    length = DoubleField(default_value=1.0)
    len = length

    capsuleAxis = CapsuleAxisEnumField(default_value=1)
    cax = capsuleAxis

    relative = BoolField(default_value=True)
    rel = relative

    lockStickyWt = BoolField(default_value=False)
    lkst = lockStickyWt

    lockSlidingWt = BoolField(default_value=False)
    lksl = lockSlidingWt

    affectSticky = BoolField(default_value=True)
    afstk = affectSticky

    affectSliding = BoolField(default_value=True)
    afsld = affectSliding

    userScaleMus = CompoundField(default_value=(1.0, 1.0, 1.0))
    uscmus = userScaleMus


class MuscleDataField(
    CompoundField[MuscleDataAttrOperator, MuscleDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MuscleDataAttrOperator
    PLUG_CLS = MuscleDataPlugOperator


class DirDataPlugOperator(CompoundPlugOperator["DirDataAttrOperator"]):
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

    strengthDir = DoubleField(default_value=1.0)
    strd = strengthDir

    falloffInnerDir = DoubleField(default_value=0.25, min_value=0.0)
    fid = falloffInnerDir

    falloffOuterDir = DoubleField(default_value=1.0, min_value=0.0)
    fod = falloffOuterDir

    dirType = DirTypeEnumField(default_value=0)
    dirtyp = dirType

    dirLength = DoubleField(default_value=1.0, min_value=0.0)
    dirlen = dirLength

    dirAxis = DirAxisEnumField(default_value=1)
    dax = dirAxis

    lockDirWt = BoolField(default_value=False)
    lkdi = lockDirWt


class DirDataAttrOperator(CompoundAttrOperator[DirDataPlugOperator]):
    __slots__ = ()

    worldMatrixDir = MatrixField()
    wmd = worldMatrixDir

    strengthDir = DoubleField(default_value=1.0)
    strd = strengthDir

    falloffInnerDir = DoubleField(default_value=0.25, min_value=0.0)
    fid = falloffInnerDir

    falloffOuterDir = DoubleField(default_value=1.0, min_value=0.0)
    fod = falloffOuterDir

    dirType = DirTypeEnumField(default_value=0)
    dirtyp = dirType

    dirLength = DoubleField(default_value=1.0, min_value=0.0)
    dirlen = dirLength

    dirAxis = DirAxisEnumField(default_value=1)
    dax = dirAxis

    lockDirWt = BoolField(default_value=False)
    lkdi = lockDirWt


class DirDataField(CompoundField[DirDataAttrOperator, DirDataPlugOperator]):
    __slots__ = ()

    ATTR_CLS = DirDataAttrOperator
    PLUG_CLS = DirDataPlugOperator


class DispDataPlugOperator(CompoundPlugOperator["DispDataAttrOperator"]):
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

    curves = GenericField(multi=True)
    crv = curves

    modeDisp = ModeDispEnumField(default_value=0)
    mdd = modeDisp

    lengthDisp = FloatField(default_value=1.0, min_value=0.0)
    lend = lengthDisp

    sizeRadiusDisp = FloatField(default_value=0.5, min_value=0.0)
    sizd = sizeRadiusDisp

    amplitudeDisp = FloatField(default_value=0.10000000149011612)
    ampd = amplitudeDisp

    falloffDisp = FloatField(default_value=0.5, min_value=0.0)
    fald = falloffDisp

    pushMode = PushModeEnumField(default_value=0)
    pmd = pushMode

    combineMode = CombineModeEnumField(default_value=0)
    cmd = combineMode

    shader = MessageField()
    sha = shader


class DispDataAttrOperator(CompoundAttrOperator[DispDataPlugOperator]):
    __slots__ = ()

    worldMatrixDisp = MatrixField()
    wmdsp = worldMatrixDisp

    curves = GenericField(multi=True)
    crv = curves

    modeDisp = ModeDispEnumField(default_value=0)
    mdd = modeDisp

    lengthDisp = FloatField(default_value=1.0, min_value=0.0)
    lend = lengthDisp

    sizeRadiusDisp = FloatField(default_value=0.5, min_value=0.0)
    sizd = sizeRadiusDisp

    amplitudeDisp = FloatField(default_value=0.10000000149011612)
    ampd = amplitudeDisp

    falloffDisp = FloatField(default_value=0.5, min_value=0.0)
    fald = falloffDisp

    pushMode = PushModeEnumField(default_value=0)
    pmd = pushMode

    combineMode = CombineModeEnumField(default_value=0)
    cmd = combineMode

    shader = MessageField()
    sha = shader


class DispDataField(CompoundField[DispDataAttrOperator, DispDataPlugOperator]):
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

    enableSmart = BoolField(default_value=True)
    enasmrt = enableSmart

    collideModeSmart = CollideModeSmartEnumField(default_value=0)
    colmodsmrt = collideModeSmart

    axisSmart = AxisSmartEnumField(default_value=1)
    axsmrt = axisSmart

    triggerMin = DoubleField(default_value=0.0, min_value=0.0, max_value=180.0)
    trgmin = triggerMin

    angleMinSmart = DoubleField(
        default_value=0.0, min_value=0.0, max_value=180.0
    )
    angminsmrt = angleMinSmart

    angleMaxSmart = DoubleField(
        default_value=90.0, min_value=0.0, max_value=180.0
    )
    angmaxsmrt = angleMaxSmart

    biasSmart = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bissmrt = biasSmart

    biasAdjustSmart = DoubleField(
        default_value=0.0, min_value=-2.0, max_value=2.0
    )
    bisadjsmrt = biasAdjustSmart

    userScaleSmarr = DoubleField(default_value=1.0)
    usrsclsmrt = userScaleSmarr

    manualScaleSmarr = DoubleField(default_value=1.0)
    mansclsmrt = manualScaleSmarr

    SMOOTH_PRE = SMOOTH_PREEnumField(default_value=0)
    SMTHPRE = SMOOTH_PRE

    smrtSmoothIterationsPre = LongField(default_value=5, min_value=0)
    smrtsmipre = smrtSmoothIterationsPre

    smrtSmoothStrengthPre = DoubleField(
        default_value=0.3, min_value=0.0, max_value=1.0
    )
    smrtsmstrpre = smrtSmoothStrengthPre

    smrtSmoothHoldPre = DoubleField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    smrthldpre = smrtSmoothHoldPre

    MOVEMENT = MOVEMENTEnumField(default_value=0)
    MOVE = MOVEMENT

    bulkASmart = DoubleField(default_value=1.0)
    blkasmrt = bulkASmart

    bulkBSmart = DoubleField(default_value=1.0)
    blkbsmrt = bulkBSmart

    bulkAngularASmart = DoubleField(default_value=1.0)
    blkaangsmrt = bulkAngularASmart

    bulkAngularBSmart = DoubleField(default_value=1.0)
    blkangbsmrt = bulkAngularBSmart

    bulkWidenASmart = DoubleField(default_value=1.0)
    blkwidasmrt = bulkWidenASmart

    bulkWidenBSmart = DoubleField(default_value=1.0)
    blkwidbsmrt = bulkWidenBSmart

    slideSmartA = DoubleField(default_value=1.0)
    sldasmrt = slideSmartA

    slideSmartB = DoubleField(default_value=1.0)
    sldbsmrt = slideSmartB

    slideRearSmartA = DoubleField(default_value=1.0)
    sldrerasmrt = slideRearSmartA

    slideRearSmartB = DoubleField(default_value=1.0)
    sldrerbsmrt = slideRearSmartB

    slideAngularSmartA = DoubleField(default_value=1.0)
    sldangasmrt = slideAngularSmartA

    slideAngularSmartB = DoubleField(default_value=1.0)
    sldangbsmrt = slideAngularSmartB

    slideAngularRearSmartA = DoubleField(default_value=1.0)
    sldangrerasmrt = slideAngularRearSmartA

    slideAngularRearSmartB = DoubleField(default_value=1.0)
    sldangrerbsmrt = slideAngularRearSmartB

    wrinkleSmartA = DoubleField(default_value=1.0)
    wrkasmrt = wrinkleSmartA

    wrinkleSmartB = DoubleField(default_value=1.0)
    wrkbsmrt = wrinkleSmartB

    wrinkleSpreadSmart = DoubleField(default_value=0.5)
    wrksprsmrt = wrinkleSpreadSmart

    COLLISIONSMART = COLLISIONSMARTEnumField(default_value=0)
    COLLSMRT = COLLISIONSMART

    flattenSmartA = DoubleField(default_value=1.0)
    fltasmrt = flattenSmartA

    flattenSmartB = DoubleField(default_value=1.0)
    fltbsmrt = flattenSmartB

    rigidSmartA = DoubleField(default_value=0.0)
    rigsmrta = rigidSmartA

    rigidSmartB = DoubleField(default_value=0.0)
    rigsmrtb = rigidSmartB

    collisionBlurIterationsSmart = LongField(default_value=0)
    colblritsmrt = collisionBlurIterationsSmart

    volumizeSmartA = DoubleField(default_value=1.0)
    vlmasmrt = volumizeSmartA

    volumizeSmartB = DoubleField(default_value=1.0)
    vlmbsmrt = volumizeSmartB

    volumizeOffsetSmartA = DoubleField(default_value=0.0)
    vlmoffsmrt = volumizeOffsetSmartA

    volumizePuffSmart = DoubleField(default_value=1.0)
    vlmpufsmrt = volumizePuffSmart

    volumizeDistSmart = DoubleField(default_value=1.0)
    vlmdsmrt = volumizeDistSmart

    volumizeFalloffSmart = DoubleField(default_value=1.0)
    vlmfallsmrt = volumizeFalloffSmart

    SMOOTH_POST = SMOOTH_POSTEnumField(default_value=0)
    SMTHPST = SMOOTH_POST

    smrtSmoothIterationsPost = LongField(default_value=5, min_value=0)
    smrtsmipst = smrtSmoothIterationsPost

    smrtSmoothStrengthPost = DoubleField(
        default_value=0.3, min_value=0.0, max_value=1.0
    )
    smrtsmstrpst = smrtSmoothStrengthPost

    smrtSmoothHoldPost = DoubleField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    smrthldpst = smrtSmoothHoldPost

    lockSmartWt = BoolField(default_value=False)
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

    enableSmart = BoolField(default_value=True)
    enasmrt = enableSmart

    collideModeSmart = CollideModeSmartEnumField(default_value=0)
    colmodsmrt = collideModeSmart

    axisSmart = AxisSmartEnumField(default_value=1)
    axsmrt = axisSmart

    triggerMin = DoubleField(default_value=0.0, min_value=0.0, max_value=180.0)
    trgmin = triggerMin

    angleMinSmart = DoubleField(
        default_value=0.0, min_value=0.0, max_value=180.0
    )
    angminsmrt = angleMinSmart

    angleMaxSmart = DoubleField(
        default_value=90.0, min_value=0.0, max_value=180.0
    )
    angmaxsmrt = angleMaxSmart

    biasSmart = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bissmrt = biasSmart

    biasAdjustSmart = DoubleField(
        default_value=0.0, min_value=-2.0, max_value=2.0
    )
    bisadjsmrt = biasAdjustSmart

    userScaleSmarr = DoubleField(default_value=1.0)
    usrsclsmrt = userScaleSmarr

    manualScaleSmarr = DoubleField(default_value=1.0)
    mansclsmrt = manualScaleSmarr

    SMOOTH_PRE = SMOOTH_PREEnumField(default_value=0)
    SMTHPRE = SMOOTH_PRE

    smrtSmoothIterationsPre = LongField(default_value=5, min_value=0)
    smrtsmipre = smrtSmoothIterationsPre

    smrtSmoothStrengthPre = DoubleField(
        default_value=0.3, min_value=0.0, max_value=1.0
    )
    smrtsmstrpre = smrtSmoothStrengthPre

    smrtSmoothHoldPre = DoubleField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    smrthldpre = smrtSmoothHoldPre

    MOVEMENT = MOVEMENTEnumField(default_value=0)
    MOVE = MOVEMENT

    bulkASmart = DoubleField(default_value=1.0)
    blkasmrt = bulkASmart

    bulkBSmart = DoubleField(default_value=1.0)
    blkbsmrt = bulkBSmart

    bulkAngularASmart = DoubleField(default_value=1.0)
    blkaangsmrt = bulkAngularASmart

    bulkAngularBSmart = DoubleField(default_value=1.0)
    blkangbsmrt = bulkAngularBSmart

    bulkWidenASmart = DoubleField(default_value=1.0)
    blkwidasmrt = bulkWidenASmart

    bulkWidenBSmart = DoubleField(default_value=1.0)
    blkwidbsmrt = bulkWidenBSmart

    slideSmartA = DoubleField(default_value=1.0)
    sldasmrt = slideSmartA

    slideSmartB = DoubleField(default_value=1.0)
    sldbsmrt = slideSmartB

    slideRearSmartA = DoubleField(default_value=1.0)
    sldrerasmrt = slideRearSmartA

    slideRearSmartB = DoubleField(default_value=1.0)
    sldrerbsmrt = slideRearSmartB

    slideAngularSmartA = DoubleField(default_value=1.0)
    sldangasmrt = slideAngularSmartA

    slideAngularSmartB = DoubleField(default_value=1.0)
    sldangbsmrt = slideAngularSmartB

    slideAngularRearSmartA = DoubleField(default_value=1.0)
    sldangrerasmrt = slideAngularRearSmartA

    slideAngularRearSmartB = DoubleField(default_value=1.0)
    sldangrerbsmrt = slideAngularRearSmartB

    wrinkleSmartA = DoubleField(default_value=1.0)
    wrkasmrt = wrinkleSmartA

    wrinkleSmartB = DoubleField(default_value=1.0)
    wrkbsmrt = wrinkleSmartB

    wrinkleSpreadSmart = DoubleField(default_value=0.5)
    wrksprsmrt = wrinkleSpreadSmart

    COLLISIONSMART = COLLISIONSMARTEnumField(default_value=0)
    COLLSMRT = COLLISIONSMART

    flattenSmartA = DoubleField(default_value=1.0)
    fltasmrt = flattenSmartA

    flattenSmartB = DoubleField(default_value=1.0)
    fltbsmrt = flattenSmartB

    rigidSmartA = DoubleField(default_value=0.0)
    rigsmrta = rigidSmartA

    rigidSmartB = DoubleField(default_value=0.0)
    rigsmrtb = rigidSmartB

    collisionBlurIterationsSmart = LongField(default_value=0)
    colblritsmrt = collisionBlurIterationsSmart

    volumizeSmartA = DoubleField(default_value=1.0)
    vlmasmrt = volumizeSmartA

    volumizeSmartB = DoubleField(default_value=1.0)
    vlmbsmrt = volumizeSmartB

    volumizeOffsetSmartA = DoubleField(default_value=0.0)
    vlmoffsmrt = volumizeOffsetSmartA

    volumizePuffSmart = DoubleField(default_value=1.0)
    vlmpufsmrt = volumizePuffSmart

    volumizeDistSmart = DoubleField(default_value=1.0)
    vlmdsmrt = volumizeDistSmart

    volumizeFalloffSmart = DoubleField(default_value=1.0)
    vlmfallsmrt = volumizeFalloffSmart

    SMOOTH_POST = SMOOTH_POSTEnumField(default_value=0)
    SMTHPST = SMOOTH_POST

    smrtSmoothIterationsPost = LongField(default_value=5, min_value=0)
    smrtsmipst = smrtSmoothIterationsPost

    smrtSmoothStrengthPost = DoubleField(
        default_value=0.3, min_value=0.0, max_value=1.0
    )
    smrtsmstrpst = smrtSmoothStrengthPost

    smrtSmoothHoldPost = DoubleField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    smrthldpst = smrtSmoothHoldPost

    lockSmartWt = BoolField(default_value=False)
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

    selfPtsA = LongField(multi=True, default_value=0)
    slfpta = selfPtsA

    selfPtsB = LongField(multi=True, default_value=0)
    slfptb = selfPtsB


class SelfCollideDataAttrOperator(
    CompoundAttrOperator[SelfCollideDataPlugOperator]
):
    __slots__ = ()

    selfName = DataStringField()
    slfnam = selfName

    selfPtsA = LongField(multi=True, default_value=0)
    slfpta = selfPtsA

    selfPtsB = LongField(multi=True, default_value=0)
    slfptb = selfPtsB


class SelfCollideDataField(
    CompoundField[SelfCollideDataAttrOperator, SelfCollideDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SelfCollideDataAttrOperator
    PLUG_CLS = SelfCollideDataPlugOperator


class RelaxDataPlugOperator(CompoundPlugOperator["RelaxDataAttrOperator"]):
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

    numStretch = LongField(default_value=0, min_value=0)
    nstr = numStretch

    numBend = LongField(default_value=0, min_value=0)
    nbnd = numBend

    relaxSt = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    relst = relaxSt

    relaxBd = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    relbd = relaxBd

    numCons = DoubleField(multi=True, default_value=0.0)
    ncns = numCons

    numPts = LongField(default_value=0, min_value=0)
    npts = numPts

    ptsBase = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    ptsBS = ptsBase

    numTri = LongField(default_value=0, min_value=0)
    ntri = numTri

    relaxTri = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0, 0.0))
    reltri = relaxTri


class RelaxDataAttrOperator(CompoundAttrOperator[RelaxDataPlugOperator]):
    __slots__ = ()

    numStretch = LongField(default_value=0, min_value=0)
    nstr = numStretch

    numBend = LongField(default_value=0, min_value=0)
    nbnd = numBend

    relaxSt = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    relst = relaxSt

    relaxBd = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    relbd = relaxBd

    numCons = DoubleField(multi=True, default_value=0.0)
    ncns = numCons

    numPts = LongField(default_value=0, min_value=0)
    npts = numPts

    ptsBase = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    ptsBS = ptsBase

    numTri = LongField(default_value=0, min_value=0)
    ntri = numTri

    relaxTri = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0, 0.0))
    reltri = relaxTri


class RelaxDataField(
    CompoundField[RelaxDataAttrOperator, RelaxDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RelaxDataAttrOperator
    PLUG_CLS = RelaxDataPlugOperator

    numStretch = LongField(default_value=0, min_value=0)
    nstr = numStretch

    numBend = LongField(default_value=0, min_value=0)
    nbnd = numBend

    relaxSt = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    relst = relaxSt

    relaxBd = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    relbd = relaxBd

    numCons = DoubleField(multi=True, default_value=0.0)
    ncns = numCons

    numPts = LongField(default_value=0, min_value=0)
    npts = numPts

    ptsBase = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    ptsBS = ptsBase

    numTri = LongField(default_value=0, min_value=0)
    ntri = numTri

    relaxTri = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0, 0.0))
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

    relativePointX = DoubleField(default_value=0.0)
    relpx = relativePointX

    relativePointY = DoubleField(default_value=0.0)
    relpy = relativePointY

    relativePointZ = DoubleField(default_value=0.0)
    relpz = relativePointZ


class RelativePointAttrOperator(
    CompoundAttrOperator[RelativePointPlugOperator]
):
    __slots__ = ()

    relativePointX = DoubleField(default_value=0.0)
    relpx = relativePointX

    relativePointY = DoubleField(default_value=0.0)
    relpy = relativePointY

    relativePointZ = DoubleField(default_value=0.0)
    relpz = relativePointZ


class RelativePointField(
    CompoundField[RelativePointAttrOperator, RelativePointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RelativePointAttrOperator
    PLUG_CLS = RelativePointPlugOperator


class SmoothDataPlugOperator(CompoundPlugOperator["SmoothDataAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("smoothEntry", "smte"),
        ("ptToPtEntry", "ptpe"),
    )

    smoothEntry = CompoundField(multi=True, default_value=-1.0)
    smte = smoothEntry

    ptToPtEntry = CompoundField(multi=True, default_value=-1.0)
    ptpe = ptToPtEntry


class SmoothDataAttrOperator(CompoundAttrOperator[SmoothDataPlugOperator]):
    __slots__ = ()

    smoothEntry = CompoundField(multi=True, default_value=-1.0)
    smte = smoothEntry

    ptToPtEntry = CompoundField(multi=True, default_value=-1.0)
    ptpe = ptToPtEntry


class SmoothDataField(
    CompoundField[SmoothDataAttrOperator, SmoothDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SmoothDataAttrOperator
    PLUG_CLS = SmoothDataPlugOperator

    smoothEntry = CompoundField(multi=True, default_value=-1.0)
    smte = smoothEntry

    ptToPtEntry = CompoundField(multi=True, default_value=-1.0)
    ptpe = ptToPtEntry


class JiggleFramePlugOperator(CompoundPlugOperator["JiggleFrameAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("force", "frc"),)

    force = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    frc = force


class JiggleFrameAttrOperator(CompoundAttrOperator[JiggleFramePlugOperator]):
    __slots__ = ()

    force = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    frc = force


class JiggleFrameField(
    CompoundField[JiggleFrameAttrOperator, JiggleFramePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = JiggleFrameAttrOperator
    PLUG_CLS = JiggleFramePlugOperator


class CacheFramePlugOperator(CompoundPlugOperator["CacheFrameAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("cachePos", "cpos"),)

    cachePos = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    cpos = cachePos


class CacheFrameAttrOperator(CompoundAttrOperator[CacheFramePlugOperator]):
    __slots__ = ()

    cachePos = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
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
    CHILD_ATTR_NAMES = (("weightsMus", "wtm"),)

    weightsMus = DoubleField(multi=True, default_value=0.0, min_value=0.0)
    wtm = weightsMus


class WeightListMusAttrOperator(
    CompoundAttrOperator[WeightListMusPlugOperator]
):
    __slots__ = ()

    weightsMus = DoubleField(multi=True, default_value=0.0, min_value=0.0)
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
    CHILD_ATTR_NAMES = (("stickyWeightsMus", "stkwtm"),)

    stickyWeightsMus = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    stkwtm = stickyWeightsMus


class StickyWeightListMusAttrOperator(
    CompoundAttrOperator[StickyWeightListMusPlugOperator]
):
    __slots__ = ()

    stickyWeightsMus = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    stkwtm = stickyWeightsMus


class StickyWeightListMusField(
    CompoundField[
        StickyWeightListMusAttrOperator, StickyWeightListMusPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = StickyWeightListMusAttrOperator
    PLUG_CLS = StickyWeightListMusPlugOperator


class StickyWeightListMusBPlugOperator(
    CompoundPlugOperator["StickyWeightListMusBAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("stickyWeightsMusB", "stkwtmb"),)

    stickyWeightsMusB = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    stkwtmb = stickyWeightsMusB


class StickyWeightListMusBAttrOperator(
    CompoundAttrOperator[StickyWeightListMusBPlugOperator]
):
    __slots__ = ()

    stickyWeightsMusB = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    stkwtmb = stickyWeightsMusB


class StickyWeightListMusBField(
    CompoundField[
        StickyWeightListMusBAttrOperator, StickyWeightListMusBPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = StickyWeightListMusBAttrOperator
    PLUG_CLS = StickyWeightListMusBPlugOperator


class StickyWeightListMusCPlugOperator(
    CompoundPlugOperator["StickyWeightListMusCAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("stickyWeightsMusC", "stkwtmc"),)

    stickyWeightsMusC = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    stkwtmc = stickyWeightsMusC


class StickyWeightListMusCAttrOperator(
    CompoundAttrOperator[StickyWeightListMusCPlugOperator]
):
    __slots__ = ()

    stickyWeightsMusC = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    stkwtmc = stickyWeightsMusC


class StickyWeightListMusCField(
    CompoundField[
        StickyWeightListMusCAttrOperator, StickyWeightListMusCPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = StickyWeightListMusCAttrOperator
    PLUG_CLS = StickyWeightListMusCPlugOperator


class StickyListPlugOperator(CompoundPlugOperator["StickyListAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("stickyData", "stkData"),)

    stickyData = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0, 0.0))
    stkData = stickyData


class StickyListAttrOperator(CompoundAttrOperator[StickyListPlugOperator]):
    __slots__ = ()

    stickyData = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0, 0.0))
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
    CHILD_ATTR_NAMES = (("weightsDir", "wtd"),)

    weightsDir = DoubleField(multi=True, default_value=0.0, min_value=0.0)
    wtd = weightsDir


class WeightListDirAttrOperator(
    CompoundAttrOperator[WeightListDirPlugOperator]
):
    __slots__ = ()

    weightsDir = DoubleField(multi=True, default_value=0.0, min_value=0.0)
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
    CHILD_ATTR_NAMES = (("weightsSmartRegionA", "wtsmrtrega"),)

    weightsSmartRegionA = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtrega = weightsSmartRegionA


class WeightListSmartRegionAAttrOperator(
    CompoundAttrOperator[WeightListSmartRegionAPlugOperator]
):
    __slots__ = ()

    weightsSmartRegionA = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtrega = weightsSmartRegionA


class WeightListSmartRegionAField(
    CompoundField[
        WeightListSmartRegionAAttrOperator, WeightListSmartRegionAPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartRegionAAttrOperator
    PLUG_CLS = WeightListSmartRegionAPlugOperator


class WeightListSmartRegionBPlugOperator(
    CompoundPlugOperator["WeightListSmartRegionBAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("weightsSmartRegionB", "wtsmrtregb"),)

    weightsSmartRegionB = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtregb = weightsSmartRegionB


class WeightListSmartRegionBAttrOperator(
    CompoundAttrOperator[WeightListSmartRegionBPlugOperator]
):
    __slots__ = ()

    weightsSmartRegionB = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtregb = weightsSmartRegionB


class WeightListSmartRegionBField(
    CompoundField[
        WeightListSmartRegionBAttrOperator, WeightListSmartRegionBPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartRegionBAttrOperator
    PLUG_CLS = WeightListSmartRegionBPlugOperator


class WeightListSmartBulkPlugOperator(
    CompoundPlugOperator["WeightListSmartBulkAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("weightsSmartBulk", "wtsmrtblk"),)

    weightsSmartBulk = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtblk = weightsSmartBulk


class WeightListSmartBulkAttrOperator(
    CompoundAttrOperator[WeightListSmartBulkPlugOperator]
):
    __slots__ = ()

    weightsSmartBulk = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtblk = weightsSmartBulk


class WeightListSmartBulkField(
    CompoundField[
        WeightListSmartBulkAttrOperator, WeightListSmartBulkPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartBulkAttrOperator
    PLUG_CLS = WeightListSmartBulkPlugOperator


class WeightListSmartBulkAngularPlugOperator(
    CompoundPlugOperator["WeightListSmartBulkAngularAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("weightsSmartBulkAngular", "wtsmrtblkang"),)

    weightsSmartBulkAngular = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtblkang = weightsSmartBulkAngular


class WeightListSmartBulkAngularAttrOperator(
    CompoundAttrOperator[WeightListSmartBulkAngularPlugOperator]
):
    __slots__ = ()

    weightsSmartBulkAngular = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtblkang = weightsSmartBulkAngular


class WeightListSmartBulkAngularField(
    CompoundField[
        WeightListSmartBulkAngularAttrOperator,
        WeightListSmartBulkAngularPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartBulkAngularAttrOperator
    PLUG_CLS = WeightListSmartBulkAngularPlugOperator


class WeightListSmartBulkWidenPlugOperator(
    CompoundPlugOperator["WeightListSmartBulkWidenAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("weightsSmartBulkWiden", "wtsmrtblkwid"),)

    weightsSmartBulkWiden = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtblkwid = weightsSmartBulkWiden


class WeightListSmartBulkWidenAttrOperator(
    CompoundAttrOperator[WeightListSmartBulkWidenPlugOperator]
):
    __slots__ = ()

    weightsSmartBulkWiden = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtblkwid = weightsSmartBulkWiden


class WeightListSmartBulkWidenField(
    CompoundField[
        WeightListSmartBulkWidenAttrOperator,
        WeightListSmartBulkWidenPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartBulkWidenAttrOperator
    PLUG_CLS = WeightListSmartBulkWidenPlugOperator


class WeightListSmartSlidePlugOperator(
    CompoundPlugOperator["WeightListSmartSlideAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("weightsSmartSlide", "wtsmrtsld"),)

    weightsSmartSlide = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtsld = weightsSmartSlide


class WeightListSmartSlideAttrOperator(
    CompoundAttrOperator[WeightListSmartSlidePlugOperator]
):
    __slots__ = ()

    weightsSmartSlide = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtsld = weightsSmartSlide


class WeightListSmartSlideField(
    CompoundField[
        WeightListSmartSlideAttrOperator, WeightListSmartSlidePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartSlideAttrOperator
    PLUG_CLS = WeightListSmartSlidePlugOperator


class WeightListSmartSlideAngularPlugOperator(
    CompoundPlugOperator["WeightListSmartSlideAngularAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("weightsSmartSlideAngular", "wtsmrtsldang"),)

    weightsSmartSlideAngular = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtsldang = weightsSmartSlideAngular


class WeightListSmartSlideAngularAttrOperator(
    CompoundAttrOperator[WeightListSmartSlideAngularPlugOperator]
):
    __slots__ = ()

    weightsSmartSlideAngular = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtsldang = weightsSmartSlideAngular


class WeightListSmartSlideAngularField(
    CompoundField[
        WeightListSmartSlideAngularAttrOperator,
        WeightListSmartSlideAngularPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartSlideAngularAttrOperator
    PLUG_CLS = WeightListSmartSlideAngularPlugOperator


class WeightListSmartSmoothPlugOperator(
    CompoundPlugOperator["WeightListSmartSmoothAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("weightsSmartSmooth", "wtsmrtsmth"),)

    weightsSmartSmooth = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtsmth = weightsSmartSmooth


class WeightListSmartSmoothAttrOperator(
    CompoundAttrOperator[WeightListSmartSmoothPlugOperator]
):
    __slots__ = ()

    weightsSmartSmooth = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtsmth = weightsSmartSmooth


class WeightListSmartSmoothField(
    CompoundField[
        WeightListSmartSmoothAttrOperator, WeightListSmartSmoothPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartSmoothAttrOperator
    PLUG_CLS = WeightListSmartSmoothPlugOperator


class WeightListSmartWrinklePlugOperator(
    CompoundPlugOperator["WeightListSmartWrinkleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("weightsSmartWrinkle", "wtsmrtwrk"),)

    weightsSmartWrinkle = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtwrk = weightsSmartWrinkle


class WeightListSmartWrinkleAttrOperator(
    CompoundAttrOperator[WeightListSmartWrinklePlugOperator]
):
    __slots__ = ()

    weightsSmartWrinkle = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtwrk = weightsSmartWrinkle


class WeightListSmartWrinkleField(
    CompoundField[
        WeightListSmartWrinkleAttrOperator, WeightListSmartWrinklePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartWrinkleAttrOperator
    PLUG_CLS = WeightListSmartWrinklePlugOperator


class WeightListSmartFlattenPlugOperator(
    CompoundPlugOperator["WeightListSmartFlattenAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("weightsSmartFlatten", "wtsmrtflt"),)

    weightsSmartFlatten = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtflt = weightsSmartFlatten


class WeightListSmartFlattenAttrOperator(
    CompoundAttrOperator[WeightListSmartFlattenPlugOperator]
):
    __slots__ = ()

    weightsSmartFlatten = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtflt = weightsSmartFlatten


class WeightListSmartFlattenField(
    CompoundField[
        WeightListSmartFlattenAttrOperator, WeightListSmartFlattenPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartFlattenAttrOperator
    PLUG_CLS = WeightListSmartFlattenPlugOperator


class WeightListSmartVolumizePlugOperator(
    CompoundPlugOperator["WeightListSmartVolumizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("weightsSmartVolumize", "wtsmrtvol"),)

    weightsSmartVolumize = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtvol = weightsSmartVolumize


class WeightListSmartVolumizeAttrOperator(
    CompoundAttrOperator[WeightListSmartVolumizePlugOperator]
):
    __slots__ = ()

    weightsSmartVolumize = DoubleField(
        multi=True, default_value=0.0, min_value=0.0
    )
    wtsmrtvol = weightsSmartVolumize


class WeightListSmartVolumizeField(
    CompoundField[
        WeightListSmartVolumizeAttrOperator,
        WeightListSmartVolumizePlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = WeightListSmartVolumizeAttrOperator
    PLUG_CLS = WeightListSmartVolumizePlugOperator
