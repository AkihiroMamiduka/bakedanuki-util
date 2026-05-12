# coding: utf-8

import abc

# maya
from maya.api import OpenMaya as om
from maya import OpenMayaMPx as ommpx


class MPxCommandBase(ommpx.MPxCommand, metaclass=abc.ABCMeta):
    COMMAND_NAME = "buildCmd"

    def __init__(self):
        super().__init__()

        self.mod = om.MDagModifier()

    @abc.abstractmethod
    def do_process(self, args):
        pass

    def doIt(self, args):
        self.do_process(args)

        self.redoIt()

    def undoIt(self):
        self.mod.undoIt()

    def redoIt(self):
        self.mod.doIt()

    def isUndoable(self):
        return True

    # initialize_plugin
    @classmethod
    def initialize_plugin(cls, plugin):
        plugin_fn = ommpx.MFnPlugin(plugin)
        plugin_fn.registerCommand(
            cls.COMMAND_NAME, lambda: ommpx.asMPxPtr(cls())
        )

    @classmethod
    def uninitialize_plugin(cls, plugin):
        plugin_fn = ommpx.MFnPlugin(plugin)
        plugin_fn.deregisterCommand(cls.COMMAND_NAME)
