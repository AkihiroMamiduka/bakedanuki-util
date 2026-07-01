# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField


class OutputsPlugOperator(
    CompoundPlugOperator["OutputsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("driver", "drvr"),
        ("filter", "ftr"),
    )

    driver = MessageField()
    drvr = driver

    filter = MessageField()
    ftr = filter


class OutputsAttrOperator(
    CompoundAttrOperator[OutputsPlugOperator]
):
    __slots__ = ()

    driver = MessageField()
    drvr = driver

    filter = MessageField()
    ftr = filter


class OutputsField(
    CompoundField[OutputsAttrOperator, OutputsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputsAttrOperator
    PLUG_CLS = OutputsPlugOperator
