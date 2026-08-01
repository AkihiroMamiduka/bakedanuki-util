# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_breakout import OutputsField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)
from ....attr.define.std.at.typed import TypedField


class GeneratedMASHBreakout(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Breakout"

    outputs = OutputsField(multi=True, writable=False)

    translateX = FloatField()

    translateY = FloatField()

    translateZ = FloatField()

    rotateX = DoubleAngleField()

    rotateY = DoubleAngleField()

    rotateZ = DoubleAngleField()

    scaleX = FloatField()

    scaleY = FloatField()

    scaleZ = FloatField()

    colorX = FloatField()
    colorx = colorX

    colorY = FloatField()
    colory = colorY

    colorZ = FloatField()
    colorz = colorZ

    velocityVectorX = FloatField()
    velocityVectorx = velocityVectorX

    velocityVectorY = FloatField()
    velocityVectory = velocityVectorY

    velocityVectorZ = FloatField()
    velocityVectorz = velocityVectorZ

    angularVelocityVectorX = FloatField()
    angularVelocityVectorx = angularVelocityVectorX

    angularVelocityVectorY = FloatField()
    angularVelocityVectory = angularVelocityVectorY

    angularVelocityVectorZ = FloatField()
    angularVelocityVectorz = angularVelocityVectorZ

    inputPoints = TypedField()

    idStart = LongField(default_value=0, min_value=0, soft_max_value=100)
