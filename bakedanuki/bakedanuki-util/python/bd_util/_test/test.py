# coding:utf-8

# self
import bd_util as bdu


def main():
    nodes = bdu.Nodes()
    transform = nodes.create.transform(name="shape_parent")
    loc = nodes.create.locator(name="shape_loc", parent=transform)
    loc.localScale.set(2, 3, 4)

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()
