# coding: utf-8
from __future__ import annotations

from pathlib import Path
import re

from maya.api import OpenMaya as om

from ._node_version_registry import NODE_TYPE_VERSION_RANGES

SUPPORTED_MAYA_VERSIONS = (2025, 2026, 2027)


def _node_name_to_module_name(node_name: str) -> str:
    module_name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", node_name)
    module_name = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", module_name)
    return module_name.lower().lstrip("_")


_VERSIONED_NODE_TYPE_BY_MODULE_NAME = {
    _node_name_to_module_name(node_type): node_type
    for node_type in NODE_TYPE_VERSION_RANGES
}


def maya_major_version() -> int:
    """実行中の Maya のメジャーバージョンを返す。"""
    return int(om.MGlobal.apiVersion()) // 10000


def is_node_type_available(
    node_type: str,
    maya_version: int | None = None,
) -> bool:
    """ノード型が指定した Maya 版で利用できるかを返す。省略時は実行中の版を使う。"""
    if maya_version is None:
        maya_version = maya_major_version()

    ranges = NODE_TYPE_VERSION_RANGES.get(node_type, ((2025, None),))
    return any(
        maya_version >= minimum and (maximum is None or maya_version < maximum)
        for minimum, maximum in ranges
    )


def require_node_type_available(
    node_type: str,
    maya_version: int | None = None,
) -> None:
    """ノード型が指定した Maya 版に非対応なら例外を送出する。"""
    if maya_version is None:
        maya_version = maya_major_version()
    if not is_node_type_available(node_type, maya_version):
        raise AttributeError(
            f"Node type {node_type!r} is unavailable in Maya {maya_version}."
        )


def require_node_name_available(
    node_name: str,
    maya_version: int | None = None,
) -> None:
    """ノード名に対応する型が指定した Maya 版で利用できるか検証する。"""
    module_name = _node_name_to_module_name(node_name)
    node_type = _VERSIONED_NODE_TYPE_BY_MODULE_NAME.get(module_name)
    if node_type is not None:
        require_node_type_available(node_type, maya_version)


def configure_generated_package_path(
    package_path: list[str],
    package_file: str,
) -> None:
    """実行中の Maya 用の差分 schema を検索パスの先頭に追加する。"""
    baseline_path = Path(package_file).resolve().parent
    maya_version = maya_major_version()
    overlay_paths = [
        baseline_path.with_name(f"{baseline_path.name}_maya{version}")
        for version in reversed(SUPPORTED_MAYA_VERSIONS)
        if 2025 < version <= maya_version
    ]

    ordered_paths = [str(path) for path in overlay_paths if path.is_dir()] + [
        str(baseline_path)
    ]
    existing_paths = [
        path
        for path in package_path
        if str(Path(path).resolve()) not in ordered_paths
    ]
    package_path[:] = ordered_paths + existing_paths
