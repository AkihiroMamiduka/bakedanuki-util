# coding:utf-8

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()
    src = nodes.create.transform(name="src")
    dst = nodes.create.joint(name="dst")

    src.t.connect(dst.t)
    src.r.connect(dst.r)
    src.s.connect(dst.s)
    src.sh.connect(dst.sh)

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    logger.debug("----")
    src_plug = dst.t.src_plug()
    logger.debug(f"src_plug      : {src_plug}")
    logger.debug(f"type(src_plug): {type(src_plug)}")

    src_name = dst.t.src_name()
    logger.debug(f"src_name      : {src_name}")
    logger.debug(f"type(src_name): {type(src_name)}")

    src_plug_name = dst.t.src_plug_name()
    logger.debug(f"src_plug_name      : {src_plug_name}")
    logger.debug(f"type(src_plug_name): {type(src_plug_name)}")

    logger.debug("----")
    src_plug = dst.t.src_plug(filter_type=nodes.types.Joint)
    logger.debug(f"src_plug      : {src_plug}")
    logger.debug(f"type(src_plug): {type(src_plug)}")

    src_name = dst.t.src_name(filter_type=nodes.types.Joint)
    logger.debug(f"src_name      : {src_name}")
    logger.debug(f"type(src_name): {type(src_name)}")

    src_plug_name = dst.t.src_plug_name(filter_type=nodes.types.Joint)
    logger.debug(f"src_plug_name      : {src_plug_name}")
    logger.debug(f"type(src_plug_name): {type(src_plug_name)}")

    logger.debug("----")
    dst_plugs = src.t.dst_plugs()
    logger.debug(f"dst_plugs      : {dst_plugs}")
    logger.debug(f"type(dst_plugs): {type(dst_plugs)}")

    dst_names = src.t.dst_names()
    logger.debug(f"dst_names      : {dst_names}")
    logger.debug(f"type(dst_names): {type(dst_names)}")

    dst_plug_names = dst.t.dst_plug_names()
    logger.debug(f"dst_plug_names      : {dst_plug_names}")
    logger.debug(f"type(dst_plug_names): {type(dst_plug_names)}")

    logger.debug("----")
    dst_plugs = src.t.dst_plugs(
        filter_type=nodes.types.Transform, include_subclasses=False
    )
    logger.debug(f"dst_plugs      : {dst_plugs}")
    logger.debug(f"type(dst_plugs): {type(dst_plugs)}")

    dst_names = src.t.dst_names(
        filter_type=nodes.types.Transform, include_subclasses=False
    )
    logger.debug(f"dst_names      : {dst_names}")
    logger.debug(f"type(dst_names): {type(dst_names)}")

    dst_plug_names = dst.t.dst_plug_names(
        filter_type=nodes.types.Transform, include_subclasses=False
    )
    logger.debug(f"dst_plug_names      : {dst_plug_names}")
    logger.debug(f"type(dst_plug_names): {type(dst_plug_names)}")
