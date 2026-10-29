# coding: utf-8
from ._generated.bd_controller_shape import GeneratedBdControllerShape


class BdControllerShape(GeneratedBdControllerShape):
    """リグ用の複数輪郭を表示するコントローラー shape。

    `shape` は24種類の基本本体を選び、`shapeWide` は帯や面上の追加輪郭を有効にする。
    `shapeWideWidth` は基準形状上の幅で、Part・Finの寸法倍率から独立する。
    `shapeAxisSwap` は基準形状の主軸と補助軸を交換し、第3軸を反転する。
    軸属性値やAxis系TRSの意味を変えず、形状・Part・Fin・GuideLineの基準配置へ作用する。
    `shapeTemplateLine` は本体線の区間をTemplate表示にし、
    `shapeTemplateLineRate` はその割合を0から1で指定する。既定値は0.7。
    `shapeTemplateFill` は表示中の本体面だけを独立してTemplate表示にする。
    Part・Fin・GuideLine・OffsetLineとColorCornerCubeの小四角は両指定の対象外とする。
    Arc 系の `shapeArcAngle` は中央方向を保って両端を対称に動かす。
    標準は主軸と第3軸の平面、`shapeAxisSwap=True` は補助軸と第3軸の平面を基準にする。
    円弧端の平面 Part は `Radial` では円の平面内、`Axial` では円筒面へ沿わせる。
    `shapeWide=False` の Arc 系では `shapeFill` は Part にだけ作用し、幅を保持して無視する。
    Arc 系以外の `AtEnds` は `shapePartSize` に、代表へ `shapePartPrimarySizeScale`、
    その他へ `shapePartOtherSizeScale` を掛ける。既定値は1と0.5で、全種類の Part に作用する。
    0の Part は省略し、両方0なら Part OFF と同じになる。負値は符号付き倍率として扱う。
    `AtEnd`・`AtApex` と Arc 系では両倍率の設定を保持して無視する。
    配置ピボットと `shapePartOffset` の距離は変えない。
    Color 系は本体の向きと軸色を固定し、`shapeAxisSwap` と
    `shape1stAxis` / `shape2ndAxis` を Part・Fin の配置姿勢にだけ適用する。
    Color 系の `shapeRotate` / `shapeAxisRotate` は引き続き無視する。
    """

    __slots__ = ()

    NODE_TYPE = "bdControllerShape"
