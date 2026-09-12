from __future__ import annotations

from dataclasses import replace

import pytest

import bd_util as bdu
from test_keyframe_anim_layer import (
    CHANNELS,
    DATA_EDITS,
    _curve_name,
    _layered,
    _queue_edit,
)
from test_keyframe_channel import _manager, _states
from test_keyframe_set_equivalence import restore_animation_preferences
from test_keyframe_target import EDITS, QUERIES

pytestmark = pytest.mark.maya


def _prefer(cmds, selected):
    for layer in cmds.ls(type="animLayer"):
        cmds.animLayer(
            layer,
            edit=True,
            selected=layer == selected,
            preferred=layer == selected,
        )


def _without(states, selected):
    return {name: state for name, state in states.items() if name != selected}


@pytest.mark.parametrize("channel", CHANNELS)
@pytest.mark.parametrize("override", [False, True])
def test_default_queries_read_base_curve_without_changing_layer_state(
    maya_cmds, channel, override
):
    keyframe, mod, layers = _layered(maya_cmds, channel, override=override)
    base = maya_cmds.animLayer(query=True, root=True)
    selected = _curve_name(maya_cmds, base, keyframe.plug.name())
    explicit = bdu.Nodes().existing(selected).keyframe
    _prefer(maya_cmds, layers[1])
    maya_cmds.animLayer(layers[0], edit=True, mute=True)
    maya_cmds.animLayer(layers[1], edit=True, solo=True)
    maya_cmds.selectKey(selected, replace=True, time=(5, 5))
    before = _states(maya_cmds)
    current_time = maya_cmds.currentTime(query=True)
    layer_state = {
        layer: tuple(
            maya_cmds.getAttr(layer + "." + attr)
            for attr in ("selected", "preferred", "mute", "solo", "weight")
        )
        for layer in [base, *layers]
    }
    maya_cmds.flushUndo()
    maya_cmds.file(modified=False)
    for method, kwargs in QUERIES:
        assert getattr(keyframe, method)(**kwargs) == getattr(
            explicit, method
        )(**kwargs)
    assert keyframe.get_curve_data(2, 4) == explicit.get_curve_data(2, 4)
    assert _states(maya_cmds) == before
    assert maya_cmds.currentTime(query=True) == current_time
    assert {
        layer: tuple(
            maya_cmds.getAttr(layer + "." + attr)
            for attr in ("selected", "preferred", "mute", "solo", "weight")
        )
        for layer in [base, *layers]
    } == layer_state
    assert not maya_cmds.file(query=True, modified=True)
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
    assert not mod.can_undo


@pytest.mark.parametrize("channel", CHANNELS)
@pytest.mark.parametrize("override", [False, True])
@pytest.mark.parametrize("method", ["set_key", "set_keys"])
def test_default_setting_matches_explicit_native_base_despite_preferred_layer(
    maya_cmds, channel, override, method
):
    keyframe, mod, layers = _layered(maya_cmds, channel, override=override)
    control, _, _ = _layered(
        maya_cmds, channel, override=override, prefix="control"
    )
    base = maya_cmds.animLayer(query=True, root=True)
    selected = _curve_name(maya_cmds, base, keyframe.plug.name())
    samples = [(3, 50)] if method == "set_key" else [(3, 50), (7, 70)]
    for frame, value in samples:
        maya_cmds.setKeyframe(
            control.plug.name(), animLayer=base, time=frame, value=value
        )
    expected_name = _curve_name(maya_cmds, base, control.plug.name())
    expected = bdu.Nodes().existing(expected_name).keyframe.get_keys()
    _prefer(maya_cmds, layers[0])
    before = _states(maya_cmds)
    if method == "set_key":
        keyframe.set_key(50, 3)
    else:
        keyframe.set_keys(samples)
    _prefer(maya_cmds, layers[1])
    assert _states(maya_cmds) == before
    mod.do_it_dg()
    assert keyframe.get_keys() == pytest.approx(expected)
    after = _states(maya_cmds)
    assert _without(after, selected) == _without(before, selected)
    for _ in range(2):
        mod.undo_it()
        assert _states(maya_cmds) == before
        _prefer(maya_cmds, layers[0])
        mod.redo_it()
        assert _states(maya_cmds) == after


@pytest.mark.parametrize(
    "mode", [0, 1, 2], ids=["last_active", "hybrid", "selected"]
)
@pytest.mark.parametrize("method", ["set_key", "set_keys"])
def test_default_setting_ignores_maya_layer_keying_mode(
    maya_cmds, mode, method
):
    keyframe, mod, layers = _layered(maya_cmds)
    base = maya_cmds.animLayer(query=True, root=True)
    selected = _curve_name(maya_cmds, base, keyframe.plug.name())
    _prefer(maya_cmds, layers[1])
    before = _states(maya_cmds)
    if method == "set_key":
        keyframe.set_key(50, 3)
    else:
        keyframe.set_keys([(3, 50)])
    option = "animLayerSelectionKey"
    existed = maya_cmds.optionVar(exists=option)
    previous = maya_cmds.optionVar(query=option) if existed else None
    try:
        maya_cmds.optionVar(intValue=(option, mode))
        mod.do_it_dg()
        assert keyframe.frames() == [1, 3, 5]
        assert _without(_states(maya_cmds), selected) == _without(
            before, selected
        )
        assert maya_cmds.optionVar(query=option) == mode
        mod.undo_it()
        assert _states(maya_cmds) == before
    finally:
        if existed:
            maya_cmds.optionVar(intValue=(option, previous))
        else:
            maya_cmds.optionVar(remove=option)


@pytest.mark.parametrize("channel", CHANNELS)
@pytest.mark.parametrize(
    "method", [method for method, _ in EDITS] + list(DATA_EDITS)
)
def test_default_edits_preserve_additive_curves_and_restore_history(
    maya_cmds, channel, method
):
    keyframe, mod, layers = _layered(maya_cmds, channel)
    base = maya_cmds.animLayer(query=True, root=True)
    selected = _curve_name(maya_cmds, base, keyframe.plug.name())
    _prefer(maya_cmds, layers[1])
    before = _states(maya_cmds)
    _queue_edit(keyframe, method)
    assert _states(maya_cmds) == before
    mod.do_it_dg()
    after = _states(maya_cmds)
    assert _without(after, selected) == _without(before, selected)
    if method == "delete_anim_curve":
        assert selected not in after
        assert keyframe.get_curve_data() is None
    else:
        assert after[selected] != before[selected]
    for _ in range(2):
        mod.undo_it()
        assert _states(maya_cmds) == before
        mod.redo_it()
        assert _states(maya_cmds) == after


def test_default_uses_renamed_root_and_ignores_unrelated_baseanimation_name(
    maya_cmds,
):
    keyframe, mod, layers = _layered(maya_cmds)
    base = maya_cmds.animLayer(query=True, root=True)
    selected = _curve_name(maya_cmds, base, keyframe.plug.name())
    before = _states(maya_cmds)
    keyframe.set_key(12, 3)
    keyframe.delete_key(1)
    renamed = maya_cmds.rename(base, "Foundation")
    unrelated = maya_cmds.createNode("network", name="BaseAnimation")
    _prefer(maya_cmds, layers[1])
    assert keyframe.get_keys() == [(1, 1), (5, 5)]
    mod.do_it_dg()
    assert keyframe.frames() == [3, 5]
    assert _curve_name(maya_cmds, renamed, keyframe.plug.name()) == selected
    assert maya_cmds.nodeType(unrelated) == "network"
    after = _states(maya_cmds)
    assert _without(after, selected) == _without(before, selected)
    mod.undo_it()
    assert _states(maya_cmds) == before
    mod.redo_it()
    assert _states(maya_cmds) == after


def test_layer_added_after_queueing_does_not_receive_default_key(maya_cmds):
    target = maya_cmds.createNode("transform")
    mod = bdu.ModifierManager()
    keyframe = _manager(target + ".ty", mod)
    assert not maya_cmds.animLayer(query=True, root=True)
    keyframe.set_key(12, 3)
    layer = maya_cmds.animLayer("Correction", attribute=target + ".ty")
    maya_cmds.setKeyframe(target + ".ty", animLayer=layer, time=1, value=20)
    _prefer(maya_cmds, layer)
    addition = keyframe.anim_layer(layer)
    before = _states(maya_cmds)
    addition_before = addition.get_curve_data()
    assert keyframe.get_curve_data() is None
    mod.do_it_dg()
    assert keyframe.frames() == [3]
    assert addition.get_curve_data() == addition_before
    after = _states(maya_cmds)
    mod.undo_it()
    assert _states(maya_cmds) == before
    assert keyframe.get_curve_data() is None
    mod.redo_it()
    assert _states(maya_cmds) == after


def test_empty_base_curve_stays_selected_for_restore(maya_cmds):
    keyframe, mod, layers = _layered(maya_cmds)
    base = maya_cmds.animLayer(query=True, root=True)
    selected = _curve_name(maya_cmds, base, keyframe.plug.name())
    setup_mod = bdu.ModifierManager()
    explicit = (
        bdu.Nodes(modifier_manager=setup_mod).existing(selected).keyframe
    )
    original = explicit.get_curve_data()
    explicit.delete_keys()
    setup_mod.do_it_dg()
    _prefer(maya_cmds, layers[1])
    before = _states(maya_cmds)
    assert keyframe.has_anim_curve() and keyframe.get_keys() == []
    assert keyframe.get_curve_data().keys == ()
    keyframe.set_curve_data(original)
    mod.do_it_dg()
    assert keyframe.get_curve_data() == original
    assert _without(_states(maya_cmds), selected) == _without(before, selected)
    mod.undo_it()
    assert _states(maya_cmds) == before


@pytest.mark.parametrize("method", DATA_EDITS)
def test_missing_base_queries_do_not_flush_and_restore_follows_first_key(
    maya_cmds, method
):
    target = maya_cmds.createNode("transform")
    layer = maya_cmds.animLayer("Correction", attribute=target + ".ty")
    for frame, value in ((1, 12), (5, 16)):
        maya_cmds.setKeyframe(
            target + ".ty", animLayer=layer, time=frame, value=value
        )
    _prefer(maya_cmds, layer)
    mod = bdu.ModifierManager()
    keyframe = _manager(target + ".ty", mod)
    data = keyframe.anim_layer(layer).get_curve_data()
    before = _states(maya_cmds)
    getattr(keyframe, method)(
        data if method == "set_curve_data" else data.keys
    )
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert _states(maya_cmds) == before
    assert not mod.can_undo
    keyframe.set_key(0, 1)
    getattr(keyframe, method)(
        data if method == "set_curve_data" else data.keys
    )
    assert keyframe.get_keys() == keyframe.get_key_data() == []
    assert keyframe.frames() == keyframe.values() == []
    assert keyframe.get_curve_data() is None
    assert keyframe.get_weighted() is None
    assert not keyframe.has_anim_curve() and not keyframe.has_key(1)
    assert keyframe.key_count() == 0
    assert _states(maya_cmds) == before
    mod.do_it_dg()
    assert keyframe.get_keys() == [(key.frame, key.value) for key in data.keys]
    assert keyframe.anim_layer(layer).get_curve_data() == data
    after = _states(maya_cmds)
    mod.undo_it()
    assert _states(maya_cmds) == before
    mod.redo_it()
    assert _states(maya_cmds) == after


@pytest.mark.parametrize("method", ["set_key", "delete_key", "set_curve_data"])
def test_default_rechecks_base_layer_lock_without_falling_back(
    maya_cmds, method
):
    keyframe, mod, layers = _layered(maya_cmds)
    base = maya_cmds.animLayer(query=True, root=True)
    _prefer(maya_cmds, layers[1])
    data = keyframe.get_curve_data()
    if method == "set_key":
        keyframe.set_key(12, 3)
    elif method == "delete_key":
        keyframe.delete_key(1)
    else:
        keyframe.set_curve_data(replace(data, weighted=True))
    maya_cmds.animLayer(base, edit=True, lock=True)
    before = _states(maya_cmds)
    assert keyframe.get_curve_data() == data
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert _states(maya_cmds) == before
    assert not mod.can_undo


def test_default_creation_and_edits_rollback_on_late_failure(maya_cmds):
    keyframe, mod, layers = _layered(maya_cmds)
    target = maya_cmds.createNode("transform", name="fresh")
    maya_cmds.animLayer(layers[0], edit=True, attribute=target + ".ty")
    fresh = _manager(target + ".ty", mod)
    _prefer(maya_cmds, layers[1])
    before = _states(maya_cmds)
    keyframe.set_key(20, 3)
    keyframe.set_weighted(True)
    fresh.set_key(12, 1)
    fresh.set_tangent(1, out_tangent_type="flat")
    keyframe.anim_layer(layers[0]).delete_key(1)
    _manager(target + ".tz", mod).insert_key(1)
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert _states(maya_cmds) == before
    assert fresh.get_curve_data() is None
    assert not mod.can_undo and not mod.can_redo


@pytest.mark.parametrize("channel", CHANNELS)
def test_sample_values_keeps_evaluating_composed_plug(maya_cmds, channel):
    keyframe, mod, layers = _layered(maya_cmds, channel)
    node = bdu.Nodes(modifier_manager=mod).existing.transform(
        keyframe.plug.name().split(".")[0]
    )
    attribute = getattr(getattr(node, channel[:-1]), channel)
    frames = [1, 3, 5]
    expected = [
        (frame, maya_cmds.getAttr(keyframe.plug.name(), time=frame))
        for frame in frames
    ]
    _prefer(maya_cmds, layers[1])
    assert expected[0][1] != pytest.approx(keyframe.values()[0])
    before = keyframe.get_curve_data()
    current_time = maya_cmds.currentTime(query=True)
    keyframe.set_key(50, 3)
    assert attribute.sample_values(frames=frames) == pytest.approx(expected)
    assert keyframe.get_curve_data() == before
    assert maya_cmds.currentTime(query=True) == current_time
    assert not mod.can_undo


@pytest.mark.parametrize("unrelated_layer", [False, True])
def test_unlayered_plug_keeps_normal_curve_creation_and_restore(
    maya_cmds, unrelated_layer
):
    target = maya_cmds.createNode("transform")
    if unrelated_layer:
        _prefer(maya_cmds, maya_cmds.animLayer("Unrelated"))
    mod = bdu.ModifierManager()
    keyframe = _manager(target + ".ty", mod)
    keyframe.set_keys([(1, 12), (5, 16)])
    assert keyframe.get_curve_data() is None
    mod.do_it_dg()
    assert keyframe.get_keys() == [(1, 12), (5, 16)]
    data = keyframe.get_curve_data()
    mod.undo_it()
    assert not keyframe.has_anim_curve()
    keyframe.set_curve_data(data)
    mod.do_it_dg()
    assert keyframe.get_curve_data() == data
    if not unrelated_layer:
        assert not maya_cmds.ls(type="animLayer")


@pytest.mark.parametrize("attribute_type", ["bool", "enum", "time"])
@pytest.mark.parametrize("method", ["set_key", "set_keys"])
def test_unrelated_layer_preserves_native_setting_on_other_scalar_types(
    maya_cmds, attribute_type, method
):
    target = maya_cmds.createNode("transform")
    flags = {"enumName": "A:B:C:D"} if attribute_type == "enum" else {}
    maya_cmds.addAttr(
        target,
        longName="customValue",
        attributeType=attribute_type,
        keyable=True,
        **flags,
    )
    plug = target + ".customValue"
    layer = maya_cmds.animLayer("Unrelated")
    _prefer(maya_cmds, layer)
    mod = bdu.ModifierManager()
    keyframe = _manager(plug, mod)
    samples = (
        [(3, 1), (7, 0)] if attribute_type == "bool" else [(3, 2), (7, 3)]
    )
    before = _states(maya_cmds)
    if method == "set_key":
        for frame, value in samples:
            keyframe.set_key(value, frame)
    else:
        keyframe.set_keys(samples)
    mod.do_it_dg()
    assert maya_cmds.keyframe(plug, query=True, timeChange=True) == [3, 7]
    assert [maya_cmds.getAttr(plug, time=frame) for frame, _ in samples] == [
        value for _, value in samples
    ]
    assert not maya_cmds.animLayer(layer, query=True, attribute=True)
    assert not maya_cmds.ls(type="animBlendNodeBase")
    after = _states(maya_cmds)
    mod.undo_it()
    assert _states(maya_cmds) == before
    mod.redo_it()
    assert _states(maya_cmds) == after
