# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.annotation_shape import PositionField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.dt.matrix import DataMatrixField
from .....attr.define.std.dt.string import DataStringField


class GeneratedAnnotationShape(Shape):
    __slots__ = ()

    NODE_TYPE = "annotationShape"

    text = DataStringField()
    txt = text

    position = PositionField(default_value=(0.0, 0.0, 0.0))
    tp = position
    positionX = position.positionX
    tpx = positionX
    positionY = position.positionY
    tpy = positionY
    positionZ = position.positionZ
    tpz = positionZ

    dagObjectMatrix = DataMatrixField(multi=True, readable=False)
    dom = dagObjectMatrix

    displayArrow = BoolField(default_value=True)
    daro = displayArrow
