# coding:utf-8

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()

    trsf = nodes.create.transform(name="test")

    layer = nodes.create.animLayer(name="Sample")

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    trsf.tx.keyframe.set_key(-100, frame=-100, out_tangent_type="flat")
    trsf.tx.keyframe.set_key(100, frame=100, in_tangent_type="flat")

    trsf.rx.keyframe.set_key(-100, frame=-100, out_tangent_type="flat")
    trsf.rx.keyframe.set_key(100, frame=100, in_tangent_type="flat")

    nodes.modifier_manager.do_it_dg()

    layer.add_nodes([trsf])
    trsf.tx.keyframe.anim_layer(layer).set_keys(
        [(i, i * 2) for i in range(-100, 101)]
    )

    nodes.modifier_manager.do_it_dg()

    samples = trsf.tx.sample_values(frames=range(-100, 101))
    trsf.ty.keyframe.set_keys(
        samples, in_tangent_type="auto", out_tangent_type="auto"
    )

    samples = trsf.rx.sample_values(frames=range(-100, 101))
    trsf.ry.keyframe.set_keys(
        samples, in_tangent_type="auto", out_tangent_type="auto"
    )

    nodes.modifier_manager.do_it_dg()

    trsf.ty.keyframe.reduce_keys(-50, 50, tolerance=0.01)
    trsf.ry.keyframe.reduce_keys(-50, 50, tolerance=1)

    nodes.modifier_manager.do_it_dg()
