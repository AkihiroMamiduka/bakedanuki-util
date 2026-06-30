# coding: utf-8
from ._core import DG
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class PickMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "pickMatrix"

    inputMatrix = MatrixField()
    imat = inputMatrix

    useScale = BoolField()
    sca = useScale

    useTranslate = BoolField()
    tra = useTranslate

    useShear = BoolField()
    she = useShear

    useRotate = BoolField()
    rot = useRotate

    outputMatrix = MatrixField()
    tmat = outputMatrix
