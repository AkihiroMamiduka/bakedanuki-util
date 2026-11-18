"""キャッシュ復元中の描画を検証し、同じシーンで操作・再生を測る。"""

from __future__ import annotations

import faulthandler
import json

_SAMPLE_FRAMES = (2, 9, 17)


def _configure_cache(benchmark, mode, fill_mode):
    from maya.plugin.evaluator.CacheEvaluatorManager import (
        CACHE_STANDARD_MODE_EVAL,
        CACHE_STANDARD_MODE_VP2_HW,
        CACHE_STANDARD_MODE_VP2_SW,
    )

    cmds = benchmark.cmds
    cmds.evaluator(name="cache", enable=False)
    benchmark.expected_cache_enabled = mode != "off"
    if mode == "off":
        return
    rules = {
        "evaluation": CACHE_STANDARD_MODE_EVAL,
        "software": CACHE_STANDARD_MODE_VP2_SW,
        "hardware": CACHE_STANDARD_MODE_VP2_HW,
    }[mode]
    cmds.cacheEvaluator(resetRules=True)
    for rule in rules:
        cmds.cacheEvaluator(**rule)
    cmds.cacheEvaluator(cacheFillMode=fill_mode)
    cmds.evaluator(name="cache", enable=True)
    cmds.cacheEvaluator(flushCache="destroy", flushCacheSync=True)


def _cache_state(benchmark):
    cmds = benchmark.cmds
    if not benchmark.expected_cache_enabled:
        return {"cached_frames": [], "points": [], "safe_mode": False}
    return {
        "cached_frames": cmds.cacheEvaluator(query=True, cachedFrames=True)
        or [],
        "points": cmds.cacheEvaluator(query=True, cachingPoints=True) or [],
        "safe_mode": bool(
            int(cmds.cacheEvaluator(query=True, safeModeTriggered=True))
        ),
        "safe_mode_messages": cmds.cacheEvaluator(
            query=True, safeModeMessages=True
        ),
        "fill_mode": cmds.cacheEvaluator(query=True, cacheFillMode=True),
    }


def _covered(state, frames):
    ranges = state["cached_frames"]
    if ranges and isinstance(ranges[0], (tuple, list)):
        ranges = [value for triplet in ranges for value in triplet]
    if len(ranges) % 3:
        raise RuntimeError(f"キャッシュ範囲の形式が不正です: {ranges}")
    return not state["safe_mode"] and all(
        any(
            status & 1 and first <= frame <= last
            for status, first, last in zip(
                ranges[::3], ranges[1::3], ranges[2::3]
            )
        )
        for frame in frames
    )


def _playback_range(cmds, last):
    cmds.playbackOptions(
        minTime=1,
        maxTime=last,
        animationStartTime=1,
        animationEndTime=last,
        loop="once",
        playbackSpeed=0,
        maxPlaybackSpeed=0,
        view="active",
        by=1,
    )


def _play(benchmark, images, label, matrix_path=None):
    cmds = benchmark.cmds
    cmds.currentTime(1)
    benchmark._activate()
    result = {
        "before": benchmark._guard()["cache_state"],
        "frames": {},
        "draws": [],
        "errors": [],
    }

    def posted(*_):
        try:
            frame = cmds.currentTime(query=True)
            result["draws"].append(frame)
            if frame not in _SAMPLE_FRAMES or int(frame) in result["frames"]:
                return
            record = images._read_buffer(
                benchmark, f"{label}_{int(frame):02}", frame
            )
            if matrix_path is not None:
                # 行列照会が評価を起こす場合に備え、描画確認の再生とは分ける。
                record["world_matrix"] = list(matrix_path.inclusiveMatrix())
            result["frames"][int(frame)] = record
        except Exception as error:
            result["errors"].append(repr(error))

    callback = benchmark.omui.MUiMessage.add3dViewPostRenderMsgCallback(
        benchmark.panel, posted
    )
    try:
        cmds.play(forward=True, wait=True)
    finally:
        benchmark.om.MMessage.removeCallback(callback)
        if cmds.play(query=True, state=True):
            cmds.play(state=False)
    after = benchmark._guard()
    result["after"] = after["cache_state"]
    result["last_frame"] = after["current_time"]
    return result


def _probe(benchmark, images, metadata):
    cmds = benchmark.cmds
    reports = benchmark.result["cached_playback"] = []
    modes = metadata.get("cache_modes", ["evaluation"])
    fill_mode = metadata.get("fill_mode", "syncOnly")
    failures = []
    for target in metadata.get("targets", ["group", "individual"]):
        benchmark.expected_cache_enabled = False
        benchmark._scene(1, f"cached_playback_{target}")
        benchmark._orbit(18)
        # 計測用 panel だけを表示し、その描画バッファを読む。
        if cmds.paneLayout("viewPanes", exists=True):
            cmds.paneLayout("viewPanes", edit=True, manage=False)
        if metadata.get("adjusted", False):
            shape = benchmark.shapes[0]
            cmds.setAttr(f"{shape}.shape1stAxis", 2)
            cmds.setAttr(f"{shape}.shapeBaseSpace1stAxisPlus", 0.75)
            cmds.setAttr(f"{shape}.shapeBaseSpace2ndAxisMinus", 0.25)
        transform = (
            benchmark.group if target == "group" else benchmark.transforms[0]
        )
        for frame, translate, rotate in (
            (1, -0.65, -18),
            (8, 0.15, 17),
            (16, 0.8, 44),
        ):
            cmds.setKeyframe(
                transform, attribute="translateX", time=frame, value=translate
            )
            cmds.setKeyframe(
                transform, attribute="rotateY", time=frame, value=rotate
            )
        cmds.keyTangent(transform, outTangentType="step")
        _playback_range(cmds, _SAMPLE_FRAMES[-1])
        selection = benchmark.om.MSelectionList()
        selection.add(benchmark.shapes[0])
        path = selection.getDagPath(0)
        references = {}
        for frame in _SAMPLE_FRAMES:
            cmds.currentTime(frame)
            record = images._refresh_read(
                benchmark, f"{target}_reference_{frame:02}", force=True
            )
            record["world_matrix"] = list(path.inclusiveMatrix())
            references[frame] = record
        if len({item["rgba_sha256"] for item in references.values()}) != len(
            _SAMPLE_FRAMES
        ):
            raise RuntimeError("静止参照に3姿勢が描画されていません")
        report = {"target": target, "references": references, "runs": []}
        reports.append(report)
        for mode in ["off", *modes]:
            _configure_cache(benchmark, mode, fill_mode)
            if fill_mode == "asyncOnly" and mode != "off":
                cmds.currentTime(1)
                benchmark._refresh()
                if not cmds.cacheEvaluator(waitForCache=30.0):
                    raise RuntimeError("背景のキャッシュ充填が完了しません")
            if mode == "off":
                phases = ("normal",)
            elif fill_mode == "asyncOnly":
                phases = ("restore",)
            else:
                phases = ("fill", "restore")
            for phase in phases:
                label = f"{target}_{mode}_{phase}"
                (benchmark.output / "progress.json").write_text(
                    json.dumps({"status": "capture_playback", "run": label}),
                    encoding="utf-8",
                )
                result = _play(benchmark, images, label)
                result.update(mode=mode, phase=phase)
                report["runs"].append(result)
                if (
                    result["errors"]
                    or set(result["frames"]) != set(_SAMPLE_FRAMES)
                    or result["last_frame"] != _SAMPLE_FRAMES[-1]
                ):
                    raise RuntimeError(f"{label} の再生画像を取得できません")
                if phase == "restore" and not _covered(
                    result["before"], _SAMPLE_FRAMES
                ):
                    raise RuntimeError(
                        f"{label} のフレームがキャッシュされていません: {result['before']}"
                    )
                result["matches"] = {
                    frame: result["frames"][frame]["rgba_sha256"]
                    == references[frame]["rgba_sha256"]
                    for frame in _SAMPLE_FRAMES
                }
                if not all(result["matches"].values()):
                    failures.append(label)
                    if phase == "restore" and metadata.get(
                        "inspect_matrix", True
                    ):
                        diagnostic = _play(
                            benchmark, images, f"{label}_matrix", path
                        )
                        result["matrix_diagnostic"] = diagnostic
                        result["matrix_matches"] = {
                            frame: all(
                                abs(a - b) <= 1e-8
                                for a, b in zip(
                                    entry["world_matrix"],
                                    references[frame]["world_matrix"],
                                )
                            )
                            for frame, entry in diagnostic["frames"].items()
                        }
        _configure_cache(benchmark, "off", fill_mode)
    if failures and (
        metadata.get("require_motion", True)
        or any(label.endswith("_off_normal") for label in failures)
    ):
        raise RuntimeError(
            "再生した画像が静止参照と一致しません: " + ", ".join(failures)
        )


def _measure(benchmark, metadata):
    cmds = benchmark.cmds
    frames = benchmark.config["frames"]
    (mode,) = metadata["cache_modes"]
    for count in benchmark.config["counts"]:
        benchmark.expected_cache_enabled = False
        benchmark._scene(count, f"{count}_{mode}")
        if cmds.paneLayout("viewPanes", exists=True):
            cmds.paneLayout("viewPanes", edit=True, manage=False)
        cmds.autoKeyframe(state=False)
        _configure_cache(benchmark, mode, "syncOnly")
        operations = [
            case for case in benchmark.config["cases"] if case != "playback"
        ]
        if operations:
            # 再生を済ませたアニメーションシーン上で、キーのない回転を編集する。
            translate = benchmark.group + ".translateZ"
            _playback_range(cmds, frames)
            cmds.setKeyframe(translate, time=1, value=0)
            cmds.setKeyframe(translate, time=frames, value=-2)
            cmds.currentTime(1)
            benchmark._activate()
            cmds.play(forward=True, wait=True)
            cmds.currentTime(1)
            primed = _cache_state(benchmark)
            benchmark.result.setdefault("operation_cache_at_start", {})[
                count
            ] = primed
            if mode != "off" and not _covered(primed, range(2, frames + 1)):
                raise RuntimeError(
                    "親・単体操作の前にキャッシュが充填されていません"
                )
            for case in operations:
                if case in ("group", "individual"):
                    _check_operation(benchmark, count, case)
                benchmark._measure(count, case)
            cmds.cutKey(translate, clear=True)
            cmds.setAttr(translate, 0)
        if "playback" in benchmark.config["cases"]:
            benchmark._measure(count, "playback")
            if mode != "off":
                for sample in benchmark.result["cases"][-1]["samples"]:
                    if not _covered(
                        sample["before"]["cache_state"], range(2, frames + 1)
                    ):
                        raise RuntimeError(
                            "再生の計時前にキャッシュ範囲が充填されていません"
                        )
        _configure_cache(benchmark, "off", "syncOnly")


def _check_operation(benchmark, count, case):
    target = benchmark.group if case == "group" else benchmark.transforms[0]
    benchmark.cmds.select(target, replace=True)
    benchmark.cmds.setFocus(benchmark.panel)
    before = benchmark._capture(f"{count}_{case}_pose_before")
    benchmark._step(case, 3)
    after = benchmark._capture(f"{count}_{case}_pose_changed")
    benchmark.cmds.setAttr(target + ".rotate", 0, 0, 0)
    if before["rgba_sha256"] == after["rgba_sha256"]:
        raise RuntimeError(f"{case} 操作が画面に反映されません")
    benchmark.result.setdefault("operation_poses", []).append(
        {"case": case, "count": count, "before": before, "changed": after}
    )


def run(benchmark, images):
    """専用 Maya で、通常描画と実キャッシュからの復元を確認する。"""
    faulthandler.cancel_dump_traceback_later()
    metadata = benchmark.config.get("run_metadata", {})
    benchmark.cmds.loadPlugin("cacheEvaluator", quiet=True)
    guard = benchmark._guard

    def cache_guard(check=True):
        result = guard(check=check)
        if check:
            result["cache_state"] = _cache_state(benchmark)
        return result

    benchmark._guard = cache_guard
    if metadata.get("measure", False):
        _measure(benchmark, metadata)
    else:
        _probe(benchmark, images, metadata)
