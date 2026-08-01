# Maya C++ Plug-in Development Guide

`bakedanuki-util` で Maya の C++ dependency node を追加・保守するための
開発ガイドです。Maya 2025 / Windows を基準にしています。

## Documents

1. [Node Basics](node-basics.md)
   - node のライフサイクル、attribute 定義、`compute()`、multi attribute、
     演算node familyの設計方針、plug-in 登録
2. [DG, Parallel Evaluation, And Cached Playback](dg-parallel-cache-playback.md)
   - DG の Pull 評価、Evaluation Graph / Scheduling Graph、Cached Playback、
     background evaluation context
3. [Evaluation And Parallelism](evaluation.md)
   - `attributeAffects()`、dirty 伝搬、Evaluation Manager、
     `schedulingType()`、Parallel 対応
4. [Testing And Debugging](testing-debugging.md)
   - 自動テスト、DG / Serial / Parallel / Cached Playback の比較、
     Visual Studio デバッグ、性能計測
5. [Node ID Registry](../NODE_IDS.md)
   - `MTypeId` の割り当てと運用
6. [Build Guide](../README.md)
   - Maya 2025 向け build、stage、test の実行方法
7. [bdDouble Multiplication Benchmark](bd-mult-double-benchmark.md)
   - 固定2入力チェーンと配列入力の性能境界、dirty位置別の実測

## Reference Implementation

現在の最小リファレンスは `bdUtilNodes` plug-in です。

- [plugin.cpp](../plugins/bdUtilNodes/src/plugin.cpp)
  - node の登録、登録失敗時の rollback、逆順での登録解除
- [BdMultDouble3PairNode.cpp](../plugins/bdUtilNodes/src/BdMultDouble3PairNode.cpp)
  - 固定2入力の compound attribute と `compute()`
- [BdMultDouble3MultiNode.cpp](../plugins/bdUtilNodes/src/BdMultDouble3MultiNode.cpp)
  - sparse な multi attribute の走査
- [BdMultDoublePairNode.cpp](../plugins/bdUtilNodes/src/BdMultDoublePairNode.cpp)
  - 固定2入力の scalar attribute と `compute()`
- [BdMultDoubleMultiNode.cpp](../plugins/bdUtilNodes/src/BdMultDoubleMultiNode.cpp)
  - scalar の sparse multi attribute と単位元
- [BdAddDouble3PairNode.cpp](../plugins/bdUtilNodes/src/BdAddDouble3PairNode.cpp)
  - 固定2入力の double3 加算と compound dirty
- [BdAddDouble3MultiNode.cpp](../plugins/bdUtilNodes/src/BdAddDouble3MultiNode.cpp)
  - double3 加算の sparse multi attribute と加法単位元
- [BdAddDoublePairNode.cpp](../plugins/bdUtilNodes/src/BdAddDoublePairNode.cpp)
  - 固定2入力の scalar 加算
- [BdAddDoubleMultiNode.cpp](../plugins/bdUtilNodes/src/BdAddDoubleMultiNode.cpp)
  - scalar 加算の sparse multi attribute と加法単位元
- [BdSubDouble3PairNode.cpp](../plugins/bdUtilNodes/src/BdSubDouble3PairNode.cpp)
  - 固定2入力の double3 減算と compound dirty
- [BdSubDouble3MultiNode.cpp](../plugins/bdUtilNodes/src/BdSubDouble3MultiNode.cpp)
  - logical index 順で畳み込む double3 配列減算
- [BdSubDoublePairNode.cpp](../plugins/bdUtilNodes/src/BdSubDoublePairNode.cpp)
  - 固定2入力の scalar 減算
- [BdSubDoubleMultiNode.cpp](../plugins/bdUtilNodes/src/BdSubDoubleMultiNode.cpp)
  - logical index 順で畳み込む scalar 配列減算
- [SafeDivision.h](../plugins/bdUtilNodes/include/bdUtilNodes/SafeDivision.h)
  - 全演算ノードで共有する除数epsilonと安全除算
- [BdDivDouble3PairNode.cpp](../plugins/bdUtilNodes/src/BdDivDouble3PairNode.cpp)
  - 固定2入力の component-wise double3 安全除算
- [BdDivDouble3MultiNode.cpp](../plugins/bdUtilNodes/src/BdDivDouble3MultiNode.cpp)
  - logical index 順で畳み込む double3 配列安全除算
- [BdDivDoublePairNode.cpp](../plugins/bdUtilNodes/src/BdDivDoublePairNode.cpp)
  - 固定2入力の scalar 安全除算
- [BdDivDoubleMultiNode.cpp](../plugins/bdUtilNodes/src/BdDivDoubleMultiNode.cpp)
  - logical index 順で畳み込む scalar 配列安全除算
- [test_bd_mult_double3.py](../../../tests/maya/node/operator/node/dg/test_bd_mult_double3.py)
  - double3 ノードの計算、dirty、接続、scene round-trip のテスト
- [test_bd_mult_double.py](../../../tests/maya/node/operator/node/dg/test_bd_mult_double.py)
  - double ノードの計算、dirty、接続、scene round-trip のテスト
- [test_bd_add_double3.py](../../../tests/maya/node/operator/node/dg/test_bd_add_double3.py)
  - double3 加算ノードの計算、dirty、接続、scene round-trip のテスト
- [test_bd_add_double.py](../../../tests/maya/node/operator/node/dg/test_bd_add_double.py)
  - double 加算ノードの計算、dirty、接続、scene round-trip のテスト
- [test_bd_sub_double3.py](../../../tests/maya/node/operator/node/dg/test_bd_sub_double3.py)
  - double3 減算ノードの順序、dirty、接続、scene round-trip のテスト
- [test_bd_sub_double.py](../../../tests/maya/node/operator/node/dg/test_bd_sub_double.py)
  - double 減算ノードの順序、dirty、接続、scene round-trip のテスト
- [test_bd_div_double3.py](../../../tests/maya/node/operator/node/dg/test_bd_div_double3.py)
  - double3 安全除算ノードのepsilon、順序、dirty、scene round-trip のテスト
- [test_bd_div_double.py](../../../tests/maya/node/operator/node/dg/test_bd_div_double.py)
  - double 安全除算ノードのepsilon、順序、dirty、scene round-trip のテスト

## Core Principles

- 入力と出力の依存関係を明示し、Maya の dirty 伝搬に推測させない。
- `compute()` は data block の入力から data block の出力を決める純粋な処理にする。
- `kParallel` は速度指定ではなく、thread safety の保証として扱う。
- background evaluation では current context と normal context を同一視しない。
- node type、`MTypeId`、attribute 名は scene file の永続データである。
- Maya の実行モードごとの差異は、実際の Maya でテストする。
- 性能は Release build と現実的な DG で計測してから最適化する。
