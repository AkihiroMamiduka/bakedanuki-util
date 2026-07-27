# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField


class GeneratedNodeGraphEditorBookmarks(DG):
    __slots__ = ()

    NODE_TYPE = "nodeGraphEditorBookmarks"

    bookmarks = MessageField(multi=True)
    b = bookmarks
