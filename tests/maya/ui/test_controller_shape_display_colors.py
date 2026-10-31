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
