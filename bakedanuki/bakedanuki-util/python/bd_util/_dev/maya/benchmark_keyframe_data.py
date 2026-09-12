"""Measure curve data in a separate mayapy process; replaces the scene."""

from __future__ import annotations

import argparse
from dataclasses import replace
import hashlib
import importlib
import json
from pathlib import Path
import statistics
import subprocess
import sys
from time import perf_counter
from types import ModuleType


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--keys", type=int, nargs="+", default=[100, 1000, 10000]
    )
    parser.add_argument("--window", type=int, default=10)
    parser.add_argument("--repeats", type=int, default=5)
    parser.add_argument(
        "--curve-types",
        nargs="+",
        default=["animCurveTA", "animCurveTL", "animCurveTU"],
        choices=["animCurveTA", "animCurveTL", "animCurveTU"],
    )
    parser.add_argument(
        "--operations",
        nargs="+",
        default=["get", "restore", "json"],
        choices=["get", "restore", "json"],
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--source-revision",
        help="Read the curve modules from this git revision without changing the checkout",
    )
    args = parser.parse_args()
    if (
        args.repeats < 1
        or args.window < 1
        or any(n <= args.window + 2 for n in args.keys)
    ):
        parser.error(
            "repeats/window must be positive and keys must exceed window + 2"
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Fail on an unwritable output before starting a potentially long measurement.
    args.output.open("a", encoding="utf-8").close()

    root = next(
        p for p in Path(__file__).parents if (p / "AGENTS.md").is_file()
    )
    package = root / "bakedanuki/bakedanuki-util/python"
    sys.path.insert(0, str(package))
    implementation = package / "bd_util/maya/node/operator/attr"
    revision = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=root, encoding="utf-8"
    ).strip()
    hashes = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for pattern in ("keyframe*.py", "_keyframe*.py")
        for p in sorted(implementation.glob(pattern))
    }

    import maya.standalone

    maya.standalone.initialize(name="python")
    try:
        from maya import cmds
        from maya.api import OpenMaya as om
        from maya.api import OpenMayaAnim as oma

        import bd_util as bdu

        if args.source_revision:
            namespace = "bd_util.maya.node.operator.attr"
            parent = importlib.import_module(namespace)
            hashes = {}
            for name in (
                "_keyframe_target",
                "keyframe_data",
                "_keyframe_snapshot",
                "keyframe",
            ):
                path = (
                    (implementation / (name + ".py"))
                    .relative_to(root)
                    .as_posix()
                )
                if (
                    name == "_keyframe_target"
                    and subprocess.run(
                        [
                            "git",
                            "cat-file",
                            "-e",
                            f"{args.source_revision}:{path}",
                        ],
                        cwd=root,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                    ).returncode
                ):
                    continue
                source = subprocess.check_output(
                    ["git", "show", f"{args.source_revision}:{path}"], cwd=root
                )
                module = ModuleType(namespace + "." + name)
                module.__file__ = path
                sys.modules[module.__name__] = module
                exec(compile(source, path, "exec"), module.__dict__)
                setattr(parent, name, module)
                hashes[name + ".py"] = hashlib.sha256(source).hexdigest()
            revision = args.source_revision
        AnimCurveData = importlib.import_module(
            "bd_util.maya.node.operator.attr.keyframe_data"
        ).AnimCurveData
        KeyframeManager = importlib.import_module(
            "bd_util.maya.node.operator.attr.keyframe"
        ).KeyframeManager

        cmds.currentUnit(linear="cm", angle="deg", time="film")
        cmds.keyTangent(
            g=True,
            inTangentType="auto",
            outTangentType="auto",
            weightedTangents=False,
        )
        results = []

        def timed(callback):
            start = perf_counter()
            value = callback()
            return value, (perf_counter() - start) * 1000

        def record(case, metadata, run):
            run()  # Warm-up and assertions are excluded from recorded samples.
            samples = [run() for _ in range(args.repeats)]
            results.append(
                {
                    **metadata,
                    "case": case,
                    "samples_ms": samples,
                    "median_ms": {
                        k: statistics.median(s[k] for s in samples)
                        for k in samples[0]
                    },
                }
            )

        def new_target(curve_type, weighted, count=0):
            node = cmds.createNode("transform")
            attribute = {
                "animCurveTA": "rx",
                "animCurveTL": "tx",
                "animCurveTU": "sx",
            }[curve_type]
            selection = om.MSelectionList()
            selection.add(node + "." + attribute)
            plug = selection.getPlug(0)
            curve = None
            if count:
                curve = oma.MFnAnimCurve()
                curve.create(plug)
                curve.setIsWeighted(weighted)
                for i in range(count):
                    curve.addKey(
                        om.MTime(i, om.MTime.uiUnit()),
                        (i % 7) * 0.1,
                        oma.MFnAnimCurve.kTangentAuto,
                        oma.MFnAnimCurve.kTangentAuto,
                    )
            mod = bdu.ModifierManager()
            return KeyframeManager(plug, modifier_manager=mod), mod, curve

        for curve_type in args.curve_types:
            for weighted in (False, True):
                for count in args.keys:
                    cmds.file(new=True, force=True)
                    source, _, native = new_target(curve_type, weighted, count)
                    full = source.get_curve_data()
                    assert full is not None and native is not None
                    middle = (count - args.window) // 2
                    partial = replace(
                        full, keys=full.keys[middle : middle + args.window]
                    )
                    metadata = {
                        "curve_type": curve_type,
                        "weighted": weighted,
                        "source_keys": count,
                    }

                    if "get" in args.operations:
                        ranges = {
                            "full": {},
                            "existing": {
                                "start_frame": middle,
                                "end_frame": middle + args.window - 1,
                                "include_boundaries": False,
                            },
                            "clip_exact": {
                                "start_frame": middle,
                                "end_frame": middle + args.window - 1,
                            },
                            "clip_between": {
                                "start_frame": middle - 0.25,
                                "end_frame": middle + args.window - 0.75,
                            },
                            "clip_constant": {
                                "start_frame": -2,
                                "end_frame": -1,
                            },
                            "clip_linear": {
                                "start_frame": count,
                                "end_frame": count + 1,
                            },
                        }
                        native.setPostInfinityType(oma.MFnAnimCurve.kLinear)
                        before = source.get_curve_data()
                        nodes = set(cmds.ls())
                        for method in ("get_key_data", "get_curve_data"):
                            for case, kwargs in ranges.items():

                                def get(method=method, kwargs=kwargs):
                                    cmds.file(modified=False)
                                    data, elapsed = timed(
                                        lambda: getattr(source, method)(
                                            **kwargs
                                        )
                                    )
                                    assert not cmds.file(q=True, modified=True)
                                    assert set(cmds.ls()) == nodes
                                    assert source.get_curve_data() == before
                                    keys = (
                                        data.keys
                                        if isinstance(data, AnimCurveData)
                                        else data
                                    )
                                    assert keys
                                    if kwargs:
                                        assert all(
                                            kwargs["start_frame"]
                                            <= key.frame
                                            <= kwargs["end_frame"]
                                            for key in keys
                                        )
                                    return {"get": elapsed}

                                record(method + "/" + case, metadata, get)

                    if "restore" in args.operations:
                        for case, data, destination_count, full_replace in (
                            ("new_full", full, 0, True),
                            ("replace_full", full, count, True),
                            ("new_partial", partial, 0, False),
                            ("overwrite_partial", partial, count, False),
                        ):

                            def restore(
                                data=data,
                                destination_count=destination_count,
                                full_replace=full_replace,
                            ):
                                cmds.file(new=True, force=True)
                                target, mod, _ = new_target(
                                    curve_type, weighted, destination_count
                                )
                                before = target.get_curve_data()

                                def queue():
                                    if full_replace:
                                        target.set_curve_data(data)
                                    else:
                                        target.set_key_data(
                                            data.keys,
                                            seconds_per_frame=data.seconds_per_frame,
                                        )

                                _, queue_ms = timed(queue)
                                _, execute_ms = timed(mod.do_it_dg)
                                after = target.get_curve_data()
                                assert after is not None
                                assert len(after.keys) == (
                                    len(data.keys)
                                    if full_replace or not destination_count
                                    else destination_count
                                )
                                actual = {
                                    key.frame: key.value for key in after.keys
                                }
                                assert all(
                                    abs(actual[key.frame] - key.value) < 1e-8
                                    for key in data.keys
                                )
                                _, undo_ms = timed(mod.undo_it)
                                assert target.get_curve_data() == before
                                _, redo_ms = timed(mod.redo_it)
                                assert target.get_curve_data() == after
                                mod.undo_it()
                                assert target.get_curve_data() == before
                                mod.redo_it()
                                assert target.get_curve_data() == after
                                mod.clear()
                                return {
                                    "queue": queue_ms,
                                    "execute": execute_ms,
                                    "total": queue_ms + execute_ms,
                                    "undo": undo_ms,
                                    "redo": redo_ms,
                                }

                            record(
                                case,
                                {
                                    **metadata,
                                    "input_keys": len(data.keys),
                                    "destination_keys": destination_count,
                                },
                                restore,
                            )

                    if "json" in args.operations:

                        def conversion():
                            mapping, to_ms = timed(full.to_dict)
                            encoded, encode_ms = timed(
                                lambda: json.dumps(mapping)
                            )
                            decoded, decode_ms = timed(
                                lambda: json.loads(encoded)
                            )
                            data, from_ms = timed(
                                lambda: AnimCurveData.from_dict(decoded)
                            )
                            assert data == full
                            return {
                                "to_dict": to_ms,
                                "json_dumps": encode_ms,
                                "json_loads": decode_ms,
                                "from_dict": from_ms,
                            }

                        record("json", metadata, conversion)
                    print(
                        f"Measured {curve_type}, weighted={weighted}, keys={count}",
                        flush=True,
                    )

        output = {
            "maya": cmds.about(version=True),
            "revision": revision,
            "implementation_sha256": hashes,
            "repeats": args.repeats,
            "window": args.window,
            "units": {"linear": "cm", "angle": "deg", "time": "film"},
            "global_tangent": "auto/nonweighted",
            "results": results,
        }
        args.output.write_text(json.dumps(output, indent=2), encoding="utf-8")
        print(f"Saved {args.output}", flush=True)
        cmds.file(new=True, force=True)
    finally:
        maya.standalone.uninitialize()


if __name__ == "__main__":
    main()
