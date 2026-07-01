# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)


class AttrAAPlugOperator(
    CompoundPlugOperator["AttrAAAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("attrAD", "ad"),
        ("attrAG", "ag"),
        ("attrAJ", "aj"),
    )

    attrAD = CompoundField()
    ad = attrAD

    attrAG = CompoundField()
    ag = attrAG

    attrAJ = CompoundField()
    aj = attrAJ


class AttrAAAttrOperator(
    CompoundAttrOperator[AttrAAPlugOperator]
):
    __slots__ = ()

    attrAD = CompoundField()
    ad = attrAD

    attrAG = CompoundField()
    ag = attrAG

    attrAJ = CompoundField()
    aj = attrAJ


class AttrAAField(
    CompoundField[AttrAAAttrOperator, AttrAAPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttrAAAttrOperator
    PLUG_CLS = AttrAAPlugOperator

    attrAD = CompoundField()
    ad = attrAD

    attrAG = CompoundField()
    ag = attrAG

    attrAJ = CompoundField()
    aj = attrAJ


class AttrABPlugOperator(
    CompoundPlugOperator["AttrABAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("attrAE", "ae"),
        ("attrAH", "ah"),
        ("attrAK", "ak"),
    )

    attrAE = CompoundField()
    ae = attrAE

    attrAH = CompoundField()
    ah = attrAH

    attrAK = CompoundField()
    ak = attrAK


class AttrABAttrOperator(
    CompoundAttrOperator[AttrABPlugOperator]
):
    __slots__ = ()

    attrAE = CompoundField()
    ae = attrAE

    attrAH = CompoundField()
    ah = attrAH

    attrAK = CompoundField()
    ak = attrAK


class AttrABField(
    CompoundField[AttrABAttrOperator, AttrABPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttrABAttrOperator
    PLUG_CLS = AttrABPlugOperator

    attrAE = CompoundField()
    ae = attrAE

    attrAH = CompoundField()
    ah = attrAH

    attrAK = CompoundField()
    ak = attrAK


class AttrACPlugOperator(
    CompoundPlugOperator["AttrACAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("attrAF", "af"),
        ("attrAI", "ai"),
        ("attrAL", "al"),
    )

    attrAF = CompoundField()
    af = attrAF

    attrAI = CompoundField()
    ai = attrAI

    attrAL = CompoundField()
    al = attrAL


class AttrACAttrOperator(
    CompoundAttrOperator[AttrACPlugOperator]
):
    __slots__ = ()

    attrAF = CompoundField()
    af = attrAF

    attrAI = CompoundField()
    ai = attrAI

    attrAL = CompoundField()
    al = attrAL


class AttrACField(
    CompoundField[AttrACAttrOperator, AttrACPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttrACAttrOperator
    PLUG_CLS = AttrACPlugOperator

    attrAF = CompoundField()
    af = attrAF

    attrAI = CompoundField()
    ai = attrAI

    attrAL = CompoundField()
    al = attrAL
