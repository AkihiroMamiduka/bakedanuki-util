# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.dt.string import DataStringField


class GeneratedFacade(DG):
    __slots__ = ()

    NODE_TYPE = "facade"

    sharedLibName = DataStringField()
    sln = sharedLibName

    connection = MessageField()
    c = connection

    uiName = DataStringField()
    uin = uiName

    keyWords = DataStringField()
    kwds = keyWords

    uiScript = DataStringField()
    uis = uiScript

    uniqueID = DataStringField()
    uid = uniqueID
