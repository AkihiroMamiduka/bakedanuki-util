# coding: utf-8
from dataclasses import dataclass
from enum import Enum


class DockArea(str, Enum):
    """Maya main window上のドッキング領域。`ALL`は許可領域専用。"""

    TOP = "top"
    LEFT = "left"
    RIGHT = "right"
    BOTTOM = "bottom"
    ALL = "all"


@dataclass(frozen=True)
class DockOptions:
    """dockable Windowの初期配置とclose時の保持方針。

    Attributes:
        area: 初回表示する領域。`DockArea.ALL`は指定できない。
        allowed_area: 移動を許可する領域。既定は全領域。
        floating: 初回から独立したWindowとして表示するか。
        initial_width: 初回の幅。`None`ならWidget側に任せる。
        initial_height: 初回の高さ。`None`ならWidget側に任せる。
        minimum_width: 最小幅。`None`なら指定しない。
        retain: close後もworkspaceControlとWidgetを保持するか。
        tab_to_control: 初回にタブ化する既存workspaceControl名。

    Raises:
        ValueError: 領域の組み合わせ、サイズ、タブ先の指定が不正な場合。
    """

    area: DockArea = DockArea.RIGHT
    allowed_area: DockArea = DockArea.ALL
    floating: bool = False
    initial_width: int | None = None
    initial_height: int | None = None
    minimum_width: int | None = None
    retain: bool = False
    tab_to_control: str | None = None

    def __post_init__(self) -> None:
        """設定値がMayaで利用できる範囲か検証する。"""
        # 初期位置は単一領域であり、許可領域の指定とも矛盾できない。
        if self.area is DockArea.ALL:
            raise ValueError("areaにはDockArea.ALLを指定できません")

        if (
            self.allowed_area is not DockArea.ALL
            and self.area is not self.allowed_area
        ):
            raise ValueError(
                "areaはallowed_areaに含まれる領域を指定してください"
            )

        # Mayaへ渡すサイズは正の値に限定する。
        for name, value in (
            ("initial_width", self.initial_width),
            ("initial_height", self.initial_height),
            ("minimum_width", self.minimum_width),
        ):
            if value is not None and value <= 0:
                raise ValueError(f"{name}には1以上の整数を指定してください")

        # 空文字のcontrol名はMaya側で解決できないため拒否する。
        if self.tab_to_control is not None and not self.tab_to_control.strip():
            raise ValueError(
                "tab_to_controlには空でない名前を指定してください"
            )

    def to_mixin_arguments(self, ui_script: str) -> dict[str, object]:
        """設定をMayaQWidgetDockableMixinの引数へ変換する。

        Args:
            ui_script: Maya再起動時に呼ばれる復元用スクリプト。

        Returns:
            Mixinの`show()`へ渡すキーワード引数。
        """
        # この境界でMixinが要求するcamelCaseのキーへ変換する。
        arguments: dict[str, object] = {
            "floating": self.floating,
            "area": self.area.value,
            "allowedArea": self.allowed_area.value,
            "retain": self.retain,
            "uiScript": ui_script,
        }

        # 未指定のサイズはWidgetのsize hintへ委ねる。
        if self.initial_width is not None:
            arguments["width"] = self.initial_width
        if self.initial_height is not None:
            arguments["height"] = self.initial_height
        if self.minimum_width is not None:
            arguments["minWidth"] = self.minimum_width

        return arguments
