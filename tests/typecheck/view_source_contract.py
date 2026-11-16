# coding: utf-8
"""再利用するViewの入力元差替えを、型付きBindingとViewModelへ固定する。"""

from typing import assert_type

from bd_util.maya.ui import MayaFloatPlugsBinding, MayaIntPlugsBinding
from bd_util.ui import (
    BoolBinding,
    BoolCheckBox,
    BoolViewModel,
    EnumBinding,
    EnumComboBox,
    EnumViewModel,
    FloatBinding,
    FloatRangeSliderSpinBox,
    FloatSlider,
    FloatSliderSpinBox,
    FloatSpinBox,
    FloatValueStepSpinBox,
    FloatViewModel,
    IntBinding,
    IntRangeSliderSpinBox,
    IntSlider,
    IntSliderSpinBox,
    IntSpinBox,
    IntValueStepSpinBox,
    IntViewModel,
    StringBinding,
    StringLineEdit,
    StringViewModel,
)
from bd_util.ui.binding.bool.store import BoolValueStore
from bd_util.ui.binding.enum.store import EnumValueStore
from bd_util.ui.binding.float.store import FloatValueStore
from bd_util.ui.binding.int.store import IntValueStore
from bd_util.ui.binding.string.store import StringValueStore


def check_float_source(
    source: FloatViewModel,
    binding: FloatBinding[FloatValueStore],
    maya_binding: MayaFloatPlugsBinding,
    spin: FloatSpinBox,
    slider: FloatSlider,
    step: FloatValueStepSpinBox,
    combined: FloatSliderSpinBox,
    ranged: FloatRangeSliderSpinBox,
) -> None:
    """float系の単体・複合Viewが同じ入力元契約を持つことを確認する。"""
    for view in (spin, slider, step, combined, ranged):
        assert_type(view.set_source(source), None)
        assert_type(view.set_source(binding), None)
        assert_type(view.set_source(maya_binding), None)
        assert_type(view.view_model, FloatViewModel)


def check_int_source(
    source: IntViewModel,
    binding: IntBinding[IntValueStore],
    maya_binding: MayaIntPlugsBinding,
    spin: IntSpinBox,
    slider: IntSlider,
    step: IntValueStepSpinBox,
    combined: IntSliderSpinBox,
    ranged: IntRangeSliderSpinBox,
) -> None:
    """整数系の単体・複合Viewが同じ入力元契約を持つことを確認する。"""
    for view in (spin, slider, step, combined, ranged):
        assert_type(view.set_source(source), None)
        assert_type(view.set_source(binding), None)
        assert_type(view.set_source(maya_binding), None)
        assert_type(view.view_model, IntViewModel)


def check_other_sources(
    bool_source: BoolViewModel,
    bool_binding: BoolBinding[BoolValueStore],
    check_box: BoolCheckBox,
    enum_source: EnumViewModel,
    enum_binding: EnumBinding[EnumValueStore],
    combo_box: EnumComboBox,
    string_source: StringViewModel,
    string_binding: StringBinding[StringValueStore],
    line_edit: StringLineEdit,
) -> None:
    """真偽値・enum・文字列Viewの入力元と戻り値の型を確認する。"""
    assert_type(check_box.set_source(bool_source), None)
    assert_type(check_box.set_source(bool_binding), None)
    assert_type(check_box.view_model, BoolViewModel)
    assert_type(combo_box.set_source(enum_source), None)
    assert_type(combo_box.set_source(enum_binding), None)
    assert_type(combo_box.view_model, EnumViewModel)
    assert_type(line_edit.set_source(string_source), None)
    assert_type(line_edit.set_source(string_binding), None)
    assert_type(line_edit.view_model, StringViewModel)
