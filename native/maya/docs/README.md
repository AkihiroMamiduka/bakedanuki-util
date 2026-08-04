# Maya C++ Plug-in Development Guide

`bakedanuki-util` で Maya の C++ dependency node を追加・保守するための
開発ガイドです。Maya 2025 / Windows を基準にしています。

## Documents

1. [Node Basics](node-basics.md)
   - node のライフサイクル、attribute 定義、`compute()`、multi attribute、
     演算node familyの設計方針、plug-in 登録
2. [Native Node Roadmap](node-roadmap.md)
   - `double` / `double3` 演算ノードの優先実装候補、family構成、実装前の検討事項
3. [Condition Nodes](condition.md)
   - 単一条件、`case[]`、比較演算、最初の一致、境界値の仕様
4. [Average Nodes](average.md)
   - 固定2入力 / 配列の算術平均、空入力、sparse配列、非有限値の仕様
5. [DG, Parallel Evaluation, And Cached Playback](dg-parallel-cache-playback.md)
   - DG の Pull 評価、Evaluation Graph / Scheduling Graph、Cached Playback、
     background evaluation context
6. [Evaluation And Parallelism](evaluation.md)
   - `attributeAffects()`、dirty 伝搬、Evaluation Manager、
     `schedulingType()`、Parallel 対応
7. [Testing And Debugging](testing-debugging.md)
   - 自動テスト、DG / Serial / Parallel / Cached Playback の比較、
     Visual Studio デバッグ、性能計測
8. [Node ID Registry](../NODE_IDS.md)
   - `MTypeId` の割り当てと運用
9. [Build Guide](../README.md)
   - Maya 2025 向け build、stage、test の実行方法
10. [bdDbl Multiplication Benchmark](bd-dbl-multiply-benchmark.md)
   - 固定2入力チェーンと配列入力の性能境界、dirty位置別の実測

## Reference Implementation

現在の最小リファレンスは `bdUtilNodes` plug-in です。

- [plugin.cpp](../plugins/bdUtilNodes/src/plugin.cpp)
  - node の登録、登録失敗時の rollback、逆順での登録解除
- [BdDbl3MultiplyNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3MultiplyNode.cpp)
  - 固定2入力の compound attribute と `compute()`
- [BdDbl3MultiplyMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3MultiplyMultiNode.cpp)
  - sparse な multi attribute の走査
- [BdDblMultiplyNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblMultiplyNode.cpp)
  - 固定2入力の scalar attribute と `compute()`
- [BdDblMultiplyMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblMultiplyMultiNode.cpp)
  - scalar の sparse multi attribute と単位元
- [BdDbl3AddNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3AddNode.cpp)
  - 固定2入力の double3 加算と compound dirty
- [BdDbl3AddMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3AddMultiNode.cpp)
  - double3 加算の sparse multi attribute と加法単位元
- [BdDblAddNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblAddNode.cpp)
  - 固定2入力の scalar 加算
- [BdDblAddMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblAddMultiNode.cpp)
  - scalar 加算の sparse multi attribute と加法単位元
- [BdDbl3SubtractNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3SubtractNode.cpp)
  - 固定2入力の double3 減算と compound dirty
- [BdDbl3SubtractMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3SubtractMultiNode.cpp)
  - logical index 順で畳み込む double3 配列減算
- [BdDblSubtractNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblSubtractNode.cpp)
  - 固定2入力の scalar 減算
- [BdDblSubtractMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblSubtractMultiNode.cpp)
  - logical index 順で畳み込む scalar 配列減算
- [SafeDivision.h](../plugins/bdUtilNodes/include/bdUtilNodes/math/SafeDivision.h)
  - 全演算ノードで共有する除数epsilonと安全除算
- [BdDbl3DivideNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3DivideNode.cpp)
  - 固定2入力の component-wise double3 安全除算
- [BdDbl3DivideMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3DivideMultiNode.cpp)
  - logical index 順で畳み込む double3 配列安全除算
- [BdDblDivideNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblDivideNode.cpp)
  - 固定2入力の scalar 安全除算
- [BdDblDivideMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblDivideMultiNode.cpp)
  - logical index 順で畳み込む scalar 配列安全除算
- [SafePower.h](../plugins/bdUtilNodes/include/bdUtilNodes/math/SafePower.h)
  - 負指数の場合だけ底へ安全除算のepsilonを適用する累乗
- [BdDbl3PowerNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3PowerNode.cpp)
  - 固定2入力の component-wise double3 累乗
- [BdDbl3PowerMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3PowerMultiNode.cpp)
  - logical index 順で左畳み込みする double3 配列累乗
- [BdDblPowerNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblPowerNode.cpp)
  - 固定2入力の scalar 累乗
- [BdDblPowerMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblPowerMultiNode.cpp)
  - logical index 順で左畳み込みする scalar 配列累乗
- [BdDblValueNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblValueNode.cpp)
  - 計算を持たず、保存・編集・双方向接続できる scalar value
- [BdDbl3ValueNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3ValueNode.cpp)
  - 計算を持たず、親子plugを保存・編集・双方向接続できる double3 value
- [Lerp.h](../plugins/bdUtilNodes/include/bdUtilNodes/math/Lerp.h)
  - `0`から`1`へclampした線形補間の共有実装
- [BdDbl3LerpNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3LerpNode.cpp)
  - scalar weightによるcomponent-wise double3線形補間
- [BdDblLerpNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblLerpNode.cpp)
  - scalarの線形補間
- [BdDbl3WeightedSumMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3WeightedSumMultiNode.cpp)
  - value/weight compound配列によるdouble3加重和
- [BdDblWeightedSumMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblWeightedSumMultiNode.cpp)
  - value/weight compound配列によるscalar加重和
- [MinMax.h](../plugins/bdUtilNodes/include/bdUtilNodes/math/MinMax.h)
  - NaN伝播、無限値、符号付きゼロを含む最小値・最大値の共有比較規則
- [BdDbl3MinNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3MinNode.cpp) / [BdDbl3MinMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3MinMultiNode.cpp)
  - component-wiseなdouble3最小値と、空入力を明示したsparse配列版
- [BdDblMinNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblMinNode.cpp) / [BdDblMinMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblMinMultiNode.cpp)
  - scalar最小値の固定2入力版と配列版
- [BdDbl3MaxNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3MaxNode.cpp) / [BdDbl3MaxMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3MaxMultiNode.cpp)
  - component-wiseなdouble3最大値と、空入力を明示したsparse配列版
- [BdDblMaxNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblMaxNode.cpp) / [BdDblMaxMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblMaxMultiNode.cpp)
  - scalar最大値の固定2入力版と配列版
- [Clamp.h](../plugins/bdUtilNodes/include/bdUtilNodes/math/Clamp.h)
  - 逆転した上下限を正規化し、Minimum / Maximumの比較規則を再利用するclamp
- [BdDbl3ClampNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3ClampNode.cpp)
  - component-wiseなdouble3 clampとcompound dirty
- [BdDblClampNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblClampNode.cpp)
  - scalar clamp
- [MapRange.h](../plugins/bdUtilNodes/include/bdUtilNodes/math/MapRange.h)
  - 方向付きSource / Target範囲、Clamp切替、Source幅0を扱う共有変換
- [BdDbl3MapRangeNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3MapRangeNode.cpp)
  - component-wiseなdouble3 Map Rangeとcompound dirty
- [BdDblMapRangeNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblMapRangeNode.cpp)
  - scalar Map Range
- [Absolute.h](../plugins/bdUtilNodes/include/bdUtilNodes/math/Absolute.h)
  - `std::fabs()`によるscalar / component-wise Absoluteの共有実装
- [BdDbl3AbsNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3AbsNode.cpp)
  - component-wiseなdouble3 Absoluteとcompound dirty
- [BdDblAbsNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblAbsNode.cpp)
  - scalar Absolute
- [Negate.h](../plugins/bdUtilNodes/include/bdUtilNodes/math/Negate.h)
  - 単項マイナスによるscalar / component-wise Negateの共有実装
- [BdDbl3NegateNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3NegateNode.cpp)
  - component-wiseなdouble3 Negateとcompound dirty
- [BdDblNegateNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblNegateNode.cpp)
  - scalar Negate
- [Condition Nodes](condition.md)
  - scalar比較、値選択、logical index順の`case[]`、境界値の共通仕様
- [Comparison.h](../plugins/bdUtilNodes/include/bdUtilNodes/math/Comparison.h)
  - 4つのCondition nodeで共有する6種類の比較演算
- [BdDbl3ConditionMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3ConditionMultiNode.cpp)
  - scalar条件からdouble3を選択するsparse case配列
- [BdDblConditionMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblConditionMultiNode.cpp)
  - scalar条件とscalar値のsparse case配列
- [Average Nodes](average.md)
  - 固定2入力 / 配列、空入力、logical index順、単純合計方式の共通仕様
- [Average.h](../plugins/bdUtilNodes/include/bdUtilNodes/math/Average.h)
  - 固定2入力版で共有する算術平均
- [BdDbl3AverageNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3AverageNode.cpp) / [BdDbl3AverageMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDbl3AverageMultiNode.cpp)
  - component-wiseなdouble3平均の固定2入力版とsparse配列版
- [BdDblAverageNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblAverageNode.cpp) / [BdDblAverageMultiNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDblAverageMultiNode.cpp)
  - scalar平均の固定2入力版とsparse配列版
- [test_bd_dbl3_multiply.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_multiply.py)
  - double3 ノードの計算、dirty、接続、scene round-trip のテスト
- [test_bd_dbl_multiply.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_multiply.py)
  - double ノードの計算、dirty、接続、scene round-trip のテスト
- [test_bd_dbl3_add.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_add.py)
  - double3 加算ノードの計算、dirty、接続、scene round-trip のテスト
- [test_bd_dbl_add.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_add.py)
  - double 加算ノードの計算、dirty、接続、scene round-trip のテスト
- [test_bd_dbl3_subtract.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_subtract.py)
  - double3 減算ノードの順序、dirty、接続、scene round-trip のテスト
- [test_bd_dbl_subtract.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_subtract.py)
  - double 減算ノードの順序、dirty、接続、scene round-trip のテスト
- [test_bd_dbl3_divide.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_divide.py)
  - double3 安全除算ノードのepsilon、順序、dirty、scene round-trip のテスト
- [test_bd_dbl_divide.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_divide.py)
  - double 安全除算ノードのepsilon、順序、dirty、scene round-trip のテスト
- [test_bd_dbl3_power.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_power.py)
  - double3 累乗ノードのepsilon、順序、dirty、scene round-trip のテスト
- [test_bd_dbl_power.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_power.py)
  - double 累乗ノードのepsilon、定義域、順序、dirty、scene round-trip のテスト
- [test_bd_dbl3_value.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_value.py)
  - double3 valueの親子plug、双方向接続、dirty、scene round-tripのテスト
- [test_bd_dbl_value.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_value.py)
  - double valueの保存、双方向接続、keyframe、dirty、scene round-tripのテスト
- [test_bd_dbl3_lerp.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_lerp.py)
  - double3線形補間、接続値clamp、dirtyのテスト
- [test_bd_dbl_lerp.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_lerp.py)
  - scalar線形補間、接続値clamp、dirtyのテスト
- [test_bd_dbl3_weighted_sum.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_weighted_sum.py)
  - double3加重和、compound配列、dirtyのテスト
- [test_bd_dbl_weighted_sum.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_weighted_sum.py)
  - scalar加重和、compound配列、dirtyのテスト
- [test_bd_dbl3_min_max.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_min_max.py)
  - double3最小値・最大値の境界値、compound dirty、接続、scene round-tripのテスト
- [test_bd_dbl_min_max.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_min_max.py)
  - scalar最小値・最大値の境界値、sparse配列、接続、scene round-tripのテスト
- [test_bd_dbl3_clamp.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_clamp.py)
  - double3 clampの逆転境界、非有限値、compound dirty、接続、scene round-tripのテスト
- [test_bd_dbl_clamp.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_clamp.py)
  - scalar clampの逆転境界、非有限値、評価モード、接続、scene round-tripのテスト
- [test_bd_dbl3_map_range.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_map_range.py)
  - double3 Map Rangeの方向、Source幅0、compound dirty、接続、scene round-tripのテスト
- [test_bd_dbl_map_range.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_map_range.py)
  - scalar Map RangeのClamp切替、外挿、非有限値、評価モード、scene round-tripのテスト
- [test_bd_dbl3_abs.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_abs.py)
  - double3 Absoluteの非有限値、符号付きzero、compound dirty、scene round-tripのテスト
- [test_bd_dbl_abs.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_abs.py)
  - scalar Absoluteの正負値、非有限値、評価モード、接続、scene round-tripのテスト
- [test_bd_dbl3_negate.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_negate.py)
  - double3 Negateの非有限値、符号付きzero、compound dirty、scene round-tripのテスト
- [test_bd_dbl_negate.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_negate.py)
  - scalar Negateの正負値、非有限値、評価モード、接続、scene round-tripのテスト
- [test_bd_condition.py](../../../tests/maya/node/operator/node/dg/test_bd_condition.py)
  - 4つのCondition nodeの比較、case順序、境界値、dirty、接続、scene round-tripのテスト
- [test_bd_average.py](../../../tests/maya/node/operator/node/dg/test_bd_average.py)
  - 4つのAverage nodeの固定入力、sparse配列、logical index順、非有限値、dirty、接続、scene round-tripのテスト

## Core Principles

- 入力と出力の依存関係を明示し、Maya の dirty 伝搬に推測させない。
- `compute()` は data block の入力から data block の出力を決める純粋な処理にする。
- `kParallel` は速度指定ではなく、thread safety の保証として扱う。
- background evaluation では current context と normal context を同一視しない。
- node type、`MTypeId`、attribute 名は scene file の永続データである。
- Maya の実行モードごとの差異は、実際の Maya でテストする。
- 性能は Release build と現実的な DG で計測してから最適化する。
