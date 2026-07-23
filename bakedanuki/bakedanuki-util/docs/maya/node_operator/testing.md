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

`tests` 以下では、公開 API、NodeOperator、matrix 操作、開発用 generator を
次のように分けて検証しています。

### 公開 node API と modifier

- `tests/maya/node/test_nodes.py`
  - `Nodes` の公開範囲、`nodes.create` / `nodes.existing` の共有状態を検証します。
- `tests/maya/node/test_existing_node.py`
  - 既存 DG / DAG / shape node の自動判定と型別アクセスを検証します。
- `tests/maya/node/creator/test_node_creator.py`
  - node 作成、nodeType 解決、補完用 node 名を検証します。
- `tests/maya/node/modifier/test_modifier_manager.py`
  - DG / DAG modifier の実行履歴と undo / redo を検証します。

### Attribute と Plug

- `tests/maya/attr/test_query.py`
  - Maya attribute 情報の取得と fallback を検証します。
- `tests/maya/node/operator/attr/test_extra_attr.py`
  - extra attribute の追加、型解決、値設定を検証します。
- `tests/maya/node/operator/attr/test_keyframe.py`
  - animCurve の作成、query、削除、tangent 操作を検証します。
- `tests/maya/node/operator/attr/test_data_matrix.py`
  - matrix plug と `TransformMatrix` の連携を検証します。

### NodeOperator

- `tests/maya/node/operator/node/dg/test_plus_minus_average.py`
  - scalar / multi plug、alias、接続、enum 操作を検証します。
- `tests/maya/node/operator/node/dg/test_wt_add_matrix.py`
  - compound multi plug と次の空き logical index への接続を検証します。
- `tests/maya/node/operator/node/dag/test_parent.py`
  - DAG の親子操作、undo / redo、循環する親子関係の防止を検証します。
- `tests/maya/node/operator/node/dag/test_matrix.py`
  - DAG 間の relative / local matrix 計算を検証します。
- `tests/maya/node/operator/node/test_process_speed.py`
  - Maya バージョンに応じた PyMEL 比較ベンチマークの実行可否を検証します。

### TransformMatrix

- `tests/maya/transform/matrix/test_transform_matrix.py`
  - matrix の入力、snapshot、分解、乗算、逆行列を検証します。

### 開発用 generator

- `tests/dev/maya/node/operator/node/test_generate.py`
  - AttributeField と NodeOperator の生成内容、安全でない nodeType の除外を検証します。
- `tests/dev/maya/node/operator/node/test_generate_existing_node_stub.py`
  - `nodes.create` / `nodes.existing` の型情報を公開する stub の生成結果を検証します。

`mayapy.exe -m pytest tests` では、上記の Maya 実行テストと開発用 generator
テストをまとめて実行します。

## pytest 化の方針

pytest 側では、ログ出力ではなく assert で仕様を固定します。

特に次のような挙動は pytest に向いています。

- `Nodes` が公開 node API の入口になり、内部 accessor が同じ `ModifierManager` を共有する。
- `nodes.existing` の自動判定と型別アクセスが、実際の Maya nodeType を正しく解決する。
- `NodeCreator` と生成 stub が、公開する node 名と具体的な戻り値型を維持する。
- alias が同じ `PlugOperator` instance を返す。
- child plug access が正しい plug 名を指す。
- `set()` / `set_direct()` / `get()` の結果が一致する。
- wrong count などの error が期待通り発生する。
- DAG の親子操作が undo / redo に対応し、循環する親子関係を作らない。
- `TransformMatrix` と matrix plug が同じ行列値を扱う。
- `ModifierManager` の undo / redo が期待通り動作する。
- `lookup_attr_cls()` が新しい型を解決できる。
- generator の生成結果と `.pyi` stub が実装と一致する。

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
