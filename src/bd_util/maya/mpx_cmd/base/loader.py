# coding: utf-8

# maya
from maya import cmds

# self
from .... import logger as u_logger
from .cmd import MPxCommandBase

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class LoaderBase:
    plugin: MPxCommandBase

    @classmethod
    def path(cls) -> str:
        return cls.plugin.__file__

    @classmethod
    def name(cls) -> str:
        name: str = cls.plugin.__name__
        return name.split(".")[-1]

    @classmethod
    def load(cls):
        if not cls.is_loaded():
            cmds.loadPlugin(cls.path())

    @classmethod
    def unload(cls):
        if cls.is_loaded():
            cmds.unloadPlugin(cls.name())

    @classmethod
    def is_loaded(cls) -> bool:
        return cmds.pluginInfo(cls.name(), q=True, loaded=True)
