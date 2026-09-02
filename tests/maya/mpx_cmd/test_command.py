# coding: utf-8
from __future__ import annotations

from pathlib import Path

import pytest

pytestmark = pytest.mark.maya

_TEST_PLUGIN_NAME = "bdu_mpx_command_test_plugin"
_SAMPLE_PLUGIN_NAME = "bdUtilSampleCommands"


@pytest.fixture
def mpx_test_plugin(new_scene, maya_cmds):
    plugin_path = (
        Path(__file__).resolve().parent
        / "fixtures"
        / f"{_TEST_PLUGIN_NAME}.py"
    )
    maya_cmds.loadPlugin(str(plugin_path), quiet=True)

    yield

    maya_cmds.flushUndo()
    if maya_cmds.pluginInfo(
        _TEST_PLUGIN_NAME,
        query=True,
        loaded=True,
    ):
        maya_cmds.unloadPlugin(_TEST_PLUGIN_NAME)


@pytest.fixture
def sample_commands_plugin(new_scene, maya_cmds):
    yield

    maya_cmds.flushUndo()
    if maya_cmds.pluginInfo(
        _SAMPLE_PLUGIN_NAME,
        query=True,
        loaded=True,
    ):
        maya_cmds.unloadPlugin(_SAMPLE_PLUGIN_NAME)


def test_failure_rolls_back_executed_modifier_history(
    mpx_test_plugin,
    maya_cmds,
):
    command = getattr(maya_cmds, "bduTestMpxFailAfterExecute")

    with pytest.raises(RuntimeError, match="intentional MPxCommand failure"):
        command(nodeName="bdu_mpx_failed_node")

    assert not maya_cmds.objExists("bdu_mpx_failed_node")
    assert not maya_cmds.objExists("bdu_mpx_failed_node_dg")


def test_no_op_command_does_not_enter_maya_undo_queue(
    mpx_test_plugin,
    maya_cmds,
):
    maya_cmds.flushUndo()
    command = getattr(maya_cmds, "bduTestMpxNoOp")

    raw_result = command()

    assert raw_result in ("no-op", ["no-op"])
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)


def test_typed_facade_uses_mpx_command_undo_and_redo(
    sample_commands_plugin,
    maya_cmds,
):
    from bd_util._sample.maya.mpx_cmd import create_transforms

    result = create_transforms(prefix="typedFacade", count=2)

    assert result.node_names == ("typedFacade1", "typedFacade2")
    assert all(maya_cmds.objExists(name) for name in result.node_names)

    plugin_path = Path(
        maya_cmds.pluginInfo(
            _SAMPLE_PLUGIN_NAME,
            query=True,
            path=True,
        )
    ).resolve()
    maya_version = str(maya_cmds.about(version=True)).split(".", 1)[0]
    expected_plugin_path = (
        Path(__file__).resolve().parents[3]
        / "bakedanuki"
        / "bakedanuki-util"
        / "plug-ins"
        / f"maya{maya_version}"
        / "bdUtilSampleCommands.py"
    ).resolve()
    assert plugin_path == expected_plugin_path

    maya_cmds.undo()
    assert all(not maya_cmds.objExists(name) for name in result.node_names)

    maya_cmds.redo()
    assert all(maya_cmds.objExists(name) for name in result.node_names)


def test_second_typed_facade_uses_same_plugin_and_supports_undo_and_redo(
    sample_commands_plugin,
    maya_cmds,
):
    from bd_util._sample.maya.mpx_cmd import set_transform_translation

    node_name = maya_cmds.createNode("transform", name="translateTarget")
    maya_cmds.flushUndo()

    result = set_transform_translation(
        node_name=node_name,
        translation=(1.5, -2.0, 3.25),
    )

    assert result.node_name == node_name
    assert result.translation.as_tuple() == (1.5, -2.0, 3.25)
    assert maya_cmds.getAttr(f"{node_name}.translate")[0] == pytest.approx(
        (1.5, -2.0, 3.25)
    )

    maya_cmds.undo()
    assert maya_cmds.getAttr(f"{node_name}.translate")[0] == pytest.approx(
        (0.0, 0.0, 0.0)
    )

    maya_cmds.redo()
    assert maya_cmds.getAttr(f"{node_name}.translate")[0] == pytest.approx(
        (1.5, -2.0, 3.25)
    )


def test_set_transform_translation_no_op_stays_out_of_undo_queue(
    sample_commands_plugin,
    maya_cmds,
):
    from bd_util._sample.maya.mpx_cmd import set_transform_translation

    node_name = maya_cmds.createNode("transform", name="noOpTarget")
    maya_cmds.flushUndo()

    set_transform_translation(
        node_name=node_name,
        translation=(0.0, 0.0, 0.0),
    )

    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)


def test_apply_create_transforms_can_be_used_directly(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu
    from bd_util._sample.maya.mpx_cmd import (
        CreateTransformsParams,
        apply_create_transforms,
    )

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)

    result = apply_create_transforms(
        nodes,
        CreateTransformsParams(prefix="directApply", count=2),
    )

    assert result.node_names == ("directApply1", "directApply2")
    assert all(maya_cmds.objExists(name) for name in result.node_names)

    mod.undo_it()
    assert all(not maya_cmds.objExists(name) for name in result.node_names)


def test_apply_set_transform_translation_can_be_used_directly(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu
    from bd_util._sample.maya.mpx_cmd import (
        SetTransformTranslationParams,
        apply_set_transform_translation,
    )

    node_name = maya_cmds.createNode("transform", name="directApplyTarget")
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)

    result = apply_set_transform_translation(
        nodes,
        SetTransformTranslationParams(
            node_name=node_name,
            translation=bdu.DoubleLinear3(4.0, 5.0, 6.0),
        ),
    )

    assert result.node_name == node_name
    assert result.translation.as_tuple() == (4.0, 5.0, 6.0)
    assert maya_cmds.getAttr(f"{node_name}.translate")[0] == pytest.approx(
        (4.0, 5.0, 6.0)
    )

    mod.undo_it()
    assert maya_cmds.getAttr(f"{node_name}.translate")[0] == pytest.approx(
        (0.0, 0.0, 0.0)
    )
