# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField


class BlendListPlugOperator(
    CompoundPlugOperator["BlendListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("blendList_Hidden", "blh"),
        ("blendList_Raw", "blr"),
        ("blendList_Inmap", "bli"),
        ("blendList_Outmap", "blo"),
    )

    blendList_Hidden = TypedField()
    blh = blendList_Hidden

    blendList_Raw = TypedField()
    blr = blendList_Raw

    blendList_Inmap = CompoundField()
    bli = blendList_Inmap

    blendList_Outmap = CompoundField()
    blo = blendList_Outmap


class BlendListAttrOperator(
    CompoundAttrOperator[BlendListPlugOperator]
):
    __slots__ = ()

    blendList_Hidden = TypedField()
    blh = blendList_Hidden

    blendList_Raw = TypedField()
    blr = blendList_Raw

    blendList_Inmap = CompoundField()
    bli = blendList_Inmap

    blendList_Outmap = CompoundField()
    blo = blendList_Outmap


class BlendListField(
    CompoundField[BlendListAttrOperator, BlendListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlendListAttrOperator
    PLUG_CLS = BlendListPlugOperator


class BlendClipsPlugOperator(
    CompoundPlugOperator["BlendClipsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("firstClip", "fcl"),
        ("secondClip", "scl"),
    )

    firstClip = LongField()
    fcl = firstClip

    secondClip = LongField()
    scl = secondClip


class BlendClipsAttrOperator(
    CompoundAttrOperator[BlendClipsPlugOperator]
):
    __slots__ = ()

    firstClip = LongField()
    fcl = firstClip

    secondClip = LongField()
    scl = secondClip


class BlendClipsField(
    CompoundField[BlendClipsAttrOperator, BlendClipsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlendClipsAttrOperator
    PLUG_CLS = BlendClipsPlugOperator


class ClipFunctionPlugOperator(
    CompoundPlugOperator["ClipFunctionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("clipFunction_Hidden", "cfh"),
        ("clipFunction_Raw", "cfr"),
        ("clipFunction_Inmap", "cfi"),
        ("clipFunction_Outmap", "cfo"),
    )

    clipFunction_Hidden = TypedField()
    cfh = clipFunction_Hidden

    clipFunction_Raw = TypedField()
    cfr = clipFunction_Raw

    clipFunction_Inmap = CompoundField()
    cfi = clipFunction_Inmap

    clipFunction_Outmap = CompoundField()
    cfo = clipFunction_Outmap


class ClipFunctionAttrOperator(
    CompoundAttrOperator[ClipFunctionPlugOperator]
):
    __slots__ = ()

    clipFunction_Hidden = TypedField()
    cfh = clipFunction_Hidden

    clipFunction_Raw = TypedField()
    cfr = clipFunction_Raw

    clipFunction_Inmap = CompoundField()
    cfi = clipFunction_Inmap

    clipFunction_Outmap = CompoundField()
    cfo = clipFunction_Outmap


class ClipFunctionField(
    CompoundField[ClipFunctionAttrOperator, ClipFunctionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClipFunctionAttrOperator
    PLUG_CLS = ClipFunctionPlugOperator

    clipFunction_Hidden = TypedField()
    cfh = clipFunction_Hidden

    clipFunction_Raw = TypedField()
    cfr = clipFunction_Raw

    clipFunction_Inmap = CompoundField()
    cfi = clipFunction_Inmap

    clipFunction_Outmap = CompoundField()
    cfo = clipFunction_Outmap
