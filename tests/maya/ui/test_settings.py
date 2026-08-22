# coding: utf-8
from pathlib import Path

from bd_util.maya.ui import get_ui_settings_root


def test_ui_settings_root_uses_maya_user_preferences(maya_cmds) -> None:
    # Mayaが返すversion別user preferences directoryを取得する。
    user_pref_dir = Path(maya_cmds.internalVar(userPrefDir=True))

    # bakedanukiのtool settings rootが配下に構成されることを確認する。
    assert get_ui_settings_root() == user_pref_dir / "bakedanuki" / "tools"
