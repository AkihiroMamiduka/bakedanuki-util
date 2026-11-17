"""固定 Cube の描画方式を独立した Maya GUI で比較する。"""

from __future__ import annotations

import ctypes
import faulthandler
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import statistics
import sys
import time
import traceback

# 12 辺を最短の degree 1 開曲線で辿るため、3 辺を重ねて通る。
_VERTICES = tuple(itertools.product((-0.5, 0.5), repeat=3))
_CURVE_INDICES = (6, 4, 5, 1, 0, 2, 3, 7, 5, 4, 0, 1, 3, 2, 6, 7)


def _write(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _profile_hashes(config: dict) -> dict:
    profile = Path(config["profile_directory"])
    version = config["maya_version"]
    return {
        relative: (
            _sha(profile / relative)
            if (profile / relative).is_file()
            else None
        )
        for relative in (
            f"{version}/prefs/userPrefs.mel",
            f"{version}/Maya.env",
            "Maya.env",
        )
    }


def _terminate_current_process(code: int) -> None:
    """結果保存済みの専用 Maya process を通常終了処理を経ずに終了する。"""
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.GetCurrentProcess.restype = ctypes.c_void_p
    kernel32.TerminateProcess.argtypes = [ctypes.c_void_p, ctypes.c_uint]
    if not kernel32.TerminateProcess(kernel32.GetCurrentProcess(), code):
        raise ctypes.WinError(ctypes.get_last_error())


class CubeBenchmark:
    """測定用の専用シーンと、その表示状態を管理する。"""

    def __init__(self, config: dict) -> None:
        from maya import cmds, OpenMayaUI as ui1, utils
        from maya.api import OpenMaya as om, OpenMayaUI as omui

        try:
            from PySide6 import QtCore, QtWidgets
            from shiboken6 import wrapInstance
        except ImportError:
            from PySide2 import QtCore, QtWidgets
            from shiboken2 import wrapInstance

        self.cmds, self.om, self.omui, self.ui1 = cmds, om, omui, ui1
        self.utils, self.QtCore, self.QtWidgets = utils, QtCore, QtWidgets
        self.wrap = wrapInstance
        self.config = config
        self.output = Path(config["output_directory"])
        self.result = {
            "status": "running",
            "pid": os.getpid(),
            "config": config,
            "cases": [],
            "scenes": [],
            "functional": [],
            "interpretation": (
                "Scripted results include setAttr and forced refresh. Playback "
                "includes start/stop overhead and is per requested frame, not HUD FPS. "
                "Trials in one process are nested samples, not independent processes."
            ),
        }
        self.window = None
        self.callbacks = []
        self.posts = 0
        self.blank_pixels = None
        main_window = self.wrap(
            int(ui1.MQtUtil.mainWindow()), QtWidgets.QWidget
        )
        main_window.showNormal()
        main_window.raise_()
        main_window.activateWindow()
        self._configure()

    def _configure(self) -> None:
        c = self.cmds
        _write(self.output / "progress.json", {"status": "configuring"})
        if c.about(batch=True):
            raise RuntimeError("実 VP2 を持つ Maya GUI が必要です")
        if int(c.about(apiVersion=True)) // 10000 != int(
            self.config["maya_version"]
        ):
            raise RuntimeError("要求した Maya version と実行環境が異なります")
        if _sha(Path(__file__)) != self.config["benchmark_sha256"]:
            raise RuntimeError("起動した benchmark の SHA256 が異なります")
        profile_hashes = _profile_hashes(self.config)
        if (
            Path(os.environ["MAYA_APP_DIR"]).resolve()
            != Path(self.config["profile_directory"]).resolve()
            or profile_hashes != self.config["profile_file_sha256"]
        ):
            raise RuntimeError(
                "専用 profile の path / 設定 SHA256 が異なります"
            )
        plugin = None
        if self.config["plugin_path"]:
            archive = Path(self.config["plugin_archive_path"]).resolve()
            archive_hash = _sha(archive)
            if (
                archive.parent != self.output.resolve()
                or archive_hash != self.config["plugin_sha256"]
                or _sha(Path(self.config["plugin_path"])) != archive_hash
            ):
                raise RuntimeError(
                    "固定 DLL と証拠 archive の SHA256 が異なります"
                )
            _write(self.output / "progress.json", {"status": "loading_plugin"})
            loaded = c.loadPlugin(self.config["plugin_path"], quiet=True)[0]
            _write(self.output / "progress.json", {"status": "plugin_loaded"})
            actual = Path(
                c.pluginInfo(loaded, query=True, path=True)
            ).resolve()
            plugin = {
                "path": str(actual),
                "sha256": _sha(actual),
                "archive_path": str(archive),
                "archive_sha256": archive_hash,
                "api_version": int(
                    c.pluginInfo(loaded, query=True, apiVersion=True)
                ),
                "commands": c.pluginInfo(loaded, query=True, command=True)
                or [],
            }
            if (
                actual != Path(self.config["plugin_path"]).resolve()
                or plugin["sha256"] != self.config["plugin_sha256"]
                or plugin["api_version"] // 10000
                != int(self.config["maya_version"])
            ):
                raise RuntimeError(
                    "実 load DLL の path / SHA256 / API が異なります"
                )
        if self.config.get("native_profile") and (
            not plugin or "bdCubeProfile" not in plugin["commands"]
        ):
            raise RuntimeError("NativeProfile には診断用ビルドが必要です")
        c.profiler(sampling=False)
        self.result["runtime"] = {
            "maya": c.about(version=True),
            "api_version": c.about(apiVersion=True),
            "gpu": c.ogs(deviceInformation=True),
            "python": sys.version,
            "plugin": plugin,
            "profile_file_sha256": profile_hashes,
            "environment": {
                name: os.environ.get(name)
                for name in (
                    "MAYA_APP_DIR",
                    "MAYA_MODULE_PATH",
                    "MAYA_VP2_DEVICE_OVERRIDE",
                    "MAYA_VP2_USE_VP1_SELECTION",
                    "MAYA_DISABLE_VP2_CONSOLIDATION",
                    "MAYA_DISABLE_VP2_PLUGIN_CONSOLIDATION",
                    "MAYA_VP2_USE_GPU_INSTANCING",
                )
            },
            "consolidation_and_instancing": (
                "Maya defaults; independent DAG nodes, no DAG instances. "
                "RenderItem requests are determined by the recorded DLL. "
                "Actual consolidation, GPU instancing and draw calls are not measured."
            ),
        }
        if c.paneLayout("viewPanes", exists=True):
            c.paneLayout("viewPanes", edit=True, manage=False)

    def _new_shape(self, parent: str, mode: str) -> str:
        c = self.cmds
        if mode == "curve":
            selection = self.om.MSelectionList()
            selection.add(parent)
            points = self.om.MPointArray(
                [self.om.MPoint(*_VERTICES[i]) for i in _CURVE_INDICES]
            )
            obj = self.om.MFnNurbsCurve().create(
                points,
                list(range(len(_CURVE_INDICES))),
                1,
                self.om.MFnNurbsCurve.kOpen,
                False,
                False,
                selection.getDependNode(0),
            )
            shape = self.om.MFnDagNode(obj).fullPathName()
        else:
            shape = c.createNode(
                "bdControllerShape" if mode == "controller" else "bdShpL_Cube",
                parent=parent,
            )
            shape = c.ls(shape, long=True)[0]
            if mode == "controller":
                names = c.attributeQuery("shape", node=shape, listEnum=True)[
                    0
                ].split(":")
                c.setAttr(shape + ".shape", names.index("Cube"))
                for attr, value in (
                    ("shapeRootSize", 1),
                    ("shapeFill", False),
                    ("shapeDrawOnTop", False),
                    ("shapeLineWidth", 1),
                    ("shapeLineTransparency", 0),
                ):
                    c.setAttr(shape + "." + attr, value)
        c.setAttr(shape + ".overrideEnabled", True)
        c.setAttr(shape + ".overrideRGBColors", True)
        c.setAttr(shape + ".overrideColorRGB", 0.8, 0.8, 0.8)
        if mode == "curve":
            c.setAttr(shape + ".lineWidth", 1)
        return shape

    def _scene(self, count: int, label: str | None = None) -> dict:
        c = self.cmds
        self._remove_callbacks()
        if self.window and c.window(self.window, exists=True):
            c.deleteUI(self.window, window=True)
        c.file(new=True, force=True)
        c.currentUnit(linear="cm", angle="deg", time="film")
        c.undoInfo(state=False)
        c.evaluationManager(mode="parallel")
        if "cache" in (c.evaluator(query=True) or []):
            c.evaluator(name="cache", enable=False)
        c.setAttr("hardwareRenderingGlobals.multiSampleEnable", False)
        c.setAttr("hardwareRenderingGlobals.lineAAEnable", False)
        self.group = c.createNode("transform", name="cubeBenchmarkGroup")
        side = math.ceil(math.sqrt(count))
        self.transforms, self.shapes = [], []
        for index in range(count):
            node = c.createNode("transform", parent=self.group)
            c.setAttr(
                node + ".translate",
                (index % side - (side - 1) / 2) * 1.8,
                (index // side - (side - 1) / 2) * 1.8,
                0,
            )
            self.transforms.append(c.ls(node, long=True)[0])
            self.shapes.append(self._new_shape(node, self.config["mode"]))
        self.group = c.ls(self.group, long=True)[0]
        self.camera, camera_shape = c.camera(orthographic=True)
        self.distance = max(100.0, side * 8.0)
        c.setAttr(camera_shape + ".farClipPlane", self.distance * 4)
        self._orbit(0)
        self.window = c.window(
            title=f"Fixed Cube {self.config['mode']} {count}",
            widthHeight=(960, 720),
        )
        c.paneLayout()
        self.panel = c.modelPanel(camera=self.camera, menuBarVisible=False)
        c.modelEditor(
            self.panel,
            edit=True,
            rendererName="vp2Renderer",
            allObjects=False,
            pluginShapes=True,
            locators=True,
            nurbsCurves=True,
            displayAppearance="smoothShaded",
            grid=False,
            headsUpDisplay=False,
            selectionHiliteDisplay=True,
        )
        c.displayPref(displayGradient=False)
        c.displayRGBColor("background", 0.05, 0.05, 0.05)
        c.toggleAxis(origin=False)
        if c.headsUpDisplay("HUDViewAxis", exists=True):
            c.headsUpDisplay("HUDViewAxis", edit=True, visible=False)
        c.showWindow(self.window)
        c.setFocus(self.panel)
        c.setToolTo("selectSuperContext")
        c.select(clear=True)
        self.utils.processIdleEvents()
        self.view = self.omui.M3dView.getM3dViewFromModelPanel(self.panel)
        aspect = self.view.portWidth() / self.view.portHeight()
        self.span = max(4.0, side * 2.3)
        c.setAttr(
            camera_shape + ".orthographicWidth", self.span * max(1, aspect)
        )
        self.widget = self.wrap(
            int(self.ui1.MQtUtil.findWindow(self.window)),
            self.QtWidgets.QWidget,
        )
        self.application = self.QtWidgets.QApplication.instance()
        self.widget.show()
        self.widget.raise_()
        self.widget.activateWindow()
        self._activate()
        self.posts = 0
        self.callbacks.append(
            self.omui.MUiMessage.add3dViewPostRenderMsgCallback(
                self.panel, self._on_render
            )
        )
        c.undoInfo(state=True)
        self.blank_pixels = None
        c.setAttr(self.group + ".visibility", False)
        scene_label = label or str(count)
        blank = self._capture(f"{scene_label}_blank", blank=True)
        c.setAttr(self.group + ".visibility", True)
        self._refresh()
        info = {
            "count": count,
            "label": scene_label,
            "mode": self.config["mode"],
            "independent_transforms": len(self.transforms),
            "independent_shapes": len(self.shapes),
            "dag_instances": 0,
            "curve_degree": 1 if self.config["mode"] == "curve" else None,
            "curve_cvs": 16 if self.config["mode"] == "curve" else None,
            "curve_segments": 15 if self.config["mode"] == "curve" else None,
            "unique_cube_edges": 12,
            "curve_history": False if self.config["mode"] == "curve" else None,
            "initial_guard": self._guard(),
            "bounds": self._bounds(),
            "blank_image": blank,
            "image": self._capture(f"{scene_label}_initial"),
        }
        self.result["scenes"].append(info)
        return info

    def _refresh(self) -> None:
        self.cmds.refresh(currentView=True, force=True)

    def _on_render(self, *unused) -> None:
        self.posts += 1

    def _orbit(self, degrees: float) -> None:
        angle = math.radians(degrees)
        self.cmds.setAttr(
            self.camera + ".translate",
            self.distance * math.sin(angle),
            0,
            self.distance * math.cos(angle),
        )
        self.cmds.setAttr(self.camera + ".rotate", 0, degrees, 0)

    def _activate(self) -> None:
        deadline = time.monotonic() + self.config["activation_timeout"]
        _write(
            self.output / "progress.json",
            {"status": "waiting_for_activation", "pid": os.getpid()},
        )
        while time.monotonic() < deadline:
            self.widget.raise_()
            self.widget.activateWindow()
            self.application.processEvents()
            self.cmds.modelEditor(self.panel, edit=True, activeView=True)
            self.cmds.setFocus(self.panel)
            guard = self._guard(check=False)
            if guard["foreground_valid"] and guard["active_view"]:
                return
            time.sleep(0.1)
        raise RuntimeError(
            "測定 window の前面状態を確認できません: "
            + json.dumps(self._guard(check=False))
        )

    def _guard(self, check: bool = True) -> dict:
        c = self.cmds
        user32 = ctypes.WinDLL("user32", use_last_error=True)
        user32.GetForegroundWindow.restype = ctypes.c_void_p
        user32.GetWindowThreadProcessId.argtypes = [
            ctypes.c_void_p,
            ctypes.POINTER(ctypes.c_ulong),
        ]
        hwnd = user32.GetForegroundWindow()
        pid = ctypes.c_ulong()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        valid = bool(
            pid.value == os.getpid()
            and self.widget.isVisible()
            and not self.widget.isMinimized()
            and self.application.applicationState()
            == self.QtCore.Qt.ApplicationActive
        )
        cache = (
            bool(c.evaluator(query=True, name="cache", enable=True))
            if "cache" in (c.evaluator(query=True) or [])
            else False
        )
        record = {
            "foreground_valid": valid,
            "foreground_pid": pid.value,
            "foreground_hwnd": int(hwnd or 0),
            "target_hwnd": int(self.widget.winId()),
            "target_active_window": bool(self.widget.isActiveWindow()),
            "active_view": int(self.omui.M3dView.active3dView().widget())
            == int(self.view.widget()),
            "viewport": [self.view.portWidth(), self.view.portHeight()],
            "camera": self.view.getCamera().fullPathName(),
            "selection": c.ls(selection=True, long=True),
            "evaluation": c.evaluationManager(query=True, mode=True),
            "cache_enabled": cache,
            "msaa": bool(
                c.getAttr("hardwareRenderingGlobals.multiSampleEnable")
            ),
            "line_aa": bool(
                c.getAttr("hardwareRenderingGlobals.lineAAEnable")
            ),
            "profiler": bool(c.profiler(query=True, sampling=True)),
            "current_time": c.currentTime(query=True),
            "undo": c.undoInfo(query=True, state=True),
            "hud": bool(
                c.modelEditor(self.panel, query=True, headsUpDisplay=True)
            ),
            "origin_axis": bool(c.toggleAxis(query=True, origin=True)),
        }
        if check and (
            not valid
            or not record["active_view"]
            or not record["evaluation"]
            or record["evaluation"][0] != "parallel"
            or any(
                record[name]
                for name in (
                    "cache_enabled",
                    "msaa",
                    "line_aa",
                    "profiler",
                    "hud",
                    "origin_axis",
                )
            )
        ):
            raise RuntimeError(
                "測定条件が成立していません: " + json.dumps(record)
            )
        return record

    def _bounds(self) -> dict:
        selection = self.om.MSelectionList()
        outside = 0
        minimum = [float("inf")] * 3
        maximum = [float("-inf")] * 3
        screen_minimum = [float("inf")] * 2
        screen_maximum = [float("-inf")] * 2
        width, height = self.view.portWidth(), self.view.portHeight()
        for shape in self.shapes:
            selection.clear()
            selection.add(shape)
            path = selection.getDagPath(0)
            box = self.om.MFnDagNode(path).boundingBox
            matrix = path.inclusiveMatrix()
            for corner in itertools.product(
                *[(box.min[i], box.max[i]) for i in range(3)]
            ):
                point = self.om.MPoint(*corner) * matrix
                x, y, visible = self.view.worldToView(point)
                outside += int(
                    not visible or not (0 <= x < width and 0 <= y < height)
                )
                screen_minimum[0] = min(screen_minimum[0], x)
                screen_minimum[1] = min(screen_minimum[1], y)
                screen_maximum[0] = max(screen_maximum[0], x)
                screen_maximum[1] = max(screen_maximum[1], y)
                for axis in range(3):
                    minimum[axis] = min(minimum[axis], point[axis])
                    maximum[axis] = max(maximum[axis], point[axis])
        record = {
            "minimum": minimum,
            "maximum": maximum,
            "outside_corners": outside,
            "screen_minimum": screen_minimum,
            "screen_maximum": screen_maximum,
        }
        if outside:
            raise RuntimeError("全 bounding box が画面に収まっていません")
        return record

    def _capture(self, name: str, blank: bool = False) -> dict:
        self._refresh()
        image = self.om.MImage()
        self.view.readColorBuffer(image, True)
        width, height = image.getSize()
        if width < 1 or height < 1:
            raise RuntimeError("取得画像の寸法が0です")
        pixels = ctypes.string_at(image.pixels(), width * height * 4)
        non_background = sum(
            pixels[i : i + 4] != pixels[:4] for i in range(0, len(pixels), 4)
        )
        if blank:
            self.blank_pixels = pixels
            changed_from_blank = 0
            changed_in_bounds = 0
        else:
            if self.blank_pixels is None or len(self.blank_pixels) != len(
                pixels
            ):
                raise RuntimeError("同じ寸法の blank 画像がありません")
            changed_from_blank = sum(
                pixels[i : i + 4] != self.blank_pixels[i : i + 4]
                for i in range(0, len(pixels), 4)
            )
            bounds = self._bounds()
            xmin, ymin = bounds["screen_minimum"]
            xmax, ymax = bounds["screen_maximum"]
            changed_in_bounds = 0
            for y in range(max(0, ymin - 2), min(height, ymax + 3)):
                for x in range(max(0, xmin - 2), min(width, xmax + 3)):
                    offset = (y * width + x) * 4
                    changed_in_bounds += (
                        pixels[offset : offset + 4]
                        != self.blank_pixels[offset : offset + 4]
                    )
            if changed_in_bounds < 8:
                raise RuntimeError("shape 非表示時から画像が変化しません")
        path = self.output / (name + ".png")
        image.writeToFile(str(path), "png")
        return {
            "path": str(path),
            "size": [width, height],
            "non_background_pixels": non_background,
            "pixels_changed_from_blank": changed_from_blank,
            "pixels_changed_from_blank_inside_shape_bounds": changed_in_bounds,
            "is_blank_reference": blank,
            "rgba_sha256": hashlib.sha256(pixels).hexdigest(),
            "file_sha256": _sha(path),
        }

    def _step(self, case: str, index: int) -> None:
        value = math.sin(index * 0.37)
        if case in ("individual", "group"):
            node = self.transforms[0] if case == "individual" else self.group
            self.cmds.setAttr(node + ".rotate", value * 5, value * 12, 0)
        elif case == "camera":
            self._orbit(value * 12)
        self._refresh()

    def _measure(self, count: int, case: str) -> None:
        faulthandler.cancel_dump_traceback_later()
        c = self.cmds
        target = (
            self.group if case in ("group", "playback") else self.transforms[0]
        )
        c.select(target, replace=True)
        c.setFocus(self.panel)
        self._refresh()
        before_image = self._capture(f"{count}_{case}_before")
        frames = self.config["frames"]
        samples = []
        curves = []
        if case == "playback":
            for frame, value in ((1, -12), (frames, 12)):
                c.setKeyframe(
                    target, attribute="rotateY", time=frame, value=value
                )
            c.keyTangent(
                target, inTangentType="linear", outTangentType="linear"
            )
            curves = (
                c.listConnections(
                    target + ".rotateY", source=True, type="animCurve"
                )
                or []
            )
            c.playbackOptions(
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
            c.currentTime(1)
            self._refresh()
            c.play(forward=True, wait=True)
        for trial in range(self.config["trials"]):
            if case == "playback":
                c.currentTime(1)
                self._refresh()
            else:
                for frame in range(self.config["warmup"]):
                    self._step(case, frame)
            self._activate()
            before = self._guard()
            posts = self.posts
            if self.config.get("native_profile"):
                c.bdCubeProfile(reset=True)
            if self.config.get("maya_profile"):
                c.profiler(reset=True)
                c.profiler(bufferSize=32)
                c.profiler(sampling=True)
            started = time.perf_counter()
            try:
                if case == "playback":
                    c.play(forward=True, wait=True)
                else:
                    for frame in range(frames):
                        self._step(case, frame + self.config["warmup"])
            finally:
                elapsed = time.perf_counter() - started
                if self.config.get("maya_profile"):
                    c.profiler(sampling=False)
            post_count = self.posts - posts
            maya_profile = None
            if self.config.get("maya_profile"):
                path = self.output / f"{count}_{case}_{trial + 1}.profiler"
                c.profiler(output=str(path))
                maya_profile = {
                    "path": str(path),
                    "sha256": _sha(path),
                    "events": c.profiler(query=True, eventCount=True),
                }
            native_profile = (
                json.loads(c.bdCubeProfile())
                if self.config.get("native_profile")
                else None
            )
            after = self._guard()
            if (
                before["selection"] != after["selection"]
                or before["viewport"] != after["viewport"]
            ):
                raise RuntimeError(
                    "測定中に選択または viewport 寸法が変化しました"
                )
            if (
                case == "playback"
                and abs(after["current_time"] - frames) > 0.01
            ):
                raise RuntimeError("再生が終端 frame に到達しませんでした")
            if post_count < 1:
                raise RuntimeError("計時区間に対象 view の描画がありません")
            samples.append(
                {
                    "trial": trial + 1,
                    "wall_seconds": elapsed,
                    "ms_per_requested_frame": elapsed * 1000 / frames,
                    "requested_frames": frames,
                    "post_render_count": post_count,
                    "before": before,
                    "after": after,
                    "native_profile": native_profile,
                    "maya_profile": maya_profile,
                }
            )
        if curves:
            c.delete(curves)
        c.setAttr(target + ".rotate", 0, 0, 0)
        c.currentTime(1)
        self._orbit(0)
        restored = self._capture(f"{count}_{case}_restored")
        if before_image["rgba_sha256"] != restored["rgba_sha256"]:
            raise RuntimeError("操作後の画像が初期画像へ復元しませんでした")
        self.result["cases"].append(
            {
                "count": count,
                "case": case,
                "samples": samples,
                "median_ms_per_requested_frame": statistics.median(
                    sample["ms_per_requested_frame"] for sample in samples
                ),
                "before_image": before_image,
                "restored_image": restored,
                "bounds_after_restore": self._bounds(),
                "denominator_note": "Requested frames; actual rendered frames are recorded separately.",
            }
        )
        _write(self.output / "results.json", self.result)

    def run(self) -> None:
        """配置数ごとの測定を行い、各条件の結果を保存する。"""
        if self.config.get("renderer_reset_gate"):
            self._scene(1, "renderer_reset_scene")
            self.cmds.setAttr(self.group + ".rotate", 12, 22, 8)
            before = self._capture("renderer_reset_before")
            self.cmds.ogs(reset=True)
            self._activate()
            after = self._capture("renderer_reset_after")
            report = {
                "before": before,
                "after": after,
                "same_rgba": before["rgba_sha256"] == after["rgba_sha256"],
                "guard": self._guard(),
            }
            self.result["renderer_reset_gate"] = report
            if not report["same_rgba"]:
                raise RuntimeError("renderer reset 後の描画が一致しません")
            self._screen_pick()
            report["status"] = "passed"
            self.result["status"] = "passed"
            return
        if self.config.get("playback_gate"):
            import importlib.util

            path = Path(__file__).with_name("playback_gate.py")
            if _sha(path) != self.config["playback_gate_sha256"]:
                raise RuntimeError("再生画像検証scriptのSHA256が異なります")
            spec = importlib.util.spec_from_file_location(
                "cube_playback_gate", path
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module.run(self)
            self.result["status"] = "passed"
            return
        for count in self.config["counts"]:
            self._scene(count)
            for case in self.config["cases"]:
                _write(
                    self.output / "progress.json",
                    {
                        "status": "measuring",
                        "count": count,
                        "case": case,
                    },
                )
                self._measure(count, case)
            if self.config.get("native_profile"):
                self.cmds.bdCubeProfile(reset=True)
                self.cmds.bdCubeProfile(dirty=True)
                self._refresh()
                control = json.loads(self.cmds.bdCubeProfile())
                self.result.setdefault("native_profile_controls", []).append(
                    {"count": count, "forced_geometry_dirty": control}
                )
                if not control["updateRenderItems"]["calls"]:
                    raise RuntimeError(
                        "診断カウンターの対照試験で描画更新を検出できません"
                    )
        if self.config["functional"]:
            self._functional()
        self.result["status"] = "passed"

    def _functional(self) -> None:
        self._scene(1, "functional_scene")
        c = self.cmds
        node = self.transforms[0]
        c.select(clear=True)
        initial = self._capture("functional_initial")
        self._screen_pick()
        c.select(clear=True)
        cases = (
            ("rotatePivot", (0.2, -0.1, 0.1)),
            ("scalePivot", (-0.1, 0.2, 0.1)),
            ("rotateAxis", (15, 25, 10)),
            ("shear", (0.2, -0.1, 0.15)),
            ("scale", (-1.2, 0.7, 1.1)),
        )
        for attribute, value in cases:
            old = c.getAttr(node + "." + attribute)[0]
            c.setAttr(node + ".rotate", 12, 22, 8)
            if attribute == "scalePivot":
                c.setAttr(node + ".scale", 1.15, 0.85, 1.1)
            reference = self._capture("functional_" + attribute + "_reference")
            c.setAttr(node + "." + attribute, *value)
            tested = self._capture("functional_" + attribute)
            if tested["rgba_sha256"] == reference["rgba_sha256"]:
                raise RuntimeError(attribute + " の変更が描画に反映されません")
            bounds = self._bounds()
            c.setAttr(node + "." + attribute, *old)
            c.setAttr(node + ".rotate", 0, 0, 0)
            if attribute == "scalePivot":
                c.setAttr(node + ".scale", 1, 1, 1)
            restored = self._capture("functional_" + attribute + "_restored")
            if restored["rgba_sha256"] != initial["rgba_sha256"]:
                raise RuntimeError(attribute + " の復元画像が一致しません")
            self.result["functional"].append(
                {
                    "attribute": attribute,
                    "value": value,
                    "image": tested,
                    "reference": reference,
                    "attribute_changed_rendering": True,
                    "bounds": bounds,
                    "restored": restored,
                    "scope": "Render/nonempty/bounds/restore smoke; compare identical case images from curve mode separately.",
                }
            )
        old_group = self.group
        joint = c.createNode("joint", name="functionalJoint")
        self.group = c.ls(
            c.parent(self.group, joint, relative=True)[0], long=True
        )[0]
        self.transforms = [
            path.replace(old_group, self.group, 1) for path in self.transforms
        ]
        self.shapes = [
            path.replace(old_group, self.group, 1) for path in self.shapes
        ]
        c.select(clear=True)
        c.setAttr(joint + ".jointOrient", 17, 23, 11)
        tested = self._capture("functional_jointOrient")
        if tested["rgba_sha256"] == initial["rgba_sha256"]:
            raise RuntimeError("jointOrient の変更が描画に反映されません")
        bounds = self._bounds()
        c.setAttr(joint + ".jointOrient", 0, 0, 0)
        restored = self._capture("functional_jointOrient_restored")
        if restored["rgba_sha256"] != initial["rgba_sha256"]:
            raise RuntimeError("jointOrient の復元画像が一致しません")
        self.result["functional"].append(
            {
                "attribute": "parent_joint.jointOrient",
                "value": [17, 23, 11],
                "image": tested,
                "attribute_changed_rendering": True,
                "bounds": bounds,
                "restored": restored,
                "scope": "Parent joint orientation smoke; compare curve run separately.",
            }
        )

    def _screen_pick(self) -> None:
        c = self.cmds
        c.selectMode(object=True)
        c.selectType(allObjects=True)
        selection = self.om.MSelectionList()
        selection.add(self.transforms[0])
        matrix = selection.getDagPath(0).inclusiveMatrix()
        checks = []
        self.result["screen_selection"] = {
            "method": "MGlobal.selectFromScreen, 5px rectangle, wireframe selection; not physical mouse input",
            "checks": checks,
        }
        for first, second in itertools.combinations(_VERTICES, 2):
            if sum(a != b for a, b in zip(first, second)) != 1:
                continue
            midpoint = (
                self.om.MPoint(*[(a + b) * 0.5 for a, b in zip(first, second)])
                * matrix
            )
            x, y, visible = self.view.worldToView(midpoint)
            if not visible:
                raise RuntimeError("選択検証の辺が画面にありません")
            c.select(clear=True)
            self._refresh()
            self.om.MGlobal.selectFromScreen(
                x - 2,
                y - 2,
                x + 2,
                y + 2,
                self.om.MGlobal.kReplaceList,
                self.om.MGlobal.kWireframeSelectMethod,
            )
            actual = c.ls(selection=True, objectsOnly=True, long=True) or []
            expected = {self.transforms[0], self.shapes[0]}
            valid = bool(actual) and all(path in expected for path in actual)
            checks.append({"screen": [x, y], "actual": actual, "valid": valid})
            if not valid:
                raise RuntimeError("Cube の辺を画面座標から選択できません")
        c.select(clear=True)

    def _remove_callbacks(self) -> None:
        for callback in self.callbacks:
            self.om.MMessage.removeCallback(callback)
        self.callbacks.clear()

    def finish(self, code: int) -> None:
        """結果保存後、専用 Maya に終了を要求する。"""
        self._remove_callbacks()
        try:
            profile_hashes = _profile_hashes(self.config)
            self.result["profile_file_sha256_after"] = profile_hashes
            if profile_hashes != self.config["profile_file_sha256"]:
                raise RuntimeError(
                    "測定中に専用 profile の設定ファイルが変更されました"
                )
            if self.config["plugin_path"]:
                hashes = {
                    "actual": _sha(Path(self.config["plugin_path"])),
                    "archive": _sha(Path(self.config["plugin_archive_path"])),
                }
                self.result["plugin_sha256_after"] = hashes
                if any(
                    value != self.config["plugin_sha256"]
                    for value in hashes.values()
                ):
                    raise RuntimeError(
                        "測定中に固定 DLL または証拠 archive が変更されました"
                    )
            else:
                self.result["plugin_sha256_after"] = None
        except (OSError, RuntimeError):
            self.result.update(
                status="failed", artifact_error=traceback.format_exc()
            )
            code = 1
        self.result["requested_exit_code"] = code
        self.result["termination_method"] = (
            "TerminateProcess current process; not graceful shutdown"
            if self.config["force_self_exit"]
            else "cmds.quit"
        )
        _write(self.output / "results.json", self.result)
        _write(
            self.output / "progress.json",
            {
                "status": self.result["status"],
                "requested_exit_code": code,
            },
        )
        if self.config["force_self_exit"]:
            _terminate_current_process(code)
        self.cmds.quit(force=True, exitCode=code)


def main() -> None:
    """`launch.ps1` が作成した設定で測定し、失敗も JSON に残す。"""
    config = json.loads(
        Path(os.environ["BD_FIXED_CUBE_CONFIG"]).read_text(encoding="utf-8")
    )
    benchmark = None
    trace_file = (Path(config["output_directory"]) / "python_stacks.log").open(
        "w"
    )
    faulthandler.enable(file=trace_file)
    faulthandler.dump_traceback_later(90, file=trace_file)
    _write(
        Path(config["output_directory"]) / "progress.json",
        {"status": "starting_benchmark"},
    )
    try:
        benchmark = CubeBenchmark(config)
        benchmark.run()
    except BaseException:
        error = traceback.format_exc()
        if benchmark is not None:
            benchmark.result.update(status="failed", error=error)
            benchmark.finish(1)
        else:
            _write(
                Path(config["output_directory"]) / "results.json",
                {
                    "status": "failed",
                    "error": error,
                    "requested_exit_code": 1,
                },
            )
            from maya import cmds

            if config["force_self_exit"]:
                _terminate_current_process(1)
            cmds.quit(force=True, exitCode=1)
        return
    benchmark.finish(0)


if __name__ == "__main__":
    try:
        from PySide6 import QtCore
    except ImportError:
        from PySide2 import QtCore
    QtCore.QTimer.singleShot(20000, main)
