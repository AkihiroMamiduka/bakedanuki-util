"""Viewport 2.0で面倍率後のPart・Fin・Guideの配置を確認する。"""

from __future__ import annotations

import math

import pytest

import bd_util as bdu

from test_controller_shape_viewport import (
    _brightness_near_world,
    _capture_view,
    _drawing_view,
)

pytestmark = pytest.mark.maya


def _look_at(cmds, camera, target_point, direction):
    cmds.setAttr(
        f"{camera}.translate",
        *(target_point[i] + direction[i] * 4 for i in range(3)),
    )
    target = cmds.createNode("transform")
    cmds.setAttr(f"{target}.translate", *target_point)
    constraint = cmds.aimConstraint(
        target, camera, aimVector=(0, 0, -1), upVector=(0, 1, 0)
    )
    cmds.delete(constraint, target)


@pytest.mark.parametrize("part", (6, 8, 10))
@pytest.mark.parametrize("swapped", (False, True))
def test_cage_solid_parts_use_the_sloping_face_frame_without_scaling(
    maya_cmds, new_scene, tmp_path, part, swapped
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds,
        "Cube",
        shapeFill=True,
        shapeLineTransparency=1,
        shapeFillTransparency=0,
        shapeAxisSwap=swapped,
        shapePart=True,
        shapePartShape=part,
        shapePartSize=2,
        shapePartOffset=0.6,
    ) as (_, shape, camera, camera_shape, panel):
        attribute = (
            "1stAxisPlusScale2ndAxis" if swapped else "2ndAxisPlusScale1stAxis"
        )
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace{attribute}", 2)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 3.2)
        along = (
            (-1 / math.sqrt(5), 2 / math.sqrt(5), 0)
            if swapped
            else (2 / math.sqrt(5), -1 / math.sqrt(5), 0)
        )
        root = (0, 0.75, 0) if swapped else (0.75, 0, 0)
        distance = 0.6 + (0.1 if part >= 9 else 0)
        sample = tuple(root[i] + along[i] * distance for i in range(3))
        _look_at(maya_cmds, camera, (0, 0, 0), (0, 0, 1))
        shown = _capture_view(panel, tmp_path / "part.png")
        assert _brightness_near_world(panel, shown, sample) > 550
        maya_cmds.setAttr(f"{shape}.shapePart", False)
        hidden = _capture_view(panel, tmp_path / "body.png")
        assert _brightness_near_world(panel, hidden, sample) < 180


@pytest.mark.parametrize("part", (0, 1))
def test_cage_arrow_part_root_stays_connected_to_the_sloping_face(
    maya_cmds, new_scene, tmp_path, part
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds,
        "Cube",
        shapeFill=True,
        shapeLineTransparency=1,
        shapeFillTransparency=0,
        shapePart=True,
        shapePartShape=part,
        shapePartSize=2,
        shapePartOffset=0.15,
    ) as (_, shape, camera, camera_shape, panel):
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace2ndAxisPlusScale1stAxis", 2)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 1.6)
        root = (0.75, 0, 0)
        along = (2 / math.sqrt(5), -1 / math.sqrt(5), 0)
        up = (1 / math.sqrt(5), 2 / math.sqrt(5), 0)
        sample = (root[0] + along[0] * 0.06, along[1] * 0.06, 0.05)
        _look_at(maya_cmds, camera, root, up)
        connected = _capture_view(panel, tmp_path / "connected.png")
        assert _brightness_near_world(panel, connected, sample) > 550
        maya_cmds.setAttr(f"{shape}.shapePart", False)
        plain = _capture_view(panel, tmp_path / "plain.png")
        assert _brightness_near_world(panel, plain, sample) < 180


def test_cage_wire_part_remains_normal_when_the_body_line_is_templated(
    maya_cmds, new_scene, tmp_path
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds,
        "Cube",
        shapeFill=False,
        shapeTemplateLine=True,
        shapeLineWidth=2,
        shapePart=True,
        shapePartShape=0,
        shapePartSize=3,
        shapePartOffset=0.15,
    ) as (_, shape, camera, camera_shape, panel):
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace2ndAxisPlusScale1stAxis", 2)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 1.6)
        root = (0.75, 0, 0)
        along = (2 / math.sqrt(5), -1 / math.sqrt(5), 0)
        up = (1 / math.sqrt(5), 2 / math.sqrt(5), 0)
        _look_at(maya_cmds, camera, root, up)
        sample = (root[0] + along[0] * 0.075, along[1] * 0.075, 0.072 * 3)
        shown = _capture_view(panel, tmp_path / "normal_part.png")
        assert _brightness_near_world(panel, shown, sample) > 550
        maya_cmds.setAttr(f"{shape}.shapePart", False)
        hidden = _capture_view(panel, tmp_path / "no_part.png")
        assert _brightness_near_world(panel, hidden, sample) < 180


def test_cage_standard_fin_keeps_its_top_parallel_to_the_main_axis(
    maya_cmds, new_scene, tmp_path
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds,
        "Cube",
        shapeFill=True,
        shapeLineTransparency=1,
        shapeFillTransparency=0,
        shapeFin=True,
        shapeFinHeight=0.4,
    ) as (_, shape, camera, camera_shape, panel):
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace1stAxisPlusScale2ndAxis", 2)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 3.2)
        _look_at(maya_cmds, camera, (0, 0.4, 0), (0, 0, 1))
        shown = _capture_view(panel, tmp_path / "fin.png")
        inside = (0.25, 1.25, 0)
        outside = (0.25, 1.5, 0)
        assert _brightness_near_world(panel, shown, inside) > 550
        assert _brightness_near_world(panel, shown, outside) < 180
        maya_cmds.setAttr(f"{shape}.shapeFin", False)
        hidden = _capture_view(panel, tmp_path / "no_fin.png")
        assert _brightness_near_world(panel, hidden, inside) < 180


def test_cage_guide_reaches_the_new_face_center(
    maya_cmds, new_scene, tmp_path
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(maya_cmds, "Cube", shapeFill=False) as (
        _,
        shape,
        camera,
        camera_shape,
        panel,
    ):
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace2ndAxisPlusScale1stAxis", 2)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 2.4)
        _look_at(maya_cmds, camera, (0, 0, 0), (0, 0, 1))
        sample = (0.65, 0, 0)
        before = _capture_view(panel, tmp_path / "no_guide.png")
        assert _brightness_near_world(panel, before, sample) < 180
        maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
        after = _capture_view(panel, tmp_path / "guide.png")
        assert _brightness_near_world(panel, after, sample) > 550


def test_cage_wrapped_cross_arc_wire_hides_the_flat_join_internal_lines(
    maya_cmds, new_scene, tmp_path
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds,
        "WideCrossArcAxial",
        shape1stAxis=0,
        shape2ndAxis=2,
        shapeFill=False,
        shapeArcAngle=360,
        shapeWideWidth=0.2,
        shapePartShape=3,
        shapePartType=1,
    ) as (_, shape, camera, camera_shape, panel):
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace2ndAxisPlusScale1stAxis", 2)
        _look_at(maya_cmds, camera, (0.7, 0, 0), (1, 0, 0))
        maya_cmds.setAttr(f"{camera}.translate", 0.9, 0, 0)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 0.5)
        maya_cmds.setAttr(f"{camera_shape}.farClipPlane", 0.3)
        sample = (0.7, 0.1, 0)
        plain = _capture_view(panel, tmp_path / "plain_cross_join.png")
        assert _brightness_near_world(panel, plain, sample) < 180
        maya_cmds.setAttr(f"{shape}.shapePart", True)
        wrapped = _capture_view(panel, tmp_path / "wrapped_cross_join.png")
        assert _brightness_near_world(panel, wrapped, sample) < 180


def test_cage_double2_parent_direct_change_updates_both_drawn_components(
    maya_cmds, new_scene, tmp_path
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds,
        "Cube",
        shapeFill=False,
        shapeLineWidth=2,
        shape1stAxis=0,
        shape2ndAxis=2,
    ) as (_, shape, camera, camera_shape, panel):
        _look_at(maya_cmds, camera, (0, 0, 0), (1, 0, 0))
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 3.8)
        samples = ((0.5, 1, 0), (0.5, 0, 1.5))
        baseline = _capture_view(
            panel, tmp_path / "double2_parent_default.png"
        )
        for sample in samples:
            assert _brightness_near_world(panel, baseline, sample) < 180
        parent = f"{shape}.shapeBaseSpace1stAxisPlusScale"
        maya_cmds.setAttr(parent, 2, 3, type="double2")
        expanded = _capture_view(
            panel, tmp_path / "double2_parent_changed.png"
        )
        for sample in samples:
            assert _brightness_near_world(panel, expanded, sample) > 550
        maya_cmds.setAttr(parent, 1, 1, type="double2")
        restored = _capture_view(
            panel, tmp_path / "double2_parent_restored.png"
        )
        for sample in samples:
            assert _brightness_near_world(panel, restored, sample) < 180


def test_cage_double2_parent_direct_edit_updates_draw_and_undo(
    maya_cmds, new_scene, tmp_path
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds,
        "Cube",
        shapeFill=False,
        shapeLineWidth=2,
        shape1stAxis=0,
        shape2ndAxis=2,
    ) as (_, shape, camera, camera_shape, panel):
        _look_at(maya_cmds, camera, (0, 0, 0), (1, 0, 0))
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 3.8)
        driver = maya_cmds.createNode("network")
        maya_cmds.addAttr(
            driver, longName="faceScale", attributeType="double2"
        )
        for child in ("inPlaneA", "inPlaneB"):
            maya_cmds.addAttr(
                driver,
                longName=child,
                attributeType="double",
                parent="faceScale",
                defaultValue=1,
                keyable=True,
            )
        with pytest.raises(RuntimeError):
            maya_cmds.connectAttr(
                f"{driver}.faceScale",
                f"{shape}.shapeBaseSpace1stAxisPlusScale",
            )
        samples = ((0.5, 1, 0), (0.5, 0, 1.5))
        baseline = _capture_view(panel, tmp_path / "double2_before_edit.png")
        for sample in samples:
            assert _brightness_near_world(panel, baseline, sample) < 180
        mod = bdu.ModifierManager()
        node = bdu.Nodes(modifier_manager=mod).existing(shape)
        node.shapeBaseSpace1stAxisPlusScale.set(2, 3)
        mod.do_it_dg()
        changed = _capture_view(panel, tmp_path / "double2_after_edit.png")
        for sample in samples:
            assert _brightness_near_world(panel, changed, sample) > 550
        mod.undo_it()
        restored = _capture_view(panel, tmp_path / "double2_after_undo.png")
        for sample in samples:
            assert _brightness_near_world(panel, restored, sample) < 180
