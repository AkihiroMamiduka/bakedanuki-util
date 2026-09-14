"""Measure curve data in a separate mayapy process; replaces the scene."""

from __future__ import annotations

import argparse
from collections.abc import Callable, Mapping
from dataclasses import replace
import hashlib
import importlib
from itertools import product
import json
from pathlib import Path
import statistics
import subprocess
import sys
from time import perf_counter
from types import ModuleType
from typing import TYPE_CHECKING, TypeVar, TypedDict, cast

if TYPE_CHECKING:
    from maya.api.OpenMayaAnim import MFnAnimCurve

    from ...maya.node.modifier import ModifierManager
    from ...maya.node.operator.attr import (
        AnimCurveData as CurveData,
        KeyframeManager as CurveManager,
    )

_T = TypeVar("_T")


class _Range(TypedDict, total=False):
    start_frame: float
    end_frame: float
    include_boundaries: bool


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
    parser.add_argument(
        "--targets",
        nargs="+",
        default=["direct"],
        choices=["direct", "base", "additive", "override"],
    )
    parser.add_argument(
        "--layer-members",
        type=int,
        default=1,
        help="Registered plugs per layer, with the measured plug registered last",
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
        or args.layer_members < 1
        or any(n <= args.window + 2 for n in args.keys)
    ):
        parser.error(
            "repeats/window/layer-members must be positive and keys must exceed window + 2"
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

        file_command = cast(Callable[..., object], cmds.file)
        if args.source_revision:
            namespace = "bd_util.maya.node.operator.attr"
            parent = importlib.import_module(namespace)
            hashes = {}
            for name in (
                "keyframe_data",
                "_keyframe_target",
                "_keyframe_command",
                "_keyframe_snapshot",
                "keyframe",
            ):
                path = (
                    (implementation / (name + ".py"))
                    .relative_to(root)
                    .as_posix()
                )
                if (
                    name in ("_keyframe_target", "_keyframe_command")
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
                module_source = subprocess.check_output(
                    ["git", "show", f"{args.source_revision}:{path}"], cwd=root
                )
                module = ModuleType(namespace + "." + name)
                module.__file__ = path
                sys.modules[module.__name__] = module
                exec(compile(module_source, path, "exec"), module.__dict__)
                setattr(parent, name, module)
                hashes[name + ".py"] = hashlib.sha256(
                    module_source
                ).hexdigest()
            revision = args.source_revision
        AnimCurveData = cast(
            "type[CurveData]",
            importlib.import_module(
                "bd_util.maya.node.operator.attr.keyframe_data"
            ).AnimCurveData,
        )
        KeyframeManager = cast(
            "type[CurveManager]",
            importlib.import_module(
                "bd_util.maya.node.operator.attr.keyframe"
            ).KeyframeManager,
        )

        cmds.currentUnit(linear="cm", angle="deg", time="film")
        cmds.keyTangent(
            g=True,
            inTangentType="auto",
            outTangentType="auto",
            weightedTangents=False,
        )
        results: list[dict[str, object]] = []

        def timed(callback: Callable[[], _T]) -> tuple[_T, float]:
            start = perf_counter()
            value = callback()
            return value, (perf_counter() - start) * 1000

        def record(
            case: str,
            metadata: Mapping[str, object],
            run: Callable[[], dict[str, float]],
        ) -> None:
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

        def new_target(
            curve_type: str, weighted: bool, target_kind: str, count: int = 0
        ) -> tuple[CurveManager, ModifierManager, MFnAnimCurve | None]:
            node = cmds.createNode("transform")
            attribute = {
                "animCurveTA": "rx",
                "animCurveTL": "tx",
                "animCurveTU": "sx",
            }[curve_type]
            selection = om.MSelectionList()
            selection.add(node + "." + attribute)
            plug = selection.getPlug(0)
            mod = bdu.ModifierManager()
            keyframe = KeyframeManager(plug, modifier_manager=mod)
            layer = None
            if target_kind != "direct":
                layer = cast(
                    str,
                    cmds.animLayer(
                        "BenchmarkLayer", override=target_kind == "override"
                    ),
                )
                members = [
                    cmds.createNode("transform", name="background#") + ".tx"
                    for _ in range(args.layer_members - 1)
                ]
                members.append(plug.name())
                cmds.animLayer(layer, edit=True, attribute=members)
                cmds.animLayer(layer, edit=True, selected=True, preferred=True)
                if target_kind == "base":
                    layer = cast(str, cmds.animLayer(query=True, root=True))
                else:
                    keyframe = keyframe.anim_layer(layer)
            curve = None
            if count:
                if layer is None:
                    curve = oma.MFnAnimCurve()
                    curve.create(plug)
                else:
                    cmds.setKeyframe(
                        plug.name(),
                        animLayer=layer,
                        time=-1,
                        value=0,
                        noResolve=True,
                    )
                    curves = cast(
                        list[str],
                        cmds.animLayer(
                            layer, query=True, findCurveForPlug=plug.name()
                        ),
                    )
                    selection = om.MSelectionList()
                    selection.add(curves[0])
                    curve = oma.MFnAnimCurve(selection.getDependNode(0))
                    for index in reversed(range(curve.numKeys)):
                        curve.remove(index)
                curve.setIsWeighted(weighted)
                for i in range(count):
                    curve.addKey(
                        om.MTime(i, om.MTime.uiUnit()),
                        (i % 7) * 0.1,
                        oma.MFnAnimCurve.kTangentAuto,
                        oma.MFnAnimCurve.kTangentAuto,
                    )
            return keyframe, mod, curve

        for curve_type in args.curve_types:
            for weighted in (False, True):
                for count, target_kind in product(args.keys, args.targets):
                    file_command(new=True, force=True)
                    source, _, native = new_target(
                        curve_type, weighted, target_kind, count
                    )
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
                        "target": target_kind,
                        "layer_members": (
                            args.layer_members
                            if target_kind != "direct"
                            else 0
                        ),
                    }

                    if "get" in args.operations:
                        ranges: dict[str, _Range] = {
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

                                def get(
                                    method: str = method,
                                    kwargs: _Range = kwargs,
                                ) -> dict[str, float]:
                                    file_command(modified=False)
                                    getter = (
                                        source.get_key_data
                                        if method == "get_key_data"
                                        else source.get_curve_data
                                    )
                                    data, elapsed = timed(
                                        lambda: getter(**kwargs)
                                    )
                                    assert data is not None
                                    assert not file_command(
                                        q=True, modified=True
                                    )
                                    assert set(cmds.ls()) == nodes
                                    assert source.get_curve_data() == before
                                    keys = (
                                        data
                                        if isinstance(data, list)
                                        else data.keys
                                    )
                                    assert keys
                                    if kwargs:
                                        start = kwargs.get("start_frame")
                                        end = kwargs.get("end_frame")
                                        assert (
                                            start is not None
                                            and end is not None
                                        )
                                        assert all(
                                            start <= key.frame <= end
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
                                data: CurveData = data,
                                destination_count: int = destination_count,
                                full_replace: bool = full_replace,
                            ) -> dict[str, float]:
                                file_command(new=True, force=True)
                                target, mod, _ = new_target(
                                    curve_type,
                                    weighted,
                                    target_kind,
                                    destination_count,
                                )
                                before = target.get_curve_data()
                                before_nodes = set(cmds.ls())

                                def queue() -> None:
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
                                assert set(cmds.ls()) == before_nodes
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

                        def conversion(
                            full: CurveData = full,
                        ) -> dict[str, float]:
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
                        f"Measured {curve_type}, target={target_kind}, weighted={weighted}, keys={count}",
                        flush=True,
                    )

        output = {
            "maya": cmds.about(version=True),
            "revision": revision,
            "implementation_sha256": hashes,
            "benchmark_sha256": hashlib.sha256(
                Path(__file__).read_bytes()
            ).hexdigest(),
            "repeats": args.repeats,
            "window": args.window,
            "units": {"linear": "cm", "angle": "deg", "time": "film"},
            "global_tangent": "auto/nonweighted",
            "results": results,
        }
        args.output.write_text(json.dumps(output, indent=2), encoding="utf-8")
        print(f"Saved {args.output}", flush=True)
        file_command(new=True, force=True)
    finally:
        maya.standalone.uninitialize()


if __name__ == "__main__":
    main()
