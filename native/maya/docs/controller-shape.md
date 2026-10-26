# Controller Shape

`bdControllerShape` はリグのコントローラー向けのカスタム DAG shape です。
１つの親 `transform` の下に１つの shape を置き、Viewport 2.0 に線と面を描画します。
本体・追加Part・Finの線を独立したストロークとして描き、不要な橋渡し線を追加しません。
コントローラーとして操作するのは親 `transform` です。

現在は、既存シーンへの保存・運用を始めていない個人開発中のノードです。
この開発段階では既存シーンとの互換性を考慮せず、設計と使いやすさを優先して
名称・enum 番号・属性・形状仕様を変更します。互換スクリプト、旧 enum へ戻すための
手順、移行用ドキュメントは作成せず、この仕様書とサンプルを現行仕様へ揃えます。
一度公開した `MTypeId` は変更・再利用しません。

## 今回の開発範囲

2026-10-26時点で、本体40種類、Part11種類、Circle系・CrossCircle系の円周変形と接合、
Fin、表示・選択・フォーカス範囲・キャッシュを本仕様書の範囲とします。
Circle系の6種類のPartは円周変形、残る5種類の立体Partは寸法を保つ角度補正を使い、
AtApexは従来の配置を使います。Circle系・CrossCircle系6本体ではFinを生成しません。

Circle系・CrossCircle系6本体を除き、通常の2D本体・Lineの帯・代表方向のPart矢印の主面を
主軸と第3軸の平面へ揃え、FinとArrow3Dの追加面を補助軸側へ立ち上げます。
2D本体には主軸と補助軸を入れ替えた `Swapped` を別の本体名で用意します。
Circle系の向きは維持し、今回の共通規約へ合わせるかは保留します。
多数配置時の再生性能測定は今後の候補とし、実際の利用で負荷が確認できた際に検討します。

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
軸指定の既定値は主軸 `+X`・補助軸 `+Y` で、通常の2D本体はXZ面、
`Swapped` とCircle系の基準円はYZ面に作られます。
作成例のCircleをXY面に向ける場合は `shape.shape1stAxis.set(4)`（`+Z`）を指定します。

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
| `shape` | enum | `Cube` (21) | 下表の40種類の本体。`Gear` を一覧の先頭に配置 |
| `shapeWideWidth` | `doubleLinear` | `0.05 cm` | Wide系本体の帯幅。最小値0。`sww` |
| `shapeCircleAngle` | `doubleAngle` | `360°` | Circle系・CrossCircle系6種類の円弧全体の角度。0–360°。`sca` |
| `shapePart` | `bool` | `false` | 対象本体へ小形状を追加。`spt` |
| `shapePartShape` | enum | `Arrow2D` (0) | 小形状の11種類。`spsh` |
| `shapePartType` | enum | `AtEnd` (0) | `AtEnd` (0)、`AtEnds` (1)、`AtApex` (2)。`sptp` |
| `shapePartOffset` | `doubleLinear` | `0 cm` | Partを配置方向へ移動。Circle系・CrossCircle系のAtEnd・AtEndsで円周へ曲げる6種類では無視し、値と接続は保持。Arrow・OctahedronArrow本体の先端調整にも使用 |
| `shapePartSize` | `double` | `1` | Partの長さ・太さの共通倍率。`sps` |
| `shapePartLengthScale` | `double` | `1` | Partの長手方向の倍率。Circle系・CrossCircle系の円周へ曲げるPartでは半径0.5の中心円弧長の倍率。Arrow・OctahedronArrow本体の調整にも使用 |
| `shapePartWidthScale` | `double` | `1` | Partの長手方向に直交する2軸の共通倍率。円周変形時はRadialの半径方向幅、Axialの円軸方向幅とArrow3Dの高さへ作用。Arrow・OctahedronArrow本体の調整にも使用 |
| `shapeFin` | `bool` | `false` | Circle系・CrossCircle系6種類を除く34形状へ通常色のFinを1枚追加。対象外では値と接続を保持して無視。`sfn` |
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

`Gear` / `GearSwapped` の後に通常の2D本体をまとめ、その後に対応するSwappedを
同じ順序で並べます。続けて `CrossLine3Axis` と `Cube` 以降の本体を並べます。

| 値 | 本体 |
| --- | --- |
| 0 | `Gear` |
| 1 | `GearSwapped` |
| 2 | `Line` |
| 3 | `WideLine` |
| 4 | `CrossLine` |
| 5 | `WideCrossLine` |
| 6 | `Triangle` |
| 7 | `Square` |
| 8 | `SquareCrossLine` |
| 9 | `SquareCrossLineTemplate` |
| 10 | `SquareTemplate` |
| 11 | `Diamond` |
| 12 | `CrossLineSwapped` |
| 13 | `WideCrossLineSwapped` |
| 14 | `TriangleSwapped` |
| 15 | `SquareSwapped` |
| 16 | `SquareCrossLineSwapped` |
| 17 | `SquareCrossLineTemplateSwapped` |
| 18 | `SquareTemplateSwapped` |
| 19 | `DiamondSwapped` |
| 20 | `CrossLine3Axis` |
| 21 | `Cube` |
| 22 | `Octahedron` |
| 23 | `OctahedronArrow` |
| 24 | `Circle` |
| 25 | `WideCircleRadial` |
| 26 | `WideCircleAxial` |
| 27 | `CrossCircle` |
| 28 | `WideCrossCircleRadial` |
| 29 | `WideCrossCircleAxial` |
| 30 | `Sphere` |
| 31 | `Cylinder` |
| 32 | `Arrow` |
| 33 | `Pyramid` |
| 34 | `Cone` |
| 35 | `ColorCrossLine3Axis` |
| 36 | `ColorCube` |
| 37 | `ColorCornerCube` |
| 38 | `ColorSphere` |
| 39 | `ColorSphereCrossLine` |

基準形状は各軸おおむね `-0.5..+0.5` を使います。矢印・小形状・FinやWideの帯は
その範囲から張り出すことがあり、形状全体を長さ1へ正規化しません。
Lineは主軸方向の長さ1、CrossLineは主軸と第3軸、CrossLineSwappedは補助軸と第3軸、
CrossLine3Axisは3軸の線を使います。既定軸ではそれぞれX、XZ、YZ、XYZです。
WideLineの帯、Gear・Triangle・Square系・Diamondの通常本体は既定軸でXZ平面に置き、
代表方向を+Xとします。Triangleの底辺は `X=-0.37` です。
各 `Swapped` は対応する通常本体の主軸・補助軸を右手系を保って入れ替え、
YZ平面に置きます。代表方向は+Y、TriangleSwappedの底辺は `Y=-0.37` です。
Circle系の基準円はYZ平面に置き、今回の2D本体の共通化から除外します。
DiamondはSquare各辺の中点を結び、縦横の対角線が1となります。

Swappedは通常本体・Part・Finを組み立てて接合した後、
基準座標へ `(x, y, z) → (y, x, -z)` を一括適用します。
主軸と補助軸の交換に合わせて第3軸も反転し、右手系を維持します。
その後に適用する `shape1stAxis` / `shape2ndAxis`、AxisOffset、Axis系TRSの
指定軸の意味や保持値は交換しません。たとえばSwappedでも
`shapeAxisOffsetDirection=+1stAxis` はノードに指定した主軸方向のままです。

Cylinderは側面と両端、Coneは側面と底面、Pyramidは側面と底面を持ちます。
ConeはFillのON/OFFにかかわらず、底円と先端を結ぶ補助線を表示します。小形状のConeも同様です。
CylinderはFillを表示する場合に両端の円だけを残し、円同士を結ぶ補助線を省略します。
Wireframeや非選択のTemplate・Referenceなど、面を表示しない状態では補助線を表示します。
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
Square系のAtEndsでは代表方向のArrowを他の3方向の2倍とします。
Square・Cube・Sphereの表面とAtApexへ付けるTriangle・Pyramid・Coneは、
底面を本体表面に置き、先端を外側へ0.1突出させます。
線・円弧端では表の先端位置を維持します。
Arrowの底辺の線は追加せず、3D矢印をOffsetで離しても元の付け根へ戻る中央線を描きません。
長手方向が直線の小形状と、円弧端の小形状で同じ変形属性を使えます。

| `shapePartType` | 配置 |
| --- | --- |
| `AtEnd` (0) | 本体の代表となる1端。Line・通常CrossLine・3軸CrossLine・通常Square系・Cube・Sphere系は+1st、SwappedのCrossLine・Square系は+2nd。CrossCircle系は基準円の1端 |
| `AtEnds` (1) | Lineは両端、2軸CrossLineは4端、3軸CrossLine・Cube・Sphere系は6端、Square系は4方向、Circle系は円弧両端、CrossCircle系は両円の4端 |
| `AtApex` (2) | Circle系・CrossCircle系6種類の円弧上部。CrossCircle系は基準円の向きで1つ。その他の対象本体ではAtEndとして扱う |

通常Square系の代表方向は+1st、SwappedのSquare系は+2ndです。
AtEndsの各矢印は、それぞれ配置先の端から外向きに進みます。
主軸方向への先端という規約は代表方向を指し、他端を主軸方向へ揃えません。
CircleのAtEndは主軸の正回転方向へ円弧をたどった終点です。
角度180°、既定軸では+3rd側で、-2nd側を向きます。
Circle・WideCircleRadialのAtEnd・AtEndsでは、6種類のPartを同じ平面内で円周へ曲げ、
立体のPartは円弧上の接合位置から先端または中心へ向けて角度を補正します。
WideCircleAxialの円弧端では、6種類のPartを円筒面へ巻き付け、立体のPartは接合条件に応じて向きを補正します。
360°で始終端が一致しても、位置・姿勢・形状が一致するPartだけ二重描画を避けます。
Circle系の360°・AtEndsでは、円周へ曲げるPartの重なる領域をまとめます。
立体のPartは各端に合わせて異なる姿勢になる場合は別々に残し、
中心が共通でも、向きの補正により2つの形状が交差する場合があります。
Circle系のAtApexは+2nd側から外向きへ突出する付属Arrowを使います。
配置は軸指定・全体回転前の基準座標に対して定義し、以後の全体変形へ追従します。

対象外は `Gear`、`GearSwapped`、`Triangle`、`TriangleSwapped`、`Diamond`、
`DiamondSwapped`、`Octahedron`、`OctahedronArrow`、`Cylinder`、`Arrow`、
`Pyramid`、`Cone`、`ColorCube`、`ColorCornerCube` の14種類です。
これらではPartをONにしても本体を変更せず、Partの値を保持します。
残る26本体がPartに対応し、Part対象外の14形状にもFinを追加できます。

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

Circle系・CrossCircle系のAtEnd・AtEndsのArrow2D・Arrow3D・Triangle・Square・Diamond・Circleは、
上式の長手方向を半径0.5の中心円弧長として使い、Offsetを無視します。
Circle・WideCircleRadialとそのCross版は同じ円の平面内で曲げ、
WideCircleAxialとそのCross版は円筒面へ巻き付けます。
立体のPartは中心または先端のOffsetに元の接線方向を使い、
長手方向を円弧との接合位置に合わせて調整します。詳細は「CircleとWide」を参照してください。
Circle・WideCircleRadial・CrossCircle・WideCrossCircleRadialのAtEnd・AtEndsでも、
立体のPartはOffsetに元の接線方向を使って先端または中心を固定し、接合位置へ合わせて
長手方向と幅方向を一緒に回転します。立体の形状・寸法は保ちます。

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

Circle系・CrossCircle系6種類の角度はPartのON/OFFから独立しています。
`shapeCircleAngle` は円弧全体の角度で、既定360°なら円、180°なら従来の半円です。
上側の中心方向+2ndを保ち、両端が対称に開閉します。
0°では円弧・Partを省略し、360°では継ぎ目に不要な線を追加しません。
接続入力も0–360°に制限します。Sphereを構成する円や小形状Circleには適用しません。
円周64分割相当の密度を使い、両端と各軸方向の点を含めます。

塗りONのCircleは中心と両端を結ぶ扇形、360°では円板を描きます。
中心へ向かう境界の輪郭線は追加しません。
180°未満の扇形では塗りの中心点もShape / ShapeCenteredの範囲へ含みます。
WideCircleRadialは同じ平面内で半径方向に幅を持つ円弧です。
塗りは帯状の円弧、360°では環となり、中央の空間を残します。

WideLine、WideCrossLine、WideCrossLineSwapped、WideCircleRadial、WideCircleAxialは帯を持つ本体です。
WideLineとWideCrossLineの帯はXZ面、WideCrossLineSwappedの帯はYZ面に置きます。
帯幅は `shapeWideWidth` だけで調整し、PartのSize・Widthから独立します。
既定の直線は中心から±0.025、WideCircleRadialは中心半径0.5に対して
内半径0.475・外半径0.525です。帯が円弧の中心へ達すると内半径は0になります。
WideCrossLineは中央を一つの十字として描き、内部線と面の重複を作りません。
Offsetが作用する円弧端のPartは、元の接線方向で先端または中心を移動し、
頭部の形を保って円弧・帯との接合位置へ向きを合わせます。
Wideの小形状のない端は平らに閉じます。
帯幅0では線だけを残し、本体の塗り面を省略します。

Circle・WideCircleRadialのAtEnd・AtEndsのArrow2D・Arrow3D・Triangle・Square・Diamond・Circleは、
長手方向を半径0.5の中心円弧上の距離、幅方向を半径方向の距離として、同じ平面内で円周へ曲げます。
`shapePartLengthScale` は中心円弧長、`shapePartWidthScale` は半径方向の幅を調整し、
どちらにも `shapePartSize` を掛けます。幅によって円の中心を越える部分は半径0へ制限します。
基準となる長さ・幅はWideCircleAxialと共通です。
`shapeCircleAngle` で変わる円弧端点へ追従し、`shapePartOffset` は無視します。
Offsetの値・接続は保持し、立体PartやAtApexへ切り替えると再び作用します。
1周を超える長さやAtEndsの重なりは円周の周期でまとめ、内部線や重複面を残しません。
Arrow2D・Arrow3D・Triangleの長さが正で幅が0でない場合は、端点から根元までの本体円弧を短縮します。
負の長さは円周方向へ反転し、元の本体円弧を保ちます。
長さ0・幅0では面積0の面を省略し、Size=0では元の本体へ戻します。
塗りONのCircleは、半径0から0.5までの扇形とPartを一体化し、内側の塗りを保ちます。
WideCircleRadialは元の帯とPartを一体化し、接合部以外の内外半径を保ちます。

Arrow3Dの追加面は曲がった主面に沿い、各円の平面の法線方向へ立ち上がります。
高さは根元で `abs(0.05 * shapePartSize * shapePartWidthScale)`、先端で0です。
既定軸の基準円では+X、Cross版の追加円では+Y軸まわりに90°回した向きへ立ち上がります。

立体のCube・Octahedron・Sphereは中心、Pyramid・Coneは先端を固定します。
元の円弧端点と接線方向のOffsetから固定点を決め、円弧上の根元または
帯幅を受ける断面からその固定点へ向けます。
幅方向も同じ角度だけ回転し、長さ・幅・立体の厚みは指定寸法を保ちます。
均等な倍率のSphereは元の姿勢を保ちます。
接合部以外のCircleの半径とWideCircleRadialの内外半径は変更しません。
円弧上で接合できる場合は、先端型・中心型とも端点から接合断面までの円弧をPartへ置き換えます。
Part内部の円弧・帯も取り除き、長いPartの途中から円弧がはみ出すことや、内部線・重複面を避けます。
立体PartのOffsetは無視せず、元の端点と接線から固定点を決めるために使います。
長さが0・負値、中心型で帯幅がPartの幅を超える場合、短い円弧やOffsetによって
接合位置を求められない場合は、固定点と指定寸法を保って元の接線姿勢へ戻します。
AtApexは円周変形・角度補正の対象外で、従来の形状・配置とOffsetの作用を維持します。

WideCircleAxialは、円の軸方向に幅を持つ薄い円筒側面状の帯です。
既定軸では、半径0.5のYZ面の円弧を `X=±shapeWideWidth/2` に置き、
その間を薄い曲面でつなぎます。既定幅0.05ではX=-0.025と+0.025です。
塗り面は内外の両側から見え、円盤状の蓋や板としての厚みは追加しません。
輪郭は2本の円弧を描き、部分円弧の両端を幅方向の線で閉じます。
360°では継ぎ目の幅方向の線を追加しません。幅0では一重の円弧線となります。

WideCircleAxialのPartは全11種類に対応し、幅方向を円の軸方向へ揃えます。
AtEnd・AtEndsのArrow2D・Arrow3D・Triangle・Square・Diamond・Circleは、
展開した円筒面の上で形状を作り、半径0.5の円周へ巻き付けます。
`shapePartLengthScale` は主面の円周方向の弧長、`shapePartWidthScale` は
円の軸方向の幅を調整し、どちらにも `shapePartSize` を掛けます。
Arrow2D・Arrow3Dの根元から先端までの基準弧長は `0.1 * cos(pi / 6)`、
その他の4種類の基準長さは0.1、6種類の基準幅は0.1です。
`shapeCircleAngle` で変わる円弧端点へ追従し、`shapePartOffset` は無視します。
Offsetの値・接続は保持し、立体PartやAtApexへ切り替えると再び作用します。
この巻き付けに新しい属性は使いません。

帯とPartは展開図上で重なる領域をまとめ、円周の周期で折り返してから巻き付けます。
1周を超える長さやAtEndsの重なりでも、同じ円筒面を二重描画せず、内部の境界線を残しません。
長さが正で幅が0でないArrow2D・Arrow3D・Triangleは根元まで帯を短縮し、
短い円弧で帯の残る区間がなくなる場合は、Part同士をまとめた形状を残します。
負の長さではPartを円周方向に反転し、元の本体円弧を保ちます。
長さ0・幅0では面積0の面を省き、退化した輪郭を扱います。
幅0では本体の帯を短縮せず、円周上の退化したPartの線を合成します。
`shapePartSize=0` ではPartを省き、元の本体円弧を残します。

Arrow3Dは、円筒面上の曲がった主面に加え、曲面の根元から半径外側へ立ち上がる薄い面を持ちます。
立ち上がる高さは根元で `abs(0.05 * shapePartSize * shapePartWidthScale)`、先端で0です。
根元の弧長と高さを保ち、上側の外周辺の長さや面積は曲がり方に応じて変わります。

AtApexは巻き付けの対象外で、円弧上部から半径外側へ向く配置とOffsetの作用を維持します。
幅方向は円の軸方向、平面のPartは既定軸のXY面へ置きます。
Square・Diamond・CircleをAtApexへ置いても本体の円弧を切らず、平面のPartを外向きに配置します。
Arrow3Dの追加面は既定軸の+Zへ立ち上がります。

立体のCube・Octahedron・Sphereは中心、Pyramid・Coneは先端を固定し、
元の円弧端点と元の接線方向のOffsetを使って、寸法を保ちながら向きを補正します。
Cubeは後端の面、Octahedronは幅を持つ断面、
非一様な倍率のSphereは実際の断面から、帯幅を受ける位置へ向けます。
均等な倍率のSphereは、回転しても球としての外形が変わらないため、元の向きを保ちます。
帯幅がPartの最大幅を超える場合、長さが0または負の場合、短い円弧などで交点を
得られない場合も、元の接線方向を基準とした向きと指定寸法を保ちます。AtApexの向きは変更しません。
候補は端から内側へ最も近い位置を選び、半周を超えて回り込む位置や、向きが反転する位置は使いません。
立体のCube・Octahedron・Sphere・Pyramid・Coneは、元の円弧と立体との実際の交差に
合わせて帯の線・面を切り取り、立体内部に残しません。
円弧上に底面を接合できるPyramid・Coneは、端点から底面までの円弧をPartへ置き換え、
底面より内側の円弧を残します。中心固定の立体は元の円弧を保って交差位置で切り取ります。
円弧と立体が接している場合は直線の接合帯を追加せず、実際の交差位置でつなぎます。

### CrossCircle系

CrossCircle・WideCrossCircleRadial・WideCrossCircleAxialは、対応するCircle系を
共通の中心・半径・上方向で90°交差させた本体です。
基準円は既定軸のYZ面、追加円は+Y軸まわりに90°回したXY面に置きます。
`shapeCircleAngle`・`shapeWideWidth`・Partの調整値は両円で共用し、
軸指定・回転・スケール・入力行列は合成後の形状全体へ適用します。
180°では上方向を共有する2つの半円、360°では直交する2つの円になります。

AtEndは基準円の1端、AtEndsは各円の両端へPartを配置します。
CrossCircle・WideCrossCircleRadialは、対応するCircle・WideCircleRadialと
同じ6種類の円周変形・Offset無視と5種類の立体Partの角度補正を、それぞれの円に適用します。
AtApexは共通の+2nd頂部へ基準円の向きで1つだけ配置します。
WideCrossCircleAxialで上部の平面接合が有効な場合は、接合面中央を基準に配置します。
360°のAtEndsでは端点が同じ位置になるため、通常4端のPartが同じ位置へ集まる場合もあります。
他方のPart内部へ入る本体やPartの面・線を切り取り、一致する面は一度だけ残します。
下記のWideCrossCircleAxialの平面接合領域を除き、異なる平面や曲面同士の交差は保ち、
透過表示で交差が濃く見える部分も残します。

WideCrossCircleRadialは各円の半径方向、WideCrossCircleAxialは各円の軸方向へ帯幅を取ります。
各円のPartは対応する既存Circle系の基本仕様を引き継ぎ、
WideCrossCircleAxialの接合領域には下記の平面化を適用します。
WideCrossCircleAxialの円弧端では6種類のPartの円周変形とOffset無視を引き継ぎ、
Arrow3Dの追加面も各円の半径外側へ立ち上がります。

WideCrossCircleAxialは、上部の4交点がそろう場合に、その交点を頂点とする平面の正方形で
2つの帯を一体化します。既定軸で `R=0.5`、`h=shapeWideWidth/2` とすると、
`0 < h < R` のとき接合面の高さは `yJoin=sqrt(R*R-h*h)`、4頂点は `(±h, yJoin, ±h)` です。
接合領域内の元の帯を置き換え、内部線・継ぎ目線・重複した面を残さず、外側の円弧を保ちます。

上部の平面接合には、円弧角度 `sweep >= 2 * asin(h / R)`（ラジアン）を満たす必要があります。
それより短い円弧は元の交差表示へ戻し、円弧端点を保ちます。
360°では下部も `Y=-yJoin` の正方形で同様に接合します。
部分円弧の下部は元の表示を維持し、開口を面で塞ぎません。
帯幅0または `shapeWideWidth >= 1` では4交点による正方形を使わず、元の交差表示へ戻します。

上部の平面接合が有効なとき、AtApexの基準は `(0, yJoin, 0)` へ追従し、
Offsetは接合面を基準に従来どおり配置方向へ加算します。
平面接合が無効なときは従来の頂部を基準にします。
円周へ巻き付けるPartが交差部へ届く場合は、その主面も接合範囲だけ平面化し、帯と一体につなぎます。
Arrow3Dの追加面は、平面化後の根元からの高さと外側へ立ち上がる向きを保ちます。
大きなPartが接合面を覆う場合も、内部に入る接合面・帯の線と面を切り取り、内部線や二重面を避けます。
立体のPartは形状を保ち、平面化により本体との接続が切れる場合は、
該当する上部または下部の平面化を控えて従来の曲面へ戻します。
上部を曲面へ戻す場合は、AtApexも従来の頂部を基準にします。

### Squareの通常線とTemplate線

SquareCrossLineはSquareへ通常線の十字を、SquareCrossLineTemplateはtemplate線の十字を追加します。
いずれも本体面は通常色で選択可能です。
SquareTemplateは四隅側をtemplate線、各辺中央の幅0.3を選択可能な通常線にした四角です。
PartがOFFでも通常線を残し、矢印で突出していた箇所を直線で結びます。
SquareTemplateの本体面はtemplate色・選択不可、追加Partの線・面は通常色・選択可能です。
PartをArrow2D / Arrow3D、AtEndsにすると従来の4方向矢印の構成を表せます。

### Fin

Circle・WideCircleRadial・WideCircleAxial・CrossCircle・WideCrossCircleRadial・
WideCrossCircleAxialを除く34形状へ、Partとは独立した通常色のFinを1枚追加できます。
対象外の6種類では、`shapeFin` がONでもFinを生成せず、Fin関連属性の全設定を無視します。
描画・クリック選択・Shape / ShapeCenteredの範囲にはFinを含みません。
属性の値・接続・キーは保持し、Fin対応形状へ切り替えると再び作用します。
Arrow3Dの追加面はPart自体の形状であり、Finの対象外設定には影響されません。
Standardは矩形など本体に合った形、Taperedは幅の負側が高く正側へ低くなる形です。
通常本体ではFinが+補助軸へ張り出し、Taperedの先細る側が+主軸を示します。
Swappedではこの役割も入れ替わり、Finは+主軸へ張り出し、先細る側は+補助軸を示します。
Finの基準は矢印や小形状を除いた本体断面です。小形状ごとにFinを追加しません。

| 本体 | Finの幅 | Finの張り出し |
| --- | --- | --- |
| 通常のGear / Triangle / Square系 / Diamond / CrossLine系 | 1st | +2nd |
| 上記のSwapped | 2nd | +1st |
| Line系 / CrossLine3Axis系 / その他の立体 | 1st | +2nd |

Finは本体中心軸または断面へ接続し、根元を閉じる線を追加しません。
ArrowのStandardはくぼみ1st=-0.25から先端+0.5までの矩形、
Taperedは従来Standardの傾斜した外形です。
Cube・CylinderのTaperedは負側の高い位置から正側の本体上端へ接続します。
TriangleにTapered Finを追加すると、本体のXZ面から+Yへ立つ薄い面になります。

```text
height = shapeFinHeight * shapeFinSize
width = shapeFinWidthScale * shapeFinSize
```

PartのSize・Width・Offset・LengthをFinの寸法へ掛けません。
Arrow・OctahedronArrow本体に追従する付け根だけは、本体側の変形を反映します。
高さ0またはFin OFFではFinの線・面だけを省略し、本体・Partを残します。
負の高さは自由頂点の張り出す向きを反転し、付け根を移し替えません。
Color系でもFinは通常色で、軸・回転の制約は本体と共通です。
方向の規約は正の寸法倍率・全体変形前の基準姿勢で定義します。
負の幅・高さによる反転を許容し、全体スケールの符号はColor系を含む各本体の変形規則に従います。
同じ平面の本体・Partと重なる塗りを差し引き、小形状内部のFinの線・面を除きます。

### Part矢印の向き

主面はArrow2Dを構成する面、追加面はArrow3Dで主面に直交して加わる薄い面です。
Arrow2DとArrow3Dの主面は同じで、進行方向と、その軸まわりの回転を区別します。
以下は `shape1stAxis=+X`、`shape2ndAxis=+Y`、回転0、正の寸法倍率・スケールでの基準ローカルXYZです。
主面は画面やワールド座標に固定した面ではありません。
Circle系6本体を除く通常本体の代表方向では先端が+主軸を示し、
主面が主軸と第3軸の平面、追加面が+補助軸側となります。
Swappedでは主軸と補助軸の役割を入れ替えます。

| 本体 | 進行方向 | 主面 | Arrow3Dの追加面が立ち上がる側 |
| --- | --- | --- | --- |
| Line / WideLine | ±X | XZ | +Y |
| CrossLine / WideCrossLine | ±X・±Z | XZ | +Y |
| CrossLineSwapped / WideCrossLineSwapped | ±Y・±Z | YZ | +X |
| CrossLine3Axis / ColorCrossLine3Axis | ±X | XZ | +Y |
| 同上 | ±Y | YZ | +X |
| 同上 | ±Z | XZ | +Y |
| Cube / Sphere / ColorSphere / ColorSphereCrossLine | ±X | XZ | +Y |
| 同上 | ±Y | YZ | +X |
| 同上 | ±Z | XZ | +Y |
| 通常Square系 | ±X・±Z | XZ | +Y |
| SwappedのSquare系 | ±Y・±Z | YZ | +X |
| Circle / WideCircleRadial（AtEnd / AtEnds） | 円周方向。立体Partは接合位置から先端・中心へ向く | YZ | +X |
| Circle / WideCircleRadial（AtApex） | +Y | YZ | +X |
| WideCircleAxial（AtEnd / AtEnds） | 円周方向 | 半径0.5の円筒面 | 各位置の半径外側 |
| WideCircleAxial（AtApex） | +Y | XY | +Z |

CrossCircle系の基準円は対応するCircle系と同じ向きです。
AtEndsの追加円側は、この表の向きを共通の+2nd軸まわりに90°回した向きです。
AtApexは基準円側の1つだけを使います。

表は配置可能な方向を示し、実際に追加する端は `shapePartType` で選びます。
Circleの元の接線方向とPartの接合位置は `shapeCircleAngle` に従って変わります。
Line・3軸CrossLine・Cube・Sphereでは、同じ進行方向の主面と追加面の向きを揃えます。
3軸CrossLine・Cube・Sphereの±Y端では追加面を+Xへ立ち上げます。
進行方向と補助軸が平行になるため、1枚のFinと全端で同じ立ち上がり方向にはしません。
通常の2D本体とSwappedでは本体面を優先し、全端のPart主面を本体面に揃えます。
Circle系・CrossCircle系6本体の向きは個別の円弧規約を維持します。

WideCircleAxialの円弧端のArrow3Dは、曲がった主面から各位置の半径外側へ追加面を立ち上げます。
Circle・WideCircleRadialの円弧端のArrow3Dは、円の平面内で曲がった主面から
その平面の法線方向へ追加面を立ち上げ、根元から先端へ高さを落とします。
その他のArrow3Dは、主面の正側だけに立ち上げ、肩の中央・立ち上がった肩・先端を結ぶ三角面にします。
肩から主面へ戻る辺はFill表示時も描きます。
WideCircleAxialの円弧端を除き、±両端とも同じ基準軸の正側に揃えます。
符号付きスケールや軸指定・全体変形はその後に適用し、追加面も本体と一緒に変換します。
Color系の軸指定・回転・スケールの制約は「塗りとColor」に記した規則に従います。
Circle系・CrossCircle系6本体の共通規約への統合だけを、後述の保留事項で扱います。

### 塗りとColor

塗りは共通のshapeFillで切り替え、OFFでも透明度やPart・Finの設定を保持します。
純粋なLine・CrossLineの線は塗らず、追加Part・Finに面があれば塗ります。
Gearは外周と内円の間を塗り、穴を残します。
3D矢印は主面に直交する薄い面、Pyramid・Coneなどの立体は底面を含む面を持ちます。
閉じた立体の本体とPartは外向きの片面だけを描き、内側から裏面は表示しません。
Color系の立体とColorCornerCubeの小四角も同様です。負のスケールや親transform、
`shapeAnimationTransformMatrix` による反転後も外向きを維持します。
平面形状・WideCircleAxialの側面・Fin・Arrow2D・Arrow3Dの薄い面は両面から表示します。
裏面による半透明の重なりは除きますが、別の面や形状同士が重なる部分の濃淡は残ります。

Line・CrossLine各種の端に付けたArrow2D・Arrow3Dは、
面を表示しない場合に軸線を先端までつなぎ、Fillを表示する場合は付け根までつなぎます。
Circle系の円周へ曲げるPartは、塗りON/OFFとも円周上で一体化した輪郭を使います。
Circleの塗りOFFのArrow2D・Arrow3Dは開いたV字と円周上の軸線で先端へつなぎます。
塗りONでは元の扇形内部に入るPartの輪郭も省略し、内側の塗りは保持します。
立体のPartを円弧上の接合断面へ接合できる場合は、端点からその断面までの円弧を除きます。
SquareCrossLine・SquareCrossLineTemplateの中央ガイドは、Fill表示時も先端までつなぎます。
延長部分にも軸色・Template線の表示種別を引き継ぎます。
Wide系の帯はこの切替の対象外です。
`shapeFillTransparency=1` で面が完全透明の場合も、面を表示しない場合の線を使います。
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
ここで `p` は部品の変形と接続線の追従、およびSwappedの入替を反映した基準形状の頂点です。
Swappedの入替はこの階層の内側で完了し、AxisOffsetとAxis系TRSの指定軸を変更しません。
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
表示上の `+Z/+Y/-X` へ向き、SwappedとCircle系の基準円はXY面になります。
通常の2D本体をXY面へ向ける場合は、たとえば `shape1stAxis=+X`・`shape2ndAxis=+Z` とします。
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

`Square` はXZ面（`y=0`）、`SquareSwapped` と `Circle` はYZ面（`x=0`）にあり、
それぞれ平面内の2軸が `-0.5` から `+0.5` の範囲に収まります。
既定の `Cube` は３軸とも同じ範囲です。
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
軸方向の円筒帯とPartの接合は [BdControllerShapeAxialCircle.inc](../plugins/bdUtilNodes/src/nodes/BdControllerShapeAxialCircle.inc)、
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
立体面は外向きの頂点順序を保持し、現在のビューに向く三角形だけを描画へ渡します。
選別結果は形状・カメラ・親transformが変わるまで再利用します。
Fillの表示で輪郭が変わる形状は、面を表示しない場合の線を形状キャッシュに保持します。
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
通常の2D本体はXZ面（`y=0`）に置き、代表方向を+X、FinとArrow3Dの追加面を+Yへ向けます。
Swappedは本体・Part・Finの組立後に `(x, y, z) → (y, x, -z)` を適用し、
代表方向+Y、平面YZ、立ち上がり+Xとします。第3軸の符号も反転して右手系を保ちます。
Circle系・CrossCircle系6本体の基準円とPartは個別の既存規約を維持します。
CircleのAtApexが+Yを向くのは、この例外に含まれます。

旧モジュール由来の `RawPoint` は XY 面・`+Z` 法線の座標です。
`appendPresetComponent()` は primitive 個別の拡縮・回転・移動後に
`(x, y, z) → (z, y, -x)` へ変換し、旧形状生成の内部座標へ渡します。
面の `appendLegacyTriangle()` なども同じ変換を使います。
この旧生成座標だけを公開基準面とみなさず、通常2DのXZ面への整列とSwappedの入替を
含めた最終の基準形状で、輪郭と面の向きを揃えてください。
`presetOrientedPoint()` は `hasLegacyPlanarOrientation()` と `isSwappedPreset()` の
判定を使い、本体・Part・Finの接合後、Axis系TRSとAxisOffsetの適用前に整列します。

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

### Circle系の保守時に確認する実装経路

形状の分岐と接合の入口は `BdControllerShapeOptions.inc` の `makeOptionShapeGeometry()` です。
下記のファイルは同じ `src/nodes` ディレクトリにあり、独立したノードではなく、その生成処理を分担します。

| ファイル | 主な責務 |
| --- | --- |
| `BdControllerShapeAxialWrap.inc` | 円周方向の周期処理・断面合成と、Axialの主面・立ち上がり |
| `BdControllerShapeRadialWrap.inc` | Circle・Radialの主面・立ち上がり、内半径0への制限、Circleの扇形との合成 |
| `BdControllerShapeAxialHead.inc` / `BdControllerShapeRadialHead.inc` | 円弧へ曲げない立体Partの固定点・接合位置・向き |
| `BdControllerShapeAxialCircle.inc` / `BdControllerShapeRadialCircle.inc` | 立体Partと本体の円弧・帯との接合 |
| `BdControllerShapeCrossCircle.inc` | 直交する2つの円の合成、Part内部の切取り、Axial交差部の平面接合 |

RadialWrapはAxialWrapの周期・断面・分割位置の処理を共用します。
Axial側の共通処理を変更するときは、Radialと両方のCross版も確認してください。
`AxialHeadPlacement` はRadialの接合判定にも使うため、名前だけを根拠にAxial専用と判断しません。

Circleの塗りは元の扇形を保ち、Partの半径区間と重複しない面へ合成します。
帯と同じ対称な幅の処理だけへまとめると、中心側の塗りを失うため、この経路を残してください。
塗りOFFのCircleのArrow2D・Arrow3Dは開いたV字と円周上の軸線を使い、
塗りONでは扇形内部の輪郭を省略します。線と塗りの生成を共通化する際も、この違いを保ちます。
Crossの平面接合はWideCrossCircleAxialだけの仕様で、Radialへ自動的に適用しません。

円周は `kCircleSegments=64` を基準にし、Partの境界・交差・中心へ達する位置を追加して分割します。
頂点数は固定ではなく、boundsは実際に生成した頂点を包みます。
分割数や交点を変更する場合は、連続した曲線の理論上の極値と、生成頂点から得るboundsを区別してください。

数値の回帰は `tests/maya/node/operator/node/dag/shape/test_bd_controller_shape.py`、
描画の回帰は `tests/maya/ui/test_controller_shape_viewport.py` にあります。
`radial_circle`・`axial_circle`・`cross_circle` のテストを変更対象に応じて確認し、
長さ6.7、複数周、負値・ゼロ、大きな幅、Offsetの接続保持、AtApexへの切替を含めます。
数値・履歴・保存再読込の成功と、実GUIでの輪郭・半透明面の成功は別々に確認します。
統一検証でbatch実行時の描画テストがskipしても、GUIでの成功を意味しません。
再実行には [Viewport 2.0描画テスト](testing-debugging.md#viewport-20描画テスト) の手順を使い、
`build/` 内の一時的な起動スクリプトや画像の存在を前提にしないでください。

### 保留中: Circle系の向きの共通化

通常2D本体・Line・3軸CrossLine・立体系の向きは「Part矢印の向き」の規約へ揃えています。
Circle・WideCircleRadial・WideCircleAxial・CrossCircle・WideCrossCircleRadial・
WideCrossCircleAxialの6本体は、円弧の平面・進行方向・追加面の向きを維持します。
Sphere・ColorSphere系はこの保留の対象に含めません。

Circle系を共通化するかは、今回の変更後の本体とPartを確認してから検討します。
円弧角度、AtEnd / AtEnds / AtApex、RadialとAxialの帯、Cross版の直交する円、
長さ・幅の負値、円周変形と立体Partの接合を一緒に確認してください。
Arrow3DがArrow2Dと主面を共有し、追加面だけを増やす関係は維持します。

### 今後の候補: 多数配置時の再生性能測定

多数の `bdControllerShape` を置いたシーンで、調整属性が静的な場合、
`shapeAxisTranslate` などにキーや入力接続がある場合、親 `transform` のみを
アニメーションする場合の再生時間を比較します。基準頂点と変換後頂点の
再生成回数も記録し、現在のキャッシュが効く条件と負荷の大きい処理を特定します。
最適化が必要と分かった場合は、描画・クリック選択・`boundingBox()` の結果を
保ったまま、実測した負荷箇所に絞って変更します。
長いPartやCross版では、周期断面の合成、Part内部を除く切取り、共面部分の合成も測定対象です。
性能測定の前に、これらを既知の不具合や必須のリファクタとして扱わないでください。

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
26. shapeの40項目、PartShapeの11項目、PartTypeの3項目と、既定shapeがCube（21）であることを確認する。Gear / GearSwappedの後に通常2D系、同じ順序のSwapped系、CrossLine3Axis、Cube以降の本体が並ぶ。Circle・WideCircleRadial・WideCircleAxial・CrossCircle・WideCrossCircleRadial・WideCrossCircleAxialの順を保つ。
27. 全本体でshapeFillを切り替え、Shadedでは面・輪郭、Wireframeでは輪郭、Wireframe on Shadedでは両方を表示する。ColorCornerCubeの小四角は常に残る。
28. Triangle・Square・Circle・WideCircleAxialの側面・Fin・Arrow3Dは両面から見える。閉じた立体の本体・小形状・Color面は外側だけ見え、内側からは見えない。負のスケール・親transform・Animation行列の反転、透視・平行投影でも確認する。
29. 各塗り面の外縁が輪郭と一致し、非等方・負スケールでも選択できる。Coneと小形状Coneの側線はFill表示時も残る。CylinderのFillは両端の円を残して側線を省略し、面を表示しない場合は側線が戻る。Finの線は維持する。
30. shapePartのON/OFFで小形状だけが切り替わり、種類・配置・Offset・Size・Length・Widthの値を保持する。
31. Part対象外14本体ではONでも本体が変わらず、対応26本体へ切り替えると保持していたPart設定が作用する。
32. Line・CrossLine・CrossLine3AxisでAtEndが+1st、CrossLineSwappedで+2nd、AtEndsが全端となり、各矢印が端の外向きへ進む。小形状のない端は元の±0.5に残る。
33. 通常Square系でAtEndが+1st、Swappedで+2nd、AtEndsが4方向となり、Arrowは代表方向と他の3方向の2:1の比率を維持する。
34. Cube・Sphere・ColorSphere系でAtEndが+1st、AtEndsが6端となる。2D本体へ3DのPart、3D本体へ平面のPartも追加できる。
35. Partの基準寸法0.1、外向きTriangle/Pyramid/Cone、端点ピボット、Offsetの加算距離、長手方向と横2軸の倍率を確認する。
36. 変形したPartの手前で接続線が止まり、小形状内へ本体・Finの線や塗り面が残らない。Line・CrossLine・CircleのArrow2D/3Dは面を表示しない場合に先端までつなぐ。SquareCrossLine系の中央ガイドはFill表示時も先端までつなぐ。
37. PartとFinの倍率に負値・ゼロを使い、面積0の面を省略し、輪郭と塗り・選択・Shape / ShapeCenteredの範囲が揃う。
38. Arrow2DとArrow3Dの主面が一致する。通常2D・Lineの主面はXZ、追加面は+Y、SwappedではYZ・+Xとなる。3軸CrossLine・Cube・Sphere系は±X/±ZでXZ・+Y、±YでYZ・+Xとなり、両端でも同じ側へ立つ。Circle・WideCircleRadialの円弧端では円の法線、WideCircleAxialでは各位置の半径外側へ立ち、先端へ高さを落とす。Cross版は各円の向きに従う。肩から主面へ戻る辺をFill表示時も描き、調整値へ追従する。
39. ArrowとOctahedronArrowはPart OFFでも既存の本体調整を適用する。OctahedronArrowは既定でOctahedronと同形、Offset・Lengthで先端だけを直線的に伸ばし、Width・Sizeで共有断面と後側の面も変える。
40. Circle系・CrossCircle系6種類のshapeCircleAngleを0・120・180・240・360°へ変更し、上側中心を保って両端が対称に動く。Part OFFでも作用し、Sphere・小形状Circleには作用しない。
41. Circleの塗りが中心からの扇形、WideCircleRadialの塗りが平面の帯、WideCircleAxialの塗りが蓋のない円筒側面となり、0°で円弧・Partの線・面を省略、360°で継ぎ目の不要線を作らない。
42. CircleのAtEndが正回転側の終点、AtEndsが両端となり、6種類のPartが同じ平面の円周へ曲がり、5種類の立体Partが接合に合わせて向きを補正する。AtApexは円弧上部、他本体ではAtEnd相当となる。円周へ曲げるPartは重複領域をまとめ、姿勢が異なる立体Partは中心が共通でも別々に残る。
43. WideLine・WideCrossLineの帯がXZ面、WideCrossLineSwappedがYZ面となる。これらとWideCircle系・WideCrossCircle系でshapeWideWidthを調整し、PartのSize・Widthを変えても帯幅を保つ。十字中央・頭部との接合・半透明面の重複を確認する。幅0では本体の塗り面を省略して線を残す。
44. WideCircleRadial・WideCircleAxialのPartを調整しても接合部以外の帯幅を保ち、帯とPartが離れない。Partのない円弧端は平らに閉じる。AtEnd・AtEndsでは6種類をRadialなら同じ平面の円周、Axialなら円筒面へ曲げてOffsetを無視する。5種類の立体は固定する中心または先端と寸法を保ちながら接合に合わせて向きを補正する。AtApexは従来の配置とOffsetの作用を保つ。
45. SquareCrossLineの通常十字、SquareCrossLineTemplateのtemplate十字、SquareTemplateの四隅template線・中央通常線・template面を確認する。Part OFFでも通常線を残す。
46. SquareTemplateのPartは線・面とも通常色で選択でき、本体のtemplate線・面だけでは選択できない。Arrow2D/3D・AtEndsで4方向を確認する。
47. Fin対応34本体を2種類・塗りON/OFFで確認する。OFF・高さ0ではFinだけが消え、設定値を保持する。
48. Finの高さ・幅はshapeFinSizeとshapeFinWidthScaleで調整し、PartのSize・Widthから独立する。Arrow・OctahedronArrowの付け根だけは本体変形へ追従する。
49. 対応する通常平面本体のFinが+2ndへ直角に立ち、Swappedでは+1stへ立つ。根元を閉じる線はない。Circle系・CrossCircle系6種類ではFinをONにしても描画・選択・範囲が変わらず、値・接続・キーを保持する。対応形状へ切り替えると保持された設定が作用する。
50. 正の寸法倍率ではTaperedの細い側が通常本体の+1st、Swappedの+2ndを示す。ArrowのStandard Finはくぼみから先端までの矩形、Taperedは傾斜した外形となる。Cube・CylinderのTaperedとOctahedronArrowの面の重複も確認する。
51. ColorCrossLine3AxisとColorSphere系の軸色を保ち、追加Part・Finは通常色となる。ColorSphereCrossLineの円と十字に橋渡し線がない。
52. ColorCubeの正側RGB枠・負側通常線、ColorCornerCubeの小四角・通常面の境界と独立した透明度を確認する。
53. Color系5本体は軸指定・shapeRotate・shapeAxisRotateで向きが変わらず、shapeScale・shapeAxisScale・shapeSize・shapeRootSizeの負値は絶対値になる。通常本体へ戻すと保持値が作用する。
54. Color系のCustom Boundsは独立した変形を保ち、入力行列と親transformの回転・シアー・反転はそのまま反映する。
55. shape・親transform・上位DAG・Display LayerでNormal/Template/Referenceを切り替え、Selection Highlighting OFFなら選択前後の線色・面表示・軸色が一致する。
56. 複数ViewportでSelection Highlightingを別々に設定し、選択色・軸色・templateの選択不可と通常線のオーバーライド色をそれぞれ確認する。
57. WideCircleAxialのArrow2D・Arrow3D・Triangle・Square・Diamond・CircleをAtEnd・AtEndsに付け、主面が半径0.5の円筒面に沿う。Lengthは円周方向の弧長、Widthは円の軸方向へ作用し、CircleAngleで動く端点へ追従する。Offsetを0・正・負へ変えても形状と範囲が変わらず、値と接続は保持する。帯とPartの内部境界・重複した塗り面・接合の段差がない。
58. WideCircleAxialのCube・Octahedron・Sphere・Pyramid・ConeをAtEnd・AtEndsに付け、Offsetが0・正・負の場合も、実際の立体との交差位置の内側に帯の輪郭線と塗り面が残らない。中心固定の3種類と先端固定の2種類で位置・寸法を保ち、接合条件に応じて向きだけが補正される。斜め方向・軸方向から、塗りON/OFFと半透明の表示で内部線・二重面・接合の隙間がなく、帯の円弧が半径0.5を保つ。均等倍率のSphereは元の向きを保ち、球としての外形を変えない。
59. WideCircleAxialの上記5種類の立体で、Partの最大幅より広い帯、長さ0・負値、短い円弧・交点のない配置を試し、元の接線方向を基準とした向きへ戻っても固定する中心または先端と指定寸法を保つ。立体と円弧が接している場合は、不要な直線帯を追加しない。Pyramid・ConeをSize=6・360°にして、底面までの円弧がPartへ置き換わり、先端付近に元の円弧の小片が残らない。AtApexの向きは変わらない。
60. WideCircleAxialのAtEnd・AtEndsのArrow3Dは、根元の弧長と半径外側への高さを保ち、先端で高さ0となる。Size・Length・Widthを変えても根元の円筒面から浮かず、曲げに伴って上側の外周辺の長さが変わる。AtApexでは平面の主面と+Zへ立つ追加面を維持する。
61. 巻き付ける6種類で1周を超える長さ・360°・AtEndsを組み合わせ、周期を跨いでも内部線・二重面が出ない。負の長さは円周方向へ反転し、長さ0・幅0では面積0の面を省く。Size=0で元の円弧へ戻り、短い円弧をPartが覆う場合も隙間なく接合する。
62. WideCircleAxialのAtApexで6種類のPartが巻き付かず、Offsetの正・負が作用する。Square・Diamond・Circleは本体円弧の輪郭を切らず外向きの平面形状として表示され、AtEnd・AtEndsへ戻すと保持されたOffsetが再び無視される。
63. CrossCircle系3種類が共通の上方向を保って直交し、AtEndは基準円の1端、AtEndsは両円の4端、AtApexは基準円の向きで頂部に1つとなる。WideCrossCircleAxialで上部接合が有効な場合はAtApexが接合面中央へ追従する。部分円弧・360°・全Part・塗りON/OFF・半透明・軸変更でも配置と選択範囲を保つ。
64. WideCrossCircleAxialで円周に沿うPartも交差部の主面だけを平面化し、帯と一体につなぐ。Arrow3Dの立ち上がりは平面化後の根元からの高さと外側への向きを保ち、円弧端のOffsetを無視する。立体Part内部の他方の帯も切り取り、位置と向きが一致する面は二重描画せず、平面接合領域外の異なる曲面同士の交差は保つ。
65. WideCrossCircleAxialで上部4交点を結ぶ平面正方形を確認し、塗りON/OFF・半透明でも内部線・継ぎ目線・重複面がない。接合面外の円弧は保ち、360°では下部も同様に接合する。軸指定・回転・非等方スケール後も接合と範囲が追従する。
66. WideCrossCircleAxialで帯幅0、0より大きく1未満、1以上を切り替える。0より大きく1未満の幅では円弧角度が2*asin(h/R)以上のときだけ上部を接合し、それより短い円弧では元の表示と端点を保つ。部分円弧の下側に接合面を追加せず開口を保ち、帯幅0・1以上でも元の交差方式へ戻る。
67. WideCrossCircleAxialのAtApexで、上部接合が有効な間は基準位置が接合面中央となり、Offsetの0・正・負がその面から作用する。接合が無効なら従来の頂部へ戻る。全11種類のPartと大きなSizeを試し、交差部へ届く円周変形Partの主面も接合面と一体になり、Arrow3Dの根元からの高さと外向きを保つ。立体Partは形状を変えず、接続が切れる極だけ従来の曲面へ戻り、内部線・二重面が残らない。
68. Circle・WideCircleRadial・CrossCircle・WideCrossCircleRadialのAtEnd・AtEndsでArrow2D・Arrow3D・Triangle・Square・Diamond・Circleを試す。LengthScale=6.7など長い設定でも主面が同じ平面の円周へ沿い、Lengthが半径0.5の中心円弧長、Widthが半径方向へ作用する。Arrow3Dは各円の法線へ立ち上がり、根元の高さを保って先端で0となる。Circleの内側の扇形の塗りを保ち、元の円弧・Partの内部境界・重複面を残さない。
69. 上記4種類の円周へ曲げる6種類でOffsetの0・正・負と接続を変えても形状が変わらず、値と接続を保持する。1周超・360°・AtEndsでも周期を跨ぐ重複や内部線を作らない。負のLengthは反転し、0では退化した輪郭を扱い、Size=0では元の本体へ戻る。大きな幅で中心を越える部分は半径0へ制限する。塗りON/OFF・半透明・軸変更・アニメーションとUndo/Redoでも同じ接合を使う。
70. 上記4種類のCube・Octahedron・Sphere・Pyramid・Coneでは剛体としての角度補正を維持し、Offsetが元の接線方向で中心または先端へ作用する。短い円弧・幅不足・交点がない配置は固定点と寸法を保って元の向きへ戻る。均等倍率のSphereは元の姿勢を保つ。全11種類のAtApexは従来の形状・配置を維持し、Offsetが作用する。
71. 通常2Dと対応するSwappedを切り替え、本体・Part・Fin・template部分・選択範囲が右手系の `(x,y,z)→(y,x,-z)` へ一括追従する。AxisOffsetとAxis系TRSは指定軸の意味と値を保ち、Swappedの代表方向に合わせて勝手に交換されない。

実際のViewport 2.0を必要とする画像比較テストは
`tests/maya/ui/test_controller_shape_viewport.py` にあります。既存作業とは別の
Maya GUIプロセスでpytestから実行します。mayapyのbatch環境では明示的にskipします。
再実行手順と画像比較の注意点は
[Testing And DebuggingのViewport 2.0描画テスト](testing-debugging.md#viewport-20描画テスト) を参照してください。
