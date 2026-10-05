# coding: utf-8
"""Maya標準の値入力を、対応する接続経路と復旧範囲へ限定する。"""

from __future__ import annotations

import math
from collections.abc import Callable
from dataclasses import dataclass
from typing import Literal, cast

from maya import cmds
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ...node.operator.attr import _keyframe_target

_Scalar = float | bool | int
_Mode = Literal["time", "driven", "layer"]


def _path(plug: om.MPlug) -> str:
    """DAGの同名ノードを区別できる属性名を返す。"""
    return _keyframe_target.plug_path(plug)


def _scalar(plug: om.MPlug) -> _Scalar:
    """setAttrと同じ現在単位でscalar値を読む。"""
    return cast(_Scalar, cmds.getAttr(_path(plug)))


def _set(plug: om.MPlug, value: _Scalar) -> None:
    """数値型ごとの差をMaya command境界へ閉じ込める。"""
    cast(Callable[[str, _Scalar], None], cmds.setAttr)(_path(plug), value)


def _units() -> tuple[int, int, int]:
    """編集時の時間・角度・距離の単位を固定する。"""
    return om.MTime.uiUnit(), om.MAngle.uiUnit(), om.MDistance.uiUnit()


def _check_plug(plug: om.MPlug) -> None:
    """値入力可能なscalar型と属性・ノードのlockを検証する。"""
    attribute = plug.attribute()
    if plug.isArray or plug.isCompound:
        raise RuntimeError("配列または複合属性への入力には対応していません")
    if not any(
        attribute.hasFn(kind)
        for kind in (
            om.MFn.kNumericAttribute,
            om.MFn.kEnumAttribute,
            om.MFn.kUnitAttribute,
        )
    ):
        raise RuntimeError("数値・角度・距離・bool・enum属性だけ編集できます")
    if (
        attribute.hasFn(om.MFn.kUnitAttribute)
        and om.MFnUnitAttribute(attribute).unitType()
        == om.MFnUnitAttribute.kTime
    ):
        raise RuntimeError("時間属性の接続編集には対応していません")
    if not om.MFnAttribute(attribute).writable:
        raise RuntimeError("書き込み不可の属性です")
    if om.MFnDependencyNode(plug.node()).isLocked:
        raise RuntimeError("ノードがロックされています")
    ancestor = plug
    while True:
        if ancestor.isLocked:
            raise RuntimeError("属性または親属性がロックされています")
        if ancestor != plug and ancestor.isDestination:
            raise RuntimeError("親属性に入力接続があります")
        if not ancestor.isChild:
            break
        ancestor = ancestor.parent()


def _unique(nodes: list[om.MObject]) -> tuple[om.MObject, ...]:
    """同じノードをAPI実体で重複排除する。"""
    result: list[om.MObject] = []
    for node in nodes:
        if node not in result:
            result.append(node)
    return tuple(result)


def _layer_owners(node: om.MObject) -> tuple[om.MObject, ...]:
    """blendNodesへ登録された正規のAnimation Layerだけを返す。"""
    message = om.MFnDependencyNode(node).findPlug("message", False)
    return _unique(
        [
            destination.node()
            for destination in message.connectedTo(False, True)
            if destination.node().hasFn(om.MFn.kAnimLayer)
            and om.MFnAttribute(destination.attribute()).name == "blendNodes"
        ]
    )


def _check_blend(
    node: om.MObject, owners: tuple[om.MObject, ...], target: om.MPlug
) -> None:
    """正規レイヤーの重みと値入力以外に演算接続を持つ合成を除外する。"""
    fn = om.MFnDependencyNode(node)
    for destination in fn.getConnections():
        if not destination.isDestination or destination.attribute().hasFn(
            om.MFn.kMessageAttribute
        ):
            continue
        attribute = om.MFnAttribute(destination.attribute()).name
        if attribute.startswith(("inputA", "inputB")):
            continue
        source = destination.sourceWithConversion()
        source_name = om.MFnAttribute(source.attribute()).name
        if attribute in ("weightA", "weightB") and source.node() in owners:
            if source_name in ("backgroundWeight", "foregroundWeight"):
                continue
        if attribute == "accumulationMode" and source.node() in owners:
            if source_name in (
                "outRotationAccumulationMode",
                "scaleAccumulationMode",
            ):
                continue
        if (
            attribute == source_name == "rotateOrder"
            and source.node() == target.node()
        ):
            continue
        raise RuntimeError(
            f"Animation Layerの合成設定に独自の入力接続があります: {source.name()} -> {destination.name()}"
        )


def _blend_inputs(source: om.MPlug) -> tuple[om.MPlug, ...]:
    """出力に対応する値入力を取り出し、回転は連動する三軸を含める。"""
    node = om.MFnDependencyNode(source.node())
    attribute = om.MFnAttribute(source.attribute()).name
    if attribute not in ("output", "outputX", "outputY", "outputZ"):
        raise RuntimeError("Animation Layerの値出力以外は編集できません")
    suffixes = (
        ("X", "Y", "Z")
        if node.typeName == "animBlendNodeAdditiveRotation"
        else (attribute.removeprefix("output"),)
    )
    return tuple(
        node.findPlug("input" + side + suffix, False)
        for side in ("A", "B")
        for suffix in suffixes
    )


def _check_curve(
    source: om.MPlug, destination: om.MPlug, *, layered: bool
) -> oma.MFnAnimCurve:
    """同じ型の非共有カーブと、対応する時間またはSDK入力を検証する。"""
    curve = oma.MFnAnimCurve(source.node())
    expected = (
        curve.timedAnimCurveTypeForPlug(destination)
        if curve.isTimeInput
        else curve.unitlessAnimCurveTypeForPlug(destination)
    )
    if (
        curve.animCurveType != expected
        or source != curve.findPlug("output", False)
        or not curve.numKeys
    ):
        raise RuntimeError("属性と同じ型の既存アニメーションだけ編集できます")
    if len(source.connectedTo(False, True)) != 1:
        raise RuntimeError("複数属性で共有するカーブは編集できません")
    if layered and not curve.isTimeInput:
        raise RuntimeError("SDKを合成するAnimation Layerは編集できません")
    if (
        curve.animCurveType
        in (
            oma.MFnAnimCurve.kAnimCurveTA,
            oma.MFnAnimCurve.kAnimCurveUA,
        )
        and curve.findPlug("rotationInterpolation", False).asInt() != 1
    ):
        raise RuntimeError("独立した回転カーブだけ編集できます")
    input_plug = curve.findPlug("input", False)
    if curve.isTimeInput and input_plug.sourceWithConversion().isNull:
        if cmds.objExists("time1.enableTimewarp") and cmds.getAttr(
            "time1.enableTimewarp"
        ):
            raise RuntimeError("独自の時間入力を持つカーブは編集できません")
    for connection in curve.getConnections():
        if not connection.isDestination or connection.attribute().hasFn(
            om.MFn.kMessageAttribute
        ):
            continue
        if connection != input_plug:
            raise RuntimeError("カーブの設定に入力接続があります")
        if curve.isTimeInput:
            driver = connection.sourceWithConversion()
            node = om.MFnDependencyNode(driver.node())
            if (
                node.typeName != "time"
                or om.MFnAttribute(driver.attribute()).name != "outTime"
                or node.findPlug("enableTimewarp", False).asBool()
            ):
                raise RuntimeError(
                    "独自の時間入力を持つカーブは編集できません"
                )
    if not layered:
        try:
            _keyframe_target.check_key_editable_curve(curve)
        except RuntimeError as error:
            raise RuntimeError(
                "カーブがロックまたは参照されています"
            ) from error
    return curve


@dataclass(frozen=True)
class ConnectedPlugEditInfo:
    """対応する入力の種類と表示文、変更監視に必要な経路を保持する。"""

    mode: _Mode
    description: str
    watched_nodes: tuple[om.MObject, ...]
    curves: tuple[om.MObject, ...]
    inputs: tuple[om.MPlug, ...]
    layers: tuple[om.MObject, ...]
    target_layer: str | None


def connected_plug_watch_nodes(plug: om.MPlug) -> tuple[om.MObject, ...]:
    """編集不可でも接続元と正規レイヤーの変更を監視できるようにする。"""
    pending = [plug]
    nodes: list[om.MObject] = []
    layered = False
    while pending:
        source = pending.pop().sourceWithConversion()
        if source.isNull or source.node() in nodes:
            continue
        node = source.node()
        nodes.append(node)
        fn = om.MFnDependencyNode(node)
        if fn.typeName.startswith("animBlendNode"):
            layered = True
            nodes.extend(_layer_owners(node))
            try:
                pending.extend(_blend_inputs(source))
            except RuntimeError:
                continue
        elif node.hasFn(om.MFn.kAnimCurve):
            driver = fn.findPlug("input", False).sourceWithConversion()
            if not driver.isNull:
                nodes.append(driver.node())
            elif cmds.objExists("time1"):
                nodes.append(om.MSelectionList().add("time1").getDependNode(0))
    if layered:
        root = cmds.animLayer(query=True, root=True)
        if isinstance(root, str) and root:
            nodes.append(om.MSelectionList().add(root).getDependNode(0))
    return _unique(nodes)


def inspect_connected_plug(plug: om.MPlug) -> ConnectedPlugEditInfo:
    """直結時間・SDK・正規レイヤーを許可し、その他は理由付きで拒否する。"""
    _check_plug(plug)
    source = plug.sourceWithConversion()
    if source.isNull:
        raise RuntimeError("入力接続がありません")
    layered = om.MFnDependencyNode(source.node()).typeName.startswith(
        "animBlendNode"
    )
    pending = [plug]
    visited: list[om.MPlug] = []
    curves: list[om.MObject] = []
    layers: list[om.MObject] = []
    inputs: list[om.MPlug] = []
    mode: _Mode = "layer" if layered else "time"
    while pending:
        destination = pending.pop()
        if destination in visited:
            continue
        visited.append(destination)
        source = destination.sourceWithConversion()
        if destination != plug:
            inputs.append(destination)
        if source.isNull:
            continue
        node = source.node()
        fn = om.MFnDependencyNode(node)
        if node.hasFn(om.MFn.kConstraint):
            raise RuntimeError(
                "コンストレイントで駆動する属性は入力できません"
            )
        if node.hasFn(om.MFn.kAnimCurve):
            curve = _check_curve(source, destination, layered=layered)
            curves.append(node)
            if not layered and not curve.isTimeInput:
                mode = "driven"
            continue
        if fn.typeName.startswith("animBlendNode") and layered:
            owners = _layer_owners(node)
            if not owners:
                raise RuntimeError("Animation Layerに属さない合成接続です")
            if fn.isLocked or fn.isFromReferencedFile:
                raise RuntimeError(
                    "レイヤーの合成ノードがロックまたは参照されています"
                )
            _check_blend(node, owners, plug)
            layers.extend(owners)
            pending.extend(_blend_inputs(source))
            continue
        raise RuntimeError(f"{fn.typeName}を介する入力接続は編集対象外です")

    target_layer: str | None = None
    auto_label = "ON" if cmds.autoKeyframe(query=True, state=True) else "OFF"
    if layered:
        root = cmds.animLayer(query=True, root=True)
        if isinstance(root, str) and root:
            layers.append(om.MSelectionList().add(root).getDependNode(0))
        best = cmds.animLayer(_path(plug), query=True, bestLayer=True)
        target_layer = best if isinstance(best, str) and best else None
        if target_layer:
            layer_node = om.MFnDependencyNode(
                om.MSelectionList().add(target_layer).getDependNode(0)
            )
            if layer_node.isLocked or layer_node.isFromReferencedFile:
                raise RuntimeError(
                    "対象レイヤーがロックまたは参照されています"
                )
        description = (
            f"Animation Layer: {target_layer or 'キー設定先なし'}。"
            f"Auto Key: {auto_label}。OFF時は一時値です。"
            "ロック時はMayaが別レイヤーを選び、ウェイトやミュートで出力が変わります"
        )
    elif mode == "driven":
        description = (
            "Driven Keyの一時値です。再評価で戻ります。SDKのキーは変更しません"
        )
    else:
        description = f"Auto Key: {auto_label}。OFF時は再評価で戻る一時値です"
    return ConnectedPlugEditInfo(
        mode,
        description,
        _unique(list(connected_plug_watch_nodes(plug)) + layers),
        _unique(curves),
        tuple(inputs),
        _unique(layers),
        target_layer,
    )


@dataclass(frozen=True)
class _Key:
    """Maya commandの単位でキー値・接線・補助情報を保存する。"""

    position: float
    value: float
    in_type: str
    out_type: str
    in_angle: float
    out_angle: float
    in_weight: float
    out_weight: float
    tangent_lock: bool
    weight_lock: bool
    breakdown: bool


def _key_query(name: str, flag: str) -> list[object]:
    """キー数によらず一回のqueryで接線情報をまとめて読む。"""
    return cast(
        list[object],
        cast(Callable[..., object], cmds.keyTangent)(
            name, query=True, **{flag: True}
        )
        or [],
    )


@dataclass(frozen=True)
class _CurveState:
    """対象経路のカーブだけを、接線を含めて保存する。"""

    handle: om.MObjectHandle
    weighted: bool
    keys: tuple[_Key, ...]

    @classmethod
    def capture(cls, node: om.MObject) -> _CurveState:
        """検証と失敗復旧に必要なキー情報を読み取る。"""
        curve = oma.MFnAnimCurve(node)
        name = curve.name()
        positions = cast(
            list[float],
            (
                cmds.keyframe(name, query=True, timeChange=True)
                if curve.isTimeInput
                else cmds.keyframe(name, query=True, floatChange=True)
            )
            or [],
        )
        values = cast(
            list[float],
            cmds.keyframe(name, query=True, valueChange=True) or [],
        )
        tangent_flags = (
            "inTangentType",
            "outTangentType",
            "inAngle",
            "outAngle",
            "inWeight",
            "outWeight",
            "lock",
            "weightLock",
        )
        tangents = {flag: _key_query(name, flag) for flag in tangent_flags}
        keys = tuple(
            _Key(
                position,
                values[index],
                str(tangents["inTangentType"][index]),
                str(tangents["outTangentType"][index]),
                float(cast(float, tangents["inAngle"][index])),
                float(cast(float, tangents["outAngle"][index])),
                float(cast(float, tangents["inWeight"][index])),
                float(cast(float, tangents["outWeight"][index])),
                bool(tangents["lock"][index]),
                bool(tangents["weightLock"][index]),
                curve.isBreakdown(index),
            )
            for index, position in enumerate(positions)
        )
        return cls(om.MObjectHandle(node), curve.isWeighted, keys)

    def matches(self) -> bool:
        """同名で再作成されたノードを取り込まず全キーの変更を検出する。"""
        if not self.handle.isAlive() or not self.handle.isValid():
            return False
        current = self.capture(self.handle.object())
        return self.weighted == current.weighted and self.keys == current.keys

    def restore(self) -> None:
        """新規キーを除き、既存値と接線情報をUndo対応commandで戻す。"""
        if self.matches():
            return
        if not self.handle.isAlive() or not self.handle.isValid():
            raise RuntimeError("復旧対象のカーブが削除されました")
        curve = oma.MFnAnimCurve(self.handle.object())
        if not curve.isTimeInput:
            raise RuntimeError("入力中にSDKのキーが外部で変更されました")
        name = curve.name()
        positions = {key.position for key in self.keys}
        current = self.capture(curve.object())
        for key in reversed(current.keys):
            if key.position not in positions:
                cmds.cutKey(
                    name, time=(key.position, key.position), clear=True
                )
        for key in self.keys:
            time = (key.position, key.position)
            cmds.keyframe(
                name,
                edit=True,
                time=time,
                absolute=True,
                valueChange=key.value,
            )
            cmds.keyframe(name, edit=True, time=time, breakdown=key.breakdown)
        # 値復旧だけで戻る自動接線は再設定せず、手動情報の差だけを補う
        if self.matches():
            return
        cmds.keyTangent(name, edit=True, weightedTangents=self.weighted)
        for key in self.keys:
            time = (key.position, key.position)
            cmds.keyTangent(name, edit=True, time=time, lock=False)
            if self.weighted:
                cmds.keyTangent(name, edit=True, time=time, weightLock=False)
            cmds.keyTangent(
                name,
                edit=True,
                time=time,
                inAngle=key.in_angle,
                outAngle=key.out_angle,
            )
            if self.weighted:
                cmds.keyTangent(
                    name,
                    edit=True,
                    time=time,
                    inWeight=key.in_weight,
                    outWeight=key.out_weight,
                )
            cmds.keyTangent(
                name,
                edit=True,
                time=time,
                inTangentType=key.in_type,
                outTangentType=key.out_type,
                lock=key.tangent_lock,
            )
            if self.weighted:
                cmds.keyTangent(
                    name, edit=True, time=time, weightLock=key.weight_lock
                )
            cmds.keyframe(name, edit=True, time=time, breakdown=key.breakdown)


def _connections(info: ConnectedPlugEditInfo) -> tuple[tuple[str, str], ...]:
    """対象経路の全接続を固定し、同じ名前でも実体は別途検証する。"""
    result: list[tuple[str, str]] = []
    for node in info.watched_nodes:
        for destination in om.MFnDependencyNode(node).getConnections():
            if destination.isDestination:
                result.append(
                    (
                        destination.name(),
                        destination.sourceWithConversion().name(),
                    )
                )
    return tuple(sorted(result))


def _layer_state(
    info: ConnectedPlugEditInfo,
) -> tuple[tuple[_Scalar, ...], ...]:
    """キー設定先を左右するレイヤー状態を固定する。"""
    result = tuple(
        tuple(
            _scalar(om.MFnDependencyNode(node).findPlug(attribute, False))
            for attribute in (
                "lock",
                "mute",
                "solo",
                "selected",
                "preferred",
                "weight",
                "override",
            )
        )
        for node in info.layers
    )
    controls = tuple(
        tuple(
            _scalar(fn.findPlug(attribute, False))
            for attribute in (
                "weightA",
                "weightB",
                "rotationInterpolation",
                "rotationAccumulationMode",
                "scaleAccumulationMode",
                "accumulationMode",
                "rotateOrder",
            )
            if fn.hasAttribute(attribute)
        )
        for node in info.watched_nodes
        if (fn := om.MFnDependencyNode(node)).typeName.startswith(
            "animBlendNode"
        )
    )
    return result + controls


@dataclass
class ConnectedPlugWrite:
    """Maya標準のsetAttrと、そのキー・実入力・一時値の失敗復旧を保持する。"""

    plug: om.MPlug
    info: ConnectedPlugEditInfo
    requested: _Scalar
    before: _Scalar
    time: om.MTime
    units: tuple[int, int, int]
    auto_key: bool
    curves: tuple[_CurveState, ...]
    inputs: tuple[tuple[om.MPlug, _Scalar], ...]
    connections: tuple[tuple[str, str], ...]
    layers: tuple[tuple[_Scalar, ...], ...]
    applied: bool = False

    def _validate_context(self) -> None:
        """バッチ内の先行値編集を許し、接続・lock・編集設定を再検証する。"""
        current = inspect_connected_plug(self.plug)
        if (
            current.mode != self.info.mode
            or current.watched_nodes != self.info.watched_nodes
            or current.target_layer != self.info.target_layer
            or _connections(current) != self.connections
            or _layer_state(current) != self.layers
        ):
            raise RuntimeError(
                "入力中に接続またはAnimation Layerの状態が変わりました"
            )
        if (
            oma.MAnimControl.currentTime() != self.time
            or _units() != self.units
        ):
            raise RuntimeError("入力中に現在時刻または単位が変わりました")
        if bool(cmds.autoKeyframe(query=True, state=True)) != self.auto_key:
            raise RuntimeError("入力中にAuto Keyの状態が変わりました")

    def validate(self) -> None:
        """値・接続・キー・時刻・単位・Auto Key・対象レイヤーを再検証する。"""
        self._validate_context()
        if (
            _scalar(self.plug) != self.before
            or any(not curve.matches() for curve in self.curves)
            or any(_scalar(plug) != before for plug, before in self.inputs)
        ):
            raise RuntimeError("入力中に対象の値またはキーが変わりました")

    def apply(self, *, prevalidated: bool = False) -> None:
        """追加のキー操作や再評価を行わず、Maya標準の値入力を適用する。"""
        if prevalidated:
            self._validate_context()
        else:
            self.validate()
        self.applied = True
        _set(self.plug, self.requested)

    def restore(self) -> None:
        """Auto Keyの再発火を止め、対象経路と表示中の一時値を元へ戻す。"""
        if not self.applied:
            return
        auto_key = bool(cmds.autoKeyframe(query=True, state=True))
        try:
            if auto_key:
                cmds.autoKeyframe(state=False)
            for curve in self.curves:
                curve.restore()
            for plug, before in reversed(self.inputs):
                if (
                    plug.sourceWithConversion().isNull
                    and _scalar(plug) != before
                ):
                    _set(plug, before)
            _set(self.plug, self.before)
            self.applied = False
        finally:
            if auto_key:
                cmds.autoKeyframe(state=True)


def prepare_connected_plug_write(
    plug: om.MPlug, requested: _Scalar
) -> ConnectedPlugWrite:
    """Maya commandの現在単位で、値入力と対象経路だけの復旧情報を作る。"""
    if not math.isfinite(float(requested)):
        raise ValueError("入力値には有限数を指定してください")
    info = inspect_connected_plug(plug)
    return ConnectedPlugWrite(
        plug,
        info,
        requested,
        _scalar(plug),
        oma.MAnimControl.currentTime(),
        _units(),
        bool(cmds.autoKeyframe(query=True, state=True)),
        tuple(_CurveState.capture(node) for node in info.curves),
        tuple((item, _scalar(item)) for item in info.inputs),
        _connections(info),
        _layer_state(info),
    )
