"""実再生の描画バッファを、追加 refresh 前に取得して検証する。"""

from __future__ import annotations

import ctypes
import hashlib
from pathlib import Path
import traceback
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .benchmark import CubeBenchmark


def _read_buffer(
    benchmark: CubeBenchmark,
    name: str,
    frame: float,
    *,
    allow_blank: bool = False,
) -> dict:
    image = benchmark.om.MImage()
    benchmark.view.readColorBuffer(image, True)
    width, height = image.getSize()
    if width < 1 or height < 1:
        raise RuntimeError("再生 gate の描画バッファが空です")
    pixels = ctypes.string_at(image.pixels(), width * height * 4)
    non_background = 0
    foreground_colors = set()
    for index in range(0, len(pixels), 4):
        pixel = pixels[index : index + 4]
        if pixel != pixels[:4]:
            non_background += 1
            foreground_colors.add(pixel.hex())
    if not allow_blank and non_background < 8:
        raise RuntimeError("再生 gate の画像に描線がありません")
    path = Path(benchmark.output) / (name + ".png")
    image.writeToFile(str(path), "png")
    return {
        "frame": frame,
        "path": str(path),
        "size": [width, height],
        "non_background_pixels": non_background,
        "foreground_rgba_colors": sorted(foreground_colors),
        "rgba_sha256": hashlib.sha256(pixels).hexdigest(),
        "file_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "buffer_read_requested_refresh": False,
    }


def _refresh_read(
    benchmark: CubeBenchmark, name: str, *, force: bool = False
) -> dict:
    """対象viewのpostRender内で読み、別viewのGL contextを参照しない。"""
    c = benchmark.cmds
    c.modelEditor(benchmark.panel, edit=True, activeView=True)
    c.setFocus(benchmark.panel)
    captured = {}
    errors = []
    posts = 0
    attempts = 0

    def on_render(*unused: object) -> None:
        nonlocal posts
        posts += 1
        if captured or errors:
            return
        try:
            captured.update(
                _read_buffer(
                    benchmark,
                    name,
                    float(c.currentTime(query=True)),
                    allow_blank=True,
                )
            )
        except Exception:
            errors.append(traceback.format_exc())

    callback = benchmark.omui.MUiMessage.add3dViewPostRenderMsgCallback(
        benchmark.panel, on_render
    )
    benchmark.callbacks.append(callback)
    try:
        for attempts in (1, 2):
            if force:
                c.refresh(currentView=True, force=True)
            else:
                c.refresh(currentView=True)
            if captured or errors:
                break
            benchmark.application.processEvents()
            if captured or errors:
                break
    finally:
        benchmark.om.MMessage.removeCallback(callback)
        benchmark.callbacks.remove(callback)
    if errors or not captured:
        raise RuntimeError(
            f"表示 gate の{name}で対象viewのpostRender画像を取得できません "
            f"(force={force}, refreshes={attempts}, target_posts={posts}): "
            + "\n".join(errors)
        )
    captured.update(
        captured_from_target_post_render=True,
        requested_refresh_force=force,
        refresh_attempts=attempts,
        target_post_render_count=posts,
    )
    return captured


def _play_frames(benchmark: CubeBenchmark, name: str) -> dict:
    c = benchmark.cmds
    sequence = {
        "status": "running",
        "frames": {},
        "drawn_frames": [],
        "callback_errors": [],
    }
    benchmark.result["playback_gate"]["display_states"]["sequences"][
        name
    ] = sequence
    c.currentTime(1)
    c.refresh(currentView=True)
    benchmark._activate()
    sequence["before"] = benchmark._guard()

    def on_render(*unused: object) -> None:
        try:
            actual = float(c.currentTime(query=True))
            sequence["drawn_frames"].append(actual)
            frame = round(actual)
            if (
                frame not in (2, 9, 17)
                or abs(actual - frame) > 1e-6
                or str(frame) in sequence["frames"]
            ):
                return
            playing = bool(c.play(query=True, state=True))
            image = _read_buffer(
                benchmark,
                f"display_gate_{name}_frame_{frame:02d}_playback",
                actual,
                allow_blank=True,
            )
            sequence["frames"][str(frame)] = {
                "playback": image,
                "playing": playing,
            }
        except Exception:
            sequence["callback_errors"].append(traceback.format_exc())

    callback = benchmark.omui.MUiMessage.add3dViewPostRenderMsgCallback(
        benchmark.panel, on_render
    )
    benchmark.callbacks.append(callback)
    try:
        c.play(forward=True, wait=True)
    finally:
        benchmark.om.MMessage.removeCallback(callback)
        benchmark.callbacks.remove(callback)
        if c.play(query=True, state=True):
            c.play(state=False)
    sequence["after"] = benchmark._guard()
    if sequence["callback_errors"] or set(sequence["frames"]) != {
        "2",
        "9",
        "17",
    }:
        sequence["status"] = "failed"
        raise RuntimeError(f"表示 gate の{name}で再生画像を取得できません")
    if sequence["after"]["current_time"] != 17 or any(
        sequence["before"][key] != sequence["after"][key]
        for key in ("selection", "camera", "viewport")
    ):
        sequence["status"] = "failed"
        raise RuntimeError(f"表示 gate の{name}で再生条件が変わりました")
    sequence["status"] = "passed"
    return sequence


def _static_frames(
    benchmark: CubeBenchmark, name: str, sequence: dict
) -> None:
    for frame, record in sequence["frames"].items():
        benchmark.cmds.currentTime(int(frame))
        reference = _refresh_read(
            benchmark,
            f"display_gate_{name}_frame_{int(frame):02d}_static",
            force=True,
        )
        record["static_reference"] = reference
        record["same_rgba"] = (
            reference["size"] == record["playback"]["size"]
            and reference["frame"] == int(frame)
            and reference["rgba_sha256"] == record["playback"]["rgba_sha256"]
        )


def _display_states(benchmark: CubeBenchmark, report: dict) -> None:
    c = benchmark.cmds
    group, shape = benchmark.group, benchmark.shapes[0]
    states = {
        "status": "running",
        "captures": {},
        "checks": [],
        "sequences": {},
        "scope": (
            "Normal attribute/selection edits and refresh(currentView=True), "
            "without setGeometryDrawDirty. Static edits are captured inside "
            "the target postRender callback using normal refresh, with up to "
            "two requests. Playback buffers are captured before any reference "
            "refresh. Post-playback static references use force=True and are "
            "also captured inside target postRender. This is not performance timing."
        ),
        "overridePlayback_scope": (
            "overridePlayback is an ability-to-animate override, not hideOnPlayback. "
            "This fixed-shape fixture animates its parent transform; the curve "
            "control remains visible when overridePlayback is false."
        ),
    }
    report["display_states"] = states
    blank_hash = report["scene"]["blank_image"]["rgba_sha256"]

    def check(name: str, condition: bool) -> None:
        states["checks"].append({"name": name, "passed": bool(condition)})

    def capture(name: str, *, blank: bool = False) -> dict:
        image = _refresh_read(
            benchmark,
            "display_gate_" + name,
        )
        states["captures"][name] = image
        check(
            name + ("_blank" if blank else "_nonempty"),
            (
                (
                    image["rgba_sha256"] == blank_hash
                    and image["non_background_pixels"] == 0
                )
                if blank
                else image["non_background_pixels"] >= 8
            ),
        )
        return image

    def same(name: str, first: dict, second: dict) -> None:
        check(name, first["rgba_sha256"] == second["rgba_sha256"])

    def changed(name: str, first: dict, second: dict) -> None:
        check(name, first["rgba_sha256"] != second["rgba_sha256"])

    def delete_animation(node: str, attributes: list[str]) -> None:
        curves = set()
        for attribute in attributes:
            curves.update(
                c.listConnections(
                    node + "." + attribute,
                    source=True,
                    destination=False,
                    type="animCurve",
                )
                or []
            )
        if curves:
            c.delete(list(curves))

    try:
        c.currentTime(9)
        c.select(clear=True)
        baseline = capture("baseline_unselected")
        c.select(group, replace=True)
        selected = capture("selected")
        changed("selection_changes_color", selected, baseline)
        c.select(clear=True)
        same("unselect_restores", capture("unselected_restored"), baseline)

        c.setAttr(shape + ".overrideColorRGB", 0.15, 0.65, 0.25)
        changed("shape_rgb_changes", capture("shape_rgb_changed"), baseline)
        c.setAttr(shape + ".overrideColorRGB", 0.8, 0.8, 0.8)
        same("shape_rgb_restores", capture("shape_rgb_restored"), baseline)
        c.setAttr(group + ".visibility", False)
        capture("parent_visibility_off", blank=True)
        c.setAttr(group + ".visibility", True)
        same(
            "parent_visibility_restores",
            capture("parent_visibility_on"),
            baseline,
        )

        c.setAttr(shape + ".overrideEnabled", False)
        c.setAttr(group + ".overrideEnabled", True)
        c.setAttr(group + ".overrideRGBColors", True)
        c.setAttr(group + ".overrideColorRGB", 0.8, 0.8, 0.8)
        inherited = capture("parent_override_normal")
        same("parent_rgb_matches_shape_rgb", inherited, baseline)
        c.setAttr(group + ".template", True)
        changed(
            "parent_template_changes", capture("parent_template_on"), inherited
        )
        c.setAttr(group + ".template", False)
        same(
            "parent_template_restores",
            capture("parent_template_off"),
            inherited,
        )
        c.setAttr(group + ".overrideDisplayType", 2)
        changed(
            "parent_reference_changes",
            capture("parent_reference_on"),
            inherited,
        )
        c.setAttr(group + ".overrideDisplayType", 0)
        same(
            "parent_reference_restores",
            capture("parent_reference_off"),
            inherited,
        )
        c.setAttr(group + ".overrideEnabled", False)

        layer = c.createDisplayLayer(name="fixedCubeStateLayer", empty=True)
        try:
            c.editDisplayLayerMembers(layer, group, noRecurse=True)
            c.setAttr(layer + ".overrideRGBColors", True)
            c.setAttr(layer + ".overrideColorRGB", 0.8, 0.8, 0.8)
            c.select(clear=True)
            layer_base = capture("layer_normal")
            same("layer_rgb_matches_shape_rgb", layer_base, baseline)
            c.setAttr(layer + ".visibility", False)
            capture("layer_visibility_off", blank=True)
            c.setAttr(layer + ".visibility", True)
            same(
                "layer_visibility_restores",
                capture("layer_visibility_on"),
                layer_base,
            )
            for value, label in ((1, "template"), (2, "reference")):
                c.setAttr(layer + ".displayType", value)
                changed(
                    "layer_" + label + "_changes",
                    capture("layer_" + label + "_on"),
                    layer_base,
                )
                c.setAttr(layer + ".displayType", 0)
                same(
                    "layer_" + label + "_restores",
                    capture("layer_" + label + "_off"),
                    layer_base,
                )
            c.setAttr(layer + ".overrideColorRGB", 0.65, 0.18, 0.45)
            changed(
                "layer_rgb_changes", capture("layer_rgb_changed"), layer_base
            )
            c.setAttr(layer + ".overrideColorRGB", 0.8, 0.8, 0.8)
            same(
                "layer_rgb_restores", capture("layer_rgb_restored"), layer_base
            )
            c.setAttr(layer + ".overrideRGBColors", False)
            c.setAttr(layer + ".color", 13)
            changed(
                "layer_index_color_changes",
                capture("layer_index_color"),
                layer_base,
            )
            c.setAttr(layer + ".overrideRGBColors", True)
            same(
                "layer_index_color_restores",
                capture("layer_index_color_restored"),
                layer_base,
            )
        finally:
            c.delete(layer)
        c.setAttr(group + ".overrideEnabled", False)
        c.setAttr(shape + ".overrideEnabled", True)
        same("layer_removal_restores", capture("layer_removed"), baseline)

        c.select(group, replace=True)
        selected = capture("highlight_on")
        c.modelEditor(benchmark.panel, edit=True, selectionHiliteDisplay=False)
        same(
            "highlight_off_matches_unselected",
            capture("highlight_off"),
            baseline,
        )
        c.modelEditor(benchmark.panel, edit=True, selectionHiliteDisplay=True)
        same("highlight_on_restores", capture("highlight_restored"), selected)
        c.select(clear=True)
        same(
            "highlight_unselect_restores",
            capture("highlight_unselected"),
            baseline,
        )

        for attribute, tested_value, normal_value, hides_during_playback in (
            ("overridePlayback", False, True, False),
            ("hideOnPlayback", True, False, True),
        ):
            c.currentTime(9)
            c.setAttr(shape + "." + attribute, tested_value)
            same(
                attribute + "_visible_while_stopped",
                capture(attribute + "_stopped"),
                baseline,
            )
            sequence = _play_frames(benchmark, attribute)
            states["sequences"][attribute] = sequence
            for frame, record in sequence["frames"].items():
                if frame in ("2", "9"):
                    check(attribute + "_playing_" + frame, record["playing"])
                hidden = record["playback"]["rgba_sha256"] == blank_hash
                check(
                    attribute + "_visibility_" + frame,
                    hidden == (hides_during_playback and record["playing"]),
                )
                if not hides_during_playback:
                    check(
                        attribute + "_nonempty_" + frame,
                        record["playback"]["non_background_pixels"] >= 8,
                    )
            if not hides_during_playback:
                _static_frames(benchmark, attribute, sequence)
                for frame, record in sequence["frames"].items():
                    check(
                        attribute + "_static_match_" + frame,
                        record["same_rgba"],
                    )
            c.currentTime(9)
            c.setAttr(shape + "." + attribute, normal_value)
            same(
                attribute + "_restores",
                capture(attribute + "_restored"),
                baseline,
            )
            restored_sequence = _play_frames(
                benchmark, attribute + "_restored"
            )
            states["sequences"][attribute + "_restored"] = restored_sequence
            _static_frames(
                benchmark, attribute + "_restored", restored_sequence
            )
            for frame, record in restored_sequence["frames"].items():
                check(
                    attribute + "_restored_nonempty_" + frame,
                    record["playback"]["non_background_pixels"] >= 8,
                )
                check(
                    attribute + "_restored_static_match_" + frame,
                    record["same_rgba"],
                )

        for frame, value in ((1, False), (2, False), (9, True), (17, False)):
            c.setKeyframe(
                group, attribute="visibility", time=frame, value=value
            )
        c.keyTangent(group, attribute="visibility", outTangentType="step")
        try:
            sequence = _play_frames(benchmark, "animated_visibility")
            states["sequences"]["animated_visibility"] = sequence
            _static_frames(benchmark, "animated_visibility", sequence)
            for frame, record in sequence["frames"].items():
                check(
                    "animated_visibility_static_match_" + frame,
                    record["same_rgba"],
                )
                check(
                    "animated_visibility_expected_" + frame,
                    (record["playback"]["rgba_sha256"] == blank_hash)
                    == (frame != "9"),
                )
                if frame == "9":
                    check(
                        "animated_visibility_frame_9_nonempty",
                        record["playback"]["non_background_pixels"] >= 8,
                    )
        finally:
            delete_animation(group, ["visibility"])
            c.setAttr(group + ".visibility", True)

        children = c.attributeQuery(
            "overrideColorRGB", node=shape, listChildren=True
        )
        if len(children) != 3:
            raise RuntimeError("overrideColorRGBの3子属性を取得できません")
        states["animated_color_attributes"] = children
        for frame, color in (
            (1, (1, 0, 0)),
            (2, (1, 0, 0)),
            (9, (0, 1, 0)),
            (17, (0, 0, 1)),
        ):
            for child, value in zip(children, color):
                c.setKeyframe(shape, attribute=child, time=frame, value=value)
        c.keyTangent(
            shape,
            attribute=children,
            inTangentType="linear",
            outTangentType="linear",
        )
        try:
            sequence = _play_frames(benchmark, "animated_rgb")
            states["sequences"]["animated_rgb"] = sequence
            _static_frames(benchmark, "animated_rgb", sequence)
            palettes = set()
            for frame, record in sequence["frames"].items():
                check(
                    "animated_rgb_static_match_" + frame, record["same_rgba"]
                )
                check(
                    "animated_rgb_nonempty_" + frame,
                    record["playback"]["non_background_pixels"] >= 8,
                )
                palettes.add(
                    tuple(record["playback"]["foreground_rgba_colors"])
                )
            check("animated_rgb_three_distinct_palettes", len(palettes) == 3)
        finally:
            c.currentTime(9)
            delete_animation(shape, children)
            c.setAttr(shape + ".overrideColorRGB", 0.8, 0.8, 0.8)
        same("all_display_states_restore", capture("all_restored"), baseline)
        states["after"] = benchmark._guard()
        failures = [
            item["name"] for item in states["checks"] if not item["passed"]
        ]
        if failures:
            raise RuntimeError(
                "表示 gate の検証に失敗しました: " + ", ".join(failures)
            )
        states["status"] = "passed"
    except Exception:
        states.update(status="failed", error=traceback.format_exc())
        raise


def run(benchmark: CubeBenchmark) -> None:
    """再生3姿勢と表示状態の変化を画像取得し、復元と静止描画を検証する。

    Args:
        benchmark: 初期化済みの`CubeBenchmark`。専用シーンを作り、結果を
            `result["playback_gate"]`へ保存します。描画読取と画像保存の負荷を
            含むため、この処理の所要時間は性能値に使用しません。

    Raises:
        RuntimeError: 必要なframeが描画されない、姿勢間の画像が変わらない、
            再生画像と静止参照が一致しない、または表示状態が追従しない場合。
    """
    c = benchmark.cmds
    expected_frames = (2, 9, 17)
    report = {
        "status": "running",
        "mode": benchmark.config["mode"],
        "expected_frames": list(expected_frames),
        "child_rotate_xyz_degrees": [12, 22, 8],
        "parent_rotate_y_keys": [[1, -30], [9, 0], [17, 30]],
        "drawn_frames": [],
        "frames": {},
        "callback_errors": [],
        "scope": (
            "Functional gate outside performance timing. The target view's "
            "postRender callback reads the existing buffer without requesting "
            "refresh. Readback and PNG writes affect playback duration. "
            "Forced-refresh references are collected only after playback. "
            "Compare matching frame RGBA hashes with a separate curve-mode run."
        ),
    }
    benchmark.result["playback_gate"] = report
    try:
        scene = benchmark._scene(1, "playback_gate_scene")
        report["scene"] = scene
        c.setAttr(benchmark.transforms[0] + ".rotate", 12, 22, 8)
        for frame, value in report["parent_rotate_y_keys"]:
            c.setKeyframe(
                benchmark.group,
                attribute="rotateY",
                time=frame,
                value=value,
            )
        c.keyTangent(
            benchmark.group,
            attribute="rotateY",
            inTangentType="linear",
            outTangentType="linear",
        )
        c.playbackOptions(
            minTime=1,
            maxTime=17,
            animationStartTime=1,
            animationEndTime=17,
            loop="once",
            playbackSpeed=0,
            maxPlaybackSpeed=0,
            view="active",
            by=1,
        )
        c.select(benchmark.group, replace=True)
        c.currentTime(1)
        benchmark._refresh()
        benchmark._activate()
        report["before"] = benchmark._guard()

        def on_render(*unused: object) -> None:
            try:
                actual_frame = float(c.currentTime(query=True))
                report["drawn_frames"].append(actual_frame)
                frame = round(actual_frame)
                if (
                    frame not in expected_frames
                    or abs(actual_frame - frame) > 1e-6
                    or str(frame) in report["frames"]
                ):
                    return
                captured = _read_buffer(
                    benchmark,
                    f"playback_gate_frame_{frame:02d}_playback",
                    actual_frame,
                )
                report["frames"][str(frame)] = {"playback": captured}
            except Exception:
                report["callback_errors"].append(traceback.format_exc())

        callback = benchmark.omui.MUiMessage.add3dViewPostRenderMsgCallback(
            benchmark.panel, on_render
        )
        benchmark.callbacks.append(callback)
        try:
            c.play(forward=True, wait=True)
        finally:
            benchmark.om.MMessage.removeCallback(callback)
            benchmark.callbacks.remove(callback)
            if c.play(query=True, state=True):
                c.play(state=False)
        report["after"] = benchmark._guard()
        if report["callback_errors"]:
            raise RuntimeError(
                "再生 gate の postRender 画像取得に失敗しました"
            )
        if set(report["frames"]) != {str(frame) for frame in expected_frames}:
            raise RuntimeError("再生 gate でframe 2 / 9 / 17を取得できません")
        if report["after"]["current_time"] != 17:
            raise RuntimeError("再生 gate がframe 17へ到達しませんでした")
        if any(
            report["before"][key] != report["after"][key]
            for key in ("selection", "camera", "viewport")
        ):
            raise RuntimeError("再生 gate 中に表示条件が変わりました")
        hashes = {
            record["playback"]["rgba_sha256"]
            for record in report["frames"].values()
        }
        report["distinct_playback_pose_hashes"] = len(hashes)
        if len(hashes) != len(expected_frames):
            raise RuntimeError("再生 gate の3姿勢が異なる画像になりません")

        # 再生画像を全て取得し、callbackを外してから静止参照を作る。
        for frame in expected_frames:
            c.currentTime(frame)
            reference = _refresh_read(
                benchmark,
                f"playback_gate_frame_{frame:02d}_static",
                force=True,
            )
            record = report["frames"][str(frame)]
            record["static_reference"] = reference
            record["bounds"] = benchmark._bounds()
            record["same_rgba"] = (
                reference["size"] == record["playback"]["size"]
                and reference["rgba_sha256"]
                == record["playback"]["rgba_sha256"]
            )
            if not record["same_rgba"]:
                raise RuntimeError(
                    f"再生 gate のframe {frame}が静止参照と一致しません"
                )
        report["reference_after"] = benchmark._guard()
        _display_states(benchmark, report)
        report["status"] = "passed"
    except Exception:
        report.update(status="failed", error=traceback.format_exc())
        raise
