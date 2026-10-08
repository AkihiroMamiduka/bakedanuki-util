# Controller Shape

`bdControllerShape` はリグのコントローラー向けのカスタム DAG shape です。
１つの親 `transform` の下に１つの shape を置き、Viewport 2.0 に線と面を描画します。
`CircleArrow2D` は円と矢印を独立した線として描くため、両者をつなぐ線は不要です。
コントローラーとして操作するのは親 `transform` です。

## 作成例

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

control, shape = nodes.create.controllerShape(name="hand_ctrl")
shape.shape.set(shape.shape.CIRCLEARROW2D)
shape.shapeRootSize.set(1.5)
shape.shapeSize.set(0.8)
shape.shapeLineWidth.set(2.0)  # 画面上で 2 px の線
shape.shapeTransparency.set(0.25)  # 25% 透明
shape.shapeDrawOnTop.set(True)

mod.do_it_dag()
mod.do_it_dg()
```

`nodes.create.controllerShape()` は `(Transform, BdControllerShape)` を返します。
両ノードの作成は `mod.do_it_dag()`、属性設定は `mod.do_it_dg()` で確定します。
標準の `nurbsCurve` / `nurbsSurface` データや生成ノードへの接続はありません。
軸指定の既定値は主軸 `+X`・補助軸 `+Y` で、平面形状は YZ 面に作られます。
XY 面に向ける場合は `shape.shape1stAxis.set(4)`（`+Z`）を指定します。

アニメーションで形状とフォーカス範囲を変形する場合は、行列ノードの出力を接続します。
次の例では `composeMatrix` の数値入力をアニメーションさせます。

```python
animation_matrix = nodes.create.composeMatrix(name="hand_shape_animation")
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
| `shape` | enum | `Square` (11) | 下表の90種類。`Gear` を一覧の先頭とし、初期値は `Square` |
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
| `showShapeOffsetLine` | `bool` | `false` | 親 `transform` のローカル原点から、軸オフセットを除いた形状基準位置まで補助線を描く |
| `shapeOffsetLineTemplate` | `bool` | `false` | 補助線をテンプレート表示・選択不可にする |
| `shapeLineWidth` | `float` | `1` | 本体と OffsetLine の画面上の線幅。単位は pixel、最小値 `1` |
| `shapeTransparency` | `float` | `0` | 本体の輪郭線と OffsetLine の透明度。`0` は不透明、`1` は完全透明。範囲は `0`–`1` |
| `shapeFillTransparency` | `float` | `0.85` | `*Filled` の面の透明度。`0` は不透明、`1` は完全透明。範囲は `0`–`1` |
| `shapeDrawOnTop` | `bool` | `false` | 本体の輪郭線・面と OffsetLine を他のシーン形状に隠れないように描画する |
| `boundsMode` | enum | `Shape` (0) | フォーカス範囲。`Shape` (0)、`ShapeCentered` (1)、`Custom` (2) |
| `showBoundsPreview` | `bool` | `false` | 選択中の `boundsMode` の最終的な軸平行範囲を template 色で表示する。選択不可 |

### 形状一覧

| 値 | 形状 |
| --- | --- |
| 0–9 | `Gear`、`GearFilled`、`Line1st`、`Line2nd`、`Line3rd`、`CrossLineXY`、`CrossLineXYZ`、`Triangle`、`TriangleFilled`、`TriangleArrow3D` |
| 10–19 | `TriangleArrow3DFilled`、`Square`、`SquareFilled`、`SquareArrow2D`、`SquareArrow2DFilled`、`SquareArrow3D`、`SquareArrow3DFilled`、`SquareArrowCrossLine2D`、`SquareArrowCrossLine2DFilled`、`SquareArrowCrossLine3D` |
| 20–29 | `SquareArrowCrossLine3DFilled`、`SquareArrowCrossLineTemplate2D`、`SquareArrowCrossLineTemplate2DFilled`、`SquareArrowCrossLineTemplate3D`、`SquareArrowCrossLineTemplate3DFilled`、`SquareArrow4Way2D`、`SquareArrow4Way2DFilled`、`SquareArrow4Way3D`、`SquareArrow4Way3DFilled`、`SquareTemplateArrow4Way2D` |
| 30–39 | `SquareTemplateArrow4Way2DFilled`、`SquareTemplateArrow4Way3D`、`SquareTemplateArrow4Way3DFilled`、`Cube`、`CubeFilled`、`CubeArrow2D`、`CubeArrow2DFilled`、`CubeArrow3D`、`CubeArrow3DFilled`、`CubeFin` |
| 40–49 | `CubeFinFilled`、`CubeFinArrow`、`CubeFinArrowFilled`、`Octahedron`、`OctahedronFilled`、`OctahedronArrow`、`OctahedronArrowFilled`、`OctahedronArrowFin`、`OctahedronArrowFinFilled`、`Circle` |
| 50–59 | `CircleFilled`、`CircleArrow2D`、`CircleArrow2DFilled`、`CircleArrow3D`、`CircleArrow3DFilled`、`Semicircle`、`SemicircleFilled`、`SemicircleArrow2D`、`SemicircleArrow2DFilled`、`SemicircleArrow3D` |
| 60–69 | `SemicircleArrow3DFilled`、`Sphere`、`SphereFilled`、`SphereArrow2D`、`SphereArrow2DFilled`、`SphereArrow3D`、`SphereArrow3DFilled`、`Cylinder`、`CylinderFilled`、`CylinderFin` |
| 70–79 | `CylinderFinFilled`、`CylinderFinArrow`、`CylinderFinArrowFilled`、`Arrow`、`ArrowFilled`、`ArrowFin`、`ArrowFinFilled`、`Pyramid`、`PyramidFilled`、`PyramidFin` |
| 80–89 | `PyramidFinFilled`、`Cone`、`ConeFilled`、`ConeFin`、`ConeFinFilled`、`ColorCrossLine`、`ColorSphere`、`ColorSphereFilled`、`ColorSphereCrossLine`、`ColorSphereCrossLineFilled` |

基準となる部分はローカル座標の各軸でおおむね `-0.5` から `+0.5` を使います。
矢印やフィンはその範囲から張り出す設計です。形状全体を長さ1に正規化しません。
`Line1st`、`Line2nd`、`Line3rd` はそれぞれ主軸、補助軸、第3軸に沿って
`-0.5` から `+0.5` まで伸びます。`CubeFinArrow` と `CylinderFinArrow` は
`-1stAxis` 側のフィンを `+2ndAxis` 方向へ高さ `1` まで伸ばし、
`+1stAxis` 側の本体上端へ斜めにつなぎます。
`2D` / `3D` は付属する矢印の立体性を示します。
`*Filled` は既存形状の輪郭を保ち、面を加えた形状です。純粋な線形状
（`Line1st/2nd/3rd`、`CrossLineXY/XYZ`、`ColorCrossLine`）以外の
各形状に用意します。十字線など面積のない付属部分は線のままです。
`TriangleFilled`、`SquareFilled`、`CircleFilled` は YZ 面にあり、
`TriangleFilled` の底辺は `Triangle` と同じ Y=`-0.37` です。
立体形状の基準形状は３軸とも `-0.5` から `+0.5` に収まります。
`CylinderFilled` は側面と両端、`ConeFilled` は側面と底面を描き、
円周は輪郭線と同じ64分割です。面は Viewport 2.0 の三角形描画であり、
NURBS の CV・UV・材質・レンダリング用サーフェスではありません。
`GearFilled` は外周と内円の間を塗り、内円の内側を穴として残します。
`Semicircle` は底辺のない半円です。`Semicircle*Filled` は半円板を描きますが、
直径の輪郭線は追加しません。矢印の突起と Fin も面を持ち、Fin は厚みのない面です。
`SquareArrowCrossLineTemplate*` は十字線、`SquareTemplateArrow4Way*` は四隅だけを
template 色・選択不可にします。`ColorSphere` は X=赤、Y=緑、Z=青の
直交円だけで構成し、十字線を含みません。`ColorSphereCrossLine` はその円に
`ColorCrossLine` の十字線を加えます。十字線の正方向は各軸色、負方向は通常色です。
軸の向きを変えても色は元の軸に付随します。
`SquareTemplateArrow4Way*Filled` では四角い本体面が template 色・選択不可、
矢印面は通常色・選択可能です。`SquareArrowCrossLineTemplate*Filled` の
十字線は template 線のままで、本体面からは選択できます。
`ColorSphereFilled` と `ColorSphereCrossLineFilled` は球殻を通常色で塗り、
軸色の円と十字線を維持します。

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

Channel Box の表示順は次の６区画です。区切りは `_`、`__`、`___`、`____`、
`_____` という表示専用の１値 enum 属性で、値は
`-----------------------------------`、非 keyable・ロック済みです。

1. `shape`、`shapeDrawOnTop`、`shapeLineWidth`、`shapeTransparency`、`shapeFillTransparency`、`showShapeOffsetLine`、`shapeOffsetLineTemplate`
2. `shape1stAxis`、`shape2ndAxis`、`shapeAxisOffset`、`shapeAxisOffsetDirection`、`shapeAxisOffsetLength`
3. `shapeRootSize`、外側の移動・回転・スケール、内側の移動・回転・スケール、`shapeSize`
4. `boundsMode`、`showBoundsPreview`
5. `customBounds1stAxis`、`customBounds2ndAxis`、`customBoundsAxisOffset`、`customBoundsAxisOffsetDirection`、`customBoundsAxisOffsetLength`
6. `customBoundsRootSize`、外側の移動・回転・スケール、内側の移動・回転・スケール、`customBoundsSize`

区切りは Python の生成 NodeOperator API から除外します。
`MPxLocatorNode` から継承する `localPositionX/Y/Z` と `localScaleX/Y/Z` は
描画に使わないため、`bdControllerShape` では Channel Box の既定表示から外します。
標準の locator の表示設定には影響しません。

点 `p` に適用する階層は `shapeAnimationTransformMatrix > shapeRootSize > shapeTranslate > shapeRotate >
shapeScale > 軸指定 > shapeAxisOffsetLength > shapeAxisOffset > shapeAxisTranslate >
shapeAxisRotate > shapeAxisScale > shapeSize > p` です。
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

### 描画属性

`shapeLineWidth`、`shapeTransparency`、`shapeFillTransparency`、
`shapeDrawOnTop` は Viewport 2.0 の描画だけを調整します。線幅は画面上の
pixel 指定で、シーン単位や `shapeSize` とは独立しています。
`shapeTransparency` は輪郭線と OffsetLine、`shapeFillTransparency` は
`*Filled` の面に適用します。面と輪郭線は選択状態に応じた色を使います。
`shapeDrawOnTop` は輪郭線・面・OffsetLine を他のシーン形状より前に描きます。
面を含む形状では、Shaded は面と輪郭線、Wireframe は輪郭線、
Wireframe on Shaded は面と輪郭線を表示します。面内のクリックも選択対象です。
`showBoundsPreview` の確認用の箱は従来の template 色・線幅・選択不可を維持し、
これらの属性の影響を受けません。描画属性の変更はフォーカス範囲を変えず、
本体と OffsetLine のクリック選択の可否も変更しません。

### フォーカス範囲

`boundsMode=Shape` は変形済みの形状本体と表示中の OffsetLine を
含む範囲を返します。このモードが既定値です。

`boundsMode=ShapeCentered` は形状の種類・軸指定・回転・スケール・サイズを使い、
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

既定の `Square` と `Circle` は YZ 面（`x=0`）にあり、Y/Z の各軸が
`-0.5` から `+0.5` の範囲に収まります。`Cube` は３軸とも同じ範囲です。
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
Maya 上の挙動テストは [test_bd_controller_shape.py](../../../tests/maya/node/operator/node/dag/shape/test_bd_controller_shape.py)、
公開 API の型確認は [public_node_types_contract.py](../../../tests/typecheck/public_node_types_contract.py)
にあります。
線の形状は独立したストロークの配列で保持し、ストロークごとに線を描きます。
そのため `CircleArrow2D` の円と矢印や、色や選択可否の異なる部分を、橋渡しの線なしで
１つの shape に収められます。現在の円は 64 分割の折れ線で、NURBS の
degree や surface を持つ形状ではありません。
`*Filled` の面は同じ shape 内で表示種別ごとの三角形列として保持し、線と同じ形状変形と
`shapeAnimationTransformMatrix` を適用します。Square は２三角形、Circle は
64分割の扇形、Cube は６面の12三角形、Sphere は32経度×16緯度の球面です。
面の頂点も描画範囲と `boundsMode=Shape` の算出に含めます。
`shapeDrawOnTop` がオンのときは、最前面表示に対応するためストロークを
線分へ展開して描画します。色と選択可否はストロークごとに保持します。
オフの既定状態では通常の深度テストを使います。

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
オンでは選択中の通常線・面と軸色の線を Maya の選択色にし、オフでは通常線・面を
非選択時の色、軸色の線を赤・緑・青で表示します。選択そのものと、
template 色・選択不可の線には影響しません。

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
32. `ColorSphere` は赤・緑・青の直交円だけ、`ColorSphereCrossLine` は同じ円と十字線として表示され、円と十字線の間に橋渡しの線がない。
33. `bdControllerShape` を選択したまま **Show > Selection Highlighting** をオフにすると通常線・面と OffsetLine が非選択時の色に戻り、軸色の線は赤・緑・青に戻る。オンに戻すと選択色になる。オフでもクリック選択できる。
34. 複数ビューポートで Selection Highlighting のオン・オフを別々に設定し、それぞれの表示色が独立する。template 色・選択不可の線と、通常線への色オーバーライドも確認する。
35. `Line1st`、`Line2nd`、`Line3rd` が既定軸で X、Y、Z の各方向へ長さ1の線として表示され、`shape1stAxis` と `shape2ndAxis` を変更すると対応する方向へ回る。
36. `CubeFinArrow` と `CylinderFinArrow` の斜線が `-1stAxis` 側の高い位置から `+1stAxis` 側の本体上端へ伸び、軸指定・拡縮後も本体とフィンの接点が離れない。
37. 42種の `*Filled` を切り替え、Shaded で面と輪郭線、Wireframe で輪郭線、Wireframe on Shaded で両方が表示される。Shaded では面内をクリックして親 `transform` を選択できる。
38. `TriangleFilled`、`SquareFilled`、`CircleFilled` を表裏から見て、面の表示と選択を確認する。立体形状では Backface Culling のオン・オフ、円柱・円錐の側面と底面、ピラミッドの底面も確認する。
39. `shapeFillTransparency` を `0`、`0.5`、`1` に変え、輪郭線の `shapeTransparency` と独立して面の透明度が変わる。半透明の Cube・Sphere で前後の面の重なりと描画順を確認する。
40. `*Filled` で `shapeDrawOnTop` を切り替え、面と輪郭線が前面表示される。`shapeFillTransparency` を組み合わせても選択色とクリック選択が期待どおりか確認する。
41. 新しい33種の `*Filled` で輪郭線と面の外縁が一致する。Gear の穴、半円の直径側、矢印・Fin の付属面、template 本体面の非選択、ColorSphere 系の軸色の線を確認する。軸指定と非等方スケールを変えても一致し、負スケール時は表裏の表示を確認する。
