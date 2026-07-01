# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class VisibilityModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NOT_OVERRIDDEN = 0
    INHERIT_PARENT_CONTROLLER = 1
    SHOW_ON_MOUSE_PROXIMITY = 2


class VisibilityModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NOT_OVERRIDDEN = 0
    INHERIT_PARENT_CONTROLLER = 1
    SHOW_ON_MOUSE_PROXIMITY = 2

    NAME_MAP = {
        NOT_OVERRIDDEN: "Not Overridden",
        INHERIT_PARENT_CONTROLLER: "Inherit Parent Controller",
        SHOW_ON_MOUSE_PROXIMITY: "Show On Mouse Proximity",
    }


class VisibilityModeEnumField(
    EnumField[VisibilityModeEnumAttrOperator, VisibilityModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VisibilityModeEnumAttrOperator
    PLUG_CLS = VisibilityModeEnumPlugOperator


class Controller(DG):
    __slots__ = ()

    NODE_TYPE = "controller"

    controllerObject = MessageField()
    act = controllerObject

    visibilityMode = VisibilityModeEnumField()
    vism = visibilityMode

    cycleWalkSibling = BoolField()
    cwsb = cycleWalkSibling

    parent = MessageField()
    pare = parent

    children = MessageField(multi=True)
    child = children

    parentprepopulate = BoolField()
    ppp = parentprepopulate

    prepopulate = BoolField()
    prep = prepopulate
