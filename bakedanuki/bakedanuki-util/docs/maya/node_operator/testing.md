# Testing

このプロジェクトでは、通常の検証を `pytest` に寄せます。

既存の `_test` 配下は、速度計測や手動確認用として残します。

## 推奨実行方法

Maya API を使うテストは `mayapy.exe` で実行します。

PowerShell では、パスにスペースが含まれる executable を呼ぶため先頭に `&` が必要です。

```powershell
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pytest tests
```

Codex 側の mayapy に pytest が入っていない場合は、target install した pytest の場所を `PYTHONPATH` に足して実行します。

```powershell
$pytestTarget = Join-Path $env:TEMP 'codex-mayapy-pytest'
$pythonPath = Resolve-Path .\bakedanuki\bakedanuki-util\python
$env:PYTHONPATH = "$pytestTarget;$pythonPath"
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pytest tests
```

## 現在の pytest 対象

主なテストは次の通りです。

- `tests/maya/node/modifier/test_modifier_manager.py`
- `tests/maya/node/operator/attr/test_extra_attr.py`
- `tests/maya/node/operator/attr/test_keyframe.py`
- `tests/maya/node/operator/node/dg/test_plus_minus_average.py`
- `tests/maya/node/operator/node/dg/test_wt_add_matrix.py`

## pytest 化の方針

pytest 側では、ログ出力ではなく assert で仕様を固定します。

特に次のような挙動は pytest に向いています。

- alias が同じ `PlugOperator` instance を返す。
- child plug access が正しい plug 名を指す。
- `set()` / `set_direct()` / `get()` の結果が一致する。
- wrong count などの error が期待通り発生する。
- `ModifierManager` の undo / redo が期待通り動作する。
- `lookup_attr_cls()` が新しい型を解決できる。

## _test の扱い

`bakedanuki/bakedanuki-util/python/bd_util/_test` は速度計測や手元確認用です。

一般的な仕様固定は pytest に移し、ベンチマークや Maya console からの確認は `_test` に残します。

代表例:

```python
import bd_util._test.maya.node.operator.node.process_speed as ps

ps.main()
ps.main(accurate=True, repeat_count=3)
```

`accurate=True` の場合は median / min / max を出すため、通常計測より時間がかかります。

PyMEL の比較ベンチマークは、現在の Maya バージョン用キャッシュが PyMEL に含まれる場合のみ実行します。未対応の Maya バージョンでは PyMEL の計測だけをスキップし、その他の比較は継続します。

## ベンチマークの見方

NodeOperator は生の `maya.api.OpenMaya` より速くなることは基本的にありません。

ただし、現行の設計では次の最適化により、OpenMaya に近い速度を目指します。

- `fn_node` lazy cache
- plug cache
- indexed plug cache
- child index direct access
- `connect_next_index()` の next index cache
- descriptor access 時の cache key 改善

速度比較では 1 回ごとの揺れが大きいため、判断が難しい場合は accurate mode の median を見ます。

## 現行 snapshot

このドキュメント作成時点では、直近の開発確認で `mayapy -m pytest tests` が通っている状態を前提にしています。

docs 変更のみの場合、通常は pytest の再実行より `git diff --check` で十分です。
