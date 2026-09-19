# coding: utf-8
"""異種属性の一括入力でbinding型と値型の対応が辿れることを固定する。"""

from collections.abc import Sequence
from typing import assert_type

from bd_util.maya.ui import (
    MayaBoolPlugsBinding,
    MayaBoolValueEdit,
    MayaEnumPlugsBinding,
    MayaEnumValueEdit,
    MayaFloatPlugsBinding,
    MayaFloatValueEdit,
    MayaFloatOffsetEdit,
    MayaPlugsValueEdit,
    apply_plugs_values,
    resolve_bool_plug,
    resolve_enum_plug,
    resolve_float_plug,
)

bool_edit = MayaBoolValueEdit(
    MayaBoolPlugsBinding([resolve_bool_plug("node", "visibility")]), False
)
float_edit = MayaFloatValueEdit(
    MayaFloatPlugsBinding([resolve_float_plug("node", "translateX")]), 5.0
)
enum_edit = MayaEnumValueEdit(
    MayaEnumPlugsBinding([resolve_enum_plug("node", "rotateOrder")]), 5
)
assert_type(bool_edit.binding, MayaBoolPlugsBinding)
assert_type(bool_edit.value, bool)
assert_type(float_edit.binding, MayaFloatPlugsBinding)
assert_type(float_edit.value, float)
float_offset = MayaFloatOffsetEdit(float_edit.binding, 1.0)
assert_type(float_offset.binding, MayaFloatPlugsBinding)
assert_type(float_offset.offset, float)
assert_type(enum_edit.binding, MayaEnumPlugsBinding)
assert_type(enum_edit.value, int)


def apply_edits(edits: Sequence[MayaPlugsValueEdit]) -> bool:
    """型の異なる入力列とbool戻り値を公開APIへ受け渡す。"""
    assert_type(apply_plugs_values(edits), bool)
    for edit in edits:
        if isinstance(edit, MayaBoolValueEdit):
            assert_type(edit.binding, MayaBoolPlugsBinding)
            assert_type(edit.value, bool)
        elif isinstance(edit, MayaFloatValueEdit):
            assert_type(edit.binding, MayaFloatPlugsBinding)
            assert_type(edit.value, float)
        elif isinstance(edit, MayaFloatOffsetEdit):
            assert_type(edit.binding, MayaFloatPlugsBinding)
            assert_type(edit.offset, float)
        else:
            assert_type(edit.binding, MayaEnumPlugsBinding)
            assert_type(edit.value, int)
    return apply_plugs_values(edits)


assert_type(apply_edits([bool_edit, float_edit, enum_edit]), bool)
assert_type(apply_plugs_values((float_edit, float_offset, enum_edit)), bool)
