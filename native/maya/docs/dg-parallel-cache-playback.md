# DG, Parallel Evaluation, And Cached Playback

この文書は、スクウェア・エニックス公開の技術資料
[Maya のしくみ - 基礎から学ぶ DG とパラレル評価、そしてキャッシュプレイバック](https://www.jp.square-enix.com/tech/library/pdf/BDSeminar20190711.pdf)
を、`bakedanuki-util` の C++ node 開発へ適用するために整理したものです。

資料は2019年7月公開で、主に Maya 2019.1 までを対象としています。DG と node 設計の
原則は現在も重要ですが、個別の evaluator、Cache Playback、Viewport 2.0 の対応状況は
version ごとに変わります。本書では資料の考え方を土台とし、Maya 2025 の API header と
Autodesk の現行資料で補足しています。

## Reading Map

原資料の主な範囲と、この文書での扱いです。

| 原資料 | 主題 | この文書での扱い |
| --- | --- | --- |
| p.17-38 | scene、DG、attribute dependency、node の役割 | node 設計の最重要原則 |
| p.45-80 | Maya API、attribute と data | `MObject` / `MPlug` / `MDataBlock` の責務 |
| p.81-105 | DG の Pull 評価と dirty propagation | `compute()` と遅延評価の基礎 |
| p.106-132 | plug-in node、dirty hook、profiling | 実装規約と性能判断 |
| p.134-218 | Evaluation Manager と Parallel 評価 | EG / SG、scheduling、thread safety |
| p.220-255 | Cached Playback | caching point、background context |
| p.257-294 | evaluator | 特殊評価の位置付け |
| p.295 | まとめ | 本プロジェクトの原則へ変換 |

## Evaluation Layers

Maya の評価機構は、次の層として捉えると整理しやすくなります。

```text
Scene
  nodes / attributes / connections / DAG hierarchy
        |
        v
Dependency Graph (DG)
  attribute 単位の dependency と Pull evaluation
        |
        v
Evaluation Manager (EM)
  Evaluation Graph (EG) -> partitioning -> Scheduling Graph (SG)
        |
        +----> Serial / Parallel Push evaluation
        |
        +----> Evaluators
                 graph の一部を所有・cluster 化・独自評価
        |
        +----> Cache evaluator
                 evaluation result / VP2 data の Cached Playback
```

Parallel 評価は DG を置き換えて無関係になる仕組みではありません。DG で宣言された
dependency を材料に EM が評価 graph と schedule を作ります。元の dependency が不正確
なら、Parallel 評価や Cached Playback の上で自動的に修復されることはありません。

## DG Is An Attribute Graph

DG の dependency の最小単位は node ではなく attribute です。edge は主に次の3種類から
作られます。

1. node 間の attribute connection
2. node 内の `attributeAffects()`
3. DAG node の親子関係による暗黙の dependency

概念上は、attribute が頂点、これらの dependency が有向 edge です。

この区別は node 開発でも重要です。`input` と `output` が同じ node にあるだけでは
依存関係は定義されません。`initialize()` で `attributeAffects(input, output)` を登録
して初めて、Maya は input の変更で output を無効化できます。

### Node Is A Function

原資料が繰り返し強調する設計原則は、node を独立した関数として作ることです。

```text
output = f(inputs)
```

この原則を C++ 実装へ変換すると、次の規約になります。

- 入力 attribute と evaluation context だけから出力を決める。
- 上流 node や下流 node を検索しない。
- 接続先を直接変更せず、自分の output data handle へ結果を書く。
- selection、current scene、UI、node 名などを暗黙の入力にしない。
- 時間に依存するなら time を input として明示する。
- 外部ファイルに依存するなら、その path や更新条件を attribute と API に表す。

「外部の事情を知る node」は DG に dependency を正しく表現できません。DG mode で偶然
動作しても、EM が正しい EG を作れず、Parallel や cache で異なる結果になりやすく
なります。

## DG Pull Evaluation

DG mode は Pull evaluation です。入力変更時に即座に出力を再計算するのではなく、
dependency に沿って dirty flag を伝搬します。

```text
input change
    |
    v
mark downstream output dirty
    |
    v
output requested?
    | no                    | yes
    v                       v
no compute             clean value exists?
                            | yes        | no
                            v            v
                         reuse       compute()
```

`compute()` は dirty な output が実際に要求されたときだけ呼ばれます。上流の入力取得も
同じ仕組みで再帰的に評価され、既に clean な地点で止まります。

この遅延評価には次の利点があります。

- 使用されない branch を計算しない。
- 変更のない clean value を再利用する。
- input を何度変更しても、output が要求されるまで計算をまとめられる。

したがって、`compute()` の呼び出し回数を input 変更回数と同じだと仮定してはいけません。
dirty 通知をイベント callback の代わりに使う実装も、EM では同じ頻度で呼ばれないため
危険です。

## `MDataBlock` Is The Evaluation Boundary

node 内部では `MPlug` より `MDataBlock` と data handle を優先します。

| API | 役割 |
| --- | --- |
| `inputValue()` | 必要なら上流を評価し、現在の context の input handle を得る |
| `inputArrayValue()` | 現在の context の multi input handle を得る |
| `outputValue()` | 上流評価を発生させず output handle を得る |
| `outputArrayValue()` | output array を更新する handle を得る |
| `setClean()` | 計算済み plug / attribute を clean にする |

data block は現在の evaluation context に属します。data handle や data block を
`compute()` の外へ保存すると、次の評価や別 context で無効な参照になる可能性が
あります。

`MPlug` は scene 上の plug の参照、connection の調査、外部からの値操作に使います。
`compute()` で値を取得するために `MPlug::getValue()` を使うと、現在の data block を
外れた Pull evaluation や意図しない dependency を起こしやすくなります。

## From DG To Evaluation Manager

EM は、DG dependency を基に毎フレーム実行可能な Push evaluation の schedule を
準備します。原資料では、次の工程として説明されています。

### 1. Evaluation Graph Construction

time や animated attribute などの起点から dirty propagation を行い、実際に通過した
dependency と下流 node を収集して Evaluation Graph (EG) を作ります。

DG は attribute 単位ですが、通常の EG は node 単位へ単純化されます。EG に入って
いない node は、通常の Push evaluation の対象になりません。

### 2. Partitioning

EG の node を evaluator や cycle の単位で cluster 化します。

- node level の cycle は cycle cluster になる。
- deformer などは専用 evaluator により cluster 化されることがある。
- cluster 内の評価方法は、通常 node とは異なる場合がある。

大きい cycle cluster は serial な塊になり、Parallel 性能のボトルネックになります。

### 3. Scheduling Graph Construction

cluster と単独 node を task として Scheduling Graph (SG) を作ります。各 task の
scheduling type と dependency を考慮して、同時実行可能な task が決まります。

### 4. Push Evaluation

毎フレーム、SG に従って task を実行します。通常の node task では `compute()` が
呼ばれます。DG mode のように毎フレーム graph 全体へ dirty propagation して Pull する
のではなく、構築済み schedule を Push 実行する点が大きな違いです。

scene structure、connection、graph 構成に関わる変更があれば EG / SG は再構築されます。
一方、attribute 値だけで dependency の形が変わる実装は、EM に変更を正しく伝えにくい
設計です。

## Scheduling Type Is A Safety Contract

`MPxNode::schedulingType()` は「速くしてほしい」という hint ではありません。
他 task と同時実行できる安全性を node が表明する contract です。

| Type | Maya に対する表明 |
| --- | --- |
| `kParallel` | 他の node と制約なく同時評価できる |
| `kSerial` | 直接接続された serial node 群の内部では同時評価しない |
| `kGloballySerial` | 同じ scheduling type の node と同時評価しない |
| `kUntrusted` | 他の node が実行されていない状態でのみ評価する |

Maya 2025 の `MPxNode` は default scheduling が `kSerial` です。純粋で thread-safe な
算術 node は明示的に `kParallel` を返します。

強い制約を付ければ thread race を隠せる場合がありますが、それは設計修正では
ありません。まず共有 mutable state を除去し、それが不可能な場合だけ実装上必要な
制約を選びます。

## Parallel-ready `compute()`

Parallel 評価では、異なる node instance の `compute()` が同時に実行されます。
`kParallel` node は次を満たす必要があります。

- file scope / class static / singleton の mutable state を変更しない。
- node instance 間で cache、scratch buffer、logger を無同期に共有しない。
- Maya command、UI、selection、scene mutation を呼ばない。
- thread-safe であることを確認していない third-party library を呼ばない。
- input data handle だけを読み、自分の output data handle だけを書く。
- data handle、data block、Maya 管理下の一時的な `MPlug` を保持しない。
- どの実行順でも同じ入力から同じ出力を返す。

class member は node instance ごとに分かれるため、異なる instance の Parallel 評価だけを
考えると static より安全です。ただし Cached Playback の background context や custom
topology evaluator まで考えると、同じ instance の状態を単一の「現在値」として持つ設計
は安全とは限りません。算術 node は member cache 自体を持たない設計を優先します。

## Compound Plug Requests

原資料では、DG と EM で `compute()` に渡される compound plug の粒度が異なる場合が
あることを指摘しています。

- DG では、実際に要求された child plug が渡される場合がある。
- EM では、top-level compound plug が渡される場合がある。

実装は parent と必要な child の両方を受け付けます。

```cpp
const MObject requested = plug.attribute();
if (
    requested != output
    && requested != outputX
    && requested != outputY
    && requested != outputZ
) {
    return MS::kUnknownParameter;
}
```

`bdDbl3_Multiply` 系 node は既にこの形です。テストでも parent output と各 child output を
個別に要求します。

## `setDependentsDirty()` Under EM

`setDependentsDirty()` には、異なる2つの用途があります。

1. dynamic attribute や multi element ごとの動的 dependency を追加する。
2. DG dirty propagation を hook して node 内部 cache を無効化する。

1の用途は EM でも必要ですが、dependency が attribute 値によって頻繁に入れ替わる
設計は EG 再構築と相性が悪くなります。可能なら dependency は固定し、条件分岐は
`compute()` 内の値の選択に留めます。

2の用途は注意が必要です。EM の通常評価は EG 構築後に DG と同じ dirty propagation を
毎フレーム行わないため、内部 cache の invalidation hook として
`setDependentsDirty()` だけに依存できません。

内部 state が本当に必要な node では、次を検討します。

- DG mode と dynamic dependency のため `setDependentsDirty()` を残す。
- EM mode では `preEvaluation()` / `postEvaluation()` と `MEvaluationNode` から
  dirty source を確認する。
- callback が worker thread から呼ばれる前提で実装する。
- state が evaluation context ごとに独立していることを保証する。

現在の `bdDbl3_Multiply` 系 node は内部 cache を持たないため、この複雑さはありません。

## Cached Playback

Cached Playback は、指定時間範囲の evaluation result を保持し、再生時に scene を毎回
再評価する代わりに cache から値を復元する仕組みです。cache evaluator が EM の
evaluator として動作します。

### Cache Modes

| Mode | 保存対象 | 主なコスト |
| --- | --- | --- |
| Evaluation Cache | node の evaluation data | 復元後、VP2 data への変換・転送が必要 |
| Viewport Software Cache | VP2 用に変換済みの data を main memory に保存 | GPU への転送が必要 |
| Viewport Hardware Cache | VP2 data を GPU memory に保存 | memory 制約があるが描画準備が最小 |

これは2019年資料の整理ですが、Maya 2025 の Evaluation Toolkit にも同じ分類が
残っています。対応 node、fallback 条件、既定 mode は version ごとに確認します。

### Caching Points

すべての node を cache するのは効率的ではありません。cache に保存する node を
caching point と呼びます。

理想的な caching point は、transform や geometry のようにユーザーへ結果を返す
network 下流の少数箇所です。下流結果を cache できれば、その上流全体の評価を省略
できます。

node 開発では「自分の node を必ず cache する」ことを目標にしません。

- downstream の caching point から自分の計算を省略できるか。
- 自分自身を cache することで十分な計算量を削減できるか。
- output data の memory cost に見合うか。
- invalidation 範囲を広げすぎないか。

これらを graph 全体で判断します。

## Background Evaluation Context

Background cache fill は、現在表示中の Maya state とは別の時間を評価します。
`MDGContext` がこの evaluation context を表します。

重要なのは「current context」と「normal context」が常に同一ではないことです。
Maya 2025 の API document も、background evaluation と caching の導入後は両者を
同一視しないよう明記しています。

node 実装では次を守ります。

- `compute()` へ渡された `MDataBlock` の値を使う。
- current time を global API や UI から取得しない。
- time が必要なら input data または data block の context から得る。
- context 固有の中間値は hidden output / internal attribute など data block 内へ置く。
- member cache が必要なら context / time を key にし、invalidating condition を定義する。
- normal context の単一状態を全 background frame で共有しない。

異なる context の結果が class member の1変数を奪い合うと、cache fill の順序によって
結果が変わります。通常の Parallel test だけではこの問題を検出できないため、
background context correctness test が必要です。

## Maya 2025 Cached Playback API

原資料の公開後、Maya 2020 で node 単位の Cached Playback API が追加されています。
Maya 2025 では次を利用できます。

### `getCacheSetup()`

EM partitioning 時に呼ばれ、node の cache 対応方針を伝えます。

- Cached Playback / background evaluation を support する。
- Evaluation Cache の caching point になりたいかを表明する。
- simulation support などの requirement を伝える。
- cache 非対応なら理由と mitigation を報告する。
- 対応可否が attribute 値で変わるなら、その attribute を監視対象へ追加する。

base implementation は Cached Playback 対応と扱いますが、default caching point には
立候補しません。通常の純粋な算術 node は、理由なく override する必要はありません。

### `configCache()`

caching rule の評価後に呼ばれ、cache schema に「どの attribute を cache するか」を
設定します。大きな data を無条件に追加せず、再計算コスト、memory、下流 cache の
有無から選びます。

### `transformInvalidationRange()`

ある時間範囲の変更が、下流ではどの時間範囲を無効化するかを変換します。
simulation や time remapping など、同一 frame の1対1 dependency でない node が対象
です。単純な frame-local 算術 node には不要です。

この関数は dirty propagation 中に呼ばれるため、値の評価や scene mutation を
行いません。

### Caching Rules Take Priority

`getCacheSetup()` の preference より caching rule が優先されます。node が caching point
を希望しても必ず cache されるとは限らず、逆に rule が明示的に追加することも
あります。実際の caching point は Evaluation Toolkit または `cacheEvaluator` で
確認します。

## Custom Evaluators

evaluator は EG の node を所有し、cluster 化、scheduling、実行処理を override できます。
標準 DG node の `compute()` より広い権限を持つ仕組みです。

用途の例は次の通りです。

- 特殊な subsystem を正しい順序で評価する。
- 複数 node を1 cluster として効率化する。
- 通常 node より細かな粒度の evaluation topology を作る。
- 特定条件の node 評価を省略する。

これは通常 node の最適化手段ではなく、独立した node 実装では解決できない問題への
最終手段です。custom evaluator は graph ownership、priority、cache evaluator との
境界、thread safety を別途設計する必要があります。

新しい算術 node では、まず DG の基本に忠実な `MPxNode` として正しく実装します。
「素の EM で正しく効率的に動く」状態が最も保守しやすい設計です。

## Performance Lessons

### DG Cost Is Not Only `compute()`

原資料の `dgtimer` 例では、個々の `compute()` が軽い複雑な rig で、dirty propagation
と value fetch の system cost が大きな割合を占めています。

性能調査では次を分けて見ます。

- node 自身の `compute()` time
- `compute()` count
- dirty propagation count / time
- upstream fetch count / time
- callback と drawing cost

算術を数命令減らすより、過剰な dependency や不要な connection を減らす方が効果的な
場合があります。ただし dependency を性能目的で削る前に correctness test を追加
します。

### Parallel Cost Is Graph-shaped

Parallel 性能は node 単体の速度だけでなく、graph topology に左右されます。

- 独立 branch が多いほど並列化しやすい。
- 長い直列 chain は core 数を増やしても短縮しにくい。
- 大きな cycle cluster は serial bottleneck になる。
- `kGloballySerial` / `kUntrusted` task は同時実行範囲を狭める。
- 極端に小さい task が大量にあると scheduling overhead が相対的に増える。

Profiler では task の時間だけでなく、SG 上で同時実行できている幅を確認します。

### Cache Cost Is Memory-shaped

Cached Playback は計算時間を memory と cache fill time に交換します。

- caching point が多すぎると memory を消費する。
- 大きな geometry data は cache mode によって RAM / VRAM を消費する。
- input 変更で広い時間範囲を invalidation すると再生成コストが増える。
- background fill 中の node が context-safe でないと correctness を失う。

cache の有無だけでなく、使用 memory、fill time、invalidation 範囲、再生速度を測定
します。

## Diagnostic Ladder

評価結果が異なる場合は、機能を一度に全部疑わず、層ごとに切り分けます。

| Result | Likely area |
| --- | --- |
| DG から誤る | `compute()`、`attributeAffects()`、clean 処理、cycle |
| DG は正しく Serial EM で誤る | EG に見えない dependency、compound request、外部状態 |
| Serial EM は正しく Parallel EM で誤る | thread race、共有 mutable state、thread-unsafe API |
| Parallel EM は正しく cache で誤る | evaluation context、member cache、cache schema / invalidation |
| Evaluation Cache は正しく VP2 cache で誤る | draw override、geometry update、VP2 data |
| 特定 evaluator の ON 時だけ誤る | evaluator ownership、cluster 境界、version 固有の evaluator |

Serial EM は DG と同じ「単なる1 thread mode」ではありません。Parallel と同じ EG / SG
機構を serial 実行するため、DG と Serial の比較で graph construction の問題を、
Serial と Parallel の比較で thread safety の問題を分離できます。

## Application To Current Nodes

| Concern | `bdDbl3_Multiply` / `bdDbl3_MultiplyMulti` |
| --- | --- |
| Function model | input double3 だけから output double3 を決める |
| Dependency | static `attributeAffects()` で明示 |
| Data access | `MDataBlock` / data handle のみ |
| Compound request | parent と X / Y / Z child を処理 |
| Multi | existing physical element を走査し sparse index に対応 |
| Shared state | なし |
| Scheduling | explicit `kParallel` |
| Evaluation context | member state と global time を使わないため context-independent |
| Cached Playback API | 現時点では override 不要 |
| Custom evaluator | 不要 |

現行2 node は、原資料が理想とする独立した関数型 node の最小例になっています。

## Development Checklist

### Dependency

- [ ] すべての output は input attribute から決定できる。
- [ ] connection、`attributeAffects()`、DAG hierarchy で dependency が表現される。
- [ ] time dependency を global current time へ隠していない。
- [ ] parent / child / multi element の dirty test がある。
- [ ] attribute 値で dependency graph 自体を切り替えていない。

### Evaluation

- [ ] `compute()` は `MDataBlock` 内だけで値を読み書きする。
- [ ] DG と EM のどちらで渡されても output plug を認識できる。
- [ ] data block / handle / Maya 管理の一時参照を保持しない。
- [ ] member cache が本当に必要か再検討した。
- [ ] `setDependentsDirty()` を dirty event callback として過信していない。

### Parallel

- [ ] mutable static / global / singleton state がない。
- [ ] third-party code を含め thread-safe である。
- [ ] scheduling type が実装上の安全性と一致する。
- [ ] DG、Serial EM、Parallel EM の結果が一致する。
- [ ] Profiler と SG で実際の並列性を確認した。

### Cached Playback

- [ ] background evaluation で normal context を仮定していない。
- [ ] context 固有の値を単一 member へ保存していない。
- [ ] cache 前後で結果が一致する。
- [ ] input 変更後に必要な frame 範囲が invalidation される。
- [ ] caching point と memory cost を確認した。
- [ ] `getCacheSetup()` / `configCache()` が本当に必要な node だけ実装した。

### Advanced Systems

- [ ] geometry output なら topology tracking と VP2 update を別途確認した。
- [ ] simulation なら restart と invalidation range を設計した。
- [ ] custom evaluator は通常 node で解決できない理由を文書化してから検討した。
- [ ] Maya version 固有の evaluator や workaround を固定仕様にしていない。

## Version-specific Cautions

原資料の次の内容は Maya 2019 当時の観測または version 固有情報として扱います。

- Maya version 別 benchmark 数値
- Legacy Viewport と当時の VP2 の比較
- evaluator の一覧、priority、default enabled state
- Cache Playback の非対応 node 一覧
- Cache rule の具体的な既定 node type
- 当時の Maya bug や workaround
- minor version ごとの geometry override callback

これらを実装判断へ使う場合は Maya 2025 の実機、local devkit sample、現行 Autodesk
document で再確認します。

## References

### Source Material

- [Maya のしくみ - 基礎から学ぶ DG とパラレル評価、そしてキャッシュプレイバック](https://www.jp.square-enix.com/tech/library/pdf/BDSeminar20190711.pdf)

### Maya 2025 And Current API

- [MPxNode C++ API Reference](https://help.autodesk.com/cloudhelp/2027/ENU/MAYA-API-REF/cpp_ref/class_m_px_node.html)
- [MDGContext Maya 2025 C++ API Reference](https://help.autodesk.com/cloudhelp/2025/ENU/MAYA-API-REF/cpp_ref/class_m_d_g_context.html)
- [Evaluation Toolkit](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Customizing/files/GUID-E22B253D-914B-4056-93F5-755702A6C998.htm)
- [Evaluator Reference](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Customizing/files/GUID-27845E36-B873-42EB-B06F-9FE983E1080D.htm)
- [Cached Playback](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Customizing/files/GUID-D3D1DC33-D0CE-4BE3-B287-CDD4DC0B72C3.htm)
- [cacheEvaluator command](https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/Commands/cacheEvaluator.html)
- [MNodeCacheSetupInfo C++ API Reference](https://help.autodesk.com/cloudhelp/2024/ENU/MAYA-API-REF/cpp_ref/class_m_node_cache_setup_info.html)
