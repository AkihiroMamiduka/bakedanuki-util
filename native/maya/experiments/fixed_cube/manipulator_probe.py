"""実マウス操作中の Cube 描画と変換を記録する診断用 UI。"""

from __future__ import annotations

import faulthandler
import importlib.util
import json
import math
import os
from pathlib import Path
import statistics
import time
import traceback

_probe = None
_trace_file = None


class ManipulatorProbe:
    """Start と Finish の間の描画通知を保存し、専用 Maya を終了する。"""

    def __init__(self, benchmark, helpers) -> None:
        self.benchmark = benchmark
        self.helpers = helpers
        self.cmds = benchmark.cmds
        self.active = None
        self.closed = False
        self.case = "group"
        self.report = {
            "kind": "manual_manipulator_diagnostic",
            "input_method": "External real mouse operation; this script does not inject input.",
            "interpretation": (
                "Start-to-Finish includes idle, focus and button handling. Post-render "
                "intervals include input pacing and callback overhead; neither is FPS "
                "or GPU render time. Profiler-enabled runs are separate diagnostics. "
                "Mouse-button observations do not independently prove input provenance."
            ),
            "trials": [],
        }
        benchmark.result["interpretation"] = self.report["interpretation"]
        benchmark.result["manipulator_probe"] = self.report
        benchmark._scene(1000, "manipulator_1000")
        # file(new) 後の通常ペインも記録し、専用 view 以外の描画を避ける。
        if self.cmds.paneLayout("viewPanes", exists=True):
            self.cmds.paneLayout("viewPanes", edit=True, manage=False)
        self.original_translation = self.cmds.getAttr(
            benchmark.transforms[0] + ".translate"
        )[0]
        benchmark.callbacks.append(
            benchmark.omui.MUiMessage.add3dViewPostRenderMsgCallback(
                benchmark.panel, self._on_render
            )
        )
        self._create_ui()
        self._prepare_case()

    def _create_ui(self) -> None:
        probe = self
        qt = self.benchmark.QtWidgets

        class ProbeDialog(qt.QDialog):
            def closeEvent(self, event) -> None:
                if not probe.closed:
                    event.ignore()
                    probe._perform(probe._cancel)
                    return
                event.accept()

        self.dialog = ProbeDialog(self.benchmark.widget)
        self.dialog.rejected.connect(lambda: self._perform(self._cancel))
        self.dialog.setWindowTitle("Cube manual move diagnostic")
        self.dialog.setWindowFlags(
            self.dialog.windowFlags() | self.benchmark.QtCore.Qt.Tool
        )
        layout = qt.QVBoxLayout(self.dialog)
        self.selector = qt.QComboBox()
        self.selector.addItems(["group", "individual"])
        self.selector.currentTextChanged.connect(
            lambda unused: self._perform(self._prepare_case)
        )
        layout.addWidget(self.selector)
        self.label = qt.QLabel(
            "Select a target, Start, drag a move handle, then Finish.\n"
            "Complete both targets before Save & Exit. No FPS is measured."
        )
        layout.addWidget(self.label)
        self.start_button = qt.QPushButton("Start")
        self.start_button.clicked.connect(lambda: self._perform(self._start))
        layout.addWidget(self.start_button)
        self.finish_button = qt.QPushButton("Finish")
        self.finish_button.setEnabled(False)
        self.finish_button.clicked.connect(lambda: self._perform(self._finish))
        layout.addWidget(self.finish_button)
        self.exit_button = qt.QPushButton("Save & Exit")
        self.exit_button.setEnabled(False)
        self.exit_button.clicked.connect(
            lambda: self._perform(self._save_exit)
        )
        layout.addWidget(self.exit_button)
        self.dialog.adjustSize()
        view_rect = self.benchmark.widget.frameGeometry()
        screen = self.benchmark.widget.screen().availableGeometry()
        x = min(view_rect.right() + 12, screen.right() - self.dialog.width())
        self.dialog.move(max(screen.left(), x), screen.top() + 40)
        self.dialog.show()

    def _perform(self, action) -> None:
        if self.closed:
            return
        try:
            action()
        except BaseException:
            error = traceback.format_exc()
            if (
                self.report["trials"]
                and self.report["trials"][-1]["status"] == "recording"
            ):
                self.report["trials"][-1].update(status="failed", error=error)
            self.benchmark.result.update(status="failed", error=error)
            self._shutdown(1)

    def _persist(self, status: str) -> None:
        self.helpers._write(
            self.benchmark.output / "results.json", self.benchmark.result
        )
        self.helpers._write(
            self.benchmark.output / "progress.json",
            {"status": status, "case": self.case, "pid": os.getpid()},
        )

    def _prepare_case(self) -> None:
        if self.active is not None:
            raise RuntimeError("記録中に対象を切り替えることはできません")
        b, c = self.benchmark, self.cmds
        self.case = self.selector.currentText()
        c.setAttr(b.group + ".translate", 0, 0, 0)
        c.setAttr(b.transforms[0] + ".translate", *self.original_translation)
        self.target = b.group if self.case == "group" else b.transforms[0]
        selection = b.om.MSelectionList()
        selection.add(self.target)
        self.target_path = selection.getDagPath(0)
        self.target_fn = b.om.MFnTransform(self.target_path)
        c.select(self.target, replace=True)
        c.setToolTo("moveSuperContext")
        b._activate()
        b._refresh()
        self.label.setText(
            f"Ready: {self.case}\nStart, drag a move handle, then Finish."
        )
        self._persist("manipulator_ready")

    def _target_state(self) -> dict:
        return {
            "translate": list(
                self.target_fn.translation(self.benchmark.om.MSpace.kTransform)
            ),
            "world_matrix": list(self.target_path.inclusiveMatrix()),
        }

    def _scene_state(self) -> dict:
        b = self.benchmark
        result = {}
        for name in [b.group, *b.transforms]:
            selection = b.om.MSelectionList()
            selection.add(name)
            path = selection.getDagPath(0)
            fn = b.om.MFnTransform(path)
            result[name] = {
                "local_matrix": list(fn.transformation().asMatrix()),
                "world_matrix": list(path.inclusiveMatrix()),
            }
        return result

    def _guard(self) -> dict:
        record = self.benchmark._guard()
        control = self.dialog.frameGeometry()
        record.update(
            active_tool=self.cmds.currentCtx(),
            move_mode=self.cmds.manipMoveContext(
                "Move", query=True, mode=True
            ),
            main_view_panes_managed=(
                bool(
                    self.cmds.paneLayout("viewPanes", query=True, manage=True)
                )
                if self.cmds.paneLayout("viewPanes", exists=True)
                else None
            ),
            control_window_geometry=[
                control.x(),
                control.y(),
                control.width(),
                control.height(),
            ],
        )
        if record["active_tool"] != "moveSuperContext":
            raise RuntimeError("Move tool が有効ではありません")
        if record["selection"] != [self.target]:
            raise RuntimeError("選択対象が診断対象と異なります")
        if record["main_view_panes_managed"]:
            raise RuntimeError("通常 view ペインが再表示されています")
        return record

    def _start(self) -> None:
        b, c = self.benchmark, self.cmds
        if self.active is not None:
            raise RuntimeError("既に記録中です")
        b._activate()
        index = len(self.report["trials"]) + 1
        prefix = f"manipulator_{index:02d}_{self.case}"
        before_image = b._capture(prefix + "_before")
        record = {
            "trial": index,
            "case": self.case,
            "target": self.target,
            "status": "recording",
            "before_image": before_image,
            "before_scene": self._scene_state(),
            "before_target": self._target_state(),
            "before_guard": self._guard(),
            "post_renders": [],
            "callback_errors": [],
            "maya_profile": None,
            "native_profile": None,
        }
        self.report["trials"].append(record)
        self.selector.setEnabled(False)
        self.start_button.setEnabled(False)
        self.exit_button.setEnabled(False)
        self.finish_button.setEnabled(True)
        self.label.setText(
            f"Recording: {self.case}\nDrag a move handle, then Finish."
        )
        self._persist("manipulator_recording")
        # UI 更新と証拠の保存を済ませてから診断区間を開始する。
        if b.config.get("native_profile"):
            c.bdCubeProfile(reset=True)
        if b.config.get("maya_profile"):
            c.profiler(reset=True)
            c.profiler(bufferSize=64)
            c.profiler(sampling=True)
        record["started_perf_counter_ns"] = time.perf_counter_ns()
        record["started_unix_ns"] = time.time_ns()
        self.active = record

    def _on_render(self, *unused) -> None:
        record = self.active
        if record is None:
            return
        timestamp = time.perf_counter_ns()
        try:
            b = self.benchmark
            buttons = b.application.mouseButtons()
            record["post_renders"].append(
                {
                    "perf_counter_ns": timestamp,
                    "elapsed_seconds": (
                        timestamp - record["started_perf_counter_ns"]
                    )
                    / 1e9,
                    "mouse_buttons": int(getattr(buttons, "value", buttons)),
                    "viewport": [b.view.portWidth(), b.view.portHeight()],
                    "active_view": int(b.omui.M3dView.active3dView().widget())
                    == int(b.view.widget()),
                    "application_active": b.application.applicationState()
                    == b.QtCore.Qt.ApplicationActive,
                    "camera": b.view.getCamera().fullPathName(),
                    "active_tool": self.cmds.currentCtx(),
                    **self._target_state(),
                }
            )
        except BaseException:
            record["callback_errors"].append(traceback.format_exc())

    @staticmethod
    def _changed(first: list, second: list) -> bool:
        return any(abs(a - b) > 1e-8 for a, b in zip(first, second))

    def _finish(self) -> None:
        b, c = self.benchmark, self.cmds
        record = self.active
        if record is None:
            raise RuntimeError("記録が開始されていません")
        record["finished_perf_counter_ns"] = time.perf_counter_ns()
        record["finished_unix_ns"] = time.time_ns()
        self.active = None
        if b.config.get("maya_profile"):
            c.profiler(sampling=False)
        if b.config.get("native_profile"):
            record["native_profile"] = json.loads(c.bdCubeProfile())
        prefix = f"manipulator_{record['trial']:02d}_{self.case}"
        if b.config.get("maya_profile"):
            path = b.output / (prefix + ".profiler")
            c.profiler(output=str(path))
            record["maya_profile"] = {
                "path": str(path),
                "sha256": self.helpers._sha(path),
                "events": c.profiler(query=True, eventCount=True),
            }
        # Finish ボタンへの移動後に対象 view を再有効化し、計測外で画像を読む。
        record["after_guard_before_reactivation"] = b._guard(check=False)
        b._activate()
        record["after_guard"] = self._guard()
        record["after_target"] = self._target_state()
        record["after_scene"] = self._scene_state()
        record["after_image"] = b._capture(prefix + "_after")
        record["wall_seconds_including_idle"] = (
            record["finished_perf_counter_ns"]
            - record["started_perf_counter_ns"]
        ) / 1e9
        samples = record["post_renders"]
        intervals = [
            (right["perf_counter_ns"] - left["perf_counter_ns"]) / 1e6
            for left, right in zip(samples, samples[1:])
        ]
        record["post_render_intervals_ms"] = intervals
        record["median_post_render_interval_ms"] = (
            statistics.median(intervals) if intervals else None
        )
        record["post_render_count"] = len(samples)
        record["translation_delta"] = [
            a - z
            for a, z in zip(
                record["after_target"]["translate"],
                record["before_target"]["translate"],
            )
        ]
        record["translation_distance"] = math.sqrt(
            sum(value * value for value in record["translation_delta"])
        )
        record["changed_local_nodes"] = []
        record["changed_world_nodes"] = []
        for name, before in record["before_scene"].items():
            after = record["after_scene"][name]
            for space in ("local", "world"):
                if self._changed(
                    before[space + "_matrix"], after[space + "_matrix"]
                ):
                    record[f"changed_{space}_nodes"].append(name)
        previous = record["before_target"]["translate"]
        changes = 0
        for sample in samples:
            changes += self._changed(previous, sample["translate"])
            previous = sample["translate"]
        record["observed_translation_changes"] = changes
        self._persist("manipulator_validating")
        expected_world = (
            {b.group, *b.transforms} if self.case == "group" else {self.target}
        )
        if (
            record["callback_errors"]
            or len(samples) < 2
            or changes < 1
            or record["translation_distance"] <= 1e-8
            or set(record["changed_local_nodes"]) != {self.target}
            or set(record["changed_world_nodes"]) != expected_world
        ):
            raise RuntimeError(
                "描画通知または対象ノードの移動を確認できません"
            )
        for key in (
            "viewport",
            "camera",
            "selection",
            "active_tool",
            "move_mode",
            "current_time",
        ):
            if record["before_guard"][key] != record["after_guard"][key]:
                raise RuntimeError(f"操作中に {key} が変化しました")
        if any(
            sample["viewport"] != record["before_guard"]["viewport"]
            or not sample["active_view"]
            or not sample["application_active"]
            or sample["camera"] != record["before_guard"]["camera"]
            or sample["active_tool"] != "moveSuperContext"
            for sample in samples
        ):
            raise RuntimeError("postRender 時の view / tool が変化しました")
        record["status"] = "passed"
        self.selector.setEnabled(True)
        self.start_button.setEnabled(True)
        self.finish_button.setEnabled(False)
        complete = {
            item["case"]
            for item in self.report["trials"]
            if item["status"] == "passed"
        }
        self.exit_button.setEnabled(complete == {"group", "individual"})
        self.label.setText(
            f"Saved: {self.case}; {len(samples)} renders, {changes} movement updates.\n"
            "Select the other target, or Save & Exit after both."
        )
        self._persist("manipulator_trial_saved")

    def _save_exit(self) -> None:
        completed = {
            record["case"]
            for record in self.report["trials"]
            if record["status"] == "passed"
        }
        if self.active is not None or completed != {"group", "individual"}:
            raise RuntimeError("group と individual の記録を完了してください")
        if self.benchmark.config.get("native_profile"):
            self.cmds.bdCubeProfile(reset=True)
            self.cmds.bdCubeProfile(dirty=True)
            self.benchmark._activate()
            self.benchmark._refresh()
            control = json.loads(self.cmds.bdCubeProfile())
            self.report["native_profile_control"] = control
            if not control["updateRenderItems"]["calls"]:
                raise RuntimeError("診断カウンターの対照試験が失敗しました")
        self.benchmark.result["status"] = "passed"
        self._shutdown(0)

    def _cancel(self) -> None:
        self.benchmark.result.update(
            status="failed", error="Manual probe cancelled before Save & Exit."
        )
        self._shutdown(1)

    def _shutdown(self, code: int) -> None:
        if self.closed:
            return
        self.closed = True
        self.active = None
        try:
            self.cmds.profiler(sampling=False)
            if (
                self.helpers._sha(Path(__file__))
                != self.benchmark.config["manipulator_probe_sha256"]
            ):
                raise RuntimeError("Manipulator probe SHA256 changed.")
        except BaseException:
            self.benchmark.result.update(
                status="failed", shutdown_error=traceback.format_exc()
            )
            code = 1
        finally:
            try:
                self.dialog.hide()
            except BaseException:
                self.benchmark.result.update(
                    status="failed",
                    dialog_cleanup_error=traceback.format_exc(),
                )
                code = 1
            finally:
                self.benchmark.finish(code)


def main() -> None:
    """archive 内のハーネスを検証し、手動操作用 UI を開く。"""
    global _probe, _trace_file
    config = json.loads(
        Path(os.environ["BD_FIXED_CUBE_CONFIG"]).read_text(encoding="utf-8")
    )
    spec = importlib.util.spec_from_file_location(
        "cube_manipulator_benchmark", Path(__file__).with_name("benchmark.py")
    )
    helpers = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helpers)
    _trace_file = (
        Path(config["output_directory"]) / "python_stacks.log"
    ).open("w")
    faulthandler.enable(file=_trace_file)
    benchmark = None
    try:
        if not config.get("manipulator_probe") or config["counts"] != [1000]:
            raise RuntimeError("ManipulatorProbe は1000 nodes専用です")
        if helpers._sha(Path(__file__)) != config["manipulator_probe_sha256"]:
            raise RuntimeError("Manipulator probe の SHA256 が異なります")
        benchmark = helpers.CubeBenchmark(config)
        _probe = ManipulatorProbe(benchmark, helpers)
    except BaseException:
        error = traceback.format_exc()
        if benchmark is not None:
            benchmark.result.update(status="failed", error=error)
            benchmark.finish(1)
        else:
            helpers._write(
                Path(config["output_directory"]) / "results.json",
                {"status": "failed", "error": error, "requested_exit_code": 1},
            )
            from maya import cmds

            if config["force_self_exit"]:
                helpers._terminate_current_process(1)
            cmds.quit(force=True, exitCode=1)


if __name__ == "__main__":
    try:
        from PySide6 import QtCore
    except ImportError:
        from PySide2 import QtCore
    QtCore.QTimer.singleShot(20000, main)
