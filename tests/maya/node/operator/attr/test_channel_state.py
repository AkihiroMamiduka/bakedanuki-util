# coding: utf-8
import pytest

from bd_util.py.error import UnsupportedOperationError

pytestmark = pytest.mark.maya

_CHANNEL_STATES = (
    ("set_keyable", "set_keyable_direct", (True, False)),
    ("set_channel_box", "set_channel_box_direct", (False, True)),
    ("set_hidden", "set_hidden_direct", (False, False)),
)


def _channel_state(maya_cmds, plug_name):
    return (
        maya_cmds.getAttr(plug_name, keyable=True),
        maya_cmds.getAttr(plug_name, channelBox=True),
    )


def _set_channel_state(maya_cmds, plug_name, state):
    maya_cmds.setAttr(
        plug_name,
        keyable=state[0],
        channelBox=state[1],
    )


def _opposite_channel_state(target_state):
    if target_state == (True, False):
        return False, True
    return True, False


@pytest.mark.parametrize(
    ("method_name", "_direct_method_name", "target_state"),
    _CHANNEL_STATES,
)
def test_scalar_channel_state_queues_and_supports_undo_redo(
    new_scene,
    maya_cmds,
    maya_om,
    method_name,
    _direct_method_name,
    target_state,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("transform", name="node")
    plug_name = f"{node_name}.translateX"
    original_state = _opposite_channel_state(target_state)
    _set_channel_state(maya_cmds, plug_name, original_state)
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.transform(node_name)
    original_hidden = maya_om.MFnAttribute(
        node.translateX.plug.attribute()
    ).hidden

    assert getattr(node.translateX, method_name)() is None
    assert _channel_state(maya_cmds, plug_name) == original_state

    mod.do_it_dg()

    assert _channel_state(maya_cmds, plug_name) == target_state
    assert (
        maya_om.MFnAttribute(node.translateX.plug.attribute()).hidden
        is original_hidden
    )

    mod.undo_it()

    assert _channel_state(maya_cmds, plug_name) == original_state

    mod.redo_it()

    assert _channel_state(maya_cmds, plug_name) == target_state


@pytest.mark.parametrize(
    ("_method_name", "direct_method_name", "target_state"),
    _CHANNEL_STATES,
)
def test_scalar_channel_state_direct_changes_immediately(
    new_scene,
    maya_cmds,
    _method_name,
    direct_method_name,
    target_state,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("transform", name="node")
    plug_name = f"{node_name}.translateX"
    _set_channel_state(
        maya_cmds,
        plug_name,
        _opposite_channel_state(target_state),
    )
    nodes = bdu.Nodes()
    node = nodes.existing.transform(node_name)

    assert getattr(node.translateX, direct_method_name)() is None

    assert _channel_state(maya_cmds, plug_name) == target_state
    assert not nodes.modifier_manager.can_undo


@pytest.mark.parametrize(
    ("method_name", "_direct_method_name", "target_state"),
    _CHANNEL_STATES,
)
def test_scalar_compound_channel_state_expands_to_children(
    new_scene,
    maya_cmds,
    method_name,
    _direct_method_name,
    target_state,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("transform", name="node")
    child_plug_names = tuple(f"{node_name}.translate{axis}" for axis in "XYZ")
    original_state = _opposite_channel_state(target_state)
    for plug_name in child_plug_names:
        _set_channel_state(maya_cmds, plug_name, original_state)
    parent_state = _channel_state(maya_cmds, f"{node_name}.translate")
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.transform(node_name)

    assert getattr(node.translate, method_name)() is None
    assert all(
        _channel_state(maya_cmds, plug_name) == original_state
        for plug_name in child_plug_names
    )

    mod.do_it_dg()

    assert all(
        _channel_state(maya_cmds, plug_name) == target_state
        for plug_name in child_plug_names
    )
    assert _channel_state(maya_cmds, f"{node_name}.translate") == parent_state

    mod.undo_it()

    assert all(
        _channel_state(maya_cmds, plug_name) == original_state
        for plug_name in child_plug_names
    )


@pytest.mark.parametrize(
    ("_method_name", "direct_method_name", "target_state"),
    _CHANNEL_STATES,
)
def test_scalar_compound_channel_state_direct_expands_to_children(
    new_scene,
    maya_cmds,
    _method_name,
    direct_method_name,
    target_state,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("transform", name="node")
    child_plug_names = tuple(f"{node_name}.translate{axis}" for axis in "XYZ")
    for plug_name in child_plug_names:
        _set_channel_state(
            maya_cmds,
            plug_name,
            _opposite_channel_state(target_state),
        )
    nodes = bdu.Nodes()
    node = nodes.existing.transform(node_name)

    assert getattr(node.translate, direct_method_name)() is None

    assert all(
        _channel_state(maya_cmds, plug_name) == target_state
        for plug_name in child_plug_names
    )
    assert not nodes.modifier_manager.can_undo


@pytest.mark.parametrize(
    (
        "method_name",
        "_direct_method_name",
        "original_state",
        "target_state",
    ),
    (
        ("set_locked", "set_locked_direct", False, True),
        ("set_unlocked", "set_unlocked_direct", True, False),
    ),
)
def test_lock_state_queues_for_every_plug_and_supports_undo_redo(
    new_scene,
    maya_cmds,
    method_name,
    _direct_method_name,
    original_state,
    target_state,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("transform", name="node")
    plug_name = f"{node_name}.matrix"
    maya_cmds.setAttr(plug_name, lock=original_state)
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.transform(node_name)

    assert getattr(node.matrix, method_name)() is None
    assert maya_cmds.getAttr(plug_name, lock=True) is original_state

    mod.do_it_dg()

    assert maya_cmds.getAttr(plug_name, lock=True) is target_state

    mod.undo_it()

    assert maya_cmds.getAttr(plug_name, lock=True) is original_state

    mod.redo_it()

    assert maya_cmds.getAttr(plug_name, lock=True) is target_state


@pytest.mark.parametrize(
    ("method_name", "original_state", "target_state"),
    (
        ("set_locked_direct", False, True),
        ("set_unlocked_direct", True, False),
    ),
)
def test_lock_state_direct_changes_every_plug_immediately(
    new_scene,
    maya_cmds,
    method_name,
    original_state,
    target_state,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("transform", name="node")
    plug_name = f"{node_name}.matrix"
    maya_cmds.setAttr(plug_name, lock=original_state)
    nodes = bdu.Nodes()
    node = nodes.existing.transform(node_name)

    assert getattr(node.matrix, method_name)() is None

    assert maya_cmds.getAttr(plug_name, lock=True) is target_state
    assert not nodes.modifier_manager.can_undo


def test_compound_lock_uses_parent_plug_and_preserves_child_lock(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("transform", name="node")
    maya_cmds.setAttr(f"{node_name}.translateX", lock=True)
    node = bdu.Nodes().existing.transform(node_name)

    node.translate.set_locked_direct()

    assert all(
        maya_cmds.getAttr(f"{node_name}.translate{axis}", lock=True)
        for axis in "XYZ"
    )

    node.translate.set_unlocked_direct()

    assert maya_cmds.getAttr(f"{node_name}.translateX", lock=True)
    assert not maya_cmds.getAttr(f"{node_name}.translateY", lock=True)
    assert not maya_cmds.getAttr(f"{node_name}.translateZ", lock=True)


def test_queued_channel_and_lock_state_calls_preserve_order(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("transform", name="node")
    plug_name = f"{node_name}.translateX"
    nodes = bdu.Nodes()
    plug = nodes.existing.transform(node_name).translateX

    plug.set_hidden()
    plug.set_keyable()
    plug.set_locked()
    plug.set_unlocked()
    nodes.modifier_manager.do_it_dg()

    assert _channel_state(maya_cmds, plug_name) == (True, False)
    assert not maya_cmds.getAttr(plug_name, lock=True)


def test_queued_channel_and_lock_states_support_pending_created_node(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    nodes = bdu.Nodes()
    node = nodes.create.transform(name="node")

    node.translateX.set_channel_box()
    node.matrix.set_locked()

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    assert _channel_state(maya_cmds, "node.translateX") == (False, True)
    assert maya_cmds.getAttr("node.matrix", lock=True)


@pytest.mark.parametrize("direct", (False, True))
def test_unindexed_multi_rejects_channel_state_but_indexed_plug_accepts_it(
    new_scene,
    maya_cmds,
    direct,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("plusMinusAverage", name="node")
    nodes = bdu.Nodes()
    input_plug = nodes.existing.plusMinusAverage(node_name).input1D
    method_name = "set_keyable_direct" if direct else "set_keyable"

    with pytest.raises(UnsupportedOperationError, match="indexed multi"):
        getattr(input_plug, method_name)()

    indexed_plug = input_plug[0]
    getattr(indexed_plug, method_name)()
    if not direct:
        nodes.modifier_manager.do_it_dg()

    assert _channel_state(maya_cmds, f"{node_name}.input1D[0]") == (
        True,
        False,
    )
