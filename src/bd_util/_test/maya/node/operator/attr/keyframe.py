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
    insert_key()
    delete_key()
    set_tangent()


def set_key():
    test_str.title("set_key")
    # ノードを作成し接続
    modifier_manager = ModifierManager()
    node = PlusMinusAverage.create(modifier_manager, name="test_set_key")
    modifier_manager.do_it_dg()
    plug = node.input3D[0].input3Dx
    for i in range(COUNT):
        plug.keyframe.set_direct(i, i)
    modifier_manager.do_it_dg()


def insert_key():
    test_str.title("insert_key")
    # ノードを作成し接続
    modifier_manager = ModifierManager()
    node = PlusMinusAverage.create(modifier_manager, name="test_insert_key")
    modifier_manager.do_it_dg()
    plug = node.input3D[0].input3Dx
    plug.keyframe.set_direct(100, 100)
    plug.keyframe.set_direct(200, 200)
    plug.keyframe.insert_direct(150, breakdown=False)
    modifier_manager.do_it_dg()


def delete_key():
    test_str.title("delete_key")
    # ノードを作成し接続
    modifier_manager = ModifierManager()
    node = PlusMinusAverage.create(modifier_manager, name="test_delete_key")
    modifier_manager.do_it_dg()
    plug = node.input3D[0].input3Dx
    plug.keyframe.set_direct(100, 100)
    plug.keyframe.delete_anim_curve()
    modifier_manager.do_it_dg()


def set_tangent():
    test_str.title("set_tangent")
    # ノードを作成し接続
    modifier_manager = ModifierManager()
    node = PlusMinusAverage.create(modifier_manager, name="test_set_tangent")
    modifier_manager.do_it_dg()
    plug = node.input3D[0].input3Dx
    tangent = plug.keyframe.tangent
    tangent_types = [
        (tangent.auto, tangent.clamped),
        (tangent.fast, tangent.flat),
        (tangent.linear, tangent.plateau),
        (tangent.slow, tangent.spline),
        (tangent.step, tangent.stepnext),
    ]
    for i, (in_tangent, out_tangent) in enumerate(tangent_types):
        plug.keyframe.set_direct(
            i,
            i * 10,
            in_tangent_type=in_tangent,
            out_tangent_type=out_tangent,
        )
    modifier_manager.do_it_dg()
