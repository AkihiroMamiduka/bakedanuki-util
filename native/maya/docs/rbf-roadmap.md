# RBF Node Family And Roadmap

この文書は、補助骨やcorrective rigで使用するRBF node familyの完成範囲、使い分け、
共通設計、性能方針、今後の開発再開条件をまとめます。各nodeの数式、attribute、statusの
詳細は個別仕様書を正とし、この文書ではfamily全体の判断基準を扱います。

## Current Status

補助骨を駆動するためのweight生成からtranslate / rotate / scaleの合成まで、基礎となる
node familyは実装済みです。現時点で追加必須のRBF nodeはありません。

次の段階では数理機能を先回りして増やさず、実際のrig制作で使用し、設定作業、評価速度、
表現力、デバッグ性のフィードバックを集めます。新しいnodeやkernelは、現在の構成で
表現できない具体的な事例が確認された場合に検討します。

## Implemented Scope

### Interpolative RBF Weight

登録したposeで目標weightを補間し、pose間も連続的にweightを生成します。

| node type | source | distance | specification |
|---|---|---|---|
| `bdRbf_OrientationWeight` | 1 Quaternion | Quaternion最短角度 | [Orientation Weight](rbf-orientation-weight.md) |
| `bdRbf_MultiOrientationWeight` | 複数Quaternion | influence付き加重RMS角度 | [Multi Orientation Weight](rbf-multi-orientation-weight.md) |
| `bdRbf_PositionWeight` | 1 position | Euclidean距離 | [Position Weight](rbf-position-weight.md) |
| `bdRbf_MultiPositionWeight` | 複数position | influence付き加重RMS距離 | [Multi Position Weight](rbf-multi-position-weight.md) |

### Independent Falloff Weight

各poseとの距離へ直接falloffを適用し、互いに正規化しない独立weightを生成します。

| node type | source | distance | specification |
|---|---|---|---|
| `bdRbf_OrientationFalloffWeight` | 1 Quaternion | Quaternion最短角度 | [Orientation Falloff](rbf-orientation-falloff-weight.md) |
| `bdRbf_MultiOrientationFalloffWeight` | 複数Quaternion | influence付き加重RMS角度 | [Multi Orientation Falloff](rbf-multi-orientation-falloff-weight.md) |
| `bdRbf_PositionFalloffWeight` | 1 position | Euclidean距離 | [Position Falloff](rbf-position-falloff-weight.md) |
| `bdRbf_MultiPositionFalloffWeight` | 複数position | influence付き加重RMS距離 | [Multi Position Falloff](rbf-multi-position-falloff-weight.md) |
| `bdRbf_BendTwistFalloffWeight` | 1 Quaternion | Bend方向角度とTwist最短角度 | [Bend Twist Falloff](rbf-bend-twist-falloff-weight.md) |
| `bdRbf_MultiBendTwistFalloffWeight` | 複数Quaternion | Bend / Twist別の加重RMS角度 | [Multi Bend Twist Falloff](rbf-multi-bend-twist-falloff-weight.md) |

### Pose Output Blend

| node type | role | specification |
|---|---|---|
| `bdRbf_PoseBlend` | `outputWeight[]`と同じindexのTRS poseを合成 | [Pose Blend](rbf-pose-blend.md) |

weight生成と出力合成を別nodeに保つため、同じweight nodeから複数の補助骨を駆動したり、
weightを別用途へ分岐したりできます。

## Selection Guide

| requirement | recommended node family |
|---|---|
| 登録pose間を補間したい | `OrientationWeight` / `PositionWeight` |
| pose周辺の限られた範囲だけ反応させたい | Orientation / Position `FalloffWeight` |
| Twistを無視し、骨の向き全体だけを比較したい | `BendTwistFalloffWeight`の`BendOnly` |
| BendとTwistの感度を別々に設定したい | `BendTwistFalloffWeight` |
| 複数の骨やdriverを1つの一致度へまとめたい | 対応する`Multi`版 |
| weightから補助骨のtranslate / rotate / scaleを生成したい | `bdRbf_PoseBlend` |

1 sourceで要件を満たす場合はsingle-source版を使用します。Multi版は複数driverの関係そのものが
pose判定に必要な箇所だけで使用し、単に全身のdriverを1 nodeへ集約する目的では使用しません。

## Shared Design Decisions

### Input Space

Orientationとpositionの入力値は、nodeへ渡された値をそのまま比較します。node内でlocal / world
変換は行いません。同じsource indexの現在値とpose値は、呼び出し側で同じ座標空間へ揃えます。

Position系はEuclidean距離だけを使用し、XYZ軸別radiusや軸weightを持ちません。必要な座標変換や
非等方スケールは、上流nodeの責務です。

### Quaternion And Bend / Twist

Orientation系はEuler XYZを軸別に比較せず、Quaternionが表すorientationの最短角度を使用します。
`q`と`-q`、有限な非zero scalar倍は同じorientationとして扱います。

Bend / Twist系はcanonical X軸をTwist軸、Y/Z軸をBend平面としてswing–twist分解します。
`BendOnly`はTwistを無視しますが、Bend量は無視せず、骨の向き全体を比較します。
Multi版ではsourceごとに`axisQuat`と`order`を設定できます。

### Multi-source Distance

Multi版はsourceごとの距離`d_j`と非負の`influence` `a_j`から、加重RMS距離を作ります。

```text
D = sqrt(sum(a_j * d_j^2) / sum(a_j))
```

sourceごとのweightを乗算しないため、source数を増やしてもfalloffが過度に狭くなりません。
Bend / Twist版はBend距離とTwist距離を別々の加重RMSへまとめ、最後に2つのfalloff weightを
乗算します。

各有効poseのsource配列は、nodeの`source[]`と同じlogical index構成が必要です。
`influence = 0`のsourceは距離と値検証から除外しますが、pose側のindex要素は維持します。
全sourceのinfluenceが0の場合は無効設定です。

### Pose And Output Topology

- `pose[].enabled`のdefaultは`true`です。
- `outputWeight[]`は`pose[]`と同じlogical indexを使用します。
- 無効化したposeにも対応するweight 0を出力します。
- `outputWeight[]`は`bdRbf_PoseBlend.weight[]`へ親multi attributeのまま接続できます。
- sparseなlogical indexを許容し、配列の作成順やphysical indexを意味へ使用しません。

### Radius And Per-pose Override

Interpolative RBFの`radius`はkernelの距離スケールです。Falloff版の`innerRadius`はweight 1の
範囲、`outerRadius`はweight 0の境界です。Falloff版は共通半径を基本とし、例外的なposeだけ
`pose[].useRadiusOverride`で上書きできます。

radiusはrig構築時の設定値です。値変更時のdirtyと再評価には対応しますが、毎フレームの
アニメーションはサポートおよび性能保証の対象外です。

### Weight Policy And Defaults

補助骨correctiveの開始点は次のとおりです。

- kernel / falloffは`CompactQuintic`。
- interpolative RBFの`regularization`は`1.0e-8`。
- `allowNegativeWeights`は`false`。
- Orientationのinterpolative radiusは60°をdefaultとし、pose間隔に応じて調整。
- Positionのradiusはrigの距離単位とpose間隔に応じて調整。
- Falloffのinner radiusは0、outer radiusはOrientation / Bend / Twistで60°を開始点とする。
- `pose[].enabled`は`true`。

`allowNegativeWeights = false`は負値を0へclampするだけで、weight合計を1へ再正規化しません。
Falloff系もposeごとに独立しており、範囲が重なる場合はweight合計が1を超えることがあります。

## Performance Policy

pose数を`N`、source数を`S`として、実装は次の評価方針を取ります。

| family | configuration change | normal input evaluation |
|---|---|---|
| single interpolative RBF | 距離行列構築と概ね`O(N^3)`のfactorization | factorizationを再利用 |
| multi interpolative RBF | `O(N^2 S)`の距離行列構築と概ね`O(N^3)`のfactorization | cacheを再利用し、`O(NS)`のkernel vector構築とQR solve |
| single falloff | 行列構築なし | `O(N)` |
| multi falloff | pose値、topology、半径などを設定cacheへ保存 | `O(NS)` |
| pose blend | 行列構築なし | 有効なweight / pose数に対して線形 |

interpolative RBFはEigenのQR solveを使用します。Falloff系はEigen、補間行列、factorizationを
使用しません。Multi Falloff系はpose値を前処理し、通常フレームでは現在sourceだけを更新します。
cacheを持つnodeはinstanceごとのmutexで保護し、RBF node familyは`MPxNode::kParallel`で
評価します。

想定運用では、全身を1 nodeへまとめず、補正の関係単位でnodeを分割します。部位単位で
12～92 pose程度を現実的な検証範囲とし、Multi版は必要な関係だけで使用します。これは
hard limitではありません。最終的な許容数は、実際のcharacter、node数、評価graph、PC環境を
含むproduction sceneで計測して決定します。

radius、pose、source topology、influence、kernel、falloff、Bend / Twistの軸・order・modeは
rig構築時の設定です。変更時には正しく再評価しますが、毎フレームアニメーションする運用は
性能保証の対象外です。

## Verification Completed

現在の自動テストは、少なくとも次を継続して確認します。

- kernel / falloff、radius、regularization、負weight policy。
- Quaternion符号・scale、Twist周期境界、BendOnly、source別axis / order。
- single / multi-source距離、influence、zero influence、source / pose topology。
- pose radius override、disabled pose、sparse logical index。
- `bdRbf_PoseBlend`への親weight接続とTRS合成。
- DG、Serial、Parallel evaluationでのdirty更新。
- Maya ASCIIの保存と再読込。
- NodeOperatorのnested multi API、生成stub、Pyright補完contract。

個別の数値精度とstatus条件は各node仕様書および対応するpytestを参照します。

## Deferred And Out Of Scope

現時点では次を実装しません。

- Position距離のXYZ軸別radiusまたは軸weight。
- node内でのlocal / world座標変換。
- radius、pose設定、influenceなどを毎フレームアニメーションする運用保証。
- 全身のdriverとposeを単一RBF nodeへ集約する設計。
- 実用途が確認されていない追加kernel、falloff、距離方式。
- weight設定を内包した大規模な専用UI。

これらは恒久的な禁止事項ではなく、実際のrigで必要性と期待する挙動が確認された場合に
再検討します。

## Roadmap

### 1. Production Rig Trial

実際の補助骨rigで使用し、次を記録します。

- pose登録数、source数、node数と評価時間。
- radius、influence、kernel / falloffを調整する頻度。
- 期待するweightを作れない姿勢や特異点。
- scene reference、複製、左右ミラー、保存・再読込での問題。
- animatorが操作したときの安定性とcorrective結果。

### 2. Setup API And Tooling

手作業の負担が確認された段階で、まず再利用可能なPython APIを作り、その上に必要最小限の
UIを構築します。候補は次のとおりです。

- 現在値からsource / poseを登録。
- weight nodeと`bdRbf_PoseBlend`の作成・接続。
- poseの追加、削除、複製、並べ替え、左右ミラー。
- radius、influence、enabledの一括設定。
- source / pose topology、重複pose、無効Quaternion、無効半径の検査。
- weight、距離、radius範囲の確認・可視化。

設定ツールは現在のnode APIを置き換えず、同じnode graphを構築・保守する補助層とします。

### 3. Production Profiling

12～92 pose程度を含む代表的な部位rigを用意し、single / multi、interpolative / falloff、
DG / Serial / Parallel、複数characterで計測します。問題が確認された場合は、設定cache、
距離計算、solve、node分割のどこが支配的かを測定してから最適化します。

### 4. Maya Version Coverage

Maya 2025 / 2026 / 2027それぞれのbuild、plugin load、scene round-trip、
Evaluation Manager動作をrelease gateとして維持します。配布対象versionを増やす場合も、
同じ検証を追加します。

### 5. Production Identity And API Stabilization

現在のMTypeIdはAutodeskのlocal test範囲です。production sceneや外部配布を始める前に、
[Node ID Registry](../NODE_IDS.md)の方針に従って正式なID blockを取得します。production sceneへ
保存したMTypeIdとattribute名は、そのnode typeが存続する限り変更しません。

このpackageはv1.0.0未満のため、実運用のフィードバックに基づく破壊的改善を許容します。
v1.0.0へ進む前に、node type、attribute、logical index、status、NodeOperator API、scene互換性を
見直し、その後の安定性境界を決定します。

### 6. Evidence-driven Extensions

現在のnodeで表現できない具体例が見つかった場合だけ、追加のdistance、kernel、falloff、
Multi構成を検討します。提案時には次を明確にします。

- 既存nodeで表現できない入力と期待出力。
- 新しいattributeまたはnode typeが必要な理由。
- pose数、source数、評価速度への影響。
- 既存sceneとNodeOperator APIへの互換性。
- 自動テストで固定できる受け入れ条件。

## Reopening Criteria

RBF node familyの基礎開発は完了とし、次のいずれかが確認された場合に開発を再開します。

- 手作業によるpose設定が継続的な制作負担になった。
- production相当のsceneで評価速度またはメモリの問題が再現した。
- 現在の距離・補間・falloff方式では表現できないcorrectiveが見つかった。
- weightの原因調査やscene保守が困難になり、デバッグ支援が必要になった。
- 対応Maya version、正式MTypeId、v1.0.0互換性の作業を開始する。

新しい開発を始めるときは、まず再現scene、期待するweight、現在のnodeで不足する理由、
pose / source規模、性能条件を記録します。

## Documentation Maintenance

- 数式、attribute、default、statusは各nodeの個別仕様書を更新します。
- family全体の完成範囲、選択基準、非対象、優先順位が変わった場合はこの文書を更新します。
- MTypeIdは[Node ID Registry](../NODE_IDS.md)、buildとtestは
  [Maya C++ Plug-in Development](../README.md)を正とします。
