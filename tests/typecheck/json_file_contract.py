"""汎用JSONファイル入出力とAnimationClipファイルAPIの補完contract。"""

from os import PathLike
from pathlib import Path
from typing import assert_type

import bd_util as bdu
from bd_util.py import json_file


def json_file_contract(
    path: str | PathLike[str], clip: bdu.AnimationClip, data: dict[str, object]
) -> None:
    assert_type(bdu.json_file.read(path), object)
    assert_type(json_file.read(Path("settings.json")), object)
    assert_type(bdu.json_file.write(path, data), Path)
    assert_type(
        json_file.write(
            path, data, indent=None, overwrite=False, create_parents=False
        ),
        Path,
    )
    assert_type(clip.save(path), Path)
    assert_type(
        clip.save(path, indent=4, overwrite=False, create_parents=True), Path
    )
    assert_type(bdu.AnimationClip.load(path), bdu.AnimationClip)
    assert_type(bdu.AnimationClip.load(clip.save(path)), bdu.AnimationClip)
    bdu.json_file.read(42)  # pyright: ignore[reportArgumentType]
    bdu.json_file.write(
        path,
        data,
        indent=" ",  # pyright: ignore[reportArgumentType]
    )
    bdu.json_file.write(
        path,
        data,
        overwrite="yes",  # pyright: ignore[reportArgumentType]
    )
    clip.save(
        path,
        create_parents="yes",  # pyright: ignore[reportArgumentType]
    )
    bdu.AnimationClip.load(42)  # pyright: ignore[reportArgumentType]
