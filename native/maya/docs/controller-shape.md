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

`Cube` の根元を原点に合わせ、主軸方向へ 5 cm 伸ばす場合は、
`shapeSize=1` として次のように設定します。

```python
shape.shape.set(1)  # Cube
shape.shapeSize.set(1.0)
shape.shapeAxisOffsetLength.set(5.0)
shape.shapeAxisOffset.set(True)
shape.shapeAxisOffsetDirection.set(0)  # +1stAxis
mod.do_it_dg()
```

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
| `shapeAxisOffsetLength` | `doubleLinear` | `1 cm` | `shapeAxisOffsetDirection` で選んだ軸に沿い、オフセットと形状を原点基準で伸縮。最小値 `0` |
| `shapeAxisOffset` | `bool` | `false` | 選択した軸方向へ基準形状を固定 `0.5` オフセット |
| `shapeAxisOffsetDirection` | enum | `+1stAxis` (0) | `+1stAxis` (0)、`-1stAxis` (1)、`+2ndAxis` (2)、`-2ndAxis` (3)、`+3rdAxis` (4)、`-3rdAxis` (5) |
| `shapeAxisTranslate` | `doubleLinear3` | `(0, 0, 0)` | 指定した軸を基準に形状を平行移動 |
| `shapeAxisRotate` | `doubleAngle3` | `(0, 0, 0)` | 指定した軸を基準に XYZ 固定順に回転 |
| `shapeAxisScale` | `double3` | `(1, 1, 1)` | 指定した軸を基準に、`shapeAxisRotate` の内側で拡縮 |
| `shapeSize` | `double` | `1` | 線の頂点を末端で一律スケール |
| `showShapeOffsetLine` | `bool` | `false` | 親 `transform` のローカル原点から、軸オフセットを除いた形状基準位置まで補助線を描く |
| `shapeOffsetLineTemplate` | `bool` | `false` | 補助線をテンプレート表示・選択不可にする |

`shape`、２つの軸属性、８つの変形属性、長さ属性、２つの軸オフセット属性、２つの補助線属性、
および３軸属性の各子属性は keyable です。
Channel Box では `shape`、`shape1stAxis`、`shape2ndAxis`、`shapeRootSize`、
外側の移動・回転・スケール、`shapeAxisOffsetLength`、`shapeAxisOffset`、`shapeAxisOffsetDirection`、
内側の移動・回転・スケール、`shapeSize` の順に並びます。
shape を選択して Channel Box から数値を調整できます。
`MPxLocatorNode` から継承する `localPositionX/Y/Z` と `localScaleX/Y/Z` は
描画に使わないため、`bdControllerShape` では Channel Box の既定表示から外します。
標準の locator の表示設定には影響しません。

点 `p` に適用する階層は `shapeRootSize > shapeTranslate > shapeRotate >
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
```

ここで `⊙` は成分ごとの積です。`shapeRootSize` は平行移動と軸オフセットにも影響し、
`shapeSize` は頂点だけを拡縮します。`shape1stAxis=+Z`・`shape2ndAxis=+Y`
では `A` は恒等回転となり、従来の形状を維持します。
`shape1stAxis` は元の `+Z`、`shape2ndAxis` は元の `+Y` の行先です。
残る `+X` は「補助軸 × 主軸」で決め、右手系を維持します。
主軸と補助軸が同じ方向または正反対のときは主軸を優先し、補助軸に
`+Y` を使います。主軸が `+Y` または `-Y` の場合だけ `+Z` を使います。
これらは親 `transform` のアニメーション用 TRS とは別です。

`shapeAxisOffset` が `false` のときは `O_axis=(0, 0, 0)` です。
`true` のときは、`shapeAxisOffsetDirection` に応じて次の値を使います。

| 方向 | 軸指定前の `O_axis` |
| --- | --- |
| `+1stAxis` / `-1stAxis` | `(0, 0, +0.5)` / `(0, 0, -0.5)` |
| `+2ndAxis` / `-2ndAxis` | `(0, +0.5, 0)` / `(0, -0.5, 0)` |
| `+3rdAxis` / `-3rdAxis` | `(+0.5, 0, 0)` / `(-0.5, 0, 0)` |

`1stAxis` は主軸、`2ndAxis` は補助軸、`3rdAxis` は「補助軸 × 主軸」の方向です。
無効な軸の組では、形状と同じ補正後の補助軸と第３軸を使います。
主軸が `-X` なら `+1stAxis` は `-X` 方向、`-1stAxis` は `+X` 方向です。
`S_axis` は方向の正負にかかわらず選択軸の１成分だけを
`shapeAxisOffsetLength / 1 cm` 倍します。基準形状の長さは内部座標で `1 cm` なので、
他の変形が既定値の `Cube` では、軸オフセットをオンにすると正方向は
`0` から指定長、負方向は `-指定長` から `0` まで伸びます。
軸オフセットがオフでも、同じ軸を原点中心に伸縮します。
`0 cm` では選択軸方向に潰れます。接続から負値が入った場合も、形状の計算では
`0 cm` として扱います。`shapeAxisTranslate` の選択軸成分も
この長さで伸縮します。`shapeSize`、`shapeAxisScale`、内側の回転、外側のスケールなどを
変更した場合、形状の端や実際の長さは指定長と一致するとは限りません。
固定 `0.5` は `shapeSize`、`shapeAxisScale`、`shapeAxisRotate` の影響を受けず、
`shapeAxisOffsetLength`、外側の `shapeScale`、`shapeRotate`、`shapeRootSize` の影響を受けます。
`shapeAxisTranslate` には加算して使えます。`shapeAxisOffset` をオフにしても
`shapeAxisOffsetDirection` は長さを適用する軸を指定し続けます。
その他の変形が既定値の `Cube` は、`+1stAxis` へのオフセットで主軸方向の範囲が
`0` から `1` になります。`shapeSize` だけを `2` にすると `-0.5` から `1.5` です。

補助線の始点は親 `transform` のローカル原点 `(0, 0, 0)`、終点は上記の式に
`p=(0, 0, 0)` と `O_axis=(0, 0, 0)` を代入した形状基準位置です。
`shapeTranslate` と `shapeAxisTranslate` の移動を反映し、軸オフセットを除外します。
`shapeAxisOffsetLength` は `shapeAxisTranslate` の選択軸成分を伸縮するため、
終点にも反映します。`shapeAxisOffset`、`shapeAxisRotate`、`shapeAxisScale`、
`shapeSize` は終点を動かしません。軸オフセットだけをオンにした場合は補助線を描きません。
始点と終点が重なる場合は線を描きません。
描画・選択範囲には、軸オフセット後の形状本体と、表示中の補助線の両方を含めます。
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

## 実装と拡張

公開済みの node type は `bdControllerShape`、`MTypeId` は `0x0014271F` です。
ID の管理方針は [NODE_IDS.md](../NODE_IDS.md) に従います。
実装は [BdControllerShapeNode.cpp](../plugins/bdUtilNodes/src/nodes/BdControllerShapeNode.cpp)、
Maya 上の挙動テストは [test_bd_controller_shape.py](../../../tests/maya/node/operator/node/dag/shape/test_bd_controller_shape.py)、
公開 API の型確認は [public_node_types_contract.py](../../../tests/typecheck/public_node_types_contract.py)
にあります。
線の形状は独立したストロークの配列で保持し、ストロークごとに線を描きます。
そのため `CircleArrow` の円と矢印や `Cube` の各辺を、橋渡しの線なしで
１つの shape に収められます。現在の円は 64 分割の折れ線で、NURBS の
degree や surface を持つ形状ではありません。

ローカル頂点・補助線・描画範囲は同じ node 内のキャッシュを共有します。
直接の属性変更と接続変更は `MNodeMessage` callback でキャッシュを無効化します。
調整属性に入力接続がある場合は、再生中の値の変化を拾うために値を比較します。
値が同じなら頂点を再生成せず、入力接続のない状態では変更通知がない限り
plug の読み取りも省きます。親 `transform` の TRS はローカル形状の
再生成条件に含めません。
描画 override は選択色などの表示変化に追従するため常時更新とし、
静的な調整値では属性の再読込と頂点・描画範囲の再計算を省きます。
キャッシュの仕組みを変更する際は、描画と両方の `boundingBox()`、
属性の直接編集、Undo/Redo、キー・接続による変化を一緒に確認してください。
再生速度の改善量はまだ実測していません。

ネイティブ属性を変更したら、対応 Maya version の plug-in をビルド・配置した後、
Maya 2025 でその plug-in をロードして `generate_node_class_file()` から
`bdControllerShape` の Python 定義を再生成します。生成対象は
`node_attr/bd_controller_shape.py` と `_generated/bd_controller_shape.py` です。
生成手順は [generator.md](../../../bakedanuki/bakedanuki-util/docs/maya/node_operator/generator.md)
を参照してください。生成ファイルは手編集せず、テストと仕様書を同時に更新します。
完了前の統一検証は repository 直下で `.\scripts\verify.cmd -IncludeNative` です。

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
8. `shapeTranslate` を動かし、`showShapeOffsetLine` をオンにすると親のローカル原点から、軸オフセットを除いた形状基準位置へ補助線が出る。オフにすると消える。
9. 本体の線と重ならない補助線上をクリックし、`shapeOffsetLineTemplate` がオンなら選択されず、オフなら親 `transform` が選択される。どちらの設定でも本体の線は選択できる。
10. `shapeOffsetLineTemplate` をオンにすると補助線だけが Maya の template 表示色になり、オフにすると通常のワイヤーフレーム色に戻る。本体の線の色は変わらない。
11. 軸指定と内側の移動・回転・スケールを変更し、形状、補助線、選択範囲が直後に更新される。無効な軸の組では主軸が保たれる。
12. 親 `transform` をアニメーションしても、形状が追従し、ローカル形状の調整値は変わらない。
13. `shapeAxisTranslate` などの調整属性にキーまたは入力接続を作り、タイムラインを動かすと形状と選択範囲が追従する。直接編集と Undo/Redo の後も更新される。
14. `shapeAxisOffset` をオンにして６方向を切り替えると、形状本体と選択範囲が更新される。`Cube` の既定サイズでは片面が原点に揃い、`shapeSize=2` でも移動量は固定 `0.5` のままになる。
15. `showShapeOffsetLine` をオンにし、軸オフセットを切り替えても補助線の終点が動かない。軸オフセットだけをオンにした場合は線が出ない。
16. `Cube` で `shapeAxisOffsetLength` を変え、指定した軸方向だけが伸縮し、形状本体と選択範囲が更新される。軸オフセットがオンなら原点から、オフなら原点を中心に伸縮する。
17. `shapeAxisTranslate` の選択軸成分がある場合、長さの変更が補助線の終点にも反映される。他の変形が既定値の `Cube` では、距離プラグからの接続やシーン単位の変更後も、骨長と形状の長さが一致する。
