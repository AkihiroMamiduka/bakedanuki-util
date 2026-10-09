# coding: utf-8
"""現在の Maya から共通 bakedanuki Module の登録を解除する。"""

from __future__ import annotations

import os
import re
import tempfile
from pathlib import Path
from typing import Protocol

ENV_NAME = "MAYA_MODULE_PATH"


class _MayaCmds(Protocol):
    def about(self, *, version: bool = ...) -> str: ...

    def internalVar(self, *, userAppDir: bool = ...) -> str: ...

    def confirmDialog(
        self,
        *,
        title: str,
        message: str,
        button: str | list[str],
        defaultButton: str,
        cancelButton: str = ...,
        dismissString: str = ...,
        icon: str = ...,
    ) -> str: ...


def _norm_path(path: str) -> str:
    path = path.strip().strip('"').strip("'")
    path = os.path.expandvars(os.path.expanduser(path))
    path = os.path.normpath(path.replace("/", "\\"))
    return os.path.normcase(path.rstrip("\\/"))


def _is_same_path(a: str, b: str) -> bool:
    return _norm_path(a) == _norm_path(b)


def _find_env_line(lines: list[str]) -> int | None:
    pattern = re.compile(rf"^\s*{ENV_NAME}\s*=", re.IGNORECASE)
    found: int | None = None
    for index, line in enumerate(lines):
        if line.lstrip().startswith("#"):
            continue
        if pattern.match(line):
            if found is not None:
                raise ValueError(f"{ENV_NAME} が複数行に定義されています")
            found = index
    return found


def _line_ending(line: str) -> str:
    if line.endswith("\r\n"):
        return "\r\n"
    if line.endswith("\n"):
        return "\n"
    if line.endswith("\r"):
        return "\r"
    return ""


def _build_env_text(text: str, target_path: str) -> tuple[str, list[str]]:
    lines = text.splitlines(keepends=True)
    line_index = _find_env_line(lines)
    if line_index is None:
        return text, []

    line = lines[line_index]
    ending = _line_ending(line)
    content = line[: -len(ending)] if ending else line
    key, value = content.split("=", 1)
    paths = [part.strip() for part in value.split(";") if part.strip()]
    removed = [path for path in paths if _is_same_path(path, target_path)]
    if not removed:
        return text, []

    # 実行元のModule pathだけを取り除き、他の登録を残す
    remaining = [
        path for path in paths if not _is_same_path(path, target_path)
    ]
    if remaining:
        lines[line_index] = f"{key}={';'.join(remaining)};{ending}"
    else:
        lines.pop(line_index)
    return "".join(lines), removed


def _read_text(path: Path) -> tuple[str, str, bytes | None]:
    if not path.exists():
        return "", "utf-8", None

    data = path.read_bytes()
    encodings = (
        ("utf-8-sig",)
        if data.startswith(b"\xef\xbb\xbf")
        else ("utf-8", "mbcs")
    )
    for encoding in encodings:
        try:
            return data.decode(encoding), encoding, data
        except UnicodeDecodeError:
            continue
    raise UnicodeError(f"Maya.env の文字コードを判定できません: {path}")


def _write_text(
    path: Path, text: str, encoding: str, original_data: bytes | None
) -> Path | None:
    if (path.read_bytes() if path.exists() else None) != original_data:
        raise RuntimeError(f"確認後に Maya.env が変更されました: {path}")

    temp_path: Path | None = None
    backup_path: Path | None = None
    try:
        # 元の内容を退避し、同じディレクトリの一時ファイルを完成させる
        if original_data is not None:
            with tempfile.NamedTemporaryFile(
                mode="wb",
                dir=path.parent,
                prefix=f"{path.name}.bakedanuki-",
                suffix=".bak",
                delete=False,
            ) as backup:
                backup_path = Path(backup.name)
                backup.write(original_data)
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding=encoding,
            newline="",
            dir=path.parent,
            prefix=f".{path.name}-",
            suffix=".tmp",
            delete=False,
        ) as file:
            temp_path = Path(file.name)
            file.write(text)
        if (path.read_bytes() if path.exists() else None) != original_data:
            raise RuntimeError(f"保存中に Maya.env が変更されました: {path}")
        os.replace(temp_path, path)
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)
    return backup_path


def _uninstaller_dir() -> Path:
    try:
        return Path(__file__).resolve().parent
    except NameError as exc:
        raise RuntimeError(
            "uninstaller.py のパスを取得できませんでした。"
        ) from exc


def _target_modules_dir() -> Path:
    return _uninstaller_dir() / "modules"


def _maya_version(cmds: _MayaCmds) -> str:
    version_text = str(cmds.about(version=True))
    match = re.search(r"\d{4}", version_text)
    return match.group(0) if match else version_text


def _maya_env_path(cmds: _MayaCmds) -> Path:
    custom_dir = os.environ.get("MAYA_ENV_DIR")
    if custom_dir:
        return (
            Path(os.path.expandvars(os.path.expanduser(custom_dir)))
            / "Maya.env"
        )

    user_app_dir = Path(cmds.internalVar(userAppDir=True))
    version_path = user_app_dir / _maya_version(cmds) / "Maya.env"
    fallback_path = user_app_dir / "Maya.env"
    if not version_path.exists() and fallback_path.exists():
        return fallback_path
    return version_path


def _confirm(cmds: _MayaCmds, message: str) -> bool:
    return (
        cmds.confirmDialog(
            title="bakedanuki uninstaller",
            message=message,
            button=["OK", "Cancel"],
            defaultButton="Cancel",
            cancelButton="Cancel",
            dismissString="Cancel",
            icon="question",
        )
        == "OK"
    )


def _message(cmds: _MayaCmds, message: str, icon: str = "information") -> None:
    cmds.confirmDialog(
        title="bakedanuki uninstaller",
        message=message,
        button=["OK"],
        defaultButton="OK",
        icon=icon,
    )


def uninstall() -> None:
    """現在のMayaの環境設定から、この配布物のModule pathだけを解除する。"""
    from maya import cmds

    target_path = _target_modules_dir().as_posix()
    env_path = _maya_env_path(cmds)
    text, encoding, original_data = _read_text(env_path)
    new_text, removed = _build_env_text(text, target_path)
    if not removed:
        _message(
            cmds,
            "この Maya の Maya.env に解除対象はありません。\n\n"
            f"Maya {_maya_version(cmds)}\n"
            f"Maya.env:\n{env_path}\n\n"
            f"探したパス:\n{target_path}\n\n"
            "別の起動バッチや環境変数から登録した場合は、"
            "その設定を確認してください。",
        )
        return

    removed_text = "\n".join(removed)
    if not _confirm(
        cmds,
        f"Maya {_maya_version(cmds)} から bakedanuki 一式を解除しますか？\n\n"
        f"Maya.env:\n{env_path}\n\n"
        f"解除するパス:\n{removed_text}\n\n"
        "同梱された util・tools などが次回起動から読み込まれなくなります。\n"
        "配布ファイル、シーン、個人設定は削除しません。",
    ):
        return

    backup_path = _write_text(env_path, new_text, encoding, original_data)
    backup_message = f"\n\nバックアップ:\n{backup_path}" if backup_path else ""
    _message(
        cmds,
        "Maya.env から bakedanuki の登録を解除しました。\n"
        "変更を反映するには Maya を再起動してください。\n\n"
        f"Maya.env:\n{env_path}{backup_message}",
    )


def main() -> None:
    """解除処理の失敗をMayaのダイアログへ表示する。"""
    try:
        uninstall()
    except Exception as exc:
        from maya import cmds

        _message(
            cmds,
            f"アンインストール中にエラーが発生しました。\n\n{exc}",
            icon="critical",
        )


def _cleanup_bytecode_cache() -> None:
    """Mayaが生成したこのスクリプト自身のcacheだけを削除する。"""
    try:
        script_path = Path(__file__).resolve()
    except (NameError, OSError):
        return
    cache_dir = script_path.parent / "__pycache__"
    if not cache_dir.is_dir() or cache_dir.is_symlink():
        return
    try:
        cache_files = list(cache_dir.glob(f"{script_path.stem}.*.pyc"))
    except OSError:
        return
    for cache_file in cache_files:
        try:
            cache_file.unlink()
        except OSError:
            pass
    try:
        cache_dir.rmdir()
    except OSError:
        pass


def _run() -> None:
    """解除後にドラッグ＆ドロップのcacheを片付ける。"""
    try:
        main()
    finally:
        _cleanup_bytecode_cache()


def onMayaDroppedPythonFile(*_args: object) -> None:
    """Mayaのビューポートへドロップしたときに解除する。"""
    _run()


if __name__ == "__main__":
    _run()
