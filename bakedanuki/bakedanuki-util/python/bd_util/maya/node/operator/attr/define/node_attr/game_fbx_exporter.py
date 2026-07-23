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

    animClipStart = FloatField(default_value=0.0)
    acs = animClipStart

    animClipEnd = FloatField(default_value=0.0)
    ace = animClipEnd

    exportAnimClip = BoolField(default_value=True)
    eac = exportAnimClip

    animClipId = LongField(default_value=0)
    aci = animClipId

    animClipSrcNode = DataStringField()
    asn = animClipSrcNode


class AnimClipsAttrOperator(
    CompoundAttrOperator[AnimClipsPlugOperator]
):
    __slots__ = ()

    animClipName = DataStringField()
    acn = animClipName

    animClipStart = FloatField(default_value=0.0)
    acs = animClipStart

    animClipEnd = FloatField(default_value=0.0)
    ace = animClipEnd

    exportAnimClip = BoolField(default_value=True)
    eac = exportAnimClip

    animClipId = LongField(default_value=0)
    aci = animClipId

    animClipSrcNode = DataStringField()
    asn = animClipSrcNode


class AnimClipsField(
    CompoundField[AnimClipsAttrOperator, AnimClipsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AnimClipsAttrOperator
    PLUG_CLS = AnimClipsPlugOperator
