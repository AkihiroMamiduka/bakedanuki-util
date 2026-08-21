# Testing

このプロジェクトでは、通常の検証を `pytest` に寄せます。

既存の `_test` 配下は、速度計測や手動確認用として残します。

## 推奨実行方法

Maya API を使うテストは `mayapy.exe` で実行します。

PowerShell では、パスにスペースが含まれる executable を呼ぶため先頭に `&` が必要です。

```powershell
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pytest tests
```

通常開発ではMaya 2025を基準にします。リリース前はMaya 2025 / 2026 / 2027の
各`mayapy`と対応する`plug-ins/maya<version>/bdUtilNodes.mll`を指定し、
全テストを実行します。ネイティブテストはversion別scriptから実行できます。

```powershell
.\scripts\test-native-maya2025.cmd
.\scripts\test-native-maya2026.cmd
.\scripts\test-native-maya2027.cmd
```

Codex 側の mayapy に pytest が入っていない場合は、target install した pytest の場所を `PYTHONPATH` に足して実行します。

```powershell
$pytestTarget = Join-Path $env:TEMP 'codex-mayapy-pytest'
$pythonPath = Resolve-Path .\bakedanuki\bakedanuki-util\python
$env:PYTHONPATH = "$pytestTarget;$pythonPath"
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pytest tests
```

## Black format

BlackはMaya実行環境とは分離した`.venv-format`へインストールします。
初回セットアップでは`requirements-format.txt`に固定したバージョンを使用します。

```powershell
.\scripts\setup-format.cmd
```

`bakedanuki`と`tests`以下のPythonコードを一括整形します。

```powershell
.\scripts\format.cmd
```

ファイルを変更せずに整形状態だけ確認する場合は`-Check`を指定します。
実際の差分も確認する場合は`-Diff`を追加します。

```powershell
.\scripts\format.cmd -Check
.\scripts\format.cmd -Check -Diff
```

設定はリポジトリ直下の`pyproject.toml`に置き、Python 3.11を対象にします。
VS CodeのBlack Formatterも`.venv-format`と同じ設定を使用します。
外部由来のMaya API stubを置く`typings`は一括整形の対象外です。

Generatorは生成コードを直接Blackへ依存させません。
ノードを再生成した場合は、生成処理の後に`format.cmd`を実行してから
差分確認とテストを行ってください。

## Pyright 型・補完 contract

`tests/typecheck/node_operator_contract.py` は、公開 API を利用したときに
Pyright が解決する型を `typing.assert_type()` で固定します。

現在は次の経路を検証します。

- `nodes.create` / `nodes.existing` の具体的な node 戻り値型。
- `AttributeField` の class access と instance access。
- compound child と alias の具体的な plug 型。
- enum plug と enum 定数。
- `multi[index]` / `multi[next]` の具体的な plug 型。
- `get()` の値型。
- 存在しない属性や不正な引数が型エラーになること。

型エラーになるべき行は、対象の diagnostic rule を
`# pyright: ignore[...]` で指定しています。
`pyrightconfig.json` の `reportUnnecessaryTypeIgnoreComment` を有効にしているため、
誤用が型エラーにならなくなった場合も contract failure になります。

Maya API stub はリポジトリの `typings/maya` に同梱しています。
`pyrightconfig.json` の `stubPath` を通して Pyright / Pylance から参照されるため、
開発環境ごとに `maya-stubs` をインストールする必要はありません。

Pyright CLI は、Maya 環境へ常設せず一時ディレクトリへ
インストールできます。

```powershell
$pyrightTarget = Join-Path $env:TEMP 'codex-mayapy-pyright'
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pip install `
    --upgrade `
    --target $pyrightTarget `
    -r requirements-typecheck.txt

$env:PYTHONPATH = $pyrightTarget
$env:PYRIGHT_PYTHON_CACHE_DIR = Join-Path $env:TEMP 'codex-pyright-cache'
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pyright `
    --project pyrightconfig.json `
    --pythonpath "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe"
```

期待する結果は `0 errors, 0 warnings, 0 informations` です。

このcontractは静的解析用で、Maya sceneを作成するruntime testではありません。
通常の挙動は引き続き `mayapy -m pytest tests` で検証します。

### 実装ファイルの診断確認

`pyrightconfig.json` の既定の `include` は `tests/typecheck` です。
これは通常実行を公開 API の型・補完 contract に限定するための設定で、
`bd_util` の全実装を自動的に総点検する設定ではありません。

実装ファイルや特定階層の Pylance 警告を調べる場合は、同じ設定と Maya interpreter を
使い、対象 path を明示します。例えば `_test` 全体を確認する場合は次の通りです。

```powershell
$pyrightTarget = Join-Path $env:TEMP 'codex-mayapy-pyright'
$env:PYTHONPATH = $pyrightTarget
$env:PYRIGHT_PYTHON_CACHE_DIR = Join-Path $env:TEMP 'codex-pyright-cache'
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pyright `
    --project pyrightconfig.json `
    --pythonpath "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" `
    bakedanuki/bakedanuki-util/python/bd_util/_test
```

通常の Python や Node.js 版 Pyright から実行すると、stub は見つかっていても Maya の
実 module source を解決できず、`reportMissingModuleSource` が出ることがあります。
コードの型不備と混同せず、最終判定は上記の `mayapy.exe` を指定した方法で行います。

診断を修正するときは次を基準にします。

- `Any` は動的 import や Maya command など避けられない境界へ限定する。
- Maya stub の可変長引数が実 API より狭い場合は、対象 callable だけを
  `Callable` へ cast し、実行時の呼び出し方は変えない。
- optional dependency は実行時 import とし、未導入時の既存 fallback を保つ。
- `_generated` 以下は生成元を修正して再生成する。
- diagnostic rule の global 無効化は、通常コードの書き間違いまで隠すため避ける。
- 接続と切断には `.connect()` / `.connect_from()` / `.disconnect()` /
  `.disconnect_from()` を使用する。

## 現在の pytest 対象

`tests` 以下では、公開 API、NodeOperator、matrix 操作、開発用 generator を
次のように分けて検証しています。

### 公開 node API と modifier

- `tests/maya/node/test_nodes.py`
  - `Nodes` の公開範囲、`nodes.create` / `nodes.existing` の共有状態を検証します。
- `tests/maya/node/test_existing_node.py`
  - 既存 DG / DAG / shape node の自動判定と型別アクセスを検証します。
  - 作成APIへ公開しない `ikHandle` / `ikEffector` も具体型へ解決し、同じ
    `ModifierManager` を共有することを検証します。
  - constraint 系14種をMaya上で作成し、全型が同じ `ModifierManager` を共有する
    concrete transform 型へ解決されることを検証します。
  - field / emitter 系11種もMaya上で作成し、全型の concrete transform 型と
    `ModifierManager` 共有を検証します。
  - dynamics / deformer 周辺5種もMaya上で作成し、全型の concrete transform 型と
    `ModifierManager` 共有を検証します。
  - HIK 系5種もMaya上で作成し、`HikFKJoint` / `HikHandle` が `Joint` /
    `IkHandle` の concrete base を維持することも検証します。
  - scene / utility 系6種もMaya上で作成し、`LookAt` が `AimConstraint` の
    concrete base を維持することも検証します。
  - VarGroup 系5種もMaya上で作成し、作成不能な抽象native基底
    `BaseGeometryVarGroup` を型階層として維持することも検証します。
- `tests/maya/node/creator/test_node_creator.py`
  - node 作成、nodeType 解決、補完用 node 名を検証します。
  - concrete transform class が存在しても、allowlistにないtypeは
    `nodes.create` へ公開しないことを検証します。
- `tests/maya/node/creator/test_shape_with_transform.py`
  - transform と shape の一括作成、命名、親子関係、undo / redo を検証します。
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
- `tests/maya/value/test_scalar_compound.py`
  - compound 専用値型の immutable sequence、component access、型ごとの
    equality、演算未対応を検証します。

### NodeOperator

- `tests/maya/node/operator/node/dg/test_plus_minus_average.py`
  - scalar / multi plug、alias、接続、enum 操作を検証します。
- `tests/maya/node/operator/node/dg/test_wt_add_matrix.py`
  - compound multi plug と次の空き logical index への接続を検証します。
- `tests/maya/node/operator/node/dag/test_parent.py`
  - DAG の親子操作、undo / redo、循環する親子関係の防止を検証します。
- `tests/maya/node/operator/node/dag/test_matrix.py`
  - DAG 間の relative / local matrix 計算を検証します。
- `tests/maya/node/operator/node/dag/shape/test_create.py`
  - 親 Transform 必須の shape 作成、明示的な公開対象、同一 modifier での
    一括作成、undo / redo を検証します。
- `tests/maya/node/operator/node/dag/shape/test_generated.py`
  - concrete shape 81種の public / generated module 対応と import を検証します。
- `tests/maya/node/operator/node/test_process_speed.py`
  - Maya バージョンに応じた PyMEL 比較ベンチマークの実行可否を検証します。

### TransformMatrix

- `tests/maya/transform/matrix/test_transform_matrix.py`
  - matrix の入力、snapshot、分解、乗算、逆行列を検証します。

### 開発用 generator

- `tests/dev/maya/node/operator/node/test_generate.py`
  - AttributeField と内部 `_generated` package の生成 NodeOperator、公開 wrapper の生成・保護、安全でない nodeType の除外を検証します。
  - transform / shape のattribute queryが調査用node instanceを作らず、
    登録済みnode typeから静的に取得されることを検証します。
  - concrete transform のnative基底が生成済みの場合、そのclassを継承して
    基底attributeを重複生成しないことを検証します。
- `tests/dev/maya/node/operator/node/test_generate_existing_node_stub.py`
  - `nodes.create` / `nodes.existing` / `nodes.create.with_transform` の型情報を
    公開する stub の生成結果を検証します。

`mayapy.exe -m pytest tests` では、上記の Maya 実行テストと開発用 generator
テストをまとめて実行します。

## MtoA 由来の warning

`tests/maya/attr/test_query.py` では、`aiAreaLight` の attribute 情報を検証するため
`mtoa` plugin を読み込みます。

Maya 2025 付属の MtoA は、読み込み時に正規表現文字列の
`invalid escape sequence` と、Python の旧 import API である
`find_module()` / `find_loader()` / `load_module()` の
`DeprecationWarning` を出力します。

これらは `bd_util` ではなく MtoA 内部から発生するため、MtoA を読み込む
`test_get_attribute_infos_handles_attrs_without_open_maya_plug` だけに
`pytest.mark.filterwarnings` を指定して抑制します。

`pytest.ini` で `DeprecationWarning` 全体を無効化すると、`bd_util` 自身の
非推奨 API を見落とす可能性があるため、外部 package 由来と確認できた warning
だけを test 単位で抑制します。

Maya / MtoA の更新により警告が解消された場合は、この filter の削除を検討します。

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

## 競合パッケージとの同条件ベンチマーク

`competitor_benchmark` は次の API を同じ Maya、同じ処理件数、
各計測前の新規シーンという条件で比較します。

- `maya.cmds`
- `maya.api.OpenMaya`
- NodeOperator
- PyMEL
- cymel
- cmdx
- AL_omx

対象シナリオは、既存ノードのラップ、plug access、scalar get / set、
node 作成、直列接続、matrix graph 作成です。library import、scene 初期化、
事前準備、結果検証、scene 破棄は計測区間に含めません。
また、import による Maya plug-in 読み込みの影響を全対象で揃えるため、
利用可能な全 library を最初に import してから計測を開始します。

NodeOperator と OpenMaya は処理を modifier に積んで最後に実行できます。
一方、cmdx と AL_omx は node 作成を途中で即時反映するため、
完全な一括実行にはなりません。この差を隠さないため、CSV の
`execution_mode` に `immediate` / `batched` / `hybrid` を記録します。
比較結果は単一の総合順位ではなく、scenario と execution mode ごとに
解釈してください。

### 競合パッケージの配置

pip で配布されている比較対象は `requirements-benchmark.txt` で
計測時のバージョンを固定します。

```powershell
$thirdParty = 'D:\thirdparty\python\site-packages'
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pip install `
    --upgrade `
    --target $thirdParty `
    -r requirements-benchmark.txt
```

cymel は PyPI package ではないため、source を同じ third-party
directory の下へ clone します。

```powershell
git clone --depth 1 --branch main `
    https://github.com/ryusas/cymel.git `
    D:\thirdparty\python\site-packages\_cymel_source
```

初回の比較基準は cymel `0.33.2026070600`
（commit `f46f395517d907b852fd7d1cede78b5268508a90`）です。
将来更新した場合は、CSV の `adapter_version` とあわせて比較してください。

### 実行方法

PyMEL が home directory に `pymel.log` を作らないよう、benchmark 同梱の
logging config を指定します。third-party packages と `bd_util` の両方を
`PYTHONPATH` に入れて mayapy から実行します。

```powershell
$thirdParty = 'D:\thirdparty\python\site-packages'
$cymelPython = Join-Path $thirdParty '_cymel_source\python'
$packagePython = Resolve-Path .\bakedanuki\bakedanuki-util\python
$env:PYTHONPATH = "$cymelPython;$thirdParty;$packagePython"
$env:PYMEL_CONF = Resolve-Path `
    .\bakedanuki\bakedanuki-util\python\bd_util\_test\maya\node\operator\node\competitor_benchmark\pymel.conf

& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m `
    bd_util._test.maya.node.operator.node.competitor_benchmark `
    --count 1000 `
    --repeat-count 5
```

手早い疎通確認では `--count 10 --repeat-count 1` を使用できます。
`--adapter NodeOperator` や `--scenario matrix_graph` は複数回指定でき、
対象を絞り込めます。

計測値は既定で repository root の
`benchmark_results/competitor/*.csv` へ保存します。
`benchmark_results/` は `.gitignore` で除外しているため、
比較結果そのものは Git 管理されません。CSV には各 repeat の生データを保存し、
console には scenario ごとの median / min / max を表示します。

## 現行 snapshot

このドキュメント作成時点では、直近の開発確認で `mayapy -m pytest tests` が通っている状態を前提にしています。

docs 変更のみの場合、通常は pytest の再実行より `git diff --check` で十分です。
