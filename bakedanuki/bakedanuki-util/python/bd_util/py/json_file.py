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
    """UTF-8 の JSON ファイルを読み込む。

    Args:
        path: 読み込むファイルのパス。UTF-8 BOM も受け付ける。

    Returns:
        復元した JSON 値。

    Raises:
        OSError: ファイルを読み込めない場合。
        ValueError: JSON が不正、または数値が非有限の場合。
    """
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
    """JSON を UTF-8 で保存し、保存先のパスを返す。

    一時ファイルを確定時に置き換える。拡張子は追加しない。

    Args:
        path: 保存先のパス。
        data: JSON に変換する値。辞書のキーは文字列のみ。
            タプルは配列として保存する。
        indent: インデント幅。``None`` は改行なし。
        overwrite: 既存ファイルを上書きするか。
        create_parents: 親ディレクトリを作成するか。

    Returns:
        保存先の ``Path``。

    Raises:
        TypeError: 引数の型や JSON 値が対応外の場合。
        ValueError: ``indent`` が負、値が非有限、または循環参照の場合。
        OSError: 保存に失敗した場合。作成済みの親ディレクトリは残る。
    """
    if indent is not None:
        if type(indent) is not int:
            raise TypeError("indent must be an int or None.")
        if indent < 0:
            raise ValueError("indent must be nonnegative.")
    if type(overwrite) is not bool or type(create_parents) is not bool:
        raise TypeError("overwrite and create_parents must be bools.")
    target = Path(path)
    # データの検証を先に終え、保存先を変更する前に失敗を確定させる。
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
