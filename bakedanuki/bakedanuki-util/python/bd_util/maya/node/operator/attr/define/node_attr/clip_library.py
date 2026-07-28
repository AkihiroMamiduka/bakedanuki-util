# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.typed import TypedField


class ClipEvalListPlugOperator(
    CompoundPlugOperator["ClipEvalListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("clipEval", "cev"),)

    clipEval = CompoundField(multi=True)
    cev = clipEval


class ClipEvalListAttrOperator(CompoundAttrOperator[ClipEvalListPlugOperator]):
    __slots__ = ()

    clipEval = CompoundField(multi=True)
    cev = clipEval


class ClipEvalListField(
    CompoundField[ClipEvalListAttrOperator, ClipEvalListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClipEvalListAttrOperator
    PLUG_CLS = ClipEvalListPlugOperator


class CharacterdataPlugOperator(
    CompoundPlugOperator["CharacterdataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("characterMapping", "cm"),
        ("clipIndexMapping", "cim"),
    )

    characterMapping = TypedField()
    cm = characterMapping

    clipIndexMapping = TypedField()
    cim = clipIndexMapping


class CharacterdataAttrOperator(
    CompoundAttrOperator[CharacterdataPlugOperator]
):
    __slots__ = ()

    characterMapping = TypedField()
    cm = characterMapping

    clipIndexMapping = TypedField()
    cim = clipIndexMapping


class CharacterdataField(
    CompoundField[CharacterdataAttrOperator, CharacterdataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CharacterdataAttrOperator
    PLUG_CLS = CharacterdataPlugOperator
