# coding:utf-8

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()

    trsf = nodes.create.transform(name="test")
    trsf.tx.keyframe.set(
        -100,
        frame=-100,
        in_tangent_type="linear",
        out_tangent_type="step",
    )
    trsf.tx.keyframe.set(
        100,
        frame=100,
        in_tangent_type="slow",
        out_tangent_type="linear",
    )

    trsf.tx.keyframe.insert(frame=15)
    trsf.tx.keyframe.set_tangent(
        frame=15,
        in_tangent_type="flat",
        out_tangent_type="step",
    )

    trsf.tx.keyframe.delete_key(15)
    trsf.tx.keyframe.delete_keys(-200, 200)

    trsf.tx.keyframe.set(
        100,
        frame=10,
        in_tangent_type="linear",
        out_tangent_type="linear",
    )

    trsf.tx.keyframe.delete_anim_curve()

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()
