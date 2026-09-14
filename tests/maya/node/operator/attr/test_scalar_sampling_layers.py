from __future__ import annotations

import pytest
from maya.api import OpenMaya as om

import bd_util as bdu
from test_scalar_sampling import _assert_samples, restore_sampling_state

pytestmark = pytest.mark.maya


def _layered(cmds, channel, backend, override=False):
    name = cmds.createNode("transform", name="ctrl")
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    ctrl = nodes.existing.transform(name)
    plug = getattr(ctrl, channel)
    if backend == "native":
        layer = cmds.animLayer("Correction", override=override)
        cmds.setAttr(layer + ".weight", 0.5)
        cmds.animLayer(layer, edit=True, attribute=name + "." + channel[:-1])
        cmds.setKeyframe(plug.plug.name(), animLayer=layer, time=3, value=12)
    else:
        layer = nodes.create.animLayer(name="Correction", override=override)
        layer.weight.set(0.5)
        layer.add_plugs([getattr(ctrl, channel[:-1])])
        plug.keyframe.anim_layer(layer).set_key(12, frame=3)
        mod.do_it_dg()
    return ctrl, plug, mod


@pytest.mark.parametrize("backend", ["native", "package"])
@pytest.mark.parametrize("override", [False, True])
@pytest.mark.parametrize("channel", ["translateY", "rotateZ", "scaleX"])
@pytest.mark.parametrize("frames", [[3], [3, 5, 3, -1]])
def test_first_sample_after_layer_key_creation(
    maya_cmds, backend, override, channel, frames
):
    _, plug, _ = _layered(maya_cmds, channel, backend, override)
    _assert_samples(
        plug.sample_values(frames=frames), [(frame, 12) for frame in frames]
    )


def _state(cmds):
    return (
        cmds.currentTime(query=True),
        cmds.ls(selection=True, long=True),
        cmds.file(query=True, modified=True),
        cmds.undoInfo(query=True, undoName=True),
        cmds.undoInfo(query=True, redoName=True),
        cmds.undoInfo(query=True, undoQueueEmpty=True),
        cmds.undoInfo(query=True, redoQueueEmpty=True),
        set(cmds.ls()),
    )


@pytest.mark.parametrize("backend", ["native", "package"])
def test_sampling_preserves_scene_history_and_pending_layer_edits(
    maya_cmds, backend
):
    ctrl, plug, mod = _layered(maya_cmds, "translateY", backend)
    keyframe = plug.keyframe.anim_layer("Correction")
    maya_cmds.select("ctrl")
    maya_cmds.setAttr("ctrl.visibility", False)
    maya_cmds.undo()
    curve_data = keyframe.get_curve_data()
    keyframe.set_key(99, frame=3)
    pending = mod.dg_mod
    history = (mod.can_undo, mod.can_redo)
    maya_cmds.file(modified=False)
    before = _state(maya_cmds)
    _assert_samples(plug.sample_values(frames=[3, 5]), [(3, 12), (5, 12)])
    assert _state(maya_cmds) == before
    assert keyframe.get_curve_data() == curve_data
    assert mod.dg_mod is pending
    assert (mod.can_undo, mod.can_redo) == history
    assert ctrl.visibility.get() is True
    mod.do_it_dg()
    _assert_samples(plug.sample_values(frames=[3]), [(3, 99)])


@pytest.mark.parametrize("failure", [False, True])
def test_sampling_restores_outer_context_and_history(
    maya_cmds, monkeypatch, failure
):
    _, plug, _ = _layered(maya_cmds, "translateY", "native")
    from bd_util.maya.node.operator.attr.define.std.at.scalar import _base

    original = _base._sample_reader

    def reader(plug, unit):
        read = original(plug, unit)

        def value():
            if om.MDGContext.current().getTime().asUnits(unit) == 5:
                raise RuntimeError("intentional sampling failure")
            return read()

        return value

    if failure:
        monkeypatch.setattr(_base, "_sample_reader", reader)
    maya_cmds.file(modified=False)
    before = _state(maya_cmds)
    outer = om.MDGContext(om.MTime(8, om.MTime.uiUnit()))
    previous = outer.makeCurrent()
    try:
        if failure:
            with pytest.raises(
                RuntimeError, match="intentional sampling failure"
            ):
                plug.sample_values(frames=[3, 5])
        else:
            _assert_samples(
                plug.sample_values(frames=[3, 5]), [(3, 12), (5, 12)]
            )
        assert om.MDGContext.current().getTime() == outer.getTime()
    finally:
        previous.makeCurrent()
    assert om.MDGContext.current().isNormal()
    assert _state(maya_cmds) == before


def test_sampling_follows_unconsumed_output_dependency(maya_cmds):
    _, plug, mod = _layered(maya_cmds, "translateY", "package")
    node = bdu.Nodes(modifier_manager=mod).create.multiplyDivide(
        name="computed"
    )
    plug.connect(node.input1.input1X)
    node.input2.input2X.set(2)
    mod.do_it_dg()
    _assert_samples(
        node.output.outputX.sample_values(frames=[3, 5]), [(3, 24), (5, 24)]
    )


def test_sampling_follows_driven_curve_input_dependencies(maya_cmds):
    _, plug, mod = _layered(maya_cmds, "translateY", "package")
    name = maya_cmds.createNode("animCurveUU", name="remap")
    for value in (0, 20):
        maya_cmds.setKeyframe(
            name,
            float=value,
            value=value * 2,
            inTangentType="linear",
            outTangentType="linear",
        )
    remap = bdu.Nodes(modifier_manager=mod).existing.animCurveUU(name)
    plug.connect(remap.input)
    mod.do_it_dg()
    _assert_samples(
        remap.output.sample_values(frames=[3, 5]), [(3, 24), (5, 24)]
    )


@pytest.mark.parametrize(
    "attribute,value,expected", [("weight", 0.25, 6), ("mute", True, 0)]
)
def test_sampling_observes_layer_state_changes(
    maya_cmds, attribute, value, expected
):
    _, plug, _ = _layered(maya_cmds, "translateY", "native")
    _assert_samples(plug.sample_values(frames=[3]), [(3, 12)])
    maya_cmds.setAttr("Correction." + attribute, value)
    _assert_samples(plug.sample_values(frames=[3]), [(3, expected)])


@pytest.mark.parametrize("kind", ["locked", "referenced"])
def test_sampling_can_read_protected_layer_animation(
    maya_cmds, tmp_path, kind
):
    _, plug, _ = _layered(maya_cmds, "translateY", "native")
    if kind == "locked":
        maya_cmds.animLayer("Correction", edit=True, lock=True)
        maya_cmds.lockNode("ctrl", lock=True)
    else:
        path = str(tmp_path / "sampling_layer.ma")
        maya_cmds.file(rename=path)
        maya_cmds.file(save=True, type="mayaAscii")
        maya_cmds.file(new=True, force=True)
        maya_cmds.file(path, reference=True, namespace="ref")
        plug = bdu.Nodes().existing.transform("ref:ctrl").ty
    maya_cmds.file(modified=False)
    before = _state(maya_cmds)
    _assert_samples(plug.sample_values(frames=[3, 5]), [(3, 12), (5, 12)])
    assert _state(maya_cmds) == before


def test_empty_or_invalid_samples_do_not_invalidate_caches(
    maya_cmds, monkeypatch
):
    _, plug, _ = _layered(maya_cmds, "translateY", "native")

    def unexpected_dirty(*args, **kwargs):
        raise AssertionError("No cache invalidation is needed.")

    monkeypatch.setattr(maya_cmds, "dgdirty", unexpected_dirty)
    assert plug.sample_values(frames=[]) == []
    with pytest.raises(ValueError):
        plug.sample_values(frames=[float("nan")])


def test_sampling_after_key_edit_and_undo_redo(maya_cmds):
    _, plug, _ = _layered(maya_cmds, "translateY", "native")
    maya_cmds.flushUndo()
    maya_cmds.setKeyframe("ctrl.ty", animLayer="Correction", time=3, value=20)
    for _ in range(2):
        _assert_samples(plug.sample_values(frames=[3]), [(3, 20)])
        maya_cmds.undo()
        _assert_samples(plug.sample_values(frames=[3]), [(3, 12)])
        maya_cmds.redo()


def test_sampling_does_not_dirty_unrelated_curves(maya_cmds):
    _, plug, _ = _layered(maya_cmds, "translateY", "native")
    maya_cmds.createNode("transform", name="other")
    maya_cmds.setKeyframe("other.tx", time=3, value=7)
    selection = om.MSelectionList()
    selection.add("other")
    dirty = []
    callback = om.MNodeMessage.addNodeDirtyPlugCallback(
        selection.getDependNode(0),
        lambda node, plug, data: dirty.append(plug.name()),
    )
    try:
        _assert_samples(plug.sample_values(frames=[3]), [(3, 12)])
        assert not dirty
    finally:
        om.MMessage.removeCallback(callback)
