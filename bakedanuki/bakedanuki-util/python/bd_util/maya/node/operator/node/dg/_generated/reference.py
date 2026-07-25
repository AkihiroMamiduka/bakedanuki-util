# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.reference import (
    ConnectionListField,
    MultiParentListField,
)
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedReference(DG):
    __slots__ = ()

    NODE_TYPE = "reference"

    fileNames = DataStringField(multi=True)
    fn = fileNames

    connectionList = ConnectionListField(multi=True)
    cl = connectionList

    setAttrList = DataStringField(multi=True)
    sl = setAttrList

    addAttrList = DataStringField(multi=True)
    al = addAttrList

    deleteAttrList = DataStringField(multi=True)
    dl = deleteAttrList

    brokenConnectionList = DataStringField(multi=True)
    bl = brokenConnectionList

    parentList = DataStringField(multi=True)
    pl = parentList

    fosterParent = MessageField(readable=False)
    fp = fosterParent

    fosterSiblings = MessageField(multi=True, readable=False)
    fs = fosterSiblings

    placeHolderList = GenericField(multi=True)
    phl = placeHolderList

    multiParentList = MultiParentListField(multi=True)
    mpl = multiParentList

    edits = TypedField()
    ed = edits

    proxyTag = DataStringField()
    ptag = proxyTag

    proxyMsg = MessageField()
    pmsg = proxyMsg

    unknownReference = MessageField()
    ur = unknownReference

    sharedReference = MessageField()
    sr = sharedReference

    locked = BoolField(default_value=False)
    lk = locked

    placeHolderNamespace = DataStringField()
    phns = placeHolderNamespace

    associatedNode = MessageField(multi=True, readable=False)
    asn = associatedNode
