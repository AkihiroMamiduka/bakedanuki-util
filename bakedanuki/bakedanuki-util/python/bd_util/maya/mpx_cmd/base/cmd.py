# coding: utf-8

import abc
from typing import ClassVar

# maya
from maya import OpenMaya as om1
from maya import OpenMayaMPx as ommpx
from maya.api import OpenMaya as om


class MPxCommandBase(ommpx.MPxCommand, metaclass=abc.ABCMeta):
    COMMAND_NAME: ClassVar[str] = "buildCmd"

    def __init__(self) -> None:
        super().__init__()

        self.mod = om.MDagModifier()

    @abc.abstractmethod
    def do_process(self, args: om1.MArgList) -> None:
        raise NotImplementedError

    def doIt(self, args: om1.MArgList) -> None:
        self.do_process(args)

        self.redoIt()

    def undoIt(self) -> None:
        self.mod.undoIt()

    def redoIt(self) -> None:
        self.mod.doIt()

    def isUndoable(self) -> bool:
        return True

    # initialize_plugin
    @classmethod
    def initialize_plugin(cls, plugin: om1.MObject) -> None:
        plugin_fn = ommpx.MFnPlugin(plugin)
        plugin_fn.registerCommand(
            cls.COMMAND_NAME, lambda: ommpx.asMPxPtr(cls())
        )

    @classmethod
    def uninitialize_plugin(cls, plugin: om1.MObject) -> None:
        plugin_fn = ommpx.MFnPlugin(plugin)
        plugin_fn.deregisterCommand(cls.COMMAND_NAME)
