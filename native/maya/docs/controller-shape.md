# Controller Shape

`bdControllerShape` はリグのコントローラー向けのカスタム DAG shape です。
１つの親 `transform` の下に１つの shape を置き、Viewport 2.0 に線と面を描画します。
本体・追加Part・Finの線を独立したストロークとして描き、不要な橋渡し線を追加しません。
コントローラーとして操作するのは親 `transform` です。

## 作成例

```python
import bd_util as bdu

mod = bdu.ModifierManager()
bd_nodes = bdu.Nodes(modifier_manager=mod)

control, shape = bd_nodes.create.controllerShape(name="hand_ctrl")
shape.shape.set(shape.shape.CIRCLE)
shape.shapePart.set(True)
shape.shapePartShape.set(shape.shapePartShape.ARROW2D)
shape.shapePartType.set(shape.shapePartType.ATAPEX)
shape.shapeRootSize.set(1.5)
shape.shapeSize.set(0.8)
shape.shapeLineWidth.set(2.0)  # 画面上で 2 px の線
shape.shapeLineTransparency.set(0.25)  # 25% 透明
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

本体を `shape` で選び、塗り・小形状・Finを独立した共通オプションで追加します。
オプションがOFF、または本体が対象外でも、設定値や接続を保持します。

| Attribute | Maya の型 | 既定値 | 意味 |
| --- | --- | --- | --- |
| `shapeDrawOnTop` | `bool` | `false` | 本体・Part・Fin・OffsetLineを他のシーン形状に隠れないように描画 |
| `shapeLineWidth` | `float` | `1` | 本体とOffsetLineの画面上の線幅。pixel単位、最小値1 |
| `shapeLineTransparency` | `float` | `0` | 輪郭・OffsetLine・ColorCornerCubeの小四角の透明度。0は不透明、1は完全透明 |
| `shapeFill` | `bool` | `false` | 本体・Part・Finの面を表示。`sfl` |
| `shapeFillTransparency` | `float` | `0.85` | 通常の塗り面の透明度。ColorCornerCubeの小四角には適用しない |
| `shape` | enum | `Cube` (16) | 下表の31種類の本体。`Gear` を一覧の先頭に配置 |
| `shapeWideWidth` | `doubleLinear` | `0.05 cm` | Wide系本体の帯幅。最小値0。`sww` |
| `shapeCircleAngle` | `doubleAngle` | `360°` | Circle・WideCircleの円弧全体の角度。0–360°。`sca` |
| `shapePart` | `bool` | `false` | 対象本体へ小形状を追加。`spt` |
| `shapePartShape` | enum | `Arrow2D` (0) | 小形状の11種類。`spsh` |
| `shapePartType` | enum | `AtEnd` (0) | `AtEnd` (0)、`AtEnds` (1)、`AtApex` (2)。`sptp` |
| `shapePartOffset` | `doubleLinear` | `0 cm` | Partを配置方向へ移動。Arrow・OctahedronArrow本体の先端調整にも使用 |
| `shapePartSize` | `double` | `1` | Partの長さ・太さの共通倍率。`sps` |
| `shapePartLengthScale` | `double` | `1` | Partの長手方向の倍率。Arrow・OctahedronArrow本体の調整にも使用 |
| `shapePartWidthScale` | `double` | `1` | Partの長手方向に直交する2軸の共通倍率。Arrow・OctahedronArrow本体の調整にも使用 |
| `shapeFin` | `bool` | `false` | 全31形状へ通常色のFinを1枚追加。`sfn` |
| `shapeFinType` | enum | `Standard` (0) | `Standard` (0)、`Tapered` (1)。`sfnt` |
| `shapeFinHeight` | `doubleLinear` | `0.5 cm` | Finの張り出す高さ。`shapeFinSize`を掛け、0ならFinのみ省略。`sfnh` |
| `shapeFinSize` | `double` | `1` | Finの高さと幅の共通倍率。`sfns` |
| `shapeFinWidthScale` | `double` | `1` | Finの付け根に沿った幅の倍率。`sfnws` |
| `shapeOffsetLine` | `bool` | `false` | 親transformのローカル原点から、軸オフセットを除いた形状基準位置へ補助線を描画。`sol` |
| `shapeOffsetLineTemplate` | `bool` | `false` | OffsetLineだけをtemplate色・選択不可にする |
| `shape1stAxis` | enum | `+X` (0) | 基準主軸の行先。`+X` (0)、`-X` (1)、`+Y` (2)、`-Y` (3)、`+Z` (4)、`-Z` (5) |
| `shape2ndAxis` | enum | `+Y` (2) | 基準補助軸の行先。選択肢はshape1stAxisと同じ |
| `shapeAxisOffset` | `bool` | `false` | 選択軸方向へ基準形状を固定0.5オフセット |
| `shapeAxisOffsetDirection` | enum | `+1stAxis` (0) | `+1stAxis` (0)、`-1stAxis` (1)、`+2ndAxis` (2)、`-2ndAxis` (3)、`+3rdAxis` (4)、`-3rdAxis` (5) |
| `shapeAxisOffsetLength` | `doubleLinear` | `1 cm` | AxisOffsetがONのとき選択軸に沿って原点基準で伸縮。最小値0 |
| `shapeRootSize` | `double` | `1` | 平行移動を含む全体の一律スケール |
| `shapeTranslate` | `doubleLinear3` | `(0, 0, 0)` | 軸指定の外側で平行移動 |
| `shapeRotate` | `doubleAngle3` | `(0, 0, 0)` | 軸指定の外側でXYZ固定順に回転 |
| `shapeScale` | `double3` | `(1, 1, 1)` | 軸指定の外側、shapeRotateの内側で拡縮 |
| `shapeAxisTranslate` | `doubleLinear3` | `(0, 0, 0)` | 指定軸を基準に平行移動 |
| `shapeAxisRotate` | `doubleAngle3` | `(0, 0, 0)` | 指定軸を基準にXYZ固定順に回転 |
| `shapeAxisScale` | `double3` | `(1, 1, 1)` | 指定軸を基準に、shapeAxisRotateの内側で拡縮 |
| `shapeSize` | `double` | `1` | 組み立てた形状の頂点を一律スケール |
| `shapeAnimationTransformMatrix` | matrix data | 単位行列 | 基準形状完成後、親transformの変換前に適用。Channel Boxには非表示 |
| `boundsMode` | enum | `ShapeCentered` (1) | `Shape` (0)、`ShapeCentered` (1)、`Custom` (2) |
| `showBoundsPreview` | `bool` | `false` | 選択中の最終フォーカス範囲をtemplate色・選択不可で表示 |

### 本体一覧

| 値 | 本体 |
| --- | --- |
| 0 | `Gear` |
| 1 | `Line` |
| 2 | `WideLine` |
| 3 | `CrossLine1st2nd` |
| 4 | `WideCrossLine1st2nd` |
| 5 | `CrossLine1st3rd` |
| 6 | `WideCrossLine1st3rd` |
| 7 | `CrossLine2nd3rd` |
| 8 | `WideCrossLine2nd3rd` |
| 9 | `CrossLine3Axis` |
| 10 | `Triangle` |
| 11 | `Square` |
| 12 | `SquareCrossLine` |
| 13 | `SquareCrossLineTemplate` |
| 14 | `SquareTemplate` |
| 15 | `Diamond` |
| 16 | `Cube` |
| 17 | `Octahedron` |
| 18 | `OctahedronArrow` |
| 19 | `Circle` |
| 20 | `WideCircle` |
| 21 | `Sphere` |
| 22 | `Cylinder` |
| 23 | `Arrow` |
| 24 | `Pyramid` |
| 25 | `Cone` |
| 26 | `ColorCrossLine3Axis` |
| 27 | `ColorCube` |
| 28 | `ColorCornerCube` |
| 29 | `ColorSphere` |
| 30 | `ColorSphereCrossLine` |

Filled・Fin・端形状・付属Arrowの複合名を共通オプションへまとめ、
本体一覧を106種類から31種類へ整理しています。
旧複合名、Semicircle、WideSemicircleの公開enum別名や自動移行はありません。
enum番号も変わるため、旧シーンは本体と各オプションを再指定してください。
属性名も `shapeTransparency` → `shapeLineTransparency`、
`shapePartFinHeight` → `shapeFinHeight`、
`showShapeOffsetLine` → `shapeOffsetLine` へ変更しました。
旧 `shapePartOffsetAngle` は削除し、円弧全体の角度を `shapeCircleAngle` で指定します。

基準形状は各軸おおむね `-0.5..+0.5` を使います。矢印・小形状・FinやWideの帯は
その範囲から張り出すことがあり、形状全体を長さ1へ正規化しません。
Lineは主軸方向の長さ1、2軸CrossLineは名称の2軸、CrossLine3Axisは3軸の線を使います。
既定軸ではそれぞれX、XY/XZ/YZ、XYZです。
Triangle・Square・Diamond・Circleは既定軸でYZ平面にあり、
Triangleの底辺は `Y=-0.37` です。
DiamondはSquare各辺の中点を結び、縦横の対角線が1となります。
Cylinderは側面と両端、Coneは側面と底面、Pyramidは側面と底面を持ちます。
円周は64分割の折れ線、Sphereの面は32経度×16緯度で構成します。

### 小形状の種類と配置

`shapePartShape` は2D・3Dを合わせた一覧で、本体が平面でも立体の小形状を選べます。
Partの線・面は通常色とし、Color系でも小形状へRGBの軸色を付けません。

| 値 | 小形状 | 基準寸法・配置 |
| --- | --- | --- |
| 0 | `Arrow2D` | 平面の開いた山形。線・円弧端は斜辺0.1、開き角60°、底辺幅0.1、深さ約0.08660254 |
| 1 | `Arrow3D` | Arrow2Dに直交する薄い面を加えた矢印。閉じた立体ではない |
| 2 | `Triangle` | 底辺幅・高さ0.1。先端を端点、底辺を内側0.1に配置 |
| 3 | `Square` | 一辺0.1。中心を端点に配置 |
| 4 | `Diamond` | 縦横の対角線0.1。中心を端点に配置 |
| 5 | `Circle` | 直径0.1、円周64分割。中心を端点に配置 |
| 6 | `Cube` | 一辺0.1。中心を端点に配置 |
| 7 | `Octahedron` | 向かい合う頂点間0.1。中心を端点に配置 |
| 8 | `Sphere` | 直径0.1。中心を端点に配置 |
| 9 | `Pyramid` | 底辺・高さ0.1。先端を端点、底面を内側0.1に配置 |
| 10 | `Cone` | 底面直径・高さ0.1。先端を端点、底面を内側0.1に配置 |

Square・Cube・Circle・Sphereなど本体表面から突出する付属Arrowは、
従来の比率を維持して基準深さ0.125を使います。
SquareのAtEndsでは主方向のArrowを他の3方向の2倍とします。
Square・Cube・Sphereの表面とAtApexへ付けるTriangle・Pyramid・Coneは、
底面を本体表面に置き、先端を外側へ0.1突出させます。
線・円弧端では表の先端位置を維持します。
Arrowの底辺の線は追加せず、3D矢印をOffsetで離しても元の付け根へ戻る中央線を描きません。
長手方向が直線の小形状と、円弧端の小形状で同じ変形属性を使えます。

| `shapePartType` | 配置 |
| --- | --- |
| `AtEnd` (0) | 本体の代表となる1端。Line・1stから始まるCrossLine・3軸CrossLineは+1st、2nd3rdは+2nd |
| `AtEnds` (1) | Lineは両端、2軸CrossLineは4端、3軸CrossLine・Cube・Sphere系は6端、Square系は4方向、Circle系は円弧両端 |
| `AtApex` (2) | Circle・WideCircleの円弧上部。その他の対象本体ではAtEndとして扱う |

Squareの代表方向は+2nd、Cube・Sphere系は+1stです。
CircleのAtEndは主軸の正回転方向へ円弧をたどった終点です。
角度180°、既定軸では+3rd側で、接線に沿って-2ndを向きます。
AtEndsでは両端の外向き接線を使います。360°で始終端が一致しても、
向きが異なる矢印は両方を維持し、同一になる小形状だけ二重描画を避けます。
AtApexは+2nd側から外向きへ突出する従来の付属Arrowを再現します。
配置は軸指定・全体回転前の基準座標に対して定義し、以後の全体変形へ追従します。

対象外は `Gear`、`Triangle`、`Diamond`、`Octahedron`、`OctahedronArrow`、
`Cylinder`、`Arrow`、`Pyramid`、`Cone`、`ColorCube`、`ColorCornerCube` の11種類です。
これらではPartをONにしても本体を変更せず、Partの値を保持します。
Finは対象外形状にも追加できます。

### Partの変形と接合

長手方向のピボットは元の端点です。直線・立体では元の `±0.5`、
円弧端では角度調整後の端点、AtApexでは円弧上部を使います。
小形状の中心または先端を固定して拡縮し、Offsetは伸縮後に配置方向へ加算します。

```text
length = shapePartSize * shapePartLengthScale
width = shapePartSize * shapePartWidthScale
p' = endpoint + along * (localLength * length + shapePartOffset)
              + side * localWidth * width + up * localDepth * width
```

Cube・Octahedron・Sphere・Square・Diamond・Circleは中心、
Triangle・Pyramid・Coneと線・円弧端のArrowは先端がピボットです。
本体表面から突出する付属Arrowは元の付け根を基準にします。
表面から突出するTriangle・Pyramid・Coneも底面を基準にします。
Sizeを変えてもOffsetの距離自体は変わりません。
Partの変形後に、shapeSize・軸指定・回転・animation matrixなどの全体変形を適用します。

接続線は変形後の小形状の手前で止め、内部へ通しません。
CrossLineでは手前の表面が原点へ達する・越える場合、反対側へ線を延長しません。
Lineでは反対端を固定し、原点を越えて移動したPartへもその端から接続します。
Finと本体の線・塗りも、変形後の小形状内部を差し引きます。
通常色・Color版・塗りのON/OFFで同じ接合位置を使います。
重なる面の二重描画と内部線を避け、半透明でも境界を揃えます。
倍率は負値・ゼロ値にも対応し、面積0の塗り面は省略します。

Arrow・OctahedronArrowは本体自身が矢印のため、PartがOFFでも
Offset・Size・Length・Widthの調整を適用します。
OctahedronArrowの既定形状はOctahedronと同じ±0.5の八面体です。
Offset・Lengthでは先端だけを動かし、中央断面から先端までを直線で結びます。
Lengthは中央断面基準で、1なら先端+0.5、2なら+1.0です。
Width・Sizeは中央断面と、それを共有する反対側の面も変え、後端を固定します。
これらの本体へ付けたFinの付け根は本体変形へ追従します。

### CircleとWide

CircleとWideCircleの角度はPartのON/OFFから独立しています。
`shapeCircleAngle` は円弧全体の角度で、既定360°なら円、180°なら従来の半円です。
上側の中心方向+2ndを保ち、両端が対称に開閉します。
0°では円弧・Part・Finを省略し、360°では継ぎ目に不要な線を追加しません。
接続入力も0–360°に制限します。Sphereを構成する円や小形状Circleには適用しません。
円周64分割相当の密度を使い、両端と各軸方向の点を含めます。

塗りONのCircleは中心と両端を結ぶ扇形、360°では円板を描きます。
中心へ向かう境界の輪郭線は追加しません。
180°未満の扇形では塗りの中心点もShape / ShapeCenteredの範囲へ含みます。
WideCircleは帯状の円弧、360°では環を塗り、中央の空間を残します。

WideLine、WideCrossLineの3平面、WideCircleは帯を持つ本体です。
帯幅は `shapeWideWidth` だけで調整し、PartのSize・Widthから独立します。
既定の直線は中心から±0.025、円弧は中心半径0.5に対して内半径0.475・外半径0.525です。
帯が円弧の中心へ達すると内半径は0になります。
WideCrossLineは中央を一つの十字として描き、内部線と面の重複を作りません。
円弧端のPartを接線方向へOffsetしても頭部の形を保ち、帯から一定幅でつなぎます。
Wideの小形状のない端は平らに閉じます。
帯幅0では線だけを残し、本体の塗り面を省略します。

### Squareの通常線とTemplate線

SquareCrossLineはSquareへ通常線の十字を、SquareCrossLineTemplateはtemplate線の十字を追加します。
いずれも本体面は通常色で選択可能です。
SquareTemplateは四隅側をtemplate線、各辺中央の幅0.3を選択可能な通常線にした四角です。
PartがOFFでも通常線を残し、矢印で突出していた箇所を直線で結びます。
SquareTemplateの本体面はtemplate色・選択不可、追加Partの線・面は通常色・選択可能です。
PartをArrow2D / Arrow3D、AtEndsにすると従来の4方向矢印の構成を表せます。

### Fin

全31形状へ、Partとは独立した通常色のFinを1枚追加できます。
Standardは矩形など本体に合った形、Taperedは幅の負側が高く正側へ低くなる形です。
Finの基準は矢印や小形状を除いた本体断面です。小形状ごとにFinを追加しません。

| 本体 | Finの幅 | Finの張り出し |
| --- | --- | --- |
| CrossLine1st2nd・WideCrossLine1st2nd | 1st | +3rd |
| CrossLine1st3rd・WideCrossLine1st3rd | 1st | +2nd |
| Gear / Triangle / Square系 / Diamond / Circle系 / CrossLine2nd3rd系 | 2nd | +1st |
| Line系 / CrossLine3Axis系 / その他の立体 | 1st | +2nd |

Finは本体中心軸または断面へ接続し、根元を閉じる線を追加しません。
ArrowのStandardはくぼみ1st=-0.25から先端+0.5までの矩形、
Taperedは従来Standardの傾斜した外形です。
Cube・CylinderのTaperedは負側の高い位置から正側の本体上端へ接続します。
TriangleにTapered Finを追加すると旧TriangleArrow3D相当の形になります。

```text
height = shapeFinHeight * shapeFinSize
width = shapeFinWidthScale * shapeFinSize
```

PartのSize・Width・Offset・LengthをFinの寸法へ掛けません。
Arrow・OctahedronArrow本体に追従する付け根だけは、本体側の変形を反映します。
高さ0またはFin OFFではFinの線・面だけを省略し、本体・Partを残します。
負の高さは自由頂点の張り出す向きを反転し、付け根を移し替えません。
Color系でもFinは通常色で、軸・回転の制約は本体と共通です。
同じ平面の本体・Partと重なる塗りを差し引き、小形状内部のFinの線・面を除きます。

Circle系のFinは角度に合わせて基準幅とピボットを連続的に変えます。
180°では2nd=0..+0.5・ピボット+0.25、360°では-0.5..+0.5・ピボット0です。
Fin専用Widthはそのピボットで拡縮し、円弧の角度・Partの変形とは別に調整できます。

### 塗りとColor

塗りは共通のshapeFillで切り替え、OFFでも透明度やPart・Finの設定を保持します。
純粋なLine・CrossLineの線は塗らず、追加Part・Finに面があれば塗ります。
Gearは外周と内円の間を塗り、穴を残します。
3D矢印は直交する薄い三角面、Pyramid・Coneなどの立体は底面を含む面を持ちます。
面はViewport 2.0用で、NURBSのCV・UV・材質・レンダリング用サーフェスは生成しません。

ColorCrossLine3Axisは正方向の線をRGB、負方向を通常色にします。
ColorSphereはX=赤・Y=緑・Z=青の直交円で、ColorSphereCrossLineは同じ円へ
ColorCrossLine3Axisの十字を加えます。円と十字の間に橋渡しの線を追加しません。
塗りONでは球殻を通常色で塗り、軸色の円を保ちます。
Part・Finの線と面は通常色です。

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
本体面には `shapeFillTransparency`、小四角には `shapeLineTransparency` を適用します。
塗りONでは、本体面は既定の透明度85%、小四角は不透明です。これら2種類にもFinオプションを適用できます。
ColorCornerCubeの小四角は `shapeFill` がOFFでも表示・選択でき、Wireframeでも残ります。

Color系5種類は、シェイプ編集を適用する段階で軸色と親transformのローカルXYZの対応を保ちます。
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

Channel Boxの表示順は次の14区画です。区切りは `_` から `_____________` までの
13本の表示専用1値enumで、値は `-----------------------------------` です。
非keyable・非接続・非保存・ロック済みとし、各区画の間へ1本ずつ置きます。

1. `shapeDrawOnTop`
2. `shapeLineWidth`、`shapeLineTransparency`
3. `shapeFill`、`shapeFillTransparency`
4. `shape`
5. `shapeWideWidth`
6. `shapeCircleAngle`
7. `shapePart`、`shapePartShape`、`shapePartType`、`shapePartOffset`、`shapePartSize`、`shapePartLengthScale`、`shapePartWidthScale`
8. `shapeFin`、`shapeFinType`、`shapeFinHeight`、`shapeFinSize`、`shapeFinWidthScale`
9. `shapeOffsetLine`、`shapeOffsetLineTemplate`
10. `shape1stAxis`、`shape2ndAxis`、`shapeAxisOffset`、`shapeAxisOffsetDirection`、`shapeAxisOffsetLength`
11. `shapeRootSize`、外側の移動・回転・スケール、内側の移動・回転・スケール、`shapeSize`
12. `boundsMode`、`showBoundsPreview`
13. `customBounds1stAxis`、`customBounds2ndAxis`、`customBoundsAxisOffset`、`customBoundsAxisOffsetDirection`、`customBoundsAxisOffsetLength`
14. `customBoundsRootSize`、外側の移動・回転・スケール、内側の移動・回転・スケール、`customBoundsSize`

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

`shapeLineWidth`、`shapeLineTransparency`、`shapeFillTransparency`、
`shapeDrawOnTop` は Viewport 2.0 の描画だけを調整します。線幅は画面上の
pixel 指定で、シーン単位や `shapeSize` とは独立しています。
`shapeLineTransparency` は輪郭線と OffsetLine、`shapeFillTransparency` は
`shapeFill` がON の本体面に適用します。`ColorCornerCube` の小四角だけは
`shapeLineTransparency` に従います。面と輪郭線は選択状態に応じた色を使います。
`shapeDrawOnTop` は輪郭線・面・OffsetLine を他のシーン形状より前に描きます。
面を含む形状では、Shaded は面と輪郭線、Wireframe は輪郭線、
Wireframe on Shaded は面と輪郭線を表示します。面内のクリックも選択対象です。
`ColorCornerCube` の小四角はWireframeでも表示・選択できます。
`showBoundsPreview` の確認用の箱は従来の template 色・線幅・選択不可を維持し、
これらの属性の影響を受けません。描画属性の変更はフォーカス範囲を変えず、
本体と OffsetLine のクリック選択の可否も変更しません。

`shapeFill` は面の生成と選択判定、形状キャッシュ、描画範囲を更新します。
Circleの扇形の中心やSphereの面の頂点が加わる場合はShape / ShapeCenteredの範囲も変わります。
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
CircleへAtApexのPartを追加した非対称な形状でも、行列適用前の範囲の中心は原点です。

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
CircleへArrow2DをAtApexで追加した既定形状は、YZ面の半径0.5の円と、
`(y, z)=(0.495096189432334, -0.075)` → `(0.625, 0)` →
`(0.495096189432334, +0.075)` の独立した山形の線からなります。
Arrow3Dでは主平面と直交する薄い矢印面も加えます。

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
そのためCircleと追加Arrowや、色や選択可否の異なる部分を、橋渡しの線なしで
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
同じ順序の `kPresetInfo` で、各選択肢を内部の輪郭番号へ対応付けます。
塗り、Partの種類・配置、Finの種類は別の設定で保持します。
Partの対象と配置点・小形状の作成・接合は
[BdControllerShapeOptions.inc](../plugins/bdUtilNodes/src/nodes/BdControllerShapeOptions.inc) で共通化し、
公開enumへ組み合わせごとの項目を追加しません。
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
14区画の表示順になります。新しい調整属性は該当区画へ登録し、非 keyable・
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
CircleのAtApexの矢印が元の `+Y` を向くのは意図した仕様で、主軸が形状の
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
透明度は線・小四角に `shapeLineTransparency`、通常の塗り面に
`shapeFillTransparency` を適用します。形状内のtemplate部分と
`shapeOffsetLineTemplate` は、DAG全体のdisplayTypeとは独立した指定です。
選択そのものと、template色・選択不可の部分には影響しません。

ビューポートの描画とクリック選択は `mayapy` のヘッドレステストだけでは
確認できません。Maya 2025 / 2026 / 2027 の GUI で次を確認してください。

1. CircleへArrow2DをAtApexで追加し、円と矢印が独立した輪郭として見え、不要な橋渡しの線がない。
2. 選択解除して本体・Part・Finの通常線と、塗りONの面をクリックし、同じ親transformを選択できる。
3. Show > Plugins > Plugin ShapesをOFFにすると描画・クリック選択を省略し、ONに戻すと再表示される。
4. Show > LocatorsをOFFにして標準locatorが消えても、このshapeは表示される。shape自身のvisibilityでは表示を切り替えられる。
5. shapeと調整値の直接変更、入力接続・キーの再生、Undo/Redoで描画と選択範囲が直後に更新される。
6. Maya ASCIIへ保存・再読込して、本体・Part・Fin・透明度・軸・区切りの順序と値を保持する。
7. shapeTranslateを動かしshapeOffsetLineをONにすると、親のローカル原点から形状基準位置へ補助線が出る。始点と終点が一致すると省略する。
8. shapeOffsetLineTemplateをONにすると補助線だけがtemplate色・選択不可になる。本体の通常線は引き続き選択できる。
9. 軸指定と内側のTRSを変更して本体・Part・Fin・OffsetLine・選択範囲が追従し、無効な軸の組では主軸を保つ。
10. 親transformをアニメーションしても形状が追従し、ローカル形状の調整値は変化しない。
11. CubeのshapeAxisOffsetを6方向へ切り替える。既定サイズでは片面が原点に揃い、shapeSize=2でも固定移動量0.5を維持する。
12. shapeOffsetLineをONにしてAxisOffsetを切り替えても補助線の終点は動かない。AxisOffsetだけをONにしても補助線は出ない。
13. AxisOffsetがONならshapeAxisOffsetLengthは指定軸だけを伸縮し、OFFなら長さ・方向の変更で伸縮しない。距離入力の接続とシーン単位変更も確認する。
14. AxisOffsetがONでshapeAxisTranslateの選択軸成分がある場合、長さの変更をOffsetLineの終点にも反映する。
15. shapeAnimationTransformMatrixへcomposeMatrix出力を接続し、移動・回転・非等方スケール・シアーに本体・Part・Fin・範囲が追従する。
16. 行列の移動で形状基準位置が原点から離れるとOffsetLineが出て、戻すと消える。行列の移動量はshapeRootSizeに掛からない。
17. boundsModeの3値でF / Ctrl+Fの範囲が追従し、Ctrl+Fでは子transformも含まれる。
18. ShapeCenteredは形状の移動・AxisOffset・OffsetLineによる中心の変化を除き、AxisOffsetLengthの大きさと入力行列の移動を反映する。
19. Customの箱を本体より小さく・大きくしても本体を描画・クリック選択できる。カメラを動かしてカリングも確認する。
20. showBoundsPreviewは各モードの最終範囲をtemplate色・選択不可で表示し、ON/OFFでフォーカス範囲を変えない。
21. Custom属性の直接編集・接続・キー・Undo/Redo・保存・再読込で範囲を更新し、Part・Fin・Circleの変更から独立する。
22. shapeLineWidthを大きくすると本体・Part・Fin・OffsetLineが画面上で太くなり、ズームやシーン単位によらず指定pixel幅を保つ。
23. shapeLineTransparencyの0・中間値・1を通常色・選択色・template色・軸色で確認し、shapeFillTransparencyとは独立して変わる。
24. shapeDrawOnTopのON/OFFで隠れた線・面を表示し、形状・クリック選択・Boundsを変えない。透明度・選択色との併用も確認する。
25. Channel Boxで13本の区切りと14区画の順序を確認し、非keyableの調整値・XYZ子属性を編集でき、明示キー・入力接続に対応する。区切りは編集・接続できない。
26. shapeの31項目、PartShapeの11項目、PartTypeの3項目を確認し、旧複合名・Semicircle・旧属性の別名がない。
27. 全本体でshapeFillを切り替え、Shadedでは面・輪郭、Wireframeでは輪郭、Wireframe on Shadedでは両方を表示する。ColorCornerCubeの小四角は常に残る。
28. Triangle・Square・Circleの表裏、立体のBackface Culling、Cylinder/Cone/Pyramidの底面、Gearの穴を確認する。
29. 各塗り面の外縁が輪郭と一致し、非等方・負スケールでも選択できる。半透明の前後面の描画順も確認する。
30. shapePartのON/OFFで小形状だけが切り替わり、種類・配置・Offset・Size・Length・Widthの値を保持する。
31. Part対象外11本体ではONでも本体が変わらず、対応本体へ切り替えると保持していたPart設定が作用する。
32. Line・CrossLine各種でAtEndが代表軸の正側、AtEndsが全端となり、小形状のない端は元の±0.5に残る。
33. Square系でAtEndが+2nd、AtEndsが4方向となり、Arrowは主方向と他の3方向の2:1の比率を維持する。
34. Cube・Sphere・ColorSphere系でAtEndが+1st、AtEndsが6端となる。2D本体へ3DのPart、3D本体へ平面のPartも追加できる。
35. Partの基準寸法0.1、外向きTriangle/Pyramid/Cone、端点ピボット、Offsetの加算距離、長手方向と横2軸の倍率を確認する。
36. 変形したPartの手前で接続線が止まり、原点越えでは反対側へ伸びない。小形状内へ本体・Finの線や塗り面が残らない。
37. PartとFinの倍率に負値・ゼロを使い、面積0の面を省略し、輪郭と塗り・選択・Shape / ShapeCenteredの範囲が揃う。
38. Arrow3DのOffsetで元の付け根へ戻る中央線が出ず、直交する薄い面の形を保つ。閉じたPyramid/Coneの面と区別できる。
39. ArrowとOctahedronArrowはPart OFFでも既存の本体調整を適用する。OctahedronArrowは既定でOctahedronと同形、Offset・Lengthで先端だけを直線的に伸ばし、Width・Sizeで共有断面と後側の面も変える。
40. Circle・WideCircleのshapeCircleAngleを0・120・180・240・360°へ変更し、上側中心を保って両端が対称に動く。Part OFFでも作用し、Sphere・小形状Circleには作用しない。
41. Circleの塗りが中心からの扇形、WideCircleの塗りが帯となり、0°で円弧の線・面を省略、360°で継ぎ目の不要線を作らない。
42. CircleのAtEndが正回転側の終点、AtEndsが両端で接線へ向く。AtApexは円弧上部、他本体ではAtEnd相当となる。360°で同位置のPartを二重描画しない。
43. WideLine・WideCrossLine3種・WideCircleでshapeWideWidthを調整し、PartのSize・Widthを変えても帯幅を保つ。十字中央・頭部との接合・半透明面の重複を確認する。
44. WideCircleのPartをOffset・Lengthで移動しても頭部の形と帯の幅を保ち、帯と頭部が離れない。Partのない円弧端は平らに閉じる。
45. SquareCrossLineの通常十字、SquareCrossLineTemplateのtemplate十字、SquareTemplateの四隅template線・中央通常線・template面を確認する。Part OFFでも通常線を残す。
46. SquareTemplateのPartは線・面とも通常色で選択でき、本体のtemplate線・面だけでは選択できない。Arrow2D/3D・AtEndsで4方向を確認する。
47. 全31本体のFinを2種類・塗りON/OFFで確認する。OFF・高さ0ではFinだけが消え、設定値を保持する。
48. Finの高さ・幅はshapeFinSizeとshapeFinWidthScaleで調整し、PartのSize・Widthから独立する。Arrow・OctahedronArrowの付け根だけは本体変形へ追従する。
49. 平面本体のFinが直角に立ち、根元を閉じる線がない。Circle角度180°では半幅・ピボット+0.25、360°では全幅・ピボット0で、その間も連続する。
50. ArrowのStandard Finはくぼみから先端までの矩形、Taperedは傾斜した外形となる。Cube・CylinderのTaperedとOctahedronArrowの面の重複も確認する。
51. ColorCrossLine3AxisとColorSphere系の軸色を保ち、追加Part・Finは通常色となる。ColorSphereCrossLineの円と十字に橋渡し線がない。
52. ColorCubeの正側RGB枠・負側通常線、ColorCornerCubeの小四角・通常面の境界と独立した透明度を確認する。
53. Color系5本体は軸指定・shapeRotate・shapeAxisRotateで向きが変わらず、shapeScale・shapeAxisScale・shapeSize・shapeRootSizeの負値は絶対値になる。通常本体へ戻すと保持値が作用する。
54. Color系のCustom Boundsは独立した変形を保ち、入力行列と親transformの回転・シアー・反転はそのまま反映する。
55. shape・親transform・上位DAG・Display LayerでNormal/Template/Referenceを切り替え、Selection Highlighting OFFなら選択前後の線色・面表示・軸色が一致する。
56. 複数ViewportでSelection Highlightingを別々に設定し、選択色・軸色・templateの選択不可と通常線のオーバーライド色をそれぞれ確認する。

実際のViewport 2.0を必要とする画像比較テストは
`tests/maya/ui/test_controller_shape_viewport.py` にあります。既存作業とは別の
Maya GUIプロセスでpytestから実行します。mayapyのbatch環境では明示的にskipします。
