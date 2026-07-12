# coding: utf-8
from ._core import Transform
from ....attr.define.node_attr.hik_effector import (
    ColorField,
    PivotOffsetField,
    PreRotationField,
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


class HikEffector(Transform):
    __slots__ = ()

    NODE_TYPE = "hikEffector"

    joint = MessageField()
    jt = joint

    fkjoint = MessageField()
    fj = fkjoint

    pinning = PinningEnumField(default_value=0)
    pin = pinning

    handle = BoolField(multi=True, default_value=False, writable=False)
    ha = handle

    effectorID = LongField(default_value=0)
    ei = effectorID

    pivots = MessageField(multi=True)
    pvt = pivots

    pivotOffset = PivotOffsetField(default_value=(0.0, 0.0, 0.0))
    po = pivotOffset
    pivotOffsetX = pivotOffset.pivotOffsetX
    px = pivotOffsetX
    pivotOffsetY = pivotOffset.pivotOffsetY
    py = pivotOffsetY
    pivotOffsetZ = pivotOffset.pivotOffsetZ
    pz = pivotOffsetZ

    reachTranslation = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    rt = reachTranslation

    reachRotation = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    rr = reachRotation

    radius = DoubleField(default_value=1.0)
    radi = radius

    auxEffector = BoolField(default_value=False)
    aeff = auxEffector

    preRotation = PreRotationField(default_value=(0.0, 0.0, 0.0))
    pr = preRotation
    preRotationX = preRotation.preRotationX
    prx = preRotationX
    preRotationY = preRotation.preRotationY
    pry = preRotationY
    preRotationZ = preRotation.preRotationZ
    prz = preRotationZ

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
