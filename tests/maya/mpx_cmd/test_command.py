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


def test_failure_during_modifier_execution_rolls_back_partial_edits(
    mpx_test_plugin,
    maya_cmds,
):
    node_name = maya_cmds.createNode(
        "transform", name="bdu_mpx_failure_target"
    )
    maya_cmds.flushUndo()
    command = getattr(maya_cmds, "bduTestMpxFailDuringExecute")

    with pytest.raises(RuntimeError):
        command(nodeName=node_name)

    assert not maya_cmds.objExists(f"{node_name}_dag")
    assert maya_cmds.getAttr(f"{node_name}.translateY") == 0.0
    assert not maya_cmds.listConnections(
        f"{node_name}.translateX", source=True, destination=False
    )
    assert not maya_cmds.ls(type="animCurve")
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)


@pytest.mark.parametrize("locked", [False, True])
def test_keyframe_set_uses_command_undo_redo_and_failure_rollback(
    mpx_test_plugin,
    maya_cmds,
    locked,
):
    node_name = maya_cmds.createNode("transform", name="keyframeTarget")
    if locked:
        maya_cmds.setAttr(f"{node_name}.translateY", lock=True)
    maya_cmds.flushUndo()
    command = getattr(maya_cmds, "bduTestMpxSetKeyframes")

    if locked:
        with pytest.raises(RuntimeError):
            command(nodeName=node_name)
        assert maya_cmds.getAttr(f"{node_name}.scaleX") == 1.0
        assert not maya_cmds.ls(type="animCurve")
        assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
        return

    command(nodeName=node_name)
    for _ in range(2):
        assert maya_cmds.getAttr(f"{node_name}.scaleX") == 2.0
        assert maya_cmds.keyframe(
            f"{node_name}.translateX", query=True, valueChange=True
        ) == [10.0]
        assert maya_cmds.keyframe(
            f"{node_name}.translateY", query=True, valueChange=True
        ) == [20.0]
        maya_cmds.undo()
        assert maya_cmds.getAttr(f"{node_name}.scaleX") == 1.0
        assert not maya_cmds.ls(type="animCurve")
        assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
        maya_cmds.redo()


def _animation_state(maya_cmds, plug_name):
    return (
        maya_cmds.keyframe(plug_name, query=True, timeChange=True),
        maya_cmds.keyframe(plug_name, query=True, valueChange=True),
        maya_cmds.keyTangent(plug_name, query=True, inTangentType=True),
        maya_cmds.keyTangent(plug_name, query=True, outTangentType=True),
        maya_cmds.listConnections(
            plug_name, source=True, destination=False, plugs=True
        ),
    )


@pytest.mark.parametrize(
    "command_name",
    [
        "bduTestMpxEditKeyframes",
        "bduTestMpxFailAfterAnimationEdit",
        "bduTestMpxFailDuringAnimationEdit",
    ],
)
def test_animation_edits_share_command_history_and_restore_on_failure(
    mpx_test_plugin,
    maya_cmds,
    command_name,
):
    node_name = maya_cmds.createNode("transform", name="animationEditTarget")
    tx = f"{node_name}.translateX"
    ty = f"{node_name}.translateY"
    for frame in (1, 3):
        maya_cmds.setKeyframe(
            tx,
            time=frame,
            value=frame,
            inTangentType="linear",
            outTangentType="linear",
        )
    maya_cmds.setKeyframe(ty, time=1, value=10)
    initial_x = _animation_state(maya_cmds, tx)
    initial_y = _animation_state(maya_cmds, ty)
    initial_curves = sorted(maya_cmds.ls(type="animCurve"))
    maya_cmds.flushUndo()
    command = getattr(maya_cmds, command_name)

    if command_name != "bduTestMpxEditKeyframes":
        with pytest.raises(RuntimeError, match="intentional animation"):
            command(nodeName=node_name)
        assert _animation_state(maya_cmds, tx) == initial_x
        assert _animation_state(maya_cmds, ty) == initial_y
        assert sorted(maya_cmds.ls(type="animCurve")) == initial_curves
        assert maya_cmds.getAttr(f"{node_name}.scaleX") == 1.0
        assert not maya_cmds.objExists(f"{node_name}_dag")
        assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
        return

    command(nodeName=node_name)
    final_x = _animation_state(maya_cmds, tx)
    assert final_x[0] == [1.0, 2.0, 5.0]
    assert final_x[1] == pytest.approx([1.0, 2.0, 5.0])
    assert final_x[2][1] == "linear"
    assert final_x[3][1] == "linear"
    for _ in range(2):
        assert _animation_state(maya_cmds, tx) == final_x
        assert not maya_cmds.listConnections(
            ty, source=True, destination=False
        )
        assert maya_cmds.getAttr(f"{node_name}.scaleX") == 2.0
        assert maya_cmds.objExists(f"{node_name}_dag")
        assert len(maya_cmds.ls(type="animCurve")) == 1
        maya_cmds.undo()
        assert _animation_state(maya_cmds, tx) == initial_x
        assert _animation_state(maya_cmds, ty) == initial_y
        assert sorted(maya_cmds.ls(type="animCurve")) == initial_curves
        assert maya_cmds.getAttr(f"{node_name}.scaleX") == 1.0
        assert not maya_cmds.objExists(f"{node_name}_dag")
        assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
        maya_cmds.redo()


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
