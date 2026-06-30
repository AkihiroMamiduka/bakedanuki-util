# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.node_graph_editor_bookmark_info import (
    NodeInfoField,
    ViewRectHighField,
    ViewRectLowField,
)
from ...attr.define.std.dt.string import DataStringField


class NodeGraphEditorBookmarkInfo(DG):
    __slots__ = ()

    NODE_TYPE = "nodeGraphEditorBookmarkInfo"

    name = DataStringField()
    nm = name

    viewRectLow = ViewRectLowField()
    vl = viewRectLow
    viewXL = viewRectLow.viewXL
    xl = viewXL
    viewYL = viewRectLow.viewYL
    yl = viewYL

    viewRectHigh = ViewRectHighField()
    vh = viewRectHigh
    viewXH = viewRectHigh.viewXH
    xh = viewXH
    viewYH = viewRectHigh.viewYH
    yh = viewYH

    nodeInfo = NodeInfoField(multi=True)
    ni = nodeInfo
