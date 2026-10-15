# coding: utf-8
from dataclasses import dataclass
from typing import assert_type

from bd_util._sample.maya.ui.int_sample import maya_view
from bd_util.maya.ui import (
    MayaIntBinding,
    MayaIntPlug,
    MayaIntPlugView,
    resolve_int_plug,
)
from bd_util.ui import (
    IntBinding,
    IntLabel,
    IntPresentation,
    IntSpinBox,
    IntViewModel,
    PythonIntAttributeStore,
    qt,
)


@dataclass
class Settings:
    """Python正本の具体型を保持する契約用データ。"""

    count: int = 128


data = Settings()
plug = resolve_int_plug("node", "count")
binding = MayaIntBinding.from_attribute(
    data, "count", maya_plug=plug, presentation=IntPresentation(minimum=0)
)
assert_type(binding, MayaIntBinding[PythonIntAttributeStore[Settings]])
assert_type(binding.store.instance, Settings)
assert_type(binding.store.read(), int)
assert_type(binding.value, int)
assert_type(binding.set_value(10), bool)
assert_type(binding.refresh(), bool)
assert_type(binding.view_model, IntViewModel)
assert_type(binding.changed, qt.QtCore.SignalInstance)
assert_type(binding.maya_view, MayaIntPlugView | None)
assert_type(IntSpinBox(binding).value(), int)
assert_type(IntLabel(binding).text(), str)
plain = IntBinding.from_attribute(data, "count")
view = MayaIntPlugView(plain.view_model, plug, qt.QObject())
assert_type(view.plug_operator, MayaIntPlug)
assert_type(view.view_model, IntViewModel)
assert_type(view.is_available, bool)
assert_type(view.is_writable, bool)
assert_type(view.is_disposed, bool)
assert_type(view.is_synchronized, bool)
assert_type(view.last_sync_error, Exception | None)
assert_type(view.sync_failed, qt.QtCore.SignalInstance)
assert_type(view.sync_from_view_model(), bool)
assert_type(view.dispose(), None)
custom = MayaIntBinding(PythonIntAttributeStore(data, "count"), maya_plug=plug)
assert_type(custom.store.instance, Settings)
sample = maya_view.show_demo(maya_view.MayaIntSampleData())
assert_type(sample, maya_view.PythonMayaIntWindow)
assert_type(sample.node_name, str)
assert_type(sample.widget.data, maya_view.MayaIntSampleData)
assert_type(
    sample.widget.long_binding.store.instance, maya_view.MayaIntSampleData
)
assert_type(sample.widget.linked_long_spin_box, IntSpinBox)
assert_type(maya_view.dispose(), None)
