# coding: utf-8
from __future__ import annotations

import os
import re
from pathlib import Path


ENV_NAME = "MAYA_MODULE_PATH"
PATH_SEPARATOR = ";"
BAKEDANUKI_FOLDER_NAME = "bakedanuki"


def _norm_path(path: str) -> str:
    path = path.strip().strip('"').strip("'")
    path = os.path.expandvars(os.path.expanduser(path))
    path = path.replace("/", "\\")
    path = os.path.normpath(path)
    return os.path.normcase(path.rstrip("\\/"))


def _is_same_path(a: str, b: str) -> bool:
    return _norm_path(a) == _norm_path(b)


def _has_bakedanuki_folder(path: str) -> bool:
    normalized = _norm_path(path)
    parts = [part.lower() for part in re.split(r"[\\/]+", normalized)]
    return BAKEDANUKI_FOLDER_NAME in parts


def _split_paths(value: str) -> list[str]:
    return [part.strip() for part in value.split(PATH_SEPARATOR) if part.strip()]


def _join_paths(paths: list[str]) -> str:
    if not paths:
        return ""
    return PATH_SEPARATOR.join(paths) + PATH_SEPARATOR


def _find_env_line(lines: list[str]) -> int | None:
    pattern = re.compile(rf"^\s*{re.escape(ENV_NAME)}\s*=", re.IGNORECASE)
    for index, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped.startswith("#"):
            continue
        if pattern.match(line):
            return index
    return None


def _split_env_line(line: str) -> tuple[str, str]:
    key, value = line.split("=", 1)
    return key.strip(), value.strip()


def _build_module_paths(current_paths: list[str], target_path: str) -> tuple[list[str], bool, list[str]]:
    new_paths: list[str] = []
    inserted_target = False
    removed_bakedanuki_paths: list[str] = []

    for path in current_paths:
        if _is_same_path(path, target_path):
            if not inserted_target:
                new_paths.append(path)
                inserted_target = True
            continue

        if _has_bakedanuki_folder(path):
            removed_bakedanuki_paths.append(path)
            if not inserted_target:
                new_paths.append(target_path)
                inserted_target = True
            continue

        new_paths.append(path)

    if not inserted_target:
        new_paths.append(target_path)

    changed = new_paths != current_paths
    return new_paths, changed, removed_bakedanuki_paths


def _detect_newline(text: str) -> str:
    if "\r\n" in text:
        return "\r\n"
    if "\n" in text:
        return "\n"
    return os.linesep


def _line_ending(line: str) -> str:
    if line.endswith("\r\n"):
        return "\r\n"
    if line.endswith("\n"):
        return "\n"
    if line.endswith("\r"):
        return "\r"
    return ""


def _strip_trailing_blank_lines(lines: list[str]) -> list[str]:
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def _read_text(path: Path) -> tuple[str, str]:
    if not path.exists():
        return "", "utf-8"

    data = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "mbcs"):
        try:
            return data.decode(encoding), encoding
        except UnicodeDecodeError:
            continue

    return data.decode("utf-8", errors="replace"), "utf-8"


def _write_text(path: Path, text: str, encoding: str) -> None:
    if encoding == "utf-8-sig":
        encoding = "utf-8"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding=encoding, newline="") as file:
        file.write(text)


def _build_env_text(text: str, target_path: str) -> tuple[str, str, list[str]]:
    newline = _detect_newline(text)
    lines = text.splitlines(keepends=True)
    line_index = _find_env_line(lines)

    if line_index is None:
        current_paths: list[str] = []
    else:
        _, value = _split_env_line(lines[line_index])
        current_paths = _split_paths(value)

    new_paths, changed, removed_bakedanuki_paths = _build_module_paths(
        current_paths,
        target_path,
    )

    if not changed:
        return text, "already_registered", removed_bakedanuki_paths

    new_line = f"{ENV_NAME}={_join_paths(new_paths)}"

    if line_index is None:
        content_lines = _strip_trailing_blank_lines(text.splitlines())
        if not content_lines:
            new_text = new_line + newline
        else:
            new_text = newline.join(content_lines) + newline + new_line + newline
    else:
        if all(not line.strip() for line in lines[line_index + 1 :]):
            lines = lines[:line_index] + [new_line]
        else:
            lines[line_index] = new_line + (_line_ending(lines[line_index]) or newline)
        new_text = "".join(lines)

    action = "replace" if removed_bakedanuki_paths else "add"
    return new_text, action, removed_bakedanuki_paths


def _installer_dir() -> Path:
    try:
        return Path(__file__).resolve().parent
    except NameError as exc:
        raise RuntimeError("installer.py のパスを取得できませんでした。") from exc


def _cleanup_bytecode_cache(installer_path: Path | None = None) -> None:
    if installer_path is None:
        try:
            installer_path = Path(__file__).resolve()
        except (NameError, OSError):
            return

    cache_dir = installer_path.parent / "__pycache__"
    if not cache_dir.is_dir() or cache_dir.is_symlink():
        return

    try:
        cache_files = list(cache_dir.glob(f"{installer_path.stem}.*.pyc"))
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


def _target_modules_dir() -> Path:
    return _installer_dir() / "modules"


def _maya_version(cmds) -> str:
    version_text = str(cmds.about(version=True))
    match = re.search(r"\d{4}", version_text)
    if match:
        return match.group(0)
    return version_text


def _maya_env_path(cmds) -> Path:
    user_app_dir = Path(cmds.internalVar(userAppDir=True))
    return user_app_dir / _maya_version(cmds) / "Maya.env"


def _confirm(cmds, title: str, message: str, icon: str = "question") -> bool:
    result = cmds.confirmDialog(
        title=title,
        message=message,
        button=["OK", "Cancel"],
        defaultButton="OK",
        cancelButton="Cancel",
        dismissString="Cancel",
        icon=icon,
    )
    return result == "OK"


def _message(cmds, title: str, message: str, icon: str = "information") -> None:
    cmds.confirmDialog(
        title=title,
        message=message,
        button=["OK"],
        defaultButton="OK",
        icon=icon,
    )


def install() -> None:
    from maya import cmds

    target_path = _target_modules_dir().as_posix()
    env_path = _maya_env_path(cmds)
    text, encoding = _read_text(env_path)
    new_text, action, removed_paths = _build_env_text(text, target_path)

    if action == "already_registered":
        _message(
            cmds,
            "bakedanuki installer",
            "この Maya の Maya.env には、既に bakedanuki modules が登録されています。\n\n"
            f"Maya.env:\n{env_path}\n\n"
            f"登録済みのパス:\n{target_path}",
        )
        return

    if action == "replace":
        removed = "\n".join(removed_paths)
        message = (
            "既に bakedanuki パスが登録されています。置き換えますか？\n\n"
            f"Maya.env:\n{env_path}\n\n"
            f"置き換え前:\n{removed}\n\n"
            f"置き換え後:\n{target_path}"
        )
    else:
        message = (
            "この Maya の Maya.env に bakedanuki modules を追加してよいですか？\n\n"
            f"Maya.env:\n{env_path}\n\n"
            f"追加するパス:\n{target_path}"
        )

    if not _confirm(cmds, "bakedanuki installer", message):
        return

    _write_text(env_path, new_text, encoding)
    _message(
        cmds,
        "bakedanuki installer",
        "Maya.env を更新しました。\n"
        "変更を反映するには Maya を再起動してください。\n\n"
        f"Maya.env:\n{env_path}",
    )


def main() -> None:
    try:
        install()
    except Exception as exc:
        try:
            from maya import cmds

            _message(
                cmds,
                "bakedanuki installer",
                f"インストール中にエラーが発生しました。\n\n{exc}",
                icon="critical",
            )
        except Exception:
            raise


def _run() -> None:
    try:
        main()
    finally:
        _cleanup_bytecode_cache()


def onMayaDroppedPythonFile(*_args) -> None:
    _run()


if __name__ == "__main__":
    _run()
