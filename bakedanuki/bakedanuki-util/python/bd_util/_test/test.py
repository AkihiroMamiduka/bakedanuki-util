# coding:utf-8

# self
import bd_util as bdu


def main():
    nodes = bdu.Nodes()
    transform, loc = nodes.create.with_transform.locator(name="locator")
    transform.translate.set(3, 6, 9)
    loc.localScale.set(2, 3, 4)

    cam = nodes.create.camera(name="camera", parent=transform)
    cam.focalLength.set(100)

    jnt = nodes.create.joint(name="jnt_locator")
    jnt.drawStyle.set(jnt.drawStyle.NONE)
    jnt.rotate.set(45, 30, 90)
    jnt_loc = nodes.create.locator(name=f"{jnt.name}Shape", parent=jnt)
    jnt_loc.localScale.set(2, 5, 8)

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()
