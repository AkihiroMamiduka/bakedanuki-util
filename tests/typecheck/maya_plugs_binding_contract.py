# coding: utf-8
"""複数属性Bindingの公開値と既存Viewへの受け渡し型を固定する。"""

from typing import assert_type

from bd_util.maya.ui.binding.plugs_binding import (
    MayaBoolPlugsBinding,
    MayaEnumPlugsBinding,
    MayaFloatPlugsBinding,
    MayaIntPlugsBinding,
    MayaIntPlugBinding,
    MayaStringPlugsBinding,
)


from bd_util.maya.ui.binding.plugs_state import MayaPlugTargetState
from bd_util.maya.ui import (
    MayaEnumValueEdit,
    MayaPlugInputState,
    MayaScalarPasteResult,
    MayaScalarValueTransfer,
    apply_plugs_values,
    apply_scalar_value_to_paths,
    apply_scalar_value_transfer,
    apply_scalar_value_transfer_to_paths,
    connected_plug_edit_reason,
    inspect_plug_input_state,
    resolve_bool_plug,
    resolve_enum_plug,
    resolve_float_plug,
    resolve_int_plug,
    resolve_string_plug,
    shared_plugs_lifetime,
    shared_scalar_plug_nodes,
)
from bd_util.ui import (
    BoolComboBox,
    BoolViewModel,
    FloatSpinBox,
    FloatSliderSpinBox,
    FloatViewModel,
    qt,
)


def lifetime_monitor_contract(enabled: bool) -> None:
    """削除監視のbool指定を全scalarと単一整数の公開入口で受け付ける。"""
    with shared_plugs_lifetime() as scope:
        assert_type(scope, None)
    with shared_scalar_plug_nodes() as nodes_scope:
        assert_type(nodes_scope, None)
    assert_type(
        MayaBoolPlugsBinding(
            [resolve_bool_plug("node", "visibility")],
            monitor=False,
            monitor_lifetime=enabled,
        ),
        MayaBoolPlugsBinding,
    )
    assert_type(
        MayaFloatPlugsBinding(
            [resolve_float_plug("node", "tx")],
            monitor=False,
            monitor_lifetime=enabled,
        ),
        MayaFloatPlugsBinding,
    )
    assert_type(
        MayaIntPlugsBinding(
            [resolve_int_plug("node", "count")],
            monitor=False,
            monitor_lifetime=enabled,
        ),
        MayaIntPlugsBinding,
    )
    assert_type(
        MayaIntPlugBinding(
            resolve_int_plug("node", "count"),
            monitor=False,
            monitor_lifetime=enabled,
        ),
        MayaIntPlugBinding,
    )
    assert_type(
        MayaEnumPlugsBinding(
            [resolve_enum_plug("node", "mode")],
            monitor=False,
            monitor_lifetime=enabled,
        ),
        MayaEnumPlugsBinding,
    )
    assert_type(
        MayaStringPlugsBinding(
            [resolve_string_plug("node", "label")],
            monitor=False,
            monitor_lifetime=enabled,
        ),
        MayaStringPlugsBinding,
    )


def operation_enum_validation_contract(
    binding: MayaEnumPlugsBinding, transfer: MayaScalarValueTransfer
) -> None:
    """一括enum検証の選択肢と、値転送APIからの型付き指定を固定する。"""
    edits = [MayaEnumValueEdit(binding, 1)]
    assert_type(apply_plugs_values(edits), bool)
    assert_type(apply_plugs_values(edits, enum_validation="per_write"), bool)
    assert_type(apply_plugs_values(edits, enum_validation="operation"), bool)
    assert_type(
        apply_scalar_value_transfer(
            ["target"], transfer, enum_validation="operation"
        ),
        MayaScalarPasteResult,
    )
    assert_type(
        apply_scalar_value_transfer_to_paths(
            ["target"], ["mode"], transfer, enum_validation="operation"
        ),
        MayaScalarPasteResult,
    )
    assert_type(
        apply_scalar_value_to_paths(
            ["target"], ["mode"], transfer, enum_validation="operation"
        ),
        MayaScalarPasteResult,
    )


bool_binding = MayaBoolPlugsBinding([resolve_bool_plug("node", "visibility")])
assert_type(
    MayaBoolPlugsBinding(
        [resolve_bool_plug("node", "visibility")], monitor=False
    ),
    MayaBoolPlugsBinding,
)
assert_type(
    MayaFloatPlugsBinding([resolve_float_plug("node", "tx")], monitor=False),
    MayaFloatPlugsBinding,
)
assert_type(
    MayaIntPlugsBinding([resolve_int_plug("node", "count")], monitor=False),
    MayaIntPlugsBinding,
)
assert_type(
    MayaEnumPlugsBinding([resolve_enum_plug("node", "mode")], monitor=False),
    MayaEnumPlugsBinding,
)
assert_type(
    MayaStringPlugsBinding(
        [resolve_string_plug("node", "label")], monitor=False
    ),
    MayaStringPlugsBinding,
)
float_binding = MayaFloatPlugsBinding(
    [resolve_float_plug("node", "translateX")]
)
assert_type(
    MayaBoolPlugsBinding(
        [resolve_bool_plug("node", "visibility")],
        key_animated=True,
        track_input_state=True,
    ),
    MayaBoolPlugsBinding,
)
assert_type(
    MayaFloatPlugsBinding(
        [resolve_float_plug("node", "translateX")], key_animated=True
    ),
    MayaFloatPlugsBinding,
)
assert_type(
    MayaEnumPlugsBinding(
        [resolve_enum_plug("node", "mode")], key_animated=True
    ),
    MayaEnumPlugsBinding,
)
assert_type(
    MayaBoolPlugsBinding(
        [resolve_bool_plug("node", "visibility")], edit_connected=True
    ),
    MayaBoolPlugsBinding,
)
assert_type(
    MayaFloatPlugsBinding(
        [resolve_float_plug("node", "translateX")], edit_connected=True
    ),
    MayaFloatPlugsBinding,
)
assert_type(
    MayaEnumPlugsBinding(
        [resolve_enum_plug("node", "mode")], edit_connected=True
    ),
    MayaEnumPlugsBinding,
)
assert_type(bool_binding.value, bool)
assert_type(float_binding.value, float)
assert_type(bool_binding.view_model, BoolViewModel)
assert_type(float_binding.view_model, FloatViewModel)
assert_type(bool_binding.apply_representative_value(), bool)
assert_type(float_binding.set_value(1), bool)
assert_type(bool_binding.target_states, tuple[MayaPlugTargetState, ...])
assert_type(
    bool_binding.target_states[0].input_state, MayaPlugInputState | None
)
assert_type(bool_binding.target_states[0].is_locked, bool | None)
assert_type(float_binding.target_states[0].edit_description, str | None)
assert_type(
    connected_plug_edit_reason(resolve_float_plug("node", "translateX").plug),
    str | None,
)
assert_type(
    inspect_plug_input_state(resolve_float_plug("node", "translateX").plug),
    MayaPlugInputState,
)
assert_type(float_binding.target_states[0].reason, str | None)
assert_type(float_binding.is_mixed, bool)
assert_type(bool_binding.target_count, int)
assert_type(float_binding.writable_count, int)
assert_type(bool_binding.state_changed, qt.QtCore.SignalInstance)
assert_type(float_binding.edit_failed, qt.QtCore.SignalInstance)
assert_type(BoolComboBox(bool_binding), BoolComboBox)
assert_type(FloatSpinBox(float_binding), FloatSpinBox)
assert_type(
    FloatSliderSpinBox(float_binding, minimum=0, maximum=1), FloatSliderSpinBox
)
