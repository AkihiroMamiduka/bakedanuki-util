# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class CompInstObjGroups_compObjectGroupsPlugOperator(
    CompoundPlugOperator["CompInstObjGroups_compObjectGroupsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("compObjectGrpCompList", "cgcl"),
        ("compObjectGroupId", "cgid"),
    )

    compObjectGrpCompList = TypedField()
    cgcl = compObjectGrpCompList

    compObjectGroupId = LongField(default_value=0)
    cgid = compObjectGroupId


class CompInstObjGroups_compObjectGroupsAttrOperator(
    CompoundAttrOperator[CompInstObjGroups_compObjectGroupsPlugOperator]
):
    __slots__ = ()

    compObjectGrpCompList = TypedField()
    cgcl = compObjectGrpCompList

    compObjectGroupId = LongField(default_value=0)
    cgid = compObjectGroupId


class CompInstObjGroups_compObjectGroupsField(
    CompoundField[
        CompInstObjGroups_compObjectGroupsAttrOperator,
        CompInstObjGroups_compObjectGroupsPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CompInstObjGroups_compObjectGroupsAttrOperator
    PLUG_CLS = CompInstObjGroups_compObjectGroupsPlugOperator


class CompInstObjGroupsPlugOperator(
    CompoundPlugOperator["CompInstObjGroupsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("compObjectGroups", "cog"),)

    compObjectGroups = CompInstObjGroups_compObjectGroupsField(multi=True)
    cog = compObjectGroups


class CompInstObjGroupsAttrOperator(
    CompoundAttrOperator[CompInstObjGroupsPlugOperator]
):
    __slots__ = ()

    compObjectGroups = CompInstObjGroups_compObjectGroupsField(multi=True)
    cog = compObjectGroups


class CompInstObjGroupsField(
    CompoundField[CompInstObjGroupsAttrOperator, CompInstObjGroupsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompInstObjGroupsAttrOperator
    PLUG_CLS = CompInstObjGroupsPlugOperator


class ComponentTagsPlugOperator(
    CompoundPlugOperator["ComponentTagsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("componentTagName", "gtagnm"),
        ("componentTagContents", "gtagcmp"),
    )

    componentTagName = DataStringField()
    gtagnm = componentTagName

    componentTagContents = TypedField()
    gtagcmp = componentTagContents


class ComponentTagsAttrOperator(
    CompoundAttrOperator[ComponentTagsPlugOperator]
):
    __slots__ = ()

    componentTagName = DataStringField()
    gtagnm = componentTagName

    componentTagContents = TypedField()
    gtagcmp = componentTagContents


class ComponentTagsField(
    CompoundField[ComponentTagsAttrOperator, ComponentTagsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ComponentTagsAttrOperator
    PLUG_CLS = ComponentTagsPlugOperator


class LocalPositionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["LocalPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localPositionX", "lpx"),
        ("localPositionY", "lpy"),
        ("localPositionZ", "lpz"),
    )

    localPositionX = DoubleLinearField(default_value=0.0)
    lpx = localPositionX

    localPositionY = DoubleLinearField(default_value=0.0)
    lpy = localPositionY

    localPositionZ = DoubleLinearField(default_value=0.0)
    lpz = localPositionZ


class LocalPositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[LocalPositionPlugOperator]
):
    __slots__ = ()

    localPositionX = DoubleLinearField(default_value=0.0)
    lpx = localPositionX

    localPositionY = DoubleLinearField(default_value=0.0)
    lpy = localPositionY

    localPositionZ = DoubleLinearField(default_value=0.0)
    lpz = localPositionZ


class LocalPositionField(
    DoubleLinear3CompoundBaseField[
        LocalPositionAttrOperator, LocalPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = LocalPositionAttrOperator
    PLUG_CLS = LocalPositionPlugOperator

    localPositionX = DoubleLinearField(default_value=0.0)
    lpx = localPositionX

    localPositionY = DoubleLinearField(default_value=0.0)
    lpy = localPositionY

    localPositionZ = DoubleLinearField(default_value=0.0)
    lpz = localPositionZ


class WorldPositionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["WorldPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldPositionX", "wpx"),
        ("worldPositionY", "wpy"),
        ("worldPositionZ", "wpz"),
    )

    worldPositionX = DoubleLinearField(default_value=0.0, writable=False)
    wpx = worldPositionX

    worldPositionY = DoubleLinearField(default_value=0.0, writable=False)
    wpy = worldPositionY

    worldPositionZ = DoubleLinearField(default_value=0.0, writable=False)
    wpz = worldPositionZ


class WorldPositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[WorldPositionPlugOperator]
):
    __slots__ = ()

    worldPositionX = DoubleLinearField(default_value=0.0, writable=False)
    wpx = worldPositionX

    worldPositionY = DoubleLinearField(default_value=0.0, writable=False)
    wpy = worldPositionY

    worldPositionZ = DoubleLinearField(default_value=0.0, writable=False)
    wpz = worldPositionZ


class WorldPositionField(
    DoubleLinear3CompoundBaseField[
        WorldPositionAttrOperator, WorldPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = WorldPositionAttrOperator
    PLUG_CLS = WorldPositionPlugOperator


class LocalScalePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["LocalScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localScaleX", "lsx"),
        ("localScaleY", "lsy"),
        ("localScaleZ", "lsz"),
    )

    localScaleX = DoubleLinearField(default_value=1.0)
    lsx = localScaleX

    localScaleY = DoubleLinearField(default_value=1.0)
    lsy = localScaleY

    localScaleZ = DoubleLinearField(default_value=1.0)
    lsz = localScaleZ


class LocalScaleAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[LocalScalePlugOperator]
):
    __slots__ = ()

    localScaleX = DoubleLinearField(default_value=1.0)
    lsx = localScaleX

    localScaleY = DoubleLinearField(default_value=1.0)
    lsy = localScaleY

    localScaleZ = DoubleLinearField(default_value=1.0)
    lsz = localScaleZ


class LocalScaleField(
    DoubleLinear3CompoundBaseField[
        LocalScaleAttrOperator, LocalScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = LocalScaleAttrOperator
    PLUG_CLS = LocalScalePlugOperator

    localScaleX = DoubleLinearField(default_value=1.0)
    lsx = localScaleX

    localScaleY = DoubleLinearField(default_value=1.0)
    lsy = localScaleY

    localScaleZ = DoubleLinearField(default_value=1.0)
    lsz = localScaleZ


class ShapeTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ShapeTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shapeTranslateX", "stx"),
        ("shapeTranslateY", "sty"),
        ("shapeTranslateZ", "stz"),
    )

    shapeTranslateX = DoubleLinearField(default_value=0.0)
    stx = shapeTranslateX

    shapeTranslateY = DoubleLinearField(default_value=0.0)
    sty = shapeTranslateY

    shapeTranslateZ = DoubleLinearField(default_value=0.0)
    stz = shapeTranslateZ


class ShapeTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ShapeTranslatePlugOperator]
):
    __slots__ = ()

    shapeTranslateX = DoubleLinearField(default_value=0.0)
    stx = shapeTranslateX

    shapeTranslateY = DoubleLinearField(default_value=0.0)
    sty = shapeTranslateY

    shapeTranslateZ = DoubleLinearField(default_value=0.0)
    stz = shapeTranslateZ


class ShapeTranslateField(
    DoubleLinear3CompoundBaseField[
        ShapeTranslateAttrOperator, ShapeTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ShapeTranslateAttrOperator
    PLUG_CLS = ShapeTranslatePlugOperator

    shapeTranslateX = DoubleLinearField(default_value=0.0)
    stx = shapeTranslateX

    shapeTranslateY = DoubleLinearField(default_value=0.0)
    sty = shapeTranslateY

    shapeTranslateZ = DoubleLinearField(default_value=0.0)
    stz = shapeTranslateZ


class ShapeRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["ShapeRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shapeRotateX", "srx"),
        ("shapeRotateY", "sry"),
        ("shapeRotateZ", "srz"),
    )

    shapeRotateX = DoubleAngleField(default_value=0.0)
    srx = shapeRotateX

    shapeRotateY = DoubleAngleField(default_value=0.0)
    sry = shapeRotateY

    shapeRotateZ = DoubleAngleField(default_value=0.0)
    srz = shapeRotateZ


class ShapeRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[ShapeRotatePlugOperator]
):
    __slots__ = ()

    shapeRotateX = DoubleAngleField(default_value=0.0)
    srx = shapeRotateX

    shapeRotateY = DoubleAngleField(default_value=0.0)
    sry = shapeRotateY

    shapeRotateZ = DoubleAngleField(default_value=0.0)
    srz = shapeRotateZ


class ShapeRotateField(
    DoubleAngle3CompoundBaseField[
        ShapeRotateAttrOperator, ShapeRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ShapeRotateAttrOperator
    PLUG_CLS = ShapeRotatePlugOperator

    shapeRotateX = DoubleAngleField(default_value=0.0)
    srx = shapeRotateX

    shapeRotateY = DoubleAngleField(default_value=0.0)
    sry = shapeRotateY

    shapeRotateZ = DoubleAngleField(default_value=0.0)
    srz = shapeRotateZ


class ShapeScalePlugOperator(
    Double3CompoundBasePlugOperator["ShapeScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shapeScaleX", "sscx"),
        ("shapeScaleY", "sscy"),
        ("shapeScaleZ", "sscz"),
    )

    shapeScaleX = DoubleField(default_value=1.0)
    sscx = shapeScaleX

    shapeScaleY = DoubleField(default_value=1.0)
    sscy = shapeScaleY

    shapeScaleZ = DoubleField(default_value=1.0)
    sscz = shapeScaleZ


class ShapeScaleAttrOperator(
    Double3CompoundBaseAttrOperator[ShapeScalePlugOperator]
):
    __slots__ = ()

    shapeScaleX = DoubleField(default_value=1.0)
    sscx = shapeScaleX

    shapeScaleY = DoubleField(default_value=1.0)
    sscy = shapeScaleY

    shapeScaleZ = DoubleField(default_value=1.0)
    sscz = shapeScaleZ


class ShapeScaleField(
    Double3CompoundBaseField[ShapeScaleAttrOperator, ShapeScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShapeScaleAttrOperator
    PLUG_CLS = ShapeScalePlugOperator

    shapeScaleX = DoubleField(default_value=1.0)
    sscx = shapeScaleX

    shapeScaleY = DoubleField(default_value=1.0)
    sscy = shapeScaleY

    shapeScaleZ = DoubleField(default_value=1.0)
    sscz = shapeScaleZ


class ShapeAxisTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ShapeAxisTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shapeAxisTranslateX", "satx"),
        ("shapeAxisTranslateY", "saty"),
        ("shapeAxisTranslateZ", "satz"),
    )

    shapeAxisTranslateX = DoubleLinearField(default_value=0.0)
    satx = shapeAxisTranslateX

    shapeAxisTranslateY = DoubleLinearField(default_value=0.0)
    saty = shapeAxisTranslateY

    shapeAxisTranslateZ = DoubleLinearField(default_value=0.0)
    satz = shapeAxisTranslateZ


class ShapeAxisTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ShapeAxisTranslatePlugOperator]
):
    __slots__ = ()

    shapeAxisTranslateX = DoubleLinearField(default_value=0.0)
    satx = shapeAxisTranslateX

    shapeAxisTranslateY = DoubleLinearField(default_value=0.0)
    saty = shapeAxisTranslateY

    shapeAxisTranslateZ = DoubleLinearField(default_value=0.0)
    satz = shapeAxisTranslateZ


class ShapeAxisTranslateField(
    DoubleLinear3CompoundBaseField[
        ShapeAxisTranslateAttrOperator, ShapeAxisTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ShapeAxisTranslateAttrOperator
    PLUG_CLS = ShapeAxisTranslatePlugOperator

    shapeAxisTranslateX = DoubleLinearField(default_value=0.0)
    satx = shapeAxisTranslateX

    shapeAxisTranslateY = DoubleLinearField(default_value=0.0)
    saty = shapeAxisTranslateY

    shapeAxisTranslateZ = DoubleLinearField(default_value=0.0)
    satz = shapeAxisTranslateZ


class ShapeAxisRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["ShapeAxisRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shapeAxisRotateX", "sarx"),
        ("shapeAxisRotateY", "sary"),
        ("shapeAxisRotateZ", "sarz"),
    )

    shapeAxisRotateX = DoubleAngleField(default_value=0.0)
    sarx = shapeAxisRotateX

    shapeAxisRotateY = DoubleAngleField(default_value=0.0)
    sary = shapeAxisRotateY

    shapeAxisRotateZ = DoubleAngleField(default_value=0.0)
    sarz = shapeAxisRotateZ


class ShapeAxisRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[ShapeAxisRotatePlugOperator]
):
    __slots__ = ()

    shapeAxisRotateX = DoubleAngleField(default_value=0.0)
    sarx = shapeAxisRotateX

    shapeAxisRotateY = DoubleAngleField(default_value=0.0)
    sary = shapeAxisRotateY

    shapeAxisRotateZ = DoubleAngleField(default_value=0.0)
    sarz = shapeAxisRotateZ


class ShapeAxisRotateField(
    DoubleAngle3CompoundBaseField[
        ShapeAxisRotateAttrOperator, ShapeAxisRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ShapeAxisRotateAttrOperator
    PLUG_CLS = ShapeAxisRotatePlugOperator

    shapeAxisRotateX = DoubleAngleField(default_value=0.0)
    sarx = shapeAxisRotateX

    shapeAxisRotateY = DoubleAngleField(default_value=0.0)
    sary = shapeAxisRotateY

    shapeAxisRotateZ = DoubleAngleField(default_value=0.0)
    sarz = shapeAxisRotateZ


class ShapeAxisScalePlugOperator(
    Double3CompoundBasePlugOperator["ShapeAxisScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shapeAxisScaleX", "sascx"),
        ("shapeAxisScaleY", "sascy"),
        ("shapeAxisScaleZ", "sascz"),
    )

    shapeAxisScaleX = DoubleField(default_value=1.0)
    sascx = shapeAxisScaleX

    shapeAxisScaleY = DoubleField(default_value=1.0)
    sascy = shapeAxisScaleY

    shapeAxisScaleZ = DoubleField(default_value=1.0)
    sascz = shapeAxisScaleZ


class ShapeAxisScaleAttrOperator(
    Double3CompoundBaseAttrOperator[ShapeAxisScalePlugOperator]
):
    __slots__ = ()

    shapeAxisScaleX = DoubleField(default_value=1.0)
    sascx = shapeAxisScaleX

    shapeAxisScaleY = DoubleField(default_value=1.0)
    sascy = shapeAxisScaleY

    shapeAxisScaleZ = DoubleField(default_value=1.0)
    sascz = shapeAxisScaleZ


class ShapeAxisScaleField(
    Double3CompoundBaseField[
        ShapeAxisScaleAttrOperator, ShapeAxisScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ShapeAxisScaleAttrOperator
    PLUG_CLS = ShapeAxisScalePlugOperator

    shapeAxisScaleX = DoubleField(default_value=1.0)
    sascx = shapeAxisScaleX

    shapeAxisScaleY = DoubleField(default_value=1.0)
    sascy = shapeAxisScaleY

    shapeAxisScaleZ = DoubleField(default_value=1.0)
    sascz = shapeAxisScaleZ
