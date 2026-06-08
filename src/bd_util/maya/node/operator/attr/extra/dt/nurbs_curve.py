# coding: utf-8

# self
from ...std.dt.nurbs_curve import DataNurbsCurveField


class ExtraDataNurbsCurveField(DataNurbsCurveField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
