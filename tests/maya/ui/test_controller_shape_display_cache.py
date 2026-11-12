"""保持済み表示データの直接編集・接続・時刻変更を実Viewportで確認する。"""

from contextlib import contextmanager
from ctypes import string_at
import time

import pytest

from test_controller_shape_viewport import (
    _capture_normal_update,
    _drawing_view,
)

pytestmark = pytest.mark.maya

DISPLAY_VALUES = (
    ("shapeLineWidth", 1.0, 6.0, 2.5),
    ("shapeLineTransparency", 0.0, 0.75, 0.35),
    ("shapeFillTransparency", 0.85, 0.15, 0.5),
    ("shapeDrawOnTop", False, True, False),
)


def _enabled(value):
    if isinstance(value, (list, tuple)):
        value = value[0] if value else False
    return (
        value.lower() in ("1", "true")
        if isinstance(value, str)
        else bool(value)
    )


@contextmanager
def _display_scene(cmds, path, attribute, first, second):
    """2値の見た目が異なるfixtureを暖機し、通常更新だけで比較する。"""
    if cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    from maya.api import OpenMayaUI as omui

    from bd_util.ui.qt import QtWidgets, wrapInstance

    previous_undo = cmds.undoInfo(query=True, state=True)
    has_cache = "cache" in (cmds.evaluator(query=True) or [])
    previous_cache = (
        _enabled(cmds.evaluator(query=True, name="cache", enable=True))
        if has_cache
        else False
    )
    cmds.undoInfo(state=True)
    if has_cache:
        cmds.evaluator(name="cache", enable=False)
    try:
        with _drawing_view(
            cmds, "Cube", shapeFill=attribute == "shapeFillTransparency"
        ) as (transform, shape, camera, _, panel):
            view = omui.M3dView.getM3dViewFromModelPanel(panel)
            widget = wrapInstance(int(view.widget()), QtWidgets.QWidget)
            widget.setFixedSize(widget.size())
            cmds.setFocus(panel)
            cmds.modelEditor(panel, edit=True, activeView=True)
            target = f"{shape}.{attribute}"
            cmds.setAttr(target, first)
            if attribute == "shapeFillTransparency":
                cmds.setAttr(f"{shape}.shapeLineTransparency", 1.0)
            if attribute == "shapeDrawOnTop":
                plane = cmds.polyPlane(
                    width=1.25,
                    height=1.25,
                    axis=(0, 0, 1),
                    constructionHistory=False,
                )[0]
                cmds.setAttr(f"{plane}.translateZ", 0.75)
                cmds.select(clear=True)

            def take(label, change):
                recording = cmds.undoInfo(query=True, state=True)

                def change_then_suspend_recording():
                    change()
                    # UIの遅延処理がUndo/Redo履歴へ入るのを、画像待機中だけ防ぐ。
                    cmds.undoInfo(stateWithoutFlush=False)

                try:
                    return _capture_normal_update(
                        panel,
                        path / f"{label}.png",
                        change_then_suspend_recording,
                    )
                finally:
                    cmds.undoInfo(stateWithoutFlush=recording)

            take.panel = panel

            take("warmup", lambda: cmds.setAttr(f"{camera}.translateX", 0.031))
            a = take(
                "reference_first",
                lambda: cmds.setAttr(f"{camera}.translateX", 0.0),
            )
            b = take("reference_second", lambda: cmds.setAttr(target, second))
            assert len(a) == len(b), "参照画像のViewport寸法が変わった"
            assert a != b, "表示属性の2値を区別できないfixture"
            assert take("warm_first", lambda: cmds.setAttr(target, first)) == a
            cmds.flushUndo()
            yield transform, shape, target, take, a, b
    finally:
        if has_cache:
            cmds.evaluator(name="cache", enable=previous_cache)
        cmds.undoInfo(state=previous_undo)


@pytest.mark.parametrize("attribute,first,second,middle", DISPLAY_VALUES)
def test_display_cache_direct_undo_redo_and_default_reset(
    maya_cmds, new_scene, tmp_path, attribute, first, second, middle
):
    """暖機済みの表示も直接編集・Undo/Redo・既定値への復帰に追従する。"""
    with _display_scene(maya_cmds, tmp_path, attribute, first, second) as (
        _,
        shape,
        target,
        take,
        a,
        b,
    ):
        assert (
            take("direct_second", lambda: maya_cmds.setAttr(target, second))
            == b
        )
        assert take("undo_first", maya_cmds.undo) == a
        assert take("redo_second", maya_cmds.redo) == b
        default = maya_cmds.attributeQuery(
            attribute, node=shape, listDefault=True
        )[0]
        assert (
            take("reset_default", lambda: maya_cmds.setAttr(target, default))
            == a
        )


@pytest.mark.parametrize("attribute,first,second,middle", DISPLAY_VALUES)
def test_display_cache_connection_edit_disconnect_and_undo(
    maya_cmds, new_scene, tmp_path, attribute, first, second, middle
):
    """接続済みの値と切断後の直接値を、接続Undo/Redoも含めて描画する。"""
    with _display_scene(maya_cmds, tmp_path, attribute, first, second) as (
        _,
        _,
        target,
        take,
        a,
        b,
    ):
        driver = maya_cmds.createNode("network")
        maya_cmds.addAttr(
            driver,
            longName="displayValue",
            attributeType="bool" if isinstance(first, bool) else "double",
            keyable=True,
        )
        source = f"{driver}.displayValue"
        maya_cmds.setAttr(source, second)
        assert (
            take(
                "connect_second", lambda: maya_cmds.connectAttr(source, target)
            )
            == b
        )
        assert (
            take("upstream_first", lambda: maya_cmds.setAttr(source, first))
            == a
        )

        def detach_to_second():
            maya_cmds.undoInfo(openChunk=True)
            try:
                maya_cmds.disconnectAttr(source, target)
                maya_cmds.setAttr(target, second)
            finally:
                maya_cmds.undoInfo(closeChunk=True)

        assert take("disconnect_second", detach_to_second) == b
        assert take("undo_reconnect_first", maya_cmds.undo) == a
        assert maya_cmds.isConnected(source, target)
        assert take("redo_disconnect_second", maya_cmds.redo) == b
        assert not maya_cmds.isConnected(source, target)
        assert (
            take("detached_first", lambda: maya_cmds.setAttr(target, first))
            == a
        )


@pytest.mark.parametrize("attribute,first,second,middle", DISPLAY_VALUES)
def test_display_cache_save_open_and_duplicate_first_draw(
    maya_cmds, new_scene, tmp_path, attribute, first, second, middle
):
    """通常保存した非既定値を、再読込・複製後の最初の描画から使う。"""
    from maya.api import OpenMayaUI as omui

    from bd_util.ui.qt import QtWidgets, wrapInstance

    with _display_scene(maya_cmds, tmp_path, attribute, first, second) as (
        transform,
        shape,
        target,
        take,
        _,
        b,
    ):
        assert (
            take("before_save", lambda: maya_cmds.setAttr(target, second)) == b
        )
        assert maya_cmds.attributeQuery(attribute, node=shape, storable=True)
        camera = maya_cmds.modelPanel(take.panel, query=True, camera=True)
        view = omui.M3dView.getM3dViewFromModelPanel(take.panel)
        window = wrapInstance(int(view.widget()), QtWidgets.QWidget).window()
        scene_path = tmp_path / "display_storage.ma"
        maya_cmds.file(rename=str(scene_path))
        maya_cmds.file(save=True, type="mayaAscii", force=True)

        def show_target():
            window.show()
            window.raise_()
            window.activateWindow()
            maya_cmds.setFocus(take.panel)
            maya_cmds.modelEditor(take.panel, edit=True, activeView=True)

        try:
            # 読込中の過渡的な画像を除き、新しいshapeを表示する最初の描画を採る。
            window.hide()
            maya_cmds.file(str(scene_path), open=True, force=True)
            maya_cmds.lookThru(take.panel, camera)
            maya_cmds.select(clear=True)
            assert take("reopened_first_draw", show_target) == b
            assert maya_cmds.getAttr(target) == pytest.approx(second)

            window.hide()
            duplicate = maya_cmds.duplicate(transform, returnRootsOnly=True)[0]
            duplicate_shape = maya_cmds.listRelatives(
                duplicate, shapes=True, fullPath=True
            )[0]
            maya_cmds.delete(transform)
            maya_cmds.select(clear=True)
            assert take("duplicate_first_draw", show_target) == b
            assert maya_cmds.getAttr(
                f"{duplicate_shape}.{attribute}"
            ) == pytest.approx(second)
        finally:
            window.show()


@pytest.mark.parametrize("attribute,first,second,middle", DISPLAY_VALUES)
@pytest.mark.parametrize("evaluation_mode", ("off", "parallel"))
def test_display_cache_connected_animation_matches_direct_scrub_reference(
    maya_cmds,
    new_scene,
    tmp_path,
    attribute,
    first,
    second,
    middle,
    evaluation_mode,
):
    """接続元のキーを往復スクラブしても、直接設定した同じ値の画像と一致する。"""
    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    previous_time = maya_cmds.currentTime(query=True)
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        with _display_scene(maya_cmds, tmp_path, attribute, first, second) as (
            _,
            _,
            target,
            take,
            a,
            b,
        ):
            c = a
            if middle != first:
                c = take(
                    "reference_middle",
                    lambda: maya_cmds.setAttr(target, middle),
                )
                take(
                    "before_connect_first",
                    lambda: maya_cmds.setAttr(target, first),
                )
            driver = maya_cmds.createNode("network")
            maya_cmds.addAttr(
                driver,
                longName="displayValue",
                attributeType="bool" if isinstance(first, bool) else "double",
                keyable=True,
            )
            for frame, value in ((1, first), (2, second), (3, middle)):
                maya_cmds.setKeyframe(
                    driver, attribute="displayValue", time=frame, value=value
                )
            maya_cmds.keyTangent(
                driver, attribute="displayValue", outTangentType="step"
            )
            maya_cmds.currentTime(1)
            maya_cmds.connectAttr(f"{driver}.displayValue", target)
            references = {1: a, 2: b, 3: c}
            for ordinal, frame in enumerate((2, 3, 1, 3, 2, 1)):
                assert (
                    take(
                        f"scrub_{ordinal}_{frame}",
                        lambda frame=frame: maya_cmds.currentTime(frame),
                    )
                    == references[frame]
                )
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)
        maya_cmds.currentTime(previous_time)


@pytest.mark.parametrize("attribute,first,second,middle", DISPLAY_VALUES)
def test_display_cache_unconnected_direct_set_during_real_playback(
    maya_cmds, new_scene, tmp_path, attribute, first, second, middle
):
    """実再生中の直接設定も、通常時の2値の画像へ追従する。"""
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    from maya import utils
    from maya.api import OpenMaya as om, OpenMayaUI as omui

    from bd_util.ui.qt import QtWidgets

    previous_time = maya_cmds.currentTime(query=True)
    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
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
        with _display_scene(maya_cmds, tmp_path, attribute, first, second) as (
            _,
            shape,
            target,
            take,
            a,
            b,
        ):
            assert not maya_cmds.listConnections(
                target, source=True, destination=False
            )
            driver = maya_cmds.createNode("transform")
            maya_cmds.setKeyframe(
                driver, attribute="translateX", time=1, value=0
            )
            maya_cmds.setKeyframe(
                driver, attribute="translateX", time=9, value=0.1
            )
            maya_cmds.playbackOptions(
                minTime=1,
                maxTime=9,
                animationStartTime=1,
                animationEndTime=9,
                loop="once",
                playbackSpeed=0,
                maxPlaybackSpeed=0,
                view="all",
                by=1,
            )
            maya_cmds.currentTime(1)
            panel = take.panel
            maya_cmds.setFocus(panel)
            maya_cmds.modelEditor(panel, edit=True, activeView=True)
            requested = []
            images = []

            def change_display(*_):
                if maya_cmds.play(query=True, state=True):
                    value = second if len(requested) % 2 == 0 else first
                    maya_cmds.setAttr(target, value)
                    requested.append(value)

            def rendered(*_):
                image = om.MImage()
                omui.M3dView.getM3dViewFromModelPanel(panel).readColorBuffer(
                    image, True
                )
                width, height = image.getSize()
                pixels = string_at(int(image.pixels()), width * height * 4)
                playing = bool(maya_cmds.play(query=True, state=True))
                if playing:
                    images.append(pixels)
                    image.writeToFile(
                        str(tmp_path / f"real_play_{len(images)}.png"), "png"
                    )

            time_callback = om.MEventMessage.addEventCallback(
                "timeChanged", change_display
            )
            post_callback = omui.MUiMessage.add3dViewPostRenderMsgCallback(
                panel, rendered
            )
            try:
                maya_cmds.play(forward=True, wait=False)
                deadline = time.monotonic() + 30
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
                om.MMessage.removeCallback(time_callback)
                om.MMessage.removeCallback(post_callback)
            assert (
                len(requested) >= 2
            ), "実再生中の直接設定を十分に通過していない"
            assert (
                len(images) >= 2
            ), "実再生中のViewport画像を十分に取得していない"
            assert all(image in (a, b) for image in images)
            assert (
                a in images and b in images
            ), "直接設定した表示が再生中に古い値へ固定されている"
    finally:
        maya_cmds.play(state=False)
        maya_cmds.playbackOptions(**previous_playback)
        maya_cmds.evaluationManager(mode=previous_mode)
        maya_cmds.currentTime(previous_time)


def test_display_cache_hidden_playback_direct_set_is_visible_after_stop(
    maya_cmds, new_scene, tmp_path
):
    """再生中ずっと非表示でも、停止後に表示した最初の画像は最後の値を使う。"""
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    from maya import utils
    from maya.api import OpenMaya as om

    from bd_util.ui.qt import QtWidgets

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
        with _display_scene(
            maya_cmds, tmp_path, "shapeLineWidth", 1.0, 6.0
        ) as (transform, _, target, take, _, wide):
            take(
                "hidden_before_play",
                lambda: maya_cmds.setAttr(f"{transform}.visibility", False),
            )
            maya_cmds.playbackOptions(
                minTime=1,
                maxTime=9,
                animationStartTime=1,
                animationEndTime=9,
                loop="once",
                playbackSpeed=0,
                maxPlaybackSpeed=0,
                view="all",
                by=1,
            )
            maya_cmds.currentTime(1)
            requested = []

            def change_hidden_display(*_):
                if maya_cmds.play(query=True, state=True):
                    maya_cmds.setAttr(target, 6.0)
                    requested.append(6.0)

            callback = om.MEventMessage.addEventCallback(
                "timeChanged", change_hidden_display
            )
            try:
                maya_cmds.play(forward=True, wait=False)
                deadline = time.monotonic() + 30
                application = QtWidgets.QApplication.instance()
                assert application is not None
                while (
                    maya_cmds.play(query=True, state=True)
                    and time.monotonic() < deadline
                ):
                    application.processEvents()
                    utils.processIdleEvents()
                assert not maya_cmds.play(query=True, state=True)
            finally:
                maya_cmds.play(state=False)
                om.MMessage.removeCallback(callback)
            assert (
                len(requested) >= 2
            ), "非表示の実再生中に直接設定を通過していない"
            assert (
                take(
                    "first_visible_after_stop",
                    lambda: maya_cmds.setAttr(f"{transform}.visibility", True),
                )
                == wide
            )
            assert maya_cmds.getAttr(target) == pytest.approx(6.0)
    finally:
        maya_cmds.play(state=False)
        maya_cmds.playbackOptions(**previous_playback)
        maya_cmds.currentTime(previous_time)


def test_display_cache_time_changed_direct_set_during_programmatic_scrub(
    maya_cmds, new_scene, tmp_path
):
    """通常の`currentTime`中の直接設定も、同じ値の通常画像と一致する。"""
    if maya_cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")
    from maya.api import OpenMaya as om

    previous_time = maya_cmds.currentTime(query=True)
    try:
        with _display_scene(
            maya_cmds, tmp_path, "shapeLineWidth", 1.0, 6.0
        ) as (_, _, target, take, thin, wide):
            maya_cmds.currentTime(1)
            requested = []

            def change_display(*_):
                assert not maya_cmds.play(query=True, state=True)
                value = 6.0 if len(requested) % 2 == 0 else 1.0
                maya_cmds.setAttr(target, value)
                requested.append(value)

            callback = om.MEventMessage.addEventCallback(
                "timeChanged", change_display
            )
            try:
                for frame, reference in ((2, wide), (3, thin), (1, wide)):
                    assert (
                        take(
                            f"programmatic_scrub_{frame}",
                            lambda frame=frame: maya_cmds.currentTime(frame),
                        )
                        == reference
                    )
                assert requested == [6.0, 1.0, 6.0]
            finally:
                om.MMessage.removeCallback(callback)
    finally:
        maya_cmds.currentTime(previous_time)
