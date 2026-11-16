"""選択強調を消したときの色を、実際の非選択表示と比較する。"""

from __future__ import annotations

import pytest

from test_controller_shape_viewport import (
    _aim_at_origin,
    _capture_view,
    _drawing_view,
)

pytestmark = pytest.mark.maya


@pytest.mark.parametrize(
    "preset", ("Cube", "WideCrossArcRadial", "ColorSphere")
)
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("rgb_override", (False, True))
def test_disabled_override_highlighting_off_matches_actual_dormant_color(
    maya_cmds, new_scene, tmp_path, preset, filled, rgb_override
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds,
        preset,
        shapeWide=True,
        shapeFill=filled,
        shapeFillTransparency=0.2,
        shapePart=True,
        shapePartShape=1,
        shapePartType=1,
        shapeFin=True,
    ) as (transform, shape, camera, _, panel):
        _aim_at_origin(maya_cmds, camera, (3, 2, 4))
        maya_cmds.setAttr(f"{shape}.overrideRGBColors", rgb_override)
        maya_cmds.setAttr(f"{shape}.overrideColorRGB", 0.84, 0.68, 0.16)
        maya_cmds.setAttr(f"{shape}.overrideColor", 17)
        maya_cmds.setAttr(f"{shape}.overrideEnabled", False)
        maya_cmds.modelEditor(panel, edit=True, selectionHiliteDisplay=False)
        dormant = _capture_view(panel, tmp_path / "dormant.png")
        background = dormant[:4]
        assert (
            sum(
                dormant[index : index + 4] != background
                for index in range(0, len(dormant), 4)
            )
            > 40
        )
        maya_cmds.select(transform)
        selected = _capture_view(
            panel, tmp_path / "selected_without_highlight.png"
        )
        assert (
            selected == dormant
        ), "無効なOverride色が選択中の非選択表示へ反映された"
        maya_cmds.modelEditor(panel, edit=True, selectionHiliteDisplay=True)
        highlighted = _capture_view(panel, tmp_path / "highlighted.png")
        assert (
            highlighted != dormant
        ), "SelectionHighlightingをONにしても選択色にならない"


@pytest.mark.parametrize(
    "override_source", ("shape", "parent", "ancestor", "layer")
)
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("rgb_override", (False, True))
def test_enabled_override_highlighting_off_matches_actual_dormant_color(
    maya_cmds, new_scene, tmp_path, override_source, filled, rgb_override
):
    """有効な継承override色は選択強調OFFでも選択前後で一致する。"""
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds, "Cube", fixed_viewport=True, shapeFill=filled
    ) as (transform, shape, camera, _, panel):
        _aim_at_origin(maya_cmds, camera, (3, 2, 4))
        maya_cmds.setToolTo("selectSuperContext")
        maya_cmds.setAttr(f"{shape}.overrideEnabled", False)
        if override_source == "ancestor":
            source = maya_cmds.group(transform, name="colorAncestor")
        elif override_source == "layer":
            source = maya_cmds.createDisplayLayer(empty=True)
            maya_cmds.editDisplayLayerMembers(
                source, transform, noRecurse=True
            )
        else:
            source = shape if override_source == "shape" else transform
        if override_source != "layer":
            maya_cmds.setAttr(f"{source}.overrideEnabled", True)
        maya_cmds.setAttr(f"{source}.overrideRGBColors", rgb_override)
        maya_cmds.setAttr(f"{source}.overrideColorRGB", 0.84, 0.23, 0.17)
        color_attribute = (
            "color" if override_source == "layer" else "overrideColor"
        )
        maya_cmds.setAttr(f"{source}.{color_attribute}", 13)
        maya_cmds.modelEditor(panel, edit=True, selectionHiliteDisplay=False)
        maya_cmds.select(clear=True)
        dormant = _capture_view(panel, tmp_path / "override_dormant.png")
        assert any(
            dormant[index : index + 4] != dormant[:4]
            for index in range(0, len(dormant), 4)
        ), "比較対象のCubeが表示されていない"
        maya_cmds.select(transform)
        selected = _capture_view(panel, tmp_path / "override_selected.png")
        assert selected == dormant, "選択強調OFFで継承override色が失われた"
        maya_cmds.modelEditor(panel, edit=True, selectionHiliteDisplay=True)
        highlighted = _capture_view(
            panel, tmp_path / "override_highlighted.png"
        )
        assert highlighted != dormant, "選択強調ONで選択色が表示されない"
        maya_cmds.modelEditor(panel, edit=True, selectionHiliteDisplay=False)
        restored = _capture_view(panel, tmp_path / "override_restored.png")
        assert restored == dormant, "選択強調OFFへの復帰でoverride色が戻らない"
