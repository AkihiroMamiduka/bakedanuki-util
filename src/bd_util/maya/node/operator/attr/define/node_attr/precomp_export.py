# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField


class ExcludedExportItemListPlugOperator(
    CompoundPlugOperator["ExcludedExportItemListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("layer", "el"),
        ("pass", "ep"),
        ("camera", "ec"),
    )

    layer = MessageField()
    el = layer

    pass_ = MessageField(long_name="pass", short_name="ep")
    ep = pass_

    camera = MessageField()
    ec = camera


class ExcludedExportItemListAttrOperator(
    CompoundAttrOperator[ExcludedExportItemListPlugOperator]
):
    __slots__ = ()

    layer = MessageField()
    el = layer

    pass_ = MessageField(long_name="pass", short_name="ep")
    ep = pass_

    camera = MessageField()
    ec = camera


class ExcludedExportItemListField(
    CompoundField[ExcludedExportItemListAttrOperator, ExcludedExportItemListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExcludedExportItemListAttrOperator
    PLUG_CLS = ExcludedExportItemListPlugOperator
