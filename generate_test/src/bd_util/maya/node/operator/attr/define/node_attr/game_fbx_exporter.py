# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.dt.string import DataStringField


class AnimClipsPlugOperator(
    CompoundPlugOperator["AnimClipsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("animClipName", "acn"),
        ("animClipStart", "acs"),
        ("animClipEnd", "ace"),
        ("exportAnimClip", "eac"),
        ("animClipId", "aci"),
        ("animClipSrcNode", "asn"),
    )

    animClipName = DataStringField()
    acn = animClipName

    animClipStart = FloatField()
    acs = animClipStart

    animClipEnd = FloatField()
    ace = animClipEnd

    exportAnimClip = BoolField()
    eac = exportAnimClip

    animClipId = LongField()
    aci = animClipId

    animClipSrcNode = DataStringField()
    asn = animClipSrcNode


class AnimClipsAttrOperator(
    CompoundAttrOperator[AnimClipsPlugOperator]
):
    __slots__ = ()

    animClipName = DataStringField()
    acn = animClipName

    animClipStart = FloatField()
    acs = animClipStart

    animClipEnd = FloatField()
    ace = animClipEnd

    exportAnimClip = BoolField()
    eac = exportAnimClip

    animClipId = LongField()
    aci = animClipId

    animClipSrcNode = DataStringField()
    asn = animClipSrcNode


class AnimClipsField(
    CompoundField[AnimClipsAttrOperator, AnimClipsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AnimClipsAttrOperator
    PLUG_CLS = AnimClipsPlugOperator
