# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.dt.string import DataStringField


class BlindDataPresetsPlugOperator(
    CompoundPlugOperator["BlindDataPresetsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("bdPresetName", "bdpn"),
        ("bdPresetElements", "bdpe"),
    )

    bdPresetName = DataStringField()
    bdpn = bdPresetName

    bdPresetElements = CompoundField(multi=True)
    bdpe = bdPresetElements


class BlindDataPresetsAttrOperator(
    CompoundAttrOperator[BlindDataPresetsPlugOperator]
):
    __slots__ = ()

    bdPresetName = DataStringField()
    bdpn = bdPresetName

    bdPresetElements = CompoundField(multi=True)
    bdpe = bdPresetElements


class BlindDataPresetsField(
    CompoundField[BlindDataPresetsAttrOperator, BlindDataPresetsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlindDataPresetsAttrOperator
    PLUG_CLS = BlindDataPresetsPlugOperator


class BdUserInfoPlugOperator(CompoundPlugOperator["BdUserInfoAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("bdUserInfoName", "bdun"),
        ("bdUserInfoValue", "bduv"),
    )

    bdUserInfoName = DataStringField()
    bdun = bdUserInfoName

    bdUserInfoValue = DataStringField()
    bduv = bdUserInfoValue


class BdUserInfoAttrOperator(CompoundAttrOperator[BdUserInfoPlugOperator]):
    __slots__ = ()

    bdUserInfoName = DataStringField()
    bdun = bdUserInfoName

    bdUserInfoValue = DataStringField()
    bduv = bdUserInfoValue


class BdUserInfoField(
    CompoundField[BdUserInfoAttrOperator, BdUserInfoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BdUserInfoAttrOperator
    PLUG_CLS = BdUserInfoPlugOperator
