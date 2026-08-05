# Native Node Roadmap

`bdUtilNodes` C++ plug-in に追加する dependency node のロードマップです。
Python 側の API・生成器に関する計画は、既存の
[NodeOperator Roadmap](../../../bakedanuki/bakedanuki-util/docs/maya/node_operator/roadmap.md)
で管理します。

このページには、`double` / `double3` 演算ノード候補のうち、優先度 A のみを
記載します。node type と基本仕様は実装候補であり、未確定事項を検討してから
確定します。

`doubleLinear` / `doubleLinear3`への展開は
[Double Linear Node Expansion](double-linear-nodes.md)で管理します。

## Implementation Order

| 順序 | 演算 | 予定 node type | 形式 | 主な用途 | 状態 |
| ---: | --- | --- | --- | --- | --- |
| 1 | Minimum | `bdDbl_Min`, `bdDbl_MinMulti`, `bdDbl3_Min`, `bdDbl3_MinMulti` | 固定2入力 / 配列 | 複数値から最小値を選択 | 実装済み |
| 2 | Maximum | `bdDbl_Max`, `bdDbl_MaxMulti`, `bdDbl3_Max`, `bdDbl3_MaxMulti` | 固定2入力 / 配列 | 複数値から最大値を選択 | 実装済み |
| 3 | Clamp | `bdDbl_Clamp`, `bdDbl3_Clamp` | 単一入力 | 値を下限と上限の範囲へ制限 | 実装済み |
| 4 | Map Range | `bdDbl_MapRange`, `bdDbl3_MapRange` | 単一入力 | ある数値範囲から別の数値範囲へ変換 | 実装済み |
| 5 | Absolute | `bdDbl_Abs`, `bdDbl3_Abs` | 単項 | 絶対値を出力 | 実装済み |
| 6 | Negate | `bdDbl_Negate`, `bdDbl3_Negate` | 単項 | 符号を反転 | 実装済み |
| 7 | Condition | `bdAny_ConditionDbl`, `bdAny_ConditionDblMulti`, `bdAny_ConditionDblL`, `bdAny_ConditionDblLMulti` | 単一条件 / 条件配列 | 型付きscalar比較でtyped-any値を選択 | 実装済み |
| 8 | Average | `bdDbl_Average`, `bdDbl_AverageMulti`, `bdDbl3_Average`, `bdDbl3_AverageMulti` | 固定2入力 / 配列 | 入力値の算術平均を出力 | 実装済み |
| 9 | Weighted Average | `bdDbl_WeightedAverageMulti`, `bdDbl3_WeightedAverageMulti` | value / weight 配列 | 入力値の加重平均を出力 | 実装済み |
| 10 | Condition Compose | `bdConditionDblExtra_Compose`, `bdConditionDblLExtra_Compose`, `bdConditionDblCase_Compose`, `bdConditionDblLCase_Compose` | 1 node = 1 element | `extra[index]` / `case[index]`用compoundを構築 | 実装済み |

## Double Linear Expansion

`doubleLinear`のtype codeは`DblL`、`doubleLinear`を3つ持つcompoundのtype codeは
`DblL3`とします。`doubleLinear3`はMayaのatomic type名ではなく、親`double3`と
3つの`doubleLinear` childからなる構造のプロジェクト内呼称です。

| Phase | Scope | Status |
| ---: | --- | --- |
| 1 | Value、Add、Subtract、Average、Min / Maxなど、距離を保つ18種 | 実装済み |
| 2 | scalar `doubleLinear`で条件を評価し、typed-any値を選択するCondition 2種 | 実装済み |
| 3 | linear valueとdimensionless factorを扱うMultiply / Divide | attribute仕様を検討中 |
| 4 | Power / PowerMulti | 具体的用途が得られるまで保留 |

実装対象、attribute型、default、unit固有のテスト条件は
[Double Linear Node Expansion](double-linear-nodes.md)を参照してください。

## Family Policy

- `double3` の演算は、別途明記しない限り XYZ の成分ごとに行う。
- Minimum / Maximum のように複数入力を自然に畳み込める演算は、固定2入力版と
  `Multi` 版を用意する。
- Clamp / Map Range のように役割の異なるパラメーターを持つ演算と、単項演算には
  固定2入力版や `Multi` 版を機械的に追加しない。
- Average は2値の平均を直接扱える固定2入力版と、任意個の入力を扱う `Multi` 版を
  用意する。詳細は [Average Nodes](average.md) を参照する。
- Weighted Average は既存の Weighted Sum と同じ value / weight の compound配列を
  使用する。詳細は [Weighted Average Nodes](weighted-average.md) を参照する。
- Conditionはnode typeで指定したscalar型の`input`と`compare`を比較し、同じ型へ
  統一して接続されたtyped-any payloadを選択する。`Multi`版は`case[]`をlogical
  index順に評価し、最初に一致した値を出力する。Single版の`extra[]`とMulti版の
  `case[].extra[]`は、追加比較をAnd / Orでlogical index順に結合する。詳細は
  [Condition Nodes](condition.md)を参照する。

## Removed From Priority A

- Sign は `-1 / 0 / 1` の出力後に追加の分岐が必要になりやすく、現時点のリグ用途では
  Condition の方が直接的なため実装対象から外す。

## Definition Of Done

各 node family は、次を完了した時点で実装済みとします。

- C++ node 本体、attribute、dirty 伝搬、plug-in 登録を実装する。
- `MTypeId` を [Node ID Registry](../NODE_IDS.md) に登録する。
- NodeOperator クラスと型情報を生成し、公開 API の補完を確認する。
- 計算、境界条件、接続、dirty 伝搬、scene round-trip を Maya 上でテストする。
- node 固有の仕様と判断理由を関連ドキュメントへ反映する。
