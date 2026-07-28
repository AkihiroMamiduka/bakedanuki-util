# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.generic import GenericField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "ocr"),
        ("outColorG", "ocg"),
        ("outColorB", "ocb"),
    )

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutSizePlugOperator(
    Float2CompoundBasePlugOperator["OutSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outSizeX", "osx"),
        ("outSizeY", "osy"),
    )

    outSizeX = FloatField(default_value=0.0, writable=False)
    osx = outSizeX

    outSizeY = FloatField(default_value=0.0, writable=False)
    osy = outSizeY


class OutSizeAttrOperator(Float2CompoundBaseAttrOperator[OutSizePlugOperator]):
    __slots__ = ()

    outSizeX = FloatField(default_value=0.0, writable=False)
    osx = outSizeX

    outSizeY = FloatField(default_value=0.0, writable=False)
    osy = outSizeY


class OutSizeField(
    Float2CompoundBaseField[OutSizeAttrOperator, OutSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutSizeAttrOperator
    PLUG_CLS = OutSizePlugOperator

    outSizeX = FloatField(default_value=0.0, writable=False)
    osx = outSizeX

    outSizeY = FloatField(default_value=0.0, writable=False)
    osy = outSizeY


class OutTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["OutTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTransparencyR", "otr"),
        ("outTransparencyG", "otg"),
        ("outTransparencyB", "otb"),
    )

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[
        OutTransparencyAttrOperator, OutTransparencyPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class BackupPlugOperator(CompoundPlugOperator["BackupAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("backupAttributes", "ba"),
        ("backupData", "bd"),
    )

    backupAttributes = DataStringField(readable=False, writable=False)
    ba = backupAttributes

    backupData = GenericField(readable=False, writable=False)
    bd = backupData


class BackupAttrOperator(CompoundAttrOperator[BackupPlugOperator]):
    __slots__ = ()

    backupAttributes = DataStringField(readable=False, writable=False)
    ba = backupAttributes

    backupData = GenericField(readable=False, writable=False)
    bd = backupData


class BackupField(CompoundField[BackupAttrOperator, BackupPlugOperator]):
    __slots__ = ()

    ATTR_CLS = BackupAttrOperator
    PLUG_CLS = BackupPlugOperator
