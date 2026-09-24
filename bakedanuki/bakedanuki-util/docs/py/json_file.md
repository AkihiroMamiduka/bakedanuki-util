# JSONファイル入出力

`bdu.json_file`は設定・プリセットなどのJSONファイルを読み書きする汎用モジュールです。
実装は`bd_util.py.json_file`に置き、Maya APIやAnimationClip固有のschemaには依存しません。
`bd_util`パッケージ全体の対応実行環境は、引き続きMayaです。

```python
import bd_util as bdu

path = bdu.json_file.write(
    r"D:\settings\my_tool\settings.json",
    {"name": "歩き", "speed": 1.0},
)
data = bdu.json_file.read(path)
```

`from bd_util.py import json_file`でも同じモジュールを利用できます。

## API

```python
json_file.write(
    path: str | os.PathLike[str],
    data: object,
    *,
    indent: int | None = 2,
    overwrite: bool = True,
    create_parents: bool = True,
) -> pathlib.Path

json_file.read(path: str | os.PathLike[str]) -> object
```

- `write()`は指定されたパスの`Path`を返します。相対パスは現在の作業ディレクトリを基準とし、
  戻り値も相対パスです。拡張子の付加や、環境変数・`~`の展開は行いません。
- 親フォルダは既定で必要な階層をまとめて作成します。`create_parents=False`では作成しません。
- 既存ファイルは既定で上書きします。`overwrite=False`では保存確定時に宛先が存在すると
  `FileExistsError`になり、途中で別処理が作成したファイルも上書きしません。
- UTF-8・BOMなし・改行LFで保存し、日本語をエスケープせず保持します。
  読み込みではBOM付きUTF-8も許容します。
- `indent`は0以上の整数または`None`です。既定は2スペース、`None`なら改行・字下げを付けません。
- 保存できる値は`None`・bool・int・有限float・str・list・tuple・strキーのdictです。
  tupleはJSON配列になり、読み込むとlistになります。循環参照や任意の独自オブジェクトは拒否します。
  JSON文字列を`write()`に渡すと、文字列自体がJSON値として保存されます。辞書データを保存する場合は
  JSON化する前のdictを渡してください。
- `NaN`・無限大は読み書きとも拒否します。読み込み時に`1e999`などがfloatの範囲を超える場合も拒否します。
- `read()`の戻り値型は`object`です。JSONのトップレベルはdictとは限らず、配列・文字列・数値・
  bool・`null`も許容します。必要なデータ構造の検証は呼び出し側で行ってください。

## 失敗時の扱い

ファイル不在・権限不足・文字コード・JSON構文・不正な値などの失敗は例外を送出します。
空辞書や`False`への置き換えは行いません。JSON構文エラーは`json.JSONDecodeError`、
非有限数は`ValueError`、保存できないPython型は`TypeError`になります。

保存先を直接切り詰めず、同じ親フォルダの一時ファイルへ書き込み、閉じてから保存先へ確定します。
書き込み・close・確定に失敗した場合は既存ファイルを維持し、一時ファイルを削除します。
作成済みの親フォルダは失敗時も残します。OSによる後始末の拒否やプロセスの強制終了、
電源断まで復旧を保証するものではありません。

保存・読込は即時のファイル操作であり、`ModifierManager`やMayaのUndo / Redoには入りません。
AnimationClipでは、schema検証も行う専用の
[`clip.save()` / `AnimationClip.load()`](../maya/node_operator/animation_clip.md#jsonファイルの保存読込)を使用できます。
