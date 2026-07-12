# coding: utf-8
from ._core import Transform
from ....attr.define.node_attr.hik_ik_effector import (
    ColorField,
    JointOrientField,
    PivotOffsetField,
    RotateOffsetField,
    ScaleOffsetField,
    TranslateOffsetField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.dt.matrix import DataMatrixField


class PinningEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UNPINNED = 0
    PINTRANSLATE = 1
    PINROTATE = 2
    PINALL = 3


class PinningEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    UNPINNED = 0
    PINTRANSLATE = 1
    PINROTATE = 2
    PINALL = 3

    NAME_MAP = {
        UNPINNED: "unpinned",
        PINTRANSLATE: "pinTranslate",
        PINROTATE: "pinRotate",
        PINALL: "pinAll",
    }


class PinningEnumField(
    EnumField[PinningEnumAttrOperator, PinningEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PinningEnumAttrOperator
    PLUG_CLS = PinningEnumPlugOperator


class MarkerLookEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CUBE = 0
    HARD_CROSS = 1
    LIGHT_CROSS = 2
    SPHERE = 3


class MarkerLookEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CUBE = 0
    HARD_CROSS = 1
    LIGHT_CROSS = 2
    SPHERE = 3

    NAME_MAP = {
        CUBE: "cube",
        HARD_CROSS: "hard cross",
        LIGHT_CROSS: "light cross",
        SPHERE: "sphere",
    }


class MarkerLookEnumField(
    EnumField[MarkerLookEnumAttrOperator, MarkerLookEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MarkerLookEnumAttrOperator
    PLUG_CLS = MarkerLookEnumPlugOperator


class LookEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    CIRCLE = 1
    SQUARE = 2
    CUBE = 3
    SPHERE = 4
    HARD_CROSS = 5
    LIGHT_CROSS = 6


class LookEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    CIRCLE = 1
    SQUARE = 2
    CUBE = 3
    SPHERE = 4
    HARD_CROSS = 5
    LIGHT_CROSS = 6

    NAME_MAP = {
        NONE: "None",
        CIRCLE: "Circle",
        SQUARE: "Square",
        CUBE: "Cube",
        SPHERE: "Sphere",
        HARD_CROSS: "Hard Cross",
        LIGHT_CROSS: "Light Cross",
    }


class LookEnumField(
    EnumField[LookEnumAttrOperator, LookEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LookEnumAttrOperator
    PLUG_CLS = LookEnumPlugOperator


class HikIKEffector(Transform):
    __slots__ = ()

    NODE_TYPE = "hikIKEffector"

    pinning = PinningEnumField(default_value=0)
    pin = pinning

    effectorID = LongField(default_value=0)
    ei = effectorID

    auxiliaries = MessageField(multi=True, readable=False)
    aux = auxiliaries

    reachTranslation = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    rt = reachTranslation

    reachRotation = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    rr = reachRotation

    radius = DoubleField(default_value=1.0)
    radi = radius

    auxEffector = BoolField(default_value=False)
    aeff = auxEffector

    jointOrient = JointOrientField(default_value=(0.0, 0.0, 0.0))
    jo = jointOrient
    jointOrientX = jointOrient.jointOrientX
    jox = jointOrientX
    jointOrientY = jointOrient.jointOrientY
    joy = jointOrientY
    jointOrientZ = jointOrient.jointOrientZ
    joz = jointOrientZ

    color = ColorField(default_value=(1.0, 0.0, 0.0))
    col = color
    colorR = color.colorR
    clr = colorR
    colorG = color.colorG
    clg = colorG
    colorB = color.colorB
    clb = colorB

    alpha = FloatField(default_value=1.0)
    alp = alpha

    markerLook = MarkerLookEnumField(default_value=3)
    mkl = markerLook

    translateOffset = TranslateOffsetField(default_value=(0.0, 0.0, 0.0))
    tof = translateOffset
    translateOffsetX = translateOffset.translateOffsetX
    tox = translateOffsetX
    translateOffsetY = translateOffset.translateOffsetY
    toy = translateOffsetY
    translateOffsetZ = translateOffset.translateOffsetZ
    toz = translateOffsetZ

    rotateOffset = RotateOffsetField(default_value=(0.0, 0.0, 0.0))
    rof = rotateOffset
    rotateOffsetX = rotateOffset.rotateOffsetX
    rox = rotateOffsetX
    rotateOffsetY = rotateOffset.rotateOffsetY
    roy = rotateOffsetY
    rotateOffsetZ = rotateOffset.rotateOffsetZ
    roz = rotateOffsetZ

    scaleOffset = ScaleOffsetField(default_value=(1.0, 1.0, 1.0))
    sof = scaleOffset
    scaleOffsetX = scaleOffset.scaleOffsetX
    sox = scaleOffsetX
    scaleOffsetY = scaleOffset.scaleOffsetY
    soy = scaleOffsetY
    scaleOffsetZ = scaleOffset.scaleOffsetZ
    soz = scaleOffsetZ

    look = LookEnumField(default_value=4)
    lk = look

    pinT = BoolField(default_value=False, writable=False)
    pint = pinT

    pinR = BoolField(default_value=False, writable=False)
    pinr = pinR

    pivotOffset = PivotOffsetField(default_value=(0.0, 0.0, 0.0))
    po = pivotOffset
    pivotOffsetX = pivotOffset.pivotOffsetX
    px = pivotOffsetX
    pivotOffsetY = pivotOffset.pivotOffsetY
    py = pivotOffsetY
    pivotOffsetZ = pivotOffset.pivotOffsetZ
    pz = pivotOffsetZ

    alternateGX = DataMatrixField()
    agx = alternateGX

    useAlternateGX = BoolField(default_value=False)
    uagx = useAlternateGX

    altConstraintTargetGX = DataMatrixField()
    atx = altConstraintTargetGX
