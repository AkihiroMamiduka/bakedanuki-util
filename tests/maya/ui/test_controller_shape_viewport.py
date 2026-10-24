"""実際のViewport 2.0でコントローラの選択表示を確認する。"""

from __future__ import annotations

import os
from contextlib import contextmanager
from ctypes import string_at
from pathlib import Path

import pytest

pytestmark = pytest.mark.maya


def _capture_view(panel, path):
    from maya import cmds, utils
    from maya.api import OpenMaya as om
    from maya.api import OpenMayaUI as omui

    cmds.setFocus(panel)
    utils.processIdleEvents()
    view = omui.M3dView.getM3dViewFromModelPanel(panel)
    cmds.playblast(
        editorPanelName=panel,
        completeFilename=str(path),
        format="image",
        compression="png",
        forceOverwrite=True,
        viewer=False,
        offScreen=True,
        showOrnaments=False,
        percent=100,
        widthHeight=(view.portWidth(), view.portHeight()),
        frame=cmds.currentTime(query=True),
    )
    image = om.MImage()
    image.readFromFile(str(path))
    width, height = image.getSize()
    return string_at(image.pixels(), width * height * 4)


@contextmanager
def _drawing_view(cmds, preset, **options):
    from maya import utils

    version = int(cmds.about(apiVersion=True)) // 10000
    plugin = Path(
        os.environ.get(
            "BD_UTIL_NODES_PLUGIN_PATH",
            Path(__file__).resolve().parents[3]
            / f"bakedanuki/bakedanuki-util/plug-ins/maya{version}/bdUtilNodes.mll",
        )
    )
    cmds.loadPlugin(str(plugin), quiet=True)
    transform = cmds.createNode("transform")
    shape = cmds.createNode("bdControllerShape", parent=transform)
    names = cmds.attributeQuery("shape", node=shape, listEnum=True)[0].split(
        ":"
    )
    cmds.setAttr(f"{shape}.shape", names.index(preset))
    for name, value in options.items():
        cmds.setAttr(f"{shape}.{name}", value)
    cmds.setAttr(f"{shape}.overrideEnabled", True)
    cmds.setAttr(f"{shape}.overrideRGBColors", True)
    cmds.setAttr(f"{shape}.overrideColorRGB", 1, 1, 1)
    window = cmds.window(widthHeight=(480, 480))
    cmds.paneLayout()
    camera, camera_shape = cmds.camera(
        orthographic=True, orthographicWidth=1.6
    )
    cmds.setAttr(f"{camera}.translateZ", 4)
    cmds.setAttr(f"{camera_shape}.nearClipPlane", 0.001)
    panel = cmds.modelPanel(camera=camera, menuBarVisible=False)
    cmds.modelEditor(
        panel,
        edit=True,
        rendererName="vp2Renderer",
        allObjects=True,
        pluginShapes=True,
        locators=True,
        displayAppearance="smoothShaded",
        grid=False,
        headsUpDisplay=False,
        selectionHiliteDisplay=False,
    )
    cmds.setAttr("hardwareRenderingGlobals.multiSampleEnable", False)
    previous_background = cmds.displayRGBColor("background", query=True)
    cmds.displayRGBColor("background", 0.07, 0.03, 0.09)
    cmds.displayPref(displayGradient=False)
    cmds.showWindow(window)
    cmds.select(clear=True)
    utils.processIdleEvents()
    try:
        yield transform, shape, camera, camera_shape, panel
    finally:
        cmds.deleteUI(window)
        cmds.displayRGBColor("background", *previous_background)


@pytest.mark.parametrize(
    "preset",
    (
        "Cube",
        "Octahedron",
        "OctahedronArrow",
        "Sphere",
        "Cylinder",
        "Pyramid",
        "Cone",
        "ColorCube",
        "ColorCornerCube",
        "ColorSphere",
    ),
)
@pytest.mark.parametrize("mirrored", (False, True))
def test_closed_fill_faces_outward(
    maya_cmds, new_scene, tmp_path, preset, mirrored
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(
        maya_cmds,
        preset,
        shapeFill=True,
        shapeLineTransparency=1,
        shapeFillTransparency=0.5,
    ) as (transform, shape, camera, camera_shape, panel):
        if mirrored:
            maya_cmds.setAttr(f"{shape}.shapeScaleX", -1)
            maya_cmds.setAttr(f"{transform}.scaleY", -1)
        maya_cmds.setAttr(f"{camera_shape}.orthographic", False)
        outside = _capture_view(panel, tmp_path / "outside.png")
        maya_cmds.setAttr(f"{camera}.translateZ", 0)
        inside = _capture_view(panel, tmp_path / "inside.png")
        background = inside[:4]
        assert all(
            inside[i : i + 4] == background for i in range(0, len(inside), 4)
        ), "立体の内側から裏面が描画されている"
        assert any(
            outside[i : i + 4] != background for i in range(0, len(outside), 4)
        ), "外向きの面が描画されていない"


@pytest.mark.parametrize("part_shape", (6, 7, 8, 9, 10))
def test_solid_part_fill_faces_outward(
    maya_cmds, new_scene, tmp_path, part_shape
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(
        maya_cmds,
        "Line",
        shapeFill=True,
        shapeLineTransparency=1,
        shapePart=True,
        shapePartShape=part_shape,
        shapePartSize=5,
    ) as (_, _, camera, camera_shape, panel):
        maya_cmds.setAttr(f"{camera_shape}.orthographic", False)
        outside = _capture_view(panel, tmp_path / "outside.png")
        # Pyramid・Coneは先端から内側へ高さの半分を戻す。
        center = 0.25 if part_shape >= 9 else 0.5
        maya_cmds.setAttr(f"{camera}.translate", center, 0, 0)
        inside = _capture_view(panel, tmp_path / "inside.png")
        background = inside[:4]
        assert all(
            inside[i : i + 4] == background for i in range(0, len(inside), 4)
        ), "小形状の内側から裏面が描画されている"
        assert any(
            outside[i : i + 4] != background for i in range(0, len(outside), 4)
        )


@pytest.mark.parametrize(
    "preset,options",
    (
        ("Triangle", {}),
        ("Line", {"shapePart": True, "shapePartShape": 1}),
        ("Line", {"shapeFin": True}),
    ),
)
def test_thin_fill_remains_visible_from_both_sides(
    maya_cmds, new_scene, tmp_path, preset, options
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(
        maya_cmds, preset, shapeFill=True, shapeLineTransparency=1, **options
    ) as (_, _, camera, _, panel):
        axis = "X" if preset == "Triangle" else "Z"
        for sign in (-1, 1):
            maya_cmds.setAttr(f"{camera}.translate", 0, 0, 0)
            maya_cmds.setAttr(f"{camera}.translate{axis}", sign * 4)
            target = maya_cmds.createNode("transform")
            constraint = maya_cmds.aimConstraint(
                target, camera, aimVector=(0, 0, -1), upVector=(0, 1, 0)
            )
            maya_cmds.delete(constraint, target)
            pixels = _capture_view(panel, tmp_path / f"side_{sign}.png")
            background = pixels[:4]
            assert any(
                pixels[i : i + 4] != background
                for i in range(0, len(pixels), 4)
            ), "薄い面が裏側から見えなくなっている"


@pytest.mark.parametrize(
    "preset,part_shape",
    (
        ("Cone", None),
        ("Cylinder", None),
        ("Line", 0),
        ("CrossLine1st2nd", 1),
        ("CrossLine1st3rd", 0),
        ("CrossLine2nd3rd", 1),
        ("CrossLine3Axis", 0),
        ("ColorCrossLine3Axis", 1),
        ("Circle", 1),
        ("SquareCrossLine", 0),
        ("SquareCrossLineTemplate", 1),
        ("Line", 10),
    ),
)
@pytest.mark.parametrize("draw_on_top", (False, True))
def test_hidden_fill_restores_wireframe(
    maya_cmds, new_scene, tmp_path, preset, part_shape, draw_on_top
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    options = dict(shapeDrawOnTop=draw_on_top)
    if part_shape is not None:
        options.update(
            shapePart=True,
            shapePartShape=part_shape,
            shapePartType=1,
            shapePartOffset=0.2,
        )
    with _drawing_view(maya_cmds, preset, **options) as (
        _,
        shape,
        camera,
        _,
        panel,
    ):
        maya_cmds.setAttr(f"{camera}.translate", 3, 2.5, 4)
        target = maya_cmds.createNode("transform")
        constraint = maya_cmds.aimConstraint(
            target, camera, aimVector=(0, 0, -1), upVector=(0, 1, 0)
        )
        maya_cmds.delete(constraint, target)
        for display_type in (0, 1, 2, 3):
            maya_cmds.setAttr(f"{shape}.overrideDisplayType", display_type % 3)
            maya_cmds.setAttr(
                f"{shape}.shapeFillTransparency",
                1 if display_type == 3 else 0.85,
            )
            appearance = "wireframe" if display_type == 0 else "smoothShaded"
            maya_cmds.modelEditor(
                panel, edit=True, displayAppearance=appearance
            )
            maya_cmds.setAttr(f"{shape}.shapeFill", False)
            expected = _capture_view(
                panel, tmp_path / f"{display_type}_off.png"
            )
            assert any(
                expected[i : i + 4] != expected[:4]
                for i in range(0, len(expected), 4)
            ), ("Viewportに検証対象の線が描かれていない", display_type)
            maya_cmds.setAttr(f"{shape}.shapeFill", True)
            actual = _capture_view(panel, tmp_path / f"{display_type}_on.png")
            assert (
                actual == expected
            ), "面を表示しない状態で線の形が変わっている"


def _brightness_near_world(panel, pixels, point):
    from maya.api import OpenMaya as om
    from maya.api import OpenMayaUI as omui

    view = omui.M3dView.getM3dViewFromModelPanel(panel)
    x, y, visible = view.worldToView(om.MPoint(*point))
    assert visible
    width = view.portWidth()
    return max(
        sum(
            pixels[(row * width + column) * 4 : (row * width + column) * 4 + 3]
        )
        for row in range(y - 1, y + 2)
        for column in range(x - 1, x + 2)
    )


@pytest.mark.parametrize(
    "preset", ("Line", "Circle", "SquareCrossLine", "SquareCrossLineTemplate")
)
@pytest.mark.parametrize("part_shape", (0, 1))
@pytest.mark.parametrize("draw_on_top", (False, True))
def test_arrow_tip_connection_matches_fill_and_guide_style(
    maya_cmds, new_scene, tmp_path, preset, part_shape, draw_on_top
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(
        maya_cmds,
        preset,
        shapePart=True,
        shapePartShape=part_shape,
        shapePartOffset=0.05,
        shapeCircleAngle=240,
        shapeDrawOnTop=draw_on_top,
    ) as (_, shape, camera, _, panel):
        maya_cmds.setAttr(f"{camera}.translate", 3, 2.5, 4)
        target = maya_cmds.createNode("transform")
        constraint = maya_cmds.aimConstraint(
            target, camera, aimVector=(0, 0, -1), upVector=(0, 1, 0)
        )
        maya_cmds.delete(constraint, target)
        if preset.startswith("SquareCrossLine"):
            point = (0, 0.645, 0)
        elif preset == "Circle":
            import math

            point = (
                0,
                -0.25 - 0.02 * math.cos(math.pi / 6),
                0.5 * math.cos(math.pi / 6) - 0.01,
            )
        else:
            point = (0.52, 0, 0)
        open_arrow = _capture_view(panel, tmp_path / "open.png")
        maya_cmds.setAttr(f"{shape}.shapeFill", True)
        filled_arrow = _capture_view(panel, tmp_path / "filled.png")
        open_brightness = _brightness_near_world(panel, open_arrow, point)
        filled_brightness = _brightness_near_world(panel, filled_arrow, point)
        if preset.startswith("SquareCrossLine"):
            assert open_brightness > 200
            assert filled_brightness >= open_brightness - 30, (
                "Fill表示時に中央ガイドが先端へ届かないか、線の表示種別が変わっている",
                open_brightness,
                filled_brightness,
            )
        else:
            assert open_brightness > filled_brightness + 120, (
                "開いた矢印が先端へ届かないか、Fillの内側に線が残っている",
                open_brightness,
                filled_brightness,
            )


@pytest.mark.parametrize(
    "preset,point,options",
    (
        ("Cone", (0, 0, 0.25), {}),
        ("Cylinder", (0, 0, 0.5), {}),
        ("Line", (0.45, 0, 0.025), {"shapePart": True, "shapePartShape": 10}),
    ),
)
@pytest.mark.parametrize("draw_on_top", (False, True))
def test_cone_keeps_side_lines_and_cylinder_hides_them_with_fill(
    maya_cmds, new_scene, tmp_path, preset, point, options, draw_on_top
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(
        maya_cmds,
        preset,
        shapeFill=True,
        shapeDrawOnTop=draw_on_top,
        **options,
    ) as (_, _, _, _, panel):
        shaded = _capture_view(panel, tmp_path / "shaded.png")
        maya_cmds.modelEditor(panel, edit=True, displayAppearance="wireframe")
        wireframe = _capture_view(panel, tmp_path / "wireframe.png")
        wire_brightness = _brightness_near_world(panel, wireframe, point)
        shaded_brightness = _brightness_near_world(panel, shaded, point)
        if preset == "Cylinder":
            assert wire_brightness > shaded_brightness + 120
        else:
            assert wire_brightness > 600
            assert shaded_brightness >= wire_brightness - 30, (
                "ConeのFill表示時に側線が消えている",
                shaded_brightness,
            )


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("all_ends", (False, True))
def test_arrow3d_raises_only_on_positive_side_and_draws_shoulder_edge(
    maya_cmds, new_scene, tmp_path, filled, all_ends
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    import math

    with _drawing_view(
        maya_cmds,
        "Line",
        shapeFill=filled,
        shapePart=True,
        shapePartShape=1,
        shapePartType=int(all_ends),
    ) as (_, _, camera, _, panel):
        maya_cmds.setAttr(f"{camera}.translate", 0, -4, 0)
        target = maya_cmds.createNode("transform")
        constraint = maya_cmds.aimConstraint(
            target, camera, aimVector=(0, 0, -1), upVector=(0, 0, 1)
        )
        maya_cmds.delete(constraint, target)
        pixels = _capture_view(panel, tmp_path / "side.png")
        depth = 0.1 * math.cos(math.pi / 6)
        for sign in (-1, 1) if all_ends else (1,):
            shoulder = ((0.5 - depth) * sign, 0, 0.025)
            negative = ((0.5 - depth * 0.5) * sign, 0, -0.025)
            assert _brightness_near_world(panel, pixels, shoulder) > 600
            assert _brightness_near_world(panel, pixels, negative) < 120, (
                "Arrow3Dが主平面の負側にも作られている",
                sign,
            )


@pytest.mark.parametrize(
    "preset,fill,part_settings",
    (
        ("Cube", True, {}),
        ("ColorCornerCube", True, {}),
        ("ColorCrossLine3Axis", False, {}),
        ("ColorSphere", True, {}),
        pytest.param(
            "Line",
            True,
            {
                "shapePart": True,
                "shapePartShape": 6,
                "shapePartType": 1,
                "shapeFin": True,
            },
            id="LineCubeAtEnds",
        ),
        pytest.param(
            "SquareTemplate",
            True,
            {"shapePart": True, "shapePartShape": 1, "shapePartType": 1},
            id="SquareTemplateArrow3DAtEnds",
        ),
        pytest.param(
            "WideCircleRadial",
            True,
            {
                "shapeCircleAngle": 240,
                "shapePart": True,
                "shapePartShape": 0,
                "shapePartType": 1,
                "shapePartOffset": 0.2,
            },
            id="WideCircleRadialArrow2DAtEnds",
        ),
        pytest.param(
            "ColorCrossLine3Axis",
            True,
            {
                "shapePart": True,
                "shapePartShape": 9,
                "shapePartType": 1,
                "shapeFin": True,
            },
            id="ColorCrossLine3AxisPyramidAtEnds",
        ),
    ),
)
@pytest.mark.parametrize(
    "override_source", ("shape", "parent", "ancestor", "layer")
)
def test_highlighting_off_matches_dormant_display(
    maya_cmds,
    new_scene,
    tmp_path,
    preset,
    fill,
    part_settings,
    override_source,
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
    for attribute, value in part_settings.items():
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
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
        allObjects=True,
        pluginShapes=True,
        locators=True,
        displayAppearance="smoothShaded",
        grid=False,
        headsUpDisplay=False,
        selectionHiliteDisplay=False,
    )
    maya_cmds.setAttr("hardwareRenderingGlobals.multiSampleEnable", False)
    previous_background = maya_cmds.displayRGBColor("background", query=True)
    maya_cmds.displayRGBColor("background", 0.07, 0.03, 0.09)
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
            background = dormant[:4]
            foreground = sum(
                dormant[index : index + 4] != background
                for index in range(0, len(dormant), 4)
            )
            assert foreground > 40, "Viewportに検証対象の形状が描かれていない"
            maya_cmds.select(transform)
            selected = _capture_view(
                panel, tmp_path / f"{display_type}_selected.png"
            )
            assert selected == dormant, (
                preset,
                part_settings,
                override_source,
                display_type,
            )
    finally:
        maya_cmds.deleteUI(window)
        maya_cmds.displayRGBColor("background", *previous_background)


def test_axial_circle_thin_fill_is_visible_from_outside_and_inside(
    maya_cmds, new_scene, tmp_path
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(
        maya_cmds,
        "WideCircleAxial",
        shapeWideWidth=0.4,
        shapeFill=True,
        shapeLineTransparency=1,
        shapeFillTransparency=0.5,
    ) as (_, _, camera, camera_shape, panel):
        maya_cmds.setAttr(f"{camera_shape}.orthographic", False)
        for name, position, point in (
            ("outside", 4, (0, 0, 0.5)),
            ("inside", 0, (0, 0, -0.5)),
        ):
            maya_cmds.setAttr(f"{camera}.translateZ", position)
            pixels = _capture_view(panel, tmp_path / f"{name}.png")
            assert _brightness_near_world(panel, pixels, point) > 120, (
                "円筒側面の薄い塗り面が見えない",
                name,
            )


def test_axial_circle_draws_two_rims_without_a_full_circle_seam(
    maya_cmds, new_scene, tmp_path
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(maya_cmds, "WideCircleAxial", shapeWideWidth=0.3) as (
        _,
        _,
        _,
        _,
        panel,
    ):
        pixels = _capture_view(panel, tmp_path / "rims.png")
        for side in (-0.15, 0.15):
            assert (
                _brightness_near_world(panel, pixels, (side, 0, 0.5)) > 600
            ), "軸方向の帯の両側に輪郭がない"
        for point in ((0, 0, 0.5), (0, -0.5, 0), (0, 0.5, 0)):
            assert _brightness_near_world(panel, pixels, point) < 120, (
                "360度の帯に継ぎ目線または不要な母線が残っている",
                point,
            )


def test_axial_circle_arrow3d_raises_radially_outward_at_both_ends(
    maya_cmds, new_scene, tmp_path
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    import math

    with _drawing_view(
        maya_cmds,
        "WideCircleAxial",
        shapeCircleAngle=180,
        shapeFill=True,
        shapePart=True,
        shapePartShape=1,
        shapePartType=1,
    ) as (_, _, camera, _, panel):
        maya_cmds.setAttr(f"{camera}.translate", 4, 0, 0)
        target = maya_cmds.createNode("transform")
        constraint = maya_cmds.aimConstraint(
            target, camera, aimVector=(0, 0, -1), upVector=(0, 1, 0)
        )
        maya_cmds.delete(constraint, target)
        pixels = _capture_view(panel, tmp_path / "radial_arrows.png")
        depth = 0.1 * math.cos(math.pi / 6)
        cosine = math.sqrt(1 - depth * depth)
        for sign in (-1, 1):
            assert (
                _brightness_near_world(
                    panel,
                    pixels,
                    (
                        0,
                        depth * cosine + 0.025 * depth,
                        sign * (0.5 - depth * depth + 0.025 * cosine),
                    ),
                )
                > 600
            ), "Arrow3Dの肩が各円弧端の半径外側へ立ち上がっていない"
            assert (
                _brightness_near_world(
                    panel, pixels, (0, depth * 0.5, sign * 0.475)
                )
                < 120
            ), "Arrow3Dが円の内側へ立ち上がっている"


def test_axial_circle_moved_part_keeps_the_band_connected_without_a_join_line(
    maya_cmds, new_scene, tmp_path
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(
        maya_cmds,
        "WideCircleAxial",
        shapeCircleAngle=180,
        shapeWideWidth=0.1,
        shapePart=True,
        shapePartShape=3,
        shapePartSize=2,
        shapePartOffset=0.3,
    ) as (_, _, _, _, panel):
        pixels = _capture_view(panel, tmp_path / "moved_part.png")
        for side in (-0.05, 0.05):
            assert (
                _brightness_near_world(panel, pixels, (side, -0.1, 0.5)) > 600
            ), "移動したPartまで帯の両側が延長されていない"
        assert (
            _brightness_near_world(panel, pixels, (0, -0.2, 0.5)) < 120
        ), "Partと帯の接合位置に内部の横線が残っている"


def _frame_axial_join(
    cmds, camera, camera_shape, *, side=False, oblique=False
):
    center = (0, 0.06, 0.495)
    position = (4, 0.06, 0.495) if side else (1 if oblique else 0, 0.06, 4)
    cmds.setAttr(f"{camera}.translate", *position)
    cmds.setAttr(f"{camera_shape}.orthographicWidth", 0.3)
    target = cmds.createNode("transform")
    cmds.setAttr(f"{target}.translate", *center)
    constraint = cmds.aimConstraint(
        target, camera, aimVector=(0, 0, -1), upVector=(0, 1, 0)
    )
    cmds.delete(constraint, target)


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("part", (0, 1, 2))
def test_axial_circle_pointed_part_joins_without_a_step(
    maya_cmds, new_scene, tmp_path, filled, part
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    import math

    depth = 0.1 * (math.cos(math.pi / 6) if part <= 1 else 1)
    delta = 2 * math.asin(depth)
    base_y, base_z = 0.5 * math.sin(delta), 0.5 * math.cos(delta)
    with _drawing_view(
        maya_cmds,
        "WideCircleAxial",
        shapeCircleAngle=180,
        shapePart=True,
        shapePartShape=part,
        shapePartType=1,
        shapeFill=filled,
    ) as (_, shape, camera, camera_shape, panel):
        _frame_axial_join(maya_cmds, camera, camera_shape, side=True)
        if part == 1:
            maya_cmds.setAttr(f"{shape}.shapeFill", False)
        side = _capture_view(panel, tmp_path / "pointed_side.png")
        old_sag = 0.5 - math.sqrt(0.25 - depth * depth)
        for point in (
            (0, base_y, base_z),
            (0, base_y / 2, (base_z + 0.5) / 2),
        ):
            assert _brightness_near_world(panel, side, point) > 600
        old_join = (0, depth, 0.5 - 0.2 * old_sag)
        if part == 1:
            # 追加面の肩線と旧段面の距離を、画像上でも十分に離す。
            maya_cmds.setAttr(
                f"{camera}.translate", 4, old_join[1], old_join[2]
            )
            maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 0.01)
            side = _capture_view(panel, tmp_path / "pointed_side_detail.png")
            cosine = math.sqrt(1 - depth * depth)
            height = (old_join[1] - base_y) * depth + (
                old_join[2] - base_z
            ) * cosine
            shoulder = (0, base_y + height * depth, base_z + height * cosine)
            assert _brightness_near_world(panel, side, shoulder) > 600
        assert _brightness_near_world(panel, side, old_join) < 120
        _frame_axial_join(maya_cmds, camera, camera_shape)
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        front = _capture_view(panel, tmp_path / "pointed_front.png")
        assert (
            _brightness_near_world(panel, front, (0.0125, base_y, base_z))
            < 600
        )
        assert _brightness_near_world(panel, front, (0.025, 0.13, 0.48)) > 600


@pytest.mark.parametrize("part", (3, 4, 5))
@pytest.mark.parametrize("offset", (0, -0.02))
def test_axial_circle_planar_part_removes_internal_rims(
    maya_cmds, new_scene, tmp_path, part, offset
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(
        maya_cmds,
        "WideCircleAxial",
        shapeCircleAngle=180,
        shapePart=True,
        shapePartShape=part,
        shapePartType=1,
        shapePartOffset=offset,
    ) as (_, _, camera, camera_shape, panel):
        _frame_axial_join(maya_cmds, camera, camera_shape)
        pixels = _capture_view(panel, tmp_path / "planar_rims.png")
        assert (
            _brightness_near_world(
                panel, pixels, (0.025, -offset + 0.015, 0.5)
            )
            < 120
        )
        assert (
            _brightness_near_world(panel, pixels, (0.05, -offset, 0.5)) > 600
        )


@pytest.mark.parametrize("part", (3, 4, 5))
@pytest.mark.parametrize("offset", (0, -0.02))
def test_axial_circle_planar_part_has_no_duplicate_transparent_fill(
    maya_cmds, new_scene, tmp_path, part, offset
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(
        maya_cmds,
        "WideCircleAxial",
        shapeCircleAngle=180,
        shapePart=True,
        shapePartShape=part,
        shapePartOffset=offset,
        shapeFill=True,
        shapeLineTransparency=1,
        shapeFillTransparency=0.5,
    ) as (_, shape, camera, camera_shape, panel):
        _frame_axial_join(maya_cmds, camera, camera_shape, oblique=True)
        combined = _capture_view(panel, tmp_path / "combined_fill.png")
        maya_cmds.setAttr(f"{shape}.shapeWideWidth", 0)
        single = _capture_view(panel, tmp_path / "single_fill.png")
        point = (0.01, -offset + 0.015, 0.5)
        actual = _brightness_near_world(panel, combined, point)
        expected = _brightness_near_world(panel, single, point)
        assert expected > 120
        assert actual == pytest.approx(expected, abs=10), (actual, expected)


@pytest.mark.parametrize("part", (3, 4, 5, 9, 10))
@pytest.mark.parametrize("filled", (False, True))
def test_axial_circle_large_part_removes_the_tangent_step(
    maya_cmds, new_scene, tmp_path, part, filled
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(
        maya_cmds,
        "WideCircleAxial",
        shapeCircleAngle=180,
        shapeWideWidth=0.1,
        shapePart=True,
        shapePartShape=part,
        shapePartType=1,
        shapePartSize=6,
        shapeFill=filled,
    ) as (_, _, camera, camera_shape, panel):
        maya_cmds.setAttr(f"{camera}.translate", 4, 0.2, 0.3)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 1.2)
        target = maya_cmds.createNode("transform")
        maya_cmds.setAttr(f"{target}.translate", 0, 0.2, 0.3)
        constraint = maya_cmds.aimConstraint(
            target, camera, aimVector=(0, 0, -1), upVector=(0, 1, 0)
        )
        maya_cmds.delete(constraint, target)
        pixels = _capture_view(panel, tmp_path / "large_part_side.png")
        for point in ((0, 0, 0.5), (0, 0.5, 0)):
            assert _brightness_near_world(panel, pixels, point) > 600
        # 元の接線配置へ延ばす補助面の位置を、輪郭と塗りの両方で確認する。
        old_step = (0, 0.3, 0.475) if part <= 5 else (0, 0.51, 0.05)
        assert _brightness_near_world(panel, pixels, old_step) < 120


@pytest.mark.parametrize("part", (6, 7, 8))
def test_axial_circle_large_solid_part_removes_rims_inside_the_volume(
    maya_cmds, new_scene, tmp_path, part
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    import math

    with _drawing_view(
        maya_cmds,
        "WideCircleAxial",
        shapeCircleAngle=180,
        shapeWideWidth=0.1,
        shapePart=True,
        shapePartShape=part,
        shapePartType=1,
        shapePartSize=6,
    ) as (_, _, _, _, panel):
        pixels = _capture_view(panel, tmp_path / "large_solid_rims.png")
        for x in (-0.05, 0.05):
            assert (
                _brightness_near_world(panel, pixels, (x, 0.5, 0)) > 600
            ), "Partの外側にある円弧の輪郭が失われている"
            assert (
                _brightness_near_world(
                    panel,
                    pixels,
                    (x, 0.5 * math.sin(0.06), 0.5 * math.cos(0.06)),
                )
                < 120
            ), "立体Partの内部に帯の輪郭が残っている"


@pytest.mark.parametrize("part", (9, 10))
@pytest.mark.parametrize("filled", (False, True))
def test_axial_circle_pointed_solid_replaces_the_arc_near_its_tip(
    maya_cmds, new_scene, tmp_path, part, filled
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    import math

    with _drawing_view(
        maya_cmds,
        "WideCircleAxial",
        shapeCircleAngle=360,
        shapeWideWidth=0.1,
        shapePart=True,
        shapePartShape=part,
        shapePartType=1,
        shapePartSize=6,
        shapeFill=filled,
    ) as (_, _, camera, camera_shape, panel):
        maya_cmds.setAttr(f"{camera}.translate", 4, 0, 0)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 1.6)
        target = maya_cmds.createNode("transform")
        constraint = maya_cmds.aimConstraint(
            target, camera, aimVector=(0, 0, -1), upVector=(0, 1, 0)
        )
        maya_cmds.delete(constraint, target)
        pixels = _capture_view(panel, tmp_path / "pointed_solid_tip.png")
        for point in ((0, -0.5, 0), (0, 0.5, 0)):
            assert _brightness_near_world(panel, pixels, point) > 600
        for sign in (-1, 1):
            point = (0, -0.5 * math.cos(0.2), sign * 0.5 * math.sin(0.2))
            assert (
                _brightness_near_world(panel, pixels, point) < 120
            ), "先端型Partで置き換えた区間に元の円弧片が残っている"
