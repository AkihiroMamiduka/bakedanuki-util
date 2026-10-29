# coding: utf-8
from ._generated.bd_controller_shape import GeneratedBdControllerShape


class BdControllerShape(GeneratedBdControllerShape):
    """リグ用の複数輪郭を表示するコントローラー shape。

    Arc 系の `shapeArcAngle` は中央方向を保って両端を対称に動かす。
    標準は主軸と第3軸の平面、`Swapped` は補助軸と第3軸の平面を基準にする。
    円弧端の平面 Part は `Radial` では円の平面内、`Axial` では円筒面へ沿わせる。
    薄い Arc 系では `shapeFill` は Part にだけ作用し、`shapeWideWidth` は無視する。
    Arc 系以外の `AtEnds` は `shapePartSize` に、代表へ `shapePartPrimarySizeScale`、
    その他へ `shapePartOtherSizeScale` を掛ける。既定値は1と0.5で、全種類の Part に作用する。
    0の Part は省略し、両方0なら Part OFF と同じになる。負値は符号付き倍率として扱う。
    `AtEnd`・`AtApex` と Arc 系では両倍率の設定を保持して無視する。
    配置ピボットと `shapePartOffset` の距離は変えない。
    Color 系は本体の向きと軸色を固定し、`shape1stAxis` / `shape2ndAxis` を
    Part・Fin の配置姿勢に適用する。`shapeRotate` / `shapeAxisRotate` は引き続き無視する。
    """

    __slots__ = ()

    NODE_TYPE = "bdControllerShape"
