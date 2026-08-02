# Maya C++ Plug-in Development Guide

`bakedanuki-util` で Maya の C++ dependency node を追加・保守するための
開発ガイドです。Maya 2025 / Windows を基準にしています。

## Documents

1. [Node Basics](node-basics.md)
   - node のライフサイクル、attribute 定義、`compute()`、multi attribute、
     演算node familyの設計方針、plug-in 登録
2. [Native Node Roadmap](node-roadmap.md)
   - `double` / `double3` 演算ノードの優先実装候補、family構成、実装前の検討事項
3. [DG, Parallel Evaluation, And Cached Playback](dg-parallel-cache-playback.md)
   - DG の Pull 評価、Evaluation Graph / Scheduling Graph、Cached Playback、
     background evaluation context
4. [Evaluation And Parallelism](evaluation.md)
   - `attributeAffects()`、dirty 伝搬、Evaluation Manager、
     `schedulingType()`、Parallel 対応
5. [Testing And Debugging](testing-debugging.md)
   - 自動テスト、DG / Serial / Parallel / Cached Playback の比較、
     Visual Studio デバッグ、性能計測
6. [Node ID Registry](../NODE_IDS.md)
   - `MTypeId` の割り当てと運用
7. [Build Guide](../README.md)
   - Maya 2025 向け build、stage、test の実行方法
8. [bdDbl Multiplication Benchmark](bd-dbl-mult-benchmark.md)
   - 固定2入力チェーンと配列入力の性能境界、dirty位置別の実測

## Reference Implementation

現在の最小リファレンスは `bdUtilNodes` plug-in です。

- [plugin.cpp](../plugins/bdUtilNodes/src/plugin.cpp)
  - node の登録、登録失敗時の rollback、逆順での登録解除
- [BdDbl3MultNode.cpp](../plugins/bdUtilNodes/src/BdDbl3MultNode.cpp)
  - 固定2入力の compound attribute と `compute()`
- [BdDbl3MultMultiNode.cpp](../plugins/bdUtilNodes/src/BdDbl3MultMultiNode.cpp)
  - sparse な multi attribute の走査
- [BdDblMultNode.cpp](../plugins/bdUtilNodes/src/BdDblMultNode.cpp)
  - 固定2入力の scalar attribute と `compute()`
- [BdDblMultMultiNode.cpp](../plugins/bdUtilNodes/src/BdDblMultMultiNode.cpp)
  - scalar の sparse multi attribute と単位元
- [BdDbl3AddNode.cpp](../plugins/bdUtilNodes/src/BdDbl3AddNode.cpp)
  - 固定2入力の double3 加算と compound dirty
- [BdDbl3AddMultiNode.cpp](../plugins/bdUtilNodes/src/BdDbl3AddMultiNode.cpp)
  - double3 加算の sparse multi attribute と加法単位元
- [BdDblAddNode.cpp](../plugins/bdUtilNodes/src/BdDblAddNode.cpp)
  - 固定2入力の scalar 加算
- [BdDblAddMultiNode.cpp](../plugins/bdUtilNodes/src/BdDblAddMultiNode.cpp)
  - scalar 加算の sparse multi attribute と加法単位元
- [BdDbl3SubNode.cpp](../plugins/bdUtilNodes/src/BdDbl3SubNode.cpp)
  - 固定2入力の double3 減算と compound dirty
- [BdDbl3SubMultiNode.cpp](../plugins/bdUtilNodes/src/BdDbl3SubMultiNode.cpp)
  - logical index 順で畳み込む double3 配列減算
- [BdDblSubNode.cpp](../plugins/bdUtilNodes/src/BdDblSubNode.cpp)
  - 固定2入力の scalar 減算
- [BdDblSubMultiNode.cpp](../plugins/bdUtilNodes/src/BdDblSubMultiNode.cpp)
  - logical index 順で畳み込む scalar 配列減算
- [SafeDivision.h](../plugins/bdUtilNodes/include/bdUtilNodes/SafeDivision.h)
  - 全演算ノードで共有する除数epsilonと安全除算
- [BdDbl3DivNode.cpp](../plugins/bdUtilNodes/src/BdDbl3DivNode.cpp)
  - 固定2入力の component-wise double3 安全除算
- [BdDbl3DivMultiNode.cpp](../plugins/bdUtilNodes/src/BdDbl3DivMultiNode.cpp)
  - logical index 順で畳み込む double3 配列安全除算
- [BdDblDivNode.cpp](../plugins/bdUtilNodes/src/BdDblDivNode.cpp)
  - 固定2入力の scalar 安全除算
- [BdDblDivMultiNode.cpp](../plugins/bdUtilNodes/src/BdDblDivMultiNode.cpp)
  - logical index 順で畳み込む scalar 配列安全除算
- [SafePower.h](../plugins/bdUtilNodes/include/bdUtilNodes/SafePower.h)
  - 負指数の場合だけ底へ安全除算のepsilonを適用する累乗
- [BdDbl3PowNode.cpp](../plugins/bdUtilNodes/src/BdDbl3PowNode.cpp)
  - 固定2入力の component-wise double3 累乗
- [BdDbl3PowMultiNode.cpp](../plugins/bdUtilNodes/src/BdDbl3PowMultiNode.cpp)
  - logical index 順で左畳み込みする double3 配列累乗
- [BdDblPowNode.cpp](../plugins/bdUtilNodes/src/BdDblPowNode.cpp)
  - 固定2入力の scalar 累乗
- [BdDblPowMultiNode.cpp](../plugins/bdUtilNodes/src/BdDblPowMultiNode.cpp)
  - logical index 順で左畳み込みする scalar 配列累乗
- [BdDblValueNode.cpp](../plugins/bdUtilNodes/src/BdDblValueNode.cpp)
  - 計算を持たず、保存・編集・双方向接続できる scalar value
- [BdDbl3ValueNode.cpp](../plugins/bdUtilNodes/src/BdDbl3ValueNode.cpp)
  - 計算を持たず、親子plugを保存・編集・双方向接続できる double3 value
- [Lerp.h](../plugins/bdUtilNodes/include/bdUtilNodes/Lerp.h)
  - `0`から`1`へclampした線形補間の共有実装
- [BdDbl3LerpNode.cpp](../plugins/bdUtilNodes/src/BdDbl3LerpNode.cpp)
  - scalar weightによるcomponent-wise double3線形補間
- [BdDblLerpNode.cpp](../plugins/bdUtilNodes/src/BdDblLerpNode.cpp)
  - scalarの線形補間
- [BdDbl3WtAddMultiNode.cpp](../plugins/bdUtilNodes/src/BdDbl3WtAddMultiNode.cpp)
  - value/weight compound配列によるdouble3加重和
- [BdDblWtAddMultiNode.cpp](../plugins/bdUtilNodes/src/BdDblWtAddMultiNode.cpp)
  - value/weight compound配列によるscalar加重和
- [MinMax.h](../plugins/bdUtilNodes/include/bdUtilNodes/MinMax.h)
  - NaN伝播、無限値、符号付きゼロを含む最小値・最大値の共有比較規則
- [BdDbl3MinNode.cpp](../plugins/bdUtilNodes/src/BdDbl3MinNode.cpp) / [BdDbl3MinMultiNode.cpp](../plugins/bdUtilNodes/src/BdDbl3MinMultiNode.cpp)
  - component-wiseなdouble3最小値と、空入力を明示したsparse配列版
- [BdDblMinNode.cpp](../plugins/bdUtilNodes/src/BdDblMinNode.cpp) / [BdDblMinMultiNode.cpp](../plugins/bdUtilNodes/src/BdDblMinMultiNode.cpp)
  - scalar最小値の固定2入力版と配列版
- [BdDbl3MaxNode.cpp](../plugins/bdUtilNodes/src/BdDbl3MaxNode.cpp) / [BdDbl3MaxMultiNode.cpp](../plugins/bdUtilNodes/src/BdDbl3MaxMultiNode.cpp)
  - component-wiseなdouble3最大値と、空入力を明示したsparse配列版
- [BdDblMaxNode.cpp](../plugins/bdUtilNodes/src/BdDblMaxNode.cpp) / [BdDblMaxMultiNode.cpp](../plugins/bdUtilNodes/src/BdDblMaxMultiNode.cpp)
  - scalar最大値の固定2入力版と配列版
- [test_bd_dbl3_mult.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_mult.py)
  - double3 ノードの計算、dirty、接続、scene round-trip のテスト
- [test_bd_dbl_mult.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_mult.py)
  - double ノードの計算、dirty、接続、scene round-trip のテスト
- [test_bd_dbl3_add.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_add.py)
  - double3 加算ノードの計算、dirty、接続、scene round-trip のテスト
- [test_bd_dbl_add.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_add.py)
  - double 加算ノードの計算、dirty、接続、scene round-trip のテスト
- [test_bd_dbl3_sub.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_sub.py)
  - double3 減算ノードの順序、dirty、接続、scene round-trip のテスト
- [test_bd_dbl_sub.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_sub.py)
  - double 減算ノードの順序、dirty、接続、scene round-trip のテスト
- [test_bd_dbl3_div.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_div.py)
  - double3 安全除算ノードのepsilon、順序、dirty、scene round-trip のテスト
- [test_bd_dbl_div.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_div.py)
  - double 安全除算ノードのepsilon、順序、dirty、scene round-trip のテスト
- [test_bd_dbl3_pow.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_pow.py)
  - double3 累乗ノードのepsilon、順序、dirty、scene round-trip のテスト
- [test_bd_dbl_pow.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_pow.py)
  - double 累乗ノードのepsilon、定義域、順序、dirty、scene round-trip のテスト
- [test_bd_dbl3_value.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_value.py)
  - double3 valueの親子plug、双方向接続、dirty、scene round-tripのテスト
- [test_bd_dbl_value.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_value.py)
  - double valueの保存、双方向接続、keyframe、dirty、scene round-tripのテスト
- [test_bd_dbl3_lerp.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_lerp.py)
  - double3線形補間、接続値clamp、dirtyのテスト
- [test_bd_dbl_lerp.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_lerp.py)
  - scalar線形補間、接続値clamp、dirtyのテスト
- [test_bd_dbl3_wt_add.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_wt_add.py)
  - double3加重和、compound配列、dirtyのテスト
- [test_bd_dbl_wt_add.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_wt_add.py)
  - scalar加重和、compound配列、dirtyのテスト
- [test_bd_dbl3_min_max.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_min_max.py)
  - double3最小値・最大値の境界値、compound dirty、接続、scene round-tripのテスト
- [test_bd_dbl_min_max.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl_min_max.py)
  - scalar最小値・最大値の境界値、sparse配列、接続、scene round-tripのテスト

## Core Principles

- 入力と出力の依存関係を明示し、Maya の dirty 伝搬に推測させない。
- `compute()` は data block の入力から data block の出力を決める純粋な処理にする。
- `kParallel` は速度指定ではなく、thread safety の保証として扱う。
- background evaluation では current context と normal context を同一視しない。
- node type、`MTypeId`、attribute 名は scene file の永続データである。
- Maya の実行モードごとの差異は、実際の Maya でテストする。
- 性能は Release build と現実的な DG で計測してから最適化する。
