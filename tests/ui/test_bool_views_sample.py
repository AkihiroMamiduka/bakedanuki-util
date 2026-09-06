# coding: utf-8
from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass

import pytest
from maya import cmds, standalone

from bd_util import Nodes
from bd_util._sample.maya.ui.bool_views import (
    BoolViewsWidget,
    BoolViewsWindow,
    BoolViewsWindowManager,
    VisibilityData,
)
from bd_util.maya.ui import MayaBoolPlugView
from bd_util.ui import (
    BoolCheckBox,
    BoolComboBox,
    BoolViewModel,
    PythonBoolAttributeStore,
    qt,
)


@dataclass
class SampleBoolData:
    """任意のPython objectとattribute名を渡せることを確認するdata。"""

    enabled: bool = True


@pytest.fixture(scope="session")
def maya_standalone(
    qt_application: qt.QApplication,
) -> Iterator[None]:
    """QApplication生成後にMayaを初期化し、test session終了まで維持する。"""
    # UI生成後にMayaを初期化し、既に初期化済みの環境も許容する。
    initialized_here = False
    try:
        standalone.initialize(name="python")
        initialized_here = True
    except RuntimeError:
        pass

    # Maya UI APIを後続testでも安全に使えるようsession中は維持する。
    yield

    # このfixtureが初期化した場合だけsession終了時に解放する。
    if initialized_here:
        standalone.uninitialize()


def _assert_value(
    widget: BoolViewsWidget,
    value: bool,
    maya_plug_name: str | None = None,
) -> None:
    """sample Widget内の正本、全Qt View、任意のMaya Viewを確認する。"""
    # Python正本とViewModelの公開値が一致することを確認する。
    assert getattr(widget.data, widget.store.attribute_name) is value
    assert widget.value is value

    # 入力・表示用の全Qt Viewが同じbool値を示すことを確認する。
    assert widget.check_box.isChecked() is value
    assert widget.combo_box.currentData() is value
    assert widget.push_button.isChecked() is value
    assert widget.push_button.text() == ("On" if value else "Off")
    assert widget.radio_button_group.false_button.isChecked() is not value
    assert widget.radio_button_group.true_button.isChecked() is value
    assert widget.status_label.text() == (
        "Status: On" if value else "Status: Off"
    )

    # Maya Viewを指定したtestだけscene上のplug値も確認する。
    if maya_plug_name is not None:
        assert bool(cmds.getAttr(maya_plug_name)) is value


def test_bool_views_widget_uses_arbitrary_python_attribute_without_maya(
    qt_application: qt.QApplication,
    capsys,
) -> None:
    # Maya指定なしで任意のPython attributeを正本にするWidgetを生成する。
    data = SampleBoolData()
    widget = BoolViewsWidget(data, "enabled")
    try:
        assert widget.maya_view is None
        _assert_value(widget, True)

        # 4種類の入力可能なQt Viewから順に値を変更する。
        widget.check_box.click()
        _assert_value(widget, False)

        widget.combo_box.setCurrentIndex(widget.combo_box.findData(True))
        _assert_value(widget, True)

        widget.push_button.click()
        _assert_value(widget, False)

        widget.radio_button_group.true_button.click()
        _assert_value(widget, True)

        # Python APIからの入力も同じCommandと全Viewへ反映する。
        assert widget.set_value(False)
        _assert_value(widget, False)

        # 正本を直接変更した場合は明示的なrefreshで全Viewへ反映する。
        data.enabled = True
        assert widget.refresh_from_data()
        _assert_value(widget, True)

        # 確認ボタンが任意のobject名とattribute名で正本値を出力する。
        widget.print_value_button.click()
        assert "SampleBoolData.enabled = True" in capsys.readouterr().out
    finally:
        # testで生成したWidgetのDeferredDeleteを処理する。
        widget.deleteLater()
        qt.QtCore.QCoreApplication.sendPostedEvents(
            widget,
            qt.QtCore.QEvent.Type.DeferredDelete,
        )
        qt_application.processEvents()


def test_bool_views_widget_requires_maya_names_as_pair(
    qt_application: qt.QApplication,
) -> None:
    # Maya Viewのnode名とattribute名は片方だけの指定を許可しない。
    data = SampleBoolData()

    with pytest.raises(ValueError, match="両方指定"):
        BoolViewsWidget(data, "enabled", maya_node_name="node")
    with pytest.raises(ValueError, match="両方指定"):
        BoolViewsWidget(data, "enabled", maya_attribute_name="visibility")


def test_bool_views_widget_destroys_binding_without_order_contract(
    qt_application: qt.QApplication,
) -> None:
    # ViewModelを最初の子として持つ通常のQt所有構成を生成する。
    widget = BoolViewsWidget(SampleBoolData(), "enabled")
    view_model = widget.view_model
    views = (
        widget.check_box,
        widget.combo_box,
        widget.push_button,
        widget.radio_button_group,
        widget.status_label,
    )
    assert view_model.parent() is widget

    # 子の登録順に依存せずFeature Widget全体を安全に破棄する。
    widget.deleteLater()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        widget,
        qt.QtCore.QEvent.Type.DeferredDelete,
    )
    qt_application.processEvents()

    assert not qt.isValid(widget)
    assert not qt.isValid(view_model)
    assert all(not qt.isValid(view) for view in views)


def test_bool_views_window_manager_owns_arguments_and_lifecycle(
    qt_application: qt.QApplication,
    maya_standalone: None,
) -> None:
    # module既定値とは独立したManagerとPython正本を用意する。
    manager = BoolViewsWindowManager()
    first_data = SampleBoolData()
    try:
        # 同じbinding構成のshow()では管理中Windowを再利用する。
        first_window = manager.show(first_data, "enabled")
        assert manager.window is first_window
        assert manager.show(first_data, "enabled") is first_window

        # Manager経由のPython入力もFeature Widgetへ委譲される。
        assert manager.set_value(False)
        assert first_data.enabled is False

        # 正本objectが変わった場合は新しいWindowへ作り直す。
        second_data = SampleBoolData(False)
        second_window = manager.show(second_data, "enabled")
        assert second_window is not first_window
        assert manager.window is second_window

        # 正本の直接変更もManager経由で全Viewへ再反映できる。
        second_data.enabled = True
        assert manager.refresh_from_data()
        _assert_value(second_window.bool_views_widget, True)
    finally:
        # ManagerからWindowを完全破棄して遅延削除まで処理する。
        manager.dispose()
        qt.QtCore.QCoreApplication.sendPostedEvents(
            None,
            qt.QtCore.QEvent.Type.DeferredDelete,
        )
        qt_application.processEvents()


def test_bool_views_window_mounts_self_contained_widget(
    qt_application: qt.QApplication,
    maya_standalone: None,
) -> None:
    # 動的Maya attributeを作成できる新規sceneを用意する。
    cmds.file(new=True, force=True)

    # 標準NodeOperatorに定義されていない追加bool attributeも同期する。
    node_name = cmds.createNode("transform", name="sampleViewTest")
    cmds.addAttr(node_name, longName="customVisibility", attributeType="bool")
    maya_plug_name = f"{node_name}.customVisibility"
    data = VisibilityData()
    window = BoolViewsWindow(
        data,
        "visible_by_default",
        maya_node_name=node_name,
        maya_attribute_name="customVisibility",
    )
    widget = window.bool_views_widget
    try:
        # Windowが渡された正本と任意のMaya ViewをWidgetへ集約する。
        assert widget.data is data
        assert widget.maya_view is not None
        _assert_value(widget, True, maya_plug_name)

        # 全Qt入力とPython入力が追加Maya attributeにも反映する。
        widget.check_box.click()
        _assert_value(widget, False, maya_plug_name)

        widget.combo_box.setCurrentIndex(widget.combo_box.findData(True))
        _assert_value(widget, True, maya_plug_name)

        widget.push_button.click()
        _assert_value(widget, False, maya_plug_name)

        widget.radio_button_group.true_button.click()
        _assert_value(widget, True, maya_plug_name)

        assert widget.set_value(False)
        _assert_value(widget, False, maya_plug_name)

        # Mayaからの外部入力も遅延callback後に全Viewと正本へ反映する。
        cmds.setAttr(maya_plug_name, True)
        qt_application.processEvents()
        qt_application.processEvents()
        _assert_value(widget, True, maya_plug_name)
    finally:
        # Windowとcallbackを破棄してsceneも初期状態へ戻す。
        window.deleteLater()
        qt.QtCore.QCoreApplication.sendPostedEvents(
            window,
            qt.QtCore.QEvent.Type.DeferredDelete,
        )
        qt_application.processEvents()
        cmds.file(new=True, force=True)


def test_shared_binding_survives_one_window_with_maya_view(
    qt_application: qt.QApplication,
    maya_standalone: None,
) -> None:
    # Window外のownerへStore、ViewModel、Maya Viewの寿命を集約する。
    cmds.file(new=True, force=True)
    node_name = cmds.createNode("transform", name="sharedBoolViewTest")
    node = Nodes().existing.transform(node_name)
    plug_name = f"{node_name}.visibility"
    binding_owner = qt.QObject()
    data = SampleBoolData(False)
    view_model = BoolViewModel(parent=binding_owner)
    view_model.attach_store(PythonBoolAttributeStore(data, "enabled"))
    maya_view = MayaBoolPlugView(
        view_model,
        node.visibility,
        binding_owner,
    )

    # 2つのWindowはbindingを所有せず、同じViewModelを表示する。
    first_window = qt.QWidget()
    second_window = qt.QWidget()
    first_view = BoolCheckBox(view_model, parent=first_window)
    second_view = BoolComboBox(view_model, parent=second_window)
    try:
        first_view.click()
        assert data.enabled is True
        assert second_view.currentData() is True
        assert bool(cmds.getAttr(plug_name)) is True

        # 一方のWindowを閉じても残りのViewとMaya同期を維持する。
        first_window.deleteLater()
        qt.QtCore.QCoreApplication.sendPostedEvents(
            first_window,
            qt.QtCore.QEvent.Type.DeferredDelete,
        )
        qt_application.processEvents()

        assert not qt.isValid(first_window)
        assert qt.isValid(view_model)
        assert not maya_view.is_disposed
        assert qt.isValid(second_view)

        cmds.setAttr(plug_name, False)
        qt_application.processEvents()
        qt_application.processEvents()
        assert data.enabled is False
        assert second_view.currentData() is False

        second_view.setCurrentIndex(second_view.findData(True))
        assert data.enabled is True
        assert bool(cmds.getAttr(plug_name)) is True
    finally:
        # Windowとは独立して、toolのbinding ownerを最後に破棄する。
        if qt.isValid(first_window):
            first_window.deleteLater()
        if qt.isValid(second_window):
            second_window.deleteLater()
        binding_owner.deleteLater()
        qt.QtCore.QCoreApplication.sendPostedEvents(
            None,
            qt.QtCore.QEvent.Type.DeferredDelete,
        )
        qt_application.processEvents()
        cmds.file(new=True, force=True)
