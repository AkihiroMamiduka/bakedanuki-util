# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ...._core import AttrOperator, PlugOperator, AttributeField
from ...std.at.double import DoubleField


class Double3PlugOperator(PlugOperator["Double3AttrOperator"]):
    __slots__ = ()

    x = DoubleField()
    y = DoubleField()
    z = DoubleField()

    # get
    def get(self) -> list[float]:
        value = [
            self.plug.child(0).asDouble(),
            self.plug.child(1).asDouble(),
            self.plug.child(2).asDouble(),
        ]

        # 戻り値
        return value

    # set
    def set(self, *value: float | list[float]):
        try:
            # set(x, y, z)
            try:
                # 型に合わせて、値をセット
                self._node._dg_mod.newPlugValueDouble(
                    self.plug.child(0), value[0]
                )
                self._node._dg_mod.newPlugValueDouble(
                    self.plug.child(1), value[1]
                )
                self._node._dg_mod.newPlugValueDouble(
                    self.plug.child(2), value[2]
                )
            # set([x, y, z])
            except Exception:
                # 型に合わせて、値をセット
                self._node._dg_mod.newPlugValueDouble(
                    self.plug.child(0), value[0][0]
                )
                self._node._dg_mod.newPlugValueDouble(
                    self.plug.child(1), value[0][1]
                )
                self._node._dg_mod.newPlugValueDouble(
                    self.plug.child(2), value[0][2]
                )
        except Exception as e:
            raise TypeError(
                f"Expected either set(x, y, z) or set([x, y, z]): {value}"
            ) from e

    # add
    def add_attr(self):
        # アトリビュートが既に存在する場合はスキップ
        if self.exists():
            return

        # ファンクションを作成
        fn_attr = om.MFnNumericAttribute()
        self._fn_attr = fn_attr

        # アトリビュートを作成
        #   子属性
        x_attr = fn_attr.create(
            f"{self.long_name}X",
            f"{self.short_name}x",
            om.MFnNumericData.kDouble,
            0.0,
        )
        y_attr = fn_attr.create(
            f"{self.long_name}Y",
            f"{self.short_name}y",
            om.MFnNumericData.kDouble,
            0.0,
        )
        z_attr = fn_attr.create(
            f"{self.long_name}Z",
            f"{self.short_name}z",
            om.MFnNumericData.kDouble,
            0.0,
        )
        #   親属性(double3)
        double3_attr = fn_attr.create(
            self.long_name,
            self.short_name,
            x_attr,
            y_attr,
            z_attr,
        )

        # ノードにアトリビュートを追加
        self._node.fn_node.addAttribute(double3_attr)


class Double3AttrOperator(AttrOperator[Double3PlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "double3"


class Double3Field(AttributeField[Double3AttrOperator, Double3PlugOperator]):
    __slots__ = ()

    ATTR_CLS = Double3AttrOperator
    PLUG_CLS = Double3PlugOperator
