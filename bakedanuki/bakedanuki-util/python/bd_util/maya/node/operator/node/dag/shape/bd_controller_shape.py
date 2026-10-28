# coding: utf-8
from ._generated.bd_controller_shape import GeneratedBdControllerShape


class BdControllerShape(GeneratedBdControllerShape):
    """リグ用の複数輪郭を表示するコントローラー shape。

    Arc 系の `shapeArcAngle` は中央方向を保って両端を対称に動かす。
    標準は主軸と第3軸の平面、`Swapped` は補助軸と第3軸の平面を基準にする。
    円弧端の平面 Part は `Radial` では円の平面内、`Axial` では円筒面へ沿わせる。
    薄い Arc 系では `shapeFill` は Part にだけ作用し、`shapeWideWidth` は無視する。
    Arc 系以外の `AtEnds` は全種類の Part で代表の1つを標準サイズ、残りを0.5倍にする。
    配置ピボットと `shapePartOffset` の距離は変えない。
    Color 系は本体の向きと軸色を固定し、`shape1stAxis` / `shape2ndAxis` を
    Part・Fin の配置姿勢に適用する。`shapeRotate` / `shapeAxisRotate` は引き続き無視する。
    """

    __slots__ = ()

    NODE_TYPE = "bdControllerShape"
