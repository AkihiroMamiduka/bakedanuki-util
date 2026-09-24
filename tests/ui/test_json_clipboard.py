# coding: utf-8
"""custom MIMEとtext fallbackを持つJSON clipboardを検証する。"""

import pytest

from bd_util.ui import JsonClipboard, qt


def test_custom_mime_and_marker_text_round_trip(saved_clipboard):
    """同じJSONを専用MIMEと可読なmarker付きtextへ保存する。"""
    adapter = JsonClipboard("application/x-bd-test+json", "BD_TEST/1\n")
    document = {"name": "値", "values": [1, True, 2.5]}
    adapter.write(document)
    mime_data = saved_clipboard.mimeData()
    assert mime_data is not None
    assert mime_data.hasFormat(adapter.mime_type)
    assert mime_data.text().startswith(adapter.text_marker)
    assert adapter.contains()
    assert adapter.read() == document


def test_marker_text_is_text_only_fallback(saved_clipboard):
    """custom MIMEが失われてもmarker付きtextだけで同じJSONを復元する。"""
    adapter = JsonClipboard("application/x-bd-test+json", "BD_TEST/1\n")
    mime_data = qt.QtCore.QMimeData()
    mime_data.setText('BD_TEST/1\n{"value":3}')
    saved_clipboard.setMimeData(mime_data)
    assert adapter.contains()
    assert adapter.read() == {"value": 3}


@pytest.mark.parametrize(
    "payload",
    [
        'BD_TEST/1\n{"value":NaN}',
        'BD_TEST/1\n{"value":1,"value":2}',
        "BD_TEST/1\n{broken",
    ],
)
def test_external_invalid_json_is_rejected(saved_clipboard, payload):
    """非標準数値、重複key、壊れたJSONを外部入力として拒否する。"""
    adapter = JsonClipboard("application/x-bd-test+json", "BD_TEST/1\n")
    saved_clipboard.setText(payload)
    with pytest.raises(ValueError):
        adapter.read()


def test_size_limit_applies_before_write_and_read(saved_clipboard):
    """過大なdocumentを保存時と外部text読込時の両方で拒否する。"""
    adapter = JsonClipboard(
        "application/x-bd-test+json", "BD_TEST/1\n", max_bytes=8
    )
    with pytest.raises(ValueError, match="8 bytes"):
        adapter.write({"value": "long"})
    mime_data = qt.QtCore.QMimeData()
    mime_data.setText('BD_TEST/1\n{"value":1}')
    saved_clipboard.setMimeData(mime_data)
    with pytest.raises(ValueError, match="8 bytes"):
        adapter.read()


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
