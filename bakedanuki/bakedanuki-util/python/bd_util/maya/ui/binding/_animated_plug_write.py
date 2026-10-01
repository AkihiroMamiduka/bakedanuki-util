# coding: utf-8
"""直接接続の時間カーブを、Maya標準Undoで値入力へ接続する。"""

from __future__ import annotations

import math
from dataclasses import dataclass

from maya import cmds
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ...node.operator.attr import _keyframe_target


def _curve(plug: om.MPlug) -> oma.MFnAnimCurve:
    """対応する接続と編集可能性を検証して直接カーブを返す。"""
    attribute = plug.attribute()
    if plug.isArray or plug.isCompound:
        raise RuntimeError("配列または複合属性のキー入力には対応していません")
    if not (
        attribute.hasFn(om.MFn.kNumericAttribute)
        or attribute.hasFn(om.MFn.kEnumAttribute)
        or attribute.hasFn(om.MFn.kUnitAttribute)
    ):
        raise RuntimeError("数値・角度・距離・bool・enum属性だけ編集できます")
    if (
        attribute.hasFn(om.MFn.kUnitAttribute)
        and om.MFnUnitAttribute(attribute).unitType()
        == om.MFnUnitAttribute.kTime
    ):
        raise RuntimeError("時間属性のキー入力には対応していません")
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

    # 変換・合成・Driven Keyを介する接続へは踏み込まない
    source = plug.sourceWithConversion()
    if source.isNull or not source.node().hasFn(om.MFn.kAnimCurve):
        raise RuntimeError("時間カーブの直接接続だけキー入力できます")
    curve = oma.MFnAnimCurve(source.node())
    if (
        not curve.isTimeInput
        or curve.animCurveType != curve.timedAnimCurveTypeForPlug(plug)
        or source != curve.findPlug("output", False)
    ):
        raise RuntimeError("属性と同じ型の時間カーブだけキー入力できます")
    if len(source.connectedTo(False, True)) != 1:
        raise RuntimeError("複数属性で共有するカーブは編集できません")
    if not curve.numKeys:
        raise RuntimeError("キーのない空カーブは編集できません")
    if (
        curve.animCurveType == oma.MFnAnimCurve.kAnimCurveTA
        and curve.findPlug("rotationInterpolation", False).asInt() != 1
    ):
        raise RuntimeError("独立した回転カーブだけキー入力できます")

    # 独自の時間変換と外部入力で駆動されるカーブ設定を除外する
    input_plug = curve.findPlug("input", False)
    for connection in curve.getConnections():
        if not connection.isDestination:
            continue
        if connection.attribute().hasFn(om.MFn.kMessageAttribute):
            continue
        if connection != input_plug:
            raise RuntimeError("カーブの設定に入力接続があります")
        driver = connection.sourceWithConversion()
        node = om.MFnDependencyNode(driver.node())
        if (
            node.typeName != "time"
            or om.MFnAttribute(driver.attribute()).name != "outTime"
            or node.findPlug("enableTimewarp", False).asBool()
        ):
            raise RuntimeError("独自の時間入力を持つカーブは編集できません")
    try:
        _keyframe_target.check_key_editable_curve(curve)
    except RuntimeError as error:
        raise RuntimeError("カーブがロックまたは参照されています") from error
    return curve


def animation_edit_reason(plug: om.MPlug) -> str | None:
    """キー入力できない理由を返し、対応する直接接続ならNoneを返す。"""
    try:
        _curve(plug)
    except RuntimeError as error:
        return str(error)
    return None


def _units() -> tuple[int, int, int]:
    """事前検証後の時間・角度・距離の単位変更を検出する。"""
    return om.MTime.uiUnit(), om.MAngle.uiUnit(), om.MDistance.uiUnit()


def _command_value(curve_type: int, value: float) -> float:
    """内部カーブ値をMaya commandの現在単位へ変換する。"""
    if curve_type == oma.MFnAnimCurve.kAnimCurveTA:
        return om.MAngle(value, om.MAngle.kRadians).asUnits(om.MAngle.uiUnit())
    if curve_type == oma.MFnAnimCurve.kAnimCurveTL:
        return om.MDistance(value, om.MDistance.kCentimeters).asUnits(
            om.MDistance.uiUnit()
        )
    return value


@dataclass
class AnimatedPlugWrite:
    """同じ属性・カーブ・時刻へ適用する、復旧可能なキー値入力。"""

    plug: om.MPlug
    curve_handle: om.MObjectHandle
    time: om.MTime
    units: tuple[int, int, int]
    value: float
    before: float | None
    key_count: int
    stepped: bool
    applied: bool = False

    def _live_curve(self) -> oma.MFnAnimCurve:
        """同名で再作成されたカーブへ操作を移さず元の実体を返す。"""
        if not self.curve_handle.isValid() or not self.curve_handle.isAlive():
            raise RuntimeError("入力対象のカーブが削除されました")
        curve = oma.MFnAnimCurve(self.curve_handle.object())
        if self.plug.sourceWithConversion() != curve.findPlug("output", False):
            raise RuntimeError("入力中にアニメーション接続が変わりました")
        return curve

    def validate(self) -> None:
        """接続・lock・時刻・単位・対象キーを実書込み直前に再検証する。"""
        curve = _curve(self.plug)
        if curve.object() != self.curve_handle.object():
            raise RuntimeError("入力中にアニメーション接続が変わりました")
        if oma.MAnimControl.currentTime() != self.time:
            raise RuntimeError("入力中に現在時刻が変わりました")
        if _units() != self.units:
            raise RuntimeError("入力中にMayaの単位が変わりました")
        index = curve.find(self.time)
        before = None if index is None else float(curve.value(index))
        if before != self.before or curve.numKeys != self.key_count:
            raise RuntimeError("入力中に対象カーブのキーが変わりました")

    def apply(self) -> None:
        """既存キーの情報を維持し、必要な時刻だけ新規キーを作成する。"""
        self.validate()
        curve = self._live_curve()
        frame = self.time.asUnits(om.MTime.uiUnit())
        value = _command_value(curve.animCurveType, self.value)
        self.applied = True
        if self.before is not None:
            cmds.keyframe(
                curve.name(),
                edit=True,
                animation="objects",
                time=(frame, frame),
                absolute=True,
                valueChange=value,
            )
        elif self.stepped:
            cmds.setKeyframe(
                curve.name(),
                time=frame,
                value=value,
                dirtyDG=True,
                insertBlend=False,
                outTangentType="step",
            )
        else:
            cmds.setKeyframe(
                curve.name(),
                time=frame,
                value=value,
                dirtyDG=True,
                insertBlend=False,
            )
        self._dirty(curve)
        index = curve.find(self.time)
        if index is None or not math.isclose(
            float(curve.value(index)), self.value, rel_tol=1e-12, abs_tol=1e-12
        ):
            raise RuntimeError("Mayaがキーの値入力を拒否しました")

    def restore(self) -> None:
        """既存キーの値を戻すか新規キーだけ除き、直後の評価を更新する。"""
        if not self.applied:
            return
        curve = self._live_curve()
        index = curve.find(self.time)
        frame = self.time.asUnits(om.MTime.uiUnit())
        if self.before is None:
            if index is not None:
                cmds.cutKey(
                    curve.name(),
                    animation="objects",
                    time=(frame, frame),
                    clear=True,
                )
        elif index is None:
            raise RuntimeError("復旧対象の既存キーが削除されました")
        elif float(curve.value(index)) != self.before:
            cmds.keyframe(
                curve.name(),
                edit=True,
                animation="objects",
                time=(frame, frame),
                absolute=True,
                valueChange=_command_value(curve.animCurveType, self.before),
            )
        self._dirty(curve)
        self.applied = False

    @staticmethod
    def _dirty(curve: oma.MFnAnimCurve) -> None:
        """現在時刻を移動せず、対象カーブから下流の評価を無効化する。"""
        cmds.dgdirty(curve.name() + ".output", propagation=True)


def prepare_animated_plug_write(
    plug: om.MPlug, value: float | bool | int
) -> AnimatedPlugWrite:
    """公開単位の値から、現在時刻に固定したキー入力を事前構築する。"""
    curve = _curve(plug)
    requested = float(value)
    if not math.isfinite(requested):
        raise ValueError("キーの入力値には有限数を指定してください")
    if curve.animCurveType == oma.MFnAnimCurve.kAnimCurveTA:
        requested = math.radians(requested)
    time = oma.MAnimControl.currentTime()
    index = curve.find(time)
    attribute = plug.attribute()
    stepped = attribute.hasFn(om.MFn.kEnumAttribute) or (
        attribute.hasFn(om.MFn.kNumericAttribute)
        and om.MFnNumericAttribute(attribute).numericType()
        == om.MFnNumericData.kBoolean
    )
    return AnimatedPlugWrite(
        plug,
        om.MObjectHandle(curve.object()),
        time,
        _units(),
        requested,
        None if index is None else float(curve.value(index)),
        curve.numKeys,
        stepped,
    )
