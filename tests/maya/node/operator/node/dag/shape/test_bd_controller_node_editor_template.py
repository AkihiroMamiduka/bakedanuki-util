# coding: utf-8
from __future__ import annotations

import os
from pathlib import Path
import xml.etree.ElementTree as ET

import pytest

pytestmark = pytest.mark.maya

_REPOSITORY_ROOT = Path(__file__).resolve().parents[7]
_PACKAGE_ROOT = _REPOSITORY_ROOT / "bakedanuki" / "bakedanuki-util"
_TEMPLATE_PATH = (
    _PACKAGE_ROOT
    / "templates"
    / "node_editor"
    / "NEbdControllerShapeTemplate.xml"
)


@pytest.fixture
def controller_shape(maya_cmds, new_scene):
    version = maya_cmds.about(version=True)
    plugin_path = Path(
        os.environ.get(
            "BD_UTIL_NODES_PLUGIN_PATH",
            _PACKAGE_ROOT / "plug-ins" / f"maya{version}" / "bdUtilNodes.mll",
        )
    )
    assert plugin_path.is_file(), f"Staged plug-in not found: {plugin_path}"
    maya_cmds.loadPlugin(str(plugin_path), quiet=True)
    return maya_cmds.createNode("bdControllerShape")


@pytest.fixture
def node_editor_template():
    root = ET.parse(_TEMPLATE_PATH).getroot()
    assert root.tag == "templates"
    assert root.find("using").attrib == {"package": "maya"}
    template = root.find("template")
    view = root.find("view")
    assert template.attrib == {"name": "NEbdControllerShape"}
    assert view.attrib == {
        "name": "NEDefault",
        "template": "NEbdControllerShape",
    }
    return template, view


def _is_separator(maya_cmds, shape, name):
    return not name.strip("_") and (
        maya_cmds.getAttr(f"{shape}.{name}", type=True) == "enum"
    )


def test_template_covers_controller_attributes_without_inherited_extras(
    maya_cmds, controller_shape, node_editor_template
):
    template, view = node_editor_template
    locator = maya_cmds.createNode("locator")
    inherited = set(maya_cmds.listAttr(locator))
    controller_attributes = {
        name
        for name in maya_cmds.listAttr(controller_shape)
        if name not in inherited
        and not maya_cmds.attributeQuery(
            name, node=controller_shape, listParent=True
        )
        and not _is_separator(maya_cmds, controller_shape, name)
    }
    attributes = template.findall("attribute")
    attribute_names = [attribute.attrib["name"] for attribute in attributes]
    property_names = [prop.attrib["name"] for prop in view.findall("property")]

    assert len(attribute_names) == 66
    assert len(attribute_names) == len(set(attribute_names))
    assert set(attribute_names) == controller_attributes | {"visibility"}
    assert property_names == attribute_names
    for attribute in attributes:
        name = attribute.attrib["name"]
        assert attribute.attrib["type"] == (
            f"maya.{maya_cmds.getAttr(f'{controller_shape}.{name}', type=True)}"
        )
        assert attribute.findtext("label") == maya_cmds.attributeQuery(
            name, node=controller_shape, niceName=True
        )


def test_template_keeps_channel_box_order_and_compound_parents(
    maya_cmds, controller_shape, node_editor_template
):
    _, view = node_editor_template
    channel_attributes = [
        name
        for name in maya_cmds.listAttr(controller_shape, channelBox=True)
        if not maya_cmds.attributeQuery(
            name, node=controller_shape, listParent=True
        )
        and not _is_separator(maya_cmds, controller_shape, name)
    ]
    property_names = [prop.attrib["name"] for prop in view.findall("property")]

    assert property_names == [
        "visibility",
        "shapeAnimationTransformMatrix",
        *channel_attributes,
    ]
    fin_start = property_names.index("shapeFin")
    assert property_names[fin_start : fin_start + 5] == [
        "shapeFin",
        "shapeFinType",
        "shapeFinHeight",
        "shapeFinWidthScale",
        "shapeGuideLine",
    ]
    assert all(not list(prop) for prop in view.findall("property"))


def test_every_module_version_resolves_the_distributed_template():
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
        assert (
            template_directory / _TEMPLATE_PATH.name
        ) == _TEMPLATE_PATH.resolve()
        assert (template_directory / _TEMPLATE_PATH.name).is_file()
