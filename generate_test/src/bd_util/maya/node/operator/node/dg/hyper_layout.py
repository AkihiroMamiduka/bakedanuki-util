# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.hyper_layout import (
    HyperPositionField,
    ImagePositionField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class HyperLayout(DG):
    __slots__ = ()

    NODE_TYPE = "hyperLayout"

    hyperPosition = HyperPositionField(multi=True)
    hyp = hyperPosition

    imageName = DataStringField()
    img = imageName

    imagePosition = ImagePositionField()
    imp = imagePosition
    imagePositionX = imagePosition.imagePositionX
    ipx = imagePositionX
    imagePositionY = imagePosition.imagePositionY
    ipy = imagePositionY

    imageScale = FloatField()
    ims = imageScale

    allNodesFreeform = BoolField()
    anf = allNodesFreeform
