"""mayapy で Fin 専用型の属性と境界を確認する。"""

import argparse
from itertools import product
import math
from pathlib import Path

import maya.standalone
from maya import cmds
from maya.api import OpenMaya as om


NODE_TYPES = (
    ("bdShpL_CubeWithFin", 0x00142724, "geometry"),
    ("bdShpL_DeformableCubeWithFin", 0x00142725, "subscene"),
)
FIN_ATTRIBUTES = (
    ("shapeFinType", "sfnt", "enum", 0),
    ("shapeFinHeight", "sfnh", "doubleLinear", 0.5),
    ("shapeFinWidthScale", "sfnws", "double", 1.0),
)


def assert_bounds(shape, expected):
    path = om.MSelectionList().add(shape).getDagPath(0)
    bounds = om.MFnDagNode(path).boundingBox
    actual = (*tuple(bounds.min)[:3], *tuple(bounds.max)[:3])
    assert all(math.isclose(a, b, abs_tol=1e-8) for a, b in zip(actual, expected)), (shape, actual, expected)


def check_attributes(shape, editable, deformable):
    for reserved in ("shapeFin", "shapeFinTemplate"):
        assert not cmds.attributeQuery(reserved, node=shape, exists=True)
    assert cmds.attributeQuery("shapeDeformMatrix", node=shape, exists=True) == deformable
    for name, short_name, attr_type, default in FIN_ATTRIBUTES:
        assert cmds.attributeQuery(name, node=shape, exists=True) == editable
        if not editable:
            continue
        plug = f"{shape}.{short_name}"
        assert cmds.attributeQuery(name, node=shape, shortName=True) == short_name
        assert cmds.getAttr(plug, type=True) == attr_type
        assert cmds.getAttr(plug) == default
        assert cmds.getAttr(plug, channelBox=True)
        assert not cmds.getAttr(plug, keyable=True)
        assert not cmds.attributeQuery(name, node=shape, connectable=True)
        assert cmds.attributeQuery(name, node=shape, storable=True)
    if editable:
        assert cmds.attributeQuery("shapeFinType", node=shape, listEnum=True) == ["Standard:Tapered"]


def check_dummy_bools(shape, count):
    names = {name for name in cmds.listAttr(shape) if name.startswith("researchDummyBool")}
    assert names == {f"researchDummyBool{index}" for index in range(1, count + 1)}
    node = om.MFnDependencyNode(om.MSelectionList().add(shape).getDependNode(0))
    for name in names:
        plug = f"{shape}.{name}"
        attribute = om.MFnAttribute(node.attribute(name))
        assert cmds.getAttr(plug, type=True) == "bool"
        assert cmds.getAttr(plug) is False
        assert not cmds.getAttr(plug, channelBox=True)
        assert not attribute.keyable and not attribute.connectable
        assert not attribute.affectsAppearance and not attribute.affectsWorldSpace


def check_shape(node_type, type_id, renderer, editable, dummy_bools):
    shape = cmds.createNode(node_type)
    deformable = renderer == "subscene"
    assert om.MNodeClass(node_type).typeId.id() == type_id
    assert cmds.getClassification(node_type) == [f"drawdb/{renderer}/{node_type}"]
    check_attributes(shape, editable, deformable)
    check_dummy_bools(shape, dummy_bools)
    default_bounds = (-0.5, -0.5, -0.5, 0.5, 1.0, 0.5)
    assert_bounds(shape, default_bounds)

    if editable:
        cmds.setAttr(f"{shape}.sfnt", 1)
        cmds.setAttr(f"{shape}.sfnh", 1.25)
        cmds.setAttr(f"{shape}.sfnws", -2.0)
        assert_bounds(shape, (-1.0, -0.5, -0.5, 1.0, 1.75, 0.5))
        cmds.setAttr(f"{shape}.sfnh", 0.0)
        assert_bounds(shape, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5))
        cmds.setAttr(f"{shape}.sfnt", 0)
        cmds.setAttr(f"{shape}.sfnh", 0.5)
        cmds.setAttr(f"{shape}.sfnws", 1.0)
        assert_bounds(shape, default_bounds)

    cmds.setAttr(f"{shape}.s1a", 4)
    cmds.setAttr(f"{shape}.s2a", 1)
    cmds.setAttr(f"{shape}.sbsp1p", 1.25)
    assert_bounds(shape, (-1.0, -0.5, -0.5, 0.5, 0.5, 1.25))
    if deformable:
        matrix = om.MMatrix((
            (-2.0, 0.5, 0.25, 0.0),
            (1.5, 3.0, -0.5, 0.0),
            (0.25, -0.5, 0.75, 0.0),
            (4.0, -5.0, 6.0, 1.0),
        ))
        cmds.setAttr(f"{shape}.shapeDeformMatrix", *list(matrix), type="matrix")
        body = list(product((-0.5, 0.5), (-0.5, 0.5), (-0.5, 1.25)))
        fin = list(product((-1.0, -0.5), (0.0,), (-0.5, 1.25)))
        transformed = [om.MPoint(*point) * matrix for point in body + fin]
        expected = tuple(
            extreme(point[axis] for point in transformed)
            for extreme in (min, max) for axis in range(3)
        )
        assert_bounds(shape, expected)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plugin", type=Path)
    parser.add_argument("--attributes", action="store_true")
    parser.add_argument("--dummy-bools", type=int, choices=(0, 100), default=0)
    args = parser.parse_args()
    path = args.plugin.resolve(strict=True)
    maya.standalone.initialize(name="python")
    try:
        plugin, = cmds.loadPlugin(str(path), quiet=True)
        assert Path(cmds.pluginInfo(plugin, query=True, path=True)).resolve() == path
        assert set(cmds.pluginInfo(plugin, query=True, dependNode=True)) == {
            name for name, _, _ in NODE_TYPES
        }
        cmds.currentUnit(linear="cm")
        for spec in NODE_TYPES:
            check_shape(*spec, args.attributes, args.dummy_bools)
        cmds.file(new=True, force=True)
        cmds.unloadPlugin(plugin)
        plugin, = cmds.loadPlugin(str(path), quiet=True)
        for name, _, _ in NODE_TYPES:
            assert_bounds(cmds.createNode(name), (-0.5, -0.5, -0.5, 0.5, 1.0, 0.5))
        cmds.file(new=True, force=True)
        cmds.unloadPlugin(plugin)
        print(f"Fin Cube contract passed: {path.name}", flush=True)
    finally:
        maya.standalone.uninitialize()


if __name__ == "__main__":
    main()
