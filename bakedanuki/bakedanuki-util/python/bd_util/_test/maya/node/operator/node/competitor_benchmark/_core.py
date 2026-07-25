# coding: utf-8
from __future__ import annotations

import csv
import gc
import platform
import statistics
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Sequence

from maya import cmds


SCALAR_VALUE = 1.25


@dataclass(frozen=True)
class BenchmarkScenario:
    name: str
    description: str


DEFAULT_SCENARIOS = (
    BenchmarkScenario(
        "wrap_existing",
        "既存ノード名からライブラリ固有のノード表現を取得する",
    ),
    BenchmarkScenario(
        "plug_access",
        "ラップ済みノードから input1X plug を繰り返し取得する",
    ),
    BenchmarkScenario(
        "scalar_get",
        "取得済み input1X plug から scalar 値を繰り返し読む",
    ),
    BenchmarkScenario(
        "scalar_set",
        "取得済み input1X plug へ scalar 値を繰り返し設定する",
    ),
    BenchmarkScenario(
        "create_nodes",
        "multiplyDivide ノードを指定数作成する",
    ),
    BenchmarkScenario(
        "create_connect_chain",
        "multiplyDivide を作成して直列接続する",
    ),
    BenchmarkScenario(
        "matrix_graph",
        "composeMatrix -> multMatrix -> decomposeMatrix を指定数作成する",
    ),
)


class AdapterUnavailable(RuntimeError):
    pass


class UnsupportedScenario(RuntimeError):
    pass


@dataclass
class OperationResult:
    value: Any = None
    last_destination: str | None = None


@dataclass
class BenchmarkRecord:
    timestamp_utc: str
    maya_version: str
    python_version: str
    adapter: str
    adapter_version: str
    scenario: str
    scenario_description: str
    execution_mode: str
    count: int
    repeat_index: int | None
    elapsed_seconds: float | None
    operations_per_second: float | None
    status: str
    note: str


class BaseBenchmarkAdapter:
    name = ""
    version = ""
    execution_modes: dict[str, str] = {}

    def load(self) -> None:
        pass

    def execution_mode(self, scenario_name: str) -> str:
        return self.execution_modes.get(scenario_name, "immediate")

    def setup_scenario(self, scenario_name: str) -> dict[str, Any]:
        if scenario_name == "wrap_existing":
            return {"node_name": cmds.createNode("multiplyDivide")}

        if scenario_name in {"plug_access", "scalar_get", "scalar_set"}:
            node_name = cmds.createNode("multiplyDivide")
            cmds.setAttr(f"{node_name}.input1X", SCALAR_VALUE)
            node = self.wrap_node(node_name)
            state = {
                "node_name": node_name,
                "node": node,
            }
            if scenario_name != "plug_access":
                state["plug"] = self.scalar_plug(node)
            return state

        return {}

    def run_scenario(
        self,
        scenario_name: str,
        count: int,
        state: dict[str, Any],
    ) -> OperationResult:
        if scenario_name == "wrap_existing":
            value = None
            for _ in range(count):
                value = self.wrap_node(state["node_name"])
            return OperationResult(value=value)

        if scenario_name == "plug_access":
            value = None
            for _ in range(count):
                value = self.scalar_plug(state["node"])
            return OperationResult(value=value)

        if scenario_name == "scalar_get":
            total = 0.0
            plug = state["plug"]
            for _ in range(count):
                total += float(self.read_scalar(plug))
            return OperationResult(value=total)

        if scenario_name == "scalar_set":
            self.set_scalar_repeated(state["plug"], count, SCALAR_VALUE)
            return OperationResult()

        if scenario_name == "create_nodes":
            return self.create_nodes(count)

        if scenario_name == "create_connect_chain":
            return self.create_connect_chain(count)

        if scenario_name == "matrix_graph":
            return self.create_matrix_graph(count)

        raise UnsupportedScenario(scenario_name)

    def validate_scenario(
        self,
        scenario_name: str,
        count: int,
        state: dict[str, Any],
        result: OperationResult,
    ) -> None:
        if scenario_name in {"wrap_existing", "plug_access"}:
            if result.value is None:
                raise AssertionError(f"{scenario_name} returned None")
            return

        if scenario_name == "scalar_get":
            expected = count * SCALAR_VALUE
            if abs(result.value - expected) > 1e-6:
                raise AssertionError(
                    f"scalar_get returned {result.value}; expected {expected}"
                )
            return

        if scenario_name == "scalar_set":
            value = float(self.read_scalar(state["plug"]))
            if abs(value - SCALAR_VALUE) > 1e-6:
                raise AssertionError(
                    f"scalar_set left {value}; expected {SCALAR_VALUE}"
                )
            return

        if scenario_name == "create_nodes":
            self._assert_node_count("multiplyDivide", count)
            return

        if scenario_name == "create_connect_chain":
            self._assert_node_count("multiplyDivide", count)
            expected_destination = count > 1
            self._assert_destination(
                result.last_destination,
                expected=expected_destination,
            )
            return

        if scenario_name == "matrix_graph":
            self._assert_node_count("composeMatrix", count)
            self._assert_node_count("multMatrix", count)
            self._assert_node_count("decomposeMatrix", count)
            self._assert_destination(
                result.last_destination,
                expected=count > 0,
            )
            return

        raise UnsupportedScenario(scenario_name)

    def wrap_node(self, node_name: str) -> Any:
        raise UnsupportedScenario("wrap_existing")

    def scalar_plug(self, node: Any) -> Any:
        raise NotImplementedError

    def read_scalar(self, plug: Any) -> float:
        raise NotImplementedError

    def set_scalar_repeated(
        self,
        plug: Any,
        count: int,
        value: float,
    ) -> None:
        raise NotImplementedError

    def create_nodes(self, count: int) -> OperationResult:
        raise NotImplementedError

    def create_connect_chain(self, count: int) -> OperationResult:
        raise NotImplementedError

    def create_matrix_graph(self, count: int) -> OperationResult:
        raise NotImplementedError

    @staticmethod
    def _assert_node_count(node_type: str, expected: int) -> None:
        actual = len(cmds.ls(type=node_type))
        if actual != expected:
            raise AssertionError(
                f"{node_type} count was {actual}; expected {expected}"
            )

    @staticmethod
    def _assert_destination(
        destination: str | None,
        expected: bool,
    ) -> None:
        if not destination:
            if expected:
                raise AssertionError("connection destination was not returned")
            return

        actual = bool(cmds.connectionInfo(destination, isDestination=True))
        if actual != expected:
            raise AssertionError(
                f"{destination} destination state was {actual}; "
                f"expected {expected}"
            )


def run_benchmarks(
    adapters: Sequence[BaseBenchmarkAdapter],
    scenarios: Sequence[BenchmarkScenario] = DEFAULT_SCENARIOS,
    *,
    count: int = 1000,
    repeat_count: int = 5,
    warmup_count: int = 3,
) -> list[BenchmarkRecord]:
    if count < 1:
        raise ValueError("count must be at least 1")
    if repeat_count < 1:
        raise ValueError("repeat_count must be at least 1")
    if warmup_count < 0:
        raise ValueError("warmup_count must not be negative")

    timestamp = datetime.now(timezone.utc).isoformat()
    maya_version = str(cmds.about(version=True))
    python_version = platform.python_version()
    records: list[BenchmarkRecord] = []
    load_errors: dict[BaseBenchmarkAdapter, Exception] = {}

    for adapter in adapters:
        try:
            adapter.load()
        except Exception as exc:
            load_errors[adapter] = exc

    for scenario in scenarios:
        for adapter in adapters:
            load_error = load_errors.get(adapter)
            if load_error is not None:
                records.append(
                    _make_record(
                        timestamp,
                        maya_version,
                        python_version,
                        adapter,
                        scenario,
                        count,
                        repeat_index=None,
                        status="unavailable",
                        note=(
                            f"{type(load_error).__name__}: {load_error}"
                        ),
                    )
                )
                continue

            if warmup_count:
                warmup_error = _run_warmup(
                    adapter,
                    scenario,
                    min(count, warmup_count),
                )
                if warmup_error is not None:
                    status, note = warmup_error
                    records.append(
                        _make_record(
                            timestamp,
                            maya_version,
                            python_version,
                            adapter,
                            scenario,
                            count,
                            repeat_index=None,
                            status=status,
                            note=note,
                        )
                    )
                    continue

            for repeat_index in range(1, repeat_count + 1):
                record = _run_once(
                    timestamp,
                    maya_version,
                    python_version,
                    adapter,
                    scenario,
                    count,
                    repeat_index,
                )
                records.append(record)
                if record.status != "ok":
                    break

    return records


def write_csv(
    records: Iterable[BenchmarkRecord],
    output_path: str | Path,
) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = tuple(BenchmarkRecord.__dataclass_fields__)
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(asdict(record))
    return path


def print_summary(records: Sequence[BenchmarkRecord]) -> None:
    grouped: dict[tuple[str, str, str], list[float]] = {}
    other: list[BenchmarkRecord] = []
    for record in records:
        if record.status == "ok" and record.elapsed_seconds is not None:
            key = (
                record.scenario,
                record.adapter,
                record.execution_mode,
            )
            grouped.setdefault(key, []).append(record.elapsed_seconds)
        else:
            other.append(record)

    print("\nCompetitor benchmark (seconds; lower is faster)")
    for (scenario, adapter, mode), elapsed_values in grouped.items():
        median = statistics.median(elapsed_values)
        print(
            f"{scenario:24} {adapter:14} {mode:10} "
            f"median={median:.6f} "
            f"min={min(elapsed_values):.6f} "
            f"max={max(elapsed_values):.6f}"
        )

    for record in other:
        print(
            f"[{record.status}] {record.adapter}/{record.scenario}: "
            f"{record.note}"
        )


def main(
    *,
    count: int = 1000,
    repeat_count: int = 5,
    warmup_count: int = 3,
    output_path: str | Path | None = None,
    adapter_names: Sequence[str] | None = None,
    scenario_names: Sequence[str] | None = None,
) -> Path:
    from ._adapters import default_adapters

    adapters = default_adapters()
    if adapter_names is not None:
        requested_adapters = set(adapter_names)
        adapters = [
            adapter
            for adapter in adapters
            if adapter.name in requested_adapters
        ]

    scenarios = list(DEFAULT_SCENARIOS)
    if scenario_names is not None:
        requested_scenarios = set(scenario_names)
        scenarios = [
            scenario
            for scenario in scenarios
            if scenario.name in requested_scenarios
        ]

    if not adapters:
        raise ValueError("No benchmark adapters were selected")
    if not scenarios:
        raise ValueError("No benchmark scenarios were selected")

    records = run_benchmarks(
        adapters,
        scenarios,
        count=count,
        repeat_count=repeat_count,
        warmup_count=warmup_count,
    )
    if output_path is None:
        output_path = (
            _find_repo_root()
            / "benchmark_results"
            / "competitor"
            / (
                "competitor_benchmark_"
                f"{datetime.now():%Y%m%d_%H%M%S}.csv"
            )
        )
    path = write_csv(records, output_path)
    print_summary(records)
    print(f"\nCSV: {path}")
    return path


def _run_warmup(
    adapter: BaseBenchmarkAdapter,
    scenario: BenchmarkScenario,
    count: int,
) -> tuple[str, str] | None:
    cmds.file(new=True, force=True)
    try:
        state = adapter.setup_scenario(scenario.name)
        result = adapter.run_scenario(scenario.name, count, state)
        adapter.validate_scenario(scenario.name, count, state, result)
    except UnsupportedScenario as exc:
        return "unsupported", str(exc)
    except Exception as exc:
        return "error", f"warmup {type(exc).__name__}: {exc}"
    finally:
        cmds.file(new=True, force=True)
    return None


def _run_once(
    timestamp: str,
    maya_version: str,
    python_version: str,
    adapter: BaseBenchmarkAdapter,
    scenario: BenchmarkScenario,
    count: int,
    repeat_index: int,
) -> BenchmarkRecord:
    cmds.file(new=True, force=True)
    try:
        state = adapter.setup_scenario(scenario.name)
        gc.collect()
        gc_was_enabled = gc.isenabled()
        if gc_was_enabled:
            gc.disable()
        start = time.perf_counter_ns()
        try:
            result = adapter.run_scenario(scenario.name, count, state)
        finally:
            elapsed = (time.perf_counter_ns() - start) / 1_000_000_000
            if gc_was_enabled:
                gc.enable()
        adapter.validate_scenario(scenario.name, count, state, result)
    except UnsupportedScenario as exc:
        return _make_record(
            timestamp,
            maya_version,
            python_version,
            adapter,
            scenario,
            count,
            repeat_index=None,
            status="unsupported",
            note=str(exc),
        )
    except Exception as exc:
        return _make_record(
            timestamp,
            maya_version,
            python_version,
            adapter,
            scenario,
            count,
            repeat_index=repeat_index,
            status="error",
            note=f"{type(exc).__name__}: {exc}",
        )
    finally:
        cmds.file(new=True, force=True)

    return _make_record(
        timestamp,
        maya_version,
        python_version,
        adapter,
        scenario,
        count,
        repeat_index=repeat_index,
        elapsed_seconds=elapsed,
        status="ok",
    )


def _make_record(
    timestamp: str,
    maya_version: str,
    python_version: str,
    adapter: BaseBenchmarkAdapter,
    scenario: BenchmarkScenario,
    count: int,
    *,
    repeat_index: int | None,
    elapsed_seconds: float | None = None,
    status: str,
    note: str = "",
) -> BenchmarkRecord:
    operations_per_second = None
    if elapsed_seconds:
        operations_per_second = count / elapsed_seconds

    return BenchmarkRecord(
        timestamp_utc=timestamp,
        maya_version=maya_version,
        python_version=python_version,
        adapter=adapter.name,
        adapter_version=adapter.version,
        scenario=scenario.name,
        scenario_description=scenario.description,
        execution_mode=adapter.execution_mode(scenario.name),
        count=count,
        repeat_index=repeat_index,
        elapsed_seconds=elapsed_seconds,
        operations_per_second=operations_per_second,
        status=status,
        note=note,
    )


def _find_repo_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / ".git").exists():
            return parent
    return Path.cwd()


if __name__ == "__main__":
    main()
