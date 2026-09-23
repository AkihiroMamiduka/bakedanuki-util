from __future__ import annotations

from dataclasses import replace

import pytest

import bd_util as bdu
from bd_util.maya.node.animation_clip import AnimationClip, NodeAnimationData

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _node(cmds, name, *, parent=None, values=((1, 2), (5, 10))):
    kwargs = {} if parent is None else {"parent": parent}
    node = cmds.createNode("transform", name=name, **kwargs)
    path = cmds.ls(node, long=True)[0]
    for frame, value in values:
        cmds.setKeyframe(
            path + ".tx",
            time=frame,
            value=value,
            inTangentType="linear",
            outTangentType="linear",
        )
    return path


def _values(cmds, plug, frames=(1, 3, 5)):
    return [cmds.getAttr(plug, time=frame) for frame in frames]


def _layer(cmds, node, name, values=((1, 3), (5, 7))):
    layer = cmds.animLayer(name)
    cmds.animLayer(layer, edit=True, attribute=node + ".tx")
    for frame, value in values:
        cmds.setKeyframe(
            node + ".tx",
            animLayer=layer,
            time=frame,
            value=value,
            noResolve=True,
            inTangentType="linear",
            outTangentType="linear",
        )
    return layer


def test_capture_uses_short_name_and_restore_survives_reparent(maya_cmds):
    cmds = maya_cmds
    first = cmds.createNode("transform", name="first")
    second = cmds.createNode("transform", name="second")
    source = _node(cmds, "portableCtrl", parent=first)
    clip = AnimationClip.capture([source], attributes=["tx"])
    assert clip.nodes[0].name == "portableCtrl"

    moved = cmds.ls(cmds.parent(source, second)[0], long=True)[0]
    cmds.cutKey(moved + ".tx", clear=True)
    cmds.setAttr(moved + ".tx", 0)
    mod = bdu.ModifierManager()
    clip.restore(mod, mode="replace_all")
    mod.do_it_dg()
    assert _values(cmds, moved + ".tx") == pytest.approx([2, 6, 10])
    mod.undo_it()
    assert _values(cmds, moved + ".tx") == pytest.approx([0, 0, 0])


def test_duplicate_dag_names_use_full_paths_and_require_unambiguous_extract(
    maya_cmds,
):
    cmds = maya_cmds
    left_group = cmds.createNode("transform", name="left")
    right_group = cmds.createNode("transform", name="right")
    left = _node(cmds, "ctrl", parent=left_group)
    right = _node(cmds, "ctrl", parent=right_group, values=((1, 20), (5, 40)))

    one = AnimationClip.capture([left], attributes=["tx"])
    assert one.nodes[0].name == left
    assert one.extract(nodes=["ctrl"]).nodes[0].name == left

    clip = AnimationClip.capture([left, right], attributes=["tx"])
    assert [node.name for node in clip.nodes] == [left, right]
    with pytest.raises(ValueError, match="Ambiguous clip node"):
        clip.extract(nodes=["ctrl"])
    extracted = clip.extract(nodes=[right, left])
    assert [node.name for node in extracted.nodes] == [right, left]

    for path in (left, right):
        cmds.cutKey(path + ".tx", clear=True)
        cmds.setAttr(path + ".tx", 0)
    mod = bdu.ModifierManager()
    clip.restore(mod, mode="replace_all")
    mod.do_it_dg()
    assert _values(cmds, left + ".tx") == pytest.approx([2, 6, 10])
    assert _values(cmds, right + ".tx") == pytest.approx([20, 30, 40])


def test_extract_preserves_metadata_and_is_independent_of_scene_and_source(
    maya_cmds,
):
    cmds = maya_cmds
    a = _node(cmds, "a")
    b = _node(cmds, "b", values=((1, 4), (5, 12)))
    c = _node(cmds, "c", values=((1, 8), (5, 24)))
    clip = AnimationClip.capture([a, b, c], attributes=["tx"])
    cmds.delete(a, b, c)

    extracted = clip.extract(nodes=["c", "a"])
    assert [node.name for node in extracted.nodes] == ["c", "a"]
    assert extracted is not clip
    assert (
        extracted.start_frame,
        extracted.end_frame,
        extracted.seconds_per_frame,
        extracted.sample_by,
        extracted.clipped,
        extracted.layer_mode,
        extracted.schema_version,
    ) == (
        clip.start_frame,
        clip.end_frame,
        clip.seconds_per_frame,
        clip.sample_by,
        clip.clipped,
        clip.layer_mode,
        clip.schema_version,
    )
    source_c = next(node for node in clip.nodes if node.name == "c")
    extracted.nodes[0].channels[0].curve.keys[0].value = 100
    assert source_c.channels[0].curve.keys[0].value == 8
    assert AnimationClip.from_json(extracted.to_json()) == extracted
    assert extracted.reversed().reversed() == extracted


def test_extract_revalidates_excluded_source_data(maya_cmds):
    cmds = maya_cmds
    a = _node(cmds, "a")
    b = _node(cmds, "b")
    clip = AnimationClip.capture([a, b], attributes=["tx"])
    clip.nodes[1].channels[0].curve.keys[0].value = float("nan")
    with pytest.raises(ValueError, match="finite"):
        clip.extract(nodes=["a"])


def test_extract_rejects_invalid_and_duplicate_selections(maya_cmds):
    cmds = maya_cmds
    a = _node(cmds, "a")
    clip = AnimationClip.capture([a], attributes=["tx"])
    with pytest.raises(TypeError, match="iterable"):
        clip.extract(nodes="a")
    with pytest.raises(ValueError, match="must not be empty"):
        clip.extract(nodes=[])
    with pytest.raises(ValueError, match="Unknown clip node"):
        clip.extract(nodes=["missing"])
    with pytest.raises(ValueError, match="Duplicate clip node"):
        clip.extract(nodes=["a", "a"])

    empty = replace(
        clip,
        nodes=(NodeAnimationData("empty", ()), clip.nodes[0]),
    )
    with pytest.raises(ValueError, match="contain no channels"):
        empty.extract(nodes=["empty"])


def test_extract_keeps_required_layer_ancestors_and_prunes_other_layers(
    maya_cmds,
):
    cmds = maya_cmds
    a = _node(cmds, "a")
    b = _node(cmds, "b")
    parent = cmds.animLayer("Parent")
    child = _layer(cmds, a, "Child")
    cmds.animLayer(child, edit=True, parent=parent)
    cmds.setKeyframe(child + ".weight", time=1, value=0.5)
    cmds.setKeyframe(child + ".weight", time=5, value=1.0)
    _layer(cmds, b, "Other")
    expected = _values(cmds, a + ".tx")
    clip = AnimationClip.capture(
        [a, b], attributes=["tx"], layer_mode="preserve"
    )

    extracted = clip.extract(nodes=["a"])
    assert [node.name for node in extracted.nodes] == ["a"]
    assert [layer.name for layer in extracted.layers] == [parent, child]
    assert extracted.layers[1].parent == parent
    assert {channel.layer for channel in extracted.nodes[0].channels} == {
        None,
        child,
    }
    assert extracted.root_settings == clip.root_settings

    cmds.file(new=True, force=True)
    target = _node(cmds, "a", values=())
    mod = bdu.ModifierManager()
    extracted.restore(mod, mode="replace_all")
    mod.do_it_dg()
    assert cmds.animLayer(child, query=True, parent=True) == parent
    assert not cmds.objExists("Other")
    assert _values(cmds, target + ".tx") == pytest.approx(expected)
    mod.undo_it()
    assert not cmds.objExists(parent)


def test_namespaced_short_name_is_not_matched_without_namespace(maya_cmds):
    cmds = maya_cmds
    cmds.namespace(add="character_a")
    source = _node(cmds, "character_a:root_ctrl")
    clip = AnimationClip.capture([source], attributes=["tx"])
    assert clip.nodes[0].name == "character_a:root_ctrl"
    assert (
        clip.extract(nodes=["character_a:root_ctrl"]).nodes[0].name
        == "character_a:root_ctrl"
    )
    with pytest.raises(ValueError, match="Unknown clip node"):
        clip.extract(nodes=["root_ctrl"])
