# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.hyper_view import (
    PositionField,
    ViewRectHighField,
    ViewRectLowField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class BuildDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UPSTREAM = 0
    DOWNSTREAM = 1
    ALL = 2


class BuildDirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    UPSTREAM = 0
    DOWNSTREAM = 1
    ALL = 2

    NAME_MAP = {
        UPSTREAM: "Upstream",
        DOWNSTREAM: "Downstream",
        ALL: "All",
    }


class BuildDirectionEnumField(
    EnumField[BuildDirectionEnumAttrOperator, BuildDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BuildDirectionEnumAttrOperator
    PLUG_CLS = BuildDirectionEnumPlugOperator


class GeneratedHyperView(DG):
    __slots__ = ()

    NODE_TYPE = "hyperView"

    position = PositionField(default_value=(0.0, 0.0))
    p = position
    positionX = position.positionX
    px = positionX
    positionY = position.positionY
    py = positionY

    viewRectLow = ViewRectLowField(default_value=(0.0, 0.0))
    vl = viewRectLow
    viewXL = viewRectLow.viewXL
    xl = viewXL
    viewYL = viewRectLow.viewYL
    yl = viewYL

    viewRectHigh = ViewRectHighField(default_value=(0.0, 0.0))
    vh = viewRectHigh
    viewXH = viewRectHigh.viewXH
    xh = viewXH
    viewYH = viewRectHigh.viewYH
    yh = viewYH

    dagView = BoolField(default_value=True)
    dag = dagView

    description = DataStringField()
    d = description

    focusNode = MessageField()
    fnd = focusNode

    rootNode = MessageField(multi=True)
    rnd = rootNode

    fullName = DataStringField()
    fn = fullName

    shortName = DataStringField()
    sn = shortName

    buildDirection = BuildDirectionEnumField(default_value=2)
    bd = buildDirection

    graphTraversalLimit = LongField(default_value=-1)
    gtl = graphTraversalLimit

    hyperLayout = MessageField()
    hl = hyperLayout
