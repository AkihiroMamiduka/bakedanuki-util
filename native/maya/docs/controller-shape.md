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
| `shapeRootSize` | `double` | `1` | 平行移動を含む全体の一律スケール |
| `shapeTranslate` | `doubleLinear3` | `(0, 0, 0)` | root の内側で形状を平行移動 |
| `shapeRotate` | `doubleAngle3` | `(0, 0, 0)` | XYZ 固定順で回転 |
| `shapeScale` | `double3` | `(1, 1, 1)` | 回転前の局所軸方向で拡縮 |
| `shapeSize` | `double` | `1` | 線の頂点を末端で一律スケール |

`shape` と５つの変形属性、および３軸属性の各子属性は keyable です。
shape を選択して Channel Box から数値を調整できます。
`MPxLocatorNode` から継承する `localPositionX/Y/Z` と `localScaleX/Y/Z` は
描画に使わないため、`bdControllerShape` では Channel Box の既定表示から外します。
標準の locator の表示設定には影響しません。

点 `p` に適用する階層は
`shapeRootSize > shapeTranslate > shapeRotate > shapeScale > shapeSize > p` です。
XYZ 回転を `R` とすると、計算結果は次のとおりです。

```text
p_out = shapeRootSize * (shapeTranslate + R_XYZ(shapeScale ⊙ (shapeSize * p)))
```

ここで `⊙` は成分ごとの積です。`shapeRootSize` は `shapeTranslate` の
移動量にも影響し、`shapeSize` は頂点だけを拡縮します。
これらは親 `transform` のアニメーション用 TRS とは別です。

既定の `Square` と `Circle` は XY 面にあり、各軸 `-0.5` から `+0.5`
の範囲に収まります。`Cube` は３軸とも同じ範囲です。
`CircleArrow` は XY 面で、半径 `0.32` の円と、
`(-0.1, 0.38)` → `(0, 0.5)` → `(0.1, 0.38)` → 始点の
独立した三角形からなります。

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
