# coding: utf-8
from __future__ import annotations

import pytest

from bd_util.maya.attr.query import (
    get_attribute_info,
    get_attribute_infos,
)


pytestmark = pytest.mark.maya


def test_get_attribute_info_includes_mfn_attribute_metadata(
    new_scene,
    maya_cmds,
):
    node = maya_cmds.createNode("transform")

    info = get_attribute_info(node, "translateX")

    assert info.long_name == "translateX"
    assert info.short_name == "tx"
    assert info.path_name == "translateX"
    assert info.enforcing_unique_name is True


def test_get_attribute_infos_includes_non_unique_attribute_metadata(
    new_scene,
    maya_cmds,
):
    try:
        maya_cmds.createNode("hierarchyTestNode4")
    except Exception as exc:
        pytest.skip(f"hierarchyTestNode4 is unavailable: {exc}")

    infos = get_attribute_infos("hierarchyTestNode4")
    by_path = {info.path_name: info for info in infos}

    assert by_path[".pnts"].long_name == ".pnts"
    assert by_path[".pnts"].short_name == ".pt"
    assert by_path[".pnts"].enforcing_unique_name is False

    assert by_path["kitA.pnts"].long_name == "kitA.pnts"
    assert by_path["kitA.pnts"].short_name == "ka.pt"
    assert by_path["kitA.pnts"].enforcing_unique_name is False
