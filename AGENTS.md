# AI Agent Guide

このファイルは、`bakedanuki-util` で作業する AI エージェント向けの作業仕様書です。

新しいチャットや別エージェントが作業を始めるときは、まずこのファイルを読んでください。

## Project Context

`bakedanuki-util` は、Autodesk Maya 用の Python ユーティリティパッケージです。

今後制作予定のリグシステムパッケージ `bakedanuki-rig` で使うために開発されています。その中でも、リグ専用ではなく他の Maya ツール開発にも使える汎用部分を `util` として切り出しています。

現状は v1.0.0 未満の開発中 API です。まだ破壊的変更が入る可能性があります。

主な関心領域は次の通りです。

- Maya の DG / DAG ノード操作
- `NodeOperator`
- `AttributeField` / `AttrOperator` / `PlugOperator`
- `ModifierManager`
- `Nodes`
- `NodeCreator` / `ExistingNode`（`Nodes` の内部実装）
- extra attribute / `AddAttr`
- Maya API / `maya.api.OpenMaya`
- pytest による Maya 実行環境での検証

## Repository Layout

主な構成です。

- `bakedanuki/bakedanuki-util/python/bd_util`
  - パッケージ本体です。
- `bakedanuki/bakedanuki-util/python/bd_util/maya`
  - Maya 関連の実装です。
- `bakedanuki/bakedanuki-util/python/bd_util/maya/node`
  - ノード、modifier、NodeOperator 関連の中心です。
- `bakedanuki/bakedanuki-util/python/bd_util/_dev`
  - 開発用コードです。ノード生成スクリプトなどがあります。
- `bakedanuki/bakedanuki-util/python/bd_util/_test`
  - 古い手動テスト、ベンチ、Maya 上で直接実行する検証コードが残っています。
- `bakedanuki/modules`
  - Maya Module の `.mod` ファイルを配置します。
- `bakedanuki/installer.py`
  - Maya のビューポートへドラッグ&ドロップして、現在の Maya バージョン用 `Maya.env` に `bakedanuki/modules` を登録する導入補助です。
- `bakedanuki/launchers/maya2025.bat` / `bakedanuki/launchers/maya2026.bat` / `bakedanuki/launchers/maya2027.bat`
  - 試用向けに `bakedanuki/modules` を `MAYA_MODULE_PATH` へ追加して対応バージョンの Maya を起動します。
- `tests`
  - pytest 化されたテストです。
- `bakedanuki/bakedanuki-util/docs/maya/node_operator`
  - NodeOperator 周辺の設計メモです。
- `README.md`
  - 開発リポジトリとしての入口です。
- `bakedanuki/README.md`
  - Maya Module 配布フォルダとしての入口です。
- `bakedanuki/bakedanuki-util/README.md`
  - `bakedanuki-util` パッケージ本体の説明です。

## Development Environment

前提環境です。

- OS: Windows
- Maya: Maya 2025 以降
- Python: Maya 2025 bundled Python 3.11.4 以降
- Shell: PowerShell
- Main checkout: `D:\develop\bakedanuki_dev\bakedanuki-util`

Maya 専用パッケージとして扱ってください。通常の Python だけで完結する前提にしないでください。

PowerShell で UTF-8 の Markdown を読むと文字化けして見えることがあります。文字化けに見えた場合は、まず UTF-8 指定で確認してください。

```powershell
Get-Content -Raw -Encoding UTF8 README.md
```

## Python Path And pytest

このリポジトリには現時点で `pyproject.toml` や `setup.py` はありません。

テストは `mayapy` で実行してください。通常の Python では Maya API が import できません。

`pytest` が Maya Python から見えない場合は、まず一時ディレクトリへ入れます。

```powershell
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pip install --target $env:TEMP\codex-mayapy-pytest pytest
```

テスト実行時は、pytest の配置先と `bakedanuki/bakedanuki-util/python` の両方を `PYTHONPATH` に入れるのが安全です。

```powershell
$pytestTarget = Join-Path $env:TEMP 'codex-mayapy-pytest'
$pythonPath = Resolve-Path .\bakedanuki\bakedanuki-util\python
$env:PYTHONPATH = "$pytestTarget;$pythonPath"
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pytest tests
```

特定テストだけ実行する例です。

```powershell
$pytestTarget = Join-Path $env:TEMP 'codex-mayapy-pytest'
$pythonPath = Resolve-Path .\bakedanuki\bakedanuki-util\python
$env:PYTHONPATH = "$pytestTarget;$pythonPath"
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pytest tests\maya\node\operator\attr\test_extra_attr.py
```

`swig/python detected a memory leak ...` のような表示がテスト終了後に出ることがあります。pytest の終了コードが成功であれば、通常は非失敗ログとして扱ってください。

## Verification Policy

変更内容に応じて検証範囲を選んでください。

- README や docs のみ
  - `git diff --check -- <changed-files>` で十分なことが多いです。
- 小さな局所変更
  - 関連する targeted pytest を実行してください。
- `AttributeField`, `PlugOperator`, `AttrOperator`, `ModifierManager`, enum base など共有基盤の変更
  - targeted pytest に加えて、原則として full pytest を実行してください。
- DG ノード生成、node attr 解決、共通 import に関わる変更
  - full pytest に加えて、必要に応じて DG モジュールの import sweep を検討してください。

全体テストです。

```powershell
$pytestTarget = Join-Path $env:TEMP 'codex-mayapy-pytest'
$pythonPath = Resolve-Path .\bakedanuki\bakedanuki-util\python
$env:PYTHONPATH = "$pytestTarget;$pythonPath"
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pytest tests
```

差分チェックです。

```powershell
git diff --check
```

CRLF warning はこの環境で出ることがあります。`git diff --check` が終了コード 0 なら、基本的には非ブロッキングとして扱ってください。

## Communication Policy

ユーザーとのやり取りは日本語を基本にしてください。

望ましい進め方です。

- まず現状を確認してから編集する。
- ユーザーが「調査のみ」「コード変更禁止」と言った場合は、絶対に編集しない。
- コード変更が許可されている場合は、提案だけで止まらず実装と検証まで進める。
- 作業中は短い進捗を挟む。
- 不明点が作業を止めるほどでなければ、妥当な仮定で進める。
- ユーザーは並行して開発していることがあるため、作業前に `git status --short` を確認する。
- 作業ツリーに自分が触っていない変更があっても、勝手に戻さない。
- 最終報告では、変更内容、検証結果、未実行の確認を簡潔に伝える。

ユーザーは実装の意図や API 設計の理解も大切にしています。必要に応じて、短く理由を添えてください。

## Git And Editing Policy

- ユーザーの許可なく commit / push しないでください。
- `git reset --hard` や `git checkout -- <file>` のような破壊的操作は、明示依頼がない限り禁止です。
- 既存変更を自分の判断で巻き戻さないでください。
- 手作業のファイル編集は `apply_patch` を使ってください。
- 生成ファイルや大きな機械的更新は、内容と理由を明確にしたうえで行ってください。
- 既存のスタイルに合わせ、無関係な整形やリファクタは避けてください。

## Coding Policy

このリポジトリでは、既存設計に寄せてください。

重要な方針です。

- Maya 専用パッケージとして割り切る。
- OpenMaya の実挙動を優先する。
- 推測で Maya API の意味を決めない。怪しい場合は `mayapy` で確認する。
- `bd_util` パッケージ内部の module 間 import は、`from bd_util.maya...` のような
  package top 起点ではなく、import 元の module を基準にした相対 import を使う。
  利用者向けサンプルやテストから公開 API を import する場合は、この制約の対象外とする。
- `cmds` / PyMEL より、可能な範囲で `maya.api.OpenMaya` を中心に考える。
- ただし Maya 標準挙動や undo の都合で必要な場合は、既存方針に従う。
- 共有基盤を触る場合は、影響範囲を広く見る。
- `NodeOperator`, `AttributeField`, `PlugOperator` の責務分離を崩さない。
- 速度改善は歓迎だが、読みやすさと既存 API の便利さを壊さない。
- コメントは必要最小限にする。

## IDE Completion And Type Hints

このパッケージでは、IDE のコード補完と型注釈を重要な API 品質として扱います。

ここでいう IDE 補完は、VS Code / Pylance / Pyright などの Language Server が、`.` アクセス時に候補を表示できる状態を指します。公開 API や具体クラスでは、意図せず補完候補が出ない状態を作らないでください。

重要な方針です。

- 公開 API は、可能な限りドットアクセス補完が効く設計にする。
- `NodeOperator` / `PlugOperator` / `AttributeField` / `Nodes` など、ユーザーが直接触る面では戻り値型が追えるようにする。
- 動的生成や `__getattr__()` を使う場合でも、必要に応じて `.pyi` stub、明示メソッド、`Generic`、型引数などで補完を補助する。
- 具象クラスで補完が失われた場合は、単なる表示上の問題として放置しない。API の使い勝手の不具合として扱う。
- 抽象基底クラス、内部 helper、意図的に型が未確定な generic base では、補完が限定的でも許容する。ただし、それが意図的な設計かどうかを判断する。
- 既存の補完を壊すリファクタは避ける。必要な場合は、代替の型情報を同時に用意する。

特に、`node.attr.child` や `nodes.create.composeMatrix(...)` / `nodes.existing.decomposeMatrix(...)` のような主要な利用経路では、ユーザーが IDE 上で候補を辿れることを重視してください。

## NodeOperator Usage Conventions

README や docs のサンプルでは、基本的に次の書き方を使ってください。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)
```

`Nodes` のインスタンス変数名は `nodes` を使う方針です。

```python
cmp_m = nodes.create.composeMatrix(name="cmp_m")
mult_m = nodes.create.multMatrix(name="mult_m")

cmp_m.outputMatrix > mult_m.matrixIn[next]
mod.do_it_dg()
```

ノード作成、値設定、接続は `ModifierManager` に積まれます。可能なら最後に 1 回 `mod.do_it_dg()` / `mod.do_it_dag()` でまとめて実行する例にしてください。

接続は即時実行ではなく、`MDGModifier.connect()` に積む処理です。`ModifierManager` の履歴に入るため、その単位で undo / redo 対象になります。

速度を重視する文脈では、演算子 `>` より `.connect()` を優先して説明しても構いません。

```python
src.output.connect(dst.input)
```

`nodes.existing` はシーン上に既に存在するノードを包む入口です。

```python
node = nodes.existing("existing_node")
```

`nodes.existing` は内部で `ExistingNode` を利用します。
既存ノードを勝手に変更しないため、初期値では `auto_add_attr=False` です。

## Important Implementation Notes

- `ModifierManager` は `MDGModifier` / `MDagModifier` を管理します。
- `Nodes` は `NodeCreator` と既存ノードアクセサに同じ `ModifierManager` を渡します。
- `do_it_dg()` / `do_it_dag()` した modifier は履歴として閉じ、次の操作には新しい modifier を使う設計です。
- `undo_it()` は積まれた modifier を逆順に undo します。
- `redo_it()` は undo 済みの stack を順順に doIt します。
- `NodeCreator` は `nodes.create` の内部実装です。`bd_util` のトップレベルには公開しません。
- `ExistingNode` は `nodes.existing` の内部実装です。`bd_util` および `bd_util.maya.node` のトップレベルには公開しません。
- `node.multiAttr[next]` は Python builtin の `next` を sentinel として使い、次の空き logical index を取ります。
- docs では `bdu`, `nodes`, `nodes.create`, `nodes.existing`, `matrixIn[next]`, 最後の 1 回の `mod.do_it_dg()` を優先してください。

## Documentation Policy

仕様を追加・変更した場合は、可能な範囲で docs も更新してください。

主なドキュメントです。

- `README.md`
  - 初見向けです。短い利用例とパッケージの位置づけを重視します。
- `bakedanuki/bakedanuki-util/docs/maya/node_operator/README.md`
  - NodeOperator 周辺の現行仕様の入口です。
- `bakedanuki/bakedanuki-util/docs/maya/node_operator/attributes.md`
  - Attribute / Plug / AddAttr 周辺です。
- `bakedanuki/bakedanuki-util/docs/maya/node_operator/modifier_manager.md`
  - ModifierManager の設計です。
- `bakedanuki/bakedanuki-util/docs/maya/node_operator/generator.md`
  - ノード生成器の設計です。
- `bakedanuki/bakedanuki-util/docs/maya/node_operator/testing.md`
  - テスト方針です。
- `bakedanuki/bakedanuki-util/docs/maya/node_operator/roadmap.md`
  - 今後の予定です。

README のコード例は、実際にユーザーが好んでいる短い書き方に寄せてください。

## When In Doubt

迷ったら、次の優先順位で判断してください。

1. ユーザーの直近の指示
2. この `AGENTS.md`
3. 既存コードの実装パターン
4. `bakedanuki/bakedanuki-util/docs/maya/node_operator` 以下の設計メモ
5. Maya / OpenMaya の実挙動

特に Maya API の挙動に関わる場合は、推測より `mayapy` での確認を優先してください。
