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

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()
