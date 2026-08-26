# coding:utf-8
import random

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()
    src_trsf = nodes.create.transform(name="src_transform")
    dst_trsf_rotate = nodes.create.transform(name="dst_transform_rotate")
    dst_trsf_rotate_axis = nodes.create.transform(
        name="dst_transform_rotate_axis"
    )

    src_joint = nodes.create.joint(name="src_joint")
    dst_joint_joint_orient = nodes.create.joint(name="dst_joint_joint_orient")
    dst_joint_rotate = nodes.create.joint(name="dst_joint_rotate")
    dst_joint_rotate_axis = nodes.create.joint(name="dst_joint_rotate_axis")

    # transform
    #   src
    src_trsf.r.set(
        random.randint(-360, 360),
        random.randint(-360, 360),
        random.randint(-360, 360),
    )
    src_trsf.rotateAxis.set(
        random.randint(-360, 360),
        random.randint(-360, 360),
        random.randint(-360, 360),
    )

    nodes.modifier_manager.do_it_dg()

    rot = src_trsf.r.get()
    r_axis = src_trsf.rotateAxis.get()
    #   dst
    #       rotate
    dst_trsf_rotate.r.set(rot)
    dst_trsf_rotate.rotateAxis.set(r_axis)
    #       rotate_axis
    dst_trsf_rotate_axis.r.set(rot)
    dst_trsf_rotate_axis.rotateAxis.set(r_axis)
    # joint
    #   src
    src_joint.jo.set(
        random.randint(-360, 360),
        random.randint(-360, 360),
        random.randint(-360, 360),
    )
    src_joint.r.set(rot)
    src_joint.rotateAxis.set(r_axis)

    nodes.modifier_manager.do_it_dg()

    jo = src_joint.jo.get()
    #   dst
    #       joint_orient
    dst_joint_joint_orient.jo.set(jo)
    dst_joint_joint_orient.r.set(rot)
    dst_joint_joint_orient.rotateAxis.set(r_axis)
    #       rotate
    dst_joint_rotate.jo.set(jo)
    dst_joint_rotate.r.set(rot)
    dst_joint_rotate.rotateAxis.set(r_axis)
    #       rotate_axis
    dst_joint_rotate_axis.jo.set(jo)
    dst_joint_rotate_axis.r.set(rot)
    dst_joint_rotate_axis.rotateAxis.set(r_axis)

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    dst_trsf_rotate.rotation_to_rotate()
    dst_trsf_rotate_axis.rotation_to_rotate_axis()

    dst_joint_joint_orient.rotation_to_joint_orient()
    dst_joint_rotate.rotation_to_rotate()
    dst_joint_rotate_axis.rotation_to_rotate_axis()

    nodes.modifier_manager.do_it_dg()
