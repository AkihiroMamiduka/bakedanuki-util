# coding: utf-8
from dataclasses import dataclass
from enum import Enum


class DockArea(str, Enum):
    """Maya main window上のドッキング領域を表す。"""

    TOP = "top"
    LEFT = "left"
    RIGHT = "right"
    BOTTOM = "bottom"
    ALL = "all"


@dataclass(frozen=True)
class DockOptions:
    """ドッキングウィンドウの初期表示設定を保持する。"""

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
        # allは許可領域専用のため、初期ドッキング位置としては拒否する。
        if self.area is DockArea.ALL:
            raise ValueError("areaにはDockArea.ALLを指定できません")

        # 初期位置が単一の許可領域から外れる矛盾した設定を拒否する。
        if (
            self.allowed_area is not DockArea.ALL
            and self.area is not self.allowed_area
        ):
            raise ValueError(
                "areaはallowed_areaに含まれる領域を指定してください"
            )

        # サイズ指定はMayaへ渡す前に正の整数へ限定する。
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
        """MayaQWidgetDockableMixinへ渡す引数を生成する。"""
        # MayaのMixinが受け取るcamelCaseの引数名へ変換する。
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
