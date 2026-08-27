# coding:utf-8
import random

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()
    # translate
    #   src
    src_t_space = nodes.create.transform(name="src_t_space")
    src_t, _ = nodes.create.with_transform.locator(
        name="src_t", parent=src_t_space
    )

    #   dst
    dst_t_space = nodes.create.transform(name="dst_t_space")
    dst_t = nodes.create.transform(name="dst_t", parent=dst_t_space)
    #       world
    dst_t_world_x = nodes.create.transform(
        name="dst_t_world_x", parent=dst_t_space
    )
    dst_t_world_y = nodes.create.transform(
        name="dst_t_world_y", parent=dst_t_space
    )
    dst_t_world_z = nodes.create.transform(
        name="dst_t_world_z", parent=dst_t_space
    )
    #       local
    dst_t_local_x = nodes.create.transform(
        name="dst_t_local_x", parent=dst_t_space
    )
    dst_t_local_y = nodes.create.transform(
        name="dst_t_local_y", parent=dst_t_space
    )
    dst_t_local_z = nodes.create.transform(
        name="dst_t_local_z", parent=dst_t_space
    )
    #       object
    dst_t_object_x = nodes.create.transform(
        name="dst_t_object_x", parent=dst_t_space
    )
    dst_t_object_y = nodes.create.transform(
        name="dst_t_object_y", parent=dst_t_space
    )
    dst_t_object_z = nodes.create.transform(
        name="dst_t_object_z", parent=dst_t_space
    )

    # rotate
    #   src
    src_r_space = nodes.create.transform(name="src_r_space")
    src_r, _ = nodes.create.with_transform.locator(
        name="src_r", parent=src_r_space
    )

    #   dst
    #       joint
    dst_r_space = nodes.create.transform(name="dst_r_space")
    dst_r_trsf_r = nodes.create.transform(
        name="dst_r_trsf_r", parent=dst_r_space
    )
    dst_r_trsf_ra = nodes.create.transform(
        name="dst_r_trsf_ra", parent=dst_r_space
    )
    dst_r_joint_jo = nodes.create.joint(
        name="dst_r_joint_jo", parent=dst_r_space
    )
    dst_r_joint_r = nodes.create.joint(
        name="dst_r_joint_r", parent=dst_r_space
    )
    dst_r_joint_ra = nodes.create.joint(
        name="dst_r_joint_ra", parent=dst_r_space
    )

    # set
    #   translate
    #      src
    src_t_space.t.set(random.random(), random.random(), random.random())
    src_t_space.r.set(
        random.randint(-360, 360),
        random.randint(-360, 360),
        random.randint(-360, 360),
    )
    src_t_space.s.set(random.random(), random.random(), random.random())
    src_t.t.set(random.random(), random.random(), random.random())
    #      dst
    dst_t_space.t.set(random.random(), random.random(), random.random())
    dst_t_space.r.set(
        random.randint(-360, 360),
        random.randint(-360, 360),
        random.randint(-360, 360),
    )
    dst_t_space.s.set(random.random(), random.random(), random.random())
    #           object
    t_object_r = (
        random.randint(-360, 360),
        random.randint(-360, 360),
        random.randint(-360, 360),
    )
    dst_t_object_x.r.set(t_object_r)
    dst_t_object_y.r.set(t_object_r)
    dst_t_object_z.r.set(t_object_r)
    #   rotate
    #       src
    src_r_space.r.set(
        random.randint(-360, 360),
        random.randint(-360, 360),
        random.randint(-360, 360),
    )
    src_r.r.set(
        random.randint(-360, 360),
        random.randint(-360, 360),
        random.randint(-360, 360),
    )
    #       dst
    dst_r_space.r.set(
        random.randint(-360, 360),
        random.randint(-360, 360),
        random.randint(-360, 360),
    )
    r_jo = (
        random.randint(-360, 360),
        random.randint(-360, 360),
        random.randint(-360, 360),
    )
    r_r = (
        random.randint(-360, 360),
        random.randint(-360, 360),
        random.randint(-360, 360),
    )
    r_ra = (
        random.randint(-360, 360),
        random.randint(-360, 360),
        random.randint(-360, 360),
    )
    #           transform
    #               r
    dst_r_trsf_r.r.set(r_r)
    dst_r_trsf_r.ra.set(r_ra)
    #               ra
    dst_r_trsf_ra.r.set(r_r)
    dst_r_trsf_ra.ra.set(r_ra)
    #           joint
    #               jo
    dst_r_joint_jo.jo.set(r_jo)
    dst_r_joint_jo.r.set(r_r)
    dst_r_joint_jo.ra.set(r_ra)
    #               r
    dst_r_joint_r.jo.set(r_jo)
    dst_r_joint_r.r.set(r_r)
    dst_r_joint_r.ra.set(r_ra)
    #               ra
    dst_r_joint_ra.jo.set(r_jo)
    dst_r_joint_ra.r.set(r_r)
    dst_r_joint_ra.ra.set(r_ra)

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    # match
    #   translate
    dst_t.match_position(src_t)
    #       world
    dst_t_world_x.match_position(src_t, axes="x", space="world")
    dst_t_world_y.match_position(src_t, axes="y", space="world")
    dst_t_world_z.match_position(src_t, axes="z", space="world")
    #       local
    dst_t_local_x.match_position(src_t, axes="x", space="local")
    dst_t_local_y.match_position(src_t, axes="y", space="local")
    dst_t_local_z.match_position(src_t, axes="z", space="local")
    #       object
    dst_t_object_x.match_position(src_t, axes="x", space="object")
    dst_t_object_y.match_position(src_t, axes="y", space="object")
    dst_t_object_z.match_position(src_t, axes="z", space="object")
    #   rotate
    #       transform
    dst_r_trsf_r.match_rotation_to_rotate(src_r)
    dst_r_trsf_ra.match_rotation_to_rotate_axis(src_r)
    #       joint
    dst_r_joint_jo.match_rotation_to_joint_orient(src_r)
    dst_r_joint_r.match_rotation_to_rotate(src_r)
    dst_r_joint_ra.match_rotation_to_rotate_axis(src_r)

    nodes.modifier_manager.do_it_dg()
