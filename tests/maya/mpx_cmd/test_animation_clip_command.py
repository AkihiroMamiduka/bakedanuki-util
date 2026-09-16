from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


@pytest.fixture
def clip_plugin(new_scene, maya_cmds):
    name = "bdu_mpx_animation_clip_test_plugin"
    maya_cmds.loadPlugin(
        str(Path(__file__).parent / "fixtures" / (name + ".py")), quiet=True
    )
    yield
    maya_cmds.flushUndo()
    maya_cmds.unloadPlugin(name)


@pytest.mark.parametrize("mode", ["flatten", "preserve"])
@pytest.mark.parametrize("fail", [False, True])
@pytest.mark.parametrize("offset", [0, 90])
def test_clip_command_history(clip_plugin, maya_cmds, mode, fail, offset):
    cmds = maya_cmds
    source = cmds.createNode("transform")
    cmds.setKeyframe(source + ".tx", time=1, value=2)
    cmds.setKeyframe(source + ".tx", time=5, value=10)
    layer = cmds.animLayer("Details")
    cmds.animLayer(layer, edit=True, attribute=source + ".tx")
    cmds.setKeyframe(
        source + ".tx", time=1, value=3, animLayer=layer, noResolve=True
    )
    clip = bdu.AnimationClip.capture(
        [source], attributes=["tx"], layer_mode=mode
    )
    expected = (
        bdu.Nodes()
        .existing.transform(source)
        .tx.sample_values(frames=[1, 3, 5])
    )
    expected = [(frame + offset, value) for frame, value in expected]
    cmds.file(new=True, force=True)
    target = cmds.createNode("transform")
    cmds.setKeyframe(target + ".tx", time=2, value=30)
    before = (
        bdu.Nodes().existing.transform(target).tx.keyframe.get_curve_data()
    )
    before_nodes = set(cmds.ls())
    cmds.flushUndo()
    command = getattr(
        cmds, "bduTestMpxFailRestoreClip" if fail else "bduTestMpxRestoreClip"
    )
    if fail:
        with pytest.raises(
            RuntimeError, match="intentional animation clip failure"
        ):
            command(
                clipData=clip.to_json(), nodeName=target, offsetFrames=offset
            )
        assert set(cmds.ls()) == before_nodes
        assert (
            bdu.Nodes().existing.transform(target).tx.keyframe.get_curve_data()
            == before
        )
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
        return
    command(clipData=clip.to_json(), nodeName=target, offsetFrames=offset)
    after_nodes = set(cmds.ls())
    for _ in range(3):
        assert bdu.Nodes().existing.transform(target).tx.sample_values(
            frames=[1 + offset, 3 + offset, 5 + offset]
        ) == pytest.approx(expected)
        cmds.undo()
        assert set(cmds.ls()) == before_nodes
        assert (
            bdu.Nodes().existing.transform(target).tx.keyframe.get_curve_data()
            == before
        )
        cmds.redo()
        assert set(cmds.ls()) == after_nodes
