"""保持した線の描画が移動・選択・再生とViewport固有の表示へ追従することを確認する。"""

import time
from ctypes import string_at

import pytest

from controller_shape_cases import SHAPE_NAMES, set_preset
from test_controller_shape_viewport import (
    _aim_at_origin,
    _capture_normal_update,
    _drawing_view,
)

pytestmark = pytest.mark.maya


def _assert_visible(pixels):
    """背景だけの画像を比較元として使わない。"""
    background = pixels[:4]
    assert any(
        pixels[index : index + 4] != background
        for index in range(0, len(pixels), 4)
    ), "比較元のシェイプが描画されていない"


@pytest.mark.parametrize("preset", SHAPE_NAMES)
def test_wire_child_and_parent_motion_restore(
    maya_cmds, new_scene, tmp_path, preset
):
    """暖機済みの各シェイプも、子と親の移動後に元の表示へ戻る。"""
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds,
        preset,
        fixed_viewport=True,
        shapeFill=False,
        shapeDrawOnTop=False,
        shapeLineWidth=1.0,
        shapeLineTransparency=0.0,
    ) as (transform, _, camera, _, panel):
        parent = maya_cmds.group(transform, name="wireShapeParent")
        _aim_at_origin(maya_cmds, camera, (3, 2, 4))
        maya_cmds.select(clear=True)
        maya_cmds.modelEditor(panel, edit=True, selectionHiliteDisplay=True)

        def take(name, change):
            return _capture_normal_update(
                panel, tmp_path / f"{name}.png", change
            )

        take(
            "warmup", lambda: maya_cmds.setAttr(f"{camera}.translateX", 3.031)
        )
        initial = take(
            "initial", lambda: maya_cmds.setAttr(f"{camera}.translateX", 3)
        )
        _assert_visible(initial)
        assert (
            take("unchanged", lambda: maya_cmds.refresh(force=True)) == initial
        )
        for label, target, distance in (
            ("child", transform, 0.2),
            ("parent", parent, -0.2),
        ):
            moved = take(
                f"{label}_moved",
                lambda: maya_cmds.setAttr(f"{target}.translateX", distance),
            )
            assert len(moved) == len(initial), "Viewport寸法が変わった"
            _assert_visible(moved)
            assert moved != initial, "移動してもシェイプが元の位置に残っている"
            restored = take(
                f"{label}_restored",
                lambda: maya_cmds.setAttr(f"{target}.translateX", 0),
            )
            assert (
                restored == initial
            ), "移動を戻してもシェイプの表示が復元しない"
            assert (
                take(
                    f"{label}_stopped",
                    lambda: maya_cmds.refresh(force=True),
                )
                == initial
            )


@pytest.mark.parametrize("preset", SHAPE_NAMES)
def test_wire_selection_color_restores(maya_cmds, new_scene, tmp_path, preset):
    """暖機済みの各シェイプも選択色へ切り替わり、解除すると元の色へ戻る。"""
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds,
        preset,
        fixed_viewport=True,
        shapeFill=False,
        shapeDrawOnTop=False,
        shapeLineWidth=1.0,
        shapeLineTransparency=0.0,
    ) as (transform, shape, camera, _, panel):
        _aim_at_origin(maya_cmds, camera, (3, 2, 4))
        maya_cmds.select(clear=True)
        maya_cmds.setAttr(f"{shape}.overrideEnabled", False)
        maya_cmds.setAttr(f"{shape}.overrideRGBColors", False)
        maya_cmds.modelEditor(panel, edit=True, selectionHiliteDisplay=True)

        def take(name, change):
            return _capture_normal_update(
                panel, tmp_path / f"{name}.png", change
            )

        take(
            "color_warmup",
            lambda: maya_cmds.setAttr(f"{camera}.translateX", 3.031),
        )
        dormant = take(
            "color_dormant",
            lambda: maya_cmds.setAttr(f"{camera}.translateX", 3),
        )
        _assert_visible(dormant)
        assert (
            take("color_unchanged", lambda: maya_cmds.refresh(force=True))
            == dormant
        )
        selected = take(
            "color_selected", lambda: maya_cmds.select(transform, replace=True)
        )
        assert len(selected) == len(dormant), "Viewport寸法が変わった"
        _assert_visible(selected)
        assert selected != dormant, "選択してもシェイプの色が変わらない"
        assert (
            take("color_deselected", lambda: maya_cmds.select(clear=True))
            == dormant
        )


@pytest.mark.parametrize(
    "preset", ("Cube", "Circle", "Sphere", "ColorCube", "ColorCornerCube")
)
def test_wire_connected_animation_matrix_updates_during_playback(
    maya_cmds, new_scene, tmp_path, preset
):
    """接続された行列の2姿勢を実再生中も描画し、停止後も元の姿勢へ戻せる。"""
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    from maya import utils
    from maya.api import OpenMaya as om, OpenMayaUI as omui

    from bd_util.ui.qt import QtWidgets

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
    previous_playback = {
        flag: maya_cmds.playbackOptions(query=True, **{flag: True})
        for flag in flags
    }
    try:
        maya_cmds.evaluationManager(mode="parallel")
        with _drawing_view(
            maya_cmds,
            preset,
            fixed_viewport=True,
            shapeFill=False,
            shapeDrawOnTop=False,
            shapeLineWidth=1.0,
            shapeLineTransparency=0.0,
        ) as (_, shape, camera, _, panel):
            _aim_at_origin(maya_cmds, camera, (3, 2, 4))
            maya_cmds.select(clear=True)
            maya_cmds.modelEditor(
                panel, edit=True, selectionHiliteDisplay=True, activeView=True
            )
            maya_cmds.setFocus(panel)
            driver = maya_cmds.createNode("composeMatrix")
            maya_cmds.connectAttr(
                f"{driver}.outputMatrix",
                f"{shape}.shapeTransformMatrix",
            )
            for frame, value in (
                (1, -0.15),
                (7, 0.15),
                (13, -0.15),
                (19, 0.15),
                (24, 0.15),
            ):
                maya_cmds.setKeyframe(
                    driver,
                    attribute="inputTranslateX",
                    time=frame,
                    value=value,
                )
            maya_cmds.keyTangent(
                driver,
                attribute="inputTranslateX",
                inTangentType="step",
                outTangentType="step",
            )
            maya_cmds.currentTime(1)

            def take(name, change):
                return _capture_normal_update(
                    panel, tmp_path / f"{name}.png", change
                )

            take(
                "matrix_warmup",
                lambda: maya_cmds.setAttr(f"{camera}.translateX", 3.031),
            )
            first = take(
                "matrix_first",
                lambda: maya_cmds.setAttr(f"{camera}.translateX", 3),
            )
            second = take("matrix_second", lambda: maya_cmds.currentTime(7))
            _assert_visible(first)
            _assert_visible(second)
            assert first != second, "接続行列の2姿勢を画像で区別できない"
            assert (
                take("matrix_scrub_first", lambda: maya_cmds.currentTime(1))
                == first
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
            images, errors = [], []

            def rendered(*_):
                try:
                    if not maya_cmds.play(query=True, state=True):
                        return
                    image = om.MImage()
                    omui.M3dView.getM3dViewFromModelPanel(
                        panel
                    ).readColorBuffer(image, True)
                    width, height = image.getSize()
                    images.append(
                        string_at(int(image.pixels()), width * height * 4)
                    )
                    image.writeToFile(
                        str(tmp_path / f"matrix_play_{len(images)}.png"), "png"
                    )
                except BaseException as error:
                    errors.append(error)

            callback = omui.MUiMessage.add3dViewPostRenderMsgCallback(
                panel, rendered
            )
            try:
                application = QtWidgets.QApplication.instance()
                assert application is not None
                maya_cmds.play(forward=True, wait=False)
                deadline = time.monotonic() + 30
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
            if errors:
                raise errors[0]
            assert (
                len(images) >= 2
            ), "実再生中のViewport画像を十分に取得していない"
            assert all(
                image in (first, second) for image in images
            ), "実再生中に参照と異なる姿勢が描画された"
            assert (
                first in images and second in images
            ), "実再生中に両方の行列姿勢が出現しない"
            assert maya_cmds.currentTime(query=True) == 24
            assert (
                take("matrix_stopped_first", lambda: maya_cmds.currentTime(1))
                == first
            )
            assert (
                take("matrix_stopped_second", lambda: maya_cmds.currentTime(7))
                == second
            )
            assert (
                take("matrix_restored_first", lambda: maya_cmds.currentTime(1))
                == first
            )
    finally:
        maya_cmds.play(state=False)
        maya_cmds.playbackOptions(**previous_playback)
        maya_cmds.evaluationManager(mode=previous_mode)
        maya_cmds.currentTime(previous_time)


@pytest.mark.parametrize(
    "preset", ("Cube", "Sphere", "ColorCube", "ColorCornerCube")
)
def test_wire_plugin_filter_is_independent_between_visible_views(
    maya_cmds, new_scene, tmp_path, preset
):
    """片方のPluginShapesを隠しても、対向Viewportの表示を変えない。"""
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    from maya import utils
    from maya.api import OpenMayaUI as omui

    from bd_util.ui.qt import QtWidgets, wrapInstance

    with _drawing_view(
        maya_cmds,
        preset,
        fixed_viewport=True,
        shapeFill=False,
        shapeDrawOnTop=False,
        shapeLineWidth=1.0,
        shapeLineTransparency=0.0,
    ) as (_, _, camera, _, panel):
        maya_cmds.modelEditor(panel, edit=True, selectionHiliteDisplay=True)
        second_window = maya_cmds.window(widthHeight=(480, 480))
        try:
            maya_cmds.paneLayout()
            second_camera = maya_cmds.duplicate(camera)[0]
            _aim_at_origin(maya_cmds, second_camera, (3, 2, 4))
            second_panel = maya_cmds.modelPanel(
                camera=second_camera, menuBarVisible=False
            )
            maya_cmds.modelEditor(
                second_panel,
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
            maya_cmds.select(clear=True)
            maya_cmds.showWindow(second_window)
            utils.processIdleEvents()
            ports = {}
            for index, target in enumerate((panel, second_panel)):
                view = omui.M3dView.getM3dViewFromModelPanel(target)
                widget = wrapInstance(int(view.widget()), QtWidgets.QWidget)
                assert widget.width() > 0 and widget.height() > 0
                widget.setFixedSize(widget.size())
                widget.window().move(40 + index * 510, 140)
                ports[target] = widget

            def take(target, name, change):
                widget = ports[target]
                widget.window().raise_()
                widget.window().activateWindow()
                maya_cmds.setFocus(target)
                maya_cmds.modelEditor(target, edit=True, activeView=True)
                pixels = _capture_normal_update(
                    target, tmp_path / f"{name}.png", change
                )
                assert all(
                    port.isVisible() and port.window().isVisible()
                    for port in ports.values()
                ), "比較中に片方のViewportが閉じている"
                return pixels

            references = {}
            for label, target, view_camera, origin in (
                ("a", panel, camera, 0.0),
                ("b", second_panel, second_camera, 3.0),
            ):
                shifted = take(
                    target,
                    f"{label}_pan_reference",
                    lambda: maya_cmds.setAttr(
                        f"{view_camera}.translateX", origin + 0.03
                    ),
                )
                initial = take(
                    target,
                    f"{label}_initial",
                    lambda: maya_cmds.setAttr(
                        f"{view_camera}.translateX", origin
                    ),
                )
                _assert_visible(initial)
                _assert_visible(shifted)
                assert shifted != initial, "カメラ移動を区別できないfixture"
                references[target] = (initial, shifted)

            for cycle, (
                hidden,
                shown,
                hidden_camera,
                shown_camera,
                hx,
                sx,
            ) in enumerate(
                (
                    (second_panel, panel, second_camera, camera, 3.0, 0.0),
                    (panel, second_panel, camera, second_camera, 0.0, 3.0),
                )
            ):
                blank = take(
                    hidden,
                    f"{cycle}_hidden",
                    lambda: maya_cmds.modelEditor(
                        hidden, edit=True, pluginShapes=False
                    ),
                )
                background = references[hidden][0][:4]
                assert all(
                    blank[index : index + 4] == background
                    for index in range(0, len(blank), 4)
                ), "PluginShapes OFFでもシェイプが残っている"
                assert (
                    take(
                        shown,
                        f"{cycle}_other_visible",
                        lambda: maya_cmds.setAttr(
                            f"{shown_camera}.translateX", sx + 0.03
                        ),
                    )
                    == references[shown][1]
                )
                assert (
                    take(
                        hidden,
                        f"{cycle}_still_hidden",
                        lambda: maya_cmds.setAttr(
                            f"{hidden_camera}.translateX", hx + 0.03
                        ),
                    )
                    == blank
                ), "対向Viewportの再描画で非表示のシェイプが戻っている"
                assert (
                    take(
                        shown,
                        f"{cycle}_other_restored",
                        lambda: maya_cmds.setAttr(
                            f"{shown_camera}.translateX", sx
                        ),
                    )
                    == references[shown][0]
                )
                assert (
                    take(
                        hidden,
                        f"{cycle}_filter_restored",
                        lambda: maya_cmds.modelEditor(
                            hidden, edit=True, pluginShapes=True
                        ),
                    )
                    == references[hidden][1]
                )
                assert (
                    take(
                        hidden,
                        f"{cycle}_camera_restored",
                        lambda: maya_cmds.setAttr(
                            f"{hidden_camera}.translateX", hx
                        ),
                    )
                    == references[hidden][0]
                )
        finally:
            maya_cmds.deleteUI(second_window)


def test_wire_shape_switch_restores(maya_cmds, new_scene, tmp_path):
    """頂点数と色分けが異なる形状へ切り替えても、前の形状を残さない。"""
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    references = {}
    for preset in ("Line", "Sphere", "ColorCornerCube"):
        with _drawing_view(
            maya_cmds,
            preset,
            fixed_viewport=True,
            shapeFill=False,
            shapeDrawOnTop=False,
            shapeLineWidth=1.0,
            shapeLineTransparency=0.0,
        ) as (transform, _, camera, _, panel):
            _aim_at_origin(maya_cmds, camera, (3, 2, 4))
            maya_cmds.select(clear=True)
            maya_cmds.modelEditor(
                panel, edit=True, selectionHiliteDisplay=True
            )
            _capture_normal_update(
                panel,
                tmp_path / f"reference_{preset}_warmup.png",
                lambda: maya_cmds.setAttr(f"{camera}.translateX", 3.031),
            )
            references[preset] = _capture_normal_update(
                panel,
                tmp_path / f"reference_{preset}.png",
                lambda: maya_cmds.setAttr(f"{camera}.translateX", 3),
            )
            _assert_visible(references[preset])
        maya_cmds.delete(transform, camera)
    assert (
        len(set(references.values())) == 3
    ), "形状の違いを区別できないfixture"

    with _drawing_view(
        maya_cmds,
        "Line",
        fixed_viewport=True,
        shapeFill=False,
        shapeDrawOnTop=False,
        shapeLineWidth=1.0,
        shapeLineTransparency=0.0,
    ) as (_, shape, camera, _, panel):
        _aim_at_origin(maya_cmds, camera, (3, 2, 4))
        maya_cmds.select(clear=True)
        maya_cmds.modelEditor(panel, edit=True, selectionHiliteDisplay=True)
        _capture_normal_update(
            panel,
            tmp_path / "switch_warmup.png",
            lambda: maya_cmds.setAttr(f"{camera}.translateX", 3.031),
        )
        assert (
            _capture_normal_update(
                panel,
                tmp_path / "switch_Line_initial.png",
                lambda: maya_cmds.setAttr(f"{camera}.translateX", 3),
            )
            == references["Line"]
        )
        for index, preset in enumerate(("Sphere", "ColorCornerCube", "Line")):
            actual = _capture_normal_update(
                panel,
                tmp_path / f"switch_{index}_{preset}.png",
                lambda: set_preset(maya_cmds, shape, preset),
            )
            assert actual == references[preset], (
                "新規作成した参照と一致しない。切替前の描画が残っている可能性がある",
                preset,
            )


@pytest.mark.parametrize(
    "attribute,value",
    (
        ("shapeFill", True),
        ("shapeLineWidth", 4.0),
        ("shapeLineTransparency", 0.5),
        ("shapeDrawOnTop", True),
        ("shapeTemplateLine", True),
    ),
)
def test_wire_fallback_roundtrip_restores(
    maya_cmds, new_scene, tmp_path, attribute, value
):
    """表示設定を繰り返し切り替えても、通常線へ正確に戻る。"""
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    with _drawing_view(
        maya_cmds,
        "Cube",
        fixed_viewport=True,
        shapeFill=False,
        shapeDrawOnTop=False,
        shapeLineWidth=1.0,
        shapeLineTransparency=0.0,
    ) as (_, shape, camera, _, panel):
        maya_cmds.modelEditor(panel, edit=True, selectionHiliteDisplay=True)
        if attribute == "shapeTemplateLine":
            maya_cmds.setAttr(f"{shape}.shapeTemplateLineRate", 1.0)
        target = f"{shape}.{attribute}"
        original = maya_cmds.getAttr(target)

        def take(name, change):
            return _capture_normal_update(
                panel, tmp_path / f"{name}.png", change
            )

        take(
            "fallback_warmup",
            lambda: maya_cmds.setAttr(f"{camera}.translateX", 0.031),
        )
        initial = take(
            "fallback_initial",
            lambda: maya_cmds.setAttr(f"{camera}.translateX", 0),
        )
        _assert_visible(initial)
        if attribute == "shapeDrawOnTop":

            def add_occluder():
                plane = maya_cmds.polyPlane(
                    width=1.25,
                    height=1.25,
                    axis=(0, 0, 1),
                    constructionHistory=False,
                )[0]
                maya_cmds.setAttr(f"{plane}.translateX", 0.4)
                maya_cmds.setAttr(f"{plane}.translateZ", 0.75)
                maya_cmds.select(clear=True)

            occluded = take("fallback_occluded", add_occluder)
            assert occluded != initial, "遮蔽物が比較画像へ反映されていない"
            initial = occluded
        changed = None
        for cycle in range(2):
            actual = take(
                f"fallback_changed_{cycle}",
                lambda: maya_cmds.setAttr(target, value),
            )
            assert len(actual) == len(initial), "Viewport寸法が変わった"
            _assert_visible(actual)
            assert actual != initial, "切替前後の見た目を区別できない"
            if changed is not None:
                assert actual == changed, "同じ設定へ戻しても描画が一致しない"
            changed = actual
            assert (
                take(
                    f"fallback_restored_{cycle}",
                    lambda: maya_cmds.setAttr(target, original),
                )
                == initial
            ), "通常線へ戻しても表示が復元しない"
