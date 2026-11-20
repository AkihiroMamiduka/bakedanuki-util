# coding: utf-8
from __future__ import annotations

import os
from pathlib import Path
import xml.etree.ElementTree as ET

import pytest

pytestmark = pytest.mark.maya

_REPOSITORY_ROOT = Path(__file__).resolve().parents[7]
_PACKAGE_ROOT = _REPOSITORY_ROOT / "bakedanuki" / "bakedanuki-util"
_TEMPLATE_DIRECTORY = _PACKAGE_ROOT / "templates" / "node_editor"
_MATRIX_ATTRIBUTE = "shapeTransformMatrix"
_FOCUS_BOX_TYPE = "bdShpL_FocusBoundingBox"
_STATIC_NODE_TYPES = ("bdShpL_Cube", _FOCUS_BOX_TYPE)


@pytest.fixture
def load_plugin(maya_cmds, new_scene):
    version = maya_cmds.about(version=True)
    plugin_path = Path(
        os.environ.get(
            "BD_UTIL_NODES_PLUGIN_PATH",
            _PACKAGE_ROOT / "plug-ins" / f"maya{version}" / "bdUtilNodes.mll",
        )
    )
    assert plugin_path.is_file(), f"Staged plug-in not found: {plugin_path}"
    maya_cmds.loadPlugin(str(plugin_path), quiet=True)


@pytest.mark.parametrize(
    ("node_type", "expected_ports"),
    [
        pytest.param(
            "bdControllerShape",
            (_MATRIX_ATTRIBUTE,),
            marks=pytest.mark.controller_shape,
        ),
        *((node_type, ()) for node_type in _STATIC_NODE_TYPES),
    ],
)
def test_custom_view_ports(maya_cmds, load_plugin, node_type, expected_ports):
    root = ET.parse(
        _TEMPLATE_DIRECTORY / f"NE{node_type}Template.xml"
    ).getroot()
    assert root.tag == "templates"
    template = root.find("template")
    view = root.find("view")
    template_name = f"NE{node_type}"
    assert template.attrib == {"name": template_name}
    assert view.attrib == {"name": "NEDefault", "template": template_name}
    assert tuple(property_.attrib for property_ in view) == tuple(
        {"name": name} for name in expected_ports
    )
    assert all(
        property_.tag == "property" and not list(property_)
        for property_ in view
    )

    shape = maya_cmds.createNode(node_type)
    assert maya_cmds.nodeType(shape) == node_type
    attributes = tuple(template)
    assert (
        tuple(attribute.attrib["name"] for attribute in attributes)
        == expected_ports
    )
    if not attributes:
        for name in (_MATRIX_ATTRIBUTE, "stm"):
            assert not maya_cmds.attributeQuery(name, node=shape, exists=True)
        if node_type == _FOCUS_BOX_TYPE:
            assert maya_cmds.attributeQuery(
                "showShape", node=shape, exists=True
            )
        return

    assert root.find("using").attrib == {"package": "maya"}
    (attribute,) = attributes
    assert attribute.tag == "attribute"
    assert attribute.attrib == {
        "name": _MATRIX_ATTRIBUTE,
        "type": "maya.matrix",
    }
    assert (
        maya_cmds.getAttr(f"{shape}.{_MATRIX_ATTRIBUTE}", type=True)
        == "matrix"
    )
    assert (
        maya_cmds.attributeQuery(_MATRIX_ATTRIBUTE, node=shape, shortName=True)
        == "stm"
    )
    assert attribute.findtext("label") == maya_cmds.attributeQuery(
        _MATRIX_ATTRIBUTE, node=shape, niceName=True
    )


def test_every_module_version_resolves_the_distributed_templates():
    module_path = _REPOSITORY_ROOT / "bakedanuki" / "modules" / "bd_util.mod"
    blocks = []
    for raw_line in module_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("+ "):
            blocks.append((line.split(), []))
        elif line and not line.startswith("#"):
            assert blocks
            blocks[-1][1].append(line)

    assert blocks
    for header, settings in blocks:
        assignments = [
            setting.removeprefix("MAYA_CUSTOM_TEMPLATE_PATH+:=")
            for setting in settings
            if setting.startswith("MAYA_CUSTOM_TEMPLATE_PATH+:=")
        ]
        assert len(assignments) == 1, header
        template_directory = (
            module_path.parent / header[-1] / assignments[0]
        ).resolve()
        assert template_directory == _TEMPLATE_DIRECTORY.resolve()
        for node_type in ("bdControllerShape", *_STATIC_NODE_TYPES):
            assert (
                template_directory / f"NE{node_type}Template.xml"
            ).is_file()
