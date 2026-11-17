"""旧 GO・候補 GO・NURBS の6独立 process を監査して比較する。"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import statistics
import sys

import summarize as common

_SEQUENCE = (
    "baseline",
    "candidate",
    "curve",
    "curve",
    "candidate",
    "baseline",
)
_VARIANTS = ("baseline", "candidate", "curve")
_RUNTIME_KEYS = (
    "maya",
    "api_version",
    "gpu",
    "python",
    "consolidation_and_instancing",
)
_VARIABLE_CONFIG_KEYS = {
    "mode",
    "output_directory",
    "plugin_path",
    "plugin_archive_path",
    "plugin_sha256",
    "requested_plugin_path",
    "started_utc",
}


def _source_hashes(root: Path) -> dict[str, str]:
    return common._source_snapshot_hashes(root)


def _settings(maya_version: str) -> dict:
    return {
        "maya_version": maya_version,
        "counts": list(common._COUNTS),
        "cases": list(common._CASES),
        "frames": 36,
        "trials": 5,
        "warmup": 8,
        "activation_timeout": 60,
        "timeout_seconds": 240,
        "exit_grace_seconds": 45,
        "functional": True,
        "force_self_exit": True,
        "native_profile": False,
        "maya_profile": False,
        "playback_gate": False,
        "playback_gate_sha256": None,
        "renderer_reset_gate": False,
    }


def _audit_manifest(study: Path, snapshot: Path) -> dict:
    manifest = common._read(study / "study_manifest.json")
    common._require(
        manifest["schema_version"] in (1, 2)
        and manifest["study_kind"] == "geometry_playback_abc_cba"
        and manifest["sequence"] == list(_SEQUENCE),
        "Study manifest schema or sequence differs",
    )
    repository = Path(manifest["repository_directory"]).resolve()
    source = repository / "native/maya/experiments/fixed_cube"
    common._require(
        Path(manifest["output_directory"]).resolve() == study
        and study.is_relative_to(repository)
        and Path(manifest["source_directory"]).resolve() == source,
        "Study output or source location differs",
    )
    version = manifest["settings"]["maya_version"]
    common._require(
        version in ("2025", "2026", "2027"), "Unknown Maya version"
    )
    common._require(
        manifest["settings"] == _settings(version),
        "Manifest measurement settings differ from the formal study",
    )
    hashes = _source_hashes(snapshot)
    common._require(
        hashes == manifest["source_snapshot_sha256"],
        "Frozen source snapshot differs from the manifest",
    )
    source_manifest_hash = common._audit_source_snapshot(
        study, snapshot, repository, required=manifest["schema_version"] == 2
    )
    common._require(
        manifest.get("source_snapshot_manifest_sha256")
        == source_manifest_hash,
        "Source snapshot manifest differs from the study manifest",
    )
    for name, path in (
        ("summarize_playback.py", Path(__file__)),
        ("summarize.py", Path(common.__file__)),
    ):
        common._require(
            common._sha(path) == hashes[name],
            name + " auditor differs from the frozen source",
        )
    profile = repository / "build/fixed_cube/profiles" / ("maya" + version)
    common._require(
        Path(manifest["profile_directory"]).resolve() == profile,
        "Study profile location differs",
    )
    baseline = common._read(study / "profile_baseline.json")
    common._require(
        baseline["maya_version"] == version
        and Path(baseline["profile_directory"]).resolve() == profile
        and baseline["profile_file_sha256"] == manifest["profile_file_sha256"],
        "Profile baseline differs from the manifest",
    )
    for relative, digest in manifest["profile_file_sha256"].items():
        path = profile / relative
        common._require(
            (common._sha(path) if path.is_file() else None) == digest,
            "Current dedicated profile differs: " + relative,
        )
    plugins = manifest["plugins"]
    common._require(
        set(plugins) == {"baseline", "candidate"}, "DLL variants differ"
    )
    for variant, suffix in (
        ("baseline", "Baseline"),
        ("candidate", "Candidate"),
    ):
        expected = (
            repository
            / "build/fixed_cube"
            / ("maya" + version)
            / "Release"
            / ("bdShpCubeGeometry" + suffix + ".mll")
        )
        common._require(
            Path(plugins[variant]["path"]).resolve() == expected
            and common._sha(expected) == plugins[variant]["sha256"],
            "Current fixed DLL differs from the manifest: " + variant,
        )
    common._require(
        plugins["baseline"]["sha256"] != plugins["candidate"]["sha256"],
        "Baseline and candidate DLLs are identical",
    )
    return manifest


def _compare(runs: list[dict]) -> list[dict]:
    comparisons = []
    for count in common._COUNTS:
        for case in common._CASES:
            groups = {}
            for variant in _VARIANTS:
                matching = [run for run in runs if run["variant"] == variant]
                samples = [
                    value
                    for run in matching
                    for value in run["cases"][(count, case)]
                ]
                processes = [
                    {
                        "run": Path(run["run"]).name,
                        "block": run["block"],
                        "median_ms": statistics.median(
                            run["cases"][(count, case)]
                        ),
                        "trial_values_ms": run["cases"][(count, case)],
                        "post_render_counts": run["post_render_counts"][
                            (count, case)
                        ],
                    }
                    for run in matching
                ]
                medians = [process["median_ms"] for process in processes]
                groups[variant] = {
                    "independent_processes": 2,
                    "nested_trials": 10,
                    "processes": processes,
                    "process_medians_ms": medians,
                    "median_of_process_medians_ms": statistics.median(medians),
                    "process_median_range_ms": [min(medians), max(medians)],
                    "pooled_trial_median_ms": statistics.median(samples),
                    "trial_range_ms": [min(samples), max(samples)],
                }
            for group in groups.values():
                for reference in ("curve", "baseline"):
                    control = groups[reference]
                    ratio = (
                        group["pooled_trial_median_ms"]
                        / control["pooled_trial_median_ms"]
                    )
                    group["time_ratio_to_" + reference] = ratio
                    group["time_change_vs_" + reference + "_percent"] = (
                        ratio - 1
                    ) * 100
                    group["process_median_time_ratio_to_" + reference] = (
                        group["median_of_process_medians_ms"]
                        / control["median_of_process_medians_ms"]
                    )
                    for process in group["processes"]:
                        control_process = next(
                            value
                            for value in control["processes"]
                            if value["block"] == process["block"]
                        )
                        process["reference_run_" + reference] = (
                            control_process["run"]
                        )
                        process[
                            "time_ratio_to_" + reference + "_process_in_block"
                        ] = (
                            process["median_ms"] / control_process["median_ms"]
                        )
            comparisons.append(
                {"count": count, "case": case, "variants": groups}
            )
    return comparisons


def summarize(study_directory: Path) -> dict:
    """固定 DLL と全6runの証跡を検証し、成功した比較だけを集計する。"""
    study = study_directory.resolve()
    snapshot = study / "source_snapshot"
    manifest = _audit_manifest(study, snapshot)
    expected_names = [
        f"{index:02d}_{variant}" for index, variant in enumerate(_SEQUENCE, 1)
    ]
    actual_names = sorted(
        path.name
        for path in study.iterdir()
        if path.is_dir() and re.match(r"^\d+_", path.name)
    )
    common._require(
        actual_names == expected_names,
        "Study must contain exactly the six expected run directories",
    )
    runs = []
    for index, (name, variant) in enumerate(zip(expected_names, _SEQUENCE)):
        mode = "curve" if variant == "curve" else "geometry"
        try:
            run = common._audit_run(study / name, mode, snapshot)
            run["variant"] = variant
            run["block"] = 1 if index < 3 else 2
            common._require(
                all(
                    run["config"][key] == value
                    for key, value in manifest["settings"].items()
                ),
                "Run settings differ from the frozen manifest",
            )
            common._require(
                run["config"]["profile_file_sha256"]
                == manifest["profile_file_sha256"]
                and Path(run["config"]["repository_directory"]).resolve()
                == Path(manifest["repository_directory"]).resolve(),
                "Run profile or repository differs from the manifest",
            )
            evidence = common._read(study / name / "results.json")
            run["post_render_counts"] = {
                (case["count"], case["case"]): [
                    sample["post_render_count"] for sample in case["samples"]
                ]
                for case in evidence["cases"]
            }
            if variant != "curve":
                plugin = manifest["plugins"][variant]
                common._require(
                    Path(run["plugin_path"]).resolve()
                    == Path(plugin["path"]).resolve()
                    and run["plugin_sha256"] == plugin["sha256"],
                    "Run uses the wrong fixed DLL variant",
                )
            runs.append(run)
        except (KeyError, IndexError, TypeError, ValueError, OSError) as error:
            raise ValueError(f"{name}: {error}") from error
    common._require(
        len({(run["pid"], run["started"]) for run in runs}) == 6,
        "Runs are not six independent process identities",
    )
    for previous, following in zip(runs, runs[1:]):
        common._require(
            previous["finished"] <= following["started"],
            "Recorded process intervals overlap",
        )
    base = runs[0]
    settings = {
        key: value
        for key, value in base["config"].items()
        if key not in _VARIABLE_CONFIG_KEYS
    }
    for run in runs[1:]:
        common._require(
            {
                key: value
                for key, value in run["config"].items()
                if key not in _VARIABLE_CONFIG_KEYS
            }
            == settings,
            "Run measurement settings differ",
        )
        common._require(
            all(
                run["runtime"][key] == base["runtime"][key]
                for key in _RUNTIME_KEYS
            )
            and run["runtime"]["environment"]
            == base["runtime"]["environment"],
            "Runtime/GPU/render environment differs",
        )
        common._require(
            run["viewport"] == base["viewport"]
            and run["signatures"] == base["signatures"],
            "Viewport/selection/camera/restored bounds differ",
        )
        common._require(
            run["post_render_counts"] == base["post_render_counts"],
            "Timed post-render counts differ between processes",
        )
    for variant in _VARIANTS:
        matching = [run for run in runs if run["variant"] == variant]
        common._require(
            len(matching) == 2
            and len({run["plugin_path"] for run in matching}) == 1
            and len({run["plugin_sha256"] for run in matching}) == 1,
            "Each variant must use two processes and one unchanged DLL location",
        )
    return {
        "status": "audited",
        "study_directory": str(study),
        "audited_utc": datetime.now(timezone.utc).isoformat(),
        "auditor_sha256": common._sha(Path(__file__)),
        "shared_auditor_sha256": common._sha(Path(common.__file__)),
        "study_manifest_sha256": common._sha(study / "study_manifest.json"),
        "source_snapshot_manifest_sha256": manifest.get(
            "source_snapshot_manifest_sha256"
        ),
        "profile_baseline_sha256": common._sha(
            study / "profile_baseline.json"
        ),
        "source_snapshot_sha256": manifest["source_snapshot_sha256"],
        "sequence": list(_SEQUENCE),
        "viewport": list(base["viewport"]),
        "settings": settings,
        "runtime": {key: base["runtime"][key] for key in _RUNTIME_KEYS},
        "environment": base["runtime"]["environment"],
        "plugins": manifest["plugins"],
        "runs": [
            {
                key: (
                    value.isoformat() if isinstance(value, datetime) else value
                )
                for key, value in run.items()
                if key
                in (
                    "run",
                    "variant",
                    "block",
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
        "comparisons": _compare(runs),
        "limits": [
            "Two independent processes per variant; five trials nested in each process are not five independent launches. Descriptive statistics only.",
            "Pooled time ratios divide the 10-trial median by the reference 10-trial median. Process-median ratios divide the medians of two process medians. Values below one mean shorter wall time.",
            "Per-process ratios compare process medians within ABC block 1 or CBA block 2; the processes are sequential and are not simultaneous or randomized pairs.",
            "Scripted cases include value settings and forced refresh. Playback wall time is divided by 36 requested frames and includes start/stop overhead. Timed post-render counts must match all six processes per condition/trial; no general one-render-per-requested-frame guarantee is asserted.",
            "PNG hashes, headers and recorded pixel guards are checked by the shared auditor; independent pixel decoding and cross-variant visual-equivalence checks are not performed.",
            "DLL and frozen source hashes identify artifacts, but do not independently prove that each DLL was built from the archived native source. Baseline and candidate intentionally differ.",
            "Schema 2 snapshots include the four shared production Cube sources. Auditor hashes must match the frozen source for both schema versions; use the archived auditor when reviewing older evidence.",
            "The dedicated profile is shared and its recorded userPrefs.mel/Maya.env hashes must match. Neither script configures plug-in trust or changes security preferences.",
            "The preserved Baseline and Candidate source DLLs must still match at audit time. Rebuilding the separate primary Geometry filename does not replace these comparison artifacts.",
            "Forced self-termination is not graceful shutdown. Recorded process exits are audited; current process absence is not independently queried.",
        ],
    }


def main() -> int:
    """study directory と新規 JSON 出力先を受け取り、監査失敗時は1を返す。"""
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
            "auditor_sha256": common._sha(Path(__file__)),
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
