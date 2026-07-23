# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)


class NormalPerVertexPlugOperator(
    CompoundPlugOperator["NormalPerVertexAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexNormal", "vn"),
    )

    vertexNormal = CompoundField(multi=True)
    vn = vertexNormal


class NormalPerVertexAttrOperator(
    CompoundAttrOperator[NormalPerVertexPlugOperator]
):
    __slots__ = ()

    vertexNormal = CompoundField(multi=True)
    vn = vertexNormal


class NormalPerVertexField(
    CompoundField[NormalPerVertexAttrOperator, NormalPerVertexPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalPerVertexAttrOperator
    PLUG_CLS = NormalPerVertexPlugOperator

    vertexNormal = CompoundField(multi=True)
    vn = vertexNormal
