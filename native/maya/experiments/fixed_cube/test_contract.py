"""固定 Cube 研究ノードの登録・保存・親変換を Maya 上で検証する。"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import sys

import pytest
from maya import cmds

if __name__ == "__main__":
    import maya.standalone

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plugin", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--module-search", action="store_true")
    args = parser.parse_args()
    maya.standalone.initialize(name="python")
    plugin = args.plugin.resolve(strict=True)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    plugin_name = cmds.loadPlugin(
        plugin.name if args.module_search else str(plugin), quiet=True
    )[0]
    actual_plugin = Path(
        cmds.pluginInfo(plugin_name, query=True, path=True)
    ).resolve()
    assert actual_plugin == plugin
    assert (
        int(cmds.pluginInfo(plugin_name, query=True, apiVersion=True)) // 10000
        == int(cmds.about(apiVersion=True)) // 10000
    )
    if args.module_search:
        module_path = Path(
            cmds.moduleInfo(moduleName="bd_util", path=True)
        ).resolve()
        assert module_path == plugin.parents[2]
    print(f"Loaded fixed Cube: {actual_plugin}", flush=True)
    test_path = (
        Path(__file__).resolve().parents[4]
        / "tests/maya/node/operator/node/dag/shape/test_bd_shp_l_cube.py"
    )
    os.environ["BD_FIXED_CUBE_PLUGIN_PATH"] = str(plugin)
    os.environ["BD_FIXED_CUBE_PLUGIN_NAME"] = plugin_name
    exit_code = pytest.main(
        [
            str(test_path),
            "-q",
            "-p",
            "no:cacheprovider",
            "--confcutdir",
            str(test_path.parent),
            "--basetemp",
            str(output / "tmp"),
            "--junitxml",
            str(output / "junit.xml"),
        ]
    )
    cmds.file(new=True, force=True)
    assert cmds.pluginInfo(plugin_name, query=True, loaded=True)
    cmds.unloadPlugin(plugin_name)
    assert not cmds.pluginInfo(plugin_name, query=True, loaded=True)
    plugin_name = cmds.loadPlugin(
        plugin.name if args.module_search else str(plugin), quiet=True
    )[0]
    shape = cmds.createNode("bdShpL_Cube")
    assert cmds.nodeType(shape) == "bdShpL_Cube"
    cmds.file(new=True, force=True)
    cmds.unloadPlugin(plugin_name)
    assert not cmds.pluginInfo(plugin_name, query=True, loaded=True)
    print("Unload / reload / create / unload passed", flush=True)
    maya.standalone.uninitialize()
    sys.exit(int(exit_code))
