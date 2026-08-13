# coding: utf-8
from __future__ import annotations

import csv
import gc
import hashlib
import math
import os
import platform
import statistics
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence

from maya import cmds, mel
from maya.api import OpenMaya as om

DEFAULT_INPUT_COUNTS = (2, 3, 4, 5, 8, 16)
DIRTY_PATTERNS = ("all", "first", "last")
EVALUATION_MODES = ("off", "serial", "parallel")
VARIANTS = ("fixed", "multi")


@dataclass(frozen=True)
class BenchmarkRecord:
    timestamp_utc: str
    maya_version: str
    maya_api_version: int
    python_version: str
    processor: str
    plugin_path: str
    plugin_sha256: str
    variant: str
    input_count: int
    dirty_pattern: str
    evaluation_mode: str
    replica_count: int
    plugin_node_count: int
    frame_count: int
    repeat_index: int
    dg_compute_count_per_frame: float
    elapsed_seconds: float
    milliseconds_per_frame: float
    network_evaluations_per_second: float


@dataclass(frozen=True)
class _SceneState:
    consumer_plug: str
    plugin_nodes: tuple[str, ...]


def run_benchmarks(
    plugin_path: str | Path,
    *,
    input_counts: Sequence[int] = DEFAULT_INPUT_COUNTS,
    dirty_patterns: Sequence[str] = DIRTY_PATTERNS,
    evaluation_modes: Sequence[str] = EVALUATION_MODES,
    replica_count: int = 500,
    frame_count: int = 80,
    repeat_count: int = 7,
    warmup_count: int = 2,
) -> list[BenchmarkRecord]:
    path = _validate_arguments(
        plugin_path=plugin_path,
        input_counts=input_counts,
        dirty_patterns=dirty_patterns,
        evaluation_modes=evaluation_modes,
        replica_count=replica_count,
        frame_count=frame_count,
        repeat_count=repeat_count,
        warmup_count=warmup_count,
    )
    cmds.loadPlugin(str(path), quiet=True)
    undo_was_enabled = bool(cmds.undoInfo(query=True, state=True))
    cmds.undoInfo(state=False)

    timestamp = datetime.now(timezone.utc).isoformat()
    metadata = {
        "timestamp_utc": timestamp,
        "maya_version": str(cmds.about(version=True)),
        "maya_api_version": int(cmds.about(apiVersion=True)),
        "python_version": platform.python_version(),
        "processor": os.environ.get(
            "PROCESSOR_IDENTIFIER",
            platform.processor(),
        ),
        "plugin_path": str(path),
        "plugin_sha256": _sha256(path),
    }
    records: list[BenchmarkRecord] = []
    previous_mode = cmds.evaluationManager(query=True, mode=True)[0]

    try:
        for dirty_pattern in dirty_patterns:
            for input_count in input_counts:
                variants = (
                    VARIANTS if input_count % 2 else tuple(reversed(VARIANTS))
                )
                for variant in variants:
                    cmds.file(newFile=True, force=True)
                    scene = _build_scene(
                        variant=variant,
                        input_count=input_count,
                        dirty_pattern=dirty_pattern,
                        replica_count=replica_count,
                        frame_count=frame_count,
                    )
                    _validate_scene(scene.consumer_plug, frame_count)
                    cmds.evaluationManager(mode="off")
                    _warm_up(scene.consumer_plug, frame_count, 1)
                    dg_compute_count = _measure_compute_count(scene)

                    for evaluation_mode in evaluation_modes:
                        cmds.evaluationManager(mode=evaluation_mode)
                        cmds.evaluationManager(invalidate=True)
                        _warm_up(
                            scene.consumer_plug,
                            frame_count,
                            warmup_count,
                        )

                        for repeat_index in range(1, repeat_count + 1):
                            elapsed = _measure_elapsed(
                                scene.consumer_plug,
                                frame_count,
                            )
                            milliseconds_per_frame = (
                                elapsed * 1000.0 / frame_count
                            )
                            records.append(
                                BenchmarkRecord(
                                    **metadata,
                                    variant=variant,
                                    input_count=input_count,
                                    dirty_pattern=dirty_pattern,
                                    evaluation_mode=evaluation_mode,
                                    replica_count=replica_count,
                                    plugin_node_count=len(scene.plugin_nodes),
                                    frame_count=frame_count,
                                    repeat_index=repeat_index,
                                    dg_compute_count_per_frame=(
                                        dg_compute_count
                                    ),
                                    elapsed_seconds=elapsed,
                                    milliseconds_per_frame=(
                                        milliseconds_per_frame
                                    ),
                                    network_evaluations_per_second=(
                                        replica_count * frame_count / elapsed
                                    ),
                                )
                            )
                    print(
                        f"measured pattern={dirty_pattern} "
                        f"inputs={input_count} variant={variant}",
                        flush=True,
                    )
    finally:
        cmds.evaluationManager(mode=previous_mode)
        cmds.file(newFile=True, force=True)
        cmds.undoInfo(state=undo_was_enabled)

    return records


def write_csv(
    records: Iterable[BenchmarkRecord],
    output_path: str | Path,
) -> Path:
    path = Path(output_path).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = tuple(BenchmarkRecord.__dataclass_fields__)
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(asdict(record))
    return path


def print_summary(records: Sequence[BenchmarkRecord]) -> None:
    grouped: dict[tuple[str, str, int, str], list[float]] = {}
    compute_counts: dict[tuple[str, str, int, str], float] = {}
    for record in records:
        key = (
            record.dirty_pattern,
            record.evaluation_mode,
            record.input_count,
            record.variant,
        )
        grouped.setdefault(key, []).append(record.milliseconds_per_frame)
        compute_counts[key] = record.dg_compute_count_per_frame

    print("\nbdDouble multiplication benchmark (median ms/frame)")
    print(
        "pattern  mode      inputs  fixed      multi      "
        "fixed/multi  DG compute fixed:multi"
    )
    combinations = sorted(
        {
            (pattern, mode, input_count)
            for pattern, mode, input_count, _ in grouped
        }
    )
    for pattern, mode, input_count in combinations:
        fixed_key = (pattern, mode, input_count, "fixed")
        multi_key = (pattern, mode, input_count, "multi")
        if fixed_key not in grouped or multi_key not in grouped:
            continue
        fixed = statistics.median(grouped[fixed_key])
        multi = statistics.median(grouped[multi_key])
        ratio = fixed / multi
        fixed_compute = compute_counts[fixed_key]
        multi_compute = compute_counts[multi_key]
        print(
            f"{pattern:8} {mode:9} {input_count:6d} "
            f"{fixed:10.4f} {multi:10.4f} {ratio:12.3f} "
            f"{fixed_compute:8.1f}:{multi_compute:.1f}"
        )


def main(
    plugin_path: str | Path,
    *,
    input_counts: Sequence[int] = DEFAULT_INPUT_COUNTS,
    dirty_patterns: Sequence[str] = DIRTY_PATTERNS,
    evaluation_modes: Sequence[str] = EVALUATION_MODES,
    replica_count: int = 500,
    frame_count: int = 80,
    repeat_count: int = 7,
    warmup_count: int = 2,
    output_path: str | Path | None = None,
) -> Path:
    records = run_benchmarks(
        plugin_path,
        input_counts=input_counts,
        dirty_patterns=dirty_patterns,
        evaluation_modes=evaluation_modes,
        replica_count=replica_count,
        frame_count=frame_count,
        repeat_count=repeat_count,
        warmup_count=warmup_count,
    )
    if output_path is None:
        output_path = (
            _find_repo_root()
            / "benchmark_results"
            / "native"
            / f"bd_dbl_multiply_{datetime.now():%Y%m%d_%H%M%S}.csv"
        )
    path = write_csv(records, output_path)
    print_summary(records)
    print(f"\nCSV: {path}")
    return path


def _validate_arguments(
    *,
    plugin_path: str | Path,
    input_counts: Sequence[int],
    dirty_patterns: Sequence[str],
    evaluation_modes: Sequence[str],
    replica_count: int,
    frame_count: int,
    repeat_count: int,
    warmup_count: int,
) -> Path:
    path = Path(plugin_path).resolve()
    if not path.is_file():
        raise FileNotFoundError(f"Plug-in was not found: {path}")
    if not input_counts or any(count < 2 for count in input_counts):
        raise ValueError("input_counts must contain values of at least 2")
    if not dirty_patterns or not set(dirty_patterns) <= set(DIRTY_PATTERNS):
        raise ValueError(
            f"dirty_patterns must be selected from {DIRTY_PATTERNS}"
        )
    if not evaluation_modes or not set(evaluation_modes) <= set(
        EVALUATION_MODES
    ):
        raise ValueError(
            f"evaluation_modes must be selected from {EVALUATION_MODES}"
        )
    for name, value, minimum in (
        ("replica_count", replica_count, 1),
        ("frame_count", frame_count, 2),
        ("repeat_count", repeat_count, 1),
        ("warmup_count", warmup_count, 0),
    ):
        if value < minimum:
            raise ValueError(f"{name} must be at least {minimum}")
    return path


def _build_scene(
    *,
    variant: str,
    input_count: int,
    dirty_pattern: str,
    replica_count: int,
    frame_count: int,
) -> _SceneState:
    factor_plugs = _create_factor_plugs(
        input_count,
        dirty_pattern,
        frame_count,
    )
    sink = cmds.createNode("plusMinusAverage", name="benchmarkSink")
    cmds.setAttr(f"{sink}.operation", 1)
    plugin_nodes: list[str] = []

    for replica_index in range(replica_count):
        if variant == "fixed":
            output_plug = _create_fixed_chain(
                factor_plugs,
                plugin_nodes,
            )
        elif variant == "multi":
            output_plug = _create_multi_node(
                factor_plugs,
                plugin_nodes,
            )
        else:
            raise ValueError(f"Unknown variant: {variant}")
        cmds.connectAttr(
            output_plug,
            f"{sink}.input1D[{replica_index}]",
        )

    consumer = cmds.createNode("transform", name="benchmarkConsumer")
    cmds.connectAttr(f"{sink}.output1D", f"{consumer}.translateX")
    return _SceneState(
        consumer_plug=f"{consumer}.translateX",
        plugin_nodes=tuple(plugin_nodes),
    )


def _create_factor_plugs(
    input_count: int,
    dirty_pattern: str,
    frame_count: int,
) -> tuple[str, ...]:
    driver = cmds.createNode("network", name="benchmarkFactors")
    if dirty_pattern == "all":
        animated_indices = set(range(input_count))
    elif dirty_pattern == "first":
        animated_indices = {0}
    elif dirty_pattern == "last":
        animated_indices = {input_count - 1}
    else:
        raise ValueError(f"Unknown dirty pattern: {dirty_pattern}")

    plugs: list[str] = []
    for input_index in range(input_count):
        attribute_name = f"factor{input_index}"
        cmds.addAttr(
            driver,
            longName=attribute_name,
            attributeType="double",
            keyable=True,
        )
        plug = f"{driver}.{attribute_name}"
        start_value = 1.0 + (input_index + 1) * 0.0001
        end_value = 1.0 + (input_index + 1) * 0.0002
        cmds.setAttr(plug, start_value)
        if input_index in animated_indices:
            cmds.setKeyframe(plug, time=0, value=start_value)
            cmds.setKeyframe(
                plug,
                time=frame_count + 1,
                value=end_value,
            )
            cmds.keyTangent(
                plug, inTangentType="linear", outTangentType="linear"
            )
        plugs.append(plug)
    return tuple(plugs)


def _create_fixed_chain(
    factor_plugs: Sequence[str],
    plugin_nodes: list[str],
) -> str:
    node = cmds.createNode("bdDbl_Multiply")
    plugin_nodes.append(node)
    cmds.connectAttr(factor_plugs[0], f"{node}.input1")
    cmds.connectAttr(factor_plugs[1], f"{node}.input2")
    output_plug = f"{node}.output"

    for factor_plug in factor_plugs[2:]:
        node = cmds.createNode("bdDbl_Multiply")
        plugin_nodes.append(node)
        cmds.connectAttr(output_plug, f"{node}.input1")
        cmds.connectAttr(factor_plug, f"{node}.input2")
        output_plug = f"{node}.output"
    return output_plug


def _create_multi_node(
    factor_plugs: Sequence[str],
    plugin_nodes: list[str],
) -> str:
    node = cmds.createNode("bdDbl_MultiplyMulti")
    plugin_nodes.append(node)
    for input_index, factor_plug in enumerate(factor_plugs):
        cmds.connectAttr(factor_plug, f"{node}.input[{input_index}]")
    return f"{node}.output"


def _validate_scene(consumer_plug: str, frame_count: int) -> None:
    cmds.currentTime(0)
    start_value = float(cmds.getAttr(consumer_plug))
    cmds.currentTime(frame_count)
    end_value = float(cmds.getAttr(consumer_plug))
    if not math.isfinite(start_value) or not math.isfinite(end_value):
        raise AssertionError("Benchmark output must remain finite")
    if math.isclose(start_value, end_value, rel_tol=1.0e-12):
        raise AssertionError("Animated benchmark output did not change")


def _warm_up(
    consumer_plug: str,
    frame_count: int,
    warmup_count: int,
) -> None:
    for _ in range(warmup_count):
        _prepare_first_frame(consumer_plug)
        mel.eval(_frame_loop_command(consumer_plug, frame_count))


def _measure_elapsed(consumer_plug: str, frame_count: int) -> float:
    _prepare_first_frame(consumer_plug)
    gc.collect()
    gc_was_enabled = gc.isenabled()
    if gc_was_enabled:
        gc.disable()
    start = time.perf_counter_ns()
    try:
        mel.eval(_frame_loop_command(consumer_plug, frame_count))
    finally:
        elapsed = (time.perf_counter_ns() - start) / 1_000_000_000
        if gc_was_enabled:
            gc.enable()
    return elapsed


def _measure_compute_count(scene: _SceneState) -> float:
    _prepare_first_frame(scene.consumer_plug)
    node_functions = [_node_function(node) for node in scene.plugin_nodes]
    cmds.dgtimer(timerOn=True)
    cmds.dgtimer(reset=True)
    try:
        cmds.currentTime(1)
        cmds.getAttr(scene.consumer_plug)
        total_count = sum(
            node_function.dgTimer(
                om.MFnDependencyNode.kTimerMetric_compute,
                om.MFnDependencyNode.kTimerType_count,
            )
            for node_function in node_functions
        )
    finally:
        cmds.dgtimer(timerOff=True)
    if total_count <= 0.0:
        raise AssertionError("No compute calls were recorded for one frame")
    return total_count


def _node_function(node: str) -> om.MFnDependencyNode:
    selection = om.MSelectionList()
    selection.add(node)
    return om.MFnDependencyNode(selection.getDependNode(0))


def _prepare_first_frame(consumer_plug: str) -> None:
    cmds.currentTime(0)
    cmds.getAttr(consumer_plug)


def _frame_loop_command(consumer_plug: str, frame_count: int) -> str:
    return (
        f"for ($bdMultFrame = 1; $bdMultFrame <= {frame_count}; "
        "++$bdMultFrame) {"
        "currentTime -edit $bdMultFrame;"
        f'getAttr "{consumer_plug}";'
        "}"
    )


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _find_repo_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / ".git").exists():
            return parent
    raise RuntimeError("Repository root could not be found")
