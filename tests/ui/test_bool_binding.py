# coding: utf-8
from __future__ import annotations

import gc
from dataclasses import dataclass
from typing import cast

import pytest

from bd_util.ui import (
    BoolCheckBox,
    BoolComboBox,
    BoolPushButton,
    BoolRadioButtonGroup,
    BoolStatusLabel,
    BoolValue,
    BoolValueStore,
    BoolViewModel,
    PythonBoolAttributeStore,
    SetBoolCommand,
    qt,
)
from bd_util.ui.binding.bool.command import (
    SetBoolCommand as ModuleSetBoolCommand,
)
from bd_util.ui.binding.bool.store import (
    BoolValueStore as ModuleBoolValueStore,
)
from bd_util.ui.binding.bool.store import (
    PythonBoolAttributeStore as ModulePythonBoolAttributeStore,
)
from bd_util.ui.binding.bool.value import BoolValue as ModuleBoolValue
from bd_util.ui.binding.bool.view.check_box import (
    BoolCheckBox as ModuleBoolCheckBox,
)
from bd_util.ui.binding.bool.view.combo_box import (
    BoolComboBox as ModuleBoolComboBox,
)
from bd_util.ui.binding.bool.view.push_button import (
    BoolPushButton as ModuleBoolPushButton,
)
from bd_util.ui.binding.bool.view.radio_button_group import (
    BoolRadioButtonGroup as ModuleBoolRadioButtonGroup,
)
from bd_util.ui.binding.bool.view.status_label import (
    BoolStatusLabel as ModuleBoolStatusLabel,
)
from bd_util.ui.binding.bool.view_model import (
    BoolViewModel as ModuleBoolViewModel,
)


class _BoolStore:
    """値の正本との同期を再現するtest Store。"""

    def __init__(
        self,
        value: bool,
        *,
        available: bool = True,
        writable: bool = True,
    ) -> None:
        """実値、利用可否、書き込み可否で初期化する。"""
        self.value = value
        self.available = available
        self.writable = writable
        self.read_count = 0
        self.writes: list[bool] = []
        self.write_error: Exception | None = None
        self.update_before_write_error = False
        self.writable_error: Exception | None = None

    @property
    def is_available(self) -> bool:
        """test用の利用可否を返す。"""
        return self.available

    @property
    def is_writable(self) -> bool:
        """test用の書き込み可否を返す。"""
        if self.writable_error is not None:
            raise self.writable_error
        return self.available and self.writable

    def read(self) -> bool:
        """読み取り回数を記録して実値を返す。"""
        self.read_count += 1
        return self.value

    def write(self, value: bool) -> bool:
        """書き込み要求を記録して確定値を返す。"""
        if self.write_error is not None:
            if self.update_before_write_error:
                self.writes.append(value)
                self.value = value
            raise self.write_error
        self.writes.append(value)
        self.value = value
        return self.value


@dataclass
class _BoolAttributeData:
    """通常dataclassのbool fieldを再現するtest data。"""

    visible: bool


@dataclass(slots=True)
class _SlottedBoolAttributeData:
    """slots付きdataclassのbool fieldを再現するtest data。"""

    visible: bool


@dataclass(frozen=True)
class _FrozenBoolAttributeData:
    """frozen dataclassのbool fieldを再現するtest data。"""

    visible: bool


@dataclass
class _NonBoolAttributeData:
    """bool以外のfieldを持つtest data。"""

    visible: int


class _PlainBoolAttributeData:
    """通常Python objectのbool attributeを再現するtest data。"""

    def __init__(self, visible: bool) -> None:
        """初期値で初期化する。"""
        self.visible = visible


class _ReadOnlyBoolAttribute:
    """setterを持たないbool property。"""

    __slots__ = ()

    @property
    def visible(self) -> bool:
        """固定のbool値を返す。"""
        return True


class _NormalizingBoolAttribute:
    """要求値と異なるboolへ確定できるproperty。"""

    __slots__ = ("_visible",)

    def __init__(self) -> None:
        """初期値で初期化する。"""
        self._visible = False

    @property
    def visible(self) -> bool:
        """確定済みのbool値を返す。"""
        return self._visible

    @visible.setter
    def visible(self, _value: bool) -> None:
        """test用に要求をFalseへ正規化する。"""
        self._visible = False


class _QObjectBoolStore(qt.QObject):
    """QObject lifecycleを持つ最小のtest Store。"""

    def __init__(self, value: bool) -> None:
        """実値を保持して初期化する。"""
        super().__init__()
        self.value = value

    @property
    def is_available(self) -> bool:
        """破棄前は読み取り可能として扱う。"""
        return True

    @property
    def is_writable(self) -> bool:
        """破棄前は書き込み可能として扱う。"""
        return True

    def read(self) -> bool:
        """現在値を返す。"""
        return self.value

    def write(self, value: bool) -> bool:
        """現在値を更新して返す。"""
        self.value = value
        return self.value


def test_role_modules_share_public_class_definitions() -> None:
    # 役割別moduleと公開APIが同じclassを指すことを保証する。
    assert ModuleBoolValue is BoolValue
    assert ModuleBoolValueStore is BoolValueStore
    assert ModulePythonBoolAttributeStore is PythonBoolAttributeStore
    assert ModuleSetBoolCommand is SetBoolCommand
    assert ModuleBoolViewModel is BoolViewModel
    assert ModuleBoolCheckBox is BoolCheckBox
    assert ModuleBoolComboBox is BoolComboBox
    assert ModuleBoolPushButton is BoolPushButton
    assert ModuleBoolRadioButtonGroup is BoolRadioButtonGroup
    assert ModuleBoolStatusLabel is BoolStatusLabel


def test_python_attribute_store_updates_dataclass_from_ui_and_python(
    qt_application: qt.QApplication,
) -> None:
    # 任意のdataclass fieldを正本としてViewModelへ接続する。
    data = _BoolAttributeData(True)
    store = PythonBoolAttributeStore(data, "visible")
    view_model = BoolViewModel()
    view_model.attach_store(store)
    checkbox = BoolCheckBox(view_model, "Visible")

    assert store.instance is data
    assert store.attribute_name == "visible"
    assert store.is_available
    assert store.is_writable
    assert view_model.value.value is True
    assert checkbox.isChecked()

    # UI入力とPython入力のどちらも同じdataclass fieldへ書き込む。
    checkbox.click()
    assert data.visible is False
    assert view_model.set_value_command.execute(True)
    assert data.visible is True
    assert checkbox.isChecked()

    checkbox.deleteLater()
    qt_application.processEvents()


def test_python_attribute_store_refreshes_direct_dataclass_change() -> None:
    # plain dataclassの直接変更は明示refreshでObservable値へ取り込む。
    data = _BoolAttributeData(True)
    store = PythonBoolAttributeStore(data, "visible")
    view_model = BoolViewModel()
    view_model.attach_store(store)

    data.visible = False
    assert view_model.refresh_from_store(store)
    assert view_model.value.value is False


def test_python_attribute_store_supports_slotted_dataclass() -> None:
    # slots descriptorを持つdataclass fieldも書き込み可能と判定する。
    data = _SlottedBoolAttributeData(True)
    store = PythonBoolAttributeStore(data, "visible")

    assert store.is_writable
    assert store.write(False) is False
    assert data.visible is False


def test_python_attribute_store_supports_plain_python_object() -> None:
    # dataclassへ限定せず、通常objectのinstance attributeも扱う。
    data = _PlainBoolAttributeData(True)
    store = PythonBoolAttributeStore(data, "visible")

    assert store.is_writable
    assert store.write(False) is False
    assert data.visible is False


def test_python_attribute_store_validates_name_and_bool_boundaries() -> None:
    # 構築時にattribute名、存在、現在値を検証する。
    data = _BoolAttributeData(True)
    with pytest.raises(ValueError, match="空でないstr"):
        PythonBoolAttributeStore(data, "")
    with pytest.raises(TypeError, match="attribute_nameにはstr"):
        PythonBoolAttributeStore(
            data,
            1,  # pyright: ignore[reportArgumentType]
        )
    with pytest.raises(AttributeError, match="missing"):
        PythonBoolAttributeStore(data, "missing")
    with pytest.raises(TypeError, match="attribute 'visible'にはbool"):
        PythonBoolAttributeStore(_NonBoolAttributeData(1), "visible")

    store = PythonBoolAttributeStore(data, "visible")
    with pytest.raises(TypeError, match="valueにはbool"):
        store.write(1)  # pyright: ignore[reportArgumentType]


def test_python_attribute_store_marks_known_read_only_values() -> None:
    # frozen dataclassとsetterなしpropertyを読み取り専用として扱う。
    stores = (
        PythonBoolAttributeStore(_FrozenBoolAttributeData(True), "visible"),
        PythonBoolAttributeStore(_ReadOnlyBoolAttribute(), "visible"),
    )

    for store in stores:
        assert store.is_available
        assert not store.is_writable
        with pytest.raises(RuntimeError, match="書き込めません"):
            store.write(False)

        view_model = BoolViewModel()
        view_model.attach_store(store)
        assert not view_model.set_value_command.can_execute
        assert not view_model.set_value_command.execute(False)


def test_python_attribute_store_returns_property_value_after_write() -> None:
    # setterが要求を変換した場合も、再読込した確定値を返す。
    data = _NormalizingBoolAttribute()
    store = PythonBoolAttributeStore(data, "visible")

    assert store.is_writable
    assert store.write(True) is False
    assert data.visible is False


def test_python_attribute_store_becomes_unavailable_after_removal() -> None:
    # 外部からattributeが削除された場合はCommandを無効化する。
    data = _BoolAttributeData(True)
    store = PythonBoolAttributeStore(data, "visible")
    view_model = BoolViewModel()
    view_model.attach_store(store)

    del data.visible
    assert not store.is_available
    assert not view_model.refresh_from_store(store)
    assert not view_model.set_value_command.can_execute
    with pytest.raises(RuntimeError, match="利用できません"):
        store.read()


def test_in_memory_command_changes_value_once() -> None:
    # nodeを持たないViewModelと変更通知の記録先を用意する。
    view_model = BoolViewModel(False)
    events: list[bool] = []
    command_events: list[bool] = []
    view_model.value.changed.connect(events.append)
    view_model.set_value_command.executed.connect(command_events.append)

    # Pythonから同じCommandを実行し、実変更だけを通知する。
    assert view_model.set_value_command.execute(True)
    assert not view_model.set_value_command.execute(True)
    assert view_model.value.value is True
    assert events == [True]
    assert command_events == [True, True]


def test_bool_binding_rejects_non_bool_values() -> None:
    # 実行時にもbool以外をデータへ混入させない。
    with pytest.raises(TypeError):
        BoolViewModel(1)  # pyright: ignore[reportArgumentType]

    view_model = BoolViewModel()
    with pytest.raises(TypeError):
        view_model.set_value_command.execute(
            1  # pyright: ignore[reportArgumentType]
        )


def test_store_is_initial_value_source_and_command_writes_through_it() -> None:
    # ViewModelと異なる実値を持つStoreを接続する。
    view_model = BoolViewModel(False)
    store = _BoolStore(True)
    view_model.attach_store(store)

    # 接続時はStoreを正本として初期同期する。
    assert view_model.store is store
    assert view_model.value.value is True
    assert view_model.set_value_command.can_execute

    # Pythonからの変更要求はStoreを経由して確定する。
    assert view_model.set_value_command.execute(False)
    assert store.writes == [False]
    assert store.value is False
    assert view_model.value.value is False


def test_store_refresh_does_not_write_value_back() -> None:
    # 接続済みStoreの外部変更を再現する。
    view_model = BoolViewModel(False)
    store = _BoolStore(False)
    view_model.attach_store(store)
    store.value = True

    # 観測結果の同期はCommand書き込みを発生させない。
    assert view_model.refresh_from_store(store)
    assert view_model.value.value is True
    assert store.writes == []


def test_store_write_failure_does_not_commit_requested_value() -> None:
    # 書き込み時に失敗するStoreを接続する。
    view_model = BoolViewModel(False)
    store = _BoolStore(False)
    store.write_error = RuntimeError("write failed")
    view_model.attach_store(store)

    # 要求値を先行してデータへ反映せず、Storeの実値を維持する。
    with pytest.raises(RuntimeError, match="write failed"):
        view_model.set_value_command.execute(True)
    assert view_model.value.value is False
    assert store.value is False


def test_store_write_failure_recovers_value_changed_before_error() -> None:
    # 値変更後に例外を返すStoreを再現する。
    view_model = BoolViewModel(False)
    store = _BoolStore(False)
    store.write_error = RuntimeError("write failed after update")
    store.update_before_write_error = True
    view_model.attach_store(store)

    # 元の例外を維持しながら、Storeの確定実値へデータを復旧する。
    with pytest.raises(RuntimeError, match="after update"):
        view_model.set_value_command.execute(True)
    assert store.value is True
    assert view_model.value.value is True
    assert view_model.set_value_command.can_execute


def test_attach_failure_does_not_partially_commit_store_value() -> None:
    # 書き込み可否の取得に失敗するStoreを用意する。
    view_model = BoolViewModel(False)
    store = _BoolStore(True)
    store.writable_error = RuntimeError("writable failed")

    # attach失敗時はStore値だけを部分反映しない。
    with pytest.raises(RuntimeError, match="writable failed"):
        view_model.attach_store(store)
    assert view_model.store is None
    assert view_model.value.value is False
    assert view_model.set_value_command.can_execute


def test_unavailable_or_read_only_store_disables_command() -> None:
    # 読み取り専用Storeを接続してCommand状態を同期する。
    view_model = BoolViewModel(False)
    store = _BoolStore(True, writable=False)
    can_execute_events: list[bool] = []
    view_model.set_value_command.can_execute_changed.connect(
        can_execute_events.append
    )
    view_model.attach_store(store)

    assert view_model.value.value is True
    assert not view_model.set_value_command.can_execute
    assert not view_model.set_value_command.execute(False)
    assert store.writes == []
    assert can_execute_events == [False]


def test_view_model_rejects_second_store() -> None:
    # 1つのViewModelへ正本を曖昧にする複数Storeを接続しない。
    view_model = BoolViewModel()
    first = _BoolStore(False)
    second = _BoolStore(True)
    view_model.attach_store(first)

    with pytest.raises(RuntimeError, match="複数のStore"):
        view_model.attach_store(second)


def test_qobject_store_destruction_disables_command(
    qt_application: qt.QApplication,
) -> None:
    # QObject Storeを接続し、外部からC++ objectを破棄する。
    view_model = BoolViewModel(False)
    store = _QObjectBoolStore(True)
    view_model.attach_store(store)
    store.deleteLater()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        store,
        qt.QtCore.QEvent.Type.DeferredDelete,
    )
    qt_application.processEvents()

    # 無効なStoreへCommandがアクセスしないよう即座に停止する。
    assert not qt.isValid(store)
    assert not view_model.set_value_command.can_execute
    assert not view_model.set_value_command.execute(False)


def test_all_bool_views_and_python_share_the_same_command(
    qt_application: qt.QApplication,
) -> None:
    # Store付きViewModelを表示・操作するすべてのViewを生成する。
    view_model = BoolViewModel(False)
    store = _BoolStore(False)
    view_model.attach_store(store)
    checkbox = BoolCheckBox(view_model, "Visibility")
    combo_box = BoolComboBox(view_model)
    push_button = BoolPushButton(view_model)
    radio_group = BoolRadioButtonGroup(view_model)
    status_label = BoolStatusLabel(
        view_model,
        false_text="Status: Off",
        true_text="Status: On",
    )

    # CheckBox入力はCommandを経由してすべてのViewとStoreを更新する。
    checkbox.click()
    assert checkbox.isChecked()
    assert combo_box.currentData() is True
    assert push_button.isChecked()
    assert push_button.text() == "On"
    assert radio_group.true_button.isChecked()
    assert not radio_group.false_button.isChecked()
    assert status_label.text() == "Status: On"
    assert view_model.value.value is True
    assert store.writes == [True]

    # ComboBox、PushButton、RadioButtonも同じCommandを共有する。
    combo_box.setCurrentIndex(combo_box.findData(False))
    assert not checkbox.isChecked()
    assert store.writes == [True, False]

    push_button.click()
    assert checkbox.isChecked()
    assert combo_box.currentData() is True
    assert store.writes == [True, False, True]

    radio_group.false_button.click()
    assert not checkbox.isChecked()
    assert not push_button.isChecked()
    assert status_label.text() == "Status: Off"
    assert store.writes == [True, False, True, False]

    # Python入力も同じCommandを通り、すべてのViewへ反映される。
    assert view_model.set_value_command.execute(True)
    assert checkbox.isChecked()
    assert combo_box.currentData() is True
    assert push_button.isChecked()
    assert radio_group.true_button.isChecked()
    assert status_label.text() == "Status: On"
    assert store.writes == [True, False, True, False, True]

    checkbox.deleteLater()
    combo_box.deleteLater()
    push_button.deleteLater()
    radio_group.deleteLater()
    status_label.deleteLater()
    qt_application.processEvents()


def test_combobox_keeps_display_text_separate_from_bool_data(
    qt_application: qt.QApplication,
) -> None:
    # 同じ表示文言でもboolの判定をitem dataへ分離したViewを生成する。
    view_model = BoolViewModel(False)
    combo_box = BoolComboBox(
        view_model,
        false_text="Visibility",
        true_text="Visibility",
    )

    assert combo_box.count() == 2
    assert combo_box.itemText(0) == "Visibility"
    assert combo_box.itemData(0) is False
    assert combo_box.itemText(1) == "Visibility"
    assert combo_box.itemData(1) is True
    assert combo_box.currentText() == "Visibility"
    assert combo_box.currentData() is False

    # 文言が同じでも選択項目のitem dataからTrueを入力する。
    combo_box.setCurrentIndex(1)
    assert view_model.value.value is True
    assert combo_box.currentText() == "Visibility"
    assert combo_box.currentData() is True

    combo_box.deleteLater()
    qt_application.processEvents()


def test_combobox_restores_actual_value_when_store_rejects_request(
    qt_application: qt.QApplication,
) -> None:
    # True要求をFalseへ正規化するStoreを接続する。
    data = _NormalizingBoolAttribute()
    view_model = BoolViewModel()
    view_model.attach_store(PythonBoolAttributeStore(data, "visible"))
    combo_box = BoolComboBox(view_model)
    true_index = combo_box.findData(True)

    # UIが先にTrueを表示してもStoreの確定実値へ戻す。
    blocker = qt.QtCore.QSignalBlocker(combo_box)
    combo_box.setCurrentIndex(true_index)
    del blocker
    combo_box._request_index(true_index)

    assert data.visible is False
    assert view_model.value.value is False
    assert combo_box.currentData() is False

    combo_box.deleteLater()
    qt_application.processEvents()


def test_combobox_restores_actual_value_when_store_write_raises(
    qt_application: qt.QApplication,
) -> None:
    # 書き込み時に失敗するStoreを接続する。
    view_model = BoolViewModel(False)
    store = _BoolStore(False)
    store.write_error = RuntimeError("write failed")
    view_model.attach_store(store)
    combo_box = BoolComboBox(view_model)
    true_index = combo_box.findData(True)

    # 先行表示したUIをStoreの実値へ復帰し、元の例外は維持する。
    blocker = qt.QtCore.QSignalBlocker(combo_box)
    combo_box.setCurrentIndex(true_index)
    del blocker
    with pytest.raises(RuntimeError, match="write failed"):
        combo_box._request_index(true_index)

    assert store.value is False
    assert view_model.value.value is False
    assert combo_box.currentData() is False

    combo_box.deleteLater()
    qt_application.processEvents()


def test_combobox_follows_command_availability(
    qt_application: qt.QApplication,
) -> None:
    # Storeの書き込み可否をComboBoxの有効状態へ反映する。
    view_model = BoolViewModel(True)
    store = _BoolStore(True)
    view_model.attach_store(store)
    combo_box = BoolComboBox(view_model)
    assert combo_box.isEnabled()

    store.writable = False
    assert not view_model.refresh_from_store(store)
    assert not combo_box.isEnabled()

    store.writable = True
    assert not view_model.refresh_from_store(store)
    assert combo_box.isEnabled()

    combo_box.deleteLater()
    qt_application.processEvents()


def test_combobox_disables_when_view_model_is_destroyed(
    qt_application: qt.QApplication,
) -> None:
    # ComboBoxとは別のownerにViewModelを持たせる。
    view_model_owner = qt.QObject()
    view_model = BoolViewModel(False, view_model_owner)
    combo_box = BoolComboBox(view_model)
    assert combo_box.isEnabled()

    # ViewModelだけを先に破棄しても、残るViewから古いQObjectを呼ばない。
    view_model_owner.deleteLater()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        view_model_owner,
        qt.QtCore.QEvent.Type.DeferredDelete,
    )
    qt_application.processEvents()
    assert not qt.isValid(view_model)
    assert not combo_box.isEnabled()
    with pytest.raises(RuntimeError, match="ViewModelは破棄"):
        _ = combo_box.view_model

    # programmaticなindex変更で破棄済みCommandへ到達しない。
    combo_box.setCurrentIndex(combo_box.findData(True))
    assert combo_box.currentData() is True

    combo_box.deleteLater()
    qt_application.processEvents()


def test_combobox_keeps_temporary_view_model_alive(
    qt_application: qt.QApplication,
) -> None:
    # factoryがViewModelを一時値として渡し、Viewだけを返す構成を再現する。
    combo_box = BoolComboBox(BoolViewModel(False))
    gc.collect()
    qt_application.processEvents()

    # Viewがbinding先を保持し、Python入力も引き続き反映できる。
    assert combo_box.isEnabled()
    view_model = combo_box.view_model
    assert view_model.set_value_command.execute(True)
    assert combo_box.currentData() is True

    combo_box.deleteLater()
    qt_application.processEvents()


def test_push_radio_and_status_views_use_distinct_representations(
    qt_application: qt.QApplication,
) -> None:
    # 同じboolを押下状態、排他選択、読み取り専用文字列で表現する。
    view_model = BoolViewModel(False)
    push_button = BoolPushButton(
        view_model,
        false_text="Disabled",
        true_text="Enabled",
    )
    radio_group = BoolRadioButtonGroup(
        view_model,
        false_text="Hidden",
        true_text="Visible",
    )
    status_label = BoolStatusLabel(
        view_model,
        false_text="Status: Hidden",
        true_text="Status: Visible",
    )

    assert push_button.isCheckable()
    assert not push_button.isChecked()
    assert push_button.text() == "Disabled"
    assert radio_group.false_button.text() == "Hidden"
    assert radio_group.false_button.isChecked()
    assert not radio_group.true_button.isChecked()
    assert status_label.text() == "Status: Hidden"

    assert view_model.set_value_command.execute(True)
    assert push_button.isChecked()
    assert push_button.text() == "Enabled"
    assert not radio_group.false_button.isChecked()
    assert radio_group.true_button.isChecked()
    assert status_label.text() == "Status: Visible"

    push_button.deleteLater()
    radio_group.deleteLater()
    status_label.deleteLater()
    qt_application.processEvents()


def test_push_and_radio_views_restore_normalized_store_value(
    qt_application: qt.QApplication,
) -> None:
    # True要求をFalseへ正規化するStoreをすべての入力Viewで共有する。
    data = _NormalizingBoolAttribute()
    view_model = BoolViewModel()
    view_model.attach_store(PythonBoolAttributeStore(data, "visible"))
    push_button = BoolPushButton(view_model)
    radio_group = BoolRadioButtonGroup(view_model)

    push_button.click()
    assert data.visible is False
    assert not push_button.isChecked()
    assert radio_group.false_button.isChecked()

    radio_group.true_button.click()
    assert data.visible is False
    assert not push_button.isChecked()
    assert radio_group.false_button.isChecked()
    assert not radio_group.true_button.isChecked()

    push_button.deleteLater()
    radio_group.deleteLater()
    qt_application.processEvents()


def test_new_input_views_follow_command_availability_but_status_stays_visible(
    qt_application: qt.QApplication,
) -> None:
    # 読み取り専用Storeでは入力Viewだけを無効にする。
    view_model = BoolViewModel(False)
    store = _BoolStore(True, writable=False)
    view_model.attach_store(store)
    push_button = BoolPushButton(view_model)
    radio_group = BoolRadioButtonGroup(view_model)
    status_label = BoolStatusLabel(view_model)

    assert not push_button.isEnabled()
    assert not radio_group.isEnabled()
    assert status_label.isEnabled()
    assert status_label.text() == "On"

    # 書き込み可能へ戻ると入力Viewを再度有効にする。
    store.writable = True
    assert not view_model.refresh_from_store(store)
    assert push_button.isEnabled()
    assert radio_group.isEnabled()
    assert status_label.isEnabled()

    push_button.deleteLater()
    radio_group.deleteLater()
    status_label.deleteLater()
    qt_application.processEvents()


def test_new_views_disable_when_view_model_is_destroyed(
    qt_application: qt.QApplication,
) -> None:
    # 3つのViewとは別のownerにViewModelを持たせる。
    view_model_owner = qt.QObject()
    view_model = BoolViewModel(False, view_model_owner)
    push_button = BoolPushButton(view_model)
    radio_group = BoolRadioButtonGroup(view_model)
    status_label = BoolStatusLabel(view_model)

    view_model_owner.deleteLater()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        view_model_owner,
        qt.QtCore.QEvent.Type.DeferredDelete,
    )
    qt_application.processEvents()

    assert not qt.isValid(view_model)
    for view in (push_button, radio_group, status_label):
        assert not view.isEnabled()
        with pytest.raises(RuntimeError, match="ViewModelは破棄"):
            _ = view.view_model

    # programmaticな状態変更でも破棄済みCommandへ到達しない。
    push_button.setChecked(True)
    radio_group.true_button.click()

    push_button.deleteLater()
    radio_group.deleteLater()
    status_label.deleteLater()
    qt_application.processEvents()


def test_new_views_keep_temporary_view_models_alive(
    qt_application: qt.QApplication,
) -> None:
    # factoryが各ViewModelを一時値として渡し、Viewだけを返す構成を再現する。
    push_button = BoolPushButton(BoolViewModel(False))
    radio_group = BoolRadioButtonGroup(BoolViewModel(False))
    status_label = BoolStatusLabel(BoolViewModel(False))
    gc.collect()
    qt_application.processEvents()

    # 各Viewがbinding先を保持し、Python入力も引き続き反映できる。
    assert push_button.view_model.set_value_command.execute(True)
    assert push_button.isChecked()
    assert radio_group.view_model.set_value_command.execute(True)
    assert radio_group.true_button.isChecked()
    assert status_label.view_model.set_value_command.execute(True)
    assert status_label.text() == "On"

    push_button.deleteLater()
    radio_group.deleteLater()
    status_label.deleteLater()
    qt_application.processEvents()


def test_external_refresh_updates_views_without_command_feedback(
    qt_application: qt.QApplication,
) -> None:
    # 1つのViewModelを表示する複数のViewを用意する。
    view_model = BoolViewModel(False)
    store = _BoolStore(False)
    view_model.attach_store(store)
    first = BoolCheckBox(view_model, "First")
    second = BoolCheckBox(view_model, "Second")
    combo_box = BoolComboBox(view_model)
    push_button = BoolPushButton(view_model)
    radio_group = BoolRadioButtonGroup(view_model)
    status_label = BoolStatusLabel(view_model)
    toggled_events: list[bool] = []
    index_events: list[int] = []
    push_events: list[bool] = []
    radio_events: list[bool] = []
    first.toggled.connect(toggled_events.append)
    second.toggled.connect(toggled_events.append)
    combo_box.currentIndexChanged.connect(index_events.append)
    push_button.toggled.connect(push_events.append)
    radio_group.false_button.toggled.connect(radio_events.append)
    radio_group.true_button.toggled.connect(radio_events.append)

    # Maya callback相当の同期ではViewのsignalとStore書き込みを発生させない。
    store.value = True
    assert view_model.refresh_from_store(cast(BoolValueStore, store))
    assert first.isChecked()
    assert second.isChecked()
    assert combo_box.currentData() is True
    assert push_button.isChecked()
    assert radio_group.true_button.isChecked()
    assert status_label.text() == "On"
    assert toggled_events == []
    assert index_events == []
    assert push_events == []
    assert radio_events == []
    assert store.writes == []

    first.deleteLater()
    second.deleteLater()
    combo_box.deleteLater()
    push_button.deleteLater()
    radio_group.deleteLater()
    status_label.deleteLater()
    qt_application.processEvents()


def test_checkbox_follows_command_availability(
    qt_application: qt.QApplication,
) -> None:
    # Storeの書き込み可否を表示へ反映するViewを生成する。
    view_model = BoolViewModel(True)
    store = _BoolStore(True)
    view_model.attach_store(store)
    checkbox = BoolCheckBox(view_model, "Visibility")
    assert checkbox.isEnabled()

    # Storeが読み取り専用になった場合は無効化する。
    store.writable = False
    assert not view_model.refresh_from_store(store)
    assert not checkbox.isEnabled()

    checkbox.deleteLater()
    qt_application.processEvents()


def test_checkbox_disables_when_view_model_is_destroyed(
    qt_application: qt.QApplication,
) -> None:
    # checkboxとは別のownerにViewModelを持たせる。
    view_model_owner = qt.QObject()
    view_model = BoolViewModel(False, view_model_owner)
    checkbox = BoolCheckBox(view_model, "Visibility")
    assert checkbox.isEnabled()

    # ViewModelだけを先に破棄しても、残るViewから古いQObjectを呼ばない。
    view_model_owner.deleteLater()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        view_model_owner,
        qt.QtCore.QEvent.Type.DeferredDelete,
    )
    qt_application.processEvents()
    assert not qt.isValid(view_model)
    assert not checkbox.isEnabled()
    with pytest.raises(RuntimeError, match="ViewModelは破棄"):
        _ = checkbox.view_model

    # clickとprogrammatic更新のどちらも破棄済みCommandへ到達しない。
    checkbox.click()
    checkbox.setChecked(True)
    assert checkbox.isChecked()

    checkbox.deleteLater()
    qt_application.processEvents()


def test_checkbox_keeps_temporary_view_model_alive(
    qt_application: qt.QApplication,
) -> None:
    # factoryがViewModelを一時値として渡し、Viewだけを返す構成を再現する。
    checkbox = BoolCheckBox(BoolViewModel(False), "Visibility")
    gc.collect()
    qt_application.processEvents()

    # Viewがbinding先を保持し、Python入力も引き続き反映できる。
    assert checkbox.isEnabled()
    view_model = checkbox.view_model
    assert view_model.set_value_command.execute(True)
    assert checkbox.isChecked()

    checkbox.deleteLater()
    qt_application.processEvents()
