# Maya version 対応

この文書は、NodeOperator の Maya version 対応を保守し、将来の Maya を追加するための
設計仕様と作業手順です。現在の正式な対応範囲は Maya 2025 / 2026 / 2027 です。

## 基本方針

version 対応は、実行時の schema 選択と IDE の補完選択を独立させます。

- 実行時は、起動中の Maya を `MGlobal.apiVersion()` から自動判定します。
- `typing_maya_version` は Pylance / Pyright の補完対象だけを選択します。
- `typing_maya_version` は実行 Maya の選択、version 一致検査、node availability の
  変更には使用しません。
- Maya 2025 の生成結果を基準 snapshot とし、後続 version は変更された schema だけを
  sparse overlay として保持します。
- version 間の比較には固定 plugin profile を使います。plugin のロード漏れを
  Maya の schema 差分として記録しません。

```python
import bd_util as bdu

nodes = bdu.Nodes(typing_maya_version="2027")
```

このコードを Maya 2025 で実行しても、runtime は Maya 2025 の schema を使用します。
一方、IDE は Maya 2027 用の `nodes.create` / `nodes.existing` / `nodes.types` を表示します。

## Runtime schema の選択

`python/bd_util/maya/node/_maya_version.py` が、実行中 Maya の major version と
generated package の検索順を決定します。

例えば Maya 2027 では、各 `_generated` package の検索順が次のようになります。

```text
_generated_maya2027
_generated_maya2026
_generated
```

2027 で変更されていない class は 2026 overlay、そこにもなければ 2025 の基準
snapshot から解決されます。後続 version ごとに全 class を複製しません。

追加・廃止 node の利用可能期間は
`python/bd_util/maya/node/_node_version_registry.py` の
`NODE_TYPE_VERSION_RANGES` が管理します。上限は exclusive です。

```python
NODE_TYPE_VERSION_RANGES = {
    "absoluteDL": ((2026, None),),
    "addDoubleLinear": ((2025, 2026),),
}
```

廃止 node の基準 class と public wrapper は履歴として残します。runtime accessor と
補完 stub から version に応じて除外し、生成済みファイル自体を削除して表現しません。

未対応の将来 version で既存 overlay が読み込める場合があっても、それを正式対応とは
扱いません。対応 version、schema、型 contract、native plug-in、テスト入口をすべて
追加して初めて正式対応とします。

## IDE 補完の選択

`nodes.pyi` は `typing_maya_version` の `Literal` ごとに `Nodes.__new__()` の戻り値を
overload します。

```python
@overload
def __new__(
    cls,
    modifier_manager: ModifierManager | None = None,
    *,
    typing_maya_version: Literal["2027"],
) -> _NodesMaya2027: ...
```

constructor の結果型を version ごとに変えるため、選択は `__init__()` ではなく
`__new__()` の overload で表現します。`_NodesMaya2027` は、version 専用の
`_NodeCreatorMaya2027`、`_ExistingNodeAccessorMaya2027`、`_NodeTypesMaya2027` を返します。

実際の補完面は `_versioned_accessors.pyi` に生成します。
`typing_maya_version` を省略した `Nodes()` は、全対応 version に共通する安全な API 面を
返します。version 間で attribute 型だけが異なる場合、共通面では union 型になります。

`nodes.pyi` と `_versioned_accessors.pyi` は生成物です。補完を修正するときは
`generate_existing_node_stub.py` と version schema を修正し、生成物を手作業で直しません。

## Source of truth

version 対応に関する主な管理場所です。

| 対象 | 管理場所 |
| --- | --- |
| runtime の対応 version・overlay 検索順 | `python/bd_util/maya/node/_maya_version.py` |
| node の追加・廃止期間 | `python/bd_util/maya/node/_node_version_registry.py` |
| 固定 plugin profile・inventory・生成対象 | `python/bd_util/_dev/maya/node/operator/node/version_schema.py` |
| NodeOperator schema の生成先選択 | `python/bd_util/_dev/maya/node/operator/node/generate.py` |
| version schema 生成 CLI | `python/bd_util/_dev/maya/node/operator/node/generate_version_schema.py` |
| 補完 stub 生成 | `python/bd_util/_dev/maya/node/operator/node/generate_existing_node_stub.py` |
| runtime の `typing_maya_version` 引数 | `python/bd_util/maya/node/nodes.py` |
| generated schema 差分 | `operator/node/**/_generated_maya<version>` |
| compound attribute 差分 | `operator/attr/define/node_attr_maya<version>` |
| runtime version contract | `tests/maya/node/test_maya_version.py` |
| schema・overlay contract | `tests/dev/maya/node/operator/node/test_version_schema.py` |
| IDE 補完 contract | `tests/typecheck/node_operator_maya_version_contract.py` |
| Maya Module の配布先選択 | `bakedanuki/modules/bd_util.mod` |

## 新しい Maya version の追加手順

以下は Maya 2028 のような次 version を追加するときのチェックリストです。

### 1. 実行環境と配布入口を追加する

1. 対象 Maya と必要な bundled plugin をインストールします。
2. `bakedanuki/launchers/maya<version>.bat` を追加します。
3. `bakedanuki/modules/bd_util.mod` に `MAYAVERSION` entry と version 別 plugin path を
   追加します。
4. `bakedanuki/bakedanuki-util/plug-ins/maya<version>` を用意します。
5. build / pytest / native test / UI test / Pyright の version 別 `.cmd` を追加します。
6. 対応する PowerShell script の `ValidateSet` と、`*-all.cmd` / `verify.ps1` の
   version loop を更新します。

native plug-in を build・stage するときは Maya を終了するか `bdUtilNodes` を
unloadします。配布先の `.mll` が Maya にロードされていると上書きできません。

### 2. version の列挙を更新する

次の4系統をすべて更新します。

1. runtime の `_maya_version.py::SUPPORTED_MAYA_VERSIONS`
2. schema 管理の `version_schema.py::SUPPORTED_MAYA_VERSIONS`
3. schema 生成先の `generate.py::_SUPPORTED_GENERATED_MAYA_VERSIONS`
4. stub 生成の `generate_existing_node_stub.py::_SUPPORTED_MAYA_VERSIONS`

`nodes.py` の `typing_maya_version` annotation と、stub generator が出力する import、
`Literal` union、version facade も新versionを含むようにします。`nodes.pyi` 自体は
generatorから再生成します。

version別schemaを持つ公開wrapperへ共通操作を追加するときは、生成baseの後ろに
名前付きのbehavior mixinを継承させます。例えばTA / TL / TUの`AnimCurveKeyframes`です。
stub生成器は同じmixinをversion別classにも継承させるため、`.keyframe`等の手書きAPIを
全versionで補完できます。mixinはschema属性を定義せず、公開wrapper本体への独自member追加は
引き続き生成時に拒否します。旧versionの公開wrapper全体を継承して、新versionで削除された
属性を再公開する方法は使用しません。

同じstub生成器は、全対応schemaを含む`AnimCurveTANode`等の型aliasと、全8型を束ねる
`AnimCurveNode`も生成します。`find_anim_curves()`はこの型情報を使い、`nodes.types`の
version別クラスをfilterに渡した場合も具体型と`.keyframe`の補完を保持します。
これらは`_versioned_accessors.pyi`内の型検査専用aliasで、実行時のimport対象ではありません。

### 3. 固定 profile で schema 差分を確定する

1. 既存 version と同じ固定 plugin profile を対象 version の `mayapy` でロードします。
2. version 固有 plugin が追加・廃止された場合だけ、`profile_plugin_requests()` の差分を
   明示します。
3. 登録 node、生成可能 node、skip node の inventory 件数を記録します。
4. 直前 version との比較から、追加、廃止、schema 変更 node を分類します。
5. `INTRODUCED_NODE_TYPES_BY_VERSION`、`REMOVED_NODE_TYPES_BY_VERSION`、
   `SCHEMA_CHANGED_NODE_TYPES_BY_VERSION` を更新します。
6. 追加・廃止境界を独立した runtime registry にも反映します。

固定 profile の plugin を1つでもロードできない場合は生成を中止します。その状態の
inventoryを正規snapshotとして採用しません。

### 4. sparse overlay と補完 stub を生成する

対象 version の `mayapy` から version schema CLI を実行します。具体的なコマンドは
[Generator](generator.md)を参照してください。

生成後は、基準 snapshot 全体が複製されていないこと、追加 node と変更 node だけが
新overlayへ出力されていることを確認します。新規 node には public wrapper が必要です。

続いて Maya 2025 の `mayapy` から `generate_existing_node_stub.py` を実行し、7つの
registry / stub 生成物を更新します。生成後に `--check` を実行し、ASTとして最新である
ことも確認します。

### 5. contract と件数を更新する

1. `test_version_schema.py` の profile、inventory、追加・廃止・変更・生成件数を更新します。
2. `test_node_types.py` の version 別 class 件数を更新します。
3. `test_maya_version.py` にoverlay検索順、追加・廃止 node、変更attributeの代表例を
   追加します。
4. `node_operator_maya_version_contract.py` に新しい `typing_maya_version` を追加します。
5. IDE contract には、少なくとも追加node、前versionから継続するnode、廃止node、
   schema変更attributeのpositive / negative例を1つずつ含めます。
6. concrete shape が増減した場合は、`dag/shape/test_generated.py` のpublic wrapper件数と
   `creator/_shape_types.py` の作成確認済み一覧を更新します。

negative例は、対象外versionでアクセスできないことを
`# pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]` で固定します。
`reportUnnecessaryTypeIgnoreComment` により、誤って補完面へ混入した場合も検出できます。

### 6. 受け入れ確認を行う

開発中は新versionのtargeted testとfull pytestを先に実行します。最終確認は統一入口を
使用します。

```powershell
.\scripts\typecheck-maya-all.cmd
.\scripts\test-pytest-maya<version>.cmd
.\scripts\verify.cmd -IncludeNative
```

リリース前は、全versionのstaged native plug-inを必須にしたfull pytestを実行します。

```powershell
.\scripts\verify.cmd -Release
```

schema生成が成功しただけでは対応完了としません。runtime、補完、native build、
version別full pytest、UI互換性、配布先 `.mll` まで成功して完了です。

## 差分確認時の注意

- 新overlayが想定より大きい場合は、まずplugin profileとロード成否を確認します。
- attributeの追加・削除だけでなく、型、default、min / max、writableなどの変更も
  schema差分です。
- 前versionのoverlayにあるclassが新versionでも変更される場合、新overlayは前versionの
  schemaを継承元として積層されます。
- `_generated`、`_generated_maya<version>`、`node_attr_maya<version>` は生成元を修正して
  再生成します。
- public wrapperはgeneratorが上書きしません。node固有の手書きAPIはwrapper側へ置きます。
- Maya / MtoA終了時のwarningは、pytestの終了codeが成功なら通常は非失敗ログです。
