# Dependency Node Basics

この文書は、`bdUtilNodes` に C++ dependency node を追加するときの基本手順と
実装上の約束をまとめたものです。

## Node Lifecycle

Maya plug-in と node は、概ね次の順番で初期化・評価されます。

1. Maya が `.mll` をロードし、`initializePlugin()` を呼ぶ。
2. `MFnPlugin::registerNode()` が node type、`MTypeId`、`creator()`、
   `initialize()` を Maya へ登録する。
3. 登録時に static な `initialize()` が呼ばれ、attribute と依存関係が作られる。
4. `createNode` や scene load により、`creator()` が node instance を生成する。
5. dirty な output が要求されると、Maya が `compute()` を呼ぶ。
6. plug-in のアンロード時に `uninitializePlugin()` が node を登録解除する。

主な責務は次の通りです。

| 関数 | 責務 |
| --- | --- |
| `creator()` | node instance を確保して返す |
| `initialize()` | static attribute の作成、追加、依存関係の登録 |
| `compute()` | data block の入力から要求された出力を計算する |
| `schedulingType()` | Evaluation Manager に thread safety の制約を伝える |
| `initializePlugin()` | Maya へ node type を登録する |
| `uninitializePlugin()` | node type を登録時と逆順に解除する |

constructor では、まだ node 自身の `MObject` を必要とする処理を行えません。
instance の初期化に Maya の node object が必要な場合は `postConstructor()` を使います。
static attribute の定義は constructor ではなく `initialize()` に置きます。

## Files And Names

1 node は原則として、宣言用 header と実装用 source に分けます。

```text
plugins/bdUtilNodes/
  include/bdUtilNodes/BdExampleNode.h
  src/BdExampleNode.cpp
  src/plugin.cpp
```

node class は、少なくとも次の static member を持ちます。

```cpp
class BdExampleNode : public MPxNode {
public:
    static void* creator();
    static MStatus initialize();

    MStatus compute(const MPlug& plug, MDataBlock& dataBlock) override;
    SchedulingType schedulingType() const override;

    static const MString typeName;
    static const MTypeId typeId;
    static MObject input;
    static MObject output;
};
```

`typeName` は `createNode`、Maya ASCII、Python API などで参照されます。
`MTypeId` は scene 内で node type を識別します。新しい ID は実装前に
[Node ID Registry](../NODE_IDS.md) へ登録してください。

開発初期の現在は API を変更できますが、production scene で使い始めた後は
`typeName`、`MTypeId`、attribute の long name / short name を永続 API として
扱います。

## Attribute Definition

attribute は function set で作成し、必要な flag を設定してから
`MPxNode::addAttribute()` で node へ追加します。

入力と出力の標準的な flag は次の通りです。

| Flag | Input | Output | 意味 |
| --- | --- | --- | --- |
| `readable` | `true` | `true` | plug から値を読める |
| `writable` | `true` | `false` | 外部から値を設定・接続できる |
| `storable` | `true` | `false` | 値を scene に保存する |
| `keyable` | 必要に応じて `true` | `false` | channel box から key を設定できる |
| `array` | multi の場合のみ `true` | 必要な場合のみ | multi attribute として扱う |
| `usesArrayDataBuilder` | array を builder で編集する場合 | 同左 | array data builder を利用する |

出力を `writable=false`、`storable=false` にすることで、出力が外部入力や保存値ではなく
計算結果であることを示します。

### Compound Attribute

`double3` は親 attribute と X / Y / Z の子 attribute からなる compound です。
親と子の `MObject` をすべて保持すると、次の処理を明示できます。

- 子 plug を直接接続・編集する。
- 親または子が要求された場合に `compute()` で処理する。
- 親・子それぞれの dirty 依存関係を `attributeAffects()` へ登録する。

乗算 node の入力 default は、乗法単位元の `(1.0, 1.0, 1.0)` です。default 値は
「未接続時に自然な結果になるか」を演算ごとに決めます。加算なら `0`、乗算なら `1`
のように、node の意味と一致させます。

## `compute()` Contract

`compute()` は、要求された plug が自分の計算対象かを最初に判定します。
対象外の plug には `MS::kUnknownParameter` を返し、Maya 側の標準処理へ委ねます。

```cpp
const MObject requestedAttribute = plug.attribute();
if (
    requestedAttribute != output
    && requestedAttribute != outputX
    && requestedAttribute != outputY
    && requestedAttribute != outputZ
) {
    return MS::kUnknownParameter;
}
```

計算本体では `MDataBlock` から入力 handle を取得し、出力 handle へ結果を書きます。

```cpp
MStatus status;
MDataHandle inputValue = dataBlock.inputValue(input, &status);
if (!status) {
    return status;
}

MDataHandle outputValue = dataBlock.outputValue(output, &status);
if (!status) {
    return status;
}

outputValue.setDouble(inputValue.asDouble() * 2.0);
outputValue.setClean();
return dataBlock.setClean(plug);
```

実装時は次を守ります。

- 入力は `inputValue()` / `inputArrayValue()` から読む。
- 出力は `outputValue()` / `outputArrayValue()` だけに書く。
- 取得、attribute 追加、登録などが返す `MStatus` を確認する。
- 計算が完了した output を clean にする。
- `MDataBlock`、`MDataHandle`、`MArrayDataHandle` を `compute()` の外へ保持しない。
- `compute()` から scene を変更したり、MEL / Python command を実行したりしない。
- 同じ入力と evaluation context には、同じ出力を返す。

親 compound を一度に計算する node では、X / Y / Z のどれが要求されても親出力を
一度書く現在の実装が単純です。複数の独立した高コスト出力を持つ node では、
要求された output ごとに計算を分ける方が無駄を減らせます。

## Multi Attribute

Maya の multi attribute は sparse です。logical index が `0, 1, 2` と連続している
とは限らず、`input[0]` と `input[10]` だけが存在することもあります。

全既存要素を処理する場合は、`elementCount()` と physical iteration を使います。

```cpp
MStatus status;
MArrayDataHandle inputArray = dataBlock.inputArrayValue(input, &status);
if (!status) {
    return status;
}

const unsigned int count = inputArray.elementCount(&status);
if (!status) {
    return status;
}

for (unsigned int physicalIndex = 0; physicalIndex < count; ++physicalIndex) {
    MDataHandle value = inputArray.inputValue(&status);
    if (!status) {
        return status;
    }

    // value を処理する。

    if (physicalIndex + 1 < count) {
        status = inputArray.next();
        if (!status) {
            return status;
        }
    }
}
```

用語を区別してください。

| 操作 | 用途 |
| --- | --- |
| `elementIndex()` | 現在位置の logical index を得る |
| `next()` | 次に存在する physical element へ進む |
| `jumpToElement(logicalIndex)` | 指定した logical index を検索する |
| `jumpToArrayElement(physicalIndex)` | 指定した physical position へ移動する |

全要素の積のように index 自体が不要な処理では、logical index を読まず `next()` で
既存要素だけを走査します。空配列の結果は演算の単位元から決めます。
`bdDbl3_MultMulti` では `(1.0, 1.0, 1.0)`、`bdDbl_MultMulti` では
`1.0` です。加算の `bdDbl3_AddMulti` と `bdDbl_AddMulti` では、それぞれ
`(0.0, 0.0, 0.0)` と `0.0` です。

array output を構築・変更する node では `MArrayDataBuilder` を使い、必要な element
だけを追加した後で array handle へ戻します。入力 array の走査と、出力 array の構築を
混同しないようにします。

## Stored Value Nodes

`bdDbl_Value`と`bdDbl3_Value`は計算結果ではなく、sceneに保存する値そのものを
`value` plugとして公開します。double3版は`valueX`、`valueY`、`valueZ`の子plugを
持ちます。defaultはdoubleが`0`、double3が`(0, 0, 0)`です。

`value`は既存のinput attributeと同様にreadable、writable、storable、keyableです。
そのため直接値を設定して接続元にできるだけでなく、別plugから接続を受けながら同じ
plugを接続元にする中継も可能です。incoming connectionがある場合は定数ではなく、
接続された値を渡すvalue nodeとして扱います。

```text
source.output -> value.value -> target.input
```

ノード内で別のoutputへ値をコピーしないため、`compute()`、`attributeAffects()`、
`schedulingType()`は実装しません。`value`の直接変更、keyframe、incoming connectionの
更新によるdownstream dirty伝搬とscene保存はMayaのplug機構へ任せます。node memberへの
値cacheも持ちません。

## Native Node Type Naming

`bdUtilNodes`の数値node typeは、次の順序で命名します。

```text
bd<TypeCode>_<Operation><Variant>
```

現行のtype codeは次のとおりです。Mayaの`double`と`double3`を短く保ちつつ、
1文字だけの略号より読みやすい`Dbl`と`Dbl3`を使います。

| Maya type | Type code |
| --- | --- |
| `double` | `Dbl` |
| `double3` | `Dbl3` |

固定入力版、単項演算、value nodeなど、その演算の基本形にはvariant suffixを付けません。
配列入力版だけ`Multi`を付けます。固定2入力版に`Pair`は付けません。
type code直後の`_`は、Node Editorで`bdDbl_`または`bdDbl3_`まで入力したときに、
対象のattribute型だけを候補へ絞り込むための区切りです。operationとvariantの間には
追加の`_`を入れません。

```text
bdDbl_Add
bdDbl_AddMulti
bdDbl3_Add
bdDbl3_AddMulti
bdDbl3_Lerp
bdDbl3_Value
```

node type名はNode Editorの入力候補だけでなく、Python API、Profiler、エラー、scene
fileにも現れます。未使用の型に対する1文字略号を先に予約せず、新しい型を追加するときに
意味が衝突しないtype codeを個別に決めます。

Python側では、Maya node type、class、moduleを次のように変換します。

| Surface | Example |
| --- | --- |
| Maya node type | `bdDbl3_AddMulti` |
| Python class | `BdDbl3AddMulti` |
| Generated class | `GeneratedBdDbl3AddMulti` |
| Python module | `bd_dbl3_add_multi.py` |
| `NodeCreator` method | `nodes.create.bdDbl3_AddMulti()` |

Maya node typeの`_`はPython class名ではPascalCaseの単語境界として除去します。
module名はsnake_caseへ正規化し、Creator methodはMaya node typeをそのまま公開します。

## Arithmetic Node Family Policy

加算、乗算など、複数入力を自然に畳み込める演算では、原則として固定2入力版と
配列入力版を1組で検討します。

| Variant | Type name | Input attributes | Primary use |
| --- | --- | --- | --- |
| 固定2入力版 | `bd<TypeCode>_<Operation>` | `input1`、`input2` | 2値だけの演算、明確なAPI |
| 配列入力版 | `bd<TypeCode>_<Operation>Multi` | `input[]` | 3値以上の集約、node数の削減 |

double乗算では `bdDbl_Mult` と `bdDbl_MultMulti`、double3乗算では
`bdDbl3_Mult` と `bdDbl3_MultMulti` を使います。加算も同様に、doubleでは
`bdDbl_Add` と `bdDbl_AddMulti`、double3では `bdDbl3_Add` と
`bdDbl3_AddMulti` を使います。出力名はどちらも `output` とし、固定版と配列版で
演算結果の型を揃えます。

この方針を適用する演算は、次の条件を満たすものです。

- 3入力以上へ拡張する利用場面がある。
- 入力列をfoldする演算として意味を明確に定義できる。
- 空配列の結果となる単位元、または明示的な空入力仕様を定義できる。
- 配列版によるnode数と中間plugの削減に実用上の価値がある。
- Maya標準nodeで十分に代替できないか、package固有nodeを持つ理由がある。

代表的な判断は次の通りです。

| Operation | Variant policy | Empty multi | Notes |
| --- | --- | --- | --- |
| 加算 | 原則2種類を作る | `0` | scalar、component-wiseとも自然 |
| 乗算 | 原則2種類を作る | `1` | scalar、component-wiseとも自然 |
| 減算 | 個別仕様で2種類 | `0`（明示仕様） | logical index昇順の左畳み込み |
| 除算 | 個別仕様で2種類 | `1`（明示仕様） | logical index昇順、安全な除数下限 |
| 論理AND | 必要に応じて2種類 | `true` | 全入力がtrueかを返す |
| 論理OR | 必要に応じて2種類 | `false` | いずれかの入力がtrueかを返す |
| 最小・最大 | 個別検討 | 型と用途ごとに決定 | 無限値や未定義状態を含めて決める |
| 累乗 | 個別仕様で2種類 | `1`（明示仕様） | logical index昇順の左畳み込み、負指数のみ底を補正 |
| 平均 | 個別検討 | 自然な結果なし | 空入力と除数0の仕様が必要 |
| 線形補間 | 固定版のみ | 該当なし | 2値間を補間し、weightを`0`から`1`へclamp |
| 加重和 | Multiのみ | `0` | value/weightのcompound配列、正規化なし |
| 行列・Quaternion乗算 | 個別検討 | identity | 入力順序を永続APIとして定義する |
| normalize、clamp、lerp | 通常は固定仕様 | 該当なし | 多入力への拡張が自然ではない |

API上で入力順を区別しない積や和では、既存elementのphysical iterationを利用できます。
非可換演算や結合順序をAPIに含める演算では、physical storage orderを演算順序として
暗黙に使いません。logical index順などの規則を明文化し、sparse indexを含むsceneで
テストします。

`bdDbl_SubMulti` と `bdDbl3_SubMulti` は、存在する要素をlogical indexの昇順に
並べ、最小indexの値から残りを順に減算します。例えばindex `2`、`7`、`20`が存在する
場合は `input[2] - input[7] - input[20]` です。1要素ならその値、空配列なら明示仕様の
`0` または `(0, 0, 0)` を返します。

### Safe Division Policy

`bdDbl_Div`、`bdDbl3_Div`とその配列版は、除数の絶対値が`1e-9`未満の場合、
符号を維持した`1e-9`へ置換してから除算します。判定は各除算、double3では各成分へ
独立に適用します。配列版の最初の既存要素は分子なので置換せず、2要素目以降だけを
安全な除数として扱います。

固定2入力版の`input1`、`input2`、`output`はすべて`1`をdefaultとし、作成直後は
`1 / 1 = 1`となります。配列版の入力elementとoutputも同じく`1`をdefaultとします。

```cpp
if (std::abs(divisor) < 1.0e-9) {
    divisor = std::copysign(1.0e-9, divisor);
}
```

`1e-9`はdouble型の表現限界ではなく、このpackageでリグ計算を安定させるための
除数下限です。epsilon未満の非zero値も同じ規則でclampし、zeroだけが非連続な結果に
ならないようにします。`compute()`からwarningは出さず、同じ規則を除算を含む今後の
演算nodeでも共通利用します。

`bdDbl_DivMulti`と`bdDbl3_DivMulti`も存在する要素をlogical index昇順に並べ、
最小indexの値から左畳み込みします。1要素ならその値、空配列なら明示仕様の`1`または
`(1, 1, 1)`を返します。

### Safe Power Policy

`bdDbl_Pow`、`bdDbl3_Pow`とその配列版は、`input1`を底、`input2`を指数として
累乗します。double3ではXYZ成分ごとに独立して計算します。固定2入力版の入力と出力の
defaultはすべて`1`です。

指数が負の場合、累乗は底を分母に持つ除算を含みます。その場合だけ底へ
`safeDivisor()`を適用し、絶対値が`1e-9`未満なら符号を維持した`1e-9`へ置換します。
指数がzero以上の場合は、`0 ^ n = 0`という有効な結果を変えないため補正しません。

```cpp
if (exponent < 0.0) {
    base = safeDivisor(base);
}
result = std::pow(base, exponent);
```

`0 ^ 0`は`std::pow()`に従って`1`とします。負の底と非整数指数は`NaN`、表現範囲を
超える結果は`inf`、underflowは`0`とし、追加のclampやwarningは行いません。

`bdDbl_PowMulti`と`bdDbl3_PowMulti`は存在する要素をlogical index昇順に並べ、
最小indexを底として左畳み込みします。index `2`、`9`、`20`が存在する場合は
`(input[2] ^ input[9]) ^ input[20]`です。1要素ならその値、空配列なら明示仕様の`1`
または`(1, 1, 1)`を返します。各段階で指数が負の場合、その時点の計算結果である底へ
同じepsilon補正を適用します。

### Lerp Policy

`bdDbl_Lerp`と`bdDbl3_Lerp`は、`input1`から`input2`への線形補間を行います。
double3版も`weight`はscalar doubleで、XYZへ同じweightを適用します。

```text
output = input1 * (1 - weight) + input2 * weight
```

`weight`のdefaultは`0`、hard minimumは`0`、hard maximumは`1`です。Mayaのattributeに
設定したhard min/maxはChannel Boxなどからの直接入力を制限しますが、incoming
connectionからは範囲外の値を受け取れます。そのため`compute()`でもweightを`0`から
`1`へclampし、`0`では厳密に`input1`、`1`では厳密に`input2`を返します。

範囲外weightによる外挿はこのnodeの責務に含めません。多入力への自然な拡張もないため、
Lerpには`Multi`版を作りません。

### Weighted Add Policy

`bdDbl_WtAddMulti`と`bdDbl3_WtAddMulti`は、valueとweightの積を全要素について加算する
正規化なしの加重和です。double3版ではscalar doubleのweightをXYZすべてへ適用します。

```text
output = sum(input[i].value * input[i].weight)
```

valueとweightのlogical indexが食い違わないよう、入力は2本の独立した配列ではなく
compound multi attributeとして公開します。

```text
input[0].value
input[0].weight
input[1].value
input[1].weight
```

valueとweightのdefaultは`0`です。空配列の結果もdoubleでは`0`、double3では
`(0, 0, 0)`です。weightは負数および`1`を超える値を許可し、合計を`1`へ正規化しません。
加算順序に意味はないため、他の加算Multi nodeと同様に既存elementだけをphysical
iterationで走査します。

浮動小数点の加算と乗算は、数学上の結合法則と完全には一致しません。固定チェーンと
配列版で演算順序が変わる場合は、ごく小さな丸め差を許容したテストにします。厳密な
再現順序が必要なnodeでは、fold順序を仕様として固定します。

性能上の標準選択は、集約後のeffective inputが2個なら固定版、3個以上なら配列版です。
変更しない入力群は先に集約し、最終nodeからは1入力として扱います。固定チェーンの
末尾1入力だけが変化するなどdirty範囲を限定できる特殊な構造は、scene全体の計測結果を
根拠に個別判断します。実測条件と境界値は
[bdDbl Multiplication Benchmark](bd-dbl-mult-benchmark.md) を参照してください。

この規約は、すべての演算に固定版と配列版の両方を必須とするものではありません。
node type、`MTypeId`、wrapper、テスト、文書という保守対象が増えるため、意味が曖昧な
配列版は追加せず、演算ごとにAPIを検討します。

## Plug-in Registration

`MFnPlugin.h` は version string を object file へ埋め込むため、通常は
entry point を定義する `plugin.cpp` だけで include します。他の source は必要な
個別 header を include します。

複数 node を登録する場合は、途中の失敗に備えて、それまで成功した登録を逆順で
rollback します。plug-in のアンロードでも登録時と逆順に解除します。

```text
register A
register B
register C

deregister C
deregister B
deregister A
```

node を含む scene では、その node type を提供する plug-in をアンロードできません。
同じ `.mll` を再 build / stage するときは、plug-in をアンロードするか Maya を
終了してください。

## Add-node Checklist

- [ ] node class、source、header を追加した。
- [ ] `typeName` と `MTypeId` を [Node ID Registry](../NODE_IDS.md) に登録した。
- [ ] input / output の flag と default 値を決めた。
- [ ] 演算nodeでは、固定2入力版と配列版を1組にする意味があるか判断した。
- [ ] 配列版では空入力の結果と、必要ならfold順序を仕様化した。
- [ ] compound の親・子を含めて dirty 依存関係を列挙した。
- [ ] `compute()` が対象 plug だけを処理し、`MStatus` を確認している。
- [ ] multi attribute で logical index の連続性を仮定していない。
- [ ] 順序依存のmulti演算でphysical storage orderを暗黙の演算順序にしていない。
- [ ] thread safety を確認して `schedulingType()` を選んだ。
- [ ] `plugin.cpp` と CMake source list へ追加した。
- [ ] 登録失敗時の rollback と逆順の登録解除を実装した。
- [ ] Maya での自動テストと evaluation mode 比較を追加した。
- [ ] public API へ公開する場合は Python wrapper / type hints も更新した。

## Autodesk References

- [Dependency Node Basics](https://help.autodesk.com/cloudhelp/2024/ENU/Maya-SDK/files/Dependency-graph-plug-ins/Maya_SDK_Dependency_graph_plug_ins_DependencyNodeBasics_html.html)
- [Implementing the compute method](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-DEVHELP/files/Dependency-graph-plug-ins/Maya_DEVHELP_Dependency_graph_plug_ins_Implementing_the_compute_method_html.html)
- [MPxNode C++ API Reference](https://help.autodesk.com/cloudhelp/2027/ENU/MAYA-API-REF/cpp_ref/class_m_px_node.html)
- [MArrayDataHandle C++ API Reference](https://help.autodesk.com/cloudhelp/2024/ENU/MAYA-API-REF/cpp_ref/class_m_array_data_handle.html)
- [initializePlugin / uninitializePlugin](https://help.autodesk.com/cloudhelp/2022/ENU/Maya-SDK/Maya-API-introduction/initialize-uninitialize.html)
- [MFnPlugin C++ API Reference](https://help.autodesk.com/cloudhelp/2024/ENU/MAYA-API-REF/cpp_ref/class_m_fn_plugin.html)
