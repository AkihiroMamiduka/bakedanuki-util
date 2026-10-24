"""実際のViewport 2.0でコントローラの選択表示を確認する。"""

from __future__ import annotations

import os
import math
from contextlib import contextmanager
from ctypes import string_at
from pathlib import Path

import pytest

pytestmark = pytest.mark.maya

CIRCLE_SHAPES = (
    "Circle",
    "WideCircleRadial",
    "WideCircleAxial",
    "CrossCircle",
    "WideCrossCircleRadial",
    "WideCrossCircleAxial",
)


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


def _aim_at_origin(cmds, camera, position):
    cmds.setAttr(f"{camera}.translate", *position)
    target = cmds.createNode("transform")
    constraint = cmds.aimConstraint(
        target, camera, aimVector=(0, 0, -1), upVector=(0, 1, 0)
    )
    cmds.delete(constraint, target)


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
            angle = -math.pi / 6 + 0.06
            point = (0, 0.5 * math.sin(angle), 0.5 * math.cos(angle))
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


@pytest.mark.parametrize("preset", CIRCLE_SHAPES)
@pytest.mark.parametrize("filled", (False, True))
def test_circle_fin_has_no_visible_geometry(
    maya_cmds, new_scene, tmp_path, preset, filled
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds,
        preset,
        shapeFill=filled,
        shapeCircleAngle=240,
        shapePart=True,
        shapePartShape=1,
        shapePartType=1,
        shapePartSize=2,
    ) as (_, shape, camera, _, panel):
        _aim_at_origin(maya_cmds, camera, (3, 2, 4))
        baseline = _capture_view(panel, tmp_path / "without_fin.png")
        maya_cmds.setAttr(f"{shape}.shapeFin", True)
        maya_cmds.setAttr(f"{shape}.shapeFinSize", 2)
        maya_cmds.setAttr(f"{shape}.shapeFinWidthScale", 3)
        for kind, height in ((0, 2), (1, -2)):
            maya_cmds.setAttr(f"{shape}.shapeFinType", kind)
            maya_cmds.setAttr(f"{shape}.shapeFinHeight", height)
            assert (
                _capture_view(panel, tmp_path / f"fin_{kind}.png") == baseline
            )


@pytest.mark.parametrize("preset", CIRCLE_SHAPES[3:])
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("placement", (0, 1, 2))
def test_cross_circle_part_sites_and_planes(
    maya_cmds, new_scene, tmp_path, preset, filled, placement
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds,
        preset,
        shapeFill=filled,
        shapeCircleAngle=180,
        shapePart=True,
        shapePartShape=0,
        shapePartType=placement,
        shapePartSize=10 if placement == 2 else 2,
    ) as (_, _, camera, camera_shape, panel):
        _aim_at_origin(maya_cmds, camera, (3, 2, 4))
        maya_cmds.setAttr(
            f"{camera_shape}.orthographicWidth", 3.8 if placement == 2 else 1.8
        )
        pixels = _capture_view(panel, tmp_path / "parts.png")
        axial = preset.endswith("Axial")
        if placement == 2:
            # 頂部は代表円の主面に一つだけ付け、もう一方の主面へ複製しない。
            height = math.sqrt(0.25 - 0.025**2) if axial else 0.5
            wing = (0.75, height, 0) if axial else (0, 0.45096189432, 0.75)
            other = (0, height, 0.75) if axial else (0.75, 0.45096189432, 0)
            assert _brightness_near_world(panel, pixels, wing) > 600
            assert _brightness_near_world(panel, pixels, other) < 120
        else:
            depth = 0.2 * math.cos(math.pi / 6)
            wing = (
                (0.1, 0.5 * math.sin(2 * depth), 0.5 * math.cos(2 * depth))
                if axial
                else (0, 0.6 * math.sin(2 * depth), 0.6 * math.cos(2 * depth))
            )
            probes = (
                wing,
                (wing[0], wing[1], -wing[2]),
                (wing[2], wing[1], -wing[0]),
                (-wing[2], wing[1], wing[0]),
            )
            for index, point in enumerate(probes):
                brightness = _brightness_near_world(panel, pixels, point)
                if placement == 1 or index == 0:
                    assert brightness > 600, (preset, placement, index)
                else:
                    assert brightness < 120, (preset, placement, index)


@pytest.mark.parametrize(
    "preset",
    ("Circle", "WideCircleRadial", "CrossCircle", "WideCrossCircleRadial"),
)
@pytest.mark.parametrize("filled", (False, True))
def test_radial_circle_long_arrow_follows_the_arc_and_keeps_its_tip(
    maya_cmds, new_scene, tmp_path, preset, filled
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(
        maya_cmds,
        preset,
        shapeCircleAngle=180,
        shapePart=True,
        shapePartShape=0,
        shapePartLengthScale=6.7,
        shapeFill=filled,
    ) as (_, shape, camera, camera_shape, panel):
        _aim_at_origin(maya_cmds, camera, (4, 0, 0))
        maya_cmds.setAttr(f"{camera}.translate", 4, 0.2, 0.05)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 1.6)
        depth = 0.67 * math.cos(math.pi / 6)
        wing_y = 0.55 * math.sin(2 * depth)
        wing_z = 0.55 * math.cos(2 * depth)
        for placement in (0, 1):
            maya_cmds.setAttr(f"{shape}.shapePartType", placement)
            pixels = _capture_view(
                panel, tmp_path / f"long_arrow_{placement}.png"
            )
            assert (
                _brightness_near_world(panel, pixels, (0, wing_y, wing_z))
                > 600
            ), "矢印の後端が円周上へ配置されていない"
            opposite = _brightness_near_world(
                panel, pixels, (0, wing_y, -wing_z)
            )
            if placement == 1:
                assert (
                    opposite > 600
                ), "AtEndsの反対側の矢印が円周へ追従していない"
            else:
                assert opposite < 120, "AtEndで反対側にも矢印が追加されている"
            for sign in ((-1, 1) if placement == 1 else (1,)):
                assert (
                    _brightness_near_world(
                        panel, pixels, (0, depth, sign * 0.55)
                    )
                    < 120
                ), "元の接線姿勢の矢印が残っている"
                assert (
                    _brightness_near_world(panel, pixels, (0, 0, sign * 0.5))
                    > 600
                ), "円周変形で矢印先端が円弧端点から移動している"


@pytest.mark.parametrize(
    "preset", ("WideCircleRadial", "WideCrossCircleRadial")
)
@pytest.mark.parametrize("filled", (False, True))
def test_radial_circle_wrapped_arrow_removes_internal_band_rims(
    maya_cmds, new_scene, tmp_path, preset, filled
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(
        maya_cmds,
        preset,
        shapeCircleAngle=180,
        shapeWideWidth=0.05,
        shapePart=True,
        shapePartShape=0,
        shapePartLengthScale=6.7,
        shapeFill=filled,
        shapeFillTransparency=0.8,
    ) as (_, _, camera, camera_shape, panel):
        depth = 0.67 * math.cos(math.pi / 6)
        rear_angle = 2 * depth
        rear = (0, 0.5 * math.sin(rear_angle), 0.5 * math.cos(rear_angle))
        _aim_at_origin(maya_cmds, camera, (4, 0, 0))
        maya_cmds.setAttr(f"{camera}.translate", 4, rear[1], rear[2])
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 0.4)
        pixels = _capture_view(panel, tmp_path / "radial_rear_join.png")
        assert (
            _brightness_near_world(panel, pixels, rear) < 400
        ), "帯と矢印の接合部に後端の内部線が残っている"
        inside_angle = 0.8 * rear_angle
        for radius in (0.475, 0.525):
            before = (
                0,
                radius * math.sin(rear_angle + 0.08),
                radius * math.cos(rear_angle + 0.08),
            )
            inside = (
                0,
                radius * math.sin(inside_angle),
                radius * math.cos(inside_angle),
            )
            assert _brightness_near_world(panel, pixels, before) > 600, (
                "Partの後端より本体側の円弧が失われている",
                radius,
            )
            assert _brightness_near_world(panel, pixels, inside) < 400, (
                "矢印内部に帯の円弧が残っている",
                radius,
            )
        for radius in (0.46, 0.54):
            assert (
                _brightness_near_world(
                    panel,
                    pixels,
                    (
                        0,
                        radius * math.sin(inside_angle),
                        radius * math.cos(inside_angle),
                    ),
                )
                > 600
            ), "帯の輪郭を除いた位置に、曲がったPartの輪郭がない"


@pytest.mark.parametrize("preset", ("Circle", "CrossCircle"))
def test_radial_circle_wrapping_preserves_sector_fill_without_overlap(
    maya_cmds, new_scene, tmp_path, preset
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds,
        preset,
        shapeCircleAngle=180,
        shapePart=True,
        shapePartShape=0,
        shapePartType=1,
        shapePartLengthScale=6.7,
        shapeFill=True,
        shapeLineTransparency=1,
        shapeFillTransparency=0.5,
    ) as (_, shape, camera, _, panel):
        _aim_at_origin(maya_cmds, camera, (4, 0, 0))
        actual = _capture_view(panel, tmp_path / "wrapped_sector.png")
        maya_cmds.setAttr(f"{shape}.shapePart", False)
        reference = _capture_view(panel, tmp_path / "plain_sector.png")
        for angle in (0.12, math.pi / 2):
            point = (0, 0.2 * math.sin(angle), 0.2 * math.cos(angle))
            expected = _brightness_near_world(panel, reference, point)
            assert expected > 120
            assert _brightness_near_world(
                panel, actual, point
            ) == pytest.approx(expected, abs=10)


@pytest.mark.parametrize("filled", (False, True))
def test_radial_circle_wide_marker_does_not_fold_through_center(
    maya_cmds, new_scene, tmp_path, filled
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds,
        "WideCircleRadial",
        shapeCircleAngle=180,
        shapePart=True,
        shapePartShape=3,
        shapePartLengthScale=6.7,
        shapePartWidthScale=40,
        shapeFill=filled,
    ) as (_, _, camera, camera_shape, panel):
        _aim_at_origin(maya_cmds, camera, (4, 0, 0))
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 6)
        pixels = _capture_view(panel, tmp_path / "center_clipped_marker.png")
        assert _brightness_near_world(panel, pixels, (0, 0, 2.5)) > 600
        assert _brightness_near_world(panel, pixels, (0, 0, -1.5)) < 120


@pytest.mark.parametrize("filled", (False, True))
def test_radial_circle_arrow3d_crest_follows_curve_and_plane_normal(
    maya_cmds, new_scene, tmp_path, filled
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds,
        "WideCircleRadial",
        shapeCircleAngle=180,
        shapePart=True,
        shapePartShape=1,
        shapePartLengthScale=6.7,
        shapeFill=filled,
    ) as (_, _, camera, camera_shape, panel):
        maya_cmds.setAttr(f"{camera}.translate", 0, 0.4, 4)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 0.35)
        angle = 1.34 * math.cos(math.pi / 6)
        point = (0.05, 0.5 * math.sin(angle), 0.5 * math.cos(angle))
        pixels = _capture_view(panel, tmp_path / "radial_crest.png")
        assert _brightness_near_world(panel, pixels, point) > 600
        assert (
            _brightness_near_world(panel, pixels, (-point[0], *point[1:]))
            < 120
        )


def test_radial_circle_multiple_turns_have_one_transparent_fill(
    maya_cmds, new_scene, tmp_path
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds,
        "WideCircleRadial",
        shapeCircleAngle=180,
        shapePart=True,
        shapePartShape=3,
        shapePartType=1,
        shapePartLengthScale=50,
        shapePartWidthScale=40,
        shapeFill=True,
        shapeLineTransparency=1,
        shapeFillTransparency=0.5,
    ) as (_, shape, camera, camera_shape, panel):
        _aim_at_origin(maya_cmds, camera, (4, 0, 0))
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 6)
        actual = _capture_view(panel, tmp_path / "periodic_fill.png")
        names = maya_cmds.attributeQuery("shape", node=shape, listEnum=True)[
            0
        ].split(":")
        maya_cmds.setAttr(f"{shape}.shape", names.index("Circle"))
        maya_cmds.setAttr(f"{shape}.shapePart", False)
        maya_cmds.setAttr(f"{shape}.shapeCircleAngle", 360)
        maya_cmds.setAttr(f"{shape}.shapeRootSize", 5)
        reference = _capture_view(panel, tmp_path / "single_disk.png")
        for point in ((0, 0.2, 0.2), (0, -1, 1), (0, 1.5, 0)):
            expected = _brightness_near_world(panel, reference, point)
            assert expected > 120
            assert _brightness_near_world(
                panel, actual, point
            ) == pytest.approx(expected, abs=10)


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("angle", (180, 360))
def test_cross_circle_axial_join_removes_internal_rims_and_keeps_outer_arcs(
    maya_cmds, new_scene, tmp_path, filled, angle
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(
        maya_cmds,
        "WideCrossCircleAxial",
        shapeWideWidth=0.3,
        shapeCircleAngle=angle,
        shapeFill=filled,
        shapeFillTransparency=0.8,
    ) as (_, _, camera, camera_shape, panel):
        sign = 1 if angle == 180 else -1
        maya_cmds.setAttr(f"{camera}.translate", 0, sign * 4, 0)
        maya_cmds.setAttr(f"{camera}.rotateX", -sign * 90)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 1.4)
        pixels = _capture_view(panel, tmp_path / "joined_rims.png")
        height = sign * math.sqrt(0.25 - 0.15**2)
        for point in (
            (0.15, height, 0),
            (-0.15, height, 0),
            (0, height, 0.15),
            (0, height, -0.15),
        ):
            assert _brightness_near_world(panel, pixels, point) < 400, (
                "交差部に元の円弧の輪郭または平面の継ぎ目線が残っている",
                angle,
                point,
            )
        outer_height = sign * math.sqrt(0.25 - 0.35**2)
        for point in (
            (0.15, outer_height, 0.35),
            (-0.15, outer_height, -0.35),
            (0.35, outer_height, 0.15),
            (-0.35, outer_height, -0.15),
        ):
            assert _brightness_near_world(panel, pixels, point) > 600, (
                "交差部の外側にある円弧の輪郭が失われている",
                angle,
                point,
            )


def test_cross_circle_axial_join_has_one_transparent_top_face(
    maya_cmds, new_scene, tmp_path
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(
        maya_cmds,
        "WideCrossCircleAxial",
        shapeWideWidth=0.3,
        shapeCircleAngle=180,
        shapeFill=True,
        shapeLineTransparency=1,
        shapeFillTransparency=0.5,
    ) as (_, shape, camera, _, panel):
        maya_cmds.setAttr(f"{camera}.translate", 0, 4, 0)
        maya_cmds.setAttr(f"{camera}.rotateX", -90)
        joined = _capture_view(panel, tmp_path / "joined_transparent_top.png")
        names = maya_cmds.attributeQuery("shape", node=shape, listEnum=True)[
            0
        ].split(":")
        maya_cmds.setAttr(f"{shape}.shape", names.index("Square"))
        maya_cmds.setAttr(f"{shape}.shapeRotateZ", 90)
        reference = _capture_view(
            panel, tmp_path / "single_transparent_face.png"
        )
        for point in ((0, 0, 0), (0.04, 0, 0.025), (-0.03, 0, 0.06)):
            expected = _brightness_near_world(panel, reference, point)
            actual = _brightness_near_world(panel, joined, point)
            assert expected > 120
            assert actual == pytest.approx(expected, abs=10), (
                "接合した平面の透過色が一枚の面と一致しない",
                actual,
                expected,
            )


@pytest.mark.parametrize("filled", (False, True))
def test_cross_circle_axial_apex_follows_the_joined_top_face(
    maya_cmds, new_scene, tmp_path, filled
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(
        maya_cmds,
        "WideCrossCircleAxial",
        shapeWideWidth=0.6,
        shapeCircleAngle=180,
        shapePart=True,
        shapePartType=2,
        shapePartShape=3,
        shapePartSize=2,
        shapeFill=filled,
        shapeFillTransparency=0.8,
    ) as (_, shape, _, _, panel):
        height = math.sqrt(0.25 - 0.3**2)
        for offset in (0, 0.1):
            maya_cmds.setAttr(f"{shape}.shapePartOffset", offset)
            pixels = _capture_view(
                panel, tmp_path / f"joined_apex_{offset}.png"
            )
            assert (
                _brightness_near_world(
                    panel, pixels, (0.075, height + 0.1 + offset, 0)
                )
                > 600
            ), "AtApexのPartが接合面中央へ追従していない"
            assert (
                _brightness_near_world(panel, pixels, (0.075, 0.6 + offset, 0))
                < 120
            ), "元の円頂部にAtApexのPartが残っている"


@pytest.mark.parametrize("filled", (False, True))
def test_cross_circle_axial_join_preserves_wrapped_arrow3d_crest(
    maya_cmds, new_scene, tmp_path, filled
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(
        maya_cmds,
        "WideCrossCircleAxial",
        shapeWideWidth=0.3,
        shapeCircleAngle=90,
        shapePart=True,
        shapePartType=0,
        shapePartShape=1,
        shapePartSize=6,
        shapeFill=filled,
        shapeFillTransparency=0.8,
    ) as (_, _, camera, camera_shape, panel):
        maya_cmds.setAttr(f"{camera}.translate", 4, 0.6, 0.05)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 0.6)
        target = maya_cmds.createNode("transform")
        maya_cmds.setAttr(f"{target}.translate", 0, 0.6, 0.05)
        constraint = maya_cmds.aimConstraint(
            target, camera, aimVector=(0, 0, -1), upVector=(0, 1, 0)
        )
        maya_cmds.delete(constraint, target)
        pixels = _capture_view(panel, tmp_path / "joined_arrow3d_crest.png")
        angle = 15 * math.pi / 32
        depth = 0.6 * math.cos(math.pi / 6)
        crest = 0.3 * (angle - math.pi / 4) / (2 * depth)
        height = math.sqrt(0.25 - 0.15**2)
        side = (0.5 + crest) * math.cos(angle)
        assert (
            _brightness_near_world(
                panel, pixels, (0, height + crest * math.sin(angle), side)
            )
            > 600
        ), "接合面へ移したArrow3Dの立ち上がりが失われている"
        assert (
            _brightness_near_world(
                panel, pixels, (0, (0.5 + crest) * math.sin(angle), side)
            )
            < 120
        ), "Arrow3Dの稜線が元の円筒面の高さに残っている"


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
        for sign in (-1, 1):
            assert (
                _brightness_near_world(
                    panel,
                    pixels,
                    (
                        0,
                        0.525 * math.sin(2 * depth),
                        sign * 0.525 * math.cos(2 * depth),
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


@pytest.mark.parametrize("part", range(6))
def test_axial_circle_wrapped_part_ignores_distance_offset(
    maya_cmds, new_scene, tmp_path, part
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
        shapePartSize=2,
    ) as (_, shape, _, _, panel):
        expected = _capture_view(panel, tmp_path / "offset_zero.png")
        for offset in (-0.3, 0.3):
            maya_cmds.setAttr(f"{shape}.shapePartOffset", offset)
            actual = _capture_view(panel, tmp_path / f"offset_{offset}.png")
            assert actual == expected, "曲面Partへ距離Offsetが作用している"
            assert maya_cmds.getAttr(f"{shape}.shapePartOffset") == offset


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
@pytest.mark.parametrize("part", range(6))
def test_axial_circle_wrapped_part_follows_the_circle(
    maya_cmds, new_scene, tmp_path, filled, part
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    import math

    with _drawing_view(
        maya_cmds,
        "WideCircleAxial",
        shapeCircleAngle=180,
        shapePart=True,
        shapePartShape=part,
        shapePartType=1,
        shapePartSize=6,
        shapeFill=filled,
    ) as (_, _, camera, camera_shape, panel):
        maya_cmds.setAttr(f"{camera}.translate", 4, 0.12, 0.46)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 0.45)
        target = maya_cmds.createNode("transform")
        maya_cmds.setAttr(f"{target}.translate", 0, 0.12, 0.46)
        constraint = maya_cmds.aimConstraint(
            target, camera, aimVector=(0, 0, -1), upVector=(0, 1, 0)
        )
        maya_cmds.delete(constraint, target)
        pixels = _capture_view(panel, tmp_path / "curved_part_side.png")
        for angle in (0.15, 0.25, 0.35):
            point = (0, 0.5 * math.sin(angle), 0.5 * math.cos(angle))
            assert (
                _brightness_near_world(panel, pixels, point) > 600
            ), "Part部分が円周から離れている"
        assert (
            _brightness_near_world(panel, pixels, (0, 0.12, 0.43)) < 120
        ), "円の内側に直線のPartや補助面が残っている"


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
        assert _brightness_near_world(panel, pixels, (0.025, 0.015, 0.5)) < 120
        assert _brightness_near_world(panel, pixels, (0.05, 0, 0.5)) > 600


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
        point = (0.01, 0.015, 0.5)
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


@pytest.mark.parametrize("part", (3, 4, 5))
@pytest.mark.parametrize("width", (0, 0.1))
@pytest.mark.parametrize("filled", (False, True))
def test_axial_circle_planar_apex_keeps_the_original_circle(
    maya_cmds, new_scene, tmp_path, part, width, filled
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    import math

    with _drawing_view(
        maya_cmds,
        "WideCircleAxial",
        shapeWideWidth=width,
        shapePart=True,
        shapePartShape=part,
        shapePartType=2,
        shapePartSize=6,
        shapeFill=filled,
    ) as (_, _, camera, _, panel):
        maya_cmds.setAttr(f"{camera}.translate", 4, 0, 0)
        target = maya_cmds.createNode("transform")
        constraint = maya_cmds.aimConstraint(
            target, camera, aimVector=(0, 0, -1), upVector=(0, 1, 0)
        )
        maya_cmds.delete(constraint, target)
        pixels = _capture_view(panel, tmp_path / "planar_apex_circle.png")
        for sign in (-1, 1):
            point = (0, 0.5 * math.cos(0.25), sign * 0.5 * math.sin(0.25))
            assert (
                _brightness_near_world(panel, pixels, point) > 600
            ), "AtApexの平面Partが円筒上部を切り取っている"
        assert (
            _brightness_near_world(panel, pixels, (0, 0.2, 0.3)) < 120
        ), "円弧を平らに置き換える接合面が残っている"


@pytest.mark.parametrize("all_ends", (False, True))
def test_axial_circle_long_wrapped_part_has_no_duplicate_periodic_fill(
    maya_cmds, new_scene, tmp_path, all_ends
):
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")

    with _drawing_view(
        maya_cmds,
        "WideCircleAxial",
        shapePart=True,
        shapePartShape=3,
        shapePartType=int(all_ends),
        shapePartSize=8,
        shapePartLengthScale=5,
        shapeFill=True,
        shapeLineTransparency=1,
        shapeFillTransparency=0.5,
    ) as (_, shape, _, _, panel):
        wrapped = _capture_view(panel, tmp_path / "periodic_wrapped_fill.png")
        # 一周より長いSquareは、同じ幅の円筒側面一枚と一致する。
        maya_cmds.setAttr(f"{shape}.shapePart", False)
        maya_cmds.setAttr(f"{shape}.shapeWideWidth", 0.8)
        reference = _capture_view(
            panel, tmp_path / "periodic_reference_fill.png"
        )
        for point in ((0.1, 0.1, 0.49), (-0.1, 0.2, 0.45)):
            expected = _brightness_near_world(panel, reference, point)
            actual = _brightness_near_world(panel, wrapped, point)
            assert expected > 120
            assert actual == pytest.approx(expected, abs=10), (
                actual,
                expected,
            )
