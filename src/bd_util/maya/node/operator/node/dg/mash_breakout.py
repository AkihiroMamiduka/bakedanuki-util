# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_breakout import OutputsField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField


class MASH_Breakout(DG):
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
