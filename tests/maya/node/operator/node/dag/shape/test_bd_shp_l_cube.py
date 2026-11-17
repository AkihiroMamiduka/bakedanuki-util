"""固定 Cube の登録・保存・親変換を本体と研究用 DLL で共通検証する。"""

from __future__ import annotations

import os
from pathlib import Path

import pytest
from maya import cmds
from maya.api import OpenMaya as om

pytestmark = pytest.mark.maya


@pytest.fixture(scope="module")
def cube_plugin():
    """通常は本体を読み込み、研究ランナー指定時は既存の DLL を検証する。"""
    research_path = os.environ.get("BD_FIXED_CUBE_PLUGIN_PATH")
    if research_path:
        plugin_path = Path(research_path).resolve(strict=True)
        plugin_name = os.environ.get(
            "BD_FIXED_CUBE_PLUGIN_NAME", plugin_path.stem
        )
        assert cmds.pluginInfo(plugin_name, query=True, loaded=True)
    else:
        version = int(cmds.about(apiVersion=True)) // 10000
        default_path = (
            Path(__file__).resolve().parents[7]
            / "bakedanuki/bakedanuki-util/plug-ins"
            / f"maya{version}"
            / "bdUtilNodes.mll"
        )
        plugin_path = Path(
            os.environ.get("BD_UTIL_NODES_PLUGIN_PATH", default_path)
        ).resolve(strict=True)
        cmds.loadPlugin(str(plugin_path), quiet=True)
        plugin_name = plugin_path.stem
    assert (
        Path(cmds.pluginInfo(plugin_name, query=True, path=True)).resolve()
        == plugin_path
    )
    assert (
        int(cmds.pluginInfo(plugin_name, query=True, apiVersion=True)) // 10000
        == int(cmds.about(apiVersion=True)) // 10000
    )
    assert "bdShpL_Cube" in (
        cmds.pluginInfo(plugin_name, query=True, dependNode=True) or []
    )
    prefix = (
        "subscene"
        if plugin_path.stem.startswith("bdShpCubeSubScene")
        else "geometry"
    )
    return plugin_name, prefix


@pytest.fixture(autouse=True)
def scene(cube_plugin):
    """空のシーンと一定の単位で実行し、変更した設定を元へ戻す。"""
    linear = cmds.currentUnit(query=True, linear=True)
    angle = cmds.currentUnit(query=True, angle=True)
    undo = cmds.undoInfo(query=True, state=True)
    cmds.file(new=True, force=True)
    cmds.currentUnit(linear="cm", angle="deg")
    cmds.undoInfo(state=True)
    try:
        yield
    finally:
        cmds.file(new=True, force=True)
        cmds.currentUnit(linear=linear, angle=angle)
        cmds.undoInfo(state=undo)


def _create_cube(parent_type="transform"):
    """指定した親の直下へ固定 Cube を作成する。"""
    parent = cmds.createNode(parent_type, name="control")
    shape = cmds.createNode("bdShpL_Cube", parent=parent, name="controlShape")
    return parent, shape


def _dag_path(name):
    """名前に対応する DAG path を返す。"""
    selection = om.MSelectionList()
    selection.add(name)
    return selection.getDagPath(0)


def test_identity_and_attributes():
    """固有 ID と独自属性なしの仕様を検証する。"""
    _, shape = _create_cube()
    fn = om.MFnDependencyNode(_dag_path(shape).node())
    assert fn.typeId.id() == 0x00142720
    assert cmds.nodeType(shape) == "bdShpL_Cube"
    assert not (cmds.listAttr(shape, userDefined=True) or [])
    standard_locator = cmds.createNode("locator")
    assert not set(cmds.listAttr(shape)).difference(
        cmds.listAttr(standard_locator)
    )
    for name in (
        "shape",
        "shapeFill",
        "shapeSize",
        "shapeAnimationTransformMatrix",
    ):
        assert not cmds.attributeQuery(name, node=shape, exists=True)


def test_draw_classification_matches_override(cube_plugin):
    """描画方式に対応する分類でノードを登録する。"""
    _, prefix = cube_plugin
    assert cmds.getClassification("bdShpL_Cube") == [
        f"drawdb/{prefix}/bdShpL_Cube"
    ]


@pytest.mark.parametrize("parent_type", ["transform", "joint"])
def test_parent_matrix_and_fixed_bounds(parent_type):
    """pivot・shear・jointOrient を含む親階層と固定範囲を検証する。"""
    group = cmds.createNode("transform", name="group")
    parent, shape = _create_cube(parent_type)
    cmds.parent(parent, group, relative=True)
    cmds.setAttr(group + ".translate", 2, -3, 4)
    cmds.setAttr(group + ".rotate", 11, 22, 33)
    cmds.setAttr(group + ".scale", 1.3, 0.7, 2)
    cmds.setAttr(parent + ".translate", 1, 2, 3)
    cmds.setAttr(parent + ".rotate", 31, -17, 54)
    cmds.setAttr(parent + ".rotateAxis", 7, 19, -13)
    cmds.setAttr(parent + ".scale", -1.2, 0.8, 1.7)
    cmds.setAttr(parent + ".rotateOrder", 4)
    cmds.setAttr(
        parent + ".offsetParentMatrix",
        *list(
            om.MMatrix([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0.3, -0.2, 0.4, 1])
        ),
        type="matrix",
    )
    if parent_type == "joint":
        cmds.setAttr(parent + ".jointOrient", 23, 34, -12)
    else:
        cmds.setAttr(parent + ".shear", 0.25, -0.17, 0.3)
        cmds.setAttr(parent + ".rotatePivot", 0.7, -0.4, 0.2)
        cmds.setAttr(parent + ".scalePivot", -0.3, 0.2, 0.5)
    path = _dag_path(shape)
    bounds = om.MFnDagNode(path).boundingBox
    assert tuple(bounds.min)[:3] == pytest.approx((-0.5,) * 3)
    assert tuple(bounds.max)[:3] == pytest.approx((0.5,) * 3)
    matrix = path.inclusiveMatrix()
    expected = om.MBoundingBox()
    for x in (-0.5, 0.5):
        for y in (-0.5, 0.5):
            for z in (-0.5, 0.5):
                expected.expand(om.MPoint(x, y, z) * matrix)
    assert cmds.exactWorldBoundingBox(shape) == pytest.approx(
        (*tuple(expected.min)[:3], *tuple(expected.max)[:3])
    )


def test_duplicate_delete_undo():
    """複製と削除後の Undo / Redo を検証する。"""
    parent, shape = _create_cube()
    duplicate = cmds.duplicate(parent)[0]
    assert (
        cmds.nodeType(cmds.listRelatives(duplicate, shapes=True)[0])
        == "bdShpL_Cube"
    )
    cmds.delete(parent)
    assert not cmds.objExists(shape)
    cmds.undo()
    assert cmds.objExists(shape)
    cmds.redo()
    assert not cmds.objExists(shape)


def test_save_reload(tmp_path):
    """シーン再読込後も型と親変換を保持する。"""
    parent, shape = _create_cube()
    cmds.setAttr(parent + ".shearXY", 0.4)
    scene_path = tmp_path / "fixed_cube.ma"
    cmds.file(rename=str(scene_path))
    cmds.file(save=True, type="mayaAscii")
    cmds.file(new=True, force=True)
    cmds.file(str(scene_path), open=True, force=True)
    assert cmds.nodeType(shape) == "bdShpL_Cube"
    assert cmds.getAttr(parent + ".shearXY") == pytest.approx(0.4)
