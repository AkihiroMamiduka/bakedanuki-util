# Maya C++ Plug-in Development Guide

`bakedanuki-util` で Maya の C++ dependency node を追加・保守するための
開発ガイドです。Maya 2025 / Windows を基準にしています。

## Documents

1. [Node Basics](node-basics.md)
   - node のライフサイクル、attribute 定義、`compute()`、multi attribute、
     plug-in 登録
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

## Reference Implementation

現在の最小リファレンスは `bdUtilNodes` plug-in です。

- [plugin.cpp](../plugins/bdUtilNodes/src/plugin.cpp)
  - node の登録、登録失敗時の rollback、逆順での登録解除
- [BdDouble3MultNode.cpp](../plugins/bdUtilNodes/src/BdDouble3MultNode.cpp)
  - 固定2入力の compound attribute と `compute()`
- [BdDouble3MultMultiNode.cpp](../plugins/bdUtilNodes/src/BdDouble3MultMultiNode.cpp)
  - sparse な multi attribute の走査
- [test_bd_double3_mult.py](../../../tests/maya/node/operator/node/dg/test_bd_double3_mult.py)
  - plug-in load、計算、接続、scene round-trip、NodeOperator のテスト

## Core Principles

- 入力と出力の依存関係を明示し、Maya の dirty 伝搬に推測させない。
- `compute()` は data block の入力から data block の出力を決める純粋な処理にする。
- `kParallel` は速度指定ではなく、thread safety の保証として扱う。
- background evaluation では current context と normal context を同一視しない。
- node type、`MTypeId`、attribute 名は scene file の永続データである。
- Maya の実行モードごとの差異は、実際の Maya でテストする。
- 性能は Release build と現実的な DG で計測してから最適化する。
