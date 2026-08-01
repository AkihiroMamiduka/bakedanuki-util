# bdDbl Multiplication Benchmark

`bdDbl_Mult` の左結合チェーンと `bdDbl_MultMulti` の境界を確認するための
Maya 2025 実測結果です。

## Conclusion

通常の運用では、集約後の入力数で次のように選択します。

| Effective inputs | Node |
| --- | --- |
| 2 | `bdDbl_Mult` |
| 3以上 | `bdDbl_MultMulti` |

全入力が毎フレーム変化する条件では、2入力は固定版が有利または実質同等、3入力から
配列版が明確に有利でした。入力数が増えるほど差は拡大します。

ただし、左結合チェーンの末尾にある1入力だけが変化する場合、固定版は最後の1ノード
だけを再計算できます。多数の入力のうち常に同じ1入力だけが変化する特殊な構造では、
固定版チェーンが有利になる場合があります。

## Environment

計測日は 2026-08-01 です。

| Item | Value |
| --- | --- |
| Maya | 2025 / API `20250000` |
| Python | Maya bundled Python 3.11.4 |
| OS | Windows x64 |
| CPU identifier | Intel64 Family 6 Model 151 Stepping 5, GenuineIntel |
| Plug-in | Release build `bdUtilNodes.mll` |
| Plug-in SHA-256 | `150c53bc85307bb63d9268d87d433d27a46e28bcbe7178a29bd19d1ee42fc798` |
| Runtime | `mayapy` standalone、Viewportなし、Cached Playbackなし |

計測後にnode typeの命名規則だけを現行形式へ変更しました。`compute()`の演算内容は
同一であるため結果は引き続き判断材料として使用し、SHA-256は計測時のbinaryを識別する
値として維持します。

絶対時間はマシン、Maya version、バックグラウンド負荷で変化します。この文書では
同一条件内の固定版と配列版の比率を判断材料にします。

## Method

- 固定版は `((a * b) * c) ...` の左結合チェーンです。
- 配列版は全factorを1個の `bdDbl_MultMulti` へ接続します。
- 同じanimCurve入力を各ネットワークへfan-outします。
- 全ネットワークの出力を共通の `plusMinusAverage` へ接続し、最終transformから
  毎フレーム結果を要求します。
- graph作成時間は含めず、連続フレーム評価だけをMEL loop内で計測します。
- warm-up後に複数回計測し、中央値を使用します。
- DG、Serial、Parallelを個別に測定します。
- `dgtimer` はwall time計測と分離し、DGモードの1フレームについてプラグイン
  ノードの `compute()` 回数だけを確認します。

主計測は500ネットワーク、80フレーム、7反復、2 warm-upです。2入力と3入力の
境界は追加で2,000ネットワーク、120フレーム、9反復、3 warm-upで再測定しました。

表の `fixed / multi` は中央値の比率です。

- `1.0` より大きい: 配列版が速い
- `1.0` より小さい: 固定版が速い

## All Inputs Dirty

全factorが毎フレーム変化する主計測です。

| Mode | Inputs | Fixed ms/frame | Multi ms/frame | Fixed / Multi |
| --- | ---: | ---: | ---: | ---: |
| DG | 2 | 1.0845 | 0.9630 | 1.126 |
| DG | 3 | 1.6010 | 1.3839 | 1.157 |
| DG | 4 | 2.3803 | 1.5214 | 1.565 |
| DG | 5 | 3.2569 | 1.8428 | 1.767 |
| DG | 8 | 6.0325 | 2.9036 | 2.078 |
| DG | 16 | 18.0865 | 5.5362 | 3.267 |
| Serial | 2 | 0.8690 | 0.9866 | 0.881 |
| Serial | 3 | 1.5494 | 1.0916 | 1.419 |
| Serial | 4 | 2.2110 | 1.2550 | 1.762 |
| Serial | 5 | 3.3216 | 1.4182 | 2.342 |
| Serial | 8 | 6.8995 | 1.9542 | 3.531 |
| Serial | 16 | 19.5433 | 3.5220 | 5.549 |
| Parallel | 2 | 0.6153 | 0.7585 | 0.811 |
| Parallel | 3 | 0.8208 | 0.7034 | 1.167 |
| Parallel | 4 | 1.0183 | 0.7477 | 1.362 |
| Parallel | 5 | 1.2179 | 0.8063 | 1.510 |
| Parallel | 8 | 1.9124 | 0.9672 | 1.977 |
| Parallel | 16 | 3.9957 | 1.3857 | 2.883 |

入力数が増えると、固定版は `N - 1` 個のノードを評価します。DG timerでも、500
ネットワークの16入力で固定版7,500回、配列版500回の `compute()` が記録されました。

## Boundary Verification

2入力と3入力だけを2,000ネットワークへ増幅した再測定です。

| Mode | Inputs | Fixed ms/frame | Multi ms/frame | Fixed / Multi |
| --- | ---: | ---: | ---: | ---: |
| DG | 2 | 3.9355 | 4.6469 | 0.847 |
| DG | 3 | 7.9536 | 5.6071 | 1.418 |
| Serial | 2 | 3.6360 | 3.8861 | 0.936 |
| Serial | 3 | 7.7403 | 4.7571 | 1.627 |
| Parallel | 2 | 2.6472 | 2.4899 | 1.063 |
| Parallel | 3 | 4.4114 | 2.7009 | 1.633 |

2入力ではDGとSerialで固定版が6～15%高速でした。Parallelは配列版が約6%高速でしたが、
反復値の範囲が重なっており、実用上は同等と判断します。3入力では全モードで配列版が
約29～39%短時間でした。

主計測の2入力DG結果は配列版有利でしたが、分散が大きく、増幅した境界再測定では
固定版有利へ変わりました。このため、2入力の小差は境界判定に使わず、実装の単純さと
DG / Serialの結果から固定版を標準とします。

## Dirty Position

左結合チェーンの先頭入力だけを動かすと、すべての固定ノードがdirtyになります。
Parallelモードの中央値は次の通りです。

| Changed input | Inputs | Fixed ms/frame | Multi ms/frame | Fixed / Multi | DG compute fixed : multi |
| --- | ---: | ---: | ---: | ---: | ---: |
| First | 3 | 0.8692 | 0.7665 | 1.134 | 1000 : 500 |
| First | 4 | 0.8729 | 0.7443 | 1.173 | 1500 : 500 |
| First | 8 | 1.5432 | 0.9531 | 1.619 | 3500 : 500 |
| First | 16 | 3.1288 | 1.3927 | 2.247 | 7500 : 500 |

末尾入力だけを動かすと、固定版も配列版も500回の `compute()` です。ただし固定版は
2値だけを読み、配列版は1回の `compute()` 内で全要素を走査します。

| Changed input | Inputs | Fixed ms/frame | Multi ms/frame | Fixed / Multi | DG compute fixed : multi |
| --- | ---: | ---: | ---: | ---: | ---: |
| Last | 3 | 0.5811 | 0.6970 | 0.834 | 500 : 500 |
| Last | 4 | 0.6079 | 0.7395 | 0.822 | 500 : 500 |
| Last | 8 | 0.6109 | 0.9645 | 0.633 | 500 : 500 |
| Last | 16 | 0.6148 | 1.4125 | 0.435 | 500 : 500 |

Serialでも同じ傾向で、16入力の末尾だけが変化する条件では固定版が約4.1倍高速でした。
これは「配列版が3入力以上で常に速い」のではなく、dirty範囲が最重要であることを
示します。

## Recommended Construction

演算node全体の固定2入力版／配列版の設計基準は
[Arithmetic Node Family Policy](node-basics.md#arithmetic-node-family-policy) にまとめます。

変更しないfactorは先に集約し、最終ノードからは1入力として扱います。

```text
static factors -> staticProduct --+
dynamic factor 1 -----------------+-> final multiplication
dynamic factor 2 -----------------+
```

最終ノードへ入るeffective inputが2個なら固定版、3個以上なら配列版を使います。
この構成ではstatic subtreeは値が変わらない限り再計算されません。

例外として、多数のfactorのうち常に同じ1入力だけが変わり、その入力を左結合チェーンの
末尾へ置ける場合は固定版チェーンが速くなる可能性があります。通常のリグ構築では、
接続順への性能依存とノード数増加を受け入れる価値があるかをscene全体で判断します。

## Reproduction

先にRelease plug-inをbuildします。

```powershell
.\scripts\build-native-maya2025.cmd
.\scripts\benchmark-native-maya2025.cmd
```

結果は既定で `benchmark_results/native` にCSV出力されます。このdirectoryは
`.gitignore` 対象です。

境界だけを再測定する例です。

```powershell
.\scripts\benchmark-native-maya2025.cmd `
    --input-count 2 `
    --input-count 3 `
    --dirty-pattern all `
    --replica-count 2000 `
    --frame-count 120 `
    --repeat-count 9 `
    --warmup-count 3
```

## References

- [Autodesk: dgtimer command](https://help.autodesk.com/cloudhelp/ENU/MayaCRE-Tech-Docs/Commands/dgtimer.html)
- [Autodesk: Evaluation Toolkit](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Customizing/files/GUID-E22B253D-914B-4056-93F5-755702A6C998.htm)
- [Autodesk: Dirty propagation and attributeAffects](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-DEVHELP/files/Dependency-graph-plug-ins/Maya_DEVHELP_Dependency_graph_plug_ins_DirtyPropagation_html.html)
