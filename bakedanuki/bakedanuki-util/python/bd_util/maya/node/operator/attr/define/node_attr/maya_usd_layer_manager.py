# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.dt.string import DataStringField


class LayersPlugOperator(
    CompoundPlugOperator["LayersAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("identifier", "id"),
        ("fileFormatId", "fid"),
        ("serialized", "szd"),
        ("anonymous", "ann"),
    )

    identifier = DataStringField()
    id = identifier

    fileFormatId = DataStringField()
    fid = fileFormatId

    serialized = DataStringField()
    szd = serialized

    anonymous = BoolField(default_value=False)
    ann = anonymous


class LayersAttrOperator(
    CompoundAttrOperator[LayersPlugOperator]
):
    __slots__ = ()

    identifier = DataStringField()
    id = identifier

    fileFormatId = DataStringField()
    fid = fileFormatId

    serialized = DataStringField()
    szd = serialized

    anonymous = BoolField(default_value=False)
    ann = anonymous


class LayersField(
    CompoundField[LayersAttrOperator, LayersPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LayersAttrOperator
    PLUG_CLS = LayersPlugOperator
