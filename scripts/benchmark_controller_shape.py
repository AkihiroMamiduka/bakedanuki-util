"""独立したMaya GUIでコントローラのVP2更新時間を比較する。"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import statistics
import subprocess
import sys
import time
import traceback

_ROOT = Path(__file__).resolve().parents[1]
_CONFIG_ENV = "BD_CONTROLLER_BENCHMARK_CONFIG"
_PRESETS = ("Circle", "Cube", "WideSphereFill")
_MODES = (
    "idle",
    "parent_one",
    "parent_all",
    "playback_all",
    "matrix_all",
    "camera",
)


def _write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def _launch() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--maya-version", choices=("2025", "2026", "2027"), default="2025"
    )
    parser.add_argument("--plugin-path", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    parser.add_argument("--profile-directory", type=Path)
    parser.add_argument("--load-in-place", action="store_true")
    parser.add_argument("--adaptive-heavy", action="store_true")
    parser.add_argument("--foreground", action="store_true")
    parser.add_argument("--label", default="candidate")
    parser.add_argument(
        "--counts", type=int, nargs="+", default=(100, 500, 1000)
    )
    parser.add_argument(
        "--presets", choices=_PRESETS, nargs="+", default=_PRESETS
    )
    parser.add_argument(
        "--modes", choices=_MODES, nargs="+", default=_MODES[:-1]
    )
    parser.add_argument("--frames", type=int, default=20)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--warmup", type=int, default=5)
    parser.add_argument("--capture-checks", action="store_true")
    args = parser.parse_args()
    if (
        min(*args.counts, args.frames, args.trials, args.warmup) < 1
        or args.frames < 2
    ):
        parser.error("counts/trials/warmupは正、framesは2以上にしてください")
    executable = Path(
        f"C:/Program Files/Autodesk/Maya{args.maya_version}/bin/maya.exe"
    )
    if not executable.is_file() or not args.plugin_path.is_file():
        parser.error("Maya GUIまたは指定plug-inがありません")
    output = args.output_directory.resolve()
    output.mkdir(parents=True, exist_ok=False)
    requested_plugin = args.plugin_path.resolve()
    plugin = output / "bdUtilNodes.mll"
    shutil.copy2(requested_plugin, plugin)
    archive_hash = hashlib.sha256(plugin.read_bytes()).hexdigest()
    requested_hash = hashlib.sha256(requested_plugin.read_bytes()).hexdigest()
    if archive_hash != requested_hash:
        raise RuntimeError(
            "保存中にplug-inが変更されました。build終了後に再実行してください"
        )
    load_plugin = requested_plugin if args.load_in_place else plugin
    config = vars(args) | {
        "plugin_path": str(load_plugin),
        "plugin_requested_path": str(requested_plugin),
        "plugin_archive_path": str(plugin),
        "plugin_archive_sha256": archive_hash,
        "output_directory": str(output),
        "profile_directory": str(
            (args.profile_directory or output / "profile").resolve()
        ),
        "plugin_sha256": requested_hash,
    }
    config_path = output / "config.json"
    _write_json(config_path, config)
    script = str(Path(__file__).resolve()).replace("\\", "/")
    bootstrap = output / "launch.mel"
    command = f"import runpy; runpy.run_path({script!r}, run_name='__main__')"
    bootstrap.write_text(
        'python("import maya.utils; maya.utils.executeDeferred('
        + repr(command).replace("\\", "\\\\").replace('"', '\\"')
        + ')");\n',
        encoding="utf-8",
    )
    environment = os.environ.copy()
    environment.update(
        {
            _CONFIG_ENV: str(config_path),
            "MAYA_APP_DIR": config["profile_directory"],
            "MAYA_MODULE_PATH": str(_ROOT / "bakedanuki" / "modules"),
            "MAYA_SKIP_USERSETUP_PY": "1",
            "QT_QPA_PLATFORM": "windows",
        }
    )
    startup = subprocess.STARTUPINFO()
    startup.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startup.wShowWindow = 0
    with (output / "console.log").open("w", encoding="utf-8") as log:
        process = subprocess.Popen(
            [
                str(executable),
                "-noAutoloadPlugins",
                "-script",
                str(bootstrap),
                "-log",
                str(output / "maya.log"),
            ],
            env=environment,
            startupinfo=startup,
            stdout=log,
            stderr=subprocess.STDOUT,
        )
    state = {
        "pid": process.pid,
        "output": str(output),
        "label": args.label,
        "plugin_path": config["plugin_path"],
        "plugin_archive_path": str(plugin),
    }
    _write_json(output / "process.json", state)
    print(json.dumps(state), flush=True)
    # ランチャーも生存させ、呼出元の終了に伴うGUIの終了を避ける。
    return_code = process.wait()
    _write_json(output / "process_exit.json", {"return_code": return_code})
    raise SystemExit(return_code)


def _panel(cmds, count: int, label: str | None = None):
    from maya import utils
    from maya.api import OpenMayaUI as omui

    title = "bdControllerShape performance" + (f" [{label}]" if label else "")
    window = cmds.window(title=title, widthHeight=(960, 720))
    cmds.paneLayout()
    side = math.ceil(math.sqrt(count))
    camera, camera_shape = cmds.camera(
        orthographic=True, orthographicWidth=side * 1.7
    )
    cmds.setAttr(camera + ".translateZ", 100)
    cmds.setAttr(camera_shape + ".farClipPlane", 1000)
    panel = cmds.modelPanel(camera=camera, menuBarVisible=False)
    cmds.modelEditor(
        panel,
        edit=True,
        rendererName="vp2Renderer",
        allObjects=False,
        pluginShapes=True,
        locators=True,
        displayAppearance="smoothShaded",
        grid=False,
        headsUpDisplay=False,
        selectionHiliteDisplay=True,
    )
    cmds.setAttr("hardwareRenderingGlobals.multiSampleEnable", False)
    cmds.displayPref(displayGradient=False)
    cmds.displayRGBColor("background", 0.05, 0.05, 0.05)
    cmds.showWindow(window)
    cmds.setFocus(panel)
    utils.processIdleEvents()
    view = omui.M3dView.getM3dViewFromModelPanel(panel)
    width, height = view.portWidth(), view.portHeight()
    if width <= 0 or height <= 0:
        raise RuntimeError("Viewportの寸法が0です")
    aspect = width / height
    required_span = side * 1.8
    ortho_width = required_span * max(1.0, aspect)
    cmds.setAttr(camera_shape + ".orthographicWidth", ortho_width)
    layout = {
        "panel_width": width,
        "panel_height": height,
        "orthographic_width": ortho_width,
        "orthographic_height": ortho_width / aspect,
        "grid_side": side,
        "grid_spacing": 1.6,
        "required_layout_span": required_span,
        "layout_fits_view": min(ortho_width, ortho_width / aspect)
        >= required_span - 1e-9,
    }
    return window, panel, camera, layout


def _scene(cmds, preset: str, count: int, label: str | None = None):
    from maya.api import OpenMaya as om

    cmds.file(new=True, force=True)
    cmds.undoInfo(state=False)
    cmds.evaluationManager(mode="parallel")
    _disable_cached_playback(cmds)
    group = cmds.createNode("transform", name="benchmarkGroup")
    side = math.ceil(math.sqrt(count))
    controllers = []
    shapes = []
    # 公開enum名から解決し、enum番号の変更に依存しない。
    sample = cmds.createNode("bdControllerShape")
    enum = cmds.attributeQuery("shape", node=sample, listEnum=True)[0].split(
        ":"
    )
    cmds.delete(cmds.listRelatives(sample, parent=True)[0])
    base = "Sphere" if preset == "WideSphereFill" else preset
    modifier = om.MDagModifier()
    selection = om.MSelectionList()
    selection.add(group)
    group_object = selection.getDependNode(0)
    for index in range(count):
        controller = modifier.createNode("transform", group_object)
        shape = modifier.createNode("bdControllerShape", controller)
        controllers.append(controller)
        shapes.append(shape)
    modifier.doIt()
    transforms = [om.MFnDagNode(node).fullPathName() for node in controllers]
    shape_names = [om.MFnDagNode(node).fullPathName() for node in shapes]
    for index, (controller, shape) in enumerate(zip(transforms, shape_names)):
        cmds.setAttr(
            controller + ".translate",
            (index % side - (side - 1) / 2) * 1.6,
            (index // side - (side - 1) / 2) * 1.6,
            0,
        )
        cmds.setAttr(shape + ".shape", enum.index(base))
        cmds.setAttr(shape + ".shapeRootSize", 0.8)
        if preset == "Circle":
            cmds.setAttr(shape + ".shapeAxisRotateX", 90)
        if preset == "WideSphereFill":
            cmds.setAttr(shape + ".shapeWide", True)
            cmds.setAttr(shape + ".shapeWideWidth", 0.14)
            cmds.setAttr(shape + ".shapeFill", True)
        cmds.setAttr(shape + ".overrideEnabled", True)
        cmds.setAttr(shape + ".overrideRGBColors", True)
        cmds.setAttr(shape + ".overrideColorRGB", 0.8, 0.8, 0.8)
    window, panel, camera, layout = _panel(cmds, count, label)
    cmds.select(clear=True)
    return group, transforms, shape_names, window, panel, camera, layout


def _refresh(cmds) -> None:
    cmds.refresh(currentView=True, force=True)


def _foreground_state(context) -> dict:
    from maya import utils

    context["application"].processEvents()
    utils.processIdleEvents()
    widget = context["widget"]
    state = context["application"].applicationState()
    return {
        "visible": bool(widget.isVisible()),
        "active_window": bool(widget.isActiveWindow()),
        "minimized": bool(widget.isMinimized()),
        "application_state": int(getattr(state, "value", state)),
        "application_state_name": str(getattr(state, "name", state)),
        "application_active": state == context["active_application_state"],
        "window_title": widget.windowTitle(),
    }


def _is_foreground(state) -> bool:
    return (
        state["visible"]
        and state["active_window"]
        and not state["minimized"]
        and state["application_active"]
    )


def _wait_for_activation(context, phase, mode=None, trial=None) -> dict:
    state = _foreground_state(context)
    if _is_foreground(state):
        return state
    wait = {"phase": phase, "mode": mode, "trial": trial, "initial": state}
    context["record"].setdefault("activation_waits", []).append(wait)
    progress = {
        "status": "waiting_for_activation",
        "phase": phase,
        "mode": mode,
        "trial": trial,
        "foreground_state": state,
        "maximum_wait_seconds": 60,
    }
    _write_json(context["output"] / "progress.json", progress)
    _write_json(context["output"] / "results.json", context["result"])
    deadline = time.monotonic() + 60
    while time.monotonic() < deadline:
        time.sleep(0.1)
        state = _foreground_state(context)
        if _is_foreground(state):
            wait["ready"] = state
            _write_json(
                context["output"] / "progress.json",
                {"status": "running", "foreground_state": state},
            )
            return state
    wait["timed_out"] = True
    wait["last_state"] = state
    raise RuntimeError(
        "performance windowを60秒以内にactiveにできませんでした"
    )


def _prepare_foreground(cmds, window, config, output, result, preset, count):
    from maya import OpenMayaUI as omui
    from bd_util.ui.qt import (
        QT_BINDING,
        QT_BINDING_VERSION,
        QtCore,
        QtWidgets,
        wrapInstance,
    )

    pointer = omui.MQtUtil.findWindow(window)
    if not pointer:
        raise RuntimeError(
            "自作performance windowのQt QWidgetを取得できません"
        )
    widget = wrapInstance(int(pointer), QtWidgets.QWidget)
    application = QtWidgets.QApplication.instance()
    if application is None:
        raise RuntimeError("MayaのQApplicationがありません")
    record = {
        "preset": preset,
        "count": count,
        "window_name": window,
        "label": config["label"],
        "qt_binding": QT_BINDING,
        "qt_binding_version": QT_BINDING_VERSION,
        "trials": [],
    }
    result.setdefault("foreground_checks", []).append(record)
    context = {
        "widget": widget,
        "application": application,
        "active_application_state": QtCore.Qt.ApplicationActive,
        "record": record,
        "output": output,
        "result": result,
    }
    record["initial"] = _foreground_state(context)
    main_pointer = omui.MQtUtil.mainWindow()
    if main_pointer:
        main_window = wrapInstance(int(main_pointer), QtWidgets.QWidget)
        main_window.setWindowTitle(
            f"Maya bdControllerShape benchmark [{config['label']}]"
        )
    widget.show()
    widget.raise_()
    widget.activateWindow()
    record["ready"] = _wait_for_activation(context, "ready")
    _write_json(output / "results.json", result)
    return context


def _before_trial(context, mode, trial):
    if context is None:
        return None
    return _wait_for_activation(context, "before_trial", mode, trial + 1)


def _after_trial(context, mode, trial, before, sample):
    if context is None:
        return None
    after = _foreground_state(context)
    record = {
        "mode": mode,
        "trial": trial + 1,
        "before": before,
        "after": after,
        "ms_per_frame": sample,
        "valid": _is_foreground(before) and _is_foreground(after),
    }
    context["record"]["trials"].append(record)
    if not record["valid"]:
        raise RuntimeError(
            "trial中にperformance windowのactive/visible状態が変わりました"
        )
    return record


def _orbit_camera(cmds, camera, degrees: float) -> None:
    angle = math.radians(degrees)
    cmds.setAttr(
        camera + ".translate", 100 * math.sin(angle), 0, 100 * math.cos(angle)
    )
    cmds.setAttr(camera + ".rotate", 0, degrees, 0)


def _measurement_config(config, preset: str, count: int) -> dict:
    measurement = dict(config)
    if config.get("adaptive_heavy") and preset == "WideSphereFill":
        measurement.update(
            frames=4 if count <= 100 else 3 if count <= 500 else 2,
            trials=2,
            warmup=1,
        )
        measurement["modes"] = [
            mode
            for mode in config["modes"]
            if mode in ("parent_all", "playback_all", "matrix_all")
        ]
        if not measurement["modes"]:
            raise ValueError(
                "adaptive-heavyにはparent_all/playback_all/matrix_allのいずれかが必要です"
            )
    return measurement


def _disable_cached_playback(cmds) -> dict:
    evaluators = cmds.evaluator(query=True) or []
    registered = "cache" in evaluators
    if registered:
        cmds.evaluator(name="cache", enable=False)
        enabled = bool(cmds.evaluator(query=True, name="cache", enable=True))
        if enabled:
            raise RuntimeError("Cached Playbackを無効にできませんでした")
    else:
        enabled = False
    return {
        "cache_evaluator_registered": registered,
        "cache_evaluator_enabled": enabled,
    }


def _capture(panel: str, path: Path) -> dict:
    from ctypes import string_at
    from maya import cmds, utils
    from maya.api import OpenMaya as om
    from maya.api import OpenMayaUI as omui

    cmds.setFocus(panel)
    utils.processIdleEvents()
    view = omui.M3dView.getM3dViewFromModelPanel(panel)
    width, height = view.portWidth(), view.portHeight()
    if width <= 0 or height <= 0:
        raise RuntimeError("Viewportの寸法が0です")
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
        widthHeight=(width, height),
        frame=cmds.currentTime(query=True),
    )
    image = om.MImage()
    image.readFromFile(str(path))
    width, height = image.getSize()
    if width <= 0 or height <= 0:
        raise RuntimeError("取得画像の寸法が0です")
    pixels = string_at(image.pixels(), width * height * 4)
    foreground = sum(
        pixels[index : index + 4] != pixels[:4]
        for index in range(0, len(pixels), 4)
    )
    if foreground < 8:
        raise RuntimeError(f"背景だけの画像を取得しました: {path}")
    return {
        "width": width,
        "height": height,
        "non_background_pixels": foreground,
        "rgba_sha256": hashlib.sha256(pixels).hexdigest(),
    }


def _capture_checks(
    cmds, panel, camera, group, transforms, shapes, output, name
):
    from maya import utils

    def capture(suffix):
        utils.processIdleEvents()
        _refresh(cmds)
        path = output / f"{name}_{suffix}.png"
        _capture(panel, path)
        return str(path)

    images = {"dormant": capture("dormant")}
    cmds.select(transforms[0], replace=True)
    images["selected"] = capture("selected")
    cmds.select(clear=True)
    cmds.setAttr(shapes[0] + ".overrideColorRGB", 1.0, 0.1, 0.1)
    images["override_color"] = capture("override_color")
    cmds.setAttr(shapes[0] + ".overrideColorRGB", 0.8, 0.8, 0.8)
    _orbit_camera(cmds, camera, 25)
    images["camera"] = capture("camera")
    _orbit_camera(cmds, camera, 0)
    cmds.setAttr(group + ".rotateY", 25)
    images["parent"] = capture("parent")
    cmds.setAttr(group + ".rotateY", 0)
    cmds.modelEditor(panel, edit=True, displayAppearance="wireframe")
    images["wireframe"] = capture("wireframe")
    cmds.modelEditor(panel, edit=True, displayAppearance="smoothShaded")
    images["restored"] = capture("restored")
    return images


def _measure(
    cmds,
    config,
    mode: str,
    group: str,
    transforms,
    shapes,
    camera,
    foreground=None,
):
    frames = config["frames"]
    compose = None
    if mode == "matrix_all":
        compose = cmds.createNode("composeMatrix")
        for shape in shapes:
            cmds.connectAttr(
                compose + ".outputMatrix",
                shape + ".shapeAnimationTransformMatrix",
            )
    if mode == "playback_all":
        for attribute, first, last in (
            ("translateX", -0.1, 0.1),
            ("rotateY", -12.0, 12.0),
        ):
            cmds.setKeyframe(group, attribute=attribute, time=1, value=first)
            cmds.setKeyframe(
                group, attribute=attribute, time=frames, value=last
            )
        cmds.keyTangent(group, inTangentType="linear", outTangentType="linear")
        cmds.playbackOptions(
            minTime=1,
            maxTime=frames,
            animationStartTime=1,
            animationEndTime=frames,
            loop="once",
            playbackSpeed=0,
            maxPlaybackSpeed=0,
            view="active",
            by=1,
        )

    def step(index):
        value = math.sin(index * 0.37)
        if mode.startswith("parent_"):
            node = transforms[0] if mode == "parent_one" else group
            cmds.setAttr(node + ".rotateY", value * 12)
            cmds.setAttr(node + ".rotateX", value * 5)
        elif mode == "matrix_all":
            cmds.setAttr(compose + ".inputTranslateZ", value * 0.1)
            cmds.setAttr(compose + ".inputRotateY", value * 12)
        elif mode == "camera":
            _orbit_camera(cmds, camera, value * 5)
        _refresh(cmds)

    samples = []
    window_states = []
    for trial in range(config["trials"]):
        if mode == "playback_all":
            cmds.currentTime(1)
            _refresh(cmds)
            # 実際のMaya再生を使い、Pythonからの各フレーム操作時間と区別する。
            if trial == 0:
                cmds.play(forward=True, wait=True)
                cmds.currentTime(1)
                _refresh(cmds)
            before = _before_trial(foreground, mode, trial)
            started = time.perf_counter()
            cmds.play(forward=True, wait=True)
            elapsed = time.perf_counter() - started
            if abs(cmds.currentTime(query=True) - frames) > 0.01:
                raise RuntimeError("再生が指定終端へ到達しませんでした")
            sample = elapsed * 1000 / (frames - 1)
        else:
            for index in range(config["warmup"]):
                step(index)
            before = _before_trial(foreground, mode, trial)
            started = time.perf_counter()
            for index in range(frames):
                step(index + config["warmup"])
            sample = (time.perf_counter() - started) * 1000 / frames
        state = _after_trial(foreground, mode, trial, before, sample)
        if state is not None:
            window_states.append(state)
        samples.append(sample)
    if mode == "playback_all":
        cmds.cutKey(group, clear=True)
        cmds.setAttr(group + ".translateX", 0)
        cmds.setAttr(group + ".rotateY", 0)
    if mode.startswith("parent_"):
        node = transforms[0] if mode == "parent_one" else group
        cmds.setAttr(node + ".rotate", 0, 0, 0)
    if compose:
        cmds.delete(compose)
        identity = (1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
        for shape in shapes:
            cmds.setAttr(
                shape + ".shapeAnimationTransformMatrix",
                *identity,
                type="matrix",
            )
    if mode == "camera":
        _orbit_camera(cmds, camera, 0)
    measured = {
        "trial_ms_per_frame": samples,
        "median_ms_per_frame": statistics.median(samples),
    }
    if foreground is not None:
        measured["trial_window_states"] = window_states
    return measured


def _save_final_state(output: Path, result: dict, exit_code: int) -> None:
    result["exit_code"] = exit_code
    _write_json(output / "results.json", result)
    _write_json(
        output / "progress.json",
        {
            "status": result["status"],
            "completed": len(result["cases"]),
            "exit_code": exit_code,
        },
    )


def _finish_gui(cmds, output: Path, result: dict, exit_code: int) -> None:
    import ctypes
    from ctypes import wintypes

    _save_final_state(output, result, exit_code)
    try:
        cmds.file(new=True, force=True)
        result["scene_cleanup"] = "complete"
    except BaseException:
        exit_code = 1
        result["status"] = "failed"
        result["scene_cleanup"] = "failed"
        result["cleanup_error"] = traceback.format_exc()
    _save_final_state(output, result, exit_code)
    try:
        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel32.GetCurrentProcess.argtypes = []
        kernel32.GetCurrentProcess.restype = wintypes.HANDLE
        kernel32.TerminateProcess.argtypes = [wintypes.HANDLE, wintypes.UINT]
        kernel32.TerminateProcess.restype = wintypes.BOOL
        result["termination_method"] = "TerminateProcess(GetCurrentProcess())"
        _save_final_state(output, result, exit_code)
        # 結果とscene破棄を確定した検証専用の自processだけを閉じ、DLL終了待ちを避ける。
        if not kernel32.TerminateProcess(
            kernel32.GetCurrentProcess(), exit_code
        ):
            raise ctypes.WinError(ctypes.get_last_error())
    except BaseException:
        result["status"] = "failed"
        result["termination_error"] = traceback.format_exc()
        _save_final_state(output, result, 1)
        os._exit(1)


def _run_gui(config_path: Path) -> None:
    from maya import cmds, utils

    config = json.loads(config_path.read_text(encoding="utf-8"))
    output = Path(config["output_directory"])
    _write_json(
        output / "progress.json", {"status": "starting", "completed": 0}
    )
    result = {"config": config, "cases": [], "status": "running"}
    exit_code = 1
    try:
        if cmds.about(batch=True):
            raise RuntimeError("実VP2パネルを持つMaya GUIが必要です")
        _write_json(
            output / "progress.json",
            {"status": "loading_plugin", "completed": 0},
        )
        loaded_plugins = cmds.loadPlugin(config["plugin_path"], quiet=True)
        loaded_name = (
            loaded_plugins[0]
            if loaded_plugins
            else Path(config["plugin_path"]).stem
        )
        loaded_path = Path(
            cmds.pluginInfo(loaded_name, query=True, path=True)
        ).resolve()
        loaded_hash = hashlib.sha256(loaded_path.read_bytes()).hexdigest()
        if (
            loaded_path != Path(config["plugin_path"]).resolve()
            or loaded_hash != config["plugin_sha256"]
        ):
            raise RuntimeError(
                "実際にロードされたplug-inが指定されたpath/hashと一致しません"
            )
        _write_json(
            output / "progress.json",
            {"status": "plugin_loaded", "completed": 0},
        )
        cmds.evaluationManager(mode="parallel")
        result["environment"] = {
            "maya": cmds.about(version=True),
            "api": cmds.about(apiVersion=True),
            "gpu": cmds.ogs(deviceInformation=True),
            "python": sys.version,
            "measurement": "wall time including DG updates and VP2 refresh; no GPU draw-call counters",
            "loaded_plugin_path": str(loaded_path),
            "loaded_plugin_sha256": loaded_hash,
            "plugin_archive_path": config["plugin_archive_path"],
            "plugin_archive_sha256": config["plugin_archive_sha256"],
            "cached_playback": _disable_cached_playback(cmds),
            "evaluation_mode": cmds.evaluationManager(query=True, mode=True),
            "units": {
                name: cmds.currentUnit(query=True, **{name: True})
                for name in ("linear", "angle", "time")
            },
        }
        for count in config["counts"]:
            for preset in config["presets"]:
                measurement = _measurement_config(config, preset, count)
                measurement_options = {
                    name: measurement[name]
                    for name in ("frames", "trials", "warmup")
                }
                started = time.perf_counter()
                group, transforms, shapes, window, panel, camera, layout = (
                    _scene(
                        cmds,
                        preset,
                        count,
                        config["label"] if config.get("foreground") else None,
                    )
                )
                foreground = (
                    _prepare_foreground(
                        cmds, window, config, output, result, preset, count
                    )
                    if config.get("foreground")
                    else None
                )
                utils.processIdleEvents()
                for _ in range(measurement["warmup"]):
                    _refresh(cmds)
                setup_seconds = time.perf_counter() - started
                viewport = _capture(panel, output / f"{preset}_{count}.png")
                for mode in measurement["modes"]:
                    _write_json(
                        output / "progress.json",
                        {
                            "preset": preset,
                            "count": count,
                            "mode": mode,
                            "completed": len(result["cases"]),
                            "status": "running",
                            "measurement_options": measurement_options,
                        },
                    )
                    case = {
                        "preset": preset,
                        "count": count,
                        "mode": mode,
                        "setup_seconds": setup_seconds,
                        "viewport": viewport,
                        "layout": layout,
                        "cached_playback": _disable_cached_playback(cmds),
                        "measurement_options": measurement_options,
                    } | _measure(
                        cmds,
                        measurement,
                        mode,
                        group,
                        transforms,
                        shapes,
                        camera,
                        foreground,
                    )
                    result["cases"].append(case)
                    _write_json(output / "results.json", result)
                    print(
                        "CONTROLLER_BENCHMARK " + json.dumps(case), flush=True
                    )
                if config.get("capture_checks"):
                    images = _capture_checks(
                        cmds,
                        panel,
                        camera,
                        group,
                        transforms,
                        shapes,
                        output,
                        f"{preset}_{count}",
                    )
                    result.setdefault("visual_checks", []).append(
                        {"preset": preset, "count": count, "images": images}
                    )
                cmds.deleteUI(window)
        result["status"] = "complete"
        exit_code = 0
    except Exception:
        result["status"] = "failed"
        result["error"] = traceback.format_exc()
        print(result["error"], flush=True)
    finally:
        _finish_gui(cmds, output, result, exit_code)


if __name__ == "__main__":
    if _CONFIG_ENV in os.environ:
        _run_gui(Path(os.environ[_CONFIG_ENV]))
    else:
        _launch()
