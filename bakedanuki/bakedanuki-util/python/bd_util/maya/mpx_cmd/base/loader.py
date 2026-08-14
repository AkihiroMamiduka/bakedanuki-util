# coding: utf-8

from types import ModuleType
from typing import ClassVar

# maya
from maya import cmds

# self
from .... import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class LoaderBase:
    plugin: ClassVar[ModuleType]

    @classmethod
    def path(cls) -> str:
        plugin_path = cls.plugin.__file__
        if plugin_path is None:
            raise RuntimeError(
                f"Plugin module '{cls.plugin.__name__}' has no file path."
            )
        return plugin_path

    @classmethod
    def name(cls) -> str:
        name: str = cls.plugin.__name__
        return name.split(".")[-1]

    @classmethod
    def load(cls) -> None:
        if not cls.is_loaded():
            cmds.loadPlugin(cls.path())

    @classmethod
    def unload(cls) -> None:
        if cls.is_loaded():
            cmds.unloadPlugin(cls.name())

    @classmethod
    def is_loaded(cls) -> bool:
        loaded: object = cmds.pluginInfo(
            cls.name(),
            query=True,
            loaded=True,
        )
        if not isinstance(loaded, bool):
            raise TypeError(
                f"Unexpected pluginInfo result for '{cls.name()}': {loaded!r}"
            )
        return loaded
