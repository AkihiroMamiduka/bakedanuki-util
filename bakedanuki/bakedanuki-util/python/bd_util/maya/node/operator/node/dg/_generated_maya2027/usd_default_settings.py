# coding: utf-8
from .._core import DG
from ....attr.define.std.dt.string import DataStringField


class GeneratedUsdDefaultSettings(DG):
    __slots__ = ()

    NODE_TYPE = "UsdDefaultSettings"

    serializedRootLayer = DataStringField()
    srl = serializedRootLayer

    serializedSessionLayer = DataStringField()
    ssl = serializedSessionLayer

    activeSettingsPath = DataStringField()
    asp = activeSettingsPath
