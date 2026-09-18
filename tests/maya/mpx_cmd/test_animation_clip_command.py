from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


@pytest.fixture(scope="module")
def clip_plugin():
    # Share registration across cases, as for move/scale commands on Maya 2027.
    maya_cmds = pytest.importorskip("maya.cmds")
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
@pytest.mark.parametrize("scale", [1, 2])
@pytest.mark.parametrize("cropped", [False, True])
def test_clip_command_history(
    clip_plugin, maya_cmds, mode, fail, offset, scale, cropped
):
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
    start, end = (2, 4) if cropped else (1, 5)
    options = dict(startFrame=start, endFrame=end) if cropped else {}
    expected = (
        bdu.Nodes()
        .existing.transform(source)
        .tx.sample_values(frames=[start, 3, end])
    )
    expected = [
        (start + (frame - start) * scale + offset, value)
        for frame, value in expected
    ]
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
                clipData=clip.to_json(),
                nodeName=target,
                offsetFrames=offset,
                timeScale=scale,
                **options,
            )
        assert set(cmds.ls()) == before_nodes
        assert (
            bdu.Nodes().existing.transform(target).tx.keyframe.get_curve_data()
            == before
        )
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
        return
    command(
        clipData=clip.to_json(),
        nodeName=target,
        offsetFrames=offset,
        timeScale=scale,
        **options,
    )
    after_nodes = set(cmds.ls())
    for _ in range(3):
        actual = (
            bdu.Nodes()
            .existing.transform(target)
            .tx.sample_values(frames=[frame for frame, _ in expected])
        )
        assert len(actual) == len(expected)
        for actual_pair, expected_pair in zip(actual, expected):
            assert actual_pair == pytest.approx(expected_pair)
        cmds.undo()
        assert set(cmds.ls()) == before_nodes
        assert (
            bdu.Nodes().existing.transform(target).tx.keyframe.get_curve_data()
            == before
        )
        cmds.redo()
        assert set(cmds.ls()) == after_nodes
