"""保持されたFill描画を、通常のViewport更新と実再生で確認する。"""

from __future__ import annotations

import os
import time
from contextlib import contextmanager
from ctypes import string_at
from pathlib import Path

import pytest

from controller_shape_cases import SHAPE_NAMES, set_preset
from test_controller_shape_viewport import (
    _aim_at_origin,
    _capture_normal_update,
    _drawing_view,
)

pytestmark = pytest.mark.maya

FILL_VARIANTS = (
    ("Cube", {"shapeFillTransparency": 0.0}),
    ("Sphere", {"shapeFillTransparency": 0.0}),
    ("Circle", {"shapeFillTransparency": 0.0}),
    ("WideCube", {}),
    ("WideSphere", {}),
    ("WideCircle", {}),
    ("WideCrossLine3Axis", {}),
    ("ColorCube", {"shapePart": True, "shapePartShape": 1}),
    (
        "ColorCube",
        {"shapePart": True, "shapePartShape": 1, "shapeFillTransparency": 0.0},
    ),
    ("ColorCornerCube", {"shapeFin": True}),
    (
        "WideArcRadial",
        {
            "shapePart": True,
            "shapePartShape": 3,
            "shape1stAxis": 2,
            "shape2ndAxis": 0,
        },
    ),
    (
        "WideArcAxial",
        {
            "shapePart": True,
            "shapePartShape": 1,
            "shape1stAxis": 2,
            "shape2ndAxis": 0,
        },
    ),
    (
        "WideCrossArcAxial",
        {
            "shapePart": True,
            "shapeFin": True,
            "shape1stAxis": 2,
            "shape2ndAxis": 0,
        },
    ),
    ("Circle", {"shapePart": True, "shapePartShape": 1, "shapeFin": True}),
)


def _require_gui(cmds):
    if cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")


def _assert_visible(pixels):
    assert any(
        pixels[index : index + 4] != pixels[:4]
        for index in range(0, len(pixels), 4)
    ), "シェイプが背景だけになっている"


@contextmanager
def _fill_view(cmds, preset, *, fixed=True, **options):
    settings = dict(
        shapeFill=True,
        shapeFillTransparency=0.85,
        shapeLineWidth=1.0,
        shapeLineTransparency=0.0,
        shapeDrawOnTop=False,
    )
    settings.update(options)
    with _drawing_view(
        cmds, preset, fixed_viewport=fixed, **settings
    ) as values:
        transform, _, camera, camera_shape, _ = values
        _aim_at_origin(cmds, camera, (3, 2, 4))
        cmds.setAttr(f"{camera_shape}.orthographicWidth", 2.8)
        try:
            yield values
        finally:
            # 比較用の別シーンに、閉じたViewportのDAGを残さない。
            for node in (transform, camera):
                if cmds.objExists(node):
                    cmds.delete(node)


def _take(panel, directory, label, change):
    directory.mkdir(parents=True, exist_ok=True)
    return _capture_normal_update(panel, directory / f"{label}.png", change)


def _warm(cmds, values, directory):
    _, _, camera, _, panel = values
    _take(
        panel,
        directory,
        "warmup",
        lambda: cmds.setAttr(f"{camera}.translateX", 3.031),
    )
    first = _take(
        panel,
        directory,
        "initial",
        lambda: cmds.setAttr(f"{camera}.translateX", 3.0),
    )
    _assert_visible(first)
    return first


@pytest.mark.parametrize("preset", SHAPE_NAMES)
def test_fill_shape_motion_and_wire_restore(
    maya_cmds, new_scene, tmp_path, preset
):
    """全基本形状のFill・線切替と親子操作は、元の画像へ復帰する。"""
    _require_gui(maya_cmds)
    with _fill_view(maya_cmds, preset) as values:
        transform, shape, _, _, panel = values
        parent = maya_cmds.group(transform)
        first = _warm(maya_cmds, values, tmp_path)
        moved = _take(
            panel,
            tmp_path,
            "child_moved",
            lambda: maya_cmds.setAttr(f"{transform}.translateX", 0.19),
        )
        assert moved != first
        assert (
            _take(
                panel,
                tmp_path,
                "child_restored",
                lambda: maya_cmds.setAttr(f"{transform}.translateX", 0),
            )
            == first
        )
        assert (
            _take(
                panel,
                tmp_path,
                "parent_rotated",
                lambda: maya_cmds.setAttr(f"{parent}.rotate", 17, 33, -11),
            )
            != first
        )
        assert (
            _take(
                panel,
                tmp_path,
                "parent_restored",
                lambda: maya_cmds.setAttr(f"{parent}.rotate", 0, 0, 0),
            )
            == first
        )
        wire = _take(
            panel,
            tmp_path,
            "wire_control",
            lambda: maya_cmds.setAttr(f"{shape}.shapeFill", False),
        )
        _assert_visible(wire)
        assert (
            _take(
                panel,
                tmp_path,
                "fill_restored",
                lambda: maya_cmds.setAttr(f"{shape}.shapeFill", True),
            )
            == first
        )


@pytest.mark.parametrize(
    "preset,options", FILL_VARIANTS, ids=[item[0] for item in FILL_VARIANTS]
)
def test_fill_variant_switch_matches_independent_shape(
    maya_cmds, new_scene, tmp_path, preset, options
):
    """Wide・Part・Finへ切り替えた像は、独立生成した同じ設定の像と一致する。"""
    _require_gui(maya_cmds)
    with _fill_view(maya_cmds, preset, **options) as values:
        expected = _warm(maya_cmds, values, tmp_path / "reference")
    with _fill_view(maya_cmds, "Cube") as values:
        _, shape, _, _, panel = values
        first = _warm(maya_cmds, values, tmp_path)
        defaults = {
            attribute: maya_cmds.getAttr(f"{shape}.{attribute}")
            for attribute in options
        }

        def switch():
            set_preset(maya_cmds, shape, preset)
            for attribute, value in options.items():
                maya_cmds.setAttr(f"{shape}.{attribute}", value)

        assert _take(panel, tmp_path, "variant", switch) == expected

        def restore():
            for attribute, value in defaults.items():
                maya_cmds.setAttr(f"{shape}.{attribute}", value)
            set_preset(maya_cmds, shape, "Cube")

        assert _take(panel, tmp_path, "cube_restored", restore) == first


@pytest.mark.parametrize("preset", ("Cube", "ColorCube", "ColorCornerCube"))
def test_fill_display_routes_restore(maya_cmds, new_scene, tmp_path, preset):
    """markerと代替線形状は、Fill・表示スタイル・線透明度の往復で残留しない。"""
    _require_gui(maya_cmds)
    with _fill_view(maya_cmds, preset) as values:
        _, shape, _, _, panel = values
        first = _warm(maya_cmds, values, tmp_path)
        for label, attribute, value in (
            ("fill_off", "shapeFill", False),
            ("line_alpha", "shapeLineTransparency", 0.55),
            ("width_fallback", "shapeLineWidth", 2.0),
            ("top_fallback", "shapeDrawOnTop", True),
            ("template_fallback", "shapeTemplateLine", True),
            ("fill_invisible", "shapeFillTransparency", 1.0),
        ):
            old = maya_cmds.getAttr(f"{shape}.{attribute}")
            _take(
                panel,
                tmp_path,
                label,
                lambda attr=attribute, changed=value: maya_cmds.setAttr(
                    f"{shape}.{attr}", changed
                ),
            )
            assert (
                _take(
                    panel,
                    tmp_path,
                    f"{label}_restored",
                    lambda attr=attribute, saved=old: maya_cmds.setAttr(
                        f"{shape}.{attr}", saved
                    ),
                )
                == first
            )
        _assert_visible(
            _take(
                panel,
                tmp_path,
                "wireframe_style",
                lambda: maya_cmds.modelEditor(
                    panel, edit=True, displayAppearance="wireframe"
                ),
            )
        )
        assert (
            _take(
                panel,
                tmp_path,
                "shaded_restored",
                lambda: maya_cmds.modelEditor(
                    panel, edit=True, displayAppearance="smoothShaded"
                ),
            )
            == first
        )


@pytest.mark.parametrize("preset", ("Cube", "Sphere", "ColorCube"))
def test_fill_independent_reflections_restore(
    maya_cmds, new_scene, tmp_path, preset
):
    """親・静的形状・接続行列を個別に反転しても、元の面と線へ復帰する。"""
    _require_gui(maya_cmds)
    with _fill_view(maya_cmds, preset) as values:
        transform, shape, _, _, panel = values
        first = _warm(maya_cmds, values, tmp_path)
        driver = maya_cmds.createNode("composeMatrix")
        maya_cmds.connectAttr(
            f"{driver}.outputMatrix", f"{shape}.shapeTransformMatrix"
        )
        for label, node, attribute in (
            ("parent", transform, "scaleX"),
            ("static", shape, "shapeScaleX"),
            ("animation", driver, "inputScaleX"),
        ):
            reflected = _take(
                panel,
                tmp_path,
                f"negative_{label}",
                lambda target=node, attr=attribute: maya_cmds.setAttr(
                    f"{target}.{attr}", -1
                ),
            )
            _assert_visible(reflected)
            assert (
                _take(
                    panel,
                    tmp_path,
                    f"{label}_restored",
                    lambda target=node, attr=attribute: maya_cmds.setAttr(
                        f"{target}.{attr}", 1
                    ),
                )
                == first
            )


def _read_frame(panel, path):
    from maya.api import OpenMaya as om, OpenMayaUI as omui

    image = om.MImage()
    omui.M3dView.getM3dViewFromModelPanel(panel).readColorBuffer(image, True)
    width, height = image.getSize()
    pixels = string_at(int(image.pixels()), width * height * 4)
    image.writeToFile(str(path), "png")
    return pixels


def _capture_pair(panels, directory, label, change):
    from maya import utils
    from maya.api import OpenMaya as om, OpenMayaUI as omui

    from bd_util.ui.qt import QtWidgets

    directory.mkdir(parents=True, exist_ok=True)
    images, callbacks, errors = {}, [], []
    for name, panel in panels.items():

        def posted(*_, target=panel, key=name):
            if key in images or errors:
                return
            try:
                images[key] = _read_frame(
                    target, directory / f"{label}_{key}.png"
                )
            except BaseException as error:
                errors.append(error)

        callbacks.append(
            omui.MUiMessage.add3dViewPostRenderMsgCallback(panel, posted)
        )
    try:
        change()
        deadline = time.monotonic() + 8
        application = QtWidgets.QApplication.instance()
        assert application is not None
        while (
            len(images) != len(panels)
            and not errors
            and time.monotonic() < deadline
        ):
            application.processEvents()
            utils.processIdleEvents()
    finally:
        for callback in callbacks:
            om.MMessage.removeCallback(callback)
    assert not errors, errors
    assert set(images) == set(
        panels
    ), "両Viewportの変更後最初の通常postが揃わない"
    return images


@pytest.mark.parametrize("preset", ("Cube", "ColorCube", "ColorCornerCube"))
def test_fill_two_views_keep_independent_highlighting(
    maya_cmds, new_scene, tmp_path, preset
):
    """同時に見える透視・平行投影で、選択強調とFillの復元を独立に保つ。"""
    _require_gui(maya_cmds)
    from maya import utils
    from maya.api import OpenMayaUI as omui

    from bd_util.ui.qt import QtWidgets, wrapInstance

    with _fill_view(maya_cmds, preset, fixed=False) as values:
        transform, _, camera, camera_shape, panel = values
        maya_cmds.setAttr(f"{camera_shape}.orthographic", False)
        control = maya_cmds.modelPanel(panel, query=True, control=True)
        pane = maya_cmds.control(control, query=True, parent=True)
        maya_cmds.paneLayout(pane, edit=True, configuration="vertical2")
        second, _ = maya_cmds.camera(orthographic=True, orthographicWidth=2.8)
        try:
            _aim_at_origin(maya_cmds, second, (-3, 2, -4))
            other = maya_cmds.modelPanel(
                parent=pane, camera=second, menuBarVisible=False
            )
            maya_cmds.modelEditor(
                other,
                edit=True,
                rendererName="vp2Renderer",
                allObjects=True,
                pluginShapes=True,
                locators=True,
                displayAppearance="smoothShaded",
                grid=False,
                headsUpDisplay=False,
                selectionHiliteDisplay=True,
            )
            other_control = maya_cmds.modelPanel(
                other, query=True, control=True
            )
            maya_cmds.paneLayout(pane, edit=True, setPane=(control, 1))
            maya_cmds.paneLayout(pane, edit=True, setPane=(other_control, 2))
            maya_cmds.paneLayout(pane, edit=True, paneSize=(1, 50, 100))
            maya_cmds.paneLayout(pane, edit=True, paneSize=(2, 50, 100))
            first_view = omui.M3dView.getM3dViewFromModelPanel(panel)
            window = wrapInstance(
                int(first_view.widget()), QtWidgets.QWidget
            ).window()
            window.resize(960, 480)
            maya_cmds.setFocus(panel)
            application = QtWidgets.QApplication.instance()
            assert application is not None
            application.processEvents()
            utils.processIdleEvents()
            panels = dict(perspective=panel, orthographic=other)
            views = {
                target: omui.M3dView.getM3dViewFromModelPanel(target)
                for target in panels.values()
            }
            if any(
                view.portWidth() <= 0 or view.portHeight() <= 0
                for view in views.values()
            ):
                # layout初期化だけに使い、変更後の撮影にはrefreshを追加しない。
                maya_cmds.refresh(force=True)
                application.processEvents()
                utils.processIdleEvents()
            assert (
                maya_cmds.paneLayout(
                    pane, query=True, numberOfVisiblePanes=True
                )
                == 2
            )
            for view in views.values():
                assert view.portWidth() > 0 and view.portHeight() > 0
                widget = wrapInstance(int(view.widget()), QtWidgets.QWidget)
                widget.setFixedSize(widget.size())
            take = lambda label, change: _capture_pair(
                panels, tmp_path, label, change
            )
            take(
                "warmup", lambda: maya_cmds.setAttr(f"{transform}.rotateY", 1)
            )
            initial = take(
                "initial", lambda: maya_cmds.setAttr(f"{transform}.rotateY", 0)
            )
            for pixels in initial.values():
                _assert_visible(pixels)
            selected = take("selected", lambda: maya_cmds.select(transform))
            assert selected["perspective"] == initial["perspective"]
            assert selected["orthographic"] != initial["orthographic"]
            take(
                "rotated",
                lambda: maya_cmds.setAttr(f"{transform}.rotate", 17, 33, -11),
            )
            assert (
                take(
                    "rotation_restored",
                    lambda: maya_cmds.setAttr(f"{transform}.rotate", 0, 0, 0),
                )
                == selected
            )
            assert (
                take("deselected", lambda: maya_cmds.select(clear=True))
                == initial
            )
        finally:
            maya_cmds.delete(second)


def _cache_enabled(value):
    if isinstance(value, (list, tuple)):
        return _cache_enabled(value[0]) if value else False
    return str(value).lower() in ("true", "1")


@contextmanager
def _initially_mirrored_view(cmds, preset):
    from maya import utils
    from maya.api import OpenMayaUI as omui

    from bd_util.ui.qt import QtWidgets, wrapInstance

    version = int(cmds.about(apiVersion=True)) // 10000
    plugin = Path(
        os.environ.get(
            "BD_UTIL_NODES_PLUGIN_PATH",
            Path(__file__).resolve().parents[3]
            / f"bakedanuki/bakedanuki-util/plug-ins/maya{version}/bdUtilNodes.mll",
        )
    )
    cmds.loadPlugin(str(plugin), quiet=True)
    parent = cmds.createNode("transform", name="fillMirrorParent")
    cmds.setAttr(f"{parent}.scaleX", -1)
    transform = cmds.createNode("transform", parent=parent)
    shape = cmds.createNode("bdControllerShape", parent=transform)
    set_preset(cmds, shape, preset)
    for attribute, value in (
        ("shapeFill", True),
        ("shapeFillTransparency", 0.0),
        ("shapeLineWidth", 1.0),
        ("shapeLineTransparency", 0.0),
        ("shapeDrawOnTop", False),
        ("overrideEnabled", True),
        ("overrideRGBColors", True),
    ):
        cmds.setAttr(f"{shape}.{attribute}", value)
    cmds.setAttr(f"{shape}.overrideColorRGB", 1, 1, 1)
    camera, camera_shape = cmds.camera(
        orthographic=True, orthographicWidth=2.8
    )
    cmds.setAttr(f"{camera_shape}.nearClipPlane", 0.01)
    _aim_at_origin(cmds, camera, (3, 2, 4))
    window = cmds.window(widthHeight=(480, 480))
    cmds.paneLayout()
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
    try:
        cmds.select(clear=True)
        cmds.showWindow(window)
        cmds.setFocus(panel)
        application = QtWidgets.QApplication.instance()
        assert application is not None
        application.processEvents()
        utils.processIdleEvents()
        view = omui.M3dView.getM3dViewFromModelPanel(panel)
        assert view.portWidth() > 0 and view.portHeight() > 0
        widget = wrapInstance(int(view.widget()), QtWidgets.QWidget)
        widget.setFixedSize(widget.size())
        application.processEvents()
        utils.processIdleEvents()
        assert (
            cmds.xform(transform, query=True, worldSpace=True, matrix=True)[0]
            == -1
        )
        yield parent, (transform, shape, camera, camera_shape, panel)
    finally:
        cmds.deleteUI(window)
        cmds.delete(parent, camera)
        cmds.displayRGBColor("background", *previous_background)


@pytest.mark.parametrize("preset", ("Cube", "ColorCube", "ColorCornerCube"))
def test_opaque_fill_initial_mirror_and_inside_culling(
    maya_cmds, new_scene, tmp_path, preset
):
    """最初から負の親worldを持つ不透明Fillは、鏡映の往復と内部カリングを保つ。"""
    _require_gui(maya_cmds)
    with _initially_mirrored_view(maya_cmds, preset) as (parent, values):
        _, _, camera, camera_shape, panel = values
        outside = _warm(maya_cmds, values, tmp_path)
        background = outside[:4]
        saved_rotation = maya_cmds.getAttr(f"{camera}.rotate")[0]
        positive = _take(
            panel,
            tmp_path,
            "positive_parent",
            lambda: maya_cmds.setAttr(f"{parent}.scaleX", 1),
        )
        _assert_visible(positive)
        assert (
            _take(
                panel,
                tmp_path,
                "negative_restored",
                lambda: maya_cmds.setAttr(f"{parent}.scaleX", -1),
            )
            == outside
        )

        def inside():
            maya_cmds.setAttr(f"{camera_shape}.orthographic", False)
            maya_cmds.setAttr(f"{camera}.translate", 0, 0, 0)
            maya_cmds.setAttr(f"{camera}.rotate", 0, 0, 0)

        for label, change in (
            ("negative_inside", inside),
            (
                "positive_inside",
                lambda: maya_cmds.setAttr(f"{parent}.scaleX", 1),
            ),
            (
                "negative_inside_restored",
                lambda: maya_cmds.setAttr(f"{parent}.scaleX", -1),
            ),
        ):
            pixels = _take(panel, tmp_path, label, change)
            assert all(
                pixels[index : index + 4] == background
                for index in range(0, len(pixels), 4)
            ), "立体内部へ裏面のFillまたは線が描画された"

        def outside_again():
            maya_cmds.setAttr(f"{camera_shape}.orthographic", True)
            maya_cmds.setAttr(f"{camera}.translate", 3, 2, 4)
            maya_cmds.setAttr(f"{camera}.rotate", *saved_rotation)

        assert (
            _take(panel, tmp_path, "outside_restored", outside_again)
            == outside
        )


@pytest.mark.parametrize("preset", ("Cube", "ColorCornerCube"))
@pytest.mark.parametrize("target", ("parent", "matrix"))
@pytest.mark.parametrize("cached", (False, True))
def test_fill_connected_motion_during_actual_playback(
    maya_cmds, new_scene, tmp_path, preset, target, cached
):
    """親と接続行列の2姿勢を、Cached PlaybackのON/OFFで実再生する。"""
    _require_gui(maya_cmds)
    from maya import utils
    from maya.api import OpenMaya as om, OpenMayaUI as omui
    from maya.plugin.evaluator.CacheEvaluatorManager import (
        CACHE_STANDARD_MODE_EVAL,
    )

    from bd_util.ui.qt import QtWidgets

    maya_cmds.loadPlugin("cacheEvaluator", quiet=True)
    previous_cache = _cache_enabled(
        maya_cmds.evaluator(query=True, name="cache", enable=True)
    )
    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    previous_time = maya_cmds.currentTime(query=True)
    flags = (
        "minTime",
        "maxTime",
        "animationStartTime",
        "animationEndTime",
        "loop",
        "playbackSpeed",
        "maxPlaybackSpeed",
        "view",
        "by",
    )
    previous = {
        flag: maya_cmds.playbackOptions(query=True, **{flag: True})
        for flag in flags
    }
    try:
        maya_cmds.evaluationManager(mode="parallel")
        maya_cmds.evaluator(name="cache", enable=False)
        with _fill_view(maya_cmds, preset) as values:
            transform, shape, _, _, panel = values
            if target == "matrix":
                driver = maya_cmds.createNode("composeMatrix")
                maya_cmds.connectAttr(
                    f"{driver}.outputMatrix",
                    f"{shape}.shapeTransformMatrix",
                )
                attributes = ("inputTranslateX", "inputRotateY", "inputScaleX")
            else:
                driver = maya_cmds.group(transform)
                attributes = ("translateX", "rotateY", "scaleX")
            for frame, pose in (
                (1, (-0.15, 0, 1)),
                (7, (0.15, 35, -1)),
                (13, (-0.15, 0, 1)),
                (19, (0.15, 35, -1)),
                (24, (0.15, 35, -1)),
            ):
                for attribute, value in zip(attributes, pose):
                    maya_cmds.setKeyframe(
                        driver, attribute=attribute, time=frame, value=value
                    )
            for attribute in attributes:
                maya_cmds.keyTangent(
                    driver, attribute=attribute, outTangentType="step"
                )
                assert set(
                    maya_cmds.keyTangent(
                        driver,
                        attribute=attribute,
                        query=True,
                        outTangentType=True,
                    )
                ) == {"step"}
            maya_cmds.currentTime(1)
            first = _warm(maya_cmds, values, tmp_path)
            second = _take(
                panel, tmp_path, "second", lambda: maya_cmds.currentTime(7)
            )
            assert first != second
            assert (
                _take(
                    panel,
                    tmp_path,
                    "scrub_first",
                    lambda: maya_cmds.currentTime(1),
                )
                == first
            )
            if cached:
                maya_cmds.cacheEvaluator(resetRules=True)
                for rule in CACHE_STANDARD_MODE_EVAL:
                    maya_cmds.cacheEvaluator(**rule)
                maya_cmds.cacheEvaluator(cacheFillMode="syncOnly")
                maya_cmds.evaluator(name="cache", enable=True)
            assert (
                _cache_enabled(
                    maya_cmds.evaluator(query=True, name="cache", enable=True)
                )
                == cached
            )
            maya_cmds.playbackOptions(
                minTime=1,
                maxTime=24,
                animationStartTime=1,
                animationEndTime=24,
                loop="once",
                playbackSpeed=0,
                maxPlaybackSpeed=0,
                view="all",
                by=1,
            )
            for ordinal in range(2):
                maya_cmds.currentTime(1)
                images, errors = [], []

                def posted(*_):
                    if not maya_cmds.play(query=True, state=True):
                        return
                    try:
                        images.append(
                            _read_frame(
                                panel,
                                tmp_path / f"play_{ordinal}_{len(images)}.png",
                            )
                        )
                    except BaseException as error:
                        errors.append(error)

                callback = omui.MUiMessage.add3dViewPostRenderMsgCallback(
                    panel, posted
                )
                try:
                    maya_cmds.play(forward=True, wait=False)
                    deadline = time.monotonic() + 60
                    application = QtWidgets.QApplication.instance()
                    assert application is not None
                    while (
                        maya_cmds.play(query=True, state=True)
                        and time.monotonic() < deadline
                    ):
                        application.processEvents()
                        utils.processIdleEvents()
                    assert not maya_cmds.play(
                        query=True, state=True
                    ), "実再生が終了しない"
                finally:
                    maya_cmds.play(state=False)
                    om.MMessage.removeCallback(callback)
                assert not errors, errors
                assert (
                    len(images) >= 2 and first in images and second in images
                )
                assert all(image in (first, second) for image in images)
                assert maya_cmds.currentTime(query=True) == 24
            assert (
                _take(
                    panel,
                    tmp_path,
                    "stopped_first",
                    lambda: maya_cmds.currentTime(1),
                )
                == first
            )
            assert (
                _take(
                    panel,
                    tmp_path,
                    "stopped_second",
                    lambda: maya_cmds.currentTime(7),
                )
                == second
            )
    finally:
        maya_cmds.play(state=False)
        maya_cmds.playbackOptions(**previous)
        maya_cmds.evaluator(name="cache", enable=previous_cache)
        maya_cmds.evaluationManager(mode=previous_mode)
        maya_cmds.currentTime(previous_time)
