# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)


class ColorPerVertexPlugOperator(
    CompoundPlugOperator["ColorPerVertexAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexColor", "vclr"),
    )

    vertexColor = CompoundField()
    vclr = vertexColor


class ColorPerVertexAttrOperator(
    CompoundAttrOperator[ColorPerVertexPlugOperator]
):
    __slots__ = ()

    vertexColor = CompoundField()
    vclr = vertexColor


class ColorPerVertexField(
    CompoundField[ColorPerVertexAttrOperator, ColorPerVertexPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorPerVertexAttrOperator
    PLUG_CLS = ColorPerVertexPlugOperator

    vertexColor = CompoundField()
    vclr = vertexColor
