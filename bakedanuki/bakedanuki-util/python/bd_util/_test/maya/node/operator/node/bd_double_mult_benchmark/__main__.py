# coding: utf-8
from __future__ import annotations

import argparse

import maya.standalone

from ._core import DEFAULT_INPUT_COUNTS, DIRTY_PATTERNS, EVALUATION_MODES, main


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Benchmark bdDoubleMult chains against bdDoubleMultMulti."
        ),
    )
    parser.add_argument("--plugin-path", required=True)
    parser.add_argument(
        "--input-count",
        action="append",
        dest="input_counts",
        type=int,
        help="Input count to measure. Repeat to select multiple counts.",
    )
    parser.add_argument(
        "--dirty-pattern",
        action="append",
        choices=DIRTY_PATTERNS,
        dest="dirty_patterns",
        help="Dirty pattern to measure. Repeat to select multiple patterns.",
    )
    parser.add_argument(
        "--evaluation-mode",
        action="append",
        choices=EVALUATION_MODES,
        dest="evaluation_modes",
        help="Evaluation mode to measure. Repeat to select multiple modes.",
    )
    parser.add_argument("--replica-count", type=int, default=500)
    parser.add_argument("--frame-count", type=int, default=80)
    parser.add_argument("--repeat-count", type=int, default=7)
    parser.add_argument("--warmup-count", type=int, default=2)
    parser.add_argument("--output-path")
    args = parser.parse_args()
    if args.input_counts is None:
        args.input_counts = list(DEFAULT_INPUT_COUNTS)
    if args.dirty_patterns is None:
        args.dirty_patterns = list(DIRTY_PATTERNS)
    if args.evaluation_modes is None:
        args.evaluation_modes = list(EVALUATION_MODES)
    return args


def _run() -> None:
    args = _parse_args()
    maya.standalone.initialize(name="python")
    try:
        main(
            plugin_path=args.plugin_path,
            input_counts=args.input_counts,
            dirty_patterns=args.dirty_patterns,
            evaluation_modes=args.evaluation_modes,
            replica_count=args.replica_count,
            frame_count=args.frame_count,
            repeat_count=args.repeat_count,
            warmup_count=args.warmup_count,
            output_path=args.output_path,
        )
    finally:
        maya.standalone.uninitialize()


if __name__ == "__main__":
    _run()
