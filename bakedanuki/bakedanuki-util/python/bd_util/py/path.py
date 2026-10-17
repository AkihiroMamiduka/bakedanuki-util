"""同梱リソースの配置を基準にしたパス解決。"""

from pathlib import Path

__all__ = ["resolve_relative_path"]


def resolve_relative_path(base_file: str | Path, relative_path: str) -> Path:
    """基準ファイルのあるフォルダから相対パスを絶対パスへ解決する。

    対象の存在確認、読み込みやファイル作成は行わない。

    Args:
        base_file: 呼び出し元の `__file__`、または基準ファイルのパス。
            相対パスの場合は呼び出し時の作業フォルダから解決する。
        relative_path: 基準ファイルのフォルダからの相対パス。
            `sub/file.png` のようなサブフォルダを含む指定も受け付ける。

    Returns:
        基準ファイルの配置から組み立てた対象の絶対パス。
    """
    return Path(base_file).resolve().parent / relative_path
