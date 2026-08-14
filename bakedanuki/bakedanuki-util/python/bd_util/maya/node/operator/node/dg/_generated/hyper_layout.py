# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.hyper_layout import (
    HyperPositionField,
    ImagePositionField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class GeneratedHyperLayout(DG):
    __slots__ = ()

    NODE_TYPE = "hyperLayout"

    hyperPosition = HyperPositionField(multi=True)
    hyp = hyperPosition

    imageName = DataStringField()
    img = imageName

    imagePosition = ImagePositionField(default_value=(0.0, 0.0))
    imp = imagePosition
    imagePositionX = imagePosition.imagePositionX
    ipx = imagePositionX
    imagePositionY = imagePosition.imagePositionY
    ipy = imagePositionY

    imageScale = FloatField(
        default_value=1.0, soft_min_value=0.1, soft_max_value=10.0
    )
    ims = imageScale

    allNodesFreeform = BoolField(default_value=False)
    anf = allNodesFreeform
