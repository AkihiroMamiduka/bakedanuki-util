# coding: utf-8

# maya
from maya.api import OpenMaya as om


def create(mod: om.MDagModifier):
    mod.createNode("joint")
    mod.createNode("joint")
