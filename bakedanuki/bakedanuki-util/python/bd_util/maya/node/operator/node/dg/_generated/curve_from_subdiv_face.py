# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class GeneratedCurveFromSubdivFace(DG):
    __slots__ = ()

    NODE_TYPE = "curveFromSubdivFace"

    inputSubdiv = TypedField()
    is_ = inputSubdiv

    minValue = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    min = minValue

    maxValue = DoubleField(
        default_value=-1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    max = maxValue

    relative = BoolField(default_value=False)
    r = relative

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve

    faceIndexL = LongField(multi=True, default_value=0)
    fil = faceIndexL

    faceIndexR = LongField(multi=True, default_value=0)
    fir = faceIndexR
