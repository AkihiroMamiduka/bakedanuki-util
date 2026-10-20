# coding: utf-8
"""一括操作のenum検証範囲と、途中変更を検出した場合の復旧を固定する。"""

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util.maya.ui import (
    MayaEnumPlugsBinding,
    MayaEnumValueEdit,
    MayaFloatPlugsBinding,
    MayaFloatValueEdit,
    apply_plugs_values,
    resolve_enum_plug,
    resolve_float_plug,
)
from bd_util.maya.ui.binding._float_edit import FloatEditUndo
from bd_util.ui import qt


@pytest.fixture
def scene(new_scene):
    """独立したenum三つと、監視しないBindingの所有者を用意する。"""
    owner = qt.QObject()
    nodes = cmds.ls(
        [cmds.createNode("transform") for _ in range(3)], long=True
    )
    for node in nodes:
        cmds.addAttr(node, longName="mode", at="enum", enumName="A:B:C")
    cmds.undoInfo(state=True)
    yield nodes, owner
    owner.deleteLater()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    assert FloatEditUndo._active is None


def enum_binding(nodes, owner, attribute="mode"):
    """指定属性を、監視を登録しない一括編集用Bindingにまとめる。"""
    return MayaEnumPlugsBinding(
        [resolve_enum_plug(node, attribute) for node in nodes],
        parent=owner,
        monitor=False,
    )


def test_disposing_unchanged_enum_row_during_write_restores_other_rows(
    scene, monkeypatch
):
    """同値enum行のBinding終了も終了検証で拒否し、先行する数値を復旧する。"""
    nodes, owner = scene
    for node in nodes:
        cmds.addAttr(node, longName="amount", attributeType="double")
    unchanged = enum_binding(nodes, owner)
    numeric = MayaFloatPlugsBinding(
        [resolve_float_plug(node, "amount") for node in nodes],
        parent=owner,
        monitor=False,
    )
    original = cmds.setAttr

    def write(path, value):
        """最初の数値書込み後に別行の表示用Bindingを終了する。"""
        original(path, value)
        if path == nodes[0] + ".amount" and value == 2:
            unchanged.dispose()

    monkeypatch.setattr(cmds, "setAttr", write)
    try:
        with pytest.raises(RuntimeError, match="削除"):
            apply_plugs_values(
                [
                    MayaFloatValueEdit(numeric, 2.0),
                    MayaEnumValueEdit(unchanged, 0),
                ],
                enum_validation="operation",
            )
        assert values(nodes, "amount") == [0, 0, 0]
    finally:
        numeric.dispose()
        unchanged.dispose()


def values(nodes, attribute="mode"):
    """要求対象の値をMayaから読み直す。"""
    return [cmds.getAttr(f"{node}.{attribute}") for node in nodes]


def test_thousand_independent_enum_reads_are_linear_and_share_undo(
    new_scene, monkeypatch
):
    """千の独立enumを線形回数で照合し、全対象を一度でUndoとRedoする。"""
    count = 1000
    nodes = [cmds.createNode("network") for _ in range(count)]
    for node in nodes:
        cmds.addAttr(node, longName="mode", at="enum", enumName="A:B:C")
    binding = MayaEnumPlugsBinding(
        [resolve_enum_plug(node, "mode") for node in nodes], monitor=False
    )
    real_add_attr = cmds.addAttr
    reads = 0

    def counting_add_attr(*args, **kwargs):
        """定義queryの実回数を数え、二乗取得への回帰を早期に止める。"""
        nonlocal reads
        if (kwargs.get("query") or kwargs.get("q")) and (
            kwargs.get("enumName") or kwargs.get("en")
        ):
            reads += 1
            if reads > 30 * count:
                pytest.fail("独立enumの定義取得回数が線形上限を超えました")
        return real_add_attr(*args, **kwargs)

    try:
        cmds.flushUndo()
        with monkeypatch.context() as counting:
            counting.setattr(cmds, "addAttr", counting_add_attr)
            assert apply_plugs_values(
                [MayaEnumValueEdit(binding, 1)], enum_validation="operation"
            )
        assert count <= reads <= 30 * count
        assert values(nodes) == [1] * count
        cmds.undo()
        assert values(nodes) == [0] * count
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
        cmds.redo()
        assert values(nodes) == [1] * count
    finally:
        binding.dispose()
        binding.deleteLater()


@pytest.mark.parametrize(
    "case,trigger_index,changed_index,expected_forward",
    [
        ("not_yet_written", 0, 2, [0, 1]),
        ("already_written", 2, 1, [0, 1, 2]),
        ("locked", 0, 2, [0, 1]),
        ("same_value", 0, 2, [0, 1]),
        ("last_write", 2, 2, [0, 1, 2]),
    ],
)
def test_changed_definition_restores_all_writes_including_final_check(
    scene, monkeypatch, case, trigger_index, changed_index, expected_forward
):
    """未適用・適用済み・除外対象と最後の書込み後の定義変更を検出する。"""
    nodes, owner = scene
    if case == "locked":
        cmds.setAttr(nodes[2] + ".mode", lock=True)
    if case == "same_value":
        cmds.setAttr(nodes[2] + ".mode", 1)
    before = values(nodes)
    binding = enum_binding(nodes, owner)
    real_set_attr = cmds.setAttr
    forward = []
    restored = []

    def changing_set_attr(path, value):
        """指定の書込み直後に、操作自身が変更しない定義を差し替える。"""
        real_set_attr(path, value)
        if value == 1:
            forward.append(path)
            if path == nodes[trigger_index] + ".mode":
                cmds.addAttr(
                    nodes[changed_index] + ".mode",
                    edit=True,
                    enumName="A:Changed:C",
                )
        elif value == 0:
            restored.append(path)

    monkeypatch.setattr(cmds, "setAttr", changing_set_attr)
    with pytest.raises(ValueError, match="enum定義"):
        apply_plugs_values(
            [MayaEnumValueEdit(binding, 1)], enum_validation="operation"
        )
    assert forward == [nodes[index] + ".mode" for index in expected_forward]
    assert restored == list(reversed(forward))
    assert values(nodes) == before
    assert (
        cmds.addAttr(nodes[changed_index] + ".mode", query=True, enumName=True)
        == "A:Changed:C"
    )


@pytest.mark.parametrize("policy", ["per_write", "operation"])
def test_definition_and_connection_changes_reject_and_restore_prior_writes(
    scene, monkeypatch, policy
):
    """同じ未適用対象の定義と接続が変わっても拒否し、先行する値を復旧する。"""
    nodes, owner = scene
    source = cmds.createNode("network")
    cmds.addAttr(source, longName="mode", at="enum", enumName="A:B:C")
    binding = enum_binding(nodes, owner)
    original = cmds.setAttr
    forward = []

    def changing_set_attr(path, value):
        """初回適用後に対象の定義と入力接続を変更し、外部変更を保持する。"""
        original(path, value)
        if value == 1:
            forward.append(path)
        if path == nodes[0] + ".mode" and value == 1:
            cmds.addAttr(
                nodes[-1] + ".mode", edit=True, enumName="A:Changed:C"
            )
            cmds.connectAttr(source + ".mode", nodes[-1] + ".mode")

    try:
        with monkeypatch.context() as changing:
            changing.setattr(cmds, "setAttr", changing_set_attr)
            with pytest.raises(
                (ValueError, RuntimeError), match="enum定義|接続|状態"
            ):
                apply_plugs_values(
                    [MayaEnumValueEdit(binding, 1)], enum_validation=policy
                )
        assert forward and nodes[-1] + ".mode" not in forward
        assert values(nodes) == [0, 0, 0]
        assert cmds.isConnected(source + ".mode", nodes[-1] + ".mode")
        assert (
            cmds.addAttr(nodes[-1] + ".mode", query=True, enumName=True)
            == "A:Changed:C"
        )
        # 例外後もchunkを閉じ、次の別操作だけを通常のUndoで戻せる
        cmds.setAttr(nodes[0] + ".tx", 7)
        cmds.undo()
        assert cmds.getAttr(nodes[0] + ".tx") == 0
        assert values(nodes) == [0, 0, 0]
    finally:
        binding.dispose()


def test_final_check_includes_another_entirely_unchanged_row(
    scene, monkeypatch
):
    """全対象が同値で書込み計画のない別行も、終了時の定義照合に含める。"""
    nodes, owner = scene
    for node in nodes:
        cmds.addAttr(node, longName="other", at="enum", enumName="A:B:C")
        cmds.setAttr(node + ".other", 1)
    binding = enum_binding(nodes, owner)
    other = enum_binding(nodes, owner, "other")
    real_set_attr = cmds.setAttr

    def changing_set_attr(path, value):
        """先の行の書込みから、後の無変更行の非基準定義を変更する。"""
        real_set_attr(path, value)
        if path == nodes[0] + ".mode" and value == 1:
            cmds.addAttr(
                nodes[2] + ".other", edit=True, enumName="A:Changed:C"
            )

    monkeypatch.setattr(cmds, "setAttr", changing_set_attr)
    with pytest.raises(ValueError, match="enum定義"):
        apply_plugs_values(
            [MayaEnumValueEdit(binding, 1), MayaEnumValueEdit(other, 1)],
            enum_validation="operation",
        )
    assert values(nodes) == [0, 0, 0]
    assert values(nodes, "other") == [1, 1, 1]


def test_uniform_definition_change_is_compared_with_start_snapshot(
    scene, monkeypatch
):
    """全員の定義が同じ内容へ変化しても、操作開始時との不一致で拒否する。"""
    nodes, owner = scene
    binding = enum_binding(nodes, owner)
    real_set_attr = cmds.setAttr
    forward = []

    def changing_set_attr(path, value):
        """初回書込みで全対象の項目名を同じ内容へ差し替える。"""
        real_set_attr(path, value)
        if value == 1:
            forward.append(path)
            if len(forward) == 1:
                for node in nodes:
                    cmds.addAttr(
                        node + ".mode", edit=True, enumName="A:Changed:C"
                    )

    monkeypatch.setattr(cmds, "setAttr", changing_set_attr)
    with pytest.raises(ValueError, match="enum定義"):
        apply_plugs_values(
            [MayaEnumValueEdit(binding, 1)], enum_validation="operation"
        )
    assert forward == [nodes[0] + ".mode"]
    assert values(nodes) == [0, 0, 0]


@pytest.mark.parametrize("all_enum_same", [False, True])
def test_float_write_changes_enum_and_is_restored_without_enum_writes(
    scene, monkeypatch, all_enum_same
):
    """float先行中にenum基準が変化したら、enum未適用でもfloatを復旧する。"""
    nodes, owner = scene
    binding = enum_binding(nodes, owner)
    distance = MayaFloatPlugsBinding(
        [resolve_float_plug(node, "tx") for node in nodes],
        parent=owner,
        monitor=False,
    )
    real_set_attr = cmds.setAttr
    enum_writes = []

    def changing_set_attr(path, value):
        """先行floatの初回適用時に、後続enumの基準定義を変更する。"""
        if path.endswith(".mode"):
            enum_writes.append(path)
        real_set_attr(path, value)
        if (
            path.startswith(nodes[0] + ".")
            and path.endswith(".translateX")
            and value == 6
        ):
            cmds.addAttr(nodes[0] + ".mode", edit=True, enumName="A:Changed:C")

    monkeypatch.setattr(cmds, "setAttr", changing_set_attr)
    with pytest.raises(ValueError, match="enum定義"):
        apply_plugs_values(
            [
                MayaFloatValueEdit(distance, 6),
                MayaEnumValueEdit(binding, 0 if all_enum_same else 1),
            ],
            enum_validation="operation",
        )
    assert not enum_writes
    assert values(nodes) == [0, 0, 0]
    assert values(nodes, "tx") == [0, 0, 0]


def ambiguous_enum_nodes():
    """同じraw文字列から異なる整数割当を作れるenumを三つ用意する。"""
    nodes = [cmds.createNode("network") for _ in range(3)]
    for node in nodes:
        selection = om.MSelectionList()
        selection.add(node)
        attribute = om.MFnEnumAttribute()
        attribute_object = attribute.create("mode", "md", 0)
        attribute.addField("A", 0)
        attribute.addField("X=9", 1)
        attribute.addField("Z", 20)
        om.MFnDependencyNode(selection.getDependNode(0)).addAttribute(
            attribute_object
        )
    assert all(
        cmds.addAttr(node + ".mode", query=True, enumName=True) == "A:X=9:Z=20"
        for node in nodes
    )
    return nodes


@pytest.mark.parametrize("all_changed", [False, True])
def test_start_snapshot_reparses_unchanged_raw_with_new_integer_mapping(
    new_scene, all_changed
):
    """rawが不変でも開始時に全員の最新割当を読み、旧cacheを再利用しない。"""
    nodes = ambiguous_enum_nodes()
    binding = MayaEnumPlugsBinding(
        [resolve_enum_plug(node, "mode") for node in nodes], monitor=False
    )
    try:
        assert binding.definition.item_for_value(1).name == "X=9"
        for node in nodes if all_changed else nodes[-1:]:
            cmds.addAttr(node + ".mode", edit=True, enumName="A:X=9:Z=20")
        if not all_changed:
            with pytest.raises(ValueError, match="enum定義"):
                apply_plugs_values(
                    [MayaEnumValueEdit(binding, 20)],
                    enum_validation="operation",
                )
            assert values(nodes) == [0, 0, 0]
            return
        assert apply_plugs_values(
            [MayaEnumValueEdit(binding, 9)], enum_validation="operation"
        )
        assert values(nodes) == [9, 9, 9]
        assert binding.definition.item_for_value(9).name == "X"
        assert binding.definition.item_for_value(1) is None
    finally:
        binding.dispose()
        binding.deleteLater()


def test_final_snapshot_reparses_unchanged_raw_with_new_integer_mapping(
    new_scene, monkeypatch
):
    """最後の書込み後もraw一致を信用せず、同じ署名の割当変更を検出する。"""
    nodes = ambiguous_enum_nodes()
    binding = MayaEnumPlugsBinding(
        [resolve_enum_plug(node, "mode") for node in nodes], monitor=False
    )
    real_set_attr = cmds.setAttr

    def changing_set_attr(path, value):
        """最後の適用直後に、既適用の非基準属性の整数割当を変更する。"""
        real_set_attr(path, value)
        if path == nodes[-1] + ".mode" and value == 20:
            cmds.addAttr(nodes[1] + ".mode", edit=True, enumName="A:X=9:Z=20")

    try:
        monkeypatch.setattr(cmds, "setAttr", changing_set_attr)
        with pytest.raises(ValueError, match="enum定義"):
            apply_plugs_values(
                [MayaEnumValueEdit(binding, 20)], enum_validation="operation"
            )
        assert values(nodes) == [0, 0, 0]
        assert (
            cmds.addAttr(nodes[1] + ".mode", query=True, enumName=True)
            == "A:X=9:Z=20"
        )
    finally:
        binding.dispose()
        binding.deleteLater()


@pytest.mark.parametrize("first_fails", [False, True])
@pytest.mark.parametrize("direct_binding", [False, True])
def test_operation_policy_does_not_leak_after_success_or_failure(
    scene, monkeypatch, first_fails, direct_binding
):
    """成功と例外のどちらの終了後も、通常入力は毎回全対象を確認する。"""
    nodes, owner = scene
    binding = enum_binding(nodes, owner)
    real_set_attr = cmds.setAttr

    def failing_set_attr(path, value):
        """操作contextから例外で抜ける経路を作る。"""
        real_set_attr(path, value)
        if value == 1:
            raise RuntimeError("operation write failed")

    if first_fails:
        with monkeypatch.context() as failing:
            failing.setattr(cmds, "setAttr", failing_set_attr)
            with pytest.raises(RuntimeError, match="operation write failed"):
                apply_plugs_values(
                    [MayaEnumValueEdit(binding, 1)],
                    enum_validation="operation",
                )
    else:
        assert apply_plugs_values(
            [MayaEnumValueEdit(binding, 1)], enum_validation="operation"
        )
    before = values(nodes)
    forward = []

    def changing_set_attr(path, value):
        """次の入力で、当該対象以外の不一致を直後に検出できるか確認する。"""
        real_set_attr(path, value)
        if value == 2:
            forward.append(path)
            if path == nodes[0] + ".mode":
                cmds.addAttr(
                    nodes[2] + ".mode", edit=True, enumName="A:B:Changed"
                )

    monkeypatch.setattr(cmds, "setAttr", changing_set_attr)
    with pytest.raises(ValueError, match="enum定義"):
        if direct_binding:
            binding.set_value(2)
        else:
            apply_plugs_values([MayaEnumValueEdit(binding, 2)])
    assert forward == [nodes[0] + ".mode"]
    assert values(nodes) == before


def test_final_validation_failure_reports_failed_restore_and_closes_chunk(
    scene, monkeypatch
):
    """終了検証の不一致と復旧失敗を併記し、他の復旧とchunk終了を続ける。"""
    nodes, owner = scene
    binding = enum_binding(nodes, owner)
    real_set_attr = cmds.setAttr
    restored = []

    def changing_set_attr(path, value):
        """最後に定義を変え、逆順復旧の途中一件だけを失敗させる。"""
        if value == 0:
            restored.append(path)
            if path == nodes[1] + ".mode":
                raise RuntimeError("restore failed")
        real_set_attr(path, value)
        if path == nodes[2] + ".mode" and value == 1:
            cmds.addAttr(nodes[2] + ".mode", edit=True, enumName="A:Changed:C")

    with monkeypatch.context() as changing:
        changing.setattr(cmds, "setAttr", changing_set_attr)
        with pytest.raises(ExceptionGroup) as captured:
            apply_plugs_values(
                [MayaEnumValueEdit(binding, 1)], enum_validation="operation"
            )
    errors = [str(error) for error in captured.value.exceptions]
    assert any("enum定義" in error for error in errors)
    assert any("restore failed" in error for error in errors)
    assert restored == [node + ".mode" for node in reversed(nodes)]
    assert values(nodes) == [0, 1, 0]
    cmds.setAttr(nodes[0] + ".ty", 7)
    cmds.undo()
    assert cmds.getAttr(nodes[0] + ".ty") == 0
    assert values(nodes) == [0, 1, 0]


def test_refresh_failure_preserves_restore_errors_and_syncs_later_stores(
    scene, monkeypatch
):
    """再同期で読めない定義も元の復旧失敗を隠さず、他の行の同期を続ける。"""
    nodes, owner = scene
    binding = enum_binding(nodes, owner)
    distance = MayaFloatPlugsBinding(
        [resolve_float_plug(node, "tx") for node in nodes],
        parent=owner,
        monitor=False,
    )
    enum_failures = []
    float_failures = []
    binding.edit_failed.connect(enum_failures.append)
    distance.edit_failed.connect(float_failures.append)
    real_set_attr = cmds.setAttr
    real_refresh = distance.store.refresh
    refreshes = []
    definition_changed = False

    def counting_refresh():
        """先のStoreの再同期失敗後も後続Storeへ到達したことを記録する。"""
        refreshes.append(True)
        return real_refresh()

    def changing_set_attr(path, value):
        """最終enumへ区切り文字を含む項目を追加し、復旧一件も失敗させる。"""
        nonlocal definition_changed
        if definition_changed and path == nodes[1] + ".mode" and value == 0:
            raise RuntimeError("restore failed")
        real_set_attr(path, value)
        if path == nodes[2] + ".mode" and value == 1:
            attribute = resolve_enum_plug(nodes[2], "mode").plug.attribute()
            om.MFnEnumAttribute(attribute).addField("Changed:Colon", 3)
            definition_changed = True

    def leaf_messages(error):
        """階層化されたExceptionGroupから元の各失敗を取り出す。"""
        if isinstance(error, ExceptionGroup):
            return [
                message
                for child in error.exceptions
                for message in leaf_messages(child)
            ]
        return [str(error)]

    monkeypatch.setattr(cmds, "setAttr", changing_set_attr)
    monkeypatch.setattr(distance.store, "refresh", counting_refresh)
    with pytest.raises(ExceptionGroup) as captured:
        apply_plugs_values(
            [MayaEnumValueEdit(binding, 1), MayaFloatValueEdit(distance, 6)],
            enum_validation="operation",
        )
    messages = leaf_messages(captured.value)
    assert any("restore failed" in message for message in messages)
    assert (
        sum("enum定義を解決できません" in message for message in messages) == 2
    )
    assert values(nodes) == [0, 1, 0]
    assert values(nodes, "tx") == [0, 0, 0]
    assert refreshes == [True]
    assert len(enum_failures) == len(float_failures) == 1


@pytest.mark.parametrize(
    "target_kind", ["pending", "locked", "same_value", "representative"]
)
def test_disappearing_target_never_retargets_same_named_replacement(
    scene, monkeypatch, target_kind
):
    """開始後の削除と同名再作成で古い対象を追従させず、他の値を復旧する。"""
    nodes, owner = scene
    if target_kind == "locked":
        cmds.setAttr(nodes[2] + ".mode", lock=True)
    if target_kind == "same_value":
        cmds.setAttr(nodes[2] + ".mode", 1)
    binding = enum_binding(nodes, owner)
    real_set_attr = cmds.setAttr
    deleted_index = 0 if target_kind == "representative" else 2
    replacement = None

    def deleting_set_attr(path, value):
        """初回適用後に基準または未適用対象を同名の別実体へ置き換える。"""
        nonlocal replacement
        real_set_attr(path, value)
        if path == nodes[0] + ".mode" and value == 1:
            cmds.delete(nodes[deleted_index])
            replacement = cmds.createNode(
                "transform", name=nodes[deleted_index].rsplit("|", 1)[-1]
            )
            cmds.addAttr(
                replacement, longName="mode", at="enum", enumName="A:B:C"
            )
            replacement = cmds.ls(replacement, long=True)[0]

    monkeypatch.setattr(cmds, "setAttr", deleting_set_attr)
    with pytest.raises((RuntimeError, ValueError, ExceptionGroup)):
        apply_plugs_values(
            [MayaEnumValueEdit(binding, 1)], enum_validation="operation"
        )
    assert replacement == nodes[deleted_index]
    assert values(nodes) == [0, 0, 0]
    assert not binding.target_states[deleted_index].is_available


@pytest.mark.parametrize("invalid", ["invalid", None, True])
def test_invalid_policy_is_rejected_even_for_empty_request(invalid):
    """未知の検証方式は空の編集要求でも黙って受理しない。"""
    with pytest.raises(ValueError):
        apply_plugs_values([], enum_validation=invalid)
