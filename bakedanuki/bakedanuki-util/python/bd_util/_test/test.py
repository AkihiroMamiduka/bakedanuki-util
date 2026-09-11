# coding:utf-8

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()

    trsf = nodes.create.transform(name="test")

    trsf.tx.keyframe.set_key(-100, frame=-100, out_tangent_type="flat")
    trsf.tx.keyframe.set_key(100, frame=100, in_tangent_type="flat")

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    samples = trsf.tx.sample_values(frames=range(-100, 101))

    trsf.ty.keyframe.set_keys(
        samples, in_tangent_type="auto", out_tangent_type="auto"
    )

    nodes.modifier_manager.do_it_dg()
