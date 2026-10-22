# Controller Shape

`bdControllerShape` はリグのコントローラー向けのカスタム DAG shape です。
１つの親 `transform` の下に１つの shape を置き、Viewport 2.0 に線と面を描画します。
`CircleArrow2D` は円と矢印を独立した線として描くため、両者をつなぐ線は不要です。
コントローラーとして操作するのは親 `transform` です。

## 作成例

```python
import bd_util as bdu

mod = bdu.ModifierManager()
bd_nodes = bdu.Nodes(modifier_manager=mod)

control, shape = bd_nodes.create.controllerShape(name="hand_ctrl")
shape.shape.set(shape.shape.CIRCLEARROW2D)
shape.shapeRootSize.set(1.5)
shape.shapeSize.set(0.8)
shape.shapeLineWidth.set(2.0)  # 画面上で 2 px の線
shape.shapeTransparency.set(0.25)  # 25% 透明
shape.shapeDrawOnTop.set(True)

mod.do_it_dag()
mod.do_it_dg()
```

`bd_nodes.create.controllerShape()` は `(Transform, BdControllerShape)` を返します。
両ノードの作成は `mod.do_it_dag()`、属性設定は `mod.do_it_dg()` で確定します。
標準の `nurbsCurve` / `nurbsSurface` データや生成ノードへの接続はありません。
軸指定の既定値は主軸 `+X`・補助軸 `+Y` で、平面形状は YZ 面に作られます。
XY 面に向ける場合は `shape.shape1stAxis.set(4)`（`+Z`）を指定します。

アニメーションで形状とフォーカス範囲を変形する場合は、行列ノードの出力を接続します。
次の例では `composeMatrix` の数値入力をアニメーションさせます。

```python
animation_matrix = bd_nodes.create.composeMatrix(name="hand_shape_animation")
animation_matrix.outputMatrix.connect(shape.shapeAnimationTransformMatrix)
mod.do_it_dg()
```

`shapeAnimationTransformMatrix` 自体には Maya の通常のキーを直接作れません。
行列の移動・回転・スケールをキー化するときは、接続元の数値属性を使います。

`Cube` の根元を原点に合わせ、主軸方向へ 5 cm 伸ばす場合は、
`shapeSize=1` として次のように設定します。

```python
shape.shape.set(shape.shape.CUBE)
shape.shapeSize.set(1.0)
shape.shapeAxisOffsetLength.set(5.0)
shape.shapeAxisOffset.set(True)
shape.shapeAxisOffsetDirection.set(0)  # +1stAxis
mod.do_it_dg()
```

フォーカス範囲を形状の位置から分離する場合は、`boundsMode` を切り替えます。
`ShapeCentered` は形状由来の大きさを原点中心で使い、`Custom` は独立した
Cube の調整値を使います。

```python
shape.boundsMode.set(1)  # ShapeCentered
shape.boundsMode.set(2)  # Custom
shape.customBoundsTranslate.set(0.0, 0.0, 2.0)
shape.customBoundsSize.set(3.0)
shape.showBoundsPreview.set(True)
mod.do_it_dg()
```

プレビューは選択中の `boundsMode` のフォーカス範囲を template 色で描画します。
プレビューの線はクリック選択できません。

## 形状と属性

| Attribute | Maya の型 | 既定値 | 意味 |
| --- | --- | --- | --- |
| `shape` | enum | `Cube` (72) | 下表の106種類。`Gear` を一覧の先頭とし、初期値は `Cube` |
| `shapeFin` | `bool` | `false` | 全106形状へ通常色のFinを1枚追加。short nameは `sfn`。OFFでも種類・高さを保持 |
| `shapeFinType` | enum | `Standard` (0) | `Standard` (0)、`Tapered` (1)。short nameは `sfnt` |
| `shape1stAxis` | enum | `+X` (0) | 基準形状の主軸 `+X` を向ける方向。`+X` (0)、`-X` (1)、`+Y` (2)、`-Y` (3)、`+Z` (4)、`-Z` (5) |
| `shape2ndAxis` | enum | `+Y` (2) | 基準形状の補助軸 `+Y` を向ける方向。選択肢は `shape1stAxis` と同じ |
| `shapeAnimationTransformMatrix` | matrix data | 単位行列 | 基準形状またはフォーカス用の箱の完成後、親 `transform` の変換前に適用するローカル行列 |
| `shapeRootSize` | `double` | `1` | 平行移動を含む全体の一律スケール |
| `shapeTranslate` | `doubleLinear3` | `(0, 0, 0)` | 軸指定の外側で形状を平行移動 |
| `shapeRotate` | `doubleAngle3` | `(0, 0, 0)` | 軸指定の外側で XYZ 固定順に回転 |
| `shapeScale` | `double3` | `(1, 1, 1)` | 軸指定の外側、`shapeRotate` の内側で拡縮 |
| `shapeAxisOffsetLength` | `doubleLinear` | `1 cm` | `shapeAxisOffset=true` のとき、`shapeAxisOffsetDirection` で選んだ軸に沿ってオフセットと形状を原点基準で伸縮。最小値 `0` |
| `shapeAxisOffset` | `bool` | `false` | 選択した軸方向へ基準形状を固定 `0.5` オフセット |
| `shapeAxisOffsetDirection` | enum | `+1stAxis` (0) | `+1stAxis` (0)、`-1stAxis` (1)、`+2ndAxis` (2)、`-2ndAxis` (3)、`+3rdAxis` (4)、`-3rdAxis` (5) |
| `shapeAxisTranslate` | `doubleLinear3` | `(0, 0, 0)` | 指定した軸を基準に形状を平行移動 |
| `shapeAxisRotate` | `doubleAngle3` | `(0, 0, 0)` | 指定した軸を基準に XYZ 固定順に回転 |
| `shapeAxisScale` | `double3` | `(1, 1, 1)` | 指定した軸を基準に、`shapeAxisRotate` の内側で拡縮 |
| `shapeSize` | `double` | `1` | 本体の頂点を末端で一律スケール |
| `shapePartOffset` | `doubleLinear` | `0 cm` | 端の小形状・Arrow・端点矢印をそれぞれの向きへ移動。矢印のない端とFinの高さには適用しない |
| `shapePartOffsetAngle` | `doubleAngle` | `0°` | Semicircle系列の両端を同じ角度ずつ開く。範囲は `-90°`–`90°`、short nameは `spoa` |
| `shapePartFinHeight` | `doubleLinear` | `0.5 cm` | Finの張り出す高さ。`shapePartSize`を掛け、0ならFinのみ省略。short nameは `spfh` |
| `shapePartSize` | `double` | `1` | 部品の長さ・太さに掛け合わせる共通倍率。short nameは `sps` |
| `shapePartLengthScale` | `double` | `1` | 部品を長手方向へ伸縮。Finの高さには適用しない |
| `shapePartWidthScale` | `double` | `1` | 部品の長手方向と直交する2軸を同じ倍率で伸縮。Finは付け根に沿う広がり |
| `showShapeOffsetLine` | `bool` | `false` | 親 `transform` のローカル原点から、軸オフセットを除いた形状基準位置まで補助線を描く |
| `shapeOffsetLineTemplate` | `bool` | `false` | 補助線をテンプレート表示・選択不可にする |
| `shapeLineWidth` | `float` | `1` | 本体と OffsetLine の画面上の線幅。単位は pixel、最小値 `1` |
| `shapeTransparency` | `float` | `0` | 本体の輪郭線、OffsetLine、`ColorCornerCube` の小四角の透明度。`0` は不透明、`1` は完全透明。範囲は `0`–`1` |
| `shapeFill` | `bool` | `false` | 本体・付属部品の面を表示する。short nameは `sfl`。線そのものは塗らず、追加Finの面には適用する |
| `shapeFillTransparency` | `float` | `0.85` | `shapeFill` がONの本体面の透明度。`ColorCornerCube` の小四角には適用しない。`0` は不透明、`1` は完全透明。範囲は `0`–`1` |
| `shapeDrawOnTop` | `bool` | `false` | 本体の輪郭線・面と OffsetLine を他のシーン形状に隠れないように描画する |
| `boundsMode` | enum | `ShapeCentered` (1) | フォーカス範囲。`Shape` (0)、`ShapeCentered` (1)、`Custom` (2) |
| `showBoundsPreview` | `bool` | `false` | 選択中の `boundsMode` の最終的な軸平行範囲を template 色で表示する。選択不可 |

### 形状一覧

| 値 | 形状 |
| --- | --- |
| 0–9 | `Gear`、`Line`、`LineArrowAtEnd`、`LineArrowAtEnds`、`LineWideArrowAtEnd`、`LineWideArrowAtEnds`、`LineSquareAtEnd`、`LineSquareAtEnds`、`LineDiamondAtEnd`、`LineDiamondAtEnds` |
| 10–19 | `LineCircleAtEnd`、`LineCircleAtEnds`、`LineTriangleAtEnd`、`LineTriangleAtEnds`、`CrossLine1st2nd`、`CrossLine1st2ndArrowAtEnd`、`CrossLine1st2ndArrowAtEnds`、`CrossLine1st2ndWideArrowAtEnd`、`CrossLine1st2ndWideArrowAtEnds`、`CrossLine1st2ndSquareAtEnd` |
| 20–29 | `CrossLine1st2ndSquareAtEnds`、`CrossLine1st2ndDiamondAtEnd`、`CrossLine1st2ndDiamondAtEnds`、`CrossLine1st2ndCircleAtEnd`、`CrossLine1st2ndCircleAtEnds`、`CrossLine1st2ndTriangleAtEnd`、`CrossLine1st2ndTriangleAtEnds`、`CrossLine1st3rd`、`CrossLine1st3rdArrowAtEnd`、`CrossLine1st3rdArrowAtEnds` |
| 30–39 | `CrossLine1st3rdWideArrowAtEnd`、`CrossLine1st3rdWideArrowAtEnds`、`CrossLine1st3rdSquareAtEnd`、`CrossLine1st3rdSquareAtEnds`、`CrossLine1st3rdDiamondAtEnd`、`CrossLine1st3rdDiamondAtEnds`、`CrossLine1st3rdCircleAtEnd`、`CrossLine1st3rdCircleAtEnds`、`CrossLine1st3rdTriangleAtEnd`、`CrossLine1st3rdTriangleAtEnds` |
| 40–49 | `CrossLine2nd3rd`、`CrossLine2nd3rdArrowAtEnd`、`CrossLine2nd3rdArrowAtEnds`、`CrossLine2nd3rdWideArrowAtEnd`、`CrossLine2nd3rdWideArrowAtEnds`、`CrossLine2nd3rdSquareAtEnd`、`CrossLine2nd3rdSquareAtEnds`、`CrossLine2nd3rdDiamondAtEnd`、`CrossLine2nd3rdDiamondAtEnds`、`CrossLine2nd3rdCircleAtEnd` |
| 50–59 | `CrossLine2nd3rdCircleAtEnds`、`CrossLine2nd3rdTriangleAtEnd`、`CrossLine2nd3rdTriangleAtEnds`、`CrossLine3Axis`、`CrossLine3AxisEndCube`、`CrossLine3AxisEndOctahedron`、`CrossLine3AxisEndSphere`、`CrossLine3AxisEndPyramid`、`CrossLine3AxisEndCone`、`Triangle` |
| 60–69 | `Square`、`SquareArrow2D`、`SquareArrow3D`、`SquareArrowCrossLine2D`、`SquareArrowCrossLine3D`、`SquareArrowCrossLineTemplate2D`、`SquareArrowCrossLineTemplate3D`、`SquareArrow4Way2D`、`SquareArrow4Way3D`、`SquareTemplateArrow4Way2D` |
| 70–79 | `SquareTemplateArrow4Way3D`、`Diamond`、`Cube`、`CubeArrow2D`、`CubeArrow3D`、`Octahedron`、`OctahedronArrow`、`Circle`、`CircleArrow2D`、`CircleArrow3D` |
| 80–89 | `Semicircle`、`SemicircleArrowAtEnd`、`SemicircleArrowAtEnds`、`SemicircleWideArrowAtEnd`、`SemicircleWideArrowAtEnds`、`SemicircleArrow2D`、`SemicircleArrow3D`、`Sphere`、`SphereArrow2D`、`SphereArrow3D` |
| 90–99 | `Cylinder`、`Arrow`、`Pyramid`、`Cone`、`ColorCrossLine3Axis`、`ColorCrossLine3AxisEndCube`、`ColorCrossLine3AxisEndOctahedron`、`ColorCrossLine3AxisEndSphere`、`ColorCrossLine3AxisEndPyramid`、`ColorCrossLine3AxisEndCone` |
| 100–105 | `ColorCube`、`ColorCornerCube`、`ColorSphere`、`ColorSphereArrow2D`、`ColorSphereArrow3D`、`ColorSphereCrossLine` |

塗りは全形状共通の `shapeFill` で切り替えます。OFFが既定値で、ONでは旧Filled版と同じ範囲を塗ります。
旧Filled付きの109項目を統合した115項目から、旧Fin付きの8項目と `TriangleArrow3D` も統合し、106項目に整理しています。
以下の面の説明は `shapeFill` がONの状態を示します。

基準となる部分はローカル座標の各軸でおおむね `-0.5` から `+0.5` を使います。
矢印やフィンはその範囲から張り出す設計です。形状全体を長さ1に正規化しません。
`Line` は主軸に沿って `-0.5` から `+0.5` まで伸びます。
向きは `shape1stAxis`、端形状の幅方向は `shape2ndAxis` で指定します。
`Cube` と `Cylinder` の `shapeFinType=Tapered` は
`-1stAxis` 側のフィンを `+2ndAxis` 方向へ高さ `1` まで伸ばし、
`+1stAxis` 側の本体上端へ斜めにつなぎます。
`2D` の矢印は主平面上にあり、`3D` の矢印は主平面と直交する三角形も持ちます。

`CrossLine1st2nd`、`CrossLine1st3rd`、`CrossLine2nd3rd` は指定された2軸の
長さ1の線を組み合わせ、`CrossLine3Axis` は3軸すべてを組み合わせます。
既定軸ではそれぞれ XY、XZ、YZ、XYZ です。

`Diamond` はSquareの各辺の中点を結んだひし形です。
既定軸ではYZ平面上の `(Y, Z) = (0.5, 0), (0, 0.5), (-0.5, 0), (0, -0.5)` を使い、
幅・高さと縦横の対角線は1です。`shapeFill` がONならDiamondの内側だけを塗ります。
Square系列の最後、Cubeの前へDiamondを並べます。
単体のDiamondには部品調整属性を適用せず、既存の全体変形を適用します。

`CrossLine3AxisEndCube/EndOctahedron/EndSphere/EndPyramid/EndCone` は、
既定値では3軸の正負6端に既存の基本形状を `0.1` 倍して配置した形状です。
同じ5系列に `Color` 接頭辞を用意し、通常色・Color版とも `shapeFill` で塗りを切り替えます。
各系列は `CrossLine3Axis` または `ColorCrossLine3Axis` の直後へ、
Cube、Octahedron、Sphere、Pyramid、Coneの順で並べます。

| 端の形状 | 基本形状の原点までの距離 | 軸線の長さ（原点から片側） | 外側の端までの距離 |
| --- | --- | --- | --- |
| Cube / Octahedron / Sphere | `0.5` | `0.45` | `0.55` |
| Pyramid / Cone | `0.45` | `0.4` | `0.5` |

Cubeは一辺 `0.1`、Octahedronは向かい合う頂点間 `0.1`、Sphereは直径 `0.1` です。
Pyramidは底面の一辺と高さが `0.1`、Coneは底面の直径と高さが `0.1` です。
PyramidとConeの先端は各軸の外側へ向け、底面は原点から `0.4` に置きます。
軸線は6端の形状の手前の表面で止め、形状の内部へ描きません。
端形状の輪郭と塗り面は既存の基本形状を共用し、既存の形状変形を全体へ適用します。
Color版の軸指定・回転・負スケールは、後述のColor系の描画規則に従います。

通常版はすべて通常色です。Color版は正方向の3本の軸線だけをRGBにし、
負方向の軸線と6端の形状の輪郭・面は通常色にします。
塗りは端の立体の面全体（PyramidとConeは底面を含む）だけを塗り、軸線は線のままです。
面には `shapeFillTransparency`、輪郭と軸線には `shapeTransparency` を適用します。
Wireframeでは端形状も輪郭線だけを表示し、選択、Template/Reference、
Selection Highlighting、Draw On Topは既存の通常色・軸色の表示規則に従います。

`Line` と `CrossLine1st2nd/1st3rd/2nd3rd` の4系列には、
平面の `Square`、`Diamond`、`Circle`、`Triangle` を端へ配置する形状を用意します。
`AtEnd` は代表の1端へ、`AtEnds` はLineの両端・2軸CrossLineの4端すべてへ配置します。
片側版16種類と全端版16種類の計32種類です。
例えば `LineSquareAtEnd`、`LineSquareAtEnds`、
`CrossLine1st3rdDiamondAtEnd` という名称です。

| 系列 | `AtEnd` の配置方向 |
| --- | --- |
| Line | `+1stAxis` |
| CrossLine1st2nd / CrossLine1st3rd | `+1stAxis` |
| CrossLine2nd3rd | `+2ndAxis` |

Lineは主軸、2軸CrossLineは名前の先頭にある軸を代表とします。
各系列のWideArrowAtEndsの後へ、Square、Diamond、Circle、Triangleの順に、
各形状の片側版、全端版を並べます。
各形状はEnd、Endsの順です。
単体Diamondと、3軸の立体端形状の名称は維持します。
Line2nd・Line3rd系列を削除し、Line1st系列をLine系列へ改名したため、
公開 `shape` enumの数値は再配置されています。旧名称の別名は設けません。
Filled項目の統合でもenum値が変わります。旧Filled相当の形状は基本名を指定して `shapeFill` をONにしてください。
既存シーンに保存された数値は自動移行しないため、旧版のシーンは形状名を確認して再指定してください。

Endは軸指定・全体回転前の代表軸の正側です。
軸指定や負スケールで反転しても端の指定は維持し、Triangleは指定端の外側を向きます。
片側版では小形状のある端だけを部品調整の対象とし、
小形状のない反対側や別軸の端は元の±0.5まで線を伸ばします。

| 端の平面形状 | 基準寸法 | 配置 | 原点から接続線の端まで |
| --- | --- | --- | --- |
| Square | 一辺0.1 | 中心を±0.5 | `0.45` |
| Diamond | 縦横の対角線0.1 | 中心を±0.5 | `0.45` |
| Circle | 直径0.1、円周64分割 | 中心を±0.5 | `0.45` |
| Triangle | 底辺幅・高さ0.1 | 外向きの先端を±0.5、底辺を±0.4 | `0.4` |

Lineの小形状は1st–2nd平面に置きます。
2軸CrossLineは名前に含まれる2軸の平面を使います。
Triangleは底辺も描く閉じた形状で、単体Triangleを0.1倍したものとは高さが異なります。
単体Triangleの比率は維持します。

Offsetは各端の外向きへ加算し、Size・Length・Widthは既存の部品調整規則を使います。
ピボットは元の±0.5とし、Square/Diamond/Circleは中心、Triangleは先端を固定して伸縮します。
接続線は変形後の小形状の手前で止め、その境界が原点に達する・越える場合は省略します。
輪郭はゼロスケールでも潰れた形で残し、面積が0の塗り面は省略します。
塗りは小形状の内側だけを通常色で塗り、接続線は線のままです。
小形状同士が重なる場合も輪郭を保ち、塗り面は和集合として二重描画を避けます。
軸指定・全体変形・Bounds・選択・透明度・表示状態・Undo/Redo・保存の規則は既存形状に従います。

`shapePartOffset`、`shapePartLengthScale`、`shapePartWidthScale`、`shapePartSize` は小形状のある端に共通で作用し、
通常版・Color版、輪郭・塗り面で同じ変形を使います。
端の立体形状10種類・平面形状32種類に加え、全Arrow・端点矢印・Fin系列を対象とします。
既定値 `0 / 1 / 1 / 1` は各形状の基準寸法を再現します。

小形状の長手方向の基準座標を `a`、横2軸の座標を `b`、`c` とすると、
部品の変形後の座標は次のとおりです。長手方向は各端の外向きを正とします。

```text
length = shapePartSize * shapePartLengthScale
width = shapePartSize * shapePartWidthScale
a' = 0.5 + (a - 0.5) * length + shapePartOffset
b' = b * width
c' = c * width
```

Cube、Octahedron、Sphereは中心を、Pyramid、Coneは先端を固定して伸縮します。
例えば長さを2倍にすると、前者の長手方向は `0.4–0.6`、後者は底面 `0.3`・先端 `0.5` です。
オフセットは伸縮後に加えるため、長さスケールを変えても加算距離は変わりません。
部品の変形は `shapeSize` など既存の全体変形より前に適用し、
ピボットと追加オフセットも全体の変形へ追従します。

接続線は変形後の小形状の手前の表面まで伸縮します。表面が原点に達する・越えるときは
線の長さを0とし、反対側へ延長しません。スケールに下限・上限は設けず、負値はピボットでの
反転として扱います。どちらかのスケールが0なら輪郭線は潰れた形で残し、塗り面は省略します。
BoundsのShapeとShapeCenteredは部品の変形へ追従し、Customは既存の独立した箱を使います。
各属性は既存と同じ非keyable・Channel Box表示で、接続、明示的なキー設定、Undo/Redo、保存に対応します。

Arrow・Finへの部品変形の範囲は次のとおりです。部品のSizeはオフセット距離に掛けず、
部品変形後に `shapeSize`、軸指定、回転、animation matrixなどの全体変形を適用します。
塗りのON/OFF・Color版で同じ輪郭を使い、軸色・template色の役割も維持します。

| 系列 | 部品変形の範囲と基準 |
| --- | --- |
| Square / Cube / Circle / Semicircle / Sphereの付属Arrow、ColorSphereArrow | 元の付け根 `+0.5` を基準に矢印を調整。本体との間の輪郭・面を接続する |
| 4Way Arrow | 各向きの付け根を基準に共通倍率を適用。元の大小の比率を保つ |
| ArrowAtEnd / ArrowAtEnds | 元の線・半円の端点にある先端をピボットに頭部を調整。矢印のある端だけが移動した先端へ追従 |
| Semicircleの端点矢印 | 角度調整後の端の接線方向を使う。角度0の既定軸では正のOffsetは `-Y` |
| Wideの端点矢印 | Lengthは頭部の深さ、WidthとSizeは頭部と帯の幅へ適用。先端・付け根の接続を再計算 |
| Cube / Cylinder / Pyramid / ConeのFin | Heightは張り出す高さ、Widthは付け根に沿う広がり。Offset・Lengthは適用せず、付け根を本体へ残す |
| Arrow | 矢印全体を一部品とし、元の先端 `+1stAxis=0.5` をピボットに調整。Finの付け根はOffset・Lengthへ追従し、高さは専用Heightで調整 |
| OctahedronArrow | 既定の本体はOctahedronと同じ±0.5の八面体。中央断面をLengthの基準とし、先端の1stAxis座標を `0.5 * shapePartSize * shapePartLengthScale + shapePartOffset` とする。OffsetとLengthは先端だけに適用し、中央断面から先端までの辺を直線に保つ。WidthとSizeは中央断面の幅へも適用し、断面を共有する反対側の面も追従。後端の1stAxis座標 `-0.5` は固定 |
| OctahedronArrowのFin | 尖った部分の変形とFinの高さを個別に調整。Finの付け根は変形後の本体へ追従 |

OctahedronArrowの中央断面の1stAxis座標は `0` のままです。
Sizeが1ならLengthが1で先端 `+0.5`、2で `+1.0`、3で従来の先端 `+1.5` になります。
Offsetは伸縮後に加算し、Fin版も同じ本体の寸法と変形規則を使います。

`shapeFin` がONなら本体へFinを1枚追加します。`shapeFinType` は `Standard` / `Tapered` の2値です。
Standardは本体に合った矩形などのFin、Taperedは付け根の一端を高く、反対側へ低くなるFinです。
立体、Line、CrossLine3Axisでは1st–2nd平面を使い、+2ndへ張り出します。
平面形状のFinは本体の中心軸から直角に立てます。向きは以下のとおりです。

| 本体 | Finの幅 | Finの張り出し |
| --- | --- | --- |
| CrossLine1st2nd系列 | 1st | +3rd |
| CrossLine1st3rd系列 | 1st | +2nd |
| Gear / Triangle / Square系列 / Diamond / Circle系列 / Semicircle系列 / CrossLine2nd3rd系列 | 2nd | +1st |

Taperedは幅の負側が高く、正側が低くなります。Color系のFinは通常色で、軸・回転の制約も本体と共通です。

ArrowのStandardは、くぼみの `1st=-0.25` から先端 `+0.5` までの矩形です。
従来のStandardの傾斜した外形はTaperedへ移しました。どちらもOffset・Lengthによる本体移動へ追従し、
根元を閉じる線は追加しません。

Finの基準は矢印や端の小形状を除いた本体断面です。端形状のSize / OffsetでFinを移動させず、
端の小形状それぞれにFinを追加することもありません。ArrowとOctahedronArrowだけは変形後の本体へ付け根が追従します。
SemicircleのFinの基準幅は `2nd=0..+0.5`、Widthのピボットは `+0.25` です。
円弧の角度を変えてもこの基準位置を使います。Circleの幅 `-0.5..+0.5` の半分となります。
平面形状のFinは本体中心軸へ接続し、根元を閉じる線は追加しません。
同じ平面にある付属矢印の面と重なる部分は差し引きます。
Line / CrossLineの平面端形状とCrossLine3Axisの立体端形状では、変形後の端形状の内部を
Finの輪郭線と塗りの両方から差し引きます。Color版にも同じ処理を適用し、Finの幅・高さ自体は保ちます。

旧Fin付き8項目と `TriangleArrow3D` は一覧から削除しました。対応は以下のとおりで、自動移行は行いません。
enum番号も変わるため、既存シーンでは `shape` を再指定し、必要な `shapeFin` / `shapeFinType` を設定してください。

| 旧名 | 現在のshape | shapeFinType（shapeFinはON） |
| --- | --- | --- |
| CubeFin / CylinderFin | Cube / Cylinder | Standard |
| CubeFinArrow / CylinderFinArrow | Cube / Cylinder | Tapered |
| OctahedronArrowFin | OctahedronArrow | Standard |
| ArrowFin | Arrow | Tapered |
| PyramidFin / ConeFin | Pyramid / Cone | Standard |
| TriangleArrow3D | Triangle | Tapered |

`shapePartFinHeight` は全106形状の `shapeFin` がONのときに適用し、
実効高さは `shapePartFinHeight * shapePartSize` とします。Offset・Length・Widthは高さに掛けません。
傾斜や頂点間の高さ比率を保ち、ArrowのTapered Finの中間頂点の高さは最大高さの半分です。
0ではFinの線・面のみを省略し、本体やArrowを残します。負値は付け根を移し替えず、自由頂点の張り出す方向を反転します。
既定値は各形状の基準寸法を維持します。`shapeFin` がOFFの間は形状を変えず、値を保持します。
接続、明示的なキー設定、Undo/Redo、保存に対応し、距離単位と全体変形に追従します。

付属ArrowとFinの塗りは、本体の断面に重なる領域を差し引きます。
付属Arrow3Dでは、Offsetで動いた矢印の付け根から元の付け根までの中央線を描きません。
直交する面は移動後の付け根・張り出し・先端からなる三角形とし、元の付け根までは延長しません。
付属Arrowの実効LengthまたはWidthが0なら、その部品の面を省略し、本体の面と潰れた輪郭を残します。
Finは専用Heightを使うため、Lengthが0でも高さを維持します。
ArrowのFinでは本体のLengthに沿って付け根も潰れますが、Widthが0でも独立したFin面を残します。
通常の端点矢印は頭部だけ、Wideの端点矢印は帯を含めて塗ります。
SemicircleのWide端点矢印の中心半径は `0.5` のまま、帯の半幅を `0.025 * abs(width)` とします。
帯が中心へ達したときは内半径を0とし、半円の外側にある頭部へも接続します。
Wideの端点矢印の頭部や帯が交差する条件では、面を重複させず和集合を塗り、外周だけを描きます。

`shapePartOffsetAngle` は `Semicircle`、`SemicircleArrow2D/3D`、
`SemicircleArrowAtEnd/AtEnds`、`SemicircleWideArrowAtEnd/AtEnds` に作用します。
円弧は上側の中心を保ち、全体の開き角を `180° + 2 * shapePartOffsetAngle` とします。
例えば `30°` は両端が30°ずつ開いて240°、`-30°` は120°の円弧です。
`-90°` は上端の一点、`90°` は360°の円になります。接続入力もこの範囲へ制限します。
円弧の分割密度は既定の円周64分割と同じで、両端と各軸方向の頂点を含めます。

Semicircleの端点矢印は、角度調整後の端点に頭部を置き、接線に沿って外向きに回転します。
その後に `shapePartOffset` の距離だけ同じ接線方向へ移動し、角度・移動では頭部の寸法を変えません。
長さと太さの調整は従来どおりSize・Length・Widthで行います。
Wide版は円弧の帯と移動後の頭部の間を一定幅の直線で接続し、頭部の底辺を一直線に保ちます。
頭部を大きく伸ばす場合も、円弧との接続が途切れない位置で帯の端を計算します。
円弧と頭部・頭部同士の面が重なるときは、和集合で二重描画と内部線を除きます。
上側に付属するArrow2D/3Dは元の位置に残し、Angleは円弧本体だけに適用します。
矢印のないSemicircleでは、Offset・Size・Length・Widthは形状を変えません。

`Line` と3種類の2軸 `CrossLine` に `ArrowAtEnds` を用意します。矢印の先端は元の線の両端 `±0.5` にあり、
中心線から30°ずつ開いた長さ `0.1` の2本の斜辺で構成します。
基準形状の開き角は60°、底辺幅は `0.1`、先端から底辺までの深さは
`0.1 × cos(30°)`（約 `0.08660254`）です。
`LineArrowAtEnds*` の矢印は1st–2nd平面に配置します。
2軸のCrossLineでは同じ平面に配置します。

`SemicircleArrowAtEnds*` の基準形状は元の半円を保ち、
半円の両端に同じ寸法の端点矢印を追加します。既定値では先端は元の端点から動かさず、
曲線の接線に沿って外向きにします。既定軸では半円はYZ平面の上半分で、
両端の矢印はともに `-Y` を向き、2nd–3rd平面に配置します。

通常の `ArrowAtEnds` は端点矢印の三角形だけを通常色で塗り、
半円の内側は塗りません。
輪郭線に底辺は追加せず、線・曲線の本体を維持します。
面には `shapeFillTransparency` を適用し、Wireframeでは通常の塗り形状と同様に
輪郭線だけを表示します。寸法と角度は基準形状での値であり、
軸指定、非等方スケール、回転、animation matrixなど既存の形状変形に追従します。

同じ5系列に `WideArrowAtEnds` を用意します。
先端位置、斜辺 `0.1`、開き角60°、底辺幅 `0.1` は通常のArrowAtEndsと共通です。
軸は中心線の両側へ `0.025` ずつ離した幅 `0.05` の帯とし、
矢印の付け根へ接続した閉じた輪郭を描きます。中心線や付け根の内側の線は描きません。
3種類のCrossLineは2本の帯を一つの十字にまとめ、中央の内部線や面の重複を作りません。
配置平面は対応する通常のArrowAtEndsと同じです。

`SemicircleWideArrowAtEnds*` は半径 `0.5` の半円を中心に、
内側半径 `0.475`、外側半径 `0.525` の帯を配置します。
帯の両端は矢印の付け根の高さ `0.1 × cos(30°)` で切り、
元の端点にある矢印へつなぎます。半円の頂点は高さ `0.525` になります。
`WideArrowAtEnds` は帯と矢印の内側全体を通常色で塗り、
半円の中央の空間は残します。面には `shapeFillTransparency` を適用し、
Wireframeでは閉じた輪郭だけを表示します。
各系列の一覧では、通常版とWide版を分け、それぞれEnd、Endsの順に並べます。

片側だけに矢印を付ける形状は、Line・2軸CrossLine3種類・Semicircleの5系列に用意します。
各系列の `ArrowAtEnd`、`WideArrowAtEnd` の計10種類です。
全端版の `ArrowAtEnds`、`WideArrowAtEnds` の10種類も維持します。
Lineと2軸CrossLineの片側版は平面の端形状と同じ代表軸の正側を使い、
CrossLineの名称から配置軸の指定を省略します。
他の向きは `shape1stAxis` / `shape2ndAxis` で調整します。
Pythonのenum定数も同じ名称へ揃え、削除した片側方向の別名は設けません。

SemicircleのEndは、主軸の正回転方向へ円弧をたどった終点です。
基準の主軸 `+X`、補助軸 `+Y` では、始点が `-Z`、終点が `+Z` となり、
終点の矢印は `-Y` を向きます。`+X` に対する正回転の接線と一致します。
この定義は主軸・補助軸で作る基準座標系に対して適用し、その後に全体変形を適用します。
旧 `SemicircleArrowAtStart` / `SemicircleWideArrowAtStart` の形状を新しい `AtEnd` とし、
旧 `AtEnd` の逆回転側は削除しました。

Endは軸指定・回転・反転後も同じ端へ追従します。
頭部の寸法・配置平面・部品変形は両端版と共通です。
`shapePartOffset` は矢印のある端だけに作用し、矢印のない端は本体の端点に残します。
Semicircleの `shapePartOffsetAngle` は片側版でも円弧の両端を開き、
矢印のある端では移動後の接線方向に頭部を合わせます。
Wide版の矢印のない端は、直線なら軸に直交、Semicircleなら半径方向の平らな線で閉じます。
通常の塗りは片側の頭部だけ、Wideの塗りは帯と片側の頭部の内側全体を塗ります。

2軸CrossLineでは代表の1端だけに矢印を付けます。
例えば `CrossLine1st3rdArrowAtEnd` は `+1stAxis`、
`CrossLine2nd3rdWideArrowAtEnd` は `+2ndAxis` の端を使います。
頭部の寸法と部品調整はLineの片側版と共通です。
Offsetは指定した矢印とその端へ作用し、残り3端は元の `±0.5` に残します。
Wide版のWidthとSizeは頭部と十字全体の帯幅へ適用し、矢印のない3端は平らに閉じます。
中央や頭部が交差する部分は和集合とし、内部線と半透明塗り面の重複を作りません。
通常の塗りは1枚の頭部だけ、Wideの塗りは帯と頭部の内側全体を塗ります。
軸指定・全体変形・Bounds・選択と表示の規則は既存形状に従います。

`shapeFill` は既存の輪郭を保ち、ONで面を追加します。純粋な線形状
（`Line`、`CrossLine1st2nd/1st3rd/2nd3rd/3Axis`、`ColorCrossLine3Axis`）では
ONでも面を作りません。値は保持し、別の形状へ切り替えるとその設定が適用されます。
OFFでも `shapeFillTransparency` を保持し、再びONにすると同じ透明度を使います。
十字線など面積のない付属部分は線のままです。
`Triangle`、`Square`、`Circle` は YZ 面にあり、
`Triangle` の底辺は塗りの有無にかかわらず Y=`-0.37` です。
立体形状の基準形状は３軸とも `-0.5` から `+0.5` に収まります。
`Cylinder` は側面と両端、`Cone` は側面と底面を描き、
円周は輪郭線と同じ64分割です。面は Viewport 2.0 の三角形描画であり、
NURBS の CV・UV・材質・レンダリング用サーフェスではありません。
`Gear` は外周と内円の間を塗り、内円の内側を穴として残します。
`Semicircle` は底辺のない半円です。`Semicircle` と
`SemicircleArrow2D/3D` は、円弧の中心と両端を結ぶ扇形を塗ります。
Angleが30°では240°の扇形、0では半円板、90°では円板、-90°では面積0となります。
中心へ向かう2本の境界線は輪郭として追加しません。付属矢印の塗り面も同じ扇形断面を差し引き、
本体との二重描画を避けます。開き角が0°より大きく180°未満の塗りでは、
中心もShape / ShapeCenteredの範囲に含みます。
Semicircleの通常の端点矢印の塗りは矢印だけ、Wide版の塗りは帯と矢印を塗ります。
矢印の突起と Fin も面を持ち、Fin は厚みのない面です。
`3D` 系の矢印の塗りは、主平面と直交する薄い三角面で表し、閉じた立体には
しません。`OctahedronArrow` のStandard Finは、八面体の上半分と重ならない左右の
三角面だけを塗ります。
`SquareArrowCrossLineTemplate*` は十字線、`SquareTemplateArrow4Way*` は四隅だけを
template 色・選択不可にします。`ColorSphere` は X=赤、Y=緑、Z=青の
直交円だけで構成し、十字線を含みません。`ColorSphereArrow2D` と
`ColorSphereArrow3D` は同じ軸色の円へ通常色の矢印を加えます。
`2D` の矢印は主平面上、`3D` の矢印はそれと直交する面にもあります。
`ColorSphereCrossLine` はその円に
`ColorCrossLine3Axis` の十字線を加えます。十字線の正方向は各軸色、負方向は通常色です。
Color系は後述の描画規則により、シェイプ編集で軸色の向きを変えません。
`SquareTemplateArrow4Way*` では四角い本体面が template 色・選択不可、
矢印面は通常色・選択可能です。`SquareArrowCrossLineTemplate*` の
十字線は template 線のままで、本体面からは選択できます。
`ColorSphere`、`ColorSphereArrow2D/3D`、
`ColorSphereCrossLine` は球殻を通常色で塗り、軸色の円を維持します。
矢印付きでは矢印面も通常色で塗り、`ColorSphereCrossLine` は十字線を維持します。

`ColorCube` は正側の3面に、面の法線に対応する軸色の四角い枠を置きます。
基準の `+X` 面は赤、`+Y` 面は緑、`+Z` 面は青です。枠は面の位置 `+0.5` を
保ち、面内の2軸を `-0.495` から `+0.495` に縮めます。各辺を内側へ `0.005` 入れることで、
異なる色が同じ線分を共有することを避けます。負側の角に集まる残り3辺は通常色です。
角には小さな隙間があり、画面上の分離量は視線・ズーム・線幅に依存します。
`shapeFill` がONなら、`ColorCube` は同じ輪郭を保ち、Cubeの6面を通常色で塗ります。

`ColorCornerCube` は通常色のCube輪郭と、正側の角 `(+0.5, +0.5, +0.5)` に
接する軸色の小四角3枚から構成します。小四角は各正側面の面内座標 `0.3` から
`0.5` にあり、一辺は基準Cubeの一辺1に対して `0.2` です。小四角はWireframeでも
塗り面として表示し、面内のクリックで選択できます。小四角に接する輪郭線3本は
その境界で止め、色面上に通常色の線を重ねません。小四角もColor系の描画規則に従い、
軸色と選択色の扱いは他のColor系と共通です。
`shapeFill` がONなら、`ColorCornerCube` は正側3面の小四角部分を除いたL字形の領域と、負側3面を
通常色で塗ります。小四角と本体面は境界を共有し、面積は重なりません。
本体面には `shapeFillTransparency`、小四角には `shapeTransparency` を適用します。
塗りONでは、本体面は既定の透明度85%、小四角は不透明です。これら2種類にもFinオプションを適用できます。
ColorCornerCubeの小四角は `shapeFill` がOFFでも表示・選択でき、Wireframeでも残ります。

Color系12種類は、シェイプ編集を適用する段階で軸色と親transformのローカルXYZの対応を保ちます。
属性値や接続は変更せず、描画用に読み取った設定だけを次のように扱います。

| 属性 | Color系の描画用設定 |
| --- | --- |
| `shape1stAxis` / `shape2ndAxis` | `+X` / `+Y` に固定 |
| `shapeRotate` / `shapeAxisRotate` | 各XYZ成分を0として扱う |
| `shapeScale` / `shapeAxisScale` | 各XYZ成分の絶対値を適用 |
| `shapeSize` / `shapeRootSize` | 絶対値を適用 |

移動、正のスケール、軸オフセット、部品の変形は引き続き適用します。0スケールも0のままです。
通常の形状へ切り替えると、保持していた軸指定・回転・符号付きスケールが再び作用します。
輪郭・塗り面・小四角・OffsetLine・Shape / ShapeCentered Boundsは同じ描画用設定を使います。
Custom Boundsの独立した軸指定・回転・スケールには、この制約を適用しません。

`shapeAnimationTransformMatrix` はColor系でも分解・加工せず、そのまま適用します。
行列や親transformに回転・シアー・反転が含まれる場合、色付き部位もその変換に追従します。
これらは利用者が与える変換として扱い、シェイプ編集の制約とは分けます。

`Custom` 用の調整属性は `shapeAnimationTransformMatrix` を除き、形状本体から独立しています。
基準形状は固定の `Cube` で、`shape` と OffsetLine に対応する属性はありません。

| Custom attribute | Maya の型 | 既定値 | 対応する形状属性 |
| --- | --- | --- | --- |
| `customBounds1stAxis` / `customBounds2ndAxis` | enum | `+X` / `+Y` | `shape1stAxis` / `shape2ndAxis` |
| `customBoundsRootSize` | `double` | `1` | `shapeRootSize` |
| `customBoundsTranslate` | `doubleLinear3` | `(0, 0, 0)` | `shapeTranslate` |
| `customBoundsRotate` | `doubleAngle3` | `(0, 0, 0)` | `shapeRotate` |
| `customBoundsScale` | `double3` | `(1, 1, 1)` | `shapeScale` |
| `customBoundsAxisOffsetLength` | `doubleLinear` | `1 cm` | `customBoundsAxisOffset=true` のときだけ作用する `shapeAxisOffsetLength` 相当の長さ。最小値 `0` |
| `customBoundsAxisOffset` | `bool` | `false` | `shapeAxisOffset` |
| `customBoundsAxisOffsetDirection` | enum | `+1stAxis` | `shapeAxisOffsetDirection` |
| `customBoundsAxisTranslate` | `doubleLinear3` | `(0, 0, 0)` | `shapeAxisTranslate` |
| `customBoundsAxisRotate` | `doubleAngle3` | `(0, 0, 0)` | `shapeAxisRotate` |
| `customBoundsAxisScale` | `double3` | `(1, 1, 1)` | `shapeAxisScale` |
| `customBoundsSize` | `double` | `1` | `shapeSize` |

表示する調整属性は、複合属性の X/Y/Z 子属性も含めて非 keyable・Channel Box 表示です。
Channel Box から値を編集でき、DG 接続や属性を明示したキー設定も可能です。
通常の一括キー操作では対象になりません。２つの軸指定と軸オフセット方向の
enum 値は形状本体と Custom で共通です。
`shapeAnimationTransformMatrix` は Channel Box に表示せず、接続と
`ModifierManager` 経由の設定に対応します。

Channel Box の表示順は次の７区画です。区切りは表示順に `_`、`__`、`___`、`______`、`____`、
`_____` という表示専用の１値 enum 属性で、値は
`-----------------------------------`、非 keyable・ロック済みです。

1. `shape`、`shapeFin`、`shapeFinType`、`shapeDrawOnTop`、`shapeLineWidth`、`shapeTransparency`、`shapeFill`、`shapeFillTransparency`、`showShapeOffsetLine`、`shapeOffsetLineTemplate`
2. `shape1stAxis`、`shape2ndAxis`、`shapeAxisOffset`、`shapeAxisOffsetDirection`、`shapeAxisOffsetLength`
3. `shapeRootSize`、外側の移動・回転・スケール、内側の移動・回転・スケール、`shapeSize`
4. `shapePartOffset`、`shapePartOffsetAngle`、`shapePartFinHeight`、`shapePartSize`、`shapePartLengthScale`、`shapePartWidthScale`
5. `boundsMode`、`showBoundsPreview`
6. `customBounds1stAxis`、`customBounds2ndAxis`、`customBoundsAxisOffset`、`customBoundsAxisOffsetDirection`、`customBoundsAxisOffsetLength`
7. `customBoundsRootSize`、外側の移動・回転・スケール、内側の移動・回転・スケール、`customBoundsSize`

区切りは Python の生成 NodeOperator API から除外します。
`MPxLocatorNode` から継承する `localPositionX/Y/Z` と `localScaleX/Y/Z` は
描画に使わないため、`bdControllerShape` では Channel Box の既定表示から外します。
標準の locator の表示設定には影響しません。

点 `p` に適用する階層は `shapeAnimationTransformMatrix > shapeRootSize > shapeTranslate > shapeRotate >
shapeScale > 軸指定 > shapeAxisOffsetLength > shapeAxisOffset > shapeAxisTranslate >
shapeAxisRotate > shapeAxisScale > shapeSize > p` です。
ここで `p` は部品の変形と接続線の追従を反映した基準形状の頂点です。
外側・内側の XYZ 回転をそれぞれ `R`・`R_axis`、軸指定から作る回転を `A`、
軸オフセットを `O_axis`、選択軸だけを伸縮する変換を `S_axis` とすると、
計算結果は次のとおりです。

```text
p_out = shapeRootSize * (
    shapeTranslate + R_XYZ(
        shapeScale ⊙ A(S_axis(
            O_axis + shapeAxisTranslate + R_axis_XYZ(
                shapeAxisScale ⊙ (shapeSize * p)
            )
        ))
    )
)
p_local = p_out * shapeAnimationTransformMatrix
```

行列の積は Maya の行ベクトル規約で表しています。行列は親 `transform` の
ローカル空間で適用し、その後の親 DAG 変換は Maya に任せます。
ワールド空間の行列を使う場合は、親の `worldInverseMatrix` でローカル空間へ
変換してから接続します。行ベクトル規約では、別ノードの `worldMatrix` を
`W`、shape の親の `worldInverseMatrix` を `P⁻¹` とすると、入力行列は
`W * P⁻¹` の順です。このとき shape の頂点は、親の変換を経た後に
`p_out * W` の位置になります。`W` をそのまま接続すると親の変換が重複します。
行列の平行移動は `shapeRootSize` の影響を受けません。
非等方スケールやシアーも、行列を分解せず頂点へ適用します。
Color系は上記の描画用設定で `p_out` を計算し、入力行列と親DAG変換はそのまま適用します。

### 描画属性

`shapeLineWidth`、`shapeTransparency`、`shapeFillTransparency`、
`shapeDrawOnTop` は Viewport 2.0 の描画だけを調整します。線幅は画面上の
pixel 指定で、シーン単位や `shapeSize` とは独立しています。
`shapeTransparency` は輪郭線と OffsetLine、`shapeFillTransparency` は
`shapeFill` がON の本体面に適用します。`ColorCornerCube` の小四角だけは
`shapeTransparency` に従います。面と輪郭線は選択状態に応じた色を使います。
`shapeDrawOnTop` は輪郭線・面・OffsetLine を他のシーン形状より前に描きます。
面を含む形状では、Shaded は面と輪郭線、Wireframe は輪郭線、
Wireframe on Shaded は面と輪郭線を表示します。面内のクリックも選択対象です。
`ColorCornerCube` の小四角はWireframeでも表示・選択できます。
`showBoundsPreview` の確認用の箱は従来の template 色・線幅・選択不可を維持し、
これらの属性の影響を受けません。描画属性の変更はフォーカス範囲を変えず、
本体と OffsetLine のクリック選択の可否も変更しません。

`shapeFill` は面の生成と選択判定、形状キャッシュ、描画範囲を更新します。
Semicircleの中心やSphereの面の頂点が加わる場合はShape / ShapeCenteredの範囲も変わります。
Custom Boundsは塗りのON/OFFから独立しています。接続・明示的なキー設定・Undo/Redo・保存に対応します。

### フォーカス範囲

`boundsMode=Shape` は変形済みの形状本体と表示中の OffsetLine を
含む範囲を返します。

`boundsMode=ShapeCentered` は形状の種類・軸指定・回転・スケール・サイズを使い、
既定のフォーカス範囲を求めます。
`shapeTranslate`、`shapeAxisTranslate`、`shapeAxisOffset` による位置ずれと
OffsetLine を除外します。`shapeAxisOffset=true` のときは
`shapeAxisOffsetLength` と `shapeAxisOffsetDirection` による伸縮を保持します。
この調整値で求めた形状の軸平行範囲を、まず親 `transform` のローカル原点を
中心とする箱に置き直します。その８角へ `shapeAnimationTransformMatrix` を
そのまま適用し、最終的な軸平行範囲を求めます。
したがって行列の平行移動もフォーカス範囲へ反映されます。
例えば他の変形が既定値の `Cube` で `shapeAxisOffset=true`、
`shapeAxisOffsetLength=5 cm` なら、
行列適用前の伸縮方向の範囲は `-2.5 cm` から `+2.5 cm` です。
`CircleArrow2D` のように非対称な形状でも、行列適用前の範囲の中心は原点です。

`boundsMode=Custom` は独立した調整属性で固定の `Cube` の８角を変形し、
さらに共有の `shapeAnimationTransformMatrix` を適用してから軸平行範囲を
求めます。Custom の箱は形状本体より小さくも大きくもできます。
`showBoundsPreview` は選択中の `boundsMode` の最終範囲を表示するだけで、
フォーカス範囲を変更しません。`Shape` では表示中の OffsetLine も範囲へ含みます。

`MPxLocatorNode::boundingBox()` は選択したモードの範囲を返すため、
`MFnDagNode.boundingBox`、親 `transform` の `xform -bb`、標準の
F / Ctrl+F によるフレームへ反映されます。Ctrl+F は子 transform も含むため、
子の範囲は別途合算されます。Viewport 2.0 の描画 override はカリング用に
形状本体・表示中の OffsetLine・表示中のフォーカス範囲プレビューを包む範囲を返します。
クリック選択に使う線は形状本体と、template ではない OffsetLine のままです。

ここで `⊙` は成分ごとの積です。`shapeRootSize` は平行移動と軸オフセットにも影響し、
`shapeSize` は頂点だけを拡縮します。既定の
`shape1stAxis=+X`・`shape2ndAxis=+Y` では `A` は恒等回転です。
`shape1stAxis` は基準の `+X`、`shape2ndAxis` は基準の `+Y` の行先です。
残る `+Z` は「主軸 × 補助軸」で決め、右手系を維持します。
したがって Axis 系の X/Y/Z 成分は、それぞれ主軸／補助軸／第３軸に対応します。
`shape1stAxis=+Z`・`shape2ndAxis=+Y` なら基準の `+X/+Y/+Z` は
表示上の `+Z/+Y/-X` へ向き、平面形状は XY 面になります。
主軸と補助軸が同じ方向または正反対のときは主軸を優先し、補助軸に
`+Y` を使います。主軸が `+Y` または `-Y` の場合だけ `+Z` を使います。
これらは親 `transform` のアニメーション用 TRS とは別です。

`shapeAxisOffset` が `false` のときは `O_axis=(0, 0, 0)` です。
`true` のときは、`shapeAxisOffsetDirection` に応じて次の値を使います。

| 方向 | 軸指定前の `O_axis` |
| --- | --- |
| `+1stAxis` / `-1stAxis` | `(+0.5, 0, 0)` / `(-0.5, 0, 0)` |
| `+2ndAxis` / `-2ndAxis` | `(0, +0.5, 0)` / `(0, -0.5, 0)` |
| `+3rdAxis` / `-3rdAxis` | `(0, 0, +0.5)` / `(0, 0, -0.5)` |

`1stAxis` は主軸、`2ndAxis` は補助軸、`3rdAxis` は「主軸 × 補助軸」の方向です。
無効な軸の組では、形状と同じ補正後の補助軸と第３軸を使います。
主軸が `-X` なら `+1stAxis` は `-X` 方向、`-1stAxis` は `+X` 方向です。
`S_axis` は `shapeAxisOffset=true` のとき、方向の正負にかかわらず選択軸の１成分だけを
`shapeAxisOffsetLength / 1 cm` 倍します。オフのときは恒等変換です。
基準形状の長さは内部座標で `1 cm` なので、
他の変形が既定値の `Cube` では、軸オフセットをオンにすると正方向は
`0` から指定長、負方向は `-指定長` から `0` まで伸びます。
軸オフセットがオフなら、長さと方向の値を変えても形状は伸縮しません。
オンで `0 cm` にすると選択軸方向に潰れます。接続から負値が入った場合も、形状の計算では
`0 cm` として扱います。`shapeAxisTranslate` の選択軸成分も
この長さで伸縮します。`shapeSize`、`shapeAxisScale`、内側の回転、外側のスケールなどを
変更した場合、形状の端や実際の長さは指定長と一致するとは限りません。
固定 `0.5` は `shapeSize`、`shapeAxisScale`、`shapeAxisRotate` の影響を受けず、
`shapeAxisOffsetLength`、外側の `shapeScale`、`shapeRotate`、`shapeRootSize` の影響を受けます。
`shapeAxisTranslate` には加算して使えます。`shapeAxisOffset` をオフにすると
`shapeAxisOffsetDirection` も変形に作用しません。
その他の変形が既定値の `Cube` は、`+1stAxis` へのオフセットで主軸方向の範囲が
`0` から `1` になります。`shapeSize` だけを `2` にすると `-0.5` から `1.5` です。

補助線の始点は親 `transform` のローカル原点 `(0, 0, 0)`、終点は上記の式に
`p=(0, 0, 0)` と `O_axis=(0, 0, 0)` を代入し、
`shapeAnimationTransformMatrix` を適用した形状基準位置です。
`shapeTranslate` と `shapeAxisTranslate` の移動を反映し、軸オフセットを除外します。
`shapeAxisOffset=true` なら `shapeAxisOffsetLength` は
`shapeAxisTranslate` の選択軸成分を伸縮するため、終点にも反映します。
`shapeAxisOffset` の固定位置成分、`shapeAxisRotate`、`shapeAxisScale`、
`shapeSize` は終点を動かしません。行列が単位行列のとき、軸オフセットだけを
オンにした場合は補助線を描きません。
始点と終点が重なる場合は線を描きません。
形状本体の描画範囲には、軸オフセット後の形状本体と、表示中の補助線の
両方を含めます。フォーカス範囲へ補助線を含めるのは `boundsMode=Shape` の
場合だけです。
`shapeOffsetLineTemplate` が `true` のときは補助線だけを選択対象から外し、
Maya の template 表示色で描きます。`false` なら補助線は通常のワイヤーフレーム色で
クリック選択に使えます。どちらの設定でも形状本体の輪郭線は選択できます。
補助線が形状本体の線と重なる箇所では、本体の線で選択される場合があります。

`Square` と `Circle` は YZ 面（`x=0`）にあり、Y/Z の各軸が
`-0.5` から `+0.5` の範囲に収まります。既定の `Cube` は３軸とも同じ範囲です。
`CircleArrow2D` は YZ 面で、半径 `0.5` の円と、
`(y, z)=(0.495096189432334, -0.075)` → `(0.625, 0)` →
`(0.495096189432334, +0.075)` の独立した山形の線からなります。
`CircleArrow3D` は矢印に第１軸方向へ張り出すフィンを加えます。

基準形状を作る調整属性が固定されている間は、その頂点を再利用します。
`shapeAnimationTransformMatrix` だけが変化する場合は、基準頂点を作り直さず、
行列による頂点変換と補助線・描画範囲の更新だけを行います。
親 `transform` のアニメーションでも基準形状は再計算しません。
基準形状の調整属性自身をアニメーションまたは接続で変更する場合は、
値が変わった時点で基準形状を更新します。

## 実装と拡張

公開済みの node type は `bdControllerShape`、`MTypeId` は `0x0014271F` です。
ID の管理方針は [NODE_IDS.md](../NODE_IDS.md) に従います。
実装は [BdControllerShapeNode.cpp](../plugins/bdUtilNodes/src/nodes/BdControllerShapeNode.cpp)、
プリセットの一覧と輪郭は [BdControllerShapePresets.inc](../plugins/bdUtilNodes/src/nodes/BdControllerShapePresets.inc)、
Maya 上の挙動テストは [test_bd_controller_shape.py](../../../tests/maya/node/operator/node/dag/shape/test_bd_controller_shape.py)、
公開 API の型確認は [public_node_types_contract.py](../../../tests/typecheck/public_node_types_contract.py)
にあります。
線の形状は独立したストロークの配列で保持し、ストロークごとに線を描きます。
そのため `CircleArrow2D` の円と矢印や、色や選択可否の異なる部分を、橋渡しの線なしで
１つの shape に収められます。現在の円は 64 分割の折れ線で、NURBS の
degree や surface を持つ形状ではありません。
`shapeFill` がONの面は同じ shape 内で表示種別ごとの三角形列として保持し、線と同じ形状変形と
`shapeAnimationTransformMatrix` を適用します。Square は２三角形、Circle は
64分割の扇形、Cube は６面の12三角形、Sphere は32経度×16緯度の球面です。
面の頂点も描画範囲と `boundsMode=Shape` の算出に含めます。
`shapeDrawOnTop` がオンのときは、最前面表示に対応するためストロークを
線分へ展開して描画します。色と選択可否はストロークごとに保持します。
オフの既定状態では通常の深度テストを使います。

### プリセットを追加するとき

`BdControllerShapePresets.inc` の `kPresetNames` の順序が公開 `shape` enum の数値です。
同じ順序の `kPresetInfo` で、各選択肢を輪郭番号、端の配置へ対応付けます。塗りの有無は `ShapeSettings.fill` で保持します。
`PartEnds` と `partAxis` は端点矢印・平面の端形状で共用します。
輪郭番号は enum 値とは別で、輪郭線の組み立ては `appendPresetGeometry()` にあります。
線ごとの `Normal`・`Template`・軸色の指定もここで行います。
塗り面を追加するときは `BdControllerShapeNode.cpp` の `makeFillParts()` に面を定義し、
輪郭と同じ変形・外縁になることを確認します。template 面の選択可否も面側で指定します。

形状を追加したら、`kPresetNames` と `kPresetInfo` の件数、仕様書の形状一覧、
`test_bd_controller_shape.py` の `SHAPE_NAMES` と bounds の期待値を揃えます。
塗りON/OFFのbounds、Undo/Redo、シーン再読込をテストし、Viewport では
Wireframe・Shaded の輪郭と面、色、クリック選択、Selection Highlighting を確認します。
Python の公開 enum は下記の生成手順で更新し、生成ファイルを手編集しません。

### 調整属性を追加するとき

`BdControllerShapeNode::initialize()` の `addAttribute()` の順序が Channel Box の
６区画の表示順になります。新しい調整属性は該当区画へ登録し、非 keyable・
Channel Box 表示を設定します。複合属性では X/Y/Z 子属性にも同じ設定が必要です。
`shapeAnimationTransformMatrix` は表示しない例外です。区画を増やす場合は
新しい区切り属性も追加し、表示専用・非接続・非保存・ロック済みとします。
区切り名を変更したときは、Python 生成器の除外条件も確認してください。

形状、フォーカス範囲、プレビューに作用する属性では、値の読み取り、
対応する基準形状・変換後のキャッシュの無効化、描画範囲まで確認します。
属性定義の変更後は下記の生成ファイルを更新し、Channel Box の順序・表示状態と
値変更後の描画・`boundingBox()` を自動テストと GUI の両方で確認します。

### 基準形状を追加する際の座標規約

新しい形状のストロークを構成する頂点は、軸指定や各変形を適用する前の
ローカル座標で作ります。
基準の `+X` を主軸、`+Y` を補助軸、`+Z` を「主軸 × 補助軸」とする右手系です。
現在の２次元形状は YZ 面（`x=0`）に置き、基準の `+X` は面の法線です。
`CircleArrow2D` の矢印が元の `+Y` を向くのは意図した仕様で、主軸が形状の
長手方向である必要はありません。

旧モジュール由来の `RawPoint` は XY 面・`+Z` 法線の座標です。
`appendPresetComponent()` は primitive 個別の拡縮・回転・移動後に
`(x, y, z) → (z, y, -x)` へ変換し、上記の基準座標へ渡します。
面の `appendLegacyTriangle()` なども同じ変換を使います。
新しい頂点を追加するときは旧座標と変換後の座標を混同せず、輪郭と面の向きを揃えます。

骨に沿う３次元形状で `shapeAxisOffsetLength` を骨長として使う場合は、
伸縮対象の軸の基準範囲を `-0.5` から `+0.5`、長さを `1` にします。
`shapeAxisOffset` は選択方向へ固定 `0.5` を加え、長さ属性は同じ軸を
伸縮するため、他の変形が既定値なら端を原点に揃えつつ指定長まで伸ばせます。
基準範囲が異なる形状では、この原点合わせと長さの一致を前提にしません。
形状を追加するときはストロークの区切り、基準 bounds、軸指定・オフセット・
行列適用後の bounds と選択範囲を確認します。

基準形状と行列適用後の形状、および Custom の基準箱と行列適用後の箱を
同じ node 内で別々にキャッシュします。
直接の属性変更と接続変更は `MNodeMessage` callback で対応するキャッシュを
無効化します。入力接続がある場合は、再生中の値の変化を拾うために値を比較します。
基準形状の調整値が同じなら頂点を再生成せず、行列が同じなら変換後の頂点も
再生成しません。入力接続のない状態では変更通知がない限り plug の読み取りも
省きます。親 `transform` の TRS は基準形状の再生成条件に含めません。
描画 override は選択色などの表示変化に追従するため常時更新とし、
静的な調整値では属性の再読込と頂点・描画範囲の再計算を省きます。
キャッシュの仕組みを変更する際は、描画と両方の `boundingBox()`、
属性の直接編集、Undo/Redo、キー・接続による変化を一緒に確認してください。
再生速度の改善量はまだ実測していません。

`shape` enum の選択肢やフォーカス関連の属性を変更する場合も、
ネイティブ属性の変更です。
対応 Maya version の plug-in をビルド・配置した後、
Maya 2025 でその plug-in をロードして `generate_node_class_file()` から
`bdControllerShape` の Python 定義を再生成します。生成対象は
`node_attr/bd_controller_shape.py` と `_generated/bd_controller_shape.py` です。
生成手順は [generator.md](../../../bakedanuki/bakedanuki-util/docs/maya/node_operator/generator.md)
を参照してください。生成ファイルは手編集せず、テストと仕様書を同時に更新します。
完了前の統一検証は repository 直下で `.\scripts\verify.cmd -IncludeNative` です。

### 今後の候補: 多数配置時の再生性能測定

多数の `bdControllerShape` を置いたシーンで、調整属性が静的な場合、
`shapeAxisTranslate` などにキーや入力接続がある場合、親 `transform` のみを
アニメーションする場合の再生時間を比較します。基準頂点と変換後頂点の
再生成回数も記録し、現在のキャッシュが効く条件と負荷の大きい処理を特定します。
最適化が必要と分かった場合は、描画・クリック選択・`boundingBox()` の結果を
保ったまま、実測した負荷箇所に絞って変更します。

## 表示と選択

この shape は Maya 標準の `nurbsCurve` ではありません。
**Show > NURBS Curves** と **Alt + 1** の切り替え対象にはなりません。
`bdControllerShape` は `MPxLocatorNode::excludeAsLocator()` で `false` を返し、
**Show > Locators** をオフにしたビューポートでも描画する設計です。
Viewport 2.0 では **Show > Plugins > Plugin Shapes** をオフにすると、
描画オーバーライドが線と面の描画を省略します。オンに戻すと描画します。
shape 自身の `visibility` をオフにすると非表示になります。
この表示条件は [Autodesk の API 説明](https://help.autodesk.com/cloudhelp/2024/ENU/MAYA-API-REF/cpp_ref/class_m_px_locator_node.html)
に基づきます。

**Show > Selection Highlighting** はビューポートごとに反映します。
オンでの選択表示は Maya の選択色に従います。オフでは、選択中も
実効displayTypeの非選択時と同じ線色・面表示にします。
`Normal` では通常色とRGBの軸色、`Template` ではMayaのtemplate色、
`Reference` ではMayaのreference色で通常線を描きます。
`Template` と `Reference` の非選択表示では通常の塗り面を省き、
`ColorCornerCube` の小四角は塗り面として残します。
親transform、上位のDAG、Display Layer経由のdrawOverrideにも同じルールを適用します。

Color系の軸色の線と小四角は、非選択表示で次のHSV値を使います。
HueはX=`360°`（`0°`）、Y=`120°`、Z=`240°`です。

| 実効displayType | Saturation | Value |
| --- | --- | --- |
| `Normal` | `1` | `1` |
| `Template` | `0.25` | `0.5` |
| `Reference` | `0.25` | `0.25` |

Selection Highlightingがオフの選択中も同じ軸色を使います。
透明度は線・小四角に `shapeTransparency`、通常の塗り面に
`shapeFillTransparency` を適用します。形状内のtemplate部分と
`shapeOffsetLineTemplate` は、DAG全体のdisplayTypeとは独立した指定です。
選択そのものと、template色・選択不可の部分には影響しません。

ビューポートの描画とクリック選択は `mayapy` のヘッドレステストだけでは
確認できません。Maya 2025 / 2026 / 2027 の GUI で次を確認してください。

1. `CircleArrow2D` を表示し、円と矢印が独立した２つの輪郭として見え、橋渡しの線がない。
2. 親 `transform` を選択解除し、円と矢印のそれぞれをクリックすると、同じ親 `transform` を選択できる。
3. **Show > Plugins > Plugin Shapes** をオフにするとこの shape が消え、オンに戻すと再び表示される。オフの間にクリックで選択されないかも確認する。
4. **Show > Locators** をオフにして標準 locator が消えても、この shape は表示される。
5. shape の `visibility` をオフにすると消え、オンに戻すと再び表示される。
6. `shape` と各変形属性を変えた直後に、描画と選択範囲が更新される。
7. シーンを Maya ASCII で保存して再読込し、上記の表示と選択を再確認する。
8. `shapeTranslate` を動かし、`showShapeOffsetLine` をオンにすると親のローカル原点から、軸オフセットを除いた形状基準位置へ補助線が出る。オフにすると消える。
9. 本体の線と重ならない補助線上をクリックし、`shapeOffsetLineTemplate` がオンなら選択されず、オフなら親 `transform` が選択される。どちらの設定でも本体の線は選択できる。
10. `shapeOffsetLineTemplate` をオンにすると補助線だけが Maya の template 表示色になり、オフにすると通常のワイヤーフレーム色に戻る。本体の線の色は変わらない。
11. 軸指定と内側の移動・回転・スケールを変更し、形状、補助線、選択範囲が直後に更新される。無効な軸の組では主軸が保たれる。
12. 親 `transform` をアニメーションしても、形状が追従し、ローカル形状の調整値は変わらない。
13. `shapeAxisTranslate` などの調整属性にキーまたは入力接続を作り、タイムラインを動かすと形状と選択範囲が追従する。直接編集と Undo/Redo の後も更新される。
14. `shapeAxisOffset` をオンにして６方向を切り替えると、形状本体と選択範囲が更新される。`Cube` の既定サイズでは片面が原点に揃い、`shapeSize=2` でも移動量は固定 `0.5` のままになる。
15. `showShapeOffsetLine` をオンにし、軸オフセットを切り替えても補助線の終点が動かない。軸オフセットだけをオンにした場合は線が出ない。
16. `Cube` で `shapeAxisOffset` をオンにすると `shapeAxisOffsetLength` で指定軸だけが伸縮し、形状本体と選択範囲が更新される。オフなら長さと方向を変更しても伸縮しない。
17. `shapeAxisOffset` がオンで `shapeAxisTranslate` の選択軸成分がある場合、長さの変更が補助線の終点にも反映される。他の変形が既定値の `Cube` では、距離プラグからの接続やシーン単位の変更後も、骨長と形状の長さが一致する。
18. `shapeAnimationTransformMatrix` に `composeMatrix.outputMatrix` を接続し、接続元をアニメーションすると形状・描画範囲・クリック選択が追従する。基準形状の調整値は変わらない。
19. 補助線の基準終点が原点でも、行列の平行移動で終点が動くと親のローカル原点から補助線が出る。行列を戻すと消える。
20. `boundsMode` を３値で切り替え、F と Ctrl+F のフレーム範囲がそれぞれの範囲に追従する。子 transform を持つ場合は Ctrl+F に子も含まれる。
21. `ShapeCentered` で形状の移動・軸オフセット・OffsetLine を変えても中心が動かず、`shapeAxisOffset` がオンなら `shapeAxisOffsetLength` で大きさだけが変わる。`shapeAnimationTransformMatrix` の平行移動を加えると中心も動く。
22. `Custom` の箱を形状本体より小さく、次に大きくしても、本体の線を描画・クリック選択できる。カメラを動かして視錐台カリングも確認する。
23. `showBoundsPreview` をオンにして `boundsMode` を３値で切り替え、各モードの最終的な軸平行範囲が template 色で表示される。プレビューの線だけをクリックしても選択されず、表示のオン/オフでフォーカス範囲は変化しない。
24. Custom の調整値を直接編集・接続・キー設定してフレームとプレビューが更新される。Undo/Redo とシーン再読込後にも同じ範囲へ戻る。
25. `shapeLineWidth` を `1` から大きくすると、本体と表示中の OffsetLine が太くなる。カメラのズームとシーン単位の変更では画面上の指定線幅が変わらない。
26. `shapeTransparency` を `0`、中間値、`1` に切り替えると、輪郭線と OffsetLine の透明度が変わる。通常色、選択色、OffsetLine の template 色で確認する。
27. `shapeDrawOnTop` をオンにすると他のシーン形状に隠れた本体の輪郭線・面と OffsetLine が見え、オフに戻すと通常の深度テストに戻る。形状やクリック選択が変わらない。
28. ４つの描画属性を組み合わせ、Undo/Redo とシーン再読込後にも表示が戻る。`showBoundsPreview` の template 色・線幅・選択不可と、F / Ctrl+F のフォーカス範囲は変わらない。
29. shape の Channel Box で５本の区切りが表示され、形状の描画・軸・変形、フォーカスモード、Custom の軸・変形が上記の６区画の順に並ぶ。
30. 調整属性とその X/Y/Z 子属性を Channel Box から編集でき、通常の一括キー操作ではキーが付かない。属性を明示すればキーや入力接続を設定できる。区切りは編集できない。
31. Maya ASCII で保存して再読込した後も、区切りの表示とロック、調整属性の順序と非 keyable 状態が保たれる。
32. `ColorSphere` は赤・緑・青の直交円だけ、`ColorSphereArrow2D/3D` はその円と通常色の矢印、`ColorSphereCrossLine` は同じ円と十字線として表示され、円と十字線の間に橋渡しの線がない。塗りONでは球殻と付属矢印の面が塗られ、軸色の円が維持される。
33. `bdControllerShape` を選択したまま **Show > Selection Highlighting** をオフにすると通常線・面と OffsetLine が実効displayTypeの非選択時と同じ表示になる。Normalの軸色はRGB、Template/Referenceの軸色は上表のHSV値を使う。オンに戻すと従来の選択表示になる。Normalではオフでもクリック選択できる。
34. 複数ビューポートで Selection Highlighting のオン・オフを別々に設定し、それぞれの表示色が独立する。template 色・選択不可の線と、通常線への色オーバーライドも確認する。
35. `Line` が既定軸でX方向へ長さ1の線として表示される。主軸と補助軸をそれぞれ `+Y/+X`、`+Z/+X` とするとY方向・Z方向へ向き、矢印・端形状の配置平面も対応する。各主軸の負方向でもAtEndは主軸の正側へ追従する。
36. `Cube` と `Cylinder` のTapered Fin の斜線が `-1stAxis` 側の高い位置から `+1stAxis` 側の本体上端へ伸び、軸指定・拡縮後も本体とフィンの接点が離れない。
37. 各形状で `shapeFill` を切り替え、Shaded で面と輪郭線、Wireframe で輪郭線、Wireframe on Shaded で両方が表示される。`ColorCornerCube` の小四角はWireframeでも残る。Shaded では面内をクリックして親 `transform` を選択できる。
38. `Triangle`、`Square`、`Circle` を表裏から見て、面の表示と選択を確認する。立体形状では Backface Culling のオン・オフ、円柱・円錐の側面と底面、ピラミッドの底面も確認する。
39. `shapeFillTransparency` を `0`、`0.5`、`1` に変え、輪郭線の `shapeTransparency` と独立して面の透明度が変わる。半透明の Cube・Sphere で前後の面の重なりと描画順を確認する。
40. `shapeFill` がON で `shapeDrawOnTop` を切り替え、面と輪郭線が前面表示される。`shapeFillTransparency` を組み合わせても選択色とクリック選択が期待どおりか確認する。
41. 各 `shapeFill` がON で輪郭線と面の外縁が一致する。Gear の穴、半円の直径側、矢印・Fin の付属面、template 本体面の非選択、ColorSphere 系の軸色の線を確認する。軸指定と非等方スケールを変えても一致し、負スケール時は表裏の表示を確認する。
42. 塗りONの `3D` 系の矢印を斜めから見て、矢印部分が直交する２枚の薄い面として表示される。`SquareArrow4Way3D` と `SquareTemplateArrow4Way3D` は４方向とも確認する。`OctahedronArrow` のStandard Finは 外周の上側で、八面体と重ならない左右２枚の三角面だけが塗られる。
43. `ColorCube` の正側3面にRGBの四角い枠、負側の角に通常色の3辺が表示される。共有辺の色の競合がなく、軸指定・回転・非等方スケールでも色が部位に追従する。塗りONは通常色のCube面と、内側へ縮めたRGB枠が表示される。
44. `ColorCornerCube` の正側の角に一辺0.2の小四角3枚が表示され、Wireframeでも残る。通常色の線が小四角の境界に重ならず、小四角の面内をクリックして選択できる。塗りONでは本体面と小四角の間に隙間や同一面の二重描画がない。
45. `ColorCornerCube` の `shapeTransparency` と `shapeFillTransparency` を別々に変え、小四角と本体面の透明度が独立して変わる。Selection Highlighting、Draw On Top、軸指定、負スケール、animation matrix、Undo/Redo、シーン再読込でも維持される。
46. 4種類のCrossLineが名前どおりの平面・軸を使い、軸指定の変更に追従する。各ArrowAtEndsの先端は元の端点に一致し、斜辺0.1・開き角60°で底辺の輪郭線がない。
47. `SemicircleArrowAtEnds*` の両端で、矢印が接線に沿って外向きになる。
48. 通常の5種類の `ArrowAtEnds` は塗りONで矢印部分だけを塗り、半円の内側を塗らない。Shadedで三角面内を選択でき、WireframeではV字の輪郭だけが残る。Selection Highlighting、透明度、Draw On Top、軸指定、負スケール、animation matrix、Undo/Redo、シーン再読込も確認する。
49. shape自身・親transform・上位DAG・Display LayerそれぞれでNormal/Template/Referenceを指定し、Selection Highlightingがオフなら選択前後の線色・面表示・軸色が一致する。ColorCornerCubeの小四角、ColorCrossLine3AxisとColorSphereの軸色線も確認する。
50. 5系列の `WideArrowAtEnds` は塗りON/OFFとも、斜辺0.1・開き角60°・先端位置を維持し、幅0.05の帯が矢印の付け根につながる。Wireframeでは閉じた外周のみを表示し、塗りでは帯と矢印の内側全体を塗る。
51. 3種類の `CrossLine*WideArrowAtEnds` の中央に内部線がなく、半透明でも面の二重描画による色の濃い部分がない。`SemicircleWideArrowAtEnds` は半径0.475–0.525の帯と矢印だけを塗り、中央の空間を残す。透明度、Template/Reference、選択、負スケール、軸指定、animation matrixも確認する。
52. `CrossLine3AxisEnd*` と `ColorCrossLine3AxisEnd*` の各5系列・塗りON/OFFで、6端の形状がサイズ0.1で配置され、軸線が手前の表面で止まる。Pyramid/Coneの先端は6方向とも外向きで原点から0.5、底面は0.4となる。
53. `ColorCrossLine3AxisEnd*` は正方向の軸線だけRGB、負方向の軸線と端形状は通常色となる。塗り面に軸色が付かず、Wireframeでは面が省略される。面内の選択、透明度、Template/Reference、Selection Highlighting、Draw On Top、軸指定、負スケール、animation matrix、Undo/Redo、シーン再読込も確認する。
54. `shapeSize` の次に区切り・`shapePartOffset`・`shapePartOffsetAngle`・`shapePartFinHeight`・`shapePartSize`・`shapePartLengthScale`・`shapePartWidthScale`・区切り・`boundsMode` が並ぶ。10種類の端形状でピボット±0.5、長手方向・横2軸の伸縮、接続線の追従、原点越えでの線の省略を確認する。全106形状のFinは塗りON/OFFとも専用Heightで高さを調整し、Offset・Lengthから独立する。Height 0でFinのみ消え、ArrowのTapered Finの高さ比率と本体に追従する付け根を保つ。
55. 部品の変形でも輪郭と塗り面が一致し、0スケールでは塗り面を省略、負スケールでも面と選択が正しく表示される。形状全体の変形、3種類のBounds、単位変更、接続・アニメーション、Undo/Redo、シーン再読込、Color版の色分けも確認する。
56. 付属Arrow3DをOffsetで移動しても、元の付け根へ伸びる中央線がない。直交する三角面の底辺は移動後の付け根にあり、面や輪郭が本体へ不要に延長されない。
57. `OctahedronArrow*` の既定の本体がOctahedronと同じ±0.5の八面体になる。Offset・Lengthで先端だけが動き、中央断面から先端までの辺が直線になる。Lengthは中央断面を基準とし、1で先端+0.5、2で+1.0になる。Width・Sizeでは中央断面とそれを共有する反対側の面も変わり、後端は固定される。Finの付け根も追従する。
58. Semicircle系列のAngleを-90°・-30°・0°・30°・90°に変え、円弧が0°・120°・180°・240°・360°になる。Semicircleと付属Arrow2D/3Dの本体塗りは中心から端点までの扇形を塗り、中心への輪郭線は増えない。ArrowAtEndsの向きとOffsetは移動後の接線に沿い、Wide版の頭部は斜辺と底辺の形を保ったまま一定幅の直線部で帯へ接続する。Lengthを3–5へ伸ばしても頭部が離れない。Size・Length・Widthとの併用、0°・360°での頭部の重なり、塗り面の範囲、負スケール、Bounds、キー設定、接続、Undo/Redo、保存・再読込も確認する。

59. Color系12種類では、shape1stAxis/2ndAxis・shapeRotate・shapeAxisRotateを変えても向きが変わらず、shapeScale・shapeAxisScale・shapeSize・shapeRootSizeの負値が絶対値として適用される。移動・正スケール・部品変形、Shape / ShapeCentered BoundsとOffsetLineが追従する。値・接続・キーを保持したまま通常形状へ切り替えると元の変形が作用し、Undo/Redo・保存・再読込でも維持される。Custom Boundsは独立した変形を保ち、入力行列と親transformの回転・シアー・反転はそのまま反映される。

60. LineとSemicircleの片側端点矢印4種類で、代表軸の正側または主軸の正回転側、反対端の固定、Wide版の平らな端を確認する。Offset・Angle・Size・Length・Widthを併用しても、通常版は頭部だけ、Wide版は帯を含めて塗る。Semicircleの新AtEndが旧AtStartと一致し、全端版が変わらないことも確認する。
61. CrossLine1st2nd/1st3rd/2nd3rdの片側端点矢印6種類で、名前の先頭にある軸の正側だけに矢印が付き、Offsetでも残り3端が固定される。Wide版の3端は平らに閉じ、中央に内部線や面の重複がない。Size・Length・Widthの負値・ゼロ値、軸指定・全体変形・Bounds・接続・Undo/Redo・シーン再読込も確認する。
62. DiamondはSquare各辺の中点を結び、幅・高さが1となる。Square系列の後に並び、塗りONでは内側全体を塗る。Lineと2軸CrossLine3種のSquare/Diamond/Circle/Triangle各端形状では、AtEndが代表軸の正側だけ、AtEndsが全端に小形状を持つことを確認する。配置平面・0.1の寸法・外向きのTriangle・接続線の停止位置・小形状のない端の±0.5維持・部品の負値とゼロ値・重なる塗り面・軸指定・全体変形・Bounds・接続・Undo/Redo・シーン再読込も確認する。

63. `shapeFill` が `shapeTransparency` と `shapeFillTransparency` の間に並び、既定OFFで非keyable・Channel Box表示となる。106形状にFilled付きのenum名がなく、ON/OFFで従来の通常版・Filled版と同じ塗り分け・選択・境界範囲になる。純粋な線形状の見た目とColorCornerCubeの軸色の小四角を維持し、透明度の値保持、接続、キー設定、Undo/Redo、保存・再読込を確認する。
64. `shape` の次に `shapeFin` / `shapeFinType` が並び、106形状へ2種類のFinを追加できる。OFFとHeight 0で本体へ戻り、Type・Heightの値を保持する。旧8種類のFinの外形と面積、本体だけの配置基準、平面形状の向き、Color系の通常色、付属矢印との塗り面の重なり、接続・キー・Undo/Redo・保存・Boundsを確認する。
65. 平面形状のFinが本体へ直角に立ち、Semicircleは基準幅0..+0.5・Widthピボット+0.25となる。ArrowのStandardはくぼみから先端までの矩形、Taperedは従来Standardの外形となり、根元を閉じる線を追加しない。TriangleArrow3Dが一覧にないこと、端形状の変形後の内部にFinの線・面が残らないことを確認する。

実際のViewport 2.0を必要とする画像比較テストは
`tests/maya/ui/test_controller_shape_viewport.py` にあります。既存作業とは別の
Maya GUIプロセスでpytestから実行します。mayapyのbatch環境では明示的にskipします。
