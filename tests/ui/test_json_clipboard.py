# coding: utf-8
"""custom MIMEとtext fallbackを持つJSON clipboardを検証する。"""

import pytest

from bd_util.ui import JsonClipboard, qt


def _saved_clipboard() -> qt.QtCore.QMimeData:
    """現在のclipboard内容をtest後に戻せるQMimeDataへ複製する。"""
    saved = qt.QtCore.QMimeData()
    original = qt.QApplication.clipboard().mimeData()
    if original is not None:
        for mime_type in original.formats():
            saved.setData(mime_type, original.data(mime_type))
    return saved


def test_custom_mime_and_marker_text_round_trip(qt_application):
    """同じJSONを専用MIMEと可読なmarker付きtextへ保存する。"""
    clipboard = qt_application.clipboard()
    saved = _saved_clipboard()
    adapter = JsonClipboard("application/x-bd-test+json", "BD_TEST/1\n")
    document = {"name": "値", "values": [1, True, 2.5]}
    try:
        adapter.write(document)
        mime_data = clipboard.mimeData()
        assert mime_data is not None
        assert mime_data.hasFormat(adapter.mime_type)
        assert mime_data.text().startswith(adapter.text_marker)
        assert adapter.contains()
        assert adapter.read() == document
    finally:
        clipboard.setMimeData(saved)


def test_marker_text_is_cross_process_fallback(qt_application):
    """custom MIMEが失われてもmarker付きtextだけで同じJSONを復元する。"""
    clipboard = qt_application.clipboard()
    saved = _saved_clipboard()
    adapter = JsonClipboard("application/x-bd-test+json", "BD_TEST/1\n")
    try:
        mime_data = qt.QtCore.QMimeData()
        mime_data.setText('BD_TEST/1\n{"value":3}')
        clipboard.setMimeData(mime_data)
        assert adapter.contains()
        assert adapter.read() == {"value": 3}
    finally:
        clipboard.setMimeData(saved)


@pytest.mark.parametrize(
    "payload",
    [
        'BD_TEST/1\n{"value":NaN}',
        'BD_TEST/1\n{"value":1,"value":2}',
        "BD_TEST/1\n{broken",
    ],
)
def test_external_invalid_json_is_rejected(qt_application, payload):
    """非標準数値、重複key、壊れたJSONを外部入力として拒否する。"""
    clipboard = qt_application.clipboard()
    saved = _saved_clipboard()
    adapter = JsonClipboard("application/x-bd-test+json", "BD_TEST/1\n")
    try:
        clipboard.setText(payload)
        with pytest.raises(ValueError):
            adapter.read()
    finally:
        clipboard.setMimeData(saved)


def test_size_limit_applies_before_write_and_read(qt_application):
    """過大なdocumentを保存時と外部text読込時の両方で拒否する。"""
    clipboard = qt_application.clipboard()
    saved = _saved_clipboard()
    adapter = JsonClipboard(
        "application/x-bd-test+json", "BD_TEST/1\n", max_bytes=8
    )
    try:
        with pytest.raises(ValueError, match="8 bytes"):
            adapter.write({"value": "long"})
        mime_data = qt.QtCore.QMimeData()
        mime_data.setText('BD_TEST/1\n{"value":1}')
        clipboard.setMimeData(mime_data)
        with pytest.raises(ValueError, match="8 bytes"):
            adapter.read()
    finally:
        clipboard.setMimeData(saved)


@pytest.mark.parametrize(
    ("arguments", "error_type"),
    [
        (("text/plain", "BD/1\n"), ValueError),
        (("application/x-test", "BD/1"), ValueError),
        (("application/x-test", "BD/1\n", True), TypeError),
    ],
)
def test_configuration_is_strict(arguments, error_type):
    """他形式を誤認する識別子と曖昧な容量指定を構築時に拒否する。"""
    with pytest.raises(error_type):
        JsonClipboard(*arguments)
