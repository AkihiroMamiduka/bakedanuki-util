# Controller Shape

`bdControllerShape` はリグのコントローラー向けのカスタム DAG shape です。
１つの親 `transform` の下に１つの shape を置き、Viewport 2.0 に線を描画します。
`CircleArrow` は円と矢印を独立した線として描くため、両者をつなぐ線は不要です。
コントローラーとして操作するのは親 `transform` です。

## 作成例

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

control, shape = nodes.create.controllerShape(name="hand_ctrl")
shape.shape.set(3)  # CircleArrow
shape.shape1stAxis.set(4)  # +Z
shape.shape2ndAxis.set(2)  # +Y
shape.shapeRootSize.set(1.5)
shape.shapeSize.set(0.8)

mod.do_it_dag()
mod.do_it_dg()
```

`nodes.create.controllerShape()` は `(Transform, BdControllerShape)` を返します。
両ノードの作成は `mod.do_it_dag()`、属性設定は `mod.do_it_dg()` で確定します。
標準の `nurbsCurve` データや生成ノードへの接続はありません。

## 形状と属性

| Attribute | Maya の型 | 既定値 | 意味 |
| --- | --- | --- | --- |
| `shape` | enum | `Square` (0) | `Square` (0)、`Cube` (1)、`Circle` (2)、`CircleArrow` (3) |
| `shape1stAxis` | enum | `+Z` (4) | 元の `+Z` 軸を向ける方向。`+X` (0)、`-X` (1)、`+Y` (2)、`-Y` (3)、`+Z` (4)、`-Z` (5) |
| `shape2ndAxis` | enum | `+Y` (2) | 元の `+Y` 軸を向ける方向。選択肢は `shape1stAxis` と同じ |
| `shapeRootSize` | `double` | `1` | 平行移動を含む全体の一律スケール |
| `shapeTranslate` | `doubleLinear3` | `(0, 0, 0)` | 軸指定の外側で形状を平行移動 |
| `shapeRotate` | `doubleAngle3` | `(0, 0, 0)` | 軸指定の外側で XYZ 固定順に回転 |
| `shapeScale` | `double3` | `(1, 1, 1)` | 軸指定の外側、`shapeRotate` の内側で拡縮 |
| `shapeAxisTranslate` | `doubleLinear3` | `(0, 0, 0)` | 指定した軸を基準に形状を平行移動 |
| `shapeAxisRotate` | `doubleAngle3` | `(0, 0, 0)` | 指定した軸を基準に XYZ 固定順に回転 |
| `shapeAxisScale` | `double3` | `(1, 1, 1)` | 指定した軸を基準に、`shapeAxisRotate` の内側で拡縮 |
| `shapeSize` | `double` | `1` | 線の頂点を末端で一律スケール |
| `showShapeOffsetLine` | `bool` | `false` | 親 `transform` のローカル原点から変形後のシェイプ原点まで補助線を描く |
| `shapeOffsetLineTemplate` | `bool` | `false` | 補助線をテンプレート表示・選択不可にする |

`shape`、２つの軸属性、８つの変形属性、２つの補助線属性、および３軸属性の各子属性は keyable です。
Channel Box では `shape`、`shape1stAxis`、`shape2ndAxis`、`shapeRootSize`、
外側の移動・回転・スケール、内側の移動・回転・スケール、`shapeSize` の順に並びます。
shape を選択して Channel Box から数値を調整できます。
`MPxLocatorNode` から継承する `localPositionX/Y/Z` と `localScaleX/Y/Z` は
描画に使わないため、`bdControllerShape` では Channel Box の既定表示から外します。
標準の locator の表示設定には影響しません。

点 `p` に適用する階層は `shapeRootSize > shapeTranslate > shapeRotate >
shapeScale > 軸指定 > shapeAxisTranslate > shapeAxisRotate > shapeAxisScale >
shapeSize > p` です。外側・内側の XYZ 回転をそれぞれ `R`・`R_axis`、
軸指定から作る回転を `A` とすると、計算結果は次のとおりです。

```text
p_out = shapeRootSize * (
    shapeTranslate + R_XYZ(
        shapeScale ⊙ A(
            shapeAxisTranslate + R_axis_XYZ(
                shapeAxisScale ⊙ (shapeSize * p)
            )
        )
    )
)
```

ここで `⊙` は成分ごとの積です。`shapeRootSize` は両方の移動量にも影響し、
`shapeSize` は頂点だけを拡縮します。`shape1stAxis=+Z`・`shape2ndAxis=+Y`
では `A` は恒等回転となり、従来の形状を維持します。
`shape1stAxis` は元の `+Z`、`shape2ndAxis` は元の `+Y` の行先です。
残る `+X` は「補助軸 × 主軸」で決め、右手系を維持します。
主軸と補助軸が同じ方向または正反対のときは主軸を優先し、補助軸に
`+Y` を使います。主軸が `+Y` または `-Y` の場合だけ `+Z` を使います。
これらは親 `transform` のアニメーション用 TRS とは別です。

補助線の始点は親 `transform` のローカル原点 `(0, 0, 0)`、終点は上記の式に
`p=(0, 0, 0)` を代入した、両方の移動を反映する最終的な形状原点です。
`shapeAxisRotate`、`shapeAxisScale`、`shapeSize` は終点を動かしません。
始点と終点が重なる場合は線を描きません。
`shapeOffsetLineTemplate` が `true` のときは補助線だけを選択対象から外し、
Maya の template 表示色で描きます。`false` なら補助線は通常のワイヤーフレーム色で
クリック選択に使えます。どちらの設定でも形状本体の線は選択できます。
補助線が形状本体の線と重なる箇所では、本体の線で選択される場合があります。

既定の `Square` と `Circle` は XY 面にあり、各軸 `-0.5` から `+0.5`
の範囲に収まります。`Cube` は３軸とも同じ範囲です。
`CircleArrow` は XY 面で、半径 `0.32` の円と、
`(-0.1, 0.38)` → `(0, 0.5)` → `(0.1, 0.38)` → 始点の
独立した三角形からなります。

調整属性が固定されている間は、形状のローカル頂点・補助線・描画範囲を
再利用します。親 `transform` のアニメーションでは形状調整を再計算しません。
調整属性自身をアニメーションまたは接続で変更する場合は、値が変わった時点で
形状を更新します。描画と親 `transform` の評価には引き続き処理が必要です。

## 表示と選択

この shape は Maya 標準の `nurbsCurve` ではありません。
**Show > NURBS Curves** と **Alt + 1** の切り替え対象にはなりません。
`bdControllerShape` は `MPxLocatorNode::excludeAsLocator()` で `false` を返し、
**Show > Locators** をオフにしたビューポートでも描画する設計です。
Viewport 2.0 では **Show > Plugins > Plugin Shapes** をオフにすると、
描画オーバーライドが線の描画を省略します。オンに戻すと線を描画します。
shape 自身の `visibility` をオフにすると非表示になります。
この表示条件は [Autodesk の API 説明](https://help.autodesk.com/cloudhelp/2024/ENU/MAYA-API-REF/cpp_ref/class_m_px_locator_node.html)
に基づきます。

ビューポートの描画とクリック選択は `mayapy` のヘッドレステストだけでは
確認できません。Maya 2025 / 2026 / 2027 の GUI で次を確認してください。

1. `CircleArrow` を表示し、円と矢印が離れた２つの輪郭として見え、橋渡しの線がない。
2. 親 `transform` を選択解除し、円と矢印のそれぞれをクリックすると、同じ親 `transform` を選択できる。
3. **Show > Plugins > Plugin Shapes** をオフにするとこの shape が消え、オンに戻すと再び表示される。オフの間にクリックで選択されないかも確認する。
4. **Show > Locators** をオフにして標準 locator が消えても、この shape は表示される。
5. shape の `visibility` をオフにすると消え、オンに戻すと再び表示される。
6. `shape` と各変形属性を変えた直後に、描画と選択範囲が更新される。
7. シーンを Maya ASCII で保存して再読込し、上記の表示と選択を再確認する。
8. `shapeTranslate` を動かし、`showShapeOffsetLine` をオンにすると親のローカル原点からシェイプの中心へ補助線が出る。オフにすると消える。
9. 本体の線と重ならない補助線上をクリックし、`shapeOffsetLineTemplate` がオンなら選択されず、オフなら親 `transform` が選択される。どちらの設定でも本体の線は選択できる。
10. `shapeOffsetLineTemplate` をオンにすると補助線だけが Maya の template 表示色になり、オフにすると通常のワイヤーフレーム色に戻る。本体の線の色は変わらない。
11. 軸指定と内側の移動・回転・スケールを変更し、形状、補助線、選択範囲が直後に更新される。無効な軸の組では主軸が保たれる。
12. 親 `transform` をアニメーションしても、形状が追従し、ローカル形状の調整値は変わらない。
