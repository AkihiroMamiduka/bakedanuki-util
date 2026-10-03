"""共有Mayaメニューの公開型を確認する。"""

from typing import assert_type

from bd_util.maya.ui import (
    is_menu_auto_install_enabled,
    register_menu_item,
    set_menu_auto_install_enabled,
    unregister_menu_owner,
)

assert_type(is_menu_auto_install_enabled(), bool)
assert_type(set_menu_auto_install_enabled(False), None)

assert_type(
    register_menu_item(
        owner="bd_tools",
        category="tools",
        item_id="bdChannelBox",
        label="bdChannelBox",
        command=lambda: None,
    ),
    bool,
)
assert_type(unregister_menu_owner("bd_tools"), None)
