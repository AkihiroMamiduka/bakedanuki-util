"""同梱リソースの配置を基準にしたパス解決。"""

from pathlib import Path

__all__ = ["icon_path"]


def icon_path(module_file: str | Path, file_name: str) -> Path:
    """基準ファイルと同じフォルダにあるアイコンの絶対パスを返す。

    画像の存在確認や読み込みは行わない。メニューでの画像検証は、
    `register_menu_item()` が担当する。

    Args:
        module_file: 呼び出し元の `__file__`、または基準ファイルのパス。
        file_name: 基準ファイルと同じフォルダからの相対画像パス。

    Returns:
        基準ファイルの配置から解決した画像の絶対パス。
    """
    return Path(module_file).resolve().parent / file_name
