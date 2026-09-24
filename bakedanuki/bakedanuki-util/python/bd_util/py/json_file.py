"""UTF-8のJSONファイル入出力。データ固有のschema検証は呼び出し側で行う。"""

from __future__ import annotations

import json
import math
import os
import tempfile
from pathlib import Path
from typing import NoReturn, cast

__all__ = ["read", "write"]


def _validate(value: object, ancestors: set[int]) -> None:
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("JSON numbers must be finite.")
        return
    if not isinstance(value, (dict, list, tuple)):
        raise TypeError(f"Unsupported JSON value: {type(value).__name__}.")
    container = cast(
        dict[object, object] | list[object] | tuple[object, ...], value
    )
    identity = id(container)
    if identity in ancestors:
        raise ValueError("Circular reference in JSON data.")
    ancestors.add(identity)
    try:
        if isinstance(container, dict):
            for key, item in container.items():
                if not isinstance(key, str):
                    raise TypeError("JSON object keys must be strings.")
                _validate(item, ancestors)
        else:
            for item in container:
                _validate(item, ancestors)
    finally:
        ancestors.remove(identity)


def _finite_float(text: str) -> float:
    value = float(text)
    if not math.isfinite(value):
        raise ValueError("JSON numbers must be finite.")
    return value


def _reject_constant(text: str) -> NoReturn:
    raise ValueError(f"Invalid JSON number: {text}.")


def read(path: str | os.PathLike[str]) -> object:
    """UTF-8 JSONを即時に読む。BOMを許容し、非有限数とI/Oの失敗は例外にする。"""
    with Path(path).open("r", encoding="utf-8-sig") as stream:
        return cast(
            object,
            json.load(
                stream,
                parse_float=_finite_float,
                parse_constant=_reject_constant,
            ),
        )


def write(
    path: str | os.PathLike[str],
    data: object,
    *,
    indent: int | None = 2,
    overwrite: bool = True,
    create_parents: bool = True,
) -> Path:
    """UTF-8 JSONを即時に保存し、指定先のPathを返す。

    既定は親フォルダを作成し、既存ファイルを上書きする。
    dictのキーはstrのみ。tupleはJSON配列になり、非有限数・循環参照は拒否する。
    一時ファイルを閉じてから確定するため、書き込み途中では保存先を変更しない。
    失敗時も作成済みの親フォルダは残す。拡張子は自動付加しない。
    """
    if indent is not None:
        if type(indent) is not int:
            raise TypeError("indent must be an int or None.")
        if indent < 0:
            raise ValueError("indent must be nonnegative.")
    if type(overwrite) is not bool or type(create_parents) is not bool:
        raise TypeError("overwrite and create_parents must be bools.")
    target = Path(path)
    _validate(data, set())
    text = json.dumps(data, ensure_ascii=False, allow_nan=False, indent=indent)
    if create_parents:
        target.parent.mkdir(parents=True, exist_ok=True)

    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=target.parent,
            prefix=".bdu-json-",
            suffix=".tmp",
            delete=False,
        ) as stream:
            temporary = Path(stream.name)
            stream.write(text)
        if overwrite:
            os.replace(temporary, target)
        elif os.name == "nt":
            # Windowsのrenameは既存宛先を上書きせず、確定時に存在を検査する。
            os.rename(temporary, target)
        else:
            os.link(temporary, target)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return target
