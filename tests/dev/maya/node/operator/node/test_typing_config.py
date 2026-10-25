# coding: utf-8
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest


@pytest.fixture(scope="module")
def typing_package(tmp_path_factory):
    import bd_util

    python_root = Path(bd_util.__file__).resolve().parent.parent
    target = tmp_path_factory.mktemp("typing_package") / "python"
    shutil.copytree(
        python_root,
        target,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )
    return target


def _check_typing(
    project_dir: Path,
    python_root: Path,
    profile: str,
    *,
    override: str | None = None,
) -> None:
    repo_root = Path(__file__).resolve().parents[6]
    stub_dir = project_dir / "typings"
    stub_dir.mkdir()
    if override is not None:
        (stub_dir / "bd_util_typing_config.pyi").write_text(
            override, encoding="utf-8"
        )

    if profile == "Maya2025":
        input_type = "DoubleLinearPlugOperator"
    elif profile == "Maya2025Plus":
        input_type = "DoubleLinearPlugOperator | DoublePlugOperator"
    else:
        input_type = "DoublePlugOperator"
    source = f"""\
from typing import assert_type

import bd_util as bdu
from bd_util.typing_profiles import {profile} as ExpectedNodes, Maya2025, Maya2027
from bd_util.maya.node import Nodes
from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric.range.double import DoublePlugOperator
from bd_util.maya.node.operator.attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearPlugOperator

bd_nodes = bdu.Nodes(namespace=":rig")
assert_type(bd_nodes, ExpectedNodes)
assert_type(Nodes(), ExpectedNodes)
assert_type(bdu.Nodes(typing_maya_version=None), ExpectedNodes)
assert_type(bd_nodes.set_namespace(":other"), ExpectedNodes)
assert_type(bd_nodes.create.absolute().input, {input_type})
assert_type(bd_nodes.existing.absolute("existing").input, {input_type})
transform, shape = bd_nodes.create.with_transform.mesh()
assert_type(transform.translateX.get(), float)
assert_type(shape.intermediateObject.get(), bool)
assert_type(bdu.Nodes(typing_maya_version="2025"), Maya2025)
assert_type(bdu.Nodes(typing_maya_version="2027"), Maya2027)
assert_type(bdu.Nodes(typing_maya_version="2025").create.absolute().input, DoubleLinearPlugOperator)
assert_type(bdu.Nodes(typing_maya_version="2027").create.absolute().input, DoublePlugOperator)
bdu.node_types.AbsoluteDL  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
"""
    node_type = "addDoubleLinear" if profile == "Maya2025" else "absoluteDL"
    suffix = (
        "  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]"
        if profile == "Maya2025Plus"
        else ""
    )
    source += f"bd_nodes.create.{node_type}(){suffix}\n"
    source += f'bd_nodes.existing.{node_type}("existing"){suffix}\n'
    suffix = (
        ""
        if profile in ("Maya2027", "Maya2027Plus")
        else "  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]"
    )
    source += f"bd_nodes.create.shotLabel(){suffix}\n"
    (project_dir / "contract.py").write_text(source, encoding="utf-8")

    config_path = project_dir / "pyrightconfig.json"
    config_path.write_text(
        json.dumps(
            {
                "extends": str(repo_root / "pyrightconfig.json"),
                "include": ["contract.py"],
                "extraPaths": [str(python_root), str(repo_root / "typings")],
                "stubPath": "typings",
            }
        ),
        encoding="utf-8",
    )
    environment = os.environ.copy()
    environment["PYTHONPATH"] = os.pathsep.join(
        filter(
            None,
            (str(repo_root / ".typecheck"), environment.get("PYTHONPATH")),
        )
    )
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pyright",
            "--project",
            str(config_path),
            "--pythonpath",
            sys.executable,
            "--outputjson",
        ],
        cwd=project_dir,
        env=environment,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=120,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    summary = json.loads(result.stdout)["summary"]
    assert summary["errorCount"] == summary["warningCount"] == 0, result.stdout


@pytest.mark.parametrize("profile", ("Maya2025Plus", "Maya2026Plus"))
def test_package_typing_default(tmp_path, typing_package, profile):
    (typing_package / "bd_util" / "config" / "typing.pyi").write_text(
        f"from ..typing_profiles import {profile} as DefaultNodes\n",
        encoding="utf-8",
    )
    _check_typing(tmp_path, typing_package, profile)


@pytest.mark.parametrize(
    "profile",
    (
        "Maya2025",
        "Maya2026",
        "Maya2027",
        "Maya2025Plus",
        "Maya2026Plus",
        "Maya2027Plus",
    ),
)
def test_project_typing_override(tmp_path, typing_package, profile):
    default_profile = "Maya2025Plus" if profile == "Maya2027" else "Maya2027"
    (typing_package / "bd_util" / "config" / "typing.pyi").write_text(
        f"from ..typing_profiles import {default_profile} as DefaultNodes\n",
        encoding="utf-8",
    )
    _check_typing(
        tmp_path,
        typing_package,
        profile,
        override=(
            f"from bd_util.typing_profiles import {profile} as DefaultNodes\n"
        ),
    )


def test_project_typing_template(tmp_path, typing_package):
    template_dir = (
        typing_package / "bd_util" / "config" / "templates" / "project"
    )
    _check_typing(
        tmp_path,
        typing_package,
        "Maya2026Plus",
        override=(
            template_dir / "typings" / "bd_util_typing_config.pyi"
        ).read_text(encoding="utf-8"),
    )


def test_stub_regeneration_preserves_typing_default(tmp_path, typing_package):
    settings_path = typing_package / "bd_util" / "config" / "typing.pyi"
    settings = "from ..typing_profiles import Maya2026Plus as DefaultNodes\n"
    settings_path.write_text(settings, encoding="utf-8")
    generator_path = (
        typing_package
        / "bd_util"
        / "_dev"
        / "maya"
        / "node"
        / "operator"
        / "node"
        / "generate_existing_node_stub.py"
    )
    result = subprocess.run(
        [sys.executable, str(generator_path)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=120,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert settings_path.read_text(encoding="utf-8") == settings
    _check_typing(tmp_path, typing_package, "Maya2026Plus")
