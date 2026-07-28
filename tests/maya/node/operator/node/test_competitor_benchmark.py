# coding: utf-8
from __future__ import annotations

import csv

import pytest

from bd_util._test.maya.node.operator.node.competitor_benchmark import (
    BenchmarkScenario,
    run_benchmarks,
    write_csv,
)
from bd_util._test.maya.node.operator.node.competitor_benchmark._adapters import (
    CmdsAdapter,
)

pytestmark = pytest.mark.maya


def test_run_benchmarks_records_each_successful_repeat():
    scenario = BenchmarkScenario(
        "create_connect_chain",
        "test scenario",
    )

    records = run_benchmarks(
        [CmdsAdapter()],
        [scenario],
        count=2,
        repeat_count=2,
        warmup_count=1,
    )

    assert len(records) == 2
    assert [record.repeat_index for record in records] == [1, 2]
    assert all(record.status == "ok" for record in records)
    assert all(record.elapsed_seconds is not None for record in records)
    assert all(record.operations_per_second is not None for record in records)
    assert all(record.execution_mode == "immediate" for record in records)


def test_run_benchmarks_records_unsupported_scenario_once():
    scenario = BenchmarkScenario("wrap_existing", "test scenario")

    records = run_benchmarks(
        [CmdsAdapter()],
        [scenario],
        count=2,
        repeat_count=3,
        warmup_count=1,
    )

    assert len(records) == 1
    assert records[0].status == "unsupported"
    assert records[0].repeat_index is None
    assert "no node wrapper" in records[0].note


def test_write_csv_preserves_measurement_metadata(tmp_path):
    scenario = BenchmarkScenario("create_nodes", "test scenario")
    records = run_benchmarks(
        [CmdsAdapter()],
        [scenario],
        count=1,
        repeat_count=1,
        warmup_count=0,
    )

    output_path = write_csv(records, tmp_path / "result.csv")

    with output_path.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))

    assert len(rows) == 1
    assert rows[0]["adapter"] == "maya.cmds"
    assert rows[0]["scenario"] == "create_nodes"
    assert rows[0]["count"] == "1"
    assert rows[0]["status"] == "ok"


@pytest.mark.parametrize(
    ("keyword", "value"),
    (
        ("count", 0),
        ("repeat_count", 0),
        ("warmup_count", -1),
    ),
)
def test_run_benchmarks_rejects_invalid_counts(keyword, value):
    arguments = {
        "count": 1,
        "repeat_count": 1,
        "warmup_count": 0,
    }
    arguments[keyword] = value

    with pytest.raises(ValueError):
        run_benchmarks(
            [CmdsAdapter()],
            [],
            **arguments,
        )
