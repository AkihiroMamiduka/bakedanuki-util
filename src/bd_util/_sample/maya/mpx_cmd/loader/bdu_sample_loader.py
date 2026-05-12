# codinf: utf-8

# self
from .....maya.mpx_cmd.base.loader import LoaderBase
from ..plugins import bdu_sample_plugin

loader = LoaderBase(bdu_sample_plugin)


def load():
    loader.load()


def unload():
    loader.unload()
