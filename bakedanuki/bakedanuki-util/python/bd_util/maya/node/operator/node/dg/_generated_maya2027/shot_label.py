# coding: utf-8
from .._core import DG
from ....attr.define.node_attr_maya2027.shot_label import ColorField
from ....attr.define.std.dt.string import DataStringField


class GeneratedShotLabel(DG):
    __slots__ = ()

    NODE_TYPE = "shotLabel"

    name_ = DataStringField(long_name="name", short_name="nm")
    nm = name_

    color = ColorField(
        default_value=(0.0, 0.0, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
    c = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB
