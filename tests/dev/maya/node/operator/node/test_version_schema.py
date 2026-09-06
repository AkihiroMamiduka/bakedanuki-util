# coding: utf-8
from __future__ import annotations

import ast
from pathlib import Path

import pytest

from bd_util._dev.maya.node.operator.node import generate_version_schema
from bd_util._dev.maya.node.operator.node import version_schema
from bd_util.maya.node._node_type_registry import NODE_TYPE_BY_CLASS_NAME
from bd_util.maya.node._node_version_registry import NODE_TYPE_VERSION_RANGES

_EXPECTED_PROFILE_COUNTS = {
    2025: 28,
    2026: 29,
    2027: 29,
}

_EXPECTED_INVENTORY_COUNTS = {
    2025: {"registered": 1417, "generated": 1297, "skipped": 120},
    2026: {"registered": 1476, "generated": 1356, "skipped": 120},
    2027: {"registered": 1485, "generated": 1365, "skipped": 120},
}

_EXPECTED_SELECTION_COUNTS = {
    2025: {
        "introduced": 0,
        "removed": 0,
        "changed": 0,
        "generation": 10,
    },
    2026: {
        "introduced": 64,
        "removed": 5,
        "changed": 89,
        "generation": 153,
    },
    2027: {
        "introduced": 9,
        "removed": 0,
        "changed": 55,
        "generation": 64,
    },
}

_VERSION_SCHEMA_PATH = Path(version_schema.__file__).resolve()
_PYTHON_ROOT = _VERSION_SCHEMA_PATH.parents[6]
_GENERATED_NODE_ROOT = (
    _PYTHON_ROOT / "bd_util" / "maya" / "node" / "operator" / "node"
)


def _collect_generated_node_types(package_name: str) -> dict[str, Path]:
    definitions: dict[str, Path] = {}
    package_dirs = sorted(
        path
        for path in _GENERATED_NODE_ROOT.rglob(package_name)
        if path.is_dir()
    )
    assert package_dirs, f"Generated package not found: {package_name}"

    for package_dir in package_dirs:
        for module_path in sorted(package_dir.glob("*.py")):
            if module_path.name == "__init__.py":
                continue

            tree = ast.parse(
                module_path.read_text(encoding="utf-8"),
                filename=str(module_path),
            )
            node_types = [
                statement.value.value
                for statement in ast.walk(tree)
                if isinstance(statement, ast.Assign)
                and any(
                    isinstance(target, ast.Name) and target.id == "NODE_TYPE"
                    for target in statement.targets
                )
                and isinstance(statement.value, ast.Constant)
                and isinstance(statement.value.value, str)
            ]
            assert len(node_types) == 1, (
                f"Expected one NODE_TYPE definition in {module_path}, "
                f"found {node_types!r}"
            )

            node_type = node_types[0]
            assert node_type not in definitions, (
                f"Duplicate NODE_TYPE {node_type!r}: "
                f"{definitions[node_type]} and {module_path}"
            )
            definitions[node_type] = module_path

    return definitions


@pytest.mark.parametrize(
    "maya_version", version_schema.SUPPORTED_MAYA_VERSIONS
)
def test_profile_and_inventory_counts(maya_version: int):
    profile_requests = version_schema.profile_plugin_requests(maya_version)
    inventory_counts = version_schema.INVENTORY_COUNTS[maya_version]

    assert len(profile_requests) == _EXPECTED_PROFILE_COUNTS[maya_version]
    assert len(set(profile_requests)) == len(profile_requests)
    assert profile_requests.count("dynamicGeometryAttributes") == (
        0 if maya_version == 2025 else 1
    )
    assert inventory_counts == _EXPECTED_INVENTORY_COUNTS[maya_version]
    assert inventory_counts["registered"] == (
        inventory_counts["generated"] + inventory_counts["skipped"]
    )


@pytest.mark.parametrize(
    "maya_version", version_schema.SUPPORTED_MAYA_VERSIONS
)
def test_version_schema_selection_counts(maya_version: int):
    expected_counts = _EXPECTED_SELECTION_COUNTS[maya_version]
    introduced = version_schema.introduced_node_types(maya_version)
    removed = version_schema.removed_node_types(maya_version)
    changed = version_schema.SCHEMA_CHANGED_NODE_TYPES_BY_VERSION.get(
        maya_version,
        (),
    )
    generation = version_schema.node_types_to_generate(maya_version)

    assert len(introduced) == expected_counts["introduced"]
    assert len(removed) == expected_counts["removed"]
    assert len(changed) == expected_counts["changed"]
    assert len(generation) == expected_counts["generation"]
    assert len(set(introduced)) == len(introduced)
    assert len(set(removed)) == len(removed)
    assert len(set(changed)) == len(changed)
    assert len(set(generation)) == len(generation)

    if maya_version == 2025:
        assert generation == version_schema.BASELINE_ADDITIONAL_NODE_TYPES
    else:
        assert set(introduced).isdisjoint(changed)
        assert set(generation) == set(introduced) | set(changed)


def test_node_version_registry_is_synchronized():
    supported_versions = version_schema.SUPPORTED_MAYA_VERSIONS
    registry_node_types = set(NODE_TYPE_VERSION_RANGES)
    registered_node_types = set(NODE_TYPE_BY_CLASS_NAME.values())
    inventory_delta_node_types: set[str] = set()

    for maya_version in supported_versions:
        introduced = set(version_schema.introduced_node_types(maya_version))
        removed = set(version_schema.removed_node_types(maya_version))
        registry_starts = {
            node_type
            for node_type, ranges in NODE_TYPE_VERSION_RANGES.items()
            if any(minimum == maya_version for minimum, _ in ranges)
        }
        registry_ends = {
            node_type
            for node_type, ranges in NODE_TYPE_VERSION_RANGES.items()
            if any(maximum == maya_version for _, maximum in ranges)
        }

        if maya_version == supported_versions[0]:
            # The baseline has no preceding supported version, so registry
            # starts at 2025 are represented by their later removal boundary.
            assert not introduced
        else:
            assert introduced == registry_starts
        assert removed == registry_ends
        inventory_delta_node_types.update(introduced)
        inventory_delta_node_types.update(removed)

    assert registry_node_types == inventory_delta_node_types
    assert registry_node_types <= registered_node_types

    for ranges in NODE_TYPE_VERSION_RANGES.values():
        for minimum, maximum in ranges:
            assert minimum in supported_versions
            assert maximum is None or maximum in supported_versions
            assert maximum is None or minimum < maximum


def test_baseline_additional_nodes_have_generated_files():
    generated_node_types = set(_collect_generated_node_types("_generated"))

    assert set(version_schema.BASELINE_ADDITIONAL_NODE_TYPES) <= (
        generated_node_types
    )


@pytest.mark.parametrize(
    ("maya_version", "expected_count"),
    [
        (2026, 153),
        (2027, 64),
    ],
)
def test_generated_overlay_node_types_match_version_schema(
    maya_version: int,
    expected_count: int,
):
    definitions = _collect_generated_node_types(
        f"_generated_maya{maya_version}"
    )
    expected_node_types = set(
        version_schema.node_types_to_generate(maya_version)
    )

    assert len(definitions) == expected_count
    assert set(definitions) == expected_node_types


@pytest.mark.parametrize("owns_standalone", [False, True])
def test_generator_main_only_cleans_up_owned_standalone(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    owns_standalone: bool,
):
    calls: list[str] = []

    monkeypatch.setattr(
        generate_version_schema,
        "_initialize_maya",
        lambda: owns_standalone,
    )
    monkeypatch.setattr(
        generate_version_schema,
        "generate_version_schema",
        lambda *args, **kwargs: calls.append("generate"),
    )
    monkeypatch.setattr(
        generate_version_schema,
        "_cleanup_mtoa",
        lambda: calls.append("cleanup"),
    )
    monkeypatch.setattr(
        "sys.argv",
        [
            "generate_version_schema.py",
            "--maya-version",
            "2026",
            "--src-dir",
            str(tmp_path),
        ],
    )

    generate_version_schema.main()

    assert calls == (
        ["generate", "cleanup"] if owns_standalone else ["generate"]
    )


@pytest.mark.parametrize("owns_standalone", [False, True])
def test_generator_main_respects_standalone_ownership_after_failure(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    owns_standalone: bool,
):
    calls: list[str] = []

    def fail_generation(*args, **kwargs):
        calls.append("generate")
        raise RuntimeError("generation failed")

    monkeypatch.setattr(
        generate_version_schema,
        "_initialize_maya",
        lambda: owns_standalone,
    )
    monkeypatch.setattr(
        generate_version_schema,
        "generate_version_schema",
        fail_generation,
    )
    monkeypatch.setattr(
        generate_version_schema,
        "_cleanup_mtoa",
        lambda: calls.append("cleanup"),
    )
    monkeypatch.setattr(
        "sys.argv",
        [
            "generate_version_schema.py",
            "--maya-version",
            "2026",
            "--src-dir",
            str(tmp_path),
        ],
    )

    with pytest.raises(RuntimeError, match="generation failed"):
        generate_version_schema.main()

    assert calls == (
        ["generate", "cleanup"] if owns_standalone else ["generate"]
    )
