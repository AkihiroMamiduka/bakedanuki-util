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
def reduce_test_plugin(new_scene, maya_cmds):
    name = "bdu_mpx_keyframe_reduce_test_plugin"
    path = Path(__file__).resolve().parent / "fixtures" / f"{name}.py"
    maya_cmds.loadPlugin(str(path), quiet=True)
    yield
    maya_cmds.flushUndo()
    maya_cmds.unloadPlugin(name)


@pytest.fixture(scope="module")
def move_test_plugin():
    # Repeated registration/unloading per parameter case crashes Maya 2027 on exit.
    maya_cmds = pytest.importorskip("maya.cmds")
    name = "bdu_mpx_keyframe_move_test_plugin"
    path = Path(__file__).resolve().parent / "fixtures" / f"{name}.py"
    maya_cmds.loadPlugin(str(path), quiet=True)
    yield
    maya_cmds.flushUndo()
    maya_cmds.unloadPlugin(name)


@pytest.fixture(scope="module")
def scale_test_plugin():
    # Share registration across cases, as for the move command on Maya 2027.
    maya_cmds = pytest.importorskip("maya.cmds")
    name = "bdu_mpx_keyframe_scale_test_plugin"
    path = Path(__file__).resolve().parent / "fixtures" / f"{name}.py"
    maya_cmds.loadPlugin(str(path), quiet=True)
    yield
    maya_cmds.flushUndo()
    maya_cmds.unloadPlugin(name)


@pytest.fixture
def value_test_plugin(new_scene, maya_cmds):
    name = "bdu_mpx_keyframe_value_test_plugin"
    path = Path(__file__).resolve().parent / "fixtures" / f"{name}.py"
    maya_cmds.loadPlugin(str(path), quiet=True)
    yield
    maya_cmds.flushUndo()
    maya_cmds.unloadPlugin(name)


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


@pytest.mark.parametrize("fail", [False, True])
@pytest.mark.parametrize("interpolate", [False, True])
def test_move_keys_uses_maya_undo_redo_and_command_failure_rollback(
    move_test_plugin, new_scene, maya_cmds, fail, interpolate
):
    from maya.api import OpenMaya as om
    from bd_util.maya.node.operator.attr import KeyframeManager

    node = maya_cmds.createNode("transform")
    managers = []
    for channel in ("tx", "ty"):
        plug = node + "." + channel
        for frame, value in ((0, 0), (10, 4), (20, 2), (30, 7)):
            maya_cmds.setKeyframe(plug, time=frame, value=value)
        managers.append(
            KeyframeManager(om.MSelectionList().add(plug).getPlug(0))
        )
    before = [k.get_curve_data() for k in managers]
    maya_cmds.flushUndo()
    command = getattr(
        maya_cmds,
        (
            "bduTestMpxFailAfterMoveKeyframes"
            if fail
            else "bduTestMpxMoveKeyframes"
        ),
    )
    if fail:
        with pytest.raises(
            RuntimeError, match="intentional keyframe move failure"
        ):
            command(nodeName=node, interpolate=interpolate)
        assert [k.get_curve_data() for k in managers] == before
        assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
        return
    command(nodeName=node, interpolate=interpolate)
    if interpolate:
        assert managers[0].get_keys() == [(0, 0), (14, 4), (24, 2), (30, 7)]
        assert managers[1].frames() == pytest.approx(
            [0, 5, 10 + 10 / 7, 14, 20, 20 + 10 / 7, 25, 30]
        )
    else:
        assert managers[0].frames() == [0, 20, 30]
        assert managers[0].get_keys() == [(0, 0), (20, 4), (30, 7)]
        assert managers[1].frames() == [0, 10, 20, 30, 40, 46]
    after = [k.get_curve_data() for k in managers]
    for _ in range(3):
        maya_cmds.undo()
        assert [k.get_curve_data() for k in managers] == before
        maya_cmds.redo()
        assert [k.get_curve_data() for k in managers] == after


@pytest.mark.parametrize("fail", [False, True])
def test_reduce_keys_uses_maya_undo_redo_and_command_failure_rollback(
    reduce_test_plugin, maya_cmds, fail
):
    import bd_util as bdu

    node = maya_cmds.createNode("transform")
    for i in range(11):
        maya_cmds.setKeyframe(
            node + ".tx",
            time=i,
            value=i,
            inTangentType="linear",
            outTangentType="linear",
        )
    keyframe = bdu.Nodes().existing.transform(node).tx.keyframe
    before = keyframe.get_curve_data()
    maya_cmds.flushUndo()
    command = getattr(
        maya_cmds,
        (
            "bduTestMpxFailAfterReduceKeyframes"
            if fail
            else "bduTestMpxReduceKeyframes"
        ),
    )
    if fail:
        with pytest.raises(
            RuntimeError, match="intentional keyframe reduction failure"
        ):
            command(nodeName=node)
        assert keyframe.get_curve_data() == before
        assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
        return
    command(nodeName=node)
    assert keyframe.frames() == [0, 10]
    after = keyframe.get_curve_data()
    for _ in range(3):
        maya_cmds.undo()
        assert keyframe.get_curve_data() == before
        maya_cmds.redo()
        assert keyframe.get_curve_data() == after


@pytest.mark.parametrize("fail", [False, True])
@pytest.mark.parametrize("interpolate", [False, True])
def test_scale_keys_uses_maya_history_and_command_failure_rollback(
    scale_test_plugin, new_scene, maya_cmds, fail, interpolate
):
    import bd_util as bdu

    name = maya_cmds.createNode("transform")
    for attr in ("tx", "ty"):
        for frame, value in ((0, 0), (10, 4), (20, 2), (30, 7)):
            maya_cmds.setKeyframe(name + "." + attr, time=frame, value=value)
        maya_cmds.keyTangent(
            name + "." + attr, edit=True, weightedTangents=True
        )
    node = bdu.Nodes().existing.transform(name)
    managers = [node.tx.keyframe, node.ty.keyframe]
    before = [k.get_curve_data() for k in managers]
    maya_cmds.flushUndo()
    command = getattr(
        maya_cmds,
        (
            "bduTestMpxFailAfterScaleKeyframes"
            if fail
            else "bduTestMpxScaleKeyframes"
        ),
    )
    if fail:
        with pytest.raises(
            RuntimeError, match="intentional keyframe scaling failure"
        ):
            command(nodeName=name, interpolate=interpolate)
        assert [k.get_curve_data() for k in managers] == before
        assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
        return
    command(nodeName=name, interpolate=interpolate)
    if interpolate:
        assert managers[0].get_keys() == [(0, 0), (10, 4), (25, 2), (30, 7)]
        assert managers[1].frames() == pytest.approx(
            [0, 5, 10 + 10 / 7, 13, 16, 20 - 15 / 7, 25, 30]
        )
    else:
        assert managers[0].get_keys() == [(0, 0), (20, 4), (40, 2)]
        assert managers[1].frames() == [0, 10, 20, 30, 32]
    after = [k.get_curve_data() for k in managers]
    for _ in range(3):
        maya_cmds.undo()
        assert [k.get_curve_data() for k in managers] == before
        maya_cmds.redo()
        assert [k.get_curve_data() for k in managers] == after


@pytest.mark.parametrize("fail", [False, True])
def test_value_edits_use_maya_history_and_command_failure_rollback(
    value_test_plugin, maya_cmds, fail
):
    import bd_util as bdu

    name = maya_cmds.createNode("transform")
    for attr in ("tx", "ty"):
        for frame, value in ((0, 0), (10, 4), (20, 2), (30, 7)):
            maya_cmds.setKeyframe(name + "." + attr, time=frame, value=value)
        maya_cmds.keyTangent(
            name + "." + attr, edit=True, weightedTangents=True
        )
    node = bdu.Nodes().existing.transform(name)
    managers = [node.tx.keyframe, node.ty.keyframe]
    before = [k.get_curve_data() for k in managers]
    maya_cmds.flushUndo()
    command = getattr(
        maya_cmds,
        (
            "bduTestMpxFailAfterEditKeyframeValues"
            if fail
            else "bduTestMpxEditKeyframeValues"
        ),
    )
    if fail:
        with pytest.raises(
            RuntimeError, match="intentional keyframe value failure"
        ):
            command(nodeName=name)
        assert [k.get_curve_data() for k in managers] == before
        assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
        return
    command(nodeName=name)
    assert managers[0].get_keys() == [(0, 0), (10, 5), (20, -3), (30, 7)]
    assert managers[1].frames() == [0, 5, 10, 12, 18, 20, 25, 30]
    after = [k.get_curve_data() for k in managers]
    for _ in range(3):
        maya_cmds.undo()
        assert [k.get_curve_data() for k in managers] == before
        maya_cmds.redo()
        assert [k.get_curve_data() for k in managers] == after


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
    "connection", ["new", "direct", "pair_blend", "layer"]
)
@pytest.mark.parametrize("fail", [False, True])
def test_curve_data_and_weighted_share_maya_command_history(
    mpx_test_plugin, maya_cmds, connection, fail
):
    from bd_util.maya.node.operator.attr import KeyframeManager
    from maya.api import OpenMaya as om

    name = maya_cmds.createNode("transform", name="curveDataTarget")
    for frame in (1, 3):
        maya_cmds.setKeyframe(name + ".tx", time=frame, value=frame)
    maya_cmds.keyTangent(name + ".tx", edit=True, weightedTangents=True)
    if connection in ("direct", "pair_blend"):
        maya_cmds.setKeyframe(name + ".ty", time=7, value=5)
    if connection == "pair_blend":
        source_plug = maya_cmds.listConnections(
            name + ".ty", source=True, destination=False, plugs=True
        )[0]
        blend = maya_cmds.createNode("pairBlend")
        maya_cmds.disconnectAttr(source_plug, name + ".ty")
        maya_cmds.connectAttr(source_plug, blend + ".inTranslateY1")
        maya_cmds.connectAttr(blend + ".outTranslateY", name + ".ty")
    if connection == "layer":
        layer = maya_cmds.animLayer("DataLayer")
        maya_cmds.animLayer(layer, edit=True, attribute=name + ".translate")
        maya_cmds.animLayer(layer, edit=True, selected=True, preferred=True)
    selection = om.MSelectionList()
    for axis in ("tx", "ty", "tz"):
        selection.add(name + "." + axis)
    src, dst, other = [KeyframeManager(selection.getPlug(i)) for i in range(3)]
    before = dst.get_curve_data()
    source = src.get_curve_data()
    maya_cmds.flushUndo()
    command_name = (
        "bduTestMpxFailAfterRestoreKeyData"
        if fail
        else "bduTestMpxRestoreKeyData"
    )
    command = getattr(maya_cmds, command_name)
    if fail:
        with pytest.raises(
            RuntimeError, match="intentional curve data failure"
        ):
            command(nodeName=name)
        assert dst.get_curve_data() == before
        assert other.get_curve_data() is None
        assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
        return
    command(nodeName=name)
    for _ in range(2):
        assert dst.get_keys() == [
            (1.0, 1.0),
            (3.0, 3.0),
            (11.0, 2.0),
            (13.0, 6.0),
        ]
        assert dst.get_weighted() is False
        assert other.get_keys() == [(1.0, 1.0), (3.0, 3.0)]
        assert other.get_weighted() is True
        assert src.get_curve_data() == source
        maya_cmds.undo()
        assert dst.get_curve_data() == before
        assert other.get_curve_data() is None
        assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
        maya_cmds.redo()


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


@pytest.mark.parametrize("fail", [False, True])
def test_explicit_curve_data_edits_participate_in_command_history(
    mpx_test_plugin, maya_cmds, fail
):
    import bd_util as bdu

    name = maya_cmds.createNode("animCurveTL")
    for frame in (1, 5):
        maya_cmds.setKeyframe(name, time=frame, value=frame)
    keyframe = bdu.Nodes().existing.animCurveTL(name).keyframe
    before = keyframe.get_curve_data()
    maya_cmds.flushUndo()
    if fail:
        with pytest.raises(
            RuntimeError, match="intentional explicit curve failure"
        ):
            maya_cmds.bduTestMpxFailAfterExplicitCurve(nodeName=name)
        assert keyframe.get_curve_data() == before
        assert maya_cmds.undoInfo(q=True, undoQueueEmpty=True)
        return
    maya_cmds.bduTestMpxEditExplicitCurve(nodeName=name)
    after = keyframe.get_curve_data()
    for _ in range(2):
        assert keyframe.get_keys() == [(3, 30), (5, 15)]
        assert keyframe.get_weighted() is True
        maya_cmds.undo()
        assert keyframe.get_curve_data() == before
        assert maya_cmds.undoInfo(q=True, undoQueueEmpty=True)
        maya_cmds.redo()
        assert keyframe.get_curve_data() == after


@pytest.mark.parametrize("fail", [False, True])
def test_layer_key_creation_restore_and_deletion_share_command_history(
    mpx_test_plugin, maya_cmds, fail
):
    import bd_util as bdu

    name = maya_cmds.createNode("transform", name="layerCommandTarget")
    for axis in ("tx", "ty", "tz"):
        for frame in (1, 5):
            maya_cmds.setKeyframe(name + "." + axis, time=frame, value=frame)
    layer = maya_cmds.animLayer("MpxLayer")
    for axis in ("tx", "ty", "tz"):
        maya_cmds.animLayer(layer, edit=True, attribute=name + "." + axis)
        if axis != "ty":
            for frame in (1, 5):
                maya_cmds.setKeyframe(
                    name + "." + axis,
                    animLayer=layer,
                    time=frame,
                    value=frame * 2,
                )
    node = bdu.Nodes().existing.transform(name)
    target = node.ty.keyframe.anim_layer(layer)
    other = node.tz.keyframe.anim_layer(layer)

    def states():
        return {
            curve: bdu.Nodes().existing(curve).keyframe.get_curve_data()
            for curve in maya_cmds.ls(type="animCurve")
        }

    before = states()
    blends = maya_cmds.animLayer(layer, query=True, blendNodes=True)
    connections = {
        blend: maya_cmds.listConnections(blend, connections=True, plugs=True)
        for blend in blends
    }
    maya_cmds.flushUndo()
    if fail:
        with pytest.raises(
            RuntimeError, match="intentional animation layer failure"
        ):
            maya_cmds.bduTestMpxFailAfterLayerKeyframes(nodeName=name)
        assert states() == before
        assert target.get_curve_data() is None
        assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
        return
    maya_cmds.bduTestMpxEditLayerKeyframes(nodeName=name)
    after = states()
    for _ in range(2):
        assert target.frames() == [3, 5]
        assert target.get_weighted() is True
        assert not other.has_anim_curve()
        assert all(maya_cmds.objExists(blend) for blend in blends)
        assert states() == after
        maya_cmds.undo()
        assert states() == before
        assert {
            blend: maya_cmds.listConnections(
                blend, connections=True, plugs=True
            )
            for blend in blends
        } == connections
        assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
        maya_cmds.redo()


@pytest.mark.parametrize("existing_root", [False, True])
@pytest.mark.parametrize("fail", [False, True])
def test_layer_creation_and_membership_share_command_history(
    mpx_test_plugin, maya_cmds, existing_root, fail
):
    import bd_util as bdu
    from maya.api import OpenMaya as om
    from maya.api import OpenMayaAnim as oma

    name = maya_cmds.createNode("transform", name="target")
    if existing_root:
        maya_cmds.animLayer("Existing")
    before = set(maya_cmds.ls())
    maya_cmds.flushUndo()
    if fail:
        with pytest.raises(
            RuntimeError, match="intentional layer creation failure"
        ):
            maya_cmds.bduTestMpxFailAfterCreateAnimLayer(nodeName=name)
        assert set(maya_cmds.ls()) == before
        assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
        return
    maya_cmds.bduTestMpxCreateAnimLayer(nodeName=name)
    node = bdu.Nodes().existing.transform(name)
    keyframe = node.tx.keyframe.anim_layer("CreatedLayer")
    after = set(maya_cmds.ls())
    data = keyframe.get_curve_data()
    assert data is not None
    for _ in range(2):
        oma.MAnimControl.setCurrentTime(om.MTime(3, om.MTime.uiUnit()))
        assert maya_cmds.getAttr(name + ".tx") == pytest.approx(12)
        assert keyframe.get_curve_data() == data
        assert set(maya_cmds.ls()) == after
        maya_cmds.undo()
        assert set(maya_cmds.ls()) == before
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
