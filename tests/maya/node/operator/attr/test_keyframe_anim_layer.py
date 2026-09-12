from __future__ import annotations

from dataclasses import replace

import pytest

import bd_util as bdu
from bd_util.maya.node.operator.attr import KeyframeManager
from test_keyframe_channel import _manager, _states
from test_keyframe_set_equivalence import restore_animation_preferences
from test_keyframe_target import EDITS, QUERIES

pytestmark = pytest.mark.maya

CHANNELS = ("translateY", "rotateZ", "scaleX")
DATA_EDITS = ("set_key_data", "set_curve_data")


def _curve_name(cmds, layer, plug):
    names = cmds.animLayer(layer, query=True, findCurveForPlug=plug)
    return names[0] if names else None


def _layered(cmds, channel="translateY", *, override=False, prefix="target"):
    target = cmds.createNode("transform", name=prefix)
    for i, attribute in enumerate(CHANNELS):
        for frame in (1, 5):
            cmds.setKeyframe(
                target + "." + attribute, time=frame, value=frame + i
            )
    layers = []
    for name, offset in (("Correction", 20), ("Secondary", 40)):
        layer = cmds.animLayer(prefix + name, override=override)
        for i, attribute in enumerate(CHANNELS):
            plug = target + "." + attribute
            cmds.animLayer(layer, edit=True, attribute=plug)
            for frame in (1, 5):
                cmds.setKeyframe(
                    plug, animLayer=layer, time=frame, value=offset + frame + i
                )
        cmds.setKeyframe(layer + ".weight", time=1, value=0.75)
        layers.append(layer)
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.transform(target)
    family = channel[:-1]
    manager = getattr(getattr(node, family), channel).keyframe
    return manager, mod, layers


def _queue_edit(keyframe, method):
    if method in DATA_EDITS:
        data = keyframe.get_curve_data()
        data = replace(
            data,
            keys=tuple(replace(key, value=key.value + 7) for key in data.keys),
            weighted=True,
        )
        getattr(keyframe, method)(
            data if method == "set_curve_data" else data.keys
        )
    else:
        getattr(keyframe, method)(**dict(EDITS)[method])


def test_layer_entry_preserves_original_manager_and_shares_modifier(maya_cmds):
    original, mod, layers = _layered(maya_cmds)
    first = original.anim_layer(layers[0])
    second = first.anim_layer(layers[1])
    assert isinstance(first, KeyframeManager)
    assert first is not original and second is not first
    assert first.plug == original.plug == second.plug
    assert original.get_keys() == [(1.0, 1.0), (5.0, 5.0)]
    base_before = original.get_curve_data()
    first_before = first.get_curve_data()
    second_before = second.get_curve_data()
    first.delete_key(1)
    second.set_weighted(True)
    assert first.get_curve_data() == first_before
    assert second.get_curve_data() == second_before
    mod.do_it_dg()
    assert first.frames() == [5]
    assert second.get_weighted() is True
    assert original.get_curve_data() == base_before
    mod.undo_it()
    assert first.get_curve_data() == first_before
    assert second.get_curve_data() == second_before


@pytest.mark.parametrize("name", [None, 1, True, [], object()])
def test_layer_name_requires_string(maya_cmds, name):
    target = maya_cmds.createNode("transform")
    manager = _manager(target + ".tx", bdu.ModifierManager())
    with pytest.raises(TypeError):
        manager.anim_layer(name)


@pytest.mark.parametrize(
    "name", ["", "missingLayer", "target", "Correction.weight", "Correct*"]
)
def test_layer_entry_requires_existing_animation_layer(maya_cmds, name):
    target = maya_cmds.createNode("transform", name="target")
    maya_cmds.animLayer("Correction")
    manager = _manager(target + ".tx", bdu.ModifierManager())
    nodes = set(maya_cmds.ls())
    with pytest.raises(ValueError):
        manager.anim_layer(name)
    assert set(maya_cmds.ls()) == nodes


@pytest.mark.parametrize("channel", CHANNELS)
@pytest.mark.parametrize("override", [False, True])
def test_layer_queries_return_raw_curve_without_changing_scene(
    maya_cmds, channel, override
):
    original, mod, layers = _layered(maya_cmds, channel, override=override)
    keyframe = original.anim_layer(layers[0])
    name = _curve_name(maya_cmds, layers[0], original.plug.name())
    explicit = bdu.Nodes().existing(name).keyframe
    maya_cmds.selectKey(name, replace=True, time=(5, 5))
    maya_cmds.animLayer(layers[0], edit=True, mute=True)
    maya_cmds.animLayer(layers[1], edit=True, solo=True)
    before = _states(maya_cmds)
    current_time = maya_cmds.currentTime(query=True)
    selected = maya_cmds.ls(selection=True)
    layers_before = {
        layer: tuple(
            maya_cmds.getAttr(layer + "." + attribute)
            for attribute in (
                "mute",
                "solo",
                "weight",
                "selected",
                "preferred",
            )
        )
        for layer in layers
    }
    maya_cmds.flushUndo()
    maya_cmds.file(modified=False)
    for method, kwargs in QUERIES:
        assert getattr(keyframe, method)(**kwargs) == getattr(
            explicit, method
        )(**kwargs)
    assert keyframe.get_curve_data(2, 4) == explicit.get_curve_data(2, 4)
    assert _states(maya_cmds) == before
    assert not maya_cmds.file(query=True, modified=True)
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
    assert maya_cmds.currentTime(query=True) == current_time
    assert maya_cmds.ls(selection=True) == selected
    assert not mod.can_undo
    assert {
        layer: tuple(
            maya_cmds.getAttr(layer + "." + attribute)
            for attribute in (
                "mute",
                "solo",
                "weight",
                "selected",
                "preferred",
            )
        )
        for layer in layers
    } == layers_before


@pytest.mark.parametrize("channel", CHANNELS)
@pytest.mark.parametrize("override", [False, True])
@pytest.mark.parametrize(
    "method", [method for method, _ in EDITS] + list(DATA_EDITS)
)
def test_layer_edits_preserve_other_curves_and_repeat_undo_redo(
    maya_cmds, channel, override, method
):
    original, mod, layers = _layered(maya_cmds, channel, override=override)
    keyframe = original.anim_layer(layers[0])
    selected = _curve_name(maya_cmds, layers[0], original.plug.name())
    before = _states(maya_cmds)
    blend_nodes = set(maya_cmds.ls(type="animBlendNodeBase"))
    _queue_edit(keyframe, method)
    assert _states(maya_cmds) == before
    mod.do_it_dg()
    after = _states(maya_cmds)
    if method == "delete_anim_curve":
        assert selected not in after
        assert not keyframe.has_anim_curve()
    else:
        assert after[selected] != before[selected]
        if method == "delete_keys":
            assert keyframe.has_anim_curve()
            assert keyframe.get_curve_data().keys == ()
    assert set(maya_cmds.ls(type="animBlendNodeBase")) == blend_nodes
    assert {
        name: state for name, state in after.items() if name != selected
    } == {name: state for name, state in before.items() if name != selected}
    for _ in range(2):
        mod.undo_it()
        assert _states(maya_cmds) == before
        assert (
            _curve_name(maya_cmds, layers[0], original.plug.name()) == selected
        )
        mod.redo_it()
        assert _states(maya_cmds) == after


@pytest.mark.parametrize("channel", CHANNELS)
@pytest.mark.parametrize("override", [False, True])
@pytest.mark.parametrize("method", ["set_key", "set_keys"])
def test_layer_key_setting_matches_native_value_resolution(
    maya_cmds, channel, override, method
):
    original, mod, layers = _layered(maya_cmds, channel, override=override)
    control, _, control_layers = _layered(
        maya_cmds, channel, override=override, prefix="control"
    )
    keyframe = original.anim_layer(layers[0])
    selected = _curve_name(maya_cmds, layers[0], original.plug.name())
    samples = [(3, 50)] if method == "set_key" else [(3, 50), (7, 70)]
    for frame, value in samples:
        maya_cmds.setKeyframe(
            control.plug.name(),
            animLayer=control_layers[0],
            time=frame,
            value=value,
        )
    expected = control.anim_layer(control_layers[0]).get_keys()
    before = _states(maya_cmds)
    if method == "set_key":
        keyframe.set_key(50, 3)
    else:
        keyframe.set_keys(samples)
    assert _states(maya_cmds) == before
    mod.do_it_dg()
    assert keyframe.get_keys() == pytest.approx(expected)
    after = _states(maya_cmds)
    assert {
        name: state for name, state in after.items() if name != selected
    } == {name: state for name, state in before.items() if name != selected}
    for _ in range(2):
        mod.undo_it()
        assert _states(maya_cmds) == before
        mod.redo_it()
        assert _states(maya_cmds) == after


def test_missing_layer_curve_queries_do_not_flush_pending_key_creation(
    maya_cmds,
):
    target = maya_cmds.createNode("transform")
    layer = maya_cmds.animLayer("Correction", attribute=target + ".ty")
    mod = bdu.ModifierManager()
    keyframe = _manager(target + ".ty", mod).anim_layer(layer)
    before = _states(maya_cmds)
    keyframe.set_keys([(1, 12), (5, 16)])
    assert keyframe.get_keys() == keyframe.get_key_data() == []
    assert keyframe.frames() == keyframe.values() == []
    assert keyframe.get_curve_data() is None
    assert keyframe.get_weighted() is None
    assert not keyframe.has_anim_curve() and not keyframe.has_key(1)
    assert keyframe.key_count() == 0
    assert _states(maya_cmds) == before
    keyframe.set_tangent(1, out_tangent_type="flat")
    keyframe.set_weighted(True)
    mod.do_it_dg()
    assert keyframe.frames() == [1, 5]
    assert keyframe.get_weighted() is True
    assert keyframe.get_key_data()[0].out_tangent_type == "flat"
    after = _states(maya_cmds)
    mod.undo_it()
    assert _states(maya_cmds) == before
    assert keyframe.get_curve_data() is None
    mod.redo_it()
    assert _states(maya_cmds) == after


@pytest.mark.parametrize("method", DATA_EDITS)
def test_restore_requires_existing_layer_curve_and_preserves_membership(
    maya_cmds, method
):
    original, _, layers = _layered(maya_cmds)
    data = original.anim_layer(layers[0]).get_curve_data()
    target = maya_cmds.createNode("transform")
    maya_cmds.animLayer(layers[0], edit=True, attribute=target + ".ty")
    mod = bdu.ModifierManager()
    keyframe = _manager(target + ".ty", mod).anim_layer(layers[0])
    before = _states(maya_cmds)
    members = maya_cmds.animLayer(layers[0], query=True, attribute=True)
    getattr(keyframe, method)(
        data if method == "set_curve_data" else data.keys
    )
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert _states(maya_cmds) == before
    assert (
        maya_cmds.animLayer(layers[0], query=True, attribute=True) == members
    )
    assert not mod.can_undo


@pytest.mark.parametrize("method", ["get_keys", "set_key", "delete_key"])
def test_nonmember_attribute_is_rejected_without_joining_layer(
    maya_cmds, method
):
    target = maya_cmds.createNode("transform")
    layer = maya_cmds.animLayer("Correction")
    mod = bdu.ModifierManager()
    keyframe = _manager(target + ".ty", mod).anim_layer(layer)
    before = _states(maya_cmds)
    if method == "get_keys":
        with pytest.raises(RuntimeError):
            keyframe.get_keys()
    else:
        if method == "set_key":
            keyframe.set_key(12, 1)
        else:
            keyframe.delete_key(1)
        with pytest.raises(RuntimeError):
            mod.do_it_dg()
    assert not maya_cmds.animLayer(layer, query=True, attribute=True)
    assert _states(maya_cmds) == before
    assert not mod.can_undo


def test_layer_and_target_rename_keep_identity_for_queries_and_queued_edits(
    maya_cmds,
):
    original, mod, layers = _layered(maya_cmds)
    keyframe = original.anim_layer(layers[0])
    before = keyframe.get_curve_data()
    keyframe.delete_key(1)
    layer = maya_cmds.rename(layers[0], "RenamedCorrection")
    target = maya_cmds.rename(
        original.plug.name().split(".")[0], "renamedTarget"
    )
    assert keyframe.get_curve_data() == before
    mod.do_it_dg()
    assert keyframe.frames() == [5]
    assert _curve_name(maya_cmds, layer, target + ".translateY")
    mod.undo_it()
    assert keyframe.get_curve_data() == before


@pytest.mark.parametrize("delete", ["layer", "target"])
def test_deleted_identity_is_not_replaced_by_same_name(maya_cmds, delete):
    original, mod, layers = _layered(maya_cmds)
    keyframe = original.anim_layer(layers[0])
    keyframe.delete_key(1)
    if delete == "layer":
        name = layers[0]
        maya_cmds.delete(name)
        maya_cmds.animLayer(name, attribute=original.plug.name())
    else:
        name = original.plug.name().split(".")[0]
        maya_cmds.delete(name)
        maya_cmds.createNode("transform", name=name)
        maya_cmds.animLayer(
            layers[0], edit=True, attribute=name + ".translateY"
        )
    before = _states(maya_cmds)
    with pytest.raises(RuntimeError):
        keyframe.get_keys()
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert _states(maya_cmds) == before
    assert not mod.can_undo


@pytest.mark.parametrize("lock", ["layer", "layer_node", "plug", "curve"])
@pytest.mark.parametrize("method", ["set_key", "delete_key", "set_curve_data"])
def test_layer_edits_recheck_locks_after_queueing(maya_cmds, lock, method):
    original, mod, layers = _layered(maya_cmds)
    keyframe = original.anim_layer(layers[0])
    before = keyframe.get_curve_data()
    if method == "set_key":
        keyframe.set_key(30, 3)
    elif method == "delete_key":
        keyframe.delete_key(1)
    else:
        keyframe.set_curve_data(replace(before, weighted=True))
    if lock == "layer":
        maya_cmds.animLayer(layers[0], edit=True, lock=True)
    elif lock == "layer_node":
        maya_cmds.lockNode(layers[0], lock=True)
    elif lock == "plug":
        maya_cmds.setAttr(original.plug.name(), lock=True)
    else:
        maya_cmds.lockNode(
            _curve_name(maya_cmds, layers[0], original.plug.name()), lock=True
        )
    assert keyframe.get_curve_data() == before
    states = _states(maya_cmds)
    with pytest.raises(
        RuntimeError, match=None if method == "set_key" else "locked"
    ):
        mod.do_it_dg()
    assert _states(maya_cmds) == states
    assert not mod.can_undo


def test_layer_native_creation_and_edits_rollback_on_late_failure(maya_cmds):
    original, mod, layers = _layered(maya_cmds)
    first = original.anim_layer(layers[0])
    second = original.anim_layer(layers[1])
    target = maya_cmds.createNode("transform", name="fresh")
    maya_cmds.animLayer(layers[0], edit=True, attribute=target + ".ty")
    fresh = _manager(target + ".ty", mod).anim_layer(layers[0])
    before = _states(maya_cmds)
    first.set_key(20, 3)
    second.set_weighted(True)
    fresh.set_key(12, 1)
    fresh.set_tangent(1, out_tangent_type="flat")
    _manager(target + ".tz", mod).anim_layer(layers[0]).delete_key(1)
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert _states(maya_cmds) == before
    assert fresh.get_curve_data() is None
    assert not mod.can_undo and not mod.can_redo


@pytest.mark.parametrize("layered", [False, True])
def test_base_layer_queries_and_edits_choose_base_curve(maya_cmds, layered):
    original, mod, layers = _layered(maya_cmds)
    if not layered:
        target = maya_cmds.createNode("transform", name="unlayered")
        for frame in (1, 5):
            maya_cmds.setKeyframe(target + ".ty", time=frame, value=frame)
        original = _manager(target + ".ty", mod)
    base = maya_cmds.animLayer(query=True, root=True)
    keyframe = original.anim_layer(base)
    assert keyframe.get_keys() == [(1, 1), (5, 5)]
    selected = keyframe._get_anim_curve_fn().name()
    before = _states(maya_cmds)
    keyframe.delete_key(1)
    mod.do_it_dg()
    after = _states(maya_cmds)
    assert keyframe.get_keys() == [(5, 5)]
    assert {
        name: state for name, state in after.items() if name != selected
    } == {name: state for name, state in before.items() if name != selected}
    mod.undo_it()
    assert _states(maya_cmds) == before


def test_layer_query_only_manager_requires_modifier_for_edits(maya_cmds):
    original, _, layers = _layered(maya_cmds)
    keyframe = KeyframeManager(original.plug).anim_layer(layers[0])
    assert keyframe.has_anim_curve()
    with pytest.raises(RuntimeError, match="ModifierManager"):
        keyframe.set_key(12, 1)


def test_layer_membership_is_rechecked_after_edit_was_queued(maya_cmds):
    original, mod, layers = _layered(maya_cmds)
    keyframe = original.anim_layer(layers[0])
    keyframe.set_key(12, 3)
    maya_cmds.animLayer(
        layers[0], edit=True, removeAttribute=original.plug.name()
    )
    before = _states(maya_cmds)
    with pytest.raises(RuntimeError):
        keyframe.get_keys()
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert _states(maya_cmds) == before
    assert not mod.can_undo


@pytest.mark.parametrize("method", ["set_key", "delete_key", "set_curve_data"])
def test_referenced_layer_queries_allow_reading_and_edits_fail(
    maya_cmds, tmp_path, method
):
    original, _, layers = _layered(maya_cmds)
    expected = original.anim_layer(layers[0]).get_curve_data()
    path = str(tmp_path / "layer_reference.ma")
    maya_cmds.file(rename=path)
    maya_cmds.file(save=True, type="mayaAscii")
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(path, reference=True, namespace="ref")
    mod = bdu.ModifierManager()
    keyframe = _manager("ref:target.translateY", mod).anim_layer(
        "ref:targetCorrection"
    )
    assert keyframe.get_curve_data() == expected
    if method == "set_key":
        keyframe.set_key(12, 3)
    elif method == "delete_key":
        keyframe.delete_key(1)
    else:
        keyframe.set_curve_data(replace(expected, weighted=True))
    before = _states(maya_cmds)
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert _states(maya_cmds) == before
    assert not mod.can_undo


def test_base_layer_can_create_first_key_on_unlayered_attribute(maya_cmds):
    maya_cmds.animLayer("Unrelated")
    base = maya_cmds.animLayer(query=True, root=True)
    target = maya_cmds.createNode("transform")
    mod = bdu.ModifierManager()
    keyframe = _manager(target + ".ty", mod).anim_layer(base)
    assert keyframe.get_curve_data() is None
    before = _states(maya_cmds)
    keyframe.set_keys([(1, 12), (5, 16)])
    mod.do_it_dg()
    assert keyframe.get_keys() == [(1, 12), (5, 16)]
    after = _states(maya_cmds)
    mod.undo_it()
    assert _states(maya_cmds) == before
    assert keyframe.get_curve_data() is None
    mod.redo_it()
    assert _states(maya_cmds) == after


def test_layer_curve_can_be_deleted_then_recreated_in_one_history(maya_cmds):
    original, mod, layers = _layered(maya_cmds)
    keyframe = original.anim_layer(layers[0])
    before = _states(maya_cmds)
    keyframe.delete_anim_curve()
    keyframe.set_key(12, 3)
    keyframe.set_weighted(True)
    mod.do_it_dg()
    assert keyframe.frames() == [3]
    assert keyframe.get_weighted() is True
    after = _states(maya_cmds)
    for _ in range(2):
        mod.undo_it()
        assert _states(maya_cmds) == before
        mod.redo_it()
        assert _states(maya_cmds) == after


@pytest.mark.parametrize("plug", ["translate", "text"])
def test_layer_selection_does_not_make_unsupported_plug_editable(
    maya_cmds, plug
):
    target = maya_cmds.createNode("transform")
    layer = maya_cmds.animLayer("Correction")
    if plug == "text":
        maya_cmds.addAttr(target, longName="text", dataType="string")
    keyframe = _manager(target + "." + plug, bdu.ModifierManager()).anim_layer(
        layer
    )
    with pytest.raises(RuntimeError):
        keyframe.get_keys()


@pytest.mark.parametrize("layered", [False, True])
def test_key_setting_resolves_aliases_duplicate_dag_names_and_sparse_indices(
    maya_cmds,
    layered,
):
    layer = maya_cmds.animLayer("Correction") if layered else None
    mod = bdu.ModifierManager()
    managers = []
    for parent in ("first", "second"):
        parent = maya_cmds.createNode("transform", name=parent)
        target = maya_cmds.createNode("transform", name="ctrl", parent=parent)
        target = "|" + parent + "|ctrl"
        maya_cmds.aliasAttr("travel", target + ".tx")
        maya_cmds.addAttr(
            target, longName="samples", attributeType="double", multi=True
        )
        for attribute in ("travel", "samples[4]", "samples[12]"):
            plug = target + "." + attribute
            keyframe = _manager(plug, mod)
            if layer is not None:
                maya_cmds.animLayer(layer, edit=True, attribute=plug)
                keyframe = keyframe.anim_layer(layer)
            keyframe.set_key(len(managers) + 1, 1)
            managers.append(keyframe)
    mod.do_it_dg()
    before = _states(maya_cmds)
    assert [keyframe.get_keys() for keyframe in managers] == [
        [(1, value)] for value in range(1, 7)
    ]
    for parent in ("first", "second"):
        assert maya_cmds.getAttr(
            "|" + parent + "|ctrl.samples", multiIndices=True
        ) == [4, 12]
    mod.undo_it()
    assert all(not keyframe.has_anim_curve() for keyframe in managers)
    mod.redo_it()
    assert _states(maya_cmds) == before


def test_nonmember_is_not_confused_with_same_named_dag_node(maya_cmds):
    for parent in ("first", "second"):
        maya_cmds.createNode("transform", name=parent)
        maya_cmds.createNode("transform", name="ctrl", parent=parent)
    layer = maya_cmds.animLayer("Correction", attribute="|first|ctrl.tx")
    mod = bdu.ModifierManager()
    keyframe = _manager("|second|ctrl.tx", mod).anim_layer(layer)
    with pytest.raises(RuntimeError, match="not a member"):
        keyframe.get_keys()
    before = _states(maya_cmds)
    keyframe.set_key(12, 1)
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert _states(maya_cmds) == before


def test_layer_selection_does_not_filter_diagnostic_candidates(maya_cmds):
    original, _, layers = _layered(maya_cmds)
    expected = tuple(curve.name for curve in original.find_anim_curves())
    assert (
        tuple(
            curve.name
            for curve in original.anim_layer(layers[0]).find_anim_curves()
        )
        == expected
    )
    assert (
        tuple(
            curve.name
            for curve in original.anim_layer(layers[1]).find_anim_curves()
        )
        == expected
    )


def test_base_layer_without_curve_does_not_choose_additive_curve(maya_cmds):
    target = maya_cmds.createNode("transform")
    layer = maya_cmds.animLayer("Correction", attribute=target + ".ty")
    maya_cmds.setKeyframe(target + ".ty", animLayer=layer, time=1, value=12)
    mod = bdu.ModifierManager()
    original = _manager(target + ".ty", mod)
    base = original.anim_layer(maya_cmds.animLayer(query=True, root=True))
    addition = original.anim_layer(layer)
    before = addition.get_curve_data()
    assert base.get_keys() == []
    base.set_key(4, 1)
    mod.do_it_dg()
    assert base.has_anim_curve()
    assert addition.get_curve_data() == before
    mod.undo_it()
    assert base.get_keys() == []
    assert addition.get_curve_data() == before


@pytest.mark.parametrize("family", ["translate", "rotate"])
@pytest.mark.parametrize("constraint_first", [False, True])
def test_layer_and_pairblend_resolve_same_axis(
    maya_cmds, family, constraint_first
):
    target = maya_cmds.createNode("transform", name="ctrl")
    driver = maya_cmds.createNode("transform", name="driver")
    for axis in "XYZ":
        maya_cmds.setKeyframe(target + "." + family + axis, time=1, value=1)
        maya_cmds.setKeyframe(driver + "." + family + axis, time=1, value=20)
    constraint = (
        maya_cmds.pointConstraint
        if family == "translate"
        else maya_cmds.orientConstraint
    )
    if constraint_first:
        constraint(driver, target)
    layer = maya_cmds.animLayer("Correction")
    for index, axis in enumerate("XYZ"):
        plug = target + "." + family + axis
        maya_cmds.animLayer(layer, edit=True, attribute=plug)
        maya_cmds.setKeyframe(plug, animLayer=layer, time=1, value=10 + index)
    if not constraint_first:
        constraint(driver, target)
    mod = bdu.ModifierManager()
    keyframe = _manager(target + "." + family + "Y", mod).anim_layer(layer)
    selected = _curve_name(maya_cmds, layer, keyframe.plug.name())
    assert (
        keyframe.get_curve_data()
        == bdu.Nodes().existing(selected).keyframe.get_curve_data()
    )
    before = _states(maya_cmds)
    keyframe.set_keys([(3, 12), (5, 18)])
    keyframe.delete_key(1)
    mod.do_it_dg()
    after = _states(maya_cmds)
    assert keyframe.frames() == [3, 5]
    assert {n: s for n, s in after.items() if n != selected} == {
        n: s for n, s in before.items() if n != selected
    }
    mod.undo_it()
    assert _states(maya_cmds) == before
    mod.redo_it()
    assert _states(maya_cmds) == after
