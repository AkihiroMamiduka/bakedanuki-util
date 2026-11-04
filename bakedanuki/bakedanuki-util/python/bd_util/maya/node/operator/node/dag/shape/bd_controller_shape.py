# coding: utf-8
from ._generated.bd_controller_shape import GeneratedBdControllerShape


class BdControllerShape(GeneratedBdControllerShape):
    """リグ用の複数輪郭を表示するコントローラー shape。

    `shape` は24種類の基本本体を選び、`shapeWide` は帯や面・曲面上のフレームを有効にする。
    `shapeWideWidth` は基準空間で変形した本体上の実距離で、基準空間の伸縮やPart・Finの倍率から独立する。
    立体Wideは穴のある厚み0の帯だけを両面表示する。Wide Sphereは3帯の和集合の外周だけを描き、
    全被覆時のFill OFFでは通常の3大円へ戻る。
    `shapeAxisSwap` は基準形状の主軸と補助軸を交換し、第3軸を反転する。
    軸属性値やAxis系TRSの意味を変えず、形状・Part・Fin・GuideLineの基準配置へ作用する。
    `shapeBaseSpace1stAxisMinus` / `shapeBaseSpace1stAxisPlus` は元の主軸両端の行き先を距離で指定する。
    `shapeBaseSpace2ndAxisMinus` / `shapeBaseSpace2ndAxisPlus` と
    `shapeBaseSpace3rdAxisMinus` / `shapeBaseSpace3rdAxisPlus` も各軸を同様に調整する。
    全軸の既定値は `-0.5 cm` / `+0.5 cm`。
    `shapeBaseSpace1stAxisPlusScale2ndAxis` など12個の面内倍率は、6面の各2軸を独立して拡縮する。
    `shapeBaseSpace1stAxisPlusScale` など6個の `double2` 親へ各面の2軸をまとめ、既定値は `(1, 1)`。
    親の `.set(0.5, 1.5)` で一括設定でき、`.get()` は `Double2` を返す。子への直接アクセスも維持する。
    面内倍率の既定値は1で、隣接面の影響を乗算し、8頂点から補間した基準空間で本体を変形する。
    面のねじれや範囲外の点への外挿も許容し、Partの寸法・OffsetとFinの高さを保つ。
    Arrow本体の後端部分だけは `0.25 cm`、OctahedronArrow本体では `0.5 cm` に固定する。
    その本体を構成してから面内倍率で変形する。
    Minusを後端、Plusを先端として短い長さでも接合位置をクランプせず、Part属性を本体へ適用しない。
    ArrowのWide先端は帯境界の交点まで延ばし、鋭角でも尖りを保つ。
    ColorCornerCubeの小四角は基準空間で各辺 `0.2 cm` を保ち、小さい本体では面内へ切り詰める。
    追加Partは配置点と姿勢だけを追従させ、局所寸法と `shapePartOffset` の距離を保つ。
    ArcのPartは変形後の曲線上の弧長と局所幅を保ち、Finは付け根と幅へ追従して高さを保つ。
    `shapeSize`・共通TRS・入力行列は、組立後の本体・Part・Fin・Wideへ共通に作用する。
    `customBoundsBaseSpaceXPlus` / `customBoundsBaseSpaceXMinus` とY/Zの両端は、
    親transformのローカルXYZへ固定した独立の箱を距離で指定する。
    `boundsMode=Custom` のフォーカスとプレビューだけへ使い、共有入力行列と親transformを反映する。
    `shapeTemplateLine` は本体線の区間をTemplate表示にし、
    `shapeTemplateLineRate` はその割合を0から1で指定する。既定値は0.7。
    `shapeTemplateLineInvert` は通常とTemplateの区間をそのまま反転する。
    `shapeTemplateFill` は表示中の本体面だけを独立してTemplate表示にする。
    `shapePartTemplate` と `shapeFinTemplate` は各部品の線と面だけをTemplate表示にする。
    本体・各部品・GuideLine・OffsetLineの指定は独立し、ColorCornerCubeの小四角を保護する。
    Arc 系の `shapeArcAngle` は中央方向を保って両端を対称に動かす。
    標準は主軸と第3軸の平面、`shapeAxisSwap=True` は補助軸と第3軸の平面を基準にする。
    円弧端の平面 Part は `Radial` では円の平面内、`Axial` では円筒面へ沿わせる。
    `shapeWide=False` の Arc 系では `shapeFill` は Part にだけ作用し、幅を保持して無視する。
    Arc 系以外の `AtEnds` は `shapePartSize` に、代表へ `shapePartPrimarySizeScale`、
    その他へ `shapePartOtherSizeScale` を掛ける。既定値は1と0.5で、全種類の Part に作用する。
    0の Part は省略し、両方0なら Part OFF と同じになる。負値は符号付き倍率として扱う。
    `AtEnd`・`AtApex` と Arc 系では両倍率の設定を保持して無視する。
    配置ピボットと `shapePartOffset` の距離は変えない。
    `shapePartLengthScale`・`shapePartWidthScale`・`shapePartHeightScale` は局所3軸の独立した倍率。
    Heightは符号を保ち、Arrow3DのHeight 0では追加面を省いてArrow2Dと一致する。
    Color 系は本体の向きと軸色を固定し、`shapeAxisSwap` と
    `shape1stAxis` / `shape2ndAxis` を Part・Fin の配置姿勢にだけ適用する。
    Color 系の `shapeRotate` / `shapeAxisRotate` は引き続き無視する。
    Color 系の面内倍率は、属性の符号を保持したまま描画時だけ絶対値を使う。
    """

    __slots__ = ()

    NODE_TYPE = "bdControllerShape"
