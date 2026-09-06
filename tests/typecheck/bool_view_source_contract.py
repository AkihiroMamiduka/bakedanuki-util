from dataclasses import dataclass
from typing import assert_type

from bd_util.maya.ui import MayaBoolBinding
from bd_util.ui import (
    BoolBinding,
    BoolCheckBox,
    BoolComboBox,
    BoolPushButton,
    BoolRadioButtonGroup,
    BoolStatusLabel,
    BoolValueStore,
    BoolViewModel,
    PythonBoolAttributeStore,
)


@dataclass
class ToolData:
    visible: bool = True


@dataclass
class OtherData:
    enabled: bool = False


class CustomStore:
    is_available = True
    is_writable = True

    def __init__(self) -> None:
        self.value = False

    def read(self) -> bool:
        return self.value

    def write(self, value: bool) -> bool:
        self.value = value
        return self.value


view_model = BoolViewModel()
binding = BoolBinding.from_attribute(ToolData(), "visible")
other_binding = BoolBinding.from_attribute(OtherData(), "enabled")
maya_binding = MayaBoolBinding.from_attribute(ToolData(), "visible")
custom_binding = BoolBinding(CustomStore())

assert_type(binding, BoolBinding[PythonBoolAttributeStore[ToolData]])
assert_type(binding.store.instance, ToolData)
assert_type(other_binding.store.instance, OtherData)
assert_type(maya_binding, MayaBoolBinding[PythonBoolAttributeStore[ToolData]])
assert_type(custom_binding.store, CustomStore)

# Storeの具体型を保った各Bindingと、生のViewModelを全Viewへ渡せる。
for source in (
    view_model,
    binding,
    other_binding,
    maya_binding,
    custom_binding,
):
    assert_type(BoolCheckBox(source), BoolCheckBox)
    assert_type(BoolComboBox(source), BoolComboBox)
    assert_type(BoolPushButton(source), BoolPushButton)
    assert_type(BoolRadioButtonGroup(source), BoolRadioButtonGroup)
    assert_type(BoolStatusLabel(source), BoolStatusLabel)
    assert_type(BoolCheckBox(source).view_model, BoolViewModel)
    assert_type(BoolComboBox(source).view_model, BoolViewModel)
    assert_type(BoolPushButton(source).view_model, BoolViewModel)
    assert_type(BoolRadioButtonGroup(source).view_model, BoolViewModel)
    assert_type(BoolStatusLabel(source).view_model, BoolViewModel)


def accept_store_boundary(source: BoolBinding[BoolValueStore]) -> None:
    assert_type(BoolCheckBox(source).view_model, BoolViewModel)


accept_store_boundary(binding)
accept_store_boundary(maya_binding)
assert_type(BoolCheckBox(view_model=view_model), BoolCheckBox)
assert_type(BoolComboBox(view_model=binding), BoolComboBox)
BoolCheckBox(object())  # pyright: ignore[reportArgumentType]
