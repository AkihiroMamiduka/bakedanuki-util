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

    curve_data = trsf.tx.keyframe.get_curve_data()
    if curve_data is not None:
        trsf.tz.keyframe.set_curve_data(curve_data)

    key_data = trsf.tx.keyframe.get_key_data(-100, 100)
    trsf.rx.keyframe.set_key_data(key_data)
    trsf.sx.keyframe.set_key_data(key_data)

    nodes.modifier_manager.do_it_dg()
