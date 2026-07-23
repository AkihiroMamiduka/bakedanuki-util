# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.dt.string import DataStringField


class ScriptTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DEMAND = 0
    OPEN_SLASH_CLOSE = 1
    GUI_OPEN_SLASH_CLOSE = 2
    UI_CONFIGURATION_INTERNAL = 3
    SOFTWARE_RENDER = 4
    SOFTWARE_FRAME_RENDER = 5
    SCENE_CONFIGURATION_INTERNAL = 6
    TIME_CHANGED = 7


class ScriptTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DEMAND = 0
    OPEN_SLASH_CLOSE = 1
    GUI_OPEN_SLASH_CLOSE = 2
    UI_CONFIGURATION_INTERNAL = 3
    SOFTWARE_RENDER = 4
    SOFTWARE_FRAME_RENDER = 5
    SCENE_CONFIGURATION_INTERNAL = 6
    TIME_CHANGED = 7

    NAME_MAP = {
        DEMAND: "Demand",
        OPEN_SLASH_CLOSE: "Open/Close",
        GUI_OPEN_SLASH_CLOSE: "GUI Open/Close",
        UI_CONFIGURATION_INTERNAL: "UI Configuration (Internal)",
        SOFTWARE_RENDER: "Software Render",
        SOFTWARE_FRAME_RENDER: "Software Frame Render",
        SCENE_CONFIGURATION_INTERNAL: "Scene Configuration (Internal)",
        TIME_CHANGED: "Time Changed",
    }


class ScriptTypeEnumField(
    EnumField[ScriptTypeEnumAttrOperator, ScriptTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScriptTypeEnumAttrOperator
    PLUG_CLS = ScriptTypeEnumPlugOperator


class SourceTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MEL = 0
    PYTHON = 1


class SourceTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MEL = 0
    PYTHON = 1

    NAME_MAP = {
        MEL: "MEL",
        PYTHON: "Python",
    }


class SourceTypeEnumField(
    EnumField[SourceTypeEnumAttrOperator, SourceTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SourceTypeEnumAttrOperator
    PLUG_CLS = SourceTypeEnumPlugOperator


class IgnoreReferenceEditsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RECORD_REFERENCE_EDITS = 0
    IGNORE_REFERENCE_EDITS = 1


class IgnoreReferenceEditsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RECORD_REFERENCE_EDITS = 0
    IGNORE_REFERENCE_EDITS = 1

    NAME_MAP = {
        RECORD_REFERENCE_EDITS: "Record reference edits",
        IGNORE_REFERENCE_EDITS: "Ignore reference edits",
    }


class IgnoreReferenceEditsEnumField(
    EnumField[IgnoreReferenceEditsEnumAttrOperator, IgnoreReferenceEditsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IgnoreReferenceEditsEnumAttrOperator
    PLUG_CLS = IgnoreReferenceEditsEnumPlugOperator


class _GeneratedScript(DG):
    __slots__ = ()

    NODE_TYPE = "script"

    before = DataStringField()
    b = before

    after = DataStringField()
    a = after

    scriptType = ScriptTypeEnumField(default_value=0)
    st = scriptType

    sourceType = SourceTypeEnumField(default_value=0)
    stp = sourceType

    ignoreReferenceEdits = IgnoreReferenceEditsEnumField(default_value=0)
    ire = ignoreReferenceEdits
