"""共有Mayaメニューの公開型を確認する。"""

from typing import assert_type

from bd_util.maya.ui import register_menu_item, unregister_menu_owner

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
