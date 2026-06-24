# coding: utf-8

# self
from ...... import logger as u_logger
from ..... import str as test_str
from ......maya.node.modifier import ModifierManager
from ......maya.node.operator.node.dg.plus_minus_average import (
    PlusMinusAverage,
)

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)

COUNT = 100000


def main():
    set_key()


def set_key():
    test_str.title("set_key")
    # ノードを作成し接続
    modifier_manager = ModifierManager()
    node = PlusMinusAverage.create(modifier_manager)
    modifier_manager.do_it_dg()
    plug = node.input3D[0].input3Dx
    for i in range(COUNT):
        plug.set_key_direct(i, i)
    modifier_manager.do_it_dg()
