"""実際のViewport 2.0でコントローラの選択表示を確認する。"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

pytestmark = pytest.mark.maya


def _capture_view(panel, path):
    from maya import cmds
    from maya.api import OpenMaya as om
    from maya.api import OpenMayaUI as omui

    cmds.setFocus(panel)
    cmds.refresh(force=True)
    image = om.MImage()
    omui.M3dView.getM3dViewFromModelPanel(panel).readColorBuffer(image, True)
    image.writeToFile(str(path), "png")
    return bytes(image.pixels())


@pytest.mark.parametrize(
    "preset,fill",
    (
        ("Cube", True),
        ("ColorCornerCube", True),
        ("ColorCrossLine3Axis", False),
        ("ColorSphere", True),
    ),
)
@pytest.mark.parametrize(
    "override_source", ("shape", "parent", "ancestor", "layer")
)
def test_highlighting_off_matches_dormant_display(
    maya_cmds, new_scene, tmp_path, preset, fill, override_source
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    maya_version = int(maya_cmds.about(apiVersion=True)) // 10000
    plugin = Path(
        os.environ.get(
            "BD_UTIL_NODES_PLUGIN_PATH",
            Path(__file__).resolve().parents[3]
            / f"bakedanuki/bakedanuki-util/plug-ins/maya{maya_version}/bdUtilNodes.mll",
        )
    )
    maya_cmds.loadPlugin(str(plugin), quiet=True)
    ancestor = maya_cmds.createNode("transform", name="displayAncestor")
    transform = maya_cmds.createNode("transform", parent=ancestor)
    shape = maya_cmds.createNode("bdControllerShape", parent=transform)
    names = maya_cmds.attributeQuery("shape", node=shape, listEnum=True)[
        0
    ].split(":")
    maya_cmds.setAttr(f"{shape}.shape", names.index(preset))
    maya_cmds.setAttr(f"{shape}.shapeFill", fill)
    if override_source == "layer":
        source = maya_cmds.createDisplayLayer(
            name="controllerDisplayLayer", empty=True
        )
        maya_cmds.editDisplayLayerMembers(source, transform)
    else:
        source = {"shape": shape, "parent": transform, "ancestor": ancestor}[
            override_source
        ]
        maya_cmds.setAttr(f"{source}.overrideEnabled", True)
    window = maya_cmds.window(widthHeight=(480, 480))
    maya_cmds.paneLayout()
    camera, _ = maya_cmds.camera(orthographic=True, orthographicWidth=1.7)
    maya_cmds.setAttr(f"{camera}.translate", 3.0, 2.5, 4.0)
    constraint = maya_cmds.aimConstraint(
        transform, camera, aimVector=(0, 0, -1), upVector=(0, 1, 0)
    )
    maya_cmds.delete(constraint)
    panel = maya_cmds.modelPanel(camera=camera, menuBarVisible=False)
    maya_cmds.modelEditor(
        panel,
        edit=True,
        rendererName="vp2Renderer",
        displayAppearance="smoothShaded",
        grid=False,
        headsUpDisplay=False,
        selectionHiliteDisplay=False,
    )
    maya_cmds.setAttr("hardwareRenderingGlobals.multiSampleEnable", False)
    maya_cmds.displayPref(displayGradient=False)
    maya_cmds.showWindow(window)
    maya_cmds.setToolTo("selectSuperContext")
    from maya import utils

    utils.processIdleEvents()
    try:
        for display_type in (0, 1, 2):
            attribute = (
                "displayType"
                if override_source == "layer"
                else "overrideDisplayType"
            )
            maya_cmds.setAttr(f"{source}.{attribute}", display_type)
            maya_cmds.select(clear=True)
            dormant = _capture_view(
                panel, tmp_path / f"{display_type}_dormant.png"
            )
            background = dormant[:3]
            foreground = sum(
                dormant[index : index + 3] != background
                for index in range(0, len(dormant), 4)
            )
            assert foreground > 40, "Viewportに検証対象の形状が描かれていない"
            maya_cmds.select(transform)
            selected = _capture_view(
                panel, tmp_path / f"{display_type}_selected.png"
            )
            assert selected == dormant, (preset, override_source, display_type)
    finally:
        maya_cmds.deleteUI(window)
