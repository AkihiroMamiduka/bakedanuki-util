# coding: utf-8
import pytest

from bd_util.ui import SettingsPath


def test_settings_path_separates_tool_and_group() -> None:
    # tool名とINI内groupを含むpathを生成する。
    settings_path = SettingsPath("tool_name/widget_a/func_a/my_window")

    # 先頭segmentだけがtool名として分離されることを確認する。
    assert settings_path.tool_name == "tool_name"
    assert settings_path.group_path == "widget_a/func_a/my_window"
    assert str(settings_path) == "tool_name/widget_a/func_a/my_window"


def test_settings_path_reuses_validated_instance() -> None:
    # 検証済みSettingsPathを変換処理へ渡す。
    settings_path = SettingsPath("tool_name/my_window")

    # 不要なinstance生成をせず同じ値が返ることを確認する。
    assert SettingsPath.from_value(settings_path) is settings_path


@pytest.mark.parametrize(
    "value",
    [
        "",
        "tool_only",
        "/tool/window",
        "tool/window/",
        "tool//window",
        "tool/./window",
        "tool/../window",
        "tool\\window",
        "C:/tool/window",
        "tool/name?/window",
        "CON/window",
        "tool/window.",
        "tool/ window",
    ],
)
def test_settings_path_rejects_unsafe_values(value: str) -> None:
    # filesystem外への移動や曖昧なpathを含む値を検証する。
    with pytest.raises(ValueError):
        SettingsPath(value)


def test_settings_path_rejects_non_string_value() -> None:
    # public typeを無視して文字列以外を渡した場合も安全に拒否する。
    with pytest.raises(TypeError):
        SettingsPath(123)  # pyright: ignore[reportArgumentType]
