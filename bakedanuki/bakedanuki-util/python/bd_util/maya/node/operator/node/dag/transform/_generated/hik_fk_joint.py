# coding: utf-8
from ..joint import Joint
from .....attr.define.node_attr.hik_fk_joint import (
    RotateOffsetField,
    ScaleOffsetField,
    TranslateOffsetField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.dt.matrix import DataMatrixField


class LookEnumPlugOperator(EnumPlugOperator["LookEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    BONE = 1
    STICK = 2
    BOX = 3
    CIRCLE = 4
    SQUARE = 5


class LookEnumAttrOperator(EnumAttrOperator[LookEnumPlugOperator]):
    __slots__ = ()

    NONE = 0
    BONE = 1
    STICK = 2
    BOX = 3
    CIRCLE = 4
    SQUARE = 5

    NAME_MAP = {
        NONE: "None",
        BONE: "Bone",
        STICK: "Stick",
        BOX: "Box",
        CIRCLE: "Circle",
        SQUARE: "Square",
    }


class LookEnumField(EnumField[LookEnumAttrOperator, LookEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = LookEnumAttrOperator
    PLUG_CLS = LookEnumPlugOperator


class GeneratedHikFKJoint(Joint):
    __slots__ = ()

    NODE_TYPE = "hikFKJoint"

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

    look = LookEnumField(default_value=1)
    lk = look

    alternateGX = DataMatrixField()
    agx = alternateGX

    useAlternateGX = BoolField(default_value=False)
    uagx = useAlternateGX

    altConstraintTargetGX = DataMatrixField()
    atx = altConstraintTargetGX
