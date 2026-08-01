# coding: utf-8
from __future__ import annotations

import csv

import pytest

from bd_util._test.maya.node.operator.node.bd_dbl_mult_benchmark import (
    BenchmarkRecord,
    print_summary,
    run_benchmarks,
    write_csv,
)

pytestmark = pytest.mark.maya


def _record(variant: str, milliseconds_per_frame: float) -> BenchmarkRecord:
    return BenchmarkRecord(
        timestamp_utc="2026-08-01T00:00:00+00:00",
        maya_version="2025",
        maya_api_version=20250000,
        python_version="3.11.4",
        processor="test processor",
        plugin_path="bdUtilNodes.mll",
        plugin_sha256="abc",
        variant=variant,
        input_count=3,
        dirty_pattern="all",
        evaluation_mode="parallel",
        replica_count=10,
        plugin_node_count=10,
        frame_count=20,
        repeat_index=1,
        dg_compute_count_per_frame=10.0,
        elapsed_seconds=0.02,
        milliseconds_per_frame=milliseconds_per_frame,
        network_evaluations_per_second=10000.0,
    )


def test_write_csv_preserves_measurement_metadata(tmp_path):
    output_path = write_csv([_record("fixed", 2.0)], tmp_path / "result.csv")

    with output_path.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))

    assert len(rows) == 1
    assert rows[0]["variant"] == "fixed"
    assert rows[0]["input_count"] == "3"
    assert rows[0]["dg_compute_count_per_frame"] == "10.0"


def test_print_summary_reports_fixed_to_multi_ratio(capsys):
    print_summary(
        [
            _record("fixed", 2.0),
            _record("multi", 1.0),
        ]
    )

    output = capsys.readouterr().out
    assert "fixed/multi" in output
    assert "2.000" in output


def test_run_benchmarks_rejects_input_counts_below_two(tmp_path):
    plugin_path = tmp_path / "bdUtilNodes.mll"
    plugin_path.touch()

    with pytest.raises(ValueError, match="at least 2"):
        run_benchmarks(plugin_path, input_counts=[1])
