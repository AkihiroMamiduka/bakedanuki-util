# coding: utf-8
from .._core import DG
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField


class GeneratedPickMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "pickMatrix"

    inputMatrix = MatrixField()
    imat = inputMatrix

    useScale = BoolField(default_value=True)
    sca = useScale

    useTranslate = BoolField(default_value=True)
    tra = useTranslate

    useShear = BoolField(default_value=True)
    she = useShear

    useRotate = BoolField(default_value=True)
    rot = useRotate

    outputMatrix = MatrixField(writable=False)
    tmat = outputMatrix
