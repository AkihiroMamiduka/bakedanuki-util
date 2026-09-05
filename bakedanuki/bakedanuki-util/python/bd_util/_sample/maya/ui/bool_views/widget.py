# coding: utf-8
from __future__ import annotations

from typing import cast

from maya.api import OpenMaya as om

from ..... import Nodes
from .....maya.node.operator.attr.define.std.at.scalar.numeric.bool import (
    BoolAttrOperator,
    BoolPlugOperator,
)
from .....maya.node.operator.node._core import NodeOperator
from .....maya.ui import MayaBoolPlugView
from .....ui import (
    BoolCheckBox,
    BoolComboBox,
    BoolPushButton,
    BoolRadioButtonGroup,
    BoolStatusLabel,
    BoolViewModel,
    PythonBoolAttributeStore,
    qt,
)


def _require_optional_name(
    value: object | None, argument_name: str
) -> str | None:
    """任意指定の名前を空でないstrとして検証する。"""
    # 任意引数のNoneは未指定としてそのまま受け入れる。
    if value is None:
        return None

    # 名前が指定された場合は空でないstrだけを受け入れる。
    if not isinstance(value, str):
        raise TypeError(
            f"{argument_name}にはstrまたはNoneを指定してください: "
            f"{type(value).__name__}"
        )
    if not value:
        raise ValueError(f"{argument_name}には空でないstrを指定してください")
    return value


def _validate_maya_view_names(
    node_name: object | None,
    attribute_name: object | None,
) -> tuple[str, str] | None:
    """Maya Viewのnode名とattribute名を組として検証する。"""
    # node名とattribute名をそれぞれ任意の名前として検証する。
    node_name = _require_optional_name(node_name, "maya_node_name")
    attribute_name = _require_optional_name(
        attribute_name,
        "maya_attribute_name",
    )

    # Maya Viewはnode名とattribute名の両方が揃った場合だけ有効にする。
    if (node_name is None) != (attribute_name is None):
        raise ValueError(
            "maya_node_nameとmaya_attribute_nameは両方指定してください"
        )
    if node_name is None or attribute_name is None:
        return None
    return node_name, attribute_name


def _dynamic_bool_plug(
    node: NodeOperator,
    attribute_name: str,
) -> BoolPlugOperator:
    """NodeOperatorに未定義のdynamic bool attributeを型付きPlugへ変換する。"""
    # Maya nodeから指定名のMPlugを直接検索する。
    try:
        m_plug = node.fn_node.findPlug(attribute_name, False)
    except RuntimeError as e:
        raise AttributeError(
            f"Maya node '{node.cmd_access_name}'にattribute "
            f"'{attribute_name}'は存在しません"
        ) from e

    # このsampleが扱う単一bool以外の配列・compoundは拒否する。
    if m_plug.isArray or m_plug.isCompound:
        raise TypeError(
            f"Maya attribute '{node.cmd_access_name}.{attribute_name}'には"
            "scalar boolを指定してください"
        )

    # numeric attributeの中でもboolean型だけを同期対象として受け入れる。
    attribute = m_plug.attribute()
    if not attribute.hasFn(om.MFn.kNumericAttribute):
        raise TypeError(
            f"Maya attribute '{node.cmd_access_name}.{attribute_name}'には"
            "boolを指定してください"
        )
    numeric_attribute = om.MFnNumericAttribute(attribute)
    if numeric_attribute.numericType() != om.MFnNumericData.kBoolean:
        raise TypeError(
            f"Maya attribute '{node.cmd_access_name}.{attribute_name}'には"
            "boolを指定してください"
        )

    # 動的attributeの正式名から型付きBoolPlugOperatorを組み立てる。
    attribute_fn = om.MFnAttribute(attribute)
    long_name = cast(str, attribute_fn.name)
    short_name = cast(str, attribute_fn.shortName)
    attribute_operator = BoolAttrOperator(
        node_cls=type(node),
        name=long_name,
        long_name=long_name,
        short_name=short_name,
        attr_path=long_name,
    )
    return BoolPlugOperator(
        node=node,
        oprt_attr=attribute_operator,
        parent_attr_path="",
    )


def _resolve_bool_plug(
    node_name: str,
    attribute_name: str,
) -> tuple[NodeOperator, BoolPlugOperator]:
    """任意nodeのscalar bool attributeを型付きPlugとして返す。"""
    # scene上の既存nodeを汎用NodeOperatorとして取得する。
    node = Nodes().existing(node_name)

    # 定義済みattributeはNodeOperatorの型付きアクセスを優先する。
    try:
        plug = node[attribute_name]
    except AttributeError:
        # 追加attributeはMaya APIから型を確認して動的に解決する。
        return node, _dynamic_bool_plug(node, attribute_name)

    # 定義済みattributeもbool型でなければ同期対象から除外する。
    if not isinstance(plug, BoolPlugOperator):
        raise TypeError(
            f"Maya attribute '{node.cmd_access_name}.{attribute_name}'には"
            "boolを指定してください"
        )
    return node, plug


class BoolViewsWidget(qt.QWidget):
    """Python objectのbool attributeを複数Viewで編集するFeature Widget。"""

    def __init__(
        self,
        data: object,
        data_attribute_name: str,
        *,
        maya_node_name: str | None = None,
        maya_attribute_name: str | None = None,
        parent: qt.QWidget | None = None,
    ) -> None:
        """値の正本と任意のMaya同期先を受け取って初期化する。"""
        # Maya Viewの指定はWidget生成前にnode名とattribute名の組で検証する。
        maya_view_names = _validate_maya_view_names(
            maya_node_name,
            maya_attribute_name,
        )
        super().__init__(parent)

        # Python object内の指定attributeを値の正本としてViewModelへ接続する。
        self.data = data
        self.store = PythonBoolAttributeStore(data, data_attribute_name)
        self.view_model = BoolViewModel(parent=self)
        self.view_model.attach_store(self.store)

        # Maya指定がない場合も同じWidget APIになるよう空の同期状態を用意する。
        self.maya_node: NodeOperator | None = None
        self.maya_node_name: str | None = None
        self.maya_attribute_name: str | None = None
        self.maya_view: MayaBoolPlugView | None = None
        self._maya_node_argument: str | None = None

        # Maya指定がある場合だけplugを入力・表示用Viewとして接続する。
        if maya_view_names is not None:
            requested_node_name, requested_attribute_name = maya_view_names
            self.maya_node, plug = _resolve_bool_plug(
                requested_node_name,
                requested_attribute_name,
            )
            self.maya_node_name = self.maya_node.cmd_access_name
            self.maya_attribute_name = requested_attribute_name
            self._maya_node_argument = requested_node_name
            self.maya_view = MayaBoolPlugView(
                self.view_model,
                plug,
                self,
            )

        # 入力可能なQt Viewをすべて同じViewModelへ接続する。
        self.check_box = BoolCheckBox(
            self.view_model,
            "Visible",
            self,
        )
        self.combo_box = BoolComboBox(
            self.view_model,
            false_text="Off",
            true_text="On",
            parent=self,
        )
        self.push_button = BoolPushButton(
            self.view_model,
            false_text="Off",
            true_text="On",
            parent=self,
        )
        self.radio_button_group = BoolRadioButtonGroup(
            self.view_model,
            false_text="Off",
            true_text="On",
            parent=self,
        )

        # 読み取り専用Viewも同じ確定値を表示する。
        self.status_label = BoolStatusLabel(
            self.view_model,
            false_text="Status: Off",
            true_text="Status: On",
            parent=self,
        )

        # 現在のData Storeと任意のMaya Viewを画面上へ明示する。
        data_label = qt.QLabel(
            f"Data: {type(data).__name__}.{self.store.attribute_name}"
        )
        maya_view_name = (
            "None"
            if self.maya_node_name is None
            else f"{self.maya_node_name}.{self.maya_attribute_name}"
        )
        maya_label = qt.QLabel(f"Maya View: {maya_view_name}")

        # Maya Viewの有無に合わせて利用できる同期経路を説明する。
        description_text = "Data Store、すべてのQt View、Pythonを同期します。"
        if self.maya_view is not None:
            description_text = (
                "Data Store、すべてのQt View、Python、Attribute Editor、"
                "undo / redoを同期します。"
            )
        description = qt.QLabel(description_text)

        # 正本の現在値をScript Editorへ出力する確認操作を用意する。
        self.print_value_button = qt.QPushButton(
            "Print Data Value",
            self,
        )
        self.print_value_button.clicked.connect(self._print_data_value)

        # 各bool Viewを役割名と対にして縦に並べる。
        form_layout = qt.QFormLayout()
        form_layout.addRow("BoolCheckBox", self.check_box)
        form_layout.addRow("BoolComboBox", self.combo_box)
        form_layout.addRow("BoolPushButton", self.push_button)
        form_layout.addRow("BoolRadioButtonGroup", self.radio_button_group)
        form_layout.addRow("BoolStatusLabel", self.status_label)

        # 対象情報、bool Views、説明、確認操作を1つのWidgetへまとめる。
        layout = qt.QVBoxLayout(self)
        layout.addWidget(data_label)
        layout.addWidget(maya_label)
        layout.addLayout(form_layout)
        layout.addWidget(description)
        layout.addWidget(self.print_value_button)

    @property
    def value(self) -> bool:
        """ViewModelが現在公開している確定値を返す。"""
        return self.view_model.value.value

    def set_value(self, value: bool) -> bool:
        """UI入力と同じCommandからbool値を変更する。"""
        # Python入力も各Qt Viewと同じ値変更Commandへ集約する。
        return self.view_model.set_value_command.execute(value)

    def refresh_from_data(self) -> bool:
        """Python objectのattributeを正本としてViewへ再反映する。"""
        # 外部で直接変更されたPython attributeをStoreから読み直す。
        return self.view_model.refresh_from_store(self.store)

    def matches_configuration(
        self,
        data: object,
        data_attribute_name: str,
        maya_node_name: str | None,
        maya_attribute_name: str | None,
    ) -> bool:
        """指定内容が現在のbinding構成と同じか返す。"""
        # 比較対象のMaya指定も生成時と同じ規則で検証する。
        maya_view_names = _validate_maya_view_names(
            maya_node_name,
            maya_attribute_name,
        )

        # Python正本が異なるか利用不能なら別構成として扱う。
        if (
            self.data is not data
            or self.store.attribute_name != data_attribute_name
            or not self.store.is_available
        ):
            return False

        # Maya指定がない構成ではMaya Viewを持たないことを確認する。
        if maya_view_names is None:
            return self.maya_view is None

        # Maya Viewが破棄済みなら同じ引数でもWindowを作り直す。
        if self.maya_view is None or not self.maya_view.is_available:
            return False

        # Python正本とMaya指定の両方が一致した場合だけ再利用する。
        return (
            self._maya_node_argument == maya_view_names[0]
            and self.maya_attribute_name == maya_view_names[1]
        )

    @qt.Slot(bool)
    def _print_data_value(self, _checked: bool = False) -> None:
        """現在の内部データ値をMaya Script Editorへ出力する。"""
        # 表示中のsnapshotではなくStoreから読み直した正本値を出力する。
        print(
            f"{type(self.data).__name__}.{self.store.attribute_name} = "
            f"{self.store.read()}"
        )
