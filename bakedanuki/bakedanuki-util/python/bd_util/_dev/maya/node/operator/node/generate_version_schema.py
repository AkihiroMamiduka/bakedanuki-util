# coding: utf-8
from __future__ import annotations

import argparse
from pathlib import Path

from .version_schema import (
    SUPPORTED_MAYA_VERSIONS,
    node_types_to_generate,
    profile_plugin_requests,
)


def _running_maya_version() -> int:
    from maya.api import OpenMaya as om

    return int(om.MGlobal.apiVersion()) // 10000


def _initialize_maya() -> bool:
    import maya.standalone

    try:
        maya.standalone.initialize(name="python")
    except RuntimeError:
        # Script Editor から呼ぶ場合は Maya が初期化済みなので、その状態を維持する。
        return False
    return True


def _load_profile(maya_version: int) -> None:
    import maya.cmds as cmds

    for plugin_name in profile_plugin_requests(maya_version):
        if cmds.pluginInfo(plugin_name, query=True, loaded=True):
            continue
        cmds.loadPlugin(plugin_name, quiet=True)


def _cleanup_mtoa() -> None:
    import maya.cmds as cmds

    cmds.file(new=True, force=True)
    if cmds.pluginInfo("mtoa", query=True, loaded=True):
        cmds.unloadPlugin("mtoa", force=True)


def generate_version_schema(
    maya_version: int,
    src_dir: str | Path,
    *,
    shard_index: int = 0,
    shard_count: int = 1,
) -> tuple[str, ...]:
    """指定した Maya 版の差分ノードを選び、対応する生成ファイルを書き出す。

    Args:
        maya_version: 実行中の Maya と一致させる対象バージョン。
        src_dir: `bd_util` パッケージの親ディレクトリ。
        shard_index: 分割実行する際の担当番号。0 から数える。
        shard_count: 分割数。1 以上を指定する。

    Returns:
        この分割で生成対象になったノード型名。

    Raises:
        ValueError: 未対応の `maya_version`、または無効な分割指定の場合。
        RuntimeError: 実行中の Maya 版が `maya_version` と異なる場合。
    """
    from .generate import generate_node_class_file

    if maya_version not in SUPPORTED_MAYA_VERSIONS:
        raise ValueError(f"Unsupported Maya version: {maya_version}")
    if shard_count < 1:
        raise ValueError("shard_count must be at least 1")
    if not 0 <= shard_index < shard_count:
        raise ValueError("shard_index must be within shard_count")

    running_version = _running_maya_version()
    if running_version != maya_version:
        raise RuntimeError(
            "Schema generation must run in the matching Maya: "
            f"requested {maya_version}, running {running_version}."
        )

    _load_profile(maya_version)
    selected_node_types = node_types_to_generate(maya_version)[
        shard_index::shard_count
    ]
    for node_type in selected_node_types:
        print(f"Generating Maya {maya_version}: {node_type}")
        generate_node_class_file(
            node_type,
            src_dir,
            node_kind="auto",
            maya_version=maya_version,
        )
    return selected_node_types


def main() -> None:
    """CLI 引数に従い、必要なら Maya を初期化して差分 schema を生成する。"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--maya-version",
        type=int,
        choices=SUPPORTED_MAYA_VERSIONS,
        required=True,
    )
    parser.add_argument(
        "--src-dir",
        type=Path,
        default=Path(__file__).resolve().parents[6],
    )
    parser.add_argument("--shard-index", type=int, default=0)
    parser.add_argument("--shard-count", type=int, default=1)
    args = parser.parse_args()

    owns_standalone = _initialize_maya()
    try:
        generate_version_schema(
            args.maya_version,
            args.src_dir,
            shard_index=args.shard_index,
            shard_count=args.shard_count,
        )
    finally:
        if owns_standalone:
            _cleanup_mtoa()


if __name__ == "__main__":
    main()
