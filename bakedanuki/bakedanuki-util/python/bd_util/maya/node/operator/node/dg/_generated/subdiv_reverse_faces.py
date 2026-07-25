# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.typed import TypedField


class _GeneratedSubdivReverseFaces(DG):
    __slots__ = ()

    NODE_TYPE = "subdivReverseFaces"

    inSubdiv = TypedField()
    is_ = inSubdiv

    xMirror = BoolField(default_value=False)
    xm = xMirror

    yMirror = BoolField(default_value=False)
    ym = yMirror

    zMirror = BoolField(default_value=False)
    zm = zMirror

    outSubdiv = TypedField()
    os = outSubdiv
