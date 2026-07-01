# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.matrix import DataMatrixField


class SubdMapSewMove(DG):
    __slots__ = ()

    NODE_TYPE = "subdMapSewMove"

    outSubdiv = TypedField()
    os = outSubdiv

    inSubdiv = TypedField()
    is_ = inSubdiv

    cachedSubdiv = TypedField()
    ic = cachedSubdiv

    inputComponents = TypedField()
    ics = inputComponents

    inputMatrix = DataMatrixField()
    ix = inputMatrix

    worldSpace = BoolField()
    ws = worldSpace

    manipMatrix = DataMatrixField()
    mp = manipMatrix

    limitPieceSize = BoolField()
    lps = limitPieceSize

    numberFaces = LongField()
    nf = numberFaces
