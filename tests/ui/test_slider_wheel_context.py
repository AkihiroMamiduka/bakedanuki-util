# coding: utf-8
"""Sliderのwheel入力種別を、Undoの開始・終了通知の間だけ公開する。"""

import pytest

from bd_util.ui import FloatSlider, FloatViewModel, IntSlider, IntViewModel, qt


def wheel_event():
    """実際のQt wheelイベントを一刻み分作る。"""
    return qt.QtGui.QWheelEvent(
        qt.QPointF(5, 5),
        qt.QPointF(5, 5),
        qt.QPoint(),
        qt.QPoint(0, 120),
        qt.Qt.MouseButton.NoButton,
        qt.Qt.KeyboardModifier.NoModifier,
        qt.Qt.ScrollPhase.NoScrollPhase,
        False,
    )


@pytest.mark.parametrize("integer", [False, True])
def test_wheel_context_covers_signals_and_value_request(
    qt_application, integer
):
    """開始・値要求・終了ではwheelを識別でき、ドラッグと未focusではFalseとする。"""
    owner = qt.QWidget()
    vm = (
        IntViewModel(parent=owner) if integer else FloatViewModel(parent=owner)
    )
    slider_type = IntSlider if integer else FloatSlider
    slider = slider_type(vm, owner, minimum=0, maximum=100)
    observations = []

    def handle(value):
        """既存の外部入力先を使い、値要求時の種別を記録する。"""
        observations.append(("value", slider.is_wheel_editing))
        vm.set_value_command.execute(value)
        return True

    slider.setValueRequestHandler(handle)
    slider.editStarted.connect(
        lambda: observations.append(("start", slider.is_wheel_editing))
    )
    slider.editFinished.connect(
        lambda: observations.append(("end", slider.is_wheel_editing))
    )
    try:
        qt.QApplication.sendEvent(slider, wheel_event())
        assert not observations
        assert not slider.is_wheel_editing
        owner.show()
        slider.setFocus()
        qt.QApplication.processEvents()
        assert slider.hasFocus()
        qt.QApplication.sendEvent(slider, wheel_event())
        assert observations == [
            ("start", True),
            ("value", True),
            ("end", True),
        ]
        assert not slider.is_wheel_editing
        observations.clear()
        slider.setSliderDown(True)
        slider.setSliderDown(False)
        assert observations == [("start", False), ("end", False)]
    finally:
        owner.close()
        owner.deleteLater()
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)


@pytest.mark.parametrize("integer", [False, True])
def test_wheel_context_clears_when_start_raises(
    qt_application, monkeypatch, integer
):
    """開始処理が例外になっても、次の入力へwheel種別を持ち越さない。"""
    owner = qt.QWidget()
    vm = (
        IntViewModel(parent=owner) if integer else FloatViewModel(parent=owner)
    )
    slider_type = IntSlider if integer else FloatSlider
    slider = slider_type(vm, owner, minimum=0, maximum=100)

    def fail():
        """開始通知の途中失敗を再現する。"""
        assert slider.is_wheel_editing
        raise RuntimeError("test wheel start")

    monkeypatch.setattr(slider, "_begin_edit", fail)
    try:
        owner.show()
        slider.setFocus()
        qt.QApplication.processEvents()
        with pytest.raises(RuntimeError, match="test wheel start"):
            slider.wheelEvent(wheel_event())
        assert not slider.is_wheel_editing
    finally:
        owner.close()
        owner.deleteLater()
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
