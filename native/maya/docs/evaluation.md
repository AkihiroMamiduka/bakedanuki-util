# Evaluation And Parallelism

Maya node の正しさと並列性能は、`compute()` の計算式だけでは決まりません。
attribute 間の依存関係を正しく宣言し、Maya が dirty な出力と安全な実行順を判断できる
ようにする必要があります。

DG、Evaluation Graph、Scheduling Graph、Cached Playback までを含む全体像は
[DG, Parallel Evaluation, And Cached Playback](dg-parallel-cache-playback.md) を
参照してください。

## Dirty Propagation

Maya の dependency graph は、値が変化したときに関連する出力をすぐ再計算するのでは
なく、まず dirty として記録します。その出力値が実際に要求された時点で
`compute()` が呼ばれます。

典型的な流れは次の通りです。

1. input plug の値または接続元が変化する。
2. `attributeAffects()` で宣言した output plug が dirty になる。
3. 接続先へ dirty が伝搬する。
4. dirty な値が要求されたときだけ `compute()` が呼ばれる。
5. 計算済み output を clean にする。

この仕組みにより、変更と無関係な node や、最終的に値を要求されない branch の計算を
省略できます。逆に dirty 依存関係が不足すると、入力を変更しても古い出力が clean の
まま再利用され、見た目上ランダムな stale value になります。

## `attributeAffects()`

static attribute 間の依存関係は、node の `initialize()` 内で
`MPxNode::attributeAffects(input, output)` を呼んで宣言します。

```cpp
status = attributeAffects(input, output);
if (!status) {
    return status;
}
```

これは「input が dirty になったら output も dirty にする」という方向付きの関係です。
値を計算するコードではなく、Maya が評価 graph を作るための metadata です。

### Compound の方針

`double3` のような compound は、親と子のどちらも直接編集・接続・要求されます。
`bdDouble3Mult` 系 node は、入力の親・子を列挙し、それぞれから output 親への関係を
登録します。

```cpp
const std::array<MObject, 4> inputs = {
    input,
    inputX,
    inputY,
    inputZ,
};

for (const MObject& inputAttribute : inputs) {
    status = attributeAffects(inputAttribute, output);
    if (!status) {
        return status;
    }
}
```

Maya 2025 では output compound 親への affects は X / Y / Z の子にも展開されます。
逆に `inputX -> outputX` だけを登録しても、affected attributes は output 親と全子に
展開されます。そのため、親・子の全組み合わせを登録する必要はありませんが、output
compound の dirty を XYZ ごとに分離する最適化にもなりません。

compound の親変更、各 child の直接変更、parent / child connection、各 output child の
直接要求を Maya 上でテストすることが前提です。XYZ ごとに独立した dirty branch が必要な
場合は、compound ではなく独立した scalar output を API として設計する必要があります。

### 過不足の影響

| 宣言 | 結果 |
| --- | --- |
| 必要な関係が不足 | 出力が再計算されず、古い値が残る |
| 不要な関係を追加 | 正しさは保ちやすいが、不要な dirty と再計算が増える |
| input / output の向きを逆にする | 期待した dirty 伝搬が起きない |
| 親だけをテストする | 子 plug を直接変更・接続した場合の問題を見逃す |

最初は正しい範囲を明示し、性能上の根拠がある場合だけ依存関係を狭めます。

## Dynamic Or Conditional Dependencies

`attributeAffects()` は `initialize()` で追加した static attribute に対して使います。
runtime に追加される dynamic attribute や、node の状態によって依存先が変わる場合は
`setDependentsDirty()` を検討します。

`setDependentsDirty()` は dirty 伝搬中に呼ばれます。この関数では affected plug を
追加するだけに留め、次の操作を行いません。

- plug の値を要求して DG evaluation を発生させる。
- output を計算する。
- connection や scene を変更する。
- 評価順に依存する mutable な副作用を起こす。

DG mode では dirty hook としても呼ばれますが、EM は Evaluation Graph 構築後の
通常評価で同じ dirty propagation を毎フレーム行いません。node 内部 cache の無効化を
`setDependentsDirty()` だけに依存させると、Serial / Parallel EM で古い member value を
使う可能性があります。内部 state が本当に必要なら、DG 用の
`setDependentsDirty()` に加えて `preEvaluation()` / `postEvaluation()` と
`MEvaluationNode` を設計します。

通常の固定 attribute の算術 node には `attributeAffects()` だけで十分です。
単純な node に `setDependentsDirty()` を追加しても品質は上がらず、依存関係が追いにくく
なります。

## Evaluation Manager

Evaluation Manager は dirty propagation の情報から Evaluation Graph (EG) を構築し、
cycle や evaluator 単位の partitioning を行い、Scheduling Graph (SG) を作ります。
毎フレームは SG に従って Push evaluation します。独立した branch は並列に評価でき
ますが、接続や依存関係で順序が必要な node は、その順序を守って評価されます。

したがって次の2点は別の責務です。

- `attributeAffects()` は、どの入力変更がどの出力を無効化するかを表す。
- `schedulingType()` は、同時実行しても安全な node の範囲を表す。

`kParallel` を返しても、不足した dirty 依存関係は補われません。
`kSerial` にしても、不正な依存関係や副作用が正しくなるわけではありません。

## Scheduling Types

`MPxNode::schedulingType()` の選択肢は次の通りです。

| Type | 同時実行の制約 | 主な用途 |
| --- | --- | --- |
| `kParallel` | 他 node と制約なく並列評価できる | data block だけで完結する純粋な計算 |
| `kSerial` | 接続された serial node 群の中では直列になる | 接続関係の中で順序・共有状態の制約がある |
| `kGloballySerial` | 同じ node type 同士を同時評価しない | type 全体で共有する資源がある |
| `kUntrusted` | 他の node と同時評価しない | Maya 全体への副作用など、安全性を保証できない |

Maya 2025 の `MPxNode` base implementation は `kSerial` が default です。
純粋で thread-safe な node は、`kParallel` への対応を明示します。

安全性を確認できない node を推測で `kParallel` にしません。一方、純粋な算術 node を
保守的に serial 化すると、大規模 rig で並列性を失います。node の実装条件から選びます。

## Conditions For `kParallel`

次をすべて満たす node は `kParallel` の候補です。

- `compute()` が `MDataBlock` の入力だけを読む。
- `compute()` が自分の `MDataBlock` の出力だけを書き換える。
- file scope / class static / singleton の mutable state を共有しない。
- global cache、logger、allocator などを競合する形で変更しない。
- Maya command の実行、selection 変更、node 作成、connection 変更を行わない。
- UI、viewport、main-thread 専用 API に触れない。
- data block や handle を評価終了後まで保持しない。
- 同じ入力と context から決定的な結果を返す。
- instance cache を使う場合は、同じ node の評価 context と thread safety を設計済みである。

mutex で共有状態を保護すれば crash は防げる場合がありますが、評価が実質的に直列化
され、lock 順による問題も増えます。算術 node では共有状態自体を持たない設計を優先
します。

`bdDouble3Mult` と `bdDouble3MultMulti` は data block 内だけで計算し、共有 mutable
state を持たないため `kParallel` です。

## Evaluation Callbacks

通常の算術 node は `compute()` と `schedulingType()` だけで十分です。
内部 cache や evaluation ごとの準備が必要になった場合に限り、`preEvaluation()` /
`postEvaluation()` を検討します。

これらは worker thread から呼ばれる可能性があります。実装する場合は次を守ります。

- thread-safe かつ non-blocking な処理にする。
- node instance が所有するデータだけを扱う。
- main thread や UI を必要とする処理を入れない。
- 同じ node が異なる evaluation context で使われる可能性を考慮する。
- context 固有の状態を単一の class member へ保存しない。

callback を追加する前に、本当に `compute()` と data block だけでは表現できないかを
確認します。

## Cached Playback

Cached Playback の background fill では、現在表示中とは異なる時間の
evaluation context で同じ scene を評価します。node は global current time や normal
context の class member state に依存せず、`MDataBlock` 内の context-specific data から
結果を作ります。

Maya 2025 では `getCacheSetup()`、`configCache()`、
`transformInvalidationRange()` を override できます。ただし、base implementation は
Cached Playback を support し、default caching point には立候補しません。単純な算術
node は、特別な cache preference、simulation、時間範囲変換がない限り override 不要
です。

cache 対応の設計と検証は
[DG, Parallel Evaluation, And Cached Playback](dg-parallel-cache-playback.md) を
参照してください。

## Performance Guidelines

### 固定入力と multi 入力

入力数が常に2つなら、固定 input 版は multi 版より処理が単純です。

- `MDataHandle` を2回取得するだけでよい。
- array element 数の取得と iterator 移動がない。
- sparse index を扱う分岐がない。

ただし、1 node 当たりの差は小さいことが多く、graph の接続、dirty 範囲、計算回数の
方が支配的になり得ます。固定版は「2入力という API を明示できる」ことも重要な利点
です。性能差は [Testing And Debugging](testing-debugging.md) の方法で Release build
を計測して判断します。

### Compute の内側

- loop 内で不要な allocation、文字列検索、`MPlug` 構築をしない。
- attribute は static `MObject` から参照する。
- 入力 handle を必要な回数だけ取得する。
- 高コストで独立した複数 output は、要求 plug に応じた遅延計算を検討する。
- 小さな compound output は、一度に計算してまとめて clean にする。
- cache は、再計算コストが同期・無効化コストを明確に上回る場合だけ追加する。

micro optimization の前に、不要な dirty propagation と意図しない再評価がないかを
確認します。

## Validation Order

評価に関する不具合は、次の順番で切り分けます。

1. **DG mode**
   - dirty 依存関係と `compute()` 自体の正しさを確認する。
2. **Serial EM**
   - Evaluation Manager が作った graph を1 thread で確認する。
3. **Parallel EM**
   - 同じ graph の同時実行にだけ問題がないか確認する。

DG で誤る場合は、まず `attributeAffects()`、要求 plug の判定、clean 処理を調べます。
Serial EM だけで誤る場合は、Evaluation Manager へ見えていない依存関係や副作用を
疑います。Serial が正しく Parallel だけで誤る場合は、共有 mutable state、
thread-unsafe API、context 非対応 cache を疑います。

## Autodesk References

- [Dirty Propagation](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-DEVHELP/files/Dependency-graph-plug-ins/Maya_DEVHELP_Dependency_graph_plug_ins_DirtyPropagation_html.html)
- [MPxNode C++ API Reference](https://help.autodesk.com/cloudhelp/2027/ENU/MAYA-API-REF/cpp_ref/class_m_px_node.html)
- [MDataBlock C++ API Reference](https://help.autodesk.com/cloudhelp/2027/ENU/MAYA-API-REF/cpp_ref/class_m_data_block.html)
- [Using the Evaluation Manager](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-Customizing/files/GUID-190D97E7-9AC0-4D67-8A07-1AF3A9DBAF15.htm)
- [Troubleshoot Evaluation Manager correctness](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-Customizing/files/GUID-4EDEF082-0EAC-493B-9256-647A8F6BD039.htm)
