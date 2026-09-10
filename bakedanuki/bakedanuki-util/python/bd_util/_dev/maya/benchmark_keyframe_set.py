# coding: utf-8
"""Run with mayapy in a separate process; this benchmark replaces the scene."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import statistics
import subprocess
import sys
from time import perf_counter
from types import ModuleType

BASELINE_REVISION = "1172c8db4eb6503d5eed42c208774192d69d2592"
KEYFRAME_PATH = (
    "bakedanuki/bakedanuki-util/python/"
    "bd_util/maya/node/operator/attr/keyframe.py"
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--keys", type=int, nargs="+", default=[10, 100, 1000])
    parser.add_argument("--repeats", type=int, default=5)
    parser.add_argument("--baseline", default=BASELINE_REVISION)
    args = parser.parse_args()
    if args.repeats < 1 or any(count < 1 for count in args.keys):
        parser.error("keys and repeats must be positive")

    root = next(
        parent
        for parent in Path(__file__).parents
        if (parent / "AGENTS.md").is_file()
    )
    sys.path.insert(0, str(root / "bakedanuki/bakedanuki-util/python"))
    baseline_source = subprocess.check_output(
        ["git", "show", f"{args.baseline}:{KEYFRAME_PATH}"],
        cwd=root,
        encoding="utf-8",
    )
    import maya.standalone

    maya.standalone.initialize(name="python")
    try:
        from maya import cmds
        from maya.api import OpenMayaAnim as oma

        import bd_util as bdu

        baseline = ModuleType(
            "bd_util.maya.node.operator.attr._benchmark_baseline"
        )
        exec(
            compile(baseline_source, KEYFRAME_PATH, "exec"), baseline.__dict__
        )
        cmds.currentUnit(linear="cm", angle="deg", time="film")
        cmds.keyTangent(
            g=True,
            inTangentType="auto",
            outTangentType="auto",
            weightedTangents=False,
        )

        def snapshot(keyframe):
            source = keyframe.plug.sourceWithConversion()
            if source.isNull:
                return None
            curve = oma.MFnAnimCurve(source.node())
            return [
                (
                    curve.input(index).value,
                    curve.value(index),
                    curve.inTangentType(index),
                    curve.outTangentType(index),
                )
                for index in range(curve.numKeys)
            ]

        def run(backend, case, count):
            cmds.file(new=True, force=True)
            name = cmds.createNode("transform")
            if case != "new":
                frames = range(count) if case == "overwrite" else [0]
                for frame in frames:
                    cmds.setKeyframe(
                        name + ".tx",
                        time=frame,
                        value=frame,
                        inTangentType="linear",
                        outTangentType="linear",
                    )
            manager = bdu.ModifierManager()
            keyframe = (
                bdu.Nodes(modifier_manager=manager).existing(name).tx.keyframe
            )
            if backend == "cmds_baseline":
                keyframe = baseline.KeyframeManager(
                    keyframe.plug, modifier_manager=manager
                )
                # The historical baseline predates the set_key() rename.
                set_key = keyframe.set
            else:
                set_key = keyframe.set_key
            before = snapshot(keyframe)
            start = perf_counter()
            for frame in range(count):
                set_key(
                    frame + 1,
                    frame,
                    in_tangent_type="linear",
                    out_tangent_type="linear",
                )
            queued = perf_counter()
            manager.do_it_dg()
            done = perf_counter()
            after = snapshot(keyframe)
            assert after == [
                (
                    float(frame),
                    float(frame + 1),
                    oma.MFnAnimCurve.kTangentLinear,
                    oma.MFnAnimCurve.kTangentLinear,
                )
                for frame in range(count)
            ]
            undo_start = perf_counter()
            manager.undo_it()
            undo_end = perf_counter()
            assert snapshot(keyframe) == before
            redo_start = perf_counter()
            manager.redo_it()
            redo_end = perf_counter()
            assert snapshot(keyframe) == after
            manager.undo_it()
            assert snapshot(keyframe) == before
            manager.redo_it()
            assert snapshot(keyframe) == after
            manager.clear()
            return [
                (queued - start) * 1000,
                (done - queued) * 1000,
                (done - start) * 1000,
                (undo_end - undo_start) * 1000,
                (redo_end - redo_start) * 1000,
            ]

        results = []
        for case in ("new", "existing", "overwrite"):
            for count in args.keys:
                samples = {
                    backend: [] for backend in ("cmds_baseline", "current")
                }
                for repeat in range(args.repeats + 1):
                    order = list(samples)
                    if repeat % 2:
                        order.reverse()
                    for backend in order:
                        sample = run(backend, case, count)
                        if repeat:
                            samples[backend].append(sample)
                for backend, rows in samples.items():
                    results.append(
                        {
                            "case": case,
                            "keys": count,
                            "backend": backend,
                            **{
                                label: round(
                                    statistics.median(
                                        row[index] for row in rows
                                    ),
                                    4,
                                )
                                for index, label in enumerate(
                                    (
                                        "queue_ms",
                                        "flush_ms",
                                        "total_ms",
                                        "undo_ms",
                                        "redo_ms",
                                    )
                                )
                            },
                        }
                    )
        print(
            json.dumps(
                {
                    "maya": cmds.about(version=True),
                    "baseline": args.baseline,
                    "repeats": args.repeats,
                    "results": results,
                }
            )
        )
        cmds.file(new=True, force=True)
    finally:
        maya.standalone.uninitialize()


if __name__ == "__main__":
    main()
