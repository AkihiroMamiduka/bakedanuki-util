from __future__ import annotations

import json

import pytest

import bd_util as bdu
from test_animation_clip import _layer, _node, _values

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _state(cmds):
    return (
        sorted(cmds.ls()),
        cmds.file(query=True, modified=True),
        cmds.currentTime(query=True),
        cmds.ls(selection=True),
        cmds.undoInfo(query=True, undoName=True),
        cmds.undoInfo(query=True, redoName=True),
    )


@pytest.mark.parametrize("mode", ["flatten", "preserve"])
@pytest.mark.parametrize("attr", ["tx", "rx", "sx"])
def test_file_roundtrip_preserves_data_and_scene(
    maya_cmds, tmp_path, mode, attr
):
    cmds = maya_cmds
    node = _node(cmds, "source", ((-2.5, 1), (1.25, 3), (4.5, 2)), attr=attr)
    cmds.keyTangent(node, edit=True, weightedTangents=True)
    cmds.keyTangent(
        node, edit=True, inTangentType="fixed", outTangentType="fixed"
    )
    cmds.keyframe(node, edit=True, time=(1.25, 1.25), breakdown=True)
    if mode == "preserve":
        layer = _layer(cmds, node, weight=0.5)
        cmds.setKeyframe(layer + ".weight", time=1, value=0.25)
        cmds.setKeyframe(layer + ".weight", time=5, value=0.75)
    clip = bdu.AnimationClip.capture(
        [node], attributes=[attr, "tx"], layer_mode=mode
    )
    before = clip.to_dict()
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    nodes.create.transform(name="pending")
    cmds.file(modified=False)
    scene = _state(cmds)
    path = clip.save(tmp_path / "アニメーション" / "歩き.json")
    loaded = bdu.AnimationClip.load(str(path))
    assert loaded == clip
    assert loaded is not clip
    assert _state(cmds) == scene
    assert not cmds.objExists("pending")
    assert not mod.can_undo
    assert json.loads(path.read_text(encoding="utf-8")) == json.loads(
        clip.to_json()
    )
    assert (
        bdu.AnimationClip.from_json(path.read_text(encoding="utf-8")) == clip
    )
    loaded.nodes[0].channels[0].curve.keys[0].value = 99
    assert clip.to_dict() == before
    assert bdu.AnimationClip.load(path) == clip
    mod.do_it_dag()
    assert cmds.objExists("pending")


@pytest.mark.parametrize("mode", ["flatten", "preserve"])
def test_loaded_clip_restores_after_source_deletion(maya_cmds, tmp_path, mode):
    cmds = maya_cmds
    node = _node(cmds, "source")
    if mode == "preserve":
        _layer(cmds, node, weight=0.5)
    expected = _values(cmds, node + ".tx")
    clip = bdu.AnimationClip.capture(
        [node], attributes=["tx"], layer_mode=mode
    )
    path = clip.save(tmp_path / "data.json")
    cmds.file(new=True, force=True)
    loaded = bdu.AnimationClip.load(path)
    assert not cmds.objExists(node)
    target = _node(cmds, "target", ())
    mod = bdu.ModifierManager()
    loaded.restore(mod, targets=[target], mode="replace_all")
    assert not cmds.keyframe(target + ".tx", query=True)
    mod.do_it_dg()
    assert _values(cmds, target + ".tx") == pytest.approx(expected)
    mod.undo_it()
    assert not cmds.keyframe(target + ".tx", query=True)
    mod.redo_it()
    assert _values(cmds, target + ".tx") == pytest.approx(expected)


def test_save_options_and_external_json(maya_cmds, tmp_path):
    node = _node(maya_cmds, "source")
    clip = bdu.AnimationClip.capture([node])
    path = tmp_path / "missing" / "data.json"
    with pytest.raises(FileNotFoundError):
        clip.save(path, create_parents=False)
    assert not path.parent.exists()
    assert clip.save(str(path), indent=None, overwrite=False) == path
    assert "\n" not in path.read_text(encoding="utf-8")
    before = path.read_bytes()
    with pytest.raises(FileExistsError):
        clip.save(path, overwrite=False)
    assert path.read_bytes() == before
    clip.save(path, indent=4, create_parents=False)
    assert "\n" in path.read_text(encoding="utf-8")
    path.write_text(clip.to_json(), encoding="utf-8-sig")
    assert bdu.AnimationClip.load(path) == clip


@pytest.mark.parametrize("value", [{}, None, {"schema_version": 1}])
def test_invalid_clip_schema_is_not_loaded(maya_cmds, tmp_path, value):
    path = bdu.json_file.write(tmp_path / "data.json", value)
    before = _state(maya_cmds)
    with pytest.raises((ValueError, TypeError)):
        bdu.AnimationClip.load(path)
    assert _state(maya_cmds) == before


@pytest.mark.parametrize(
    "field,value",
    [
        ("schema_version", 1),
        ("schema_version", True),
        ("seconds_per_frame", 0),
        ("clipped", "yes"),
        ("layer_mode", "invalid"),
    ],
)
def test_load_valid_json_with_invalid_clip_data(
    maya_cmds, tmp_path, field, value
):
    node = _node(maya_cmds, "source")
    data = bdu.AnimationClip.capture([node]).to_dict()
    data[field] = value
    path = bdu.json_file.write(tmp_path / "data.json", data)
    before = _state(maya_cmds)
    with pytest.raises((ValueError, TypeError)):
        bdu.AnimationClip.load(path)
    assert _state(maya_cmds) == before


def test_empty_clip_roundtrip(tmp_path):
    clip = bdu.AnimationClip(
        nodes=(),
        layers=(),
        layer_mode="flatten",
        start_frame=0,
        end_frame=0,
        seconds_per_frame=1 / 24,
    )
    assert bdu.AnimationClip.load(clip.save(tmp_path / "data.json")) == clip


@pytest.mark.parametrize(
    "field,value",
    [("value", float("nan")), ("frame", 99), ("in_tangent_type", "invalid")],
)
def test_save_revalidates_mutated_key_data(maya_cmds, tmp_path, field, value):
    node = _node(maya_cmds, "source")
    clip = bdu.AnimationClip.capture([node])
    path = clip.save(tmp_path / "data.json")
    original = path.read_bytes()
    setattr(clip.nodes[0].channels[0].curve.keys[0], field, value)
    before = _state(maya_cmds)
    for target in (path, tmp_path / "missing" / "data.json"):
        with pytest.raises((ValueError, TypeError)):
            clip.save(target)
    assert path.read_bytes() == original
    assert list(tmp_path.iterdir()) == [path]
    assert _state(maya_cmds) == before


def test_load_file_errors(maya_cmds, tmp_path):
    path = tmp_path / "data.json"
    before = _state(maya_cmds)
    with pytest.raises(FileNotFoundError):
        bdu.AnimationClip.load(path)
    path.write_text("{broken", encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        bdu.AnimationClip.load(path)
    assert _state(maya_cmds) == before
