# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)


class AttrAAPlugOperator(CompoundPlugOperator["AttrAAAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("attrAD", "ad"),
        ("attrAG", "ag"),
        ("attrAJ", "aj"),
    )

    attrAD = CompoundField(default_value=(0.0, 0.0, 0.0))
    ad = attrAD

    attrAG = CompoundField(default_value=(0.0, 0.0, 0.0))
    ag = attrAG

    attrAJ = CompoundField(default_value=(0.0, 0.0, 0.0))
    aj = attrAJ


class AttrAAAttrOperator(CompoundAttrOperator[AttrAAPlugOperator]):
    __slots__ = ()

    attrAD = CompoundField(default_value=(0.0, 0.0, 0.0))
    ad = attrAD

    attrAG = CompoundField(default_value=(0.0, 0.0, 0.0))
    ag = attrAG

    attrAJ = CompoundField(default_value=(0.0, 0.0, 0.0))
    aj = attrAJ


class AttrAAField(CompoundField[AttrAAAttrOperator, AttrAAPlugOperator]):
    __slots__ = ()

    ATTR_CLS = AttrAAAttrOperator
    PLUG_CLS = AttrAAPlugOperator

    attrAD = CompoundField(default_value=(0.0, 0.0, 0.0))
    ad = attrAD

    attrAG = CompoundField(default_value=(0.0, 0.0, 0.0))
    ag = attrAG

    attrAJ = CompoundField(default_value=(0.0, 0.0, 0.0))
    aj = attrAJ


class AttrABPlugOperator(CompoundPlugOperator["AttrABAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("attrAE", "ae"),
        ("attrAH", "ah"),
        ("attrAK", "ak"),
    )

    attrAE = CompoundField(default_value=(0.0, 0.0, 0.0))
    ae = attrAE

    attrAH = CompoundField(default_value=(0.0, 0.0, 0.0))
    ah = attrAH

    attrAK = CompoundField(default_value=(0.0, 0.0, 0.0))
    ak = attrAK


class AttrABAttrOperator(CompoundAttrOperator[AttrABPlugOperator]):
    __slots__ = ()

    attrAE = CompoundField(default_value=(0.0, 0.0, 0.0))
    ae = attrAE

    attrAH = CompoundField(default_value=(0.0, 0.0, 0.0))
    ah = attrAH

    attrAK = CompoundField(default_value=(0.0, 0.0, 0.0))
    ak = attrAK


class AttrABField(CompoundField[AttrABAttrOperator, AttrABPlugOperator]):
    __slots__ = ()

    ATTR_CLS = AttrABAttrOperator
    PLUG_CLS = AttrABPlugOperator

    attrAE = CompoundField(default_value=(0.0, 0.0, 0.0))
    ae = attrAE

    attrAH = CompoundField(default_value=(0.0, 0.0, 0.0))
    ah = attrAH

    attrAK = CompoundField(default_value=(0.0, 0.0, 0.0))
    ak = attrAK


class AttrACPlugOperator(CompoundPlugOperator["AttrACAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("attrAF", "af"),
        ("attrAI", "ai"),
        ("attrAL", "al"),
    )

    attrAF = CompoundField(default_value=(0.0, 0.0, 0.0))
    af = attrAF

    attrAI = CompoundField(default_value=(0.0, 0.0, 0.0))
    ai = attrAI

    attrAL = CompoundField(default_value=(0.0, 0.0, 0.0))
    al = attrAL


class AttrACAttrOperator(CompoundAttrOperator[AttrACPlugOperator]):
    __slots__ = ()

    attrAF = CompoundField(default_value=(0.0, 0.0, 0.0))
    af = attrAF

    attrAI = CompoundField(default_value=(0.0, 0.0, 0.0))
    ai = attrAI

    attrAL = CompoundField(default_value=(0.0, 0.0, 0.0))
    al = attrAL


class AttrACField(CompoundField[AttrACAttrOperator, AttrACPlugOperator]):
    __slots__ = ()

    ATTR_CLS = AttrACAttrOperator
    PLUG_CLS = AttrACPlugOperator

    attrAF = CompoundField(default_value=(0.0, 0.0, 0.0))
    af = attrAF

    attrAI = CompoundField(default_value=(0.0, 0.0, 0.0))
    ai = attrAI

    attrAL = CompoundField(default_value=(0.0, 0.0, 0.0))
    al = attrAL
