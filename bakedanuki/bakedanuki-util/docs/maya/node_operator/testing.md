# Testing

このプロジェクトでは、通常の検証を `pytest` に寄せます。

既存の `_test` 配下は、速度計測や手動確認用として残します。

## 推奨実行方法

最終検証は統一入口から実行します。

```powershell
.\scripts\verify.cmd
```

通常modeでは次を順に実行し、途中の失敗で停止します。

1. Black format check。
2. Maya 2025 / 2026 / 2027のPyright型contract。
3. Maya 2025のfull pytest。
4. Maya 2025 / 2026 / 2027のUI互換性test。
5. `git diff --check`。

native変更とリリース前の検証です。

```powershell
.\scripts\verify.cmd -IncludeNative
.\scripts\verify.cmd -Release
```

`-IncludeNative`は通常modeに3 versionのnative build/testを追加します。
`-Release`はその全項目に加えて、各versionのstaged plug-inを必須にしたfull pytestを
実行します。個別scriptは開発中の切り分け用で、最終確認では`verify.cmd`を使用します。

pytestは`requirements-test.txt`に固定し、repository直下の`.test`へtarget installします。
`verify.cmd`は環境がない場合に自動作成します。手動で作成・再作成する場合です。

```powershell
.\scripts\setup-test.cmd
.\scripts\setup-test.cmd -ForceRecreate
```

Maya 2025を基準にfull pytestまたはtargeted pytestだけを切り分ける場合です。

```powershell
.\scripts\test-pytest-maya2025.cmd
.\scripts\test-pytest-maya2025.cmd tests/maya/node/operator/attr/test_extra_attr.py
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

`tests/typecheck/node_operator_contract.py` と
`tests/typecheck/node_operator_maya_version_contract.py` は、公開 API を利用したときに
Pyright が解決する型を `typing.assert_type()` で固定します。

現在は次の経路を検証します。

- `nodes.create` / `nodes.existing` の具体的な node 戻り値型。
- `typing_maya_version="2025" / "2026" / "2027"` ごとの `nodes.create` /
  `nodes.existing` / `nodes.types` の候補とversioned attribute schema。省略時は
  3 version共通面と共通型を検証します。
- `AttributeField` の class access と instance access。
- compound child と alias の具体的な plug 型。
- enum plug と enum 定数。
- `multi[index]` / `multi[next]` の具体的な plug 型。
- `get()` の値型。
- `get()` / `set()` / `set_direct()` / `round()` が対応するplug型だけに存在すること。
- scalar plugの`keyframe.set_key()` / `set_keys()` / `insert_key()`、tangent変更・削除、
  変更methodの`None`戻り値とqueryの型。`set_keys()`の`(frame, value)` iterable入力と
  tangent引数、`get_keys()`の`list[tuple[float, float]]`戻り値の型。
- `get_key_data()` / `get_curve_data()`の範囲指定、`include_boundaries`、戻り値型。
  KeyDataの直接編集、JSON変換、`set_key_data()` / `set_curve_data()`、weighted操作の型と、
  廃止した`set_key_data(weighted=...)`引数の拒否。
- 単体`KeyframeManager`の`modifier_manager`引数と、廃止した`keyframe.set_direct()` /
  `keyframe.insert_direct()`および旧名`keyframe.set()` / `keyframe.insert()`の非公開。
- `nodes.types`から取得するNodeOperator classと、DAG traversalの
  `filter_type`に応じた具体的なtuple要素型。
- `ancestors(until=...)` / `descendant_chain(until=...)`の、引数省略時と
  境界指定時で異なるoptional戻り値型。
- 存在しない属性や不正な引数が型エラーになること。

型エラーになるべき行は、対象の diagnostic rule を
`# pyright: ignore[...]` で指定しています。
`pyrightconfig.json` の `reportUnnecessaryTypeIgnoreComment` を有効にしているため、
誤用が型エラーにならなくなった場合も contract failure になります。

Maya API stub はリポジトリの `typings/maya` に同梱しています。
`pyrightconfig.json` の `stubPath` を通して Pyright / Pylance から参照されるため、
開発環境ごとに `maya-stubs` をインストールする必要はありません。

Pyright CLIはMaya環境へ常設せず、repository直下の`.typecheck`へ
target installします。初回だけ次を実行してください。

```powershell
.\scripts\setup-typecheck.cmd
```

通常開発ではMaya 2025を基準に実行します。

```powershell
.\scripts\typecheck-maya2025.cmd
```

Maya同梱のPySide6 stub差分も含めて対応versionを一括確認する場合は、
次を実行します。

```powershell
.\scripts\typecheck-maya-all.cmd
```

versionごとのscriptとして`typecheck-maya2025.cmd`、
`typecheck-maya2026.cmd`、`typecheck-maya2027.cmd`も使用できます。
各scriptは対象versionの`mayapy.exe`をPyrightの`--pythonpath`へ指定します。
期待する結果はそれぞれ `0 errors, 0 warnings, 0 informations` です。

型チェック環境が起動できない場合は、明示的に作り直します。

```powershell
.\scripts\setup-typecheck.cmd -ForceRecreate
```

このcontractは静的解析用で、Maya sceneを作成するruntime testではありません。
`typing_maya_version` は実行時には破棄され、実行Mayaの選択、version不一致検査、
node availabilityの変更には使われません。
runtime挙動は各versionの`.\scripts\test-pytest-maya2025.cmd`、
`.\scripts\test-pytest-maya2026.cmd`、`.\scripts\test-pytest-maya2027.cmd`で検証します。

### 実装ファイルの診断確認

`pyrightconfig.json` の既定の `include` は `tests/typecheck` です。
これは通常実行を公開 API の型・補完 contract に限定するための設定で、
`bd_util` の全実装を自動的に総点検する設定ではありません。

実装ファイルや特定階層の Pylance 警告を調べる場合は、同じ設定と Maya interpreter を
使い、対象 path を明示します。例えば `_test` 全体を確認する場合は次の通りです。

```powershell
.\scripts\typecheck-maya2025.cmd bakedanuki/bakedanuki-util/python/bd_util/_test
```

Mayaの解析interpreterを指定せずに通常のPythonやNode.js版Pyrightを実行すると、
stubは見つかっていてもMayaの実module sourceを解決できず、
`reportMissingModuleSource`が出ることがあります。
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
- `tests/maya/node/test_maya_version.py`
  - 実行中Mayaからのmajor version判定、sparse overlayの検索順、version固有nodeの
    availability、変更されたattribute schemaが実行Mayaへ追従することを検証します。
  - `typing_maya_version`を指定しないruntime経路で、新旧nodeの作成可否も検証します。
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
  - `ufeProxyTransform` / `unknownTransform` もMaya上で作成し、具体型解決と
    runtime-defined `ufePath` の静的fieldを検証します。
  - `unknownDag` もMaya上で作成し、`UnknownDag` への具体型解決、自動作成される
    親`Transform`、同じ`ModifierManager`の共有を検証します。
- `tests/maya/node/creator/test_node_creator.py`
  - node 作成、nodeType 解決、補完用 node 名を検証します。
  - concrete transform class が存在しても、allowlistにないtypeは
    `nodes.create` へ公開しないことを検証します。
  - `unknownDag` の具体classを解決できても、汎用DAG作成APIには公開しないことを
    検証します。
- `tests/maya/node/creator/test_shape_with_transform.py`
  - transform と shape の一括作成、命名、親子関係、undo / redo を検証します。
- `tests/maya/node/modifier/test_modifier_manager.py`
  - DG / DAG modifierと`MAnimCurveChange`の実行順・undo / redoを検証します。
  - animation callbackが初回だけ実行されること、同じ実行境界の部分変更の復元、
    それ以前に成功した履歴の維持、pending操作の破棄を検証します。

### Attribute と Plug

- `tests/maya/attr/test_query.py`
  - Maya attribute 情報の取得と fallback を検証します。
- `tests/maya/node/operator/attr/test_extra_attr.py`
  - extra attribute の追加、型解決、値設定を検証します。
- `tests/maya/node/operator/attr/test_channel_state.py`
  - scalar / scalar compoundのChannel Box 3状態、全plug型のlock / unlock、
    queued / directの反映時期、undo / redo、compound child展開、multi element制約、
    呼び出し順、作成予約中nodeへの適用を検証します。
- `tests/maya/node/operator/attr/test_plug_capabilities.py`
  - 値操作、Channel Box公開状態操作、lock操作が、対応する具象plug型だけの
    runtime APIとして現れることを検証します。
- `tests/maya/node/operator/attr/test_keyframe.py`
  - `keyframe.set_key()`の実行、animCurve作成、query、単体MPlugからの使用、
    Maya標準のtangent挙動と予約方式の挿入・削除・tangent操作を検証します。
  - 対象がない場合の挿入エラーと編集・削除のno-op、カーブ全体の削除、
    `None`戻り値を検証します。
- `tests/maya/node/operator/attr/test_keyframe_undo.py`
  - 予約、既存キー更新、undo / redo、作成・改名待ちのplug、queryの再探索、
    角度・距離・時間の単位変換と予約後の単位変更を検証します。
  - 挿入・tangent変更・キー削除のundo / redo、共有カーブ削除の拒否、同じ予約列の
    設定から編集への順序、不正な引数やキーを設定できない場合のエラー、
    部分変更の復元も検証します。
  - キー削除後の空カーブ保持と、manager必須の変更操作を検証します。
- `tests/maya/node/operator/attr/test_keyframe_set_backend.py`
  - 初回カーブ作成のcmds経路と後続キーのAPI経路、予約した再接続・カーブ削除後の
    経路の再判定、unitConversionのある接続へのcmds委譲を検証します。
  - API / cmdsの途中失敗で同じ実行境界の変更を戻し、Undo / Redoでは初回の
    callbackを再実行しないことを検証します。
- `tests/maya/node/operator/attr/test_keyframe_set_equivalence.py`
  - numeric / unit / bool / enum属性で、公開`set_key()`と`cmds.setKeyframe()`の結果を比較します。
    weighted tangent、単位変更、breakdown、tangent lock、カーブのinfinity設定を含め、
    追加・上書きとUndo / Redo後の状態を検証します。
- `tests/maya/node/operator/attr/test_keyframe_set_keys.py`
  - `set_keys()`と`set_key()`の順次呼び出しを、未整列・重複時刻を含む入力で比較します。
    `(frame, value)`のpair列の捕捉、呼び出し入口の単位、空入力、不正な入力やgeneratorの失敗で
    バッチの一部を予約しないことを検証します。
- `tests/maya/node/operator/attr/test_keyframe_set_keys_backend.py`
  - バッチ内のカーブ取得・経路判定の再利用、新規作成後のAPIへの切り替え、bool・
    unitConversion・共有カーブ・layerでのcmds委譲を検証します。
  - API編集・再判定・後続cmdsの途中失敗で先行する変更を戻し、Undo / Redoでは
    初回のcallbackを再実行しないことを検証します。
- `tests/maya/node/operator/attr/test_scalar_sampling.py`
  - scalarの`sample_values()`の入力順・重複、型別の公開単位、UI単位変更、
    generatorの捕捉、不正入力、空入力、multi要素を検証します。
  - constraint・計算ノード・unitConversion・layer合成後の評価値と、
    constraint削除後の再キー設定からUndo / Redoまでを検証します。
  - 現在時刻・Undo履歴・保留中modifierを変更しないことと、ネストした評価時刻からの
    呼び出しや途中例外でも、元の評価コンテキストへ復帰することを検証します。
- `tests/maya/node/operator/attr/test_scalar_sampling_layers.py`
  - native / 本パッケージによる加算・Override layerの作成と初回キー設定直後に、TL / TA / TUの
    最初の1点・複数時刻・重複・範囲外のサンプルが正しい合成値になることを検証します。
  - キー再設定とUndo / Redo、weight・muteの変更、未接続の計算出力、driven curve越しの
    上流依存関係、lock・referenceされた対象の読み取りを確認します。
  - 正常時・例外時の外側の評価コンテキスト、現在時刻・選択・modified flag・Undo / Redo・
    保留中modifierとカーブデータの保持を検証します。無関係なノードへのdirty通知がないこと、
    空入力・不正入力でキャッシュを無効化しないことも対象です。
- `tests/maya/node/operator/attr/test_keyframe_data.py`
  - KeyData / AnimCurveDataのJSON往復、接線type・XY・lock・breakdown、weightedと
    infinity、単位・FPS変更後の復元を検証します。
  - 新規・既存・空カーブ、部分上書き、保留中の処理順、反復Undo / Redo、
    復元途中の失敗と既存履歴の保持を検証します。
  - キー間と範囲外の評価値、未対応接続・lockの拒否、layer付き属性のベース取得・復元、入力検証も対象です。
  - 変更可能なKeyDataの予約時再検証・コピー、予約後の編集、weighted間の適用と
    Maya標準変換の比較、未対応schemaの拒否、weighted取得・変更のUndo / Redoを検証します。
  - `tests/maya/mpx_cmd/test_command.py`では、カーブ復元・部分キー編集・weighted変更を
    1 commandとして実行し、MayaのUndo / Redoと失敗時rollbackも確認します。
    未接続・直接接続・pairBlend越しの復元と、layer上のベースカーブ自動作成も対象です。
- `tests/maya/node/operator/attr/test_keyframe_restore_creation.py`
  - ベース・明示ベース・加算・Override layerの未作成カーブへ、TA / TL / TUの詳細データを復元します。
    全置換・部分適用・空カーブでの作成、内部の仮キー除去、空キー列のno-opを検証します。
  - weightedの形状・単位、weightが0・mute時の生値復元、既存の手動キーを残す部分適用、
    同じbatchでのlayer作成・add_nodes / add_plugs・改名・復元を確認します。
  - ノード・接続・別軸・別layer・選択・現在時刻・履歴・保留中queryの保持、反復Undo / Redo、
    復元途中・後続失敗のrollback、実行時のlockと未登録属性の拒否を検証します。
  - constraint・driven key・空入力のpairBlend・blendWeightedを自動で組み替えないことを、
    layerなし・無関係なlayer・layer入力側の構成で確認します。
- `tests/maya/node/operator/attr/test_keyframe_clip.py`
  - 境界補完の既定値、既存キーだけの取得、片側範囲・同一境界・空カーブ・単一キーを検証します。
  - weighted / nonweighted、接線各種、単位・FPS、constant / linearの範囲外、
    cycle系の範囲外の拒否、JSON復元後の区間内評価値と反復Undo / Redoを検証します。
  - 元カーブ・scene node・選択・現在時刻・Undo / Redo・保留中処理・modified flagの保持と、
    成功・例外時の作業用カーブの解放を検証します。
- `tests/maya/node/operator/attr/test_keyframe_get_keys.py`
  - 実在キーの昇順取得、範囲の両端包含・片側指定・非キー端点、カーブ無し・空カーブ・
    カーブの有無によらない不正範囲の拒否を検証します。
  - TA / TL / TU / TTの公開単位、bool / enumもfloatのpairで返すこと、UI単位変更、
    `set_keys()`との往復と、予約を実行しないsnapshot取得を検証します。
  - カーブ型から単位を換算することと、constraintのdriverのキーを取得しないことを検証します。
- `tests/maya/node/operator/attr/test_keyframe_target.py`
  - query・挿入・削除・weighted操作で共通のチャンネル選択ルールを検証します。
    unitConversion・pairBlend・時間入力接続・無関係なlayerを許可し、driven keyやconstraintの
    driverを対象から除外します。共有出力、quaternion補間を拒否し、layer付き属性はベースを選びます。
  - queryと編集のlock / reference制約の違い、実行時の再接続、set→query→editの対象一致、
    Undo / Redoと同じbatchの先行変更のrollbackを検証します。
  - キー配列のelement・value・tangent、sparseな追加配列とcompoundの子属性について、
    予約後のlockを検出し、解除後には復元できることを直接接続・layer付き属性で確認します。
- `tests/maya/node/operator/attr/test_keyframe_channel.py`
  - Mayaがconstraint用に作るpairBlendでtranslate / rotateの全6軸を検証します。
    別軸・constraint driver・blend weightを変えず、取得・編集・削除・詳細復元を行います。
  - currentDriverとMayaのquery / setKeyframeの対象一致、blendWeightedのsparse入力index順、
    driven keyを通り越さないこと、単位変換係数のカーブを編集しないことを確認します。
  - 空カーブの取得・復元、入れ子のblend、保留中の接続変更、予約後の対象変更、
    Undo / Redoと失敗時rollback、対象のない復元で既存接続を保つことを検証します。
  - queryがscene、選択、現在時刻、Undo / Redo、modifier、modified flagを変更しないことと、
    未対応utilityで軸を推測せずエラーにすることを確認します。
- `tests/maya/node/operator/node/dg/test_anim_layer.py`
  - ベースと加算・Override layerの作成、rootの改名・名前衝突、複数layerでのroot共有、選択の保持を検証します。
  - 作成・weight設定・add_plugs / add_nodes・キー設定を1回のdo_it_dgで実行し、Undo / Redoを2往復します。
    作成待ちqueryは実行しないこと、TL / TA / TUの生カーブ値がnative操作と一致することを確認します。
  - PlugOperator / MPlug / 名前、NodeOperator / MObject / 名前、compound・sparse配列・非keyable、
    ノード自身のkeyable属性・dynamic属性と非対象の子孫・shape、byte / char等の除外を検証します。
  - 予約後の入力列変更、改名、ノード・属性の削除と同名再作成、同名DAG、作成待ちDGとdynamic属性、
    lock / reference、既存登録と重複、native失敗・黙示的な登録見送り・後続失敗でのrollbackを確認します。
  - `tests/maya/mpx_cmd/test_command.py`ではlayer作成・登録・キー設定のコマンド単位のUndo / Redoと、
    実行後失敗によるrollbackを検証します。評価時刻はMAnimControlで変え、検証自体でcmds.currentTimeの
    Undo履歴を追加しないようにします。型補完は共通・3 versionのnode_operator contractが対象です。
- `tests/maya/node/operator/attr/test_keyframe_anim_layer.py`
  - `anim_layer()`が元のmanagerを変更せず、plugとModifierManagerを共有することを検証します。
    BaseAnimation、加算・上書きlayer、登録済み属性、未作成・空カーブの対象解決を確認します。
  - layerを明示したMayaのキー設定と、生カーブの取得・挿入・接線・削除・weighted・詳細復元を
    検証します。別layer・別軸のカーブを保持し、合成値と生カーブ値を区別します。
  - layer名の入力検証、改名後の同一性、同名再作成、登録解除、lock / referenceの再検査と、
    保留中modifierをqueryで実行しないこと、変更のUndo / Redo・失敗時rollbackを確認します。
  - カーブ未作成時の詳細復元と所属の保持、find_anim_curvesの候補がlayer指定で絞り込まれないことを
    確認します。同名DAG・alias・sparse配列要素の区別と、pairBlendを併用した軸の選択も対象です。
    返却型と操作methodの補完は`node_operator_contract.py`で検証します。
  - `tests/maya/mpx_cmd/test_command.py`ではカーブ未作成のlayerへ直接、詳細復元・
    weighted変更・挿入・削除を1 commandで実行し、MayaのUndo / Redoと失敗時rollbackを確認します。
- `tests/maya/node/operator/attr/test_keyframe_default_layer.py`
  - layer未指定のキー設定・取得・挿入・接線変更・削除・詳細データ・weighted操作が
    ベース（root）layerを対象とすることを検証します。別layer・別軸・weightを保持します。
  - 選択layer・preferredと3種類のkeying modeからの独立、rootの改名、予約後のlayer作成と選択変更、
    layerなし・未所属属性、未作成・空のベースカーブ、lockの検査を確認します。
    無関係なlayerがあるsceneで、未所属のbool / enum / time属性へのキー設定も検証します。
  - カーブ未作成時の詳細復元とqueryの保留、Undo / Redo・途中失敗時rollback、
    queryの副作用がないこと、sample_valuesの合成値の保持を確認します。
- `tests/maya/node/operator/attr/test_curve_keyframe.py`
  - TA / TL / TUノードの明示指定、作成待ちqueryの拒否、改名・再接続・削除時のnode同一性、
    公開単位と予約時の時間単位、共有出力・時間入力・message接続を検証します。
  - 詳細データ・境界補完・JSON復元の共通処理、入力コピー、元カーブとmodified flagの保持、
    lock / referenceの再検査、全接続の削除前検査、反復Undo / Redoと失敗時rollbackを確認します。
  - layer内の生カーブ値と合成値を区別し、所属layerのlockを尊重します。
  - `tests/maya/mpx_cmd/test_command.py`は明示カーブの復元・weighted・キー編集を
    MayaのUndo / Redoと例外時rollbackで検証します。補完は`node_operator_contract.py`が対象です。
- `tests/maya/node/operator/attr/test_keyframe_discovery.py`
  - 全8型の具体wrapper、型filter、名前順、共有候補の重複排除と、driven key / time driverを
    通り越さない探索を検証します。layerのbase・加算・weight、mute / lock、constraint、
    world-space依存、別軸入力とmessage接続の扱いも確認します。
  - 未接続出力の依存入力補完、sparse array indexの区別と要素数の保持、scene / 時刻 /
    選択 / Undo / modifierへの副作用がないこと、改名・再接続後の明示編集を検証します。
    型filterと返却型、`.keyframe`の補完は`node_operator_contract.py`で検証します。
- `tests/maya/node/operator/attr/test_data_matrix.py`
  - typed matrix plugと`TransformMatrix`の連携、常に具体型を返す`get()`、
    未設定時の`ValueError`、分解値のcompound専用値型、flat 16要素 / 4行4列の
    sequenceによるdirect設定を検証します。
- `tests/maya/node/operator/attr/test_matrix_attr.py`
  - matrix plugの`TransformMatrix`取得と、`TransformMatrix` / `MMatrix` /
    `MTransformationMatrix` / matrix sequenceによるqueued値設定を検証します。
- `tests/maya/value/test_scalar_compound.py`
  - compound 専用値型の immutable sequence、component access、型ごとの
    equalityを検証します。
  - 浮動小数点numeric値型の同型加減算、scalar乗除算、符号反転、元の値の不変性、
    exactな戻り値型と、cross-type・要素積・unit / 整数値型の非対応境界を検証します。

### NodeOperator

- `tests/maya/node/operator/node/dg/test_plus_minus_average.py`
  - scalar / multi plug、alias、接続、enum 操作を検証します。
- `tests/maya/node/operator/node/dg/test_wt_add_matrix.py`
  - compound multi plug と次の空き logical index への接続を検証します。
- `tests/maya/node/operator/node/dag/test_parent.py`
  - DAG の親子操作、undo / redo、循環する親子関係の防止を検証します。
- `tests/maya/node/operator/node/dag/test_traversal.py`
  - `children()`の直接の子、child index順、Transform / Shape / `UnknownDag`の
    具体型解決、`ModifierManager`共有、未実行modifier、instancingを検証します。
  - `children()` / `descendants()`のShape除外、class-based type filter、
    派生classを含む判定と完全一致判定、filterを理由に探索範囲を狭めないことを
    検証します。
  - `ancestors()`の直接親からrootへの順序、world除外、具体型解決、未実行modifier、
    cacheなし、instanced nodeで保持pathを基準にすること、type filterを検証します。
  - `descendants()`のdepth-first pre-order、Transform / Shape / `UnknownDag`の
    具体型解決、未実行modifier、cacheなし、instanced subtreeのpath別再訪を検証します。
  - `descendant_chain()`が各階層で同じchild indexだけを選び、別indexへfallbackせず、
    TransformとShapeを区別しないことを検証します。
  - `ancestors()` / `descendant_chain()`の`until`境界がinclusiveであること、
    `MObject` identityによる比較、境界未発見時の`None`、未実行modifierを境界として
    認識しないことを検証します。
- `tests/maya/node/operator/node/dag/test_matrix.py`
  - DAG 間の relative / local matrix 計算を検証します。
- `tests/maya/node/operator/node/dag/transform/test_rotation.py`
  - Transform / Jointの回転集約と姿勢維持した回転値設定、全rotateOrderでの
    local matrix維持、undo / redo、lock・入力接続・keyframeの拒否を検証します。
- `tests/maya/node/operator/node/dag/transform/test_matching.py`
  - Transform / JointのDAG原点とworld姿勢のマッチ、world / local / objectの
    軸指定、offsetParentMatrix、全rotateOrder、undo / redo、lock・入力接続、
    shape source、instanced DAGの拒否、非ゼロrotatePivotでdst自身の位置を補償しない
    ことに加え、直接の子のworld姿勢・位置補償、Joint子の`rotate` /
    `jointOrient`選択、既定の非補償、no-op、非可逆な実効親行列の拒否、
    変更予約前の原子的な検証を検証します。
- `tests/maya/node/operator/node/dag/transform/test_aim.py`
  - Transform / Jointの属性別エイム姿勢設定について、Transform系operator／名前／座標の
    ターゲット、world / local座標、任意のエイム／アップ軸、アップ省略時の最短回転、
    rotate pivot、offsetParentMatrix、全rotateOrder、undo / redo、lock、
    instanced DAG、子補償を検証します。
  - 直接子エイムについて、Shapeを除外したTransform系子index、全直接子のworld姿勢・
    位置補償、親空間アップ方向、既定のエンド親合わせ、エンドのエラー選択、Joint子の
    既定`jointOrient`補償、入力エラー時の原子性を検証します。
- `tests/maya/node/operator/node/dag/transform/test_axis_remap.py`
  - 処理前の正軸から処理後の符号付き軸への対応方向、2軸から決定する右手系、属性別の
    `rotate` / `rotateAxis` / `jointOrient`設定、全rotateOrder、offsetParentMatrix、
    undo / redo、lock、no-op、子のworld姿勢・位置補償を検証します。
  - 3種類の処理前軸pair、処理後軸の全順列、全符号を組み合わせた72通りと、指定数、
    重複軸、未対応文字列、子補償optionの入力エラーを検証します。
- `tests/maya/node/operator/node/dag/transform/test_transform_round.py`
  - Transform / Jointの階層補償付き`translate` / `rotateAxis` / `rotate` /
    `jointOrient`丸め、
    補償ON / OFF、姿勢のみ／位置を含む補償、Joint子の`rotate` / `jointOrient`
    選択、全rotateOrder、pivot、offsetParentMatrix、非一様scale / shear、
    undo / redo、lock・入力接続、instanced DAG、`inheritsTransform=False`を
    検証します。
- `tests/maya/node/operator/node/dag/transform/test_transform_set.py`
  - Transform / Jointの`translate` / `rotateAxis` / `rotate` / `jointOrient`設定、
    sequence / 3 scalar入力、local / world空間、全rotateOrder、offsetParentMatrix、
    非一様scale / shear、既定の非補償、world姿勢のみ／位置を含む補償、Joint子の
    補償属性選択、ジンバルロック条件でのquaternion等価性、undo / redo、instanced DAGと
    非可逆な実効親行列の拒否、変更予約前の原子的な検証を検証します。
- `tests/maya/node/operator/node/dag/shape/test_create.py`
  - 親 Transform 必須の shape 作成、明示的な公開対象、同一 modifier での
    一括作成、undo / redo を検証します。
- `tests/maya/node/operator/node/dag/shape/test_generated.py`
  - concrete shape 81種の public / generated module 対応と import を検証します。
- `tests/maya/node/operator/node/test_process_speed.py`
  - Maya バージョンに応じた PyMEL 比較ベンチマークの実行可否を検証します。

### TransformMatrix

- `tests/maya/transform/matrix/test_transform_matrix.py`
  - matrixの入力、flat 16要素 / 4行4列のsequenceと形状検証、snapshot、
    keyword-only componentの既定値・部分指定・入力検証、回転順序名とMaya indexによる
    全Euler回転順序 / quaternionでの`composeMatrix` nodeとの等価性、compound専用値型に
    よる分解、`MMatrix`を含む左右の乗算、逆行列を検証します。

### Quat

- `tests/maya/value/test_quat.py`
  - identity / component / sequence / `MQuaternion` constructorとsnapshot、
    回転順序名とMaya indexによる全Euler回転順序、axis-angle、2-vector、matrixとの
    相互変換、raw lengthと状態照会、
    `MQuaternion`と一致する左右の積・逆元・共役・正規化・符号反転・slerp、
    raw equalityと`q` / `-q`の等価性、zero Quaternionの境界挙動を検証します。
- `tests/maya/value/test_scalar_compound.py`
  - `Quat`が`Double4`の派生型ではないことと、numeric値型のcomponent-wise演算が
    `Quat`へ波及せず、Quaternion積だけを維持することを検証します。

### 開発用 generator

- `tests/dev/maya/node/operator/node/test_generate.py`
  - AttributeField と内部 `_generated` package の生成 NodeOperator、公開 wrapper の生成・保護、安全でない nodeType の除外を検証します。
  - transform / shape のattribute queryが調査用node instanceを作らず、
    登録済みnode typeから静的に取得されることを検証します。
  - concrete transform のnative基底が生成済みの場合、そのclassを継承して
    基底attributeを重複生成しないことを検証します。
- `tests/dev/maya/node/operator/node/test_generate_existing_node_stub.py`
  - `nodes.create` / `nodes.existing` / `nodes.create.with_transform` の型情報と、
    raw作成を公開するtransform系メソッドのstub生成結果を検証します。
- `tests/dev/maya/node/operator/node/test_version_schema.py`
  - 固定plugin profile、version別inventory、生成対象数、availability registryとの同期、
    Maya 2025のbaseline追加node、Maya 2026 / 2027の物理overlay全体を検証します。

version schemaとoverlayだけを切り分ける場合は、次を実行します。

```powershell
.\scripts\test-pytest-maya2025.cmd `
    tests\dev\maya\node\operator\node\test_version_schema.py
```

### DAG traversal変更時の検証

DAG traversalは共通の`DAG`基底実装と、公開APIのoverloadを同時に変更する可能性が
あります。変更時は少なくとも次を確認します。

```powershell
.\scripts\test-pytest-maya2025.cmd `
    tests\maya\node\operator\node\dag\test_traversal.py
```

- Maya上の列挙順、具体型解決、`ModifierManager`共有、instancing、実行済みscene状態は
  `test_traversal.py`で固定します。
- filter追加・変更では、filter対象外nodeを探索経路として残すかを明示的に検証します。
- `until`などで戻り値がoptionalになる場合は、境界発見と結果filteringを分離し、
  空tupleと`None`の意味を混同しないtestを追加します。
- 引数や戻り値型を変更した場合は`tests/typecheck/node_operator_contract.py`も更新し、
  `.\scripts\typecheck-maya2025.cmd`を実行します。
- `DAG`基底の共有実装を変更した場合は、targeted pytestとPyrightに加えてfull pytestを
  実行します。

`.\scripts\test-pytest-maya2025.cmd`では、上記のMaya実行テストと開発用generator
テストをまとめて実行します。最終確認は`.\scripts\verify.cmd`から実行します。

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
- 値操作methodが対応するplug型だけに存在し、未対応型と共通基底には存在しない。
- `round()`がPythonと同じ偶数丸め、正負の`ndigits`、unit型の公開単位、
  compound専用値型、ModifierManagerのundo / redoを維持する。
- typed dataのdefault値が現在値だけでなく`MFnTypedAttribute.default`にも保持され、
  空文字列などのfalseyな値も失われない。
- wrong count などの error が期待通り発生する。
- DAG の親子操作が undo / redo に対応し、循環する親子関係を作らない。
- `TransformMatrix`とmatrix plugが同じ行列値を扱い、分解値の具体型と単位が
  対応するplugの`get()`と一致する。
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

## KeyframeManagerの引き継ぎ時点の検証

2026-09-14、`dc4fa1ee`（レイヤー対応後の性能測定と高速化）までの実装で、
次を確認済みです。利用者によるMaya上での動作確認とcommit / pushも完了しています。
この記録は過去の検証結果で、新しい実装変更の最終検証を代替するものではありません。

| 確認内容 | 結果 |
| --- | --- |
| attr・MPxCommand・AnimLayerの関連pytest | Maya 2025 / 2026 / 2027で各1,542件成功 |
| `scripts/verify.cmd` | 成功。Black、3 versionの型・補完contract、Maya 2025 full pytest、3 versionのUI互換性、差分確認を含む |
| 上記のMaya 2025 full pytest | 3,912件成功、130件skip |
| `_keyframe_target.py`・`benchmark_keyframe_data.py`を明示した型チェック | 3 versionともerror / warningなし |
| 詳細データbenchmarkの最終smoke | 3 versionでTA / TL / TU、weighted / nonweighted、直接接続・ベース・加算・Overrideの取得・復元・JSONを確認 |

関連pytestの実行範囲です。Maya 2026 / 2027も同じ引数を対応versionのscriptへ渡します。

```powershell
.\scripts\test-pytest-maya2025.cmd tests\maya\node\operator\attr tests\maya\mpx_cmd tests\maya\node\operator\node\dg\test_anim_layer.py -q --tb=short
```

## 範囲内キーの接線変更の検証

`set_tangents()`は、既存`set_tangent()`の単一時刻と同じ対象選択・編集履歴を使用し、
次の契約を検証します。

- 両端包含、片側省略、全キー、負時刻・subframe、範囲端にキーがない場合もキーを挿入しないこと。
- `tangent_type`によるin / out共通指定、個別側の上書き、片側だけの変更、
  全指定省略・カーブなし・該当キーなしのno-op。単数版の接線引数がkeyword専用であること。
- 値・時刻・breakdown・tangent / weight lock・weighted・infinityと範囲外キーを維持すること。
  type変更による接線XYの再計算と、lockしたキーの片側変更はMaya標準動作に従うこと。
- 予約時のUI時間単位、同一batchで先行予約したキー、予約後の再接続・改名を初回実行時に解決すること。
- 既定ベース・明示layer・明示TA / TL / TUカーブ、通常の上流チャンネル、lock / referenceの拒否。
- 反復Undo / Redo、MPxCommandのMaya標準履歴、同一batchの途中失敗時rollback。
- 逆転範囲・非有限時刻・未対応tangent typeを予約時に拒否し、部分予約を残さないこと。
- 属性・layer・明示カーブの3入口から引数と`None`の戻り値をIDE補完で追えること。

開発中の局所確認には、`test_keyframe.py` / `test_keyframe_undo.py` /
`test_keyframe_target.py` / `test_curve_keyframe.py`とMPxCommand testを使用します。

2026-09-20、範囲接線変更追加後の検証結果です。

| 確認内容 | 結果 |
| --- | --- |
| attr・MPxCommand・AnimLayerの関連pytest | Maya 2025 / 2026 / 2027で各3,377件成功、プロセス正常終了 |
| 変更実装と型・補完contractの明示Pyright | Maya 2025でエラー・警告0件 |
| 3 versionの型・補完contract | Maya 2025 / 2026 / 2027ですべてエラー・警告0件 |
| `scripts/verify.cmd` | `QT_QPA_PLATFORM=offscreen`で成功。Black 4,473ファイル、3 versionの型・補完contract、Maya 2025 full pytest、3 versionのUI互換性、差分確認を含む |
| 上記のMaya 2025 full pytest | 6,765件成功、632件skip |
| 上記のUI互換性 | Maya 2025 / 2026 / 2027で各Qt/UI 726件・Maya UI 244件成功 |

範囲接線変更の利用者によるMaya画面上での確認とcommit / pushも完了し、
`3509264f`へ反映されています。

## node・複数nodeの接線変更の検証

`test_node_keyframe_tangent.py`では、`node.keyframes.set_tangents()`と
`nodes.keyframes.set_tangents([...])`の次の契約を検証します。

- keyable属性の自動収集、明示属性、既存カーブ・既存キーだけの変更と静的属性のno-op。
- 通常の接線指定を連続属性だけへ適用し、離散属性は既定で維持すること。
  `discrete_tangent_type`を明示するとin / out両側を同じtypeへ変更すること。
- 複数nodeでは属性が存在するnodeだけへ適用し、全nodeにない名前、重複・空node列を拒否すること。
- root / 明示layer、lock / reference / 未所属・未対応接続の検査、全対象のUndo / Redo・rollback。
- 両端包含、片側省略、全キー、負時刻・subframe、予約時のUI時間単位と作成待ちnode / layer。
- `NodeKeyframeManager` / `NodesKeyframeManager`の公開引数と戻り値をIDE補完で追えること。

## キー単位のtangent / weight lock変更の検証

`test_keyframe_lock.py`と`test_node_keyframe_lock.py`では、属性・明示カーブ・node・複数nodeの
`set_tangent_lock()` / `set_tangent_locks()`について次の契約を検証します。

- 単一キー、両端包含、片側省略、全キー、負時刻・subframeと、境界キーを追加しないこと。
- `tangents_locked` / `weights_locked`の個別指定、`None`による維持、両方省略・カーブなし・
  該当キーなしのno-opと、bool以外・逆転範囲・非有限時刻の予約時拒否。
- 接線type・接線XY、値・時刻・breakdown・weighted・infinityと範囲外キーを維持すること。
  nonweightedカーブでもweight lockを保存し、weighted設定を変更しないこと。
- 既定ベース・明示layer・明示TA / TL / TUカーブ、通常の上流チャンネルと作成待ち明示カーブ。
- node・複数nodeのkeyable / channelBox・明示属性、連続・離散属性、既存カーブだけの変更、
  missing・重複・空node列、lock / reference / layer所属と全対象の事前検証。
- 反復Undo / Redo、MPxCommandのMaya標準履歴、同一batchの途中失敗時rollback。
- 属性・layer・明示カーブ・node・複数nodeの公開引数と`None`の戻り値をIDE補完で追えること。

Maya 2025の実挙動確認では、`MFnAnimCurve.setTangentsLocked()` /
`setWeightsLocked()`が接線type・XYやweightedを変更しないこと、nonweightedでもweight lockが
保存されることを確認しています。また、これらのsetterへ渡した`MAnimCurveChange`だけでは
Undo時にlockが戻らないことを確認したため、実装はanimCurveの`keyTanLocked` /
`keyWeightLocked`配列plugを`MDGModifier`で編集します。

開発中の局所確認には次を使用します。

```powershell
.\scripts\test-pytest-maya2025.cmd tests\maya\node\operator\attr\test_keyframe_lock.py tests\maya\node\operator\node\test_node_keyframe_lock.py tests\maya\mpx_cmd\test_command.py -q --tb=short
```

## node・複数nodeのweighted変更の検証

`test_node_keyframe_weighted.py`では、`node.keyframes.set_weighted()`と
`nodes.keyframes.set_weighted([...])`について次の契約を検証します。

- TA / TL / TUの既存カーブ、連続・離散属性、0キーカーブと同値設定を扱い、静的属性へ
  カーブを作成しないこと。同じbatchで先に作成したカーブは実行時に認識すること。
- keyable / channelBox・明示属性、複数nodeの属性名のunion、unitConversionを含む上流探索、
  rootと明示layerを`set_tangents()`と同じ規則で選択すること。
- missing・空／重複node列、bool以外のoption、plug・curve・node・layerのlock / reference、
  layer未所属・共有カーブを拒否し、全対象を変更前に検証すること。
- Maya標準のweighted変換、接線type等の保持、反復Undo / Redoで失われたweightまで復元すること。
  後続処理の失敗時に同じbatch全体をrollbackすること。
- `NodeKeyframeManager` / `NodesKeyframeManager`の引数と`None`戻り値をIDE補完で追えること。

Maya 2025の実挙動確認では、`MFnAnimCurve.setIsWeighted()`がキー時刻・値、全接線type、
tangent / weight lock、breakdown、pre / post infinityを維持することを確認しています。
nonweightedからweightedへの変換は密な評価値を維持し、weightedからnonweightedへの変換は
接線方向を保ってweightを正規化するため、任意weightの形状は変わり得ます。Falseへ変更後に
Trueへ戻しても元のweightは復元されません。`MAnimCurveChange`のUndoは元のweightと形状を
正確に復元します。`weightedTangents` plugの`MDGModifier`編集では復元できないため使用しません。

```powershell
.\scripts\test-pytest-maya2025.cmd tests\maya\node\operator\node\test_node_keyframe_weighted.py tests\maya\node\operator\attr\test_keyframe_data.py -q --tb=short
```

## plug入力ベイクの検証

`test_keyframe_bake.py`では、`KeyframeManager.bake()`の次の契約を検証します。

- 呼び出し時の再生範囲、明示範囲、終了端を含むsample間隔、負時刻・subframe、静的入力。
  予約後のFPS変更では物理時刻を維持し、値は初回実行時のsceneから取得すること。
- TA / TL / TU、連続値の既定auto / auto、bool・enum・整数系の既定step / step、
  連続用の共通・個別接線指定と離散用`discrete_tangent_type`、constant infinity、nonweightedへの全置換。
  連続・離散の全生成キーでtangent lockが有効、weight lockが無効であり、同じbatchの
  `set_tangent_locks(tangents_locked=False)`で明示的にBreak Tangentsへ変更できること。
  既存カーブの範囲外キー・設定を削除し、直接の非共有カーブは再利用すること。
- constraint・expression等の上流nodeを残して対象入力だけを切断すること。
  親compound接続の非対象子、共有カーブの別出力先、ベース以外のlayerを維持すること。
- layer未指定ではrootの生入力、`anim_layer()`では指定layerの生入力をベイクし、
  既存layerの合成効果を二重に加えないこと。
- target plug / node、接続元node、layerのlockとreference、不正引数、TT、非有限サンプルの拒否。
  10,000,001点の上限、対象なしではなく静的カーブを作ること。
- query時に予約を実行しないこと、同じbatchの先行変更、反復Undo / Redo、
  接続変更後・後続処理・適用後検査の失敗時rollback、現在時刻と選択の維持。

専用MPxCommand fixtureはMaya標準Undo / Redoとcommand失敗時の接続・カーブ復元を検証します。
型・補完contractは属性経由の引数・戻り値と、明示カーブへ`bake()`を公開しないことを確認します。
各時刻を順に進めるsimulationやcacheの検証は初期版に含めません。

```powershell
.\scripts\test-pytest-maya2025.cmd tests/maya/node/operator/attr/test_keyframe_bake.py
.\scripts\test-pytest-maya2025.cmd tests/maya/mpx_cmd/test_command.py -k bake
```

## node入力ベイクの検証

`test_node_keyframe_bake.py`では、`node.keyframes.bake()`の次の契約を検証します。

- keyable属性の自動収集、channelBox属性の任意追加、非keyable明示属性、compound展開、重複排除。
- `include_static=True`の既定動作による静的カーブ作成と、`False`による生入力の
  アニメーション判定。明示属性にも同じ静的値規則を適用し、対象0件をエラーにすること。
- 自動収集での未対応・lock属性と指定layer未所属属性の除外、明示時のmissing・未対応・
  lock・未所属の拒否。node / layer / 接続元のlock・reference検査。
- 全属性のsamplingが最初の接続変更より前に完了すること。同じ親compound接続を複数leafが
  共有しても1回だけ切断し、対象外の兄弟を維持すること。
- 既存nodeと同じDG modifierで作成待ちのDG node、ベース・指定layer、Undo / Redo、
  複数対象の途中失敗時rollback、適用後の全サンプル値検査。
- 開始・終了・sample間隔、bool option、属性列・接線の入力検証と、IDE補完で追える
  `NodeKeyframeManager`の引数・戻り値型。

専用MPxCommand fixtureのベイク経路も`node.keyframes.bake(attributes=["tx"])`を使用し、
Maya標準Undo / Redoとcommand失敗時rollbackを検証します。plug単位の既存テストは同じ
複数対象内部処理を1対象で通し、従来の接続分割・layer・静的入力の契約を回帰確認します。

```powershell
.\scripts\test-pytest-maya2025.cmd tests/maya/node/operator/node/test_node_keyframe_bake.py
.\scripts\test-pytest-maya2026.cmd tests/maya/node/operator/node/test_node_keyframe_bake.py
.\scripts\test-pytest-maya2027.cmd tests/maya/node/operator/node/test_node_keyframe_bake.py
.\scripts\test-pytest-maya2025.cmd tests/maya/mpx_cmd/test_command.py -k bake
```

`test_nodes_keyframe_bake.py`では、`nodes.keyframes.bake([...])`の次の契約を検証します。

- NodeOperator / MObject / node名の複数指定、重複nodeと空の入力列の拒否。
- 明示属性名を存在するnodeだけへ適用し、全nodeで見つからない名前、既存の未対応・lock属性を
  操作全体のエラーにすること。自動収集では対象0件のnodeをスキップすること。
- 上流・下流nodeを逆順で指定しても、全nodeのsamplingを接続変更より前に完了すること。
- 共通layer、作成待ちnode / layer、1回のUndo / Redo、後半nodeの検査失敗時の全体rollback。
- 共通・個別・離散用の接線指定、`フレーム数 × 対象leaf数`による総サンプル数上限と、
  `NodesKeyframeManager`の型・補完契約。

```powershell
.\scripts\test-pytest-maya2025.cmd tests/maya/node/operator/node/test_nodes_keyframe_bake.py
.\scripts\test-pytest-maya2026.cmd tests/maya/node/operator/node/test_nodes_keyframe_bake.py
.\scripts\test-pytest-maya2027.cmd tests/maya/node/operator/node/test_nodes_keyframe_bake.py
```

2026-09-20の複数node版実装時点で、plug版31件・node版21件・複数node版21件・
MPxCommand 2件を合わせた関連75件がMaya 2025 / 2026 / 2027ですべて成功しています。
`_keyframes.py` / `_keyframe_bake.py`の明示Pyrightと型・補完contractは3 versionで
error / warningなしです。`QT_QPA_PLATFORM=offscreen`で実行した`verify.cmd`も成功し、
Maya 2025 full pytestは6,722件成功・632件skip、UI互換性は各versionで
Qt/UI 726件・Maya UI 244件成功しました。Blackは4,473ファイル、差分検査も成功しています。

## キーフレーム移動の検証

2026-09-15に`move_frame()` / `move_frames()`と専用の`test_keyframe_move.py`を追加しました。
以下は移動実装の検証範囲であり、上の引き継ぎ時点の成功件数には含まれません。

- 単一・範囲・全体の相対移動と開始/終了基準の絶対移動、正負の移動、subframe、範囲端、
  FPS変更、対象なし・移動量0、不正入力、移動先の対象外キーの置換。
- `insert_missing`の既定False、明示境界だけの補完、同時刻境界の重複排除、
  実在キーのない区間、infinity領域での値取得、挿入から移動までの履歴。
- 複数キーが互いの元時刻へ移る場合と、移動対象外のキーをまたぐ場合。
  処理順による一時的な重複と、最終結果の重複を区別し、元キーが余分に残らないこと。
- 値・接線type / XY / lock・breakdown・weighted・infinityについて仕様で定めた保持や再計算、
  移動対象外のキーと隣接区間の評価。TA / TL / TU / TT、weightedの有無、auto・fixed・step系を含める。
- 直接接続・対応済みの上流チャンネル・ベース・加算・Override・明示カーブ指定の対象一致。
  非対象のlayer・軸・weightと接続を保持し、予約後の対象変更、lock / referenceを検査すること。
- 同一batchの先行キー設定からの移動、保留中query、反復Undo / Redo、
  移動途中・後続処理の失敗時rollback、MPxCommandからの履歴と型・IDE補完。

`test_keyframe_target.py`と`test_curve_keyframe.py`の共通編集パラメーターにも移動を登録し、
上流チャンネル・指定layer・既定ベース・明示カーブのlock / reference等を検査します。
`tests/maya/mpx_cmd/test_command.py`はMaya標準Undo / Redoとcommand失敗時の復元、
`tests/typecheck/node_operator_contract.py`は3入口の引数・戻り値・排他指定を検査します。

```powershell
.\scripts\test-pytest-maya2025.cmd tests/maya/node/operator/attr tests/maya/mpx_cmd tests/maya/node/operator/node/dg/test_anim_layer.py -q --tb=short
```

Maya 2026 / 2027でも同じ範囲を実行し、最終検証は`scripts/verify.cmd`を使用します。

2026-09-15、移動実装追加後の検証結果です。

| 確認内容 | 結果 |
| --- | --- |
| 移動専用pytest | Maya 2025で261件成功。下記の関連・全体テストにも含む |
| attr・MPxCommand・AnimLayerの関連pytest | Maya 2026 / 2027で各1,861件成功、プロセス正常終了。Maya 2025は下記のfull pytestで同じ範囲を確認 |
| `scripts/verify.cmd` | 成功。Black、3 versionの型・補完contract、Maya 2025 full pytest、3 versionのUI互換性、差分確認を含む |
| 上記のMaya 2025 full pytest | 4,413件成功、632件skip。Qt/UIの対象は専用ランナーでも別途実行 |
| 上記のUI互換性 | Maya 2025 / 2026 / 2027で各Qt/UI 726件・Maya UI 244件成功 |

通常実行は既存のクリップボードテスト1件で停止したため、
`QT_QPA_PLATFORM=offscreen`をプロセス環境に設定して`verify.cmd`全体を再実行し、成功しました。
テストの除外やUI実装の変更はしていません。
その後、移動APIは利用者によるMaya画面上での動作確認とpushまで完了しました（`218751db`）。

## キーフレーム移動の補間の検証

`test_keyframe_move_interpolation.py`では、`move_frames()`の補間による移動量の重み付けを検証します。

- 移動前の時刻によるlinear / smoothstep、相対移動と元範囲を基準にした開始・終了合わせ、
  片側補間・片側省略・幅0の元範囲、負の時刻・subframe、実在キーのない元範囲。
- 影響度0の端点を含む対象キー同士の衝突・順序逆転の拒否、対象外キーへの上書きと追い越し。
  欠けた補間端点を仮キーとしては扱わず、明示挿入したときだけ固定点として検査すること。
- TA / TL / TU / TT、weightedの有無、fixed・auto・linear・step系、値・接線・lock・breakdown・
  infinityの保持。短いweighted接線とnonweightedの生XY、再挿入で再現できないTT接線のrollback。
- 最大4境界の挿入とinfinityの事前評価、影響度0のキーを移動・再挿入しないこと。
  移動量0では挿入しないこと、キーだけへの重み付けで自動サンプリングをしないこと。
- 対象なし・空カーブ・不正引数、予約時のFPS捕捉、no-opでもmanager・write検査を通すこと。
  保留中作成・先行編集とqueryの非実行、再接続・改名、反復Undo / Redo。
- 境界挿入後・時刻変更後・削除後・再挿入後の失敗で同一batch全体をrollbackすること。

共通の`test_keyframe_target.py` / `test_curve_keyframe.py`でも`move_frames()`へ補間を指定し、
チャンネル・既定ベース・指定layer・明示カーブ・lock / referenceを検証します。
MPxCommand fixtureには補間移動と境界挿入の組み合わせを追加し、Maya標準Undo / Redoと
command失敗時rollbackを検証します。型contractは3種類の配置方法と補間引数を検査します。
影響度計算とキー復元を共有するため、通常移動・時間拡縮・値編集も回帰テストに含めます。

関連pytestの範囲と最終検証方法は通常移動・時間拡縮と同じです。
その後、補間移動も利用者によるMaya画面上の動作確認・pushまで完了しました（`9a63af85`）。

2026-09-18、補間移動追加後の検証結果です。

| 確認内容 | 結果 |
| --- | --- |
| 補間移動の専用pytest | 182件。下記の関連・全体テストにも含む |
| attr・MPxCommand・AnimLayerの関連pytest | Maya 2026 / 2027で各3,021件成功、プロセス正常終了。Maya 2025は下記のfull pytestで同じ範囲を確認 |
| 変更実装5ファイルと型contractの明示Pyright | Maya 2025でエラー・警告0件 |
| `scripts/verify.cmd` | `QT_QPA_PLATFORM=offscreen`で成功。Black 4,457ファイル、3 versionの型・補完contract、Maya 2025 full pytest、3 versionのUI互換性、差分確認を含む |
| 上記のMaya 2025 full pytest | 5,995件成功、632件skip |
| 上記のUI互換性 | Maya 2025 / 2026 / 2027で各Qt/UI 726件・Maya UI 244件成功 |

Maya 2027では、移動の検証用MPxCommandをパラメーターごとに登録・解除する構成で、
全テスト成功後のプロセス終了時に異常終了（`-1073740940`）が再現しました。
push済みコミットと一時フォルダーで比較し、現在の実装と従来のテストでは正常終了することを確認しました。
検証用commandへ補間の切り替えを追加し、module内では登録を共有する構成に整理しています。
シーン初期化は各テストで維持し、同じ57件のMPxCommandテストと3,021件の関連テストで
正常終了を確認しました。テストの除外や終了コードの無視はしていません。

## キーフレーム時間拡縮の検証

`test_keyframe_scale.py`では、`scale_frames()`の時間拡縮と配置先の置換を検証します。

- 倍率・長さ・両端合わせ、相対配置・開始/終了合わせ、明示境界と実在キーの違い、
  片側省略・全体・単一キー、負の時刻・subframe、元区間と配置先の重なり。
- 既定の`replace_range`と`merge`、欠けた境界も含めた配置先区間の置換、対象外fixedキーの保持。
- TA / TL / TU / TT、weighted / nonweighted、14種類の接線、値・lock・breakdown・infinity、
  密なサンプルでの形状照合と`fast` / `slow`のMaya標準拡縮との照合。
- 短いweighted接線が下限補正されないこと、TTで再現できない接線のrollback。
  境界挿入前の値評価、区間外のinfinity補完、挿入を伴う反復Undo / Redo。
- カーブなし・空カーブ・対象なし・恒等変換、0幅区間・不正引数・時刻の表現限界と精度限界、
  予約後のFPS / 表示単位変更、no-opでもmanager・write検査を通すこと。
- 保留中node作成と先行キー編集、queryの非実行、再接続・改名、bool・enum等の属性。
  挿入後・削除後・再挿入後の失敗時に、同じbatchの先行変更もrollbackすること。

`test_keyframe_target.py` / `test_curve_keyframe.py`の共通編集一覧にも拡縮を登録しています。
通常チャンネル・既定ベース・明示layer・明示カーブの対象選択、上流接続、lock / reference、
非対象layerのキー・weight保持を、既存の共通テストで検証します。
専用MPxCommand fixtureはMaya標準Undo / Redoとcommand失敗時rollback、型contractは
属性・layer・明示カーブの3入口、戻り値、排他引数、modeと境界補完の補完を検証します。

2026-09-17、下記の関連pytestはMaya 2025 / 2026 / 2027それぞれ2,360件成功しました。
変更した実装3ファイルと型contractを明示したMaya 2025のPyright検証も、エラー・警告0件でした。
その後、長さ指定の丸めで恒等変換が不要な境界挿入をしないように補強し、
時間拡縮の専用pytestは3 versionで各322件成功しました。
補強後の最終`verify.cmd`も`QT_QPA_PLATFORM=offscreen`で成功しました。
Blackは4,452ファイル、3 versionの型・補完contractはすべて成功、Maya 2025 full pytestは
5,336件成功・632件skip、Qt/UIは各versionで726件、Maya UIは各versionで244件成功しました。
`git diff --check`も成功しています。
その後、利用者によるMaya画面上での`scale_frames()`の動作確認とpushまで完了しました（`66dee785`）。

```powershell
.\scripts\test-pytest-maya2025.cmd tests/maya/node/operator/attr tests/maya/mpx_cmd tests/maya/node/operator/node/dg/test_anim_layer.py -q --tb=short
.\scripts\test-pytest-maya2026.cmd tests/maya/node/operator/attr tests/maya/mpx_cmd tests/maya/node/operator/node/dg/test_anim_layer.py -q --tb=short
.\scripts\test-pytest-maya2027.cmd tests/maya/node/operator/attr tests/maya/mpx_cmd tests/maya/node/operator/node/dg/test_anim_layer.py -q --tb=short
.\scripts\verify.cmd
```

## キーフレーム時間拡縮の補間の検証

`test_keyframe_scale_interpolation.py`は、`scale_frames()`の時刻と接線Xへの影響度を検証します。

- 元時刻によるlinear / smoothstepと既定値、倍率・長さ・両端合わせと各配置方法。
  主区間だけを基準にすること、片側省略・キーのない主区間・幅0・負の時刻・subframe。
- 主区間の配置先だけの部分置き換え、merge、置換範囲外の補間キーの衝突上書き。
  動かない端点が置換範囲内でも保持されること、主ピボットの接線だけの拡縮。
- 対象キーの衝突・順序逆転の拒否、欠けた補間端点を仮キーとせず、明示挿入時のみ検査すること。
- TA / TL / TU / TT、weightedの有無、fixed・auto・linear・step系、実効倍率による接線X、
  値・種類・lock・breakdown・infinityの保持と反復Undo / Redo。
  復元できないTTのweighted接線は同じbatch全体をrollbackすること。
- 最大4境界の事前評価・挿入・重複除去、恒等変換や影響度0だけの場合は変更しないこと。
  no-opでもmanagerとwrite検査を通すこと、対象なし・空カーブ・不正引数。
- 予約時のFPS捕捉、保留中の作成・先行編集・queryの非実行。
  挿入後・捕捉後・削除後・復元後の失敗で先行編集も含めてrollbackすること。

`test_keyframe_target.py` / `test_curve_keyframe.py`も補間拡縮を指定し、ベース・指定layer・
明示カーブとlock / referenceを検証します。MPxCommandは補間拡縮と境界挿入を追加し、
Maya標準Undo / Redo・command失敗時rollbackを確認します。登録は移動のfixtureと同じく
module内で共有し、シーンは各caseで初期化します。型contractは3入口と全配置形式の補間引数を検査します。
その後、補間拡縮も利用者によるMaya画面上の動作確認・pushまで完了しました（`fbf9c033`）。

2026-09-18、補間拡縮追加後の検証結果です。

| 確認内容 | 結果 |
| --- | --- |
| 補間拡縮の専用pytest | 150件。下記の関連・全体テストにも含む |
| attr・MPxCommand・AnimLayerの関連pytest | Maya 2025 / 2026 / 2027で各3,173件成功、プロセス正常終了 |
| 変更実装2ファイルと型contractの明示Pyright | Maya 2025でエラー・警告0件 |
| `scripts/verify.cmd` | `QT_QPA_PLATFORM=offscreen`で成功。Black 4,458ファイル、3 versionの型・補完contract、Maya 2025 full pytest、3 versionのUI互換性、差分確認を含む |
| 上記のMaya 2025 full pytest | 6,147件成功、632件skip |
| 上記のUI互換性 | Maya 2025 / 2026 / 2027で各Qt/UI 726件・Maya UI 244件成功 |

## キーフレーム時間拡縮のピボット指定の検証

`test_keyframe_scale_pivot.py`では、`scale_frames()`の`pivot`を検証します。

- 中央・開始・終了・区間外のピボット、明示Noneと従来動作、正の倍率・長さ、拡縮後の相対移動。
  片側省略・全体・単一キー、負の時刻・subframe、ピボットにキーがなくても挿入しないこと。
- 変換後の主区間による部分置き換えとmerge、補間キーの配置先が置換範囲外にある場合の衝突上書き。
  linear / smoothstepでピボット変換と相対移動を重み付けすること、接線Xの実効倍率。
- TA / TL / TU / TT、weightedの有無、拡縮後の形状・値・種類・lock・breakdown・infinity、反復Undo / Redo。
- 予約時のピボット・長さ・相対移動の時間単位捕捉。遠いピボットの恒等変換や、
  長さから算出した倍率の丸めで不要な編集をしないこと。小さい倍率で表現可能な移動先を維持すること。
- 不正なピボット、配置先境界との併用を予約時に拒否すること。表現範囲外や対象キー同士の
  衝突・順序逆転、途中の失敗で同一batchの先行編集・境界挿入もrollbackすること。
- 保留中の作成・先行移動・queryの非実行、no-opでもmanagerとwrite検査を通すこと。

共通の対象選択テストもピボットを指定し、ベース・指定layer・明示カーブとlock / referenceを確認します。
MPxCommandのfixtureでは倍率・長さ・補間・境界挿入とピボットを組み合わせ、Maya標準の履歴と
command失敗時rollbackを確認します。型contractは3入口のピボット指定と排他引数を検査します。
その後、利用者によるMaya画面上でのピボット指定の動作確認・pushまで完了しました（`f0def8ab`）。

2026-09-18、ピボット指定追加後の検証結果です。

| 確認内容 | 結果 |
| --- | --- |
| ピボット指定の専用pytest | 112件。下記の関連・全体テストにも含む |
| attr・MPxCommand・AnimLayerの関連pytest | Maya 2025 / 2026 / 2027で各3,285件成功、プロセス正常終了 |
| 変更実装2ファイルと型contractの明示Pyright | Maya 2025でエラー・警告0件 |
| `scripts/verify.cmd` | `QT_QPA_PLATFORM=offscreen`で成功。Black 4,459ファイル、3 versionの型・補完contract、Maya 2025 full pytest、3 versionのUI互換性、差分確認を含む |
| 上記のMaya 2025 full pytest | 6,259件成功、632件skip |
| 上記のUI互換性 | Maya 2025 / 2026 / 2027で各Qt/UI 726件・Maya UI 244件成功 |

## キーフレーム編集APIの名称整理の検証

時間方向は`move_frame()` / `move_frames()` / `scale_frames()`に改名し、
時間・値の編集引数を`offset` / `to` / `to_start` / `to_end` / `scale` / `duration` / `pivot`へ整理しました。
旧メソッド名・旧keyword引数のaliasは提供しません。変更対応表は[旧APIからの移行](attributes.md#旧apiからの移行)を参照してください。

既存の移動・時間拡縮・値編集・共通resolver・MPxCommandのテストと手動サンプルを新名へ更新しています。
型・補完contractも属性・指定layer・明示カーブの3入口で新名と排他引数を検査します。
`AnimationClip.restore()`の引数と検証は維持しています。
本書の過去の実装・検証記録もAPI名は現在の名前で表記しますが、過去の成功件数は当時の実績です。
その後、名称整理も利用者によるMaya画面上の動作確認・pushまで完了しました（`b90965c0`）。

2026-09-18、名称整理後に改めて実行した検証結果です。

| 確認内容 | 結果 |
| --- | --- |
| attr・MPxCommand・AnimLayerの関連pytest | Maya 2025 / 2026 / 2027で各3,285件成功、プロセス正常終了 |
| 変更実装3ファイルと型contractの明示Pyright | Maya 2025でエラー・警告0件 |
| `scripts/verify.cmd` | `QT_QPA_PLATFORM=offscreen`で成功。Black 4,459ファイル、3 versionの型・補完contract、Maya 2025 full pytest、3 versionのUI互換性、差分確認を含む |
| 上記のMaya 2025 full pytest | 6,259件成功、632件skip |
| 上記のUI互換性 | Maya 2025 / 2026 / 2027で各Qt/UI 726件・Maya UI 244件成功 |

## キーフレーム値編集の検証

`test_keyframe_value.py`では、`set_value(s)` / `add_value(s)` / `scale_value(s)`の
値編集と既存キーへの補間ウェイトを検証します。

- 単一・両端包含範囲・片側省略・全体、負の時刻・subframe、0・負の倍率とピボット。
- linear / smoothstepと既定値、片側補間、補間端点の影響度0、疎なキーで自動samplingや
  イーズ再現用接線調整を行わないこと、最大4境界だけの挿入とinfinityの事前評価。
- TA / TL / TU / TT、weighted / nonweighted、fixed・auto・linear・step・stepnext、
  接線・lock・breakdown・infinity保持、全体拡縮後の密なサンプル照合。
  短いweighted接線の保持、nonweighted接線の正規化、対象外キーを正規化しないこと。
- 生値の設定・加算・拡縮を加算 / Override layerとベースで照合し、合成値の逆算をしないこと。
  bool・enum・整数属性でもカーブの数値を丸めず扱うこと。
- カーブなし・空カーブ・対象なし・恒等演算、同値setと任意境界挿入、不正引数・overflow・TT時間値の表現限界。
- 保留中node作成・先行編集、queryの非実行、再接続・改名、予約後のFPS / 表示単位変更。
- 反復Undo / Redo、境界挿入後・値更新後・削除後・復元後の失敗時rollback。

6メソッドを`test_keyframe_target.py` / `test_curve_keyframe.py`の共通編集一覧にも登録し、
属性・明示layer・既定ベース・明示カーブの対象選択、上流探索、lock / referenceを検証します。
専用MPxCommand fixtureはMaya標準のUndo / Redoとcommand失敗時rollbackを確認します。
型・補完contractは3入口、6メソッド、戻り値、値・補間・境界挿入の引数を検査します。

関連pytestは時間拡縮と同じattr・MPxCommand・AnimLayerの範囲をMaya 2025 / 2026 / 2027で
実行し、最後に`QT_QPA_PLATFORM=offscreen`を設定した`scripts/verify.cmd`で検証します。

2026-09-17、値編集追加後の検証結果です。

| 確認内容 | 結果 |
| --- | --- |
| 値編集の専用pytest | 305件。下記の関連・全体テストに含み、3 versionで成功 |
| attr・MPxCommand・AnimLayerの関連pytest | Maya 2026 / 2027で各2,837件成功。Maya 2025は補強前の2,786件成功に加え、補強後のfull pytestで確認 |
| 変更実装3ファイルと型contractの明示Pyright | Maya 2025でエラー・警告0件 |
| `scripts/verify.cmd` | 成功。Black 4,455ファイル、3 versionの型・補完contract、Maya 2025 full pytest、3 versionのUI互換性、差分確認を含む |
| 上記のMaya 2025 full pytest | 5,811件成功、632件skip |
| 上記のUI互換性 | Maya 2025 / 2026 / 2027で各Qt/UI 726件・Maya UI 244件成功 |

その後、値編集も利用者によるMaya画面上での動作確認とpushまで完了しました（`ba5fc139`）。

## キー削減の検証

`test_keyframe_reduce.py`では、手動接線を維持する`reduce_keys()`を検証します。

- TA / TL / TU、weighted / nonweighted、相対的なキー密度・負の時刻・subframe、
  部分範囲・全体・実在境界の保持、予約後のFPS / 表示単位変更。
- fixed接線・lock・breakdown・weighted / infinity設定の保持、step / stepnextの切り替わり。
  auto・spline等の再計算後も、初回実行時の元カーブとの誤差内にあること。
- Bezier区間の値とMayaネイティブ評価の照合、同値キー間の膨らみ、
  累積削減誤差の高密度サンプル検証、範囲外形状・linear infinityの外挿傾き。
- 誤差を判定できないweighted区間の保護、カーブなし・空カーブ・対象なし・不正引数。
- 作業用カーブやmodified flagを残さないこと、予約後の再接続・改名、
  既定ベース・明示layer・共有出力の明示カーブ、先行キー設定からの削減。
- 作業用カーブでの失敗・適用後検査の失敗・後続処理の失敗時rollbackと反復Undo / Redo。

共通の`test_keyframe_target.py` / `test_curve_keyframe.py`にも削減を登録し、
派生するチャンネル・layer・lock / reference等のテストを実行します。
専用MPxCommand fixtureでMaya標準Undo / Redoとcommand失敗時の復元を確認し、
型・補完contractは3つの入口の引数と戻り値を検査します。

関連pytestは移動実装時と同じattr・MPxCommand・AnimLayerの範囲を3バージョンで実行し、
最終確認には`scripts/verify.cmd`を使用します。キー削減の利用者による手動確認は未実施です。

2026-09-15、キー削減追加後の検証結果です。

| 確認内容 | 結果 |
| --- | --- |
| attr・MPxCommand・AnimLayerの関連pytest | Maya 2025 / 2026 / 2027で各1,993件成功、プロセス正常終了 |
| Bezier分割の計算改善後の削減専用pytest・MPxCommand | 3 versionで各137件成功。削減専用は102件 |
| `scripts/verify.cmd` | `QT_QPA_PLATFORM=offscreen`で成功。Black、3 versionの型・補完contract、full pytest、UI互換性、差分確認を含む |
| 上記のMaya 2025 full pytest | 4,545件成功、632件skip。Qt/UI対象は専用ランナーでも別途実行 |
| 上記のUI互換性 | 3 versionで各Qt/UI 726件・Maya UI 244件成功 |

## AnimationClipの検証

仕様は[AnimationClip](animation_clip.md)を参照してください。

### JSONファイルの保存・読込

- `tests/py/test_json_file.py`: UTF-8・日本語・BOM、JSON各型とtuple、PathLike・相対パス、
  親フォルダの既定作成と無効化、整形・上書き禁止・保存確定時の競合、
  不正値・非有限数・循環・文字コード・JSON構文・ファイル不在・親がファイルの場合の拒否。
  書き込み・close・確定の失敗時に既存ファイルを保護し、一時ファイルを除去すること。
- `tests/maya/node/test_animation_clip_file.py`: flatten / preserveとTA / TL / TUの往復、
  詳細データ・layer設定の保持、schema 2・BOM・オプション、編集済みKeyDataの保存前再検証、
  元clipとscene状態・Undo履歴・保留中modifierの維持、元scene削除後の読込と復元・Undo / Redo。
- `tests/typecheck/json_file_contract.py`: `bdu.json_file`と直接import、PathLike引数・保存オプション、
  `Path` / `object` / `AnimationClip`の戻り値型と不正な引数型の拒否。

2026-09-19、JSONファイルAPI追加後の検証結果です。

| 確認内容 | 結果 |
| --- | --- |
| 汎用JSON・AnimationClip関連pytest | Maya 2025 / 2026 / 2027で各790件成功、プロセス正常終了。今回追加したテストは73件 |
| JSONモジュール・AnimationClip実装と新しい型contractの明示Pyright | Maya 2025でエラー・警告0件 |
| `scripts/verify.cmd` | `QT_QPA_PLATFORM=offscreen`で成功。Black 4,467ファイル、3 versionの型・補完contract、Maya 2025 full pytest、3 versionのUI互換性、差分確認を含む |
| 上記のMaya 2025 full pytest | 6,647件成功、632件skip |
| 上記のUI互換性 | Maya 2025 / 2026 / 2027で各Qt/UI 726件・Maya UI 244件成功 |

ファイルAPIの利用者によるMaya画面上での確認は未実施です。

### 復元に使用する範囲

`test_animation_clip_range.py`では、`restore(start_frame=..., end_frame=...)`の次の契約を検証します。

- flatten / preserve、3種類の復元mode、両端包含・片側省略・1時刻・全保存区間、未指定時の既存経路。
- 境界補完後のTA / TL / TUの密な形状比較、全対応接線・weighted / nonweighted、stepの切り替わり、
  接線のfixed化・lock解除・breakdown保持。空node・空チャンネル・node順も維持。
- 切り出し後の区間を基準とする相対移動・絶対配置・倍率・長さ・両端合わせ、保存FPSと復元FPSの区別、
  予約後のFPS変更、負時刻・subframe・任意の保存時間単位、削減済みデータとJSON往復。
- root / layer設定の切り出し・拡縮・比較・再利用と、明示設定上書きによる範囲外キーの削除。
- チャンネル固有のキー範囲外のconstant / linear補完、周期infinityの範囲外拒否。
- 予約前の入力検証、元clipとscene状態・Undo履歴の保持、作業nodeの破棄、後続チャンネル失敗時の非予約。
  保留中node作成、予約後のデータ独立、反復Undo / Redo、後続失敗時rollback。

専用MPxCommandも範囲指定あり・なしでMaya標準Undo / Redoと失敗時rollbackを検証します。
型・補完contractでは範囲引数と既存の時刻・拡縮指定を組み合わせ、戻り値が`None`であることを確認します。

2026-09-18、範囲復元追加後の検証結果です。

| 確認内容 | 結果 |
| --- | --- |
| attr・AnimationClip・MPxCommand・AnimLayerの関連pytest | Maya 2025 / 2026 / 2027で各4,018件成功、プロセス正常終了 |
| 変更実装4ファイルと型contractの明示Pyright | Maya 2025でエラー・警告0件 |
| `scripts/verify.cmd` | `QT_QPA_PLATFORM=offscreen`で成功。Black 4,463ファイル、3 versionの型・補完contract、Maya 2025 full pytest、3 versionのUI互換性、差分確認を含む |
| 上記のMaya 2025 full pytest | 6,574件成功、632件skip |
| 上記のUI互換性 | Maya 2025 / 2026 / 2027で各Qt/UI 726件・Maya UI 244件成功 |

その後、範囲復元も利用者によるMaya画面上での確認・pushまで完了しました（`9c405008`）。

Maya 2027の初回関連テストは4,018件の判定成功後、終了コード`-1073740940`となりました。
範囲・削減・詳細切り出し・専用MPxCommandに絞った480件では正常終了しました。
過去の移動テストの終了時異常と同じ登録の反復を避けるため、clip用MPxCommandもmodule内で登録を共有し、
scene初期化は各テストで維持する構成に整理しました。その後、同じ4,018件で正常終了を確認しました。
テストの除外や終了コードの無視はしていません。

### 保存データのキー削減

`test_animation_clip_reduce.py`は、`AnimationClip.reduce_keys()`の次の契約を検証します。

- flatten / preserve、TA / TL / TU、全体・両端包含・片側指定・対象なし、境界を挿入しないこと。
- 実カーブの削減との比較、weighted / nonweighted、fixed / auto / linear等の形状とメタデータ保持。
  キー間の膨らみ、短いweighted接線、breakdown保護とstepの切り替わり。
- 許容誤差の公開値単位、保存時FPS・任意のseconds_per_frame、負時刻・subframe、sceneのFPS変更。
- 元clipとの独立、schema 2 JSON往復、空node・空カーブ・node順、rootとlayerの設定維持・既存layer再利用。
- 元nodeを削除した後の処理、sceneのnode・modified flag・現在時刻・選択・Undo / Redo履歴と保留中編集の維持。
  復元・削減・再取得の失敗や後続チャンネルの失敗で部分変更を残さないこと。
- 削減済みclipの復元予約、Undo / Redo・後続失敗時rollback・予約後の独立コピー。
  保存カーブの誤差と、復元先の加算layerによる最終合成値の誤差を区別すること。

2026-09-18、クリップ削減追加後に実行した検証結果です。

| 確認内容 | 結果 |
| --- | --- |
| attr・AnimationClip・MPxCommand・AnimLayerの関連pytest | Maya 2025 / 2026 / 2027で各3,805件成功、プロセス正常終了 |
| 変更実装4ファイルと型contractの明示Pyright | Maya 2025でエラー・警告0件 |
| `scripts/verify.cmd` | `QT_QPA_PLATFORM=offscreen`で成功。Black 4,461ファイル、3 versionの型・補完contract、Maya 2025 full pytest、3 versionのUI互換性、差分確認を含む |
| 上記のUI互換性 | Maya 2025 / 2026 / 2027で各Qt/UI 726件・Maya UI 244件成功 |

その後、クリップ削減も利用者によるMaya画面上での確認・pushまで完了しました（`8a722b40`）。

### 逆再生clip

`tests/maya/node/test_animation_clip_reverse.py`は、`AnimationClip.reversed()`の次の契約を検証します。

- 保存範囲の共通秒軸による時刻の鏡映、負時刻・subframe、単一キー・空カーブ、
  元clipと変更可能な`KeyData`の独立、schema 2のファイル往復、二重反転。
- TA / TL / TU、weighted / nonweighted、fixed / linear / auto接線について、
  反転前後の密なカーブ評価値が鏡映時刻で一致すること。
- step / stepnextを区間単位で相互変換し、キー時刻・直前・直後・区間内の値を維持すること。
  incoming側だけにある非標準のstep系をoutへ移して区間をstep化しないこと。
- 全infinity種別の交換と範囲外評価、値・breakdown・weighted・tangent / weight lock、
  接線type・XY、clipとlayerのメタデータ保持。
- layer / root設定curveにもchannelと同じ秒軸を使い、保存範囲外キーと異なる
  `seconds_per_frame`を反転すること。
- 呼出時の再検証、Maya時刻精度、scene・現在時刻・選択・modified flag・保留中modifierの維持。
  反転clipの復元、反復Undo / Redo、後続処理失敗時のrollback。
- 型・補完contractでは`clip.reversed()`が`bdu.AnimationClip`を返し、連続呼出しできること。

2026-09-22の開発中確認では、逆再生専用pytest 34件と、既存の移動・拡縮・範囲・
ファイルAPIを含む関連pytest 581件がMaya 2025で成功しました。
変更実装と型contractを明示したPyrightもエラー・警告0件です。

### AnimationClipのnode部分抽出

`tests/maya/node/test_animation_clip_extract.py`は、`AnimationClip.extract(nodes=...)`と
capture時の保存node名について、次の契約を検証します。

- scene全体で一意な階層下DAGはnamespace込みのshort name、同名DAGはfull pathで保存すること。
  short name保存後の親変更、同名DAGのfull pathによるcaptureと既定restoreを含む。
- 新しいshort保存と従来のfull path入りschema 2を、clip内で一意なshort nameから抽出できること。
  short nameの複数一致、不明名、空・重複指定、裸の文字列、namespace省略を拒否すること。
- `nodes`の指定順、全channel、空node、保存範囲・時間単位・schema等のメタデータを維持すること。
  元scene削除後にも処理でき、元clipと変更可能な`KeyData`を共有しないこと。
- preserve clipでは使用layerと全祖先、root設定、設定curve、相対順を維持し、
  除外nodeだけが使用するlayerを除外すること。抽出clipの復元とUndoも確認すること。
- 呼出時に除外対象を含む元clip全体を再検証し、JSON往復、`reversed()`との連続利用、
  公開戻り値の型・補完contractを維持すること。

2026-09-23の開発中確認では、node抽出専用pytest 7件と、既存の保存・範囲・削減・逆再生・
時間変換・ファイルAPIを含むAnimationClip関連pytest 780件がMaya 2025で成功しました。
変更実装と型contractを明示したPyrightもエラー・警告0件です。

### 保存・復元の既存テスト

- `tests/maya/node/test_animation_clip.py`: 合成保存・layer保持、keyable / channelBox / 明示属性、
  static・compound・sparse array・enum・単位、JSON、範囲とFPS、名前空間とnode順対応、
  全置換・部分置換・merge、接線・lock・breakdown・weighted・infinity、layer階層・順序・
  設定競合・root設定、保留中操作と同一性、合成結果の検査、失敗時の全体rollbackを検証します。
- `tests/maya/mpx_cmd/test_animation_clip_command.py`と同階層`fixtures`の専用plug-in:
  時刻移動・時間拡縮の有無それぞれで、`cmds.undo()` / `cmds.redo()`によるlayer作成・キー復元の履歴と、
  command失敗時rollbackを検証します。
- `tests/maya/node/test_animation_clip_static.py`: `include_static`の既定除外・明示取得、
  明示属性・compoundへの適用、定数キー・空カーブ、constraint / expression / time / driven key、
  layer再現に必要な定数値とweight・親のweight、回転3軸の依存、layer限定、空nodeの順番維持、
  保留中編集の非実行とscene状態、復元先の対象外キーの維持を検証します。
- `tests/maya/node/test_animation_clip_time.py`: 相対移動・開始/終了合わせと3種類の復元mode、
  全node共通の区間基準、負の時刻・subframe・1時刻clip・移動量0、FPS変更前後の予約・実行、
  データの非変更・複数予約、不正引数の予約前拒否、接線等の詳細情報の保持、
  layerとrootの設定カーブの移動・比較・上書き、weighted接線の丸めとnonweighted接線の正規化、
  移動先layerの合成値解決、保留中node作成・後続失敗のrollback、Undo / Redoを検証します。
- `tests/maya/node/test_animation_clip_scale.py`: 倍率・長さ・両端指定、配置との組み合わせ、
  全node共通の基準、保存区間の境界、TA / TL / TUの各接線・weighted・lock・breakdown・infinity、
  `fast` / `slow`のMaya標準再計算、レイヤー設定の比較・再利用・区間外キー、
  置換mode・衝突、FPS変更前後の予約、データの非変更・複数予約、1時刻clip・不正引数・精度限界、
  移動先layerの合成値解決、保留中node作成・後続失敗・Undo / Redoを検証します。
- `tests/maya/node/operator/attr/test_keyframe_discovery.py`: 上流探索に加え、
  未接続outputの内部依存を含むアニメーション判定も検証します。
- `tests/maya/node/modifier/test_modifier_manager.py`: `queue_dg_batch()`の準備一回、
  初回・後続失敗、Undo / Redoを検証します。
- `tests/typecheck/node_operator_contract.py`: `bdu.AnimationClip`の入口、データ型とJSON・抽出・復元の
  戻り値型、抽出node iterable、modeのLiteral補完、`include_static`のbool型、
  復元時刻・拡縮引数の型と組み合わせを検証します。

2026-09-16時点で、次の関連範囲はMaya 2025 / 2026 / 2027それぞれ2,083件成功しました。
新機能のclip・専用MPxCommandは61件です。検証実績はこの時点の変更に対するもので、
以後の変更を自動的に保証するものではありません。

同日の最終`verify.cmd`も成功しました（`QT_QPA_PLATFORM=offscreen`）。
Blackは4,445ファイル、3 versionのPyright contractはすべて成功、Maya 2025 full pytestは
4,610件成功・632件skip、Qt/UIは各versionで726件、Maya UIは各versionで244件成功しました。
`git diff --check`も成功しています。

同日の`include_static`追加後は、次の関連範囲がMaya 2025 / 2026 / 2027それぞれ
2,117件成功しました。静的属性の専用テスト33件と、上流判定のテスト1件を追加しています。
変更した実装ファイルを明示したPyright検証も、エラー・警告0件でした。
追加後の最終`verify.cmd`も成功しました（`QT_QPA_PLATFORM=offscreen`）。
Blackは4,446ファイル、3 versionの型・補完contractはすべて成功、Maya 2025 full pytestは
4,644件成功・632件skip、Qt/UIは各versionで726件、Maya UIは各versionで244件成功しました。

2026-09-17の復元時刻指定追加後は、次の関連範囲がMaya 2025 / 2026 / 2027それぞれ
2,183件成功しました。復元時刻の専用テスト62件と、MPxCommandの時刻移動4件を追加しています。
変更した実装3ファイルを明示したMaya 2025のPyright検証も、エラー・警告0件でした。
最終`verify.cmd`も成功しました（`QT_QPA_PLATFORM=offscreen`）。Blackは4,448ファイル、
3 versionの型・補完contractはすべて成功、Maya 2025 full pytestは4,710件成功・632件skip、
Qt/UIは各versionで726件、Maya UIは各versionで244件成功しました。

同日の時間拡縮追加後は、次の関連範囲がMaya 2025 / 2026 / 2027それぞれ2,457件成功しました。
時間拡縮の専用テスト266件と、MPxCommandの時間拡縮8件を追加しています。
変更した実装3ファイルを明示したMaya 2025のPyright検証も、エラー・警告0件でした。
最終`verify.cmd`も成功しました（`QT_QPA_PLATFORM=offscreen`）。Blackは4,449ファイル、
3 versionの型・補完contract、Maya 2025 full pytestが成功しました。
Qt/UIは各versionで726件、Maya UIは各versionで244件成功しています。

```powershell
.\scripts\test-pytest-maya2025.cmd tests/maya/node/test_animation_clip.py tests/maya/node/test_animation_clip_static.py tests/maya/node/test_animation_clip_time.py tests/maya/node/test_animation_clip_scale.py tests/maya/node/operator/attr tests/maya/node/operator/node/dg/test_anim_layer.py tests/maya/node/modifier tests/maya/mpx_cmd
.\scripts\test-pytest-maya2026.cmd tests/maya/node/test_animation_clip.py tests/maya/node/test_animation_clip_static.py tests/maya/node/test_animation_clip_time.py tests/maya/node/test_animation_clip_scale.py tests/maya/node/operator/attr tests/maya/node/operator/node/dg/test_anim_layer.py tests/maya/node/modifier tests/maya/mpx_cmd
.\scripts\test-pytest-maya2027.cmd tests/maya/node/test_animation_clip.py tests/maya/node/test_animation_clip_static.py tests/maya/node/test_animation_clip_time.py tests/maya/node/test_animation_clip_scale.py tests/maya/node/operator/attr tests/maya/node/operator/node/dg/test_anim_layer.py tests/maya/node/modifier tests/maya/mpx_cmd
.\scripts\verify.cmd
```

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

## KeyframeManagerのキー設定の実装比較

`python/bd_util/_dev/maya/benchmark_keyframe_set.py`は、旧cmds実装の公開`set()`の反復、
現行実装の`set_key()`の反復、`set_keys()`の一括設定を、同じ現行`ModifierManager`上で
比較します。repository rootから、独立したmayapyプロセスで実行してください。
各計測でsceneを破棄するため、
作業中のMayaからは実行しません。

```powershell
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -B `
    .\bakedanuki\bakedanuki-util\python\bd_util\_dev\maya\benchmark_keyframe_set.py
```

既定ではcommit `1172c8db4eb6503d5eed42c208774192d69d2592`の`keyframe.py`を
`git show`で読み込みます。新規カーブ、既存1キーがあるカーブ、全キーの上書きの
3条件を、各10 / 100 / 1,000キーで比較します。対象はtransformの`tx`、単位は
cm / degree / film、tangentはlinearでweightを使用しません。ウォームアップ後の
5回の中央値をJSONで出力し、予約・実行・その合計・Undo・Redoの時間を分けて記録します。
出力の`backend`は、`cmds_baseline`が旧cmds実装、`current`が`set_key()`の反復、
`batch`が`set_keys()`の一括設定です。

scene準備と状態assertは測定区間に含めず、各計測でUndo / Redoを2往復して復元を
確認します。`--keys 10 100`、`--repeats 3`、`--baseline <revision>`で条件を変更できます。
Maya 2026 / 2027では実行するmayapyのversionを変更してください。

2026-09-10に同一Windows環境で測定した、transform.translateXへの1000キー設定の
単発呼び出しの比較結果です。一括APIの追加前の測定で、`set_keys()`は含みません。
単位はmsで「旧cmds実装 → 当時のAPI併用実装」を示します。各versionは別プロセスで
順に実行し、他のMayaテスト・ベンチとは並行実行していません。

| Maya | 条件 | 予約＋実行 | Undo | Redo |
| --- | --- | --- | --- | --- |
| 2025 | 新規カーブ | 36.62 → 20.93 | 86.32 → 2.44 | 82.75 → 2.30 |
| 2025 | 既存カーブ | 37.48 → 21.15 | 87.95 → 2.40 | 84.08 → 2.30 |
| 2025 | 全キー上書き | 37.35 → 21.97 | 172.89 → 2.47 | 168.81 → 2.52 |
| 2026 | 新規カーブ | 39.09 → 23.34 | 81.30 → 2.58 | 77.88 → 2.45 |
| 2026 | 既存カーブ | 47.53 → 25.52 | 90.95 → 2.63 | 83.98 → 2.52 |
| 2026 | 全キー上書き | 38.61 → 24.27 | 159.31 → 2.60 | 156.24 → 2.71 |
| 2027 | 新規カーブ | 36.60 → 23.49 | 79.92 → 2.68 | 75.82 → 2.53 |
| 2027 | 既存カーブ | 35.67 → 22.93 | 78.50 → 2.42 | 75.16 → 2.33 |
| 2027 | 全キー上書き | 35.59 → 23.52 | 157.97 → 2.40 | 151.21 → 2.52 |

この単純な接続の測定では、予約＋実行が約1.5〜1.9倍高速でした。
新規カーブも最初の1キーはcmdsへ委譲し、後続をAPIで処理しています。
レイヤーなどcmdsへ委譲する構成の速度向上を示す結果ではありません。
予約処理そのものは、実行時の経路選択と変更キャッシュの準備によって増えます。
現在の`set_keys()`ではバッチ内でカーブ取得と変更キャッシュを共有します。
別の呼び出しをまたぐ永続キャッシュは導入していません。

同日に一括APIを追加した状態で、同じ条件・5回の中央値を再測定した結果です。
この表の`set_keys()`は、当時の`values`と`frames`を別々に渡す形式です。
現在の`(frame, value)` pair形式への変更前の測定であり、変更後の実測値ではありません。
各versionのプロセスを順に実行し、他のMayaテスト・ベンチとは並行実行していません。
以下は1,000キーの予約＋実行時間（ms）です。

| Maya | 条件 | 旧cmds実装 | `set_key()`の反復 | `set_keys()` |
| --- | --- | --- | --- | --- |
| 2025 | 新規カーブ | 36.44 | 24.25 | 5.23 |
| 2025 | 既存カーブ | 36.18 | 21.67 | 4.54 |
| 2025 | 全キー上書き | 36.40 | 21.94 | 4.84 |
| 2026 | 新規カーブ | 37.79 | 24.22 | 5.67 |
| 2026 | 既存カーブ | 37.19 | 24.61 | 6.05 |
| 2026 | 全キー上書き | 38.64 | 24.43 | 5.65 |
| 2027 | 新規カーブ | 35.75 | 24.52 | 6.05 |
| 2027 | 既存カーブ | 35.46 | 23.74 | 5.81 |
| 2027 | 全キー上書き | 35.64 | 24.39 | 5.73 |

このAPI経路を利用できる構成では、当時の`set_keys()`は`set_key()`の反復より約4.0〜4.8倍、
旧cmds実装より約5.9〜8.0倍高速でした。一括設定のUndoは約1.9〜2.2 ms、
Redoは約1.7〜2.0 msです。レイヤーなどcmdsへ委譲する構成では、同じ速度向上を
保証するものではありません。

2026-09-11に`set_keys()`を`(frame, value)`入力へ変更した後、Maya 2025で
`--keys 1000 --repeats 5`を再測定しました。他のMayaプロセスと並行実行せず、
上記と同じ条件で測定した予約＋実行時間（ms）です。

| 条件 | 旧cmds実装 | `set_key()`の反復 | pair形式の`set_keys()` |
| --- | --- | --- | --- |
| 新規カーブ | 36.79 | 21.83 | 4.89 |
| 既存カーブ | 35.44 | 21.50 | 4.71 |
| 全キー上書き | 35.91 | 21.49 | 5.02 |

pair形式でも`set_key()`の反復より約4.3〜4.6倍高速でした。
各試行でキーの状態とUndo / Redoの復元も確認しています。

### 詳細データAPIの性能測定

`python/bd_util/_dev/maya/benchmark_keyframe_data.py`は、詳細データを専用に測定します。
sceneを毎回破棄するため、作業中のMayaではなく、repository rootから独立したmayapyで
実行します。他のMayaテスト・benchmarkと並行実行せず、versionごとに順番に測定します。

```powershell
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -B `
    .\bakedanuki\bakedanuki-util\python\bd_util\_dev\maya\benchmark_keyframe_data.py `
    --output .\benchmark_results\keyframe_data\current.json
```

既定は100 / 1,000 / 10,000キー、TA / TL / TU、weighted / nonweighted、取得区間10キー、
warm-upを除く5回です。単位はcm / degree / film、global tangentはauto / nonweightedに
固定します。`--keys`、`--window`、`--curve-types`、`--repeats`で条件を変更できます。
`--targets direct base additive override`で、直接接続、layer付き属性の既定ベース、
明示した加算・Override layerを比較できます。省略時は`direct`です。
`--layer-members 500`のように、1 layerに登録する属性数も変更できます（既定1）。
測定対象は最後に登録し、それ以外はキーを持たないtransformのtranslateXです。
scene・layer・属性・既存キーの準備は測定時間に含めません。
`--operations get restore json`で測定群を選べます。準備・検証を除外し、次を個別に記録します。

- 取得: 両詳細APIの全体、既存キーだけ、既存キー上の境界補完、キー間の境界補完、
  constant / linearの範囲外補完。総キー数と返却区間を別々に変える。
- 復元: 全体置換と部分上書きについて、新規・既存を区別する。入力コピー・検証を含む
  予約、`do_it_dg()`、Undo、Redoを分離し、2往復の履歴復元を検査する。
  部分上書きでは入力キー数を固定したまま、移植先の総キー数の影響を測定できる。
- JSON: `to_dict()`、`json.dumps()`、`json.loads()`、`from_dict()`を分離する。
  ファイルI/Oとメモリ使用量は測定対象外。接線を保存しない`set_keys()`との単純な倍率比較はしない。

結果JSONはMaya version、commit、対象実装とbenchmark自身のSHA-256、
接続構成・所属属性数を含む条件、各試行のmsと中央値を含みます。
通常は作業ツリーを読み、`--source-revision 574239b1`を追加すると、checkoutを変更せずに
そのcommitのkeyframe / data / snapshot / target / command各moduleを依存順に読み込んで比較できます。
そのcommitにtarget / command moduleがない場合は読み込みません。過去のcommitで未対応の
layer構成は指定できません。ModifierManager等の共通基盤は
現行実装を使うため、keyframe周辺以外も変更されたcommit間の完全な環境比較ではありません。

2026-09-12のMaya 2025、TL、10,000キー、3回中央値で、`574239b1`と範囲取得改善後を
比較した結果です。単位はms、既存キー取得は10キー、キー間の境界補完は内部10キー＋境界2キーです。

| weighted | 取得条件 | 変更前 | 改善後 |
| --- | --- | --- | --- |
| False | `get_curve_data()`の既存キーのみ | 110.91 | 0.26 |
| True | 同上 | 101.40 | 0.27 |
| False | `get_curve_data()`のキー間境界補完 | 440.10 | 286.46 |
| True | 同上 | 395.35 | 260.04 |

同日、Maya 2026 / 2027でも1,000キー、同じ10キー区間、TA / TL / TUの全組合せで
3回中央値を比較しました。下表は3種類の型とweightedの有無による中央値の最小〜最大です。

| Maya | 既存キーのみ・変更前 → 改善後 | キー間境界補完・変更前 → 改善後 |
| --- | --- | --- |
| 2026 | 10.65〜13.65 → 0.22〜0.29 ms | 46.40〜57.33 → 31.73〜34.28 ms |
| 2027 | 10.33〜13.56 → 0.26〜0.30 ms | 46.64〜51.59 → 30.16〜33.96 ms |

補完なしの取得は指定indexのキーだけを詳細取得します。nonweightedの接線換算には、
範囲外も含めた隣接キーとの時間幅を維持します。境界補完後の再取得も返却範囲に限定しました。
境界補完の元snapshotと作業用カーブは引き続き全キーを扱うため、総キー数への依存は残ります。
この測定値は特定条件の比較で、全体取得や復元を同じ割合で高速化するものではありません。

layer所属確認は単一plugのlayeredPlug照会へ変更し、全属性名の列挙・解決を省略しました。
配列・compoundのlock検査はMPlug.isFreeToChangeで子孫が変更可能か確認し、
通常の未lockカーブでキーごとのMPlugをPythonへ取り出す処理を省略します。
変更不可の場合は従来の個別巡回でlocked plugを特定するため、接続による変更不可とlockを区別します。
いずれも永続キャッシュは使わず、所属・lockはqueryまたは初回実行時に再検査します。

2026-09-14、Maya 2025、TL / nonweighted、1,000キー、3回中央値で、
`9585aef1`と上記の改善後を比較した結果です。layer付き条件の所属属性数は500、
既存キー取得・部分復元は10キーです。復元は予約時間を除いた`do_it_dg()`の時間です。

| 対象 | 操作 | 変更前 | 改善後 |
| --- | --- | --- | --- |
| 加算layer | `get_curve_data()`の既存キーのみ | 7.11 ms | 0.32 ms |
| 加算layer | `get_curve_data()`のキー間境界補完 | 35.18 ms | 28.37 ms |
| 加算layer | `set_key_data()`のカーブ新規作成 | 33.38 ms | 1.20 ms |
| 加算layer | `set_key_data()`の既存キー上書き | 11.87 ms | 0.77 ms |
| 直接接続 | `set_key_data()`の既存キー上書き | 4.42 ms | 0.37 ms |

Maya 2026 / 2027では、加算layer・100所属属性・1,000キー・3回中央値で、
TA / TL / TUとweightedの有無を比較しました。6通りの最小〜最大は次のとおりです。

| Maya | 10キー取得・変更前 → 改善後 | 10キー上書き実行・変更前 → 改善後 |
| --- | --- | --- |
| 2026 | 1.34〜1.52 → 0.25〜0.29 ms | 6.06〜6.70 → 0.53〜0.66 ms |
| 2027 | 1.40〜2.61 → 0.27〜0.30 ms | 6.66〜7.02 → 0.53〜0.62 ms |

Maya 2025の500所属属性の条件を再測定する例です。改善前を測る場合は`--source-revision 9585aef1`を追加し、
出力先を分けます。結果は接続構成・キー数・所属属性数に依存し、全体取得や境界補完が
同じ割合で高速化するわけではありません。

```powershell
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -B `
    .\bakedanuki\bakedanuki-util\python\bd_util\_dev\maya\benchmark_keyframe_data.py `
    --keys 1000 --curve-types animCurveTL --repeats 3 `
    --targets direct base additive override --layer-members 500 --operations get restore `
    --output .\benchmark_results\keyframe_layers\current-maya2025.json
```

追加の改善候補は予約時の重複コピーと、作業用カーブの必要区間への縮小です。
形状・入力検証・独立コピーを保つことを条件に、測定結果から選びます。
回帰確認では区間内の評価値、元カーブの不変性、modified flag、Undo / Redo、例外時の
作業用node解放を維持します。実機検証の入口は`test_keyframe_data.py`と`test_keyframe_clip.py`です。

### 新規layerの先頭サンプルの回帰確認

修正前はMaya 2025 / 2026 / 2027の新規sceneで、以下の先頭値が0、次の値が12となりました。
明示context付きMPlug、現在のcontextを切り替えたMPlug、cmds.getAttr(time=...)でも再現し、
単なる二重読み取りや通常時刻の評価では解消しませんでした。カーブの出力は更新済みでも
下流のtimed contextの入力に古い値が残るケースを、上流出力からのdirty伝播で回避します。
シーン全体へのdgdirtyや現在時刻の往復は使用せず、対象の上流カーブ出力を1回の
`cmds.dgdirty(..., propagation=True)`へ渡し、値はOpenMayaで読み取ります。
修正後の結果は`[(3.0, 12.0), (5.0, 12.0)]`です。検証専用のsceneで実行してください。

```python
from maya import cmds
import bd_util as bdu

cmds.createNode("transform", name="sampling_ctrl")
layer = cmds.animLayer("SamplingLayer")
cmds.setAttr(layer + ".weight", 0.5)
cmds.animLayer(layer, edit=True, attribute="sampling_ctrl.translate")
cmds.setKeyframe("sampling_ctrl.ty", animLayer=layer, time=3, value=12)
ctrl = bdu.Nodes().existing.transform("sampling_ctrl")
print(ctrl.ty.sample_values(frames=[3, 5]))
```

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

## version別生成snapshotの受け入れ確認

新しい対応versionの登録箇所と追加順序は
[Maya Version Support](maya_versions.md)を参照してください。

NodeOperator の生成snapshotはMaya 2025を基準とし、Maya 2026 / 2027の
schema差分をsparse overlayとして保持します。実行時importは実Maya version、
Pyright contractは`typing_maya_version`だけを参照し、両者を独立に検証します。

各versionのsparse overlayは、対応する実Maya環境の`mayapy`で固定plugin profileを
ロードして生成します。生成成功だけでruntime test、Pyright、全体検証まで成功したとは
扱いません。snapshotの受け入れ確認には次の入口を使用します。

```powershell
.\scripts\test-pytest-maya2025.cmd
.\scripts\test-pytest-maya2026.cmd
.\scripts\test-pytest-maya2027.cmd
.\scripts\typecheck-maya-all.cmd
.\scripts\verify.cmd
```

リリース前に3 versionすべてのfull pytestとstaged native plug-inまで確認する場合は、
`.\scripts\verify.cmd -Release`を使用します。snapshotの合否は、この文書の記述ではなく
最新のcommand結果で判断します。

docs変更のみの局所確認には`git diff --check -- <changed-files>`を使用できます。
