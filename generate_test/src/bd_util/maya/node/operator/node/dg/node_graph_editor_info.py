# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.node_graph_editor_info import TabGraphInfoField
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class NodeGraphEditorInfo(DG):
    __slots__ = ()

    NODE_TYPE = "nodeGraphEditorInfo"

    parentEditorEmbedded = BoolField()
    pee = parentEditorEmbedded

    default = BoolField()
    def_ = default

    tabGraphInfo = TabGraphInfoField(multi=True)
    tgi = tabGraphInfo

    # TODO: tabGraphInfo.compoundInfo.compViewXL (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: tabGraphInfo.compoundInfo.compViewYL (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: tabGraphInfo.compoundInfo.compViewXH (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: tabGraphInfo.compoundInfo.compViewYH (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: tabGraphInfo.panelPosX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: tabGraphInfo.panelPosY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: tabGraphInfo.panelWidth (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: tabGraphInfo.panelHeight (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: tabGraphInfo.viewXL (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: tabGraphInfo.viewYL (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: tabGraphInfo.viewXH (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: tabGraphInfo.viewYH (attributeType=None, dataType=None) は未対応のため手動で追加してください
