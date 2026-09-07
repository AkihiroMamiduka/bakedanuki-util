from typing import assert_type

from bd_util._sample.maya.ui.bool_sample import multi_attribute
from bd_util.ui import BoolBinding, BoolCheckBox, PythonBoolAttributeStore, qt

data = multi_attribute.DisplayOptionsData(allow_editing=False)
widget = multi_attribute.DisplayOptionsWidget(data)
assert_type(widget.data, multi_attribute.DisplayOptionsData)
assert_type(widget.data.visible, bool)
assert_type(widget.data.show_labels, bool)
assert_type(widget.data.allow_editing, bool)
for binding in (
    widget.visible_binding,
    widget.labels_binding,
    widget.editing_binding,
):
    assert_type(
        binding,
        BoolBinding[
            PythonBoolAttributeStore[multi_attribute.DisplayOptionsData]
        ],
    )
    assert_type(binding.store.instance, multi_attribute.DisplayOptionsData)
    binding.changed.connect(print)
assert_type(widget.visible_check_box, BoolCheckBox)
assert_type(widget.labels_check_box, BoolCheckBox)
assert_type(widget.editing_check_box, BoolCheckBox)
assert_type(widget.options_group, qt.QGroupBox)
assert_type(widget.preview_content, qt.QWidget)
assert_type(widget.preview_label, qt.QLabel)
assert_type(widget.refresh_from_data(), None)
window = multi_attribute.show()
assert_type(window, multi_attribute.DisplayOptionsWindow)
assert_type(window.widget, multi_attribute.DisplayOptionsWidget)
assert_type(multi_attribute.dispose(), None)
