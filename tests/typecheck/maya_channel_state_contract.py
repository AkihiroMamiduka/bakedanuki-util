# coding: utf-8
"""状態編集APIの型と、既存PlugOperatorからの補完契約を固定する。"""

from typing import assert_type

from bd_util.maya.ui import (
    ChannelDisplayState,
    MayaChannelStateBinding,
    MayaChannelStateSnapshot,
    MayaChannelTargetState,
    resolve_bool_plug,
    resolve_enum_plug,
    resolve_float_plug,
)
from bd_util.ui import qt

binding = MayaChannelStateBinding(
    [
        resolve_bool_plug("node", "visibility"),
        resolve_enum_plug("node", "rotateOrder"),
        resolve_float_plug("node", "tx"),
    ],
    parent=qt.QObject(),
)
assert_type(binding.state, MayaChannelStateSnapshot)
assert_type(binding.state.display_state, ChannelDisplayState | None)
assert_type(binding.state.locked, bool | None)
assert_type(binding.state.display_mixed, bool)
assert_type(binding.state.lock_mixed, bool)
assert_type(binding.state.targets, tuple[MayaChannelTargetState, ...])
assert_type(binding.state.targets[0].parent_locked, bool)
assert_type(binding.state.targets[0].can_set_display, bool)
assert_type(binding.state.targets[0].can_set_locked, bool)
assert_type(binding.set_display_state("channel_box"), bool)
assert_type(binding.set_locked(False), bool)
assert_type(binding.refresh(), bool)
assert_type(binding.dispose(), None)
