"""固定 Cube の8独立 process の記録を監査し、条件別の記述統計を保存する。"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import re
import statistics
import struct
import sys

_SEQUENCE = (
    "geometry",
    "subscene",
    "controller",
    "curve",
    "curve",
    "controller",
    "subscene",
    "geometry",
)
_COUNTS = (1, 100, 1000)
_CASES = ("static", "individual", "group", "camera", "playback")
_PRODUCTION_CUBE_SOURCES = (
    "src/nodes/BdShpLCubeNode.cpp",
    "src/nodes/BdShpLCubeGeometryOverride.cpp",
    "include/bdUtilNodes/nodes/BdShpLCubeNode.h",
    "include/bdUtilNodes/draw/FixedCubeGeometry.h",
)


def _read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def _source_snapshot_hashes(snapshot: Path) -> dict[str, str]:
    return {
        path.relative_to(snapshot).as_posix(): _sha(path)
        for path in sorted(snapshot.rglob("*"))
        if path.is_file()
        and "__pycache__" not in path.relative_to(snapshot).parts
        and path.suffix not in (".pyc", ".pyo")
    }


def _audit_source_snapshot(
    study: Path, snapshot: Path, repository: Path, *, required: bool = False
) -> str | None:
    manifest_path = study / "source_snapshot_manifest.json"
    if not manifest_path.exists():
        _require(
            not required and not (snapshot / "production_cube").exists(),
            "Production source snapshot manifest is missing",
        )
        return None
    manifest = _read(manifest_path)
    _require(manifest["schema_version"] == 2, "Unknown source snapshot schema")
    _require(
        Path(manifest["research_source_directory"]).resolve()
        == repository / "native/maya/experiments/fixed_cube"
        and Path(manifest["production_source_directory"]).resolve()
        == repository / "native/maya/plugins/bdUtilNodes",
        "Source snapshot locations differ",
    )
    hashes = _source_snapshot_hashes(snapshot)
    _require(
        hashes == manifest["source_snapshot_sha256"],
        "Source snapshot files differ from the manifest",
    )
    _require(
        {name for name in hashes if name.startswith("production_cube/")}
        == {"production_cube/" + name for name in _PRODUCTION_CUBE_SOURCES},
        "Production Cube source snapshot is incomplete",
    )
    return _sha(manifest_path)


def _positive(value: object, label: str) -> float:
    _require(
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
        and value > 0,
        label + " must be finite and positive",
    )
    return float(value)


def _time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _image(record: dict, run: Path, viewport: tuple[int, int]) -> None:
    path = Path(record["path"]).resolve()
    _require(path.parent == run, "Image is outside its run directory")
    _require(_sha(path) == record["file_sha256"], "Image file SHA256 differs")
    header = path.read_bytes()[:24]
    _require(len(header) == 24, "PNG header is incomplete")
    _require(header[:8] == b"\x89PNG\r\n\x1a\n", "Image is not PNG")
    _require(header[12:16] == b"IHDR", "PNG IHDR is missing")
    size = struct.unpack(">II", header[16:24])
    _require(size == viewport == tuple(record["size"]), "Image size differs")
    _require(
        bool(re.fullmatch(r"[0-9a-f]{64}", record["rgba_sha256"])),
        "Recorded RGBA SHA256 is invalid",
    )
    if not record["is_blank_reference"]:
        _require(
            record["pixels_changed_from_blank_inside_shape_bounds"] >= 8,
            "Image has no recorded shape pixels relative to blank",
        )


def _guard(record: dict, pid: int) -> tuple[int, int]:
    _require(record["foreground_valid"] is True, "Foreground guard failed")
    _require(record["foreground_pid"] == pid, "Foreground process differs")
    _require(record["active_view"] is True, "Target view is not active")
    _require(
        record["evaluation"] and record["evaluation"][0] == "parallel",
        "Evaluation is not parallel",
    )
    for name in (
        "cache_enabled",
        "msaa",
        "line_aa",
        "profiler",
        "hud",
        "origin_axis",
    ):
        _require(record[name] is False, name + " must be disabled")
    _require(record["undo"] is True, "Undo must be enabled")
    viewport = tuple(record["viewport"])
    _require(len(viewport) == 2 and min(viewport) > 0, "Viewport is empty")
    return viewport


def _audit_run(run: Path, mode: str, snapshot: Path) -> dict:
    config = _read(run / "config.json")
    result = _read(run / "results.json")
    process = _read(run / "process.json")
    process_exit = _read(run / "process_exit.json")
    launcher_exit = _read(run / "launcher_exit.json")
    _require(result["status"] == "passed", "Results are not passed")
    _require(result["requested_exit_code"] == 0, "Maya requested failure exit")
    _require(
        process_exit["actual_exit_code"] == 0, "Actual process exit failed"
    )
    _require(process_exit["timed_out"] is False, "Process timed out")
    _require(launcher_exit["exit_code"] == 0, "Launcher exit failed")
    _require(not (run / "timeout.json").exists(), "Timeout evidence exists")
    _require(
        not (run / "launcher_error.txt").exists(), "Launcher error exists"
    )
    _require(result["config"] == config, "Config and results config differ")
    _require(config["mode"] == mode, "Mode differs from the study sequence")
    _require(
        tuple(config["counts"]) == _COUNTS,
        "Counts differ from the formal study",
    )
    _require(
        tuple(config["cases"]) == _CASES, "Cases differ from the formal study"
    )
    _require(
        (config["frames"], config["trials"], config["warmup"]) == (36, 5, 8),
        "Formal study requires frames=36, trials=5, warmup=8",
    )
    _require(config["functional"] is True, "Functional smoke was disabled")
    _require(
        not config.get("native_profile", False),
        "Diagnostic timings are not formal performance results",
    )
    _require(
        not config.get("maya_profile", False),
        "Maya profiler timings are not formal performance results",
    )
    _require(
        not config.get("renderer_reset_gate", False),
        "Renderer reset gate is not a performance run",
    )
    _require(
        Path(config["output_directory"]).resolve() == run, "Run path differs"
    )
    repository = Path(config["repository_directory"]).resolve()
    _require(run.is_relative_to(repository), "Run is outside its repository")
    profile = (
        repository
        / "build/fixed_cube/profiles"
        / ("maya" + config["maya_version"])
    )
    _require(
        Path(config["profile_directory"]).resolve() == profile,
        "Run does not use the fixed task profile",
    )
    profile_hashes = config["profile_file_sha256"]
    _require(
        set(profile_hashes)
        == {
            config["maya_version"] + "/prefs/userPrefs.mel",
            config["maya_version"] + "/Maya.env",
            "Maya.env",
        }
        and all(
            value is None or re.fullmatch(r"[0-9a-f]{64}", value)
            for value in profile_hashes.values()
        ),
        "Profile file hashes are incomplete or invalid",
    )
    _require(
        result["profile_file_sha256_after"]
        == launcher_exit["profile_file_sha256"]
        == profile_hashes
        and launcher_exit["profile_audit_error"] is None,
        "Dedicated profile changed during the run",
    )
    pid = process["pid"]
    _require(result["pid"] == process_exit["pid"] == pid, "Process IDs differ")
    started, finished = _time(process["started_utc"]), _time(
        process_exit["finished_utc"]
    )
    _require(started < finished, "Process timestamps are not ordered")
    for name, key in (
        ("benchmark.py", "benchmark_sha256"),
        ("launch.ps1", "launcher_sha256"),
    ):
        _require(
            _sha(snapshot / name) == config[key],
            name + " snapshot SHA256 differs",
        )
    _require(
        _sha(run / "benchmark.py") == config["benchmark_sha256"],
        "Archived runner differs",
    )
    runtime = result["runtime"]
    _require(
        not runtime.get("plugin")
        or "bdCubeProfile" not in runtime["plugin"].get("commands", []),
        "Diagnostic DLL is not eligible for formal performance results",
    )
    _require(
        Path(runtime["environment"]["MAYA_APP_DIR"]).resolve() == profile
        and runtime["profile_file_sha256"] == profile_hashes,
        "Runtime profile differs from launch configuration",
    )
    _require(
        int(runtime["api_version"]) // 10000 == int(config["maya_version"]),
        "Maya API version differs",
    )
    plugin_hash = None
    if mode == "curve":
        _require(
            config["plugin_path"] is None
            and config["plugin_archive_path"] is None
            and config["plugin_sha256"] is None
            and runtime["plugin"] is None
            and result["plugin_sha256_after"] is None,
            "Curve control loaded a plug-in",
        )
    else:
        plugin = runtime["plugin"]
        path = Path(config["plugin_path"]).resolve()
        archive = Path(config["plugin_archive_path"]).resolve()
        _require(
            archive.parent == run and archive.name == path.name,
            "Plug-in archive is outside the run directory or name differs",
        )
        _require(
            not path.is_relative_to(run.parent),
            "Runtime plug-in must use its fixed source location",
        )
        _require(
            Path(plugin["path"]).resolve() == path
            and Path(plugin["archive_path"]).resolve() == archive,
            "Runtime plug-in or archive path differs",
        )
        plugin_hash = _sha(path)
        _require(
            plugin_hash
            == _sha(archive)
            == config["plugin_sha256"]
            == plugin["sha256"]
            == plugin["archive_sha256"]
            == result["plugin_sha256_after"]["actual"]
            == result["plugin_sha256_after"]["archive"],
            "Fixed source/archived/runtime plug-in SHA256 differs",
        )
        _require(
            plugin["api_version"] // 10000 == int(config["maya_version"]),
            "Plug-in API version differs",
        )
    scenes = {scene["label"]: scene for scene in result["scenes"]}
    _require(
        len(scenes) == len(result["scenes"]) == 4,
        "Expected three measured scenes and one functional scene",
    )
    _require(
        set(scenes) == {"1", "100", "1000", "functional_scene"},
        "Scene labels differ",
    )
    viewport = None
    for label, scene in scenes.items():
        count = 1 if label == "functional_scene" else int(label)
        _require(
            scene["mode"] == mode and scene["count"] == count,
            "Scene mode/count differs",
        )
        _require(
            scene["independent_transforms"]
            == scene["independent_shapes"]
            == count,
            "Independent node count differs",
        )
        _require(scene["dag_instances"] == 0, "DAG instances were used")
        _require(scene["unique_cube_edges"] == 12, "Cube edge count differs")
        if mode == "curve":
            _require(
                (
                    scene["curve_degree"],
                    scene["curve_cvs"],
                    scene["curve_segments"],
                    scene["curve_history"],
                )
                == (1, 16, 15, False),
                "Curve topology/history differs",
            )
        dimensions = _guard(scene["initial_guard"], pid)
        viewport = dimensions if viewport is None else viewport
        _require(dimensions == viewport, "Viewport differs between scenes")
        _require(
            scene["bounds"]["outside_corners"] == 0,
            "Scene bounds leave viewport",
        )
        _image(scene["blank_image"], run, viewport)
        _image(scene["image"], run, viewport)
    cases = {}
    signatures = {}
    for case in result["cases"]:
        key = (case["count"], case["case"])
        _require(key not in cases, "Duplicate measured condition")
        _require(
            key[0] in _COUNTS and key[1] in _CASES,
            "Unknown measured condition",
        )
        samples = case["samples"]
        _require(len(samples) == 5, "Condition does not have five trials")
        values = []
        selected = None
        camera = None
        for trial, sample in enumerate(samples, 1):
            _require(sample["trial"] == trial, "Trial order differs")
            _require(
                sample["requested_frames"] == 36,
                "Requested frame count differs",
            )
            elapsed = _positive(sample["wall_seconds"], "wall_seconds")
            value = _positive(
                sample["ms_per_requested_frame"], "ms_per_requested_frame"
            )
            _require(
                math.isclose(value, elapsed * 1000 / 36, rel_tol=1e-10),
                "Per-frame time is inconsistent",
            )
            _require(
                isinstance(sample["post_render_count"], int)
                and not isinstance(sample["post_render_count"], bool)
                and sample["post_render_count"] > 0,
                "No target render in timed interval",
            )
            before, after = sample["before"], sample["after"]
            _require(
                _guard(before, pid) == _guard(after, pid) == viewport,
                "Trial viewport differs",
            )
            _require(
                before["selection"] == after["selection"],
                "Selection changed in trial",
            )
            _require(
                before["camera"] == after["camera"],
                "Camera path changed in trial",
            )
            _require(
                before["current_time"] == 1, "Trial did not start at frame 1"
            )
            expected_end = 36 if key[1] == "playback" else 1
            _require(
                after["current_time"] == expected_end, "Trial end time differs"
            )
            selected = before["selection"] if selected is None else selected
            camera = before["camera"] if camera is None else camera
            _require(
                before["selection"] == selected and before["camera"] == camera,
                "Trial selection/camera differs",
            )
            values.append(value)
        median = statistics.median(values)
        _require(
            math.isclose(
                median, case["median_ms_per_requested_frame"], rel_tol=1e-10
            ),
            "Recorded median differs",
        )
        _image(case["before_image"], run, viewport)
        _image(case["restored_image"], run, viewport)
        _require(
            case["before_image"]["rgba_sha256"]
            == case["restored_image"]["rgba_sha256"],
            "Pose did not restore",
        )
        _require(
            case["bounds_after_restore"]["outside_corners"] == 0,
            "Restored bounds leave viewport",
        )
        cases[key] = values
        signatures[key] = {
            "selection": selected,
            "camera": camera,
            "bounds": case["bounds_after_restore"],
        }
    _require(
        set(cases) == {(count, case) for count in _COUNTS for case in _CASES},
        "Measured condition matrix is incomplete",
    )
    pick = result["screen_selection"]["checks"]
    _require(
        len(pick) == 12 and all(item["valid"] is True for item in pick),
        "Screen selection smoke failed",
    )
    _require(
        [item["attribute"] for item in result["functional"]]
        == [
            "rotatePivot",
            "scalePivot",
            "rotateAxis",
            "shear",
            "scale",
            "parent_joint.jointOrient",
        ],
        "Functional smoke is incomplete",
    )
    for item in result["functional"]:
        _require(
            item["attribute_changed_rendering"] is True,
            "Functional change did not affect rendering",
        )
        _require(
            item["bounds"]["outside_corners"] == 0,
            "Functional bounds leave viewport",
        )
        _image(item["image"], run, viewport)
        _image(item["restored"], run, viewport)
        reference = item.get("reference", scenes["functional_scene"]["image"])
        _image(reference, run, viewport)
        _require(
            item["image"]["rgba_sha256"] != reference["rgba_sha256"],
            "Functional reference and changed image are equal",
        )
        _require(
            item["restored"]["rgba_sha256"]
            == scenes["functional_scene"]["image"]["rgba_sha256"],
            "Functional pose did not restore",
        )
    return {
        "run": str(run),
        "mode": mode,
        "pid": pid,
        "started": started,
        "finished": finished,
        "viewport": viewport,
        "plugin_path": config["plugin_path"],
        "plugin_archive_path": config["plugin_archive_path"],
        "plugin_sha256": plugin_hash,
        "runtime": runtime,
        "config": config,
        "cases": cases,
        "signatures": signatures,
        "evidence_sha256": {
            name: _sha(run / name)
            for name in (
                "config.json",
                "results.json",
                "process.json",
                "process_exit.json",
                "launcher_exit.json",
                "benchmark.py",
            )
        },
        "termination_method": result["termination_method"],
    }


def summarize(study_directory: Path) -> dict:
    """全runを検証し、成功した正式studyだけを集計する。"""
    study = study_directory.resolve()
    snapshot = study / "source_snapshot"
    expected_names = [
        f"{index:02d}_{mode}" for index, mode in enumerate(_SEQUENCE, 1)
    ]
    actual_names = sorted(
        path.name
        for path in study.iterdir()
        if path.is_dir() and re.match(r"^\d+_", path.name)
    )
    _require(
        actual_names == expected_names,
        "Study must contain exactly the eight expected run directories",
    )
    runs = []
    for name, mode in zip(expected_names, _SEQUENCE):
        try:
            runs.append(_audit_run(study / name, mode, snapshot))
        except (KeyError, IndexError, TypeError, ValueError, OSError) as error:
            raise ValueError(f"{name}: {error}") from error
    base = runs[0]
    baseline = _read(study / "profile_baseline.json")
    source_manifest_hash = _audit_source_snapshot(
        study,
        snapshot,
        Path(base["config"]["repository_directory"]).resolve(),
        required="source_snapshot_manifest_sha256" in baseline,
    )
    _require(
        baseline.get("source_snapshot_manifest_sha256")
        == source_manifest_hash,
        "Source snapshot manifest differs from the study baseline",
    )
    _require(
        baseline["maya_version"] == base["config"]["maya_version"]
        and Path(baseline["profile_directory"]).resolve()
        == Path(base["config"]["profile_directory"]).resolve()
        and baseline["profile_file_sha256"]
        == base["config"]["profile_file_sha256"],
        "First run differs from the study profile baseline",
    )
    identities = {(run["pid"], run["started"]) for run in runs}
    _require(
        len(identities) == 8,
        "Runs are not eight independent process identities",
    )
    for previous, following in zip(runs, runs[1:]):
        _require(
            previous["finished"] <= following["started"],
            "Recorded process intervals overlap",
        )
    settings = (
        "maya_version",
        "counts",
        "cases",
        "frames",
        "trials",
        "warmup",
        "functional",
        "force_self_exit",
        "benchmark_sha256",
        "launcher_sha256",
        "repository_directory",
        "profile_directory",
        "profile_file_sha256",
    )
    runtime_keys = (
        "maya",
        "api_version",
        "gpu",
        "python",
        "consolidation_and_instancing",
    )
    environment_keys = (
        "MAYA_APP_DIR",
        "MAYA_MODULE_PATH",
        "MAYA_VP2_DEVICE_OVERRIDE",
        "MAYA_VP2_USE_VP1_SELECTION",
        "MAYA_DISABLE_VP2_CONSOLIDATION",
        "MAYA_DISABLE_VP2_PLUGIN_CONSOLIDATION",
        "MAYA_VP2_USE_GPU_INSTANCING",
    )
    for run in runs[1:]:
        _require(
            all(run["config"][key] == base["config"][key] for key in settings),
            "Run measurement settings differ",
        )
        _require(
            all(
                run["runtime"][key] == base["runtime"][key]
                for key in runtime_keys
            ),
            "Runtime/GPU configuration differs",
        )
        _require(
            all(
                run["runtime"]["environment"].get(key)
                == base["runtime"]["environment"].get(key)
                for key in environment_keys
            ),
            "Render environment differs",
        )
        _require(
            run["viewport"] == base["viewport"],
            "Viewport differs between runs",
        )
        _require(
            run["signatures"] == base["signatures"],
            "Selection/camera/restored bounds differ between runs",
        )
    modes = tuple(dict.fromkeys(_SEQUENCE))
    for mode in modes:
        matching = [run for run in runs if run["mode"] == mode]
        _require(len(matching) == 2, "Each mode requires two process launches")
        _require(
            len({run["plugin_sha256"] for run in matching}) == 1,
            "Repeated mode uses different DLLs",
        )
        _require(
            len({run["plugin_path"] for run in matching}) == 1,
            "Repeated mode does not use the same fixed DLL location",
        )
    comparisons = []
    for count in _COUNTS:
        for case in _CASES:
            group = {}
            for mode in modes:
                matching = [run for run in runs if run["mode"] == mode]
                samples = [
                    value
                    for run in matching
                    for value in run["cases"][(count, case)]
                ]
                medians = [
                    statistics.median(run["cases"][(count, case)])
                    for run in matching
                ]
                group[mode] = {
                    "independent_processes": 2,
                    "nested_trials": 10,
                    "process_medians_ms": medians,
                    "process_median_range_ms": [min(medians), max(medians)],
                    "pooled_trial_median_ms": statistics.median(samples),
                    "trial_range_ms": [min(samples), max(samples)],
                    "trial_values_ms": samples,
                }
            curve = group["curve"]["pooled_trial_median_ms"]
            for values in group.values():
                ratio = values["pooled_trial_median_ms"] / curve
                values["time_ratio_to_curve"] = ratio
                values["time_change_vs_curve_percent"] = (ratio - 1) * 100
            comparisons.append({"count": count, "case": case, "modes": group})
    return {
        "status": "audited",
        "study_directory": str(study),
        "audited_utc": datetime.now(timezone.utc).isoformat(),
        "auditor_sha256": _sha(Path(__file__)),
        "sequence": list(_SEQUENCE),
        "viewport": list(base["viewport"]),
        "settings": {key: base["config"][key] for key in settings},
        "runtime": {key: base["runtime"][key] for key in runtime_keys},
        "profile_baseline_sha256": _sha(study / "profile_baseline.json"),
        "source_snapshot_manifest_sha256": source_manifest_hash,
        "source_snapshot_sha256": {
            str(path.relative_to(snapshot)): _sha(path)
            for path in sorted(snapshot.rglob("*"))
            if path.is_file()
        },
        "runs": [
            {
                key: (
                    value.isoformat() if isinstance(value, datetime) else value
                )
                for key, value in run.items()
                if key
                in (
                    "run",
                    "mode",
                    "pid",
                    "started",
                    "finished",
                    "plugin_path",
                    "plugin_archive_path",
                    "plugin_sha256",
                    "evidence_sha256",
                    "termination_method",
                )
            }
            for run in runs
        ],
        "comparisons": comparisons,
        "limits": [
            "Descriptive statistics from two independent processes per mode; five nested trials per process are not five independent launches.",
            "Time ratio is mode / curve; values below one are shorter wall time. No statistical significance or general performance guarantee is asserted.",
            "Scripted trials include value settings and forced refresh. Playback time is divided by requested frames and includes start/stop overhead; no HUD FPS or one-image-per-frame assertion.",
            "PNG SHA256, IHDR and recorded pixel guards were checked; no independent pixel codec reconstruction or cross-mode visual-equivalence audit is performed here.",
            "Source archive and runtime DLL hashes identify artifacts; this audit does not independently prove the DLL was compiled from every archived native source.",
            "Processes share one dedicated task profile. Recorded userPrefs.mel and Maya.env hashes must remain identical; trust settings are not created, copied or modified by this harness.",
            "Forced self-termination is not graceful shutdown. Recorded process exits are checked; process absence after exit is not independently queried by this script.",
        ],
    }


def main() -> int:
    """study directory と新規 output JSON を受け取り、監査失敗時は1を返す。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("study_directory", type=Path)
    parser.add_argument("output_json", type=Path)
    args = parser.parse_args()
    if args.output_json.exists():
        parser.error(
            "Output JSON already exists; previous evidence is preserved"
        )
    try:
        report = summarize(args.study_directory)
        code = 0
    except (KeyError, IndexError, TypeError, ValueError, OSError) as error:
        report = {
            "status": "rejected",
            "study_directory": str(args.study_directory.resolve()),
            "auditor_sha256": _sha(Path(__file__)),
            "errors": [str(error)],
        }
        code = 1
    with args.output_json.open("x", encoding="utf-8") as output:
        json.dump(
            report, output, ensure_ascii=False, indent=2, allow_nan=False
        )
        output.write("\n")
    print(
        json.dumps(
            {
                "status": report["status"],
                "output": str(args.output_json.resolve()),
                "errors": report.get("errors", []),
            }
        )
    )
    return code


if __name__ == "__main__":
    sys.exit(main())
