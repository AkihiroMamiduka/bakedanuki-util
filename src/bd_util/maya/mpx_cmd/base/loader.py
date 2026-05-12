# coding: utf-8

# maya
from maya import cmds

# self
from .... import logger as u_logger
from .cmd import MPxCommandBase

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class LoaderBase:
    def __init__(self, plugin: MPxCommandBase):
        self.plugin: MPxCommandBase = plugin
        self.path = self.plugin.__file__

    def load(self):
        if not self.is_loaded():
            cmds.loadPlugin(self.path)

    def unload(self):
        if self.is_loaded():
            cmds.unloadPlugin(self.path)

    def is_loaded(self):
        return cmds.pluginInfo(self.plugin.__name__, q=True, loaded=True)
