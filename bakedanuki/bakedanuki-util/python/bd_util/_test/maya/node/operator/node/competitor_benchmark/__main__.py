# coding: utf-8
from __future__ import annotations

import argparse

import maya.standalone

from ._core import main


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run bakedanuki-util competitor benchmarks in Maya.",
    )
    parser.add_argument("--count", type=int, default=1000)
    parser.add_argument("--repeat-count", type=int, default=5)
    parser.add_argument("--warmup-count", type=int, default=3)
    parser.add_argument("--output-path")
    parser.add_argument(
        "--adapter",
        action="append",
        dest="adapter_names",
        help="Adapter name to include. Repeat to select multiple adapters.",
    )
    parser.add_argument(
        "--scenario",
        action="append",
        dest="scenario_names",
        help="Scenario name to include. Repeat to select multiple scenarios.",
    )
    return parser.parse_args()


def _run() -> None:
    args = _parse_args()
    maya.standalone.initialize(name="python")
    try:
        main(
            count=args.count,
            repeat_count=args.repeat_count,
            warmup_count=args.warmup_count,
            output_path=args.output_path,
            adapter_names=args.adapter_names,
            scenario_names=args.scenario_names,
        )
    finally:
        maya.standalone.uninitialize()


if __name__ == "__main__":
    _run()
