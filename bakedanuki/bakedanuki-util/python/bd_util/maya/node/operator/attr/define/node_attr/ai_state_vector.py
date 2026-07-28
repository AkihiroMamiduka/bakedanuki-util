# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class OutValuePlugOperator(
    Float3CompoundBasePlugOperator["OutValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outValueX", "outx"),
        ("outValueY", "outy"),
        ("outValueZ", "outz"),
    )

    outValueX = FloatField(default_value=0.0, writable=False)
    outx = outValueX

    outValueY = FloatField(default_value=0.0, writable=False)
    outy = outValueY

    outValueZ = FloatField(default_value=0.0, writable=False)
    outz = outValueZ


class OutValueAttrOperator(
    Float3CompoundBaseAttrOperator[OutValuePlugOperator]
):
    __slots__ = ()

    outValueX = FloatField(default_value=0.0, writable=False)
    outx = outValueX

    outValueY = FloatField(default_value=0.0, writable=False)
    outy = outValueY

    outValueZ = FloatField(default_value=0.0, writable=False)
    outz = outValueZ


class OutValueField(
    Float3CompoundBaseField[OutValueAttrOperator, OutValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutValueAttrOperator
    PLUG_CLS = OutValuePlugOperator

    outValueX = FloatField(default_value=0.0, writable=False)
    outx = outValueX

    outValueY = FloatField(default_value=0.0, writable=False)
    outy = outValueY

    outValueZ = FloatField(default_value=0.0, writable=False)
    outz = outValueZ


class RoPlugOperator(Float3CompoundBasePlugOperator["RoAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RoX", "Rox"),
        ("RoY", "Roy"),
        ("RoZ", "Roz"),
    )

    RoX = FloatField(default_value=0.0, writable=False)
    Rox = RoX

    RoY = FloatField(default_value=0.0, writable=False)
    Roy = RoY

    RoZ = FloatField(default_value=0.0, writable=False)
    Roz = RoZ


class RoAttrOperator(Float3CompoundBaseAttrOperator[RoPlugOperator]):
    __slots__ = ()

    RoX = FloatField(default_value=0.0, writable=False)
    Rox = RoX

    RoY = FloatField(default_value=0.0, writable=False)
    Roy = RoY

    RoZ = FloatField(default_value=0.0, writable=False)
    Roz = RoZ


class RoField(Float3CompoundBaseField[RoAttrOperator, RoPlugOperator]):
    __slots__ = ()

    ATTR_CLS = RoAttrOperator
    PLUG_CLS = RoPlugOperator

    RoX = FloatField(default_value=0.0, writable=False)
    Rox = RoX

    RoY = FloatField(default_value=0.0, writable=False)
    Roy = RoY

    RoZ = FloatField(default_value=0.0, writable=False)
    Roz = RoZ


class RdPlugOperator(Float3CompoundBasePlugOperator["RdAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RdX", "Rdx"),
        ("RdY", "Rdy"),
        ("RdZ", "Rdz"),
    )

    RdX = FloatField(default_value=0.0, writable=False)
    Rdx = RdX

    RdY = FloatField(default_value=0.0, writable=False)
    Rdy = RdY

    RdZ = FloatField(default_value=0.0, writable=False)
    Rdz = RdZ


class RdAttrOperator(Float3CompoundBaseAttrOperator[RdPlugOperator]):
    __slots__ = ()

    RdX = FloatField(default_value=0.0, writable=False)
    Rdx = RdX

    RdY = FloatField(default_value=0.0, writable=False)
    Rdy = RdY

    RdZ = FloatField(default_value=0.0, writable=False)
    Rdz = RdZ


class RdField(Float3CompoundBaseField[RdAttrOperator, RdPlugOperator]):
    __slots__ = ()

    ATTR_CLS = RdAttrOperator
    PLUG_CLS = RdPlugOperator

    RdX = FloatField(default_value=0.0, writable=False)
    Rdx = RdX

    RdY = FloatField(default_value=0.0, writable=False)
    Rdy = RdY

    RdZ = FloatField(default_value=0.0, writable=False)
    Rdz = RdZ


class PoPlugOperator(Float3CompoundBasePlugOperator["PoAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("PoX", "Pox"),
        ("PoY", "Poy"),
        ("PoZ", "Poz"),
    )

    PoX = FloatField(default_value=0.0, writable=False)
    Pox = PoX

    PoY = FloatField(default_value=0.0, writable=False)
    Poy = PoY

    PoZ = FloatField(default_value=0.0, writable=False)
    Poz = PoZ


class PoAttrOperator(Float3CompoundBaseAttrOperator[PoPlugOperator]):
    __slots__ = ()

    PoX = FloatField(default_value=0.0, writable=False)
    Pox = PoX

    PoY = FloatField(default_value=0.0, writable=False)
    Poy = PoY

    PoZ = FloatField(default_value=0.0, writable=False)
    Poz = PoZ


class PoField(Float3CompoundBaseField[PoAttrOperator, PoPlugOperator]):
    __slots__ = ()

    ATTR_CLS = PoAttrOperator
    PLUG_CLS = PoPlugOperator

    PoX = FloatField(default_value=0.0, writable=False)
    Pox = PoX

    PoY = FloatField(default_value=0.0, writable=False)
    Poy = PoY

    PoZ = FloatField(default_value=0.0, writable=False)
    Poz = PoZ


class PPlugOperator(Float3CompoundBasePlugOperator["PAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("PX", "Px"),
        ("PY", "Py"),
        ("PZ", "Pz"),
    )

    PX = FloatField(default_value=0.0, writable=False)
    Px = PX

    PY = FloatField(default_value=0.0, writable=False)
    Py = PY

    PZ = FloatField(default_value=0.0, writable=False)
    Pz = PZ


class PAttrOperator(Float3CompoundBaseAttrOperator[PPlugOperator]):
    __slots__ = ()

    PX = FloatField(default_value=0.0, writable=False)
    Px = PX

    PY = FloatField(default_value=0.0, writable=False)
    Py = PY

    PZ = FloatField(default_value=0.0, writable=False)
    Pz = PZ


class PField(Float3CompoundBaseField[PAttrOperator, PPlugOperator]):
    __slots__ = ()

    ATTR_CLS = PAttrOperator
    PLUG_CLS = PPlugOperator

    PX = FloatField(default_value=0.0, writable=False)
    Px = PX

    PY = FloatField(default_value=0.0, writable=False)
    Py = PY

    PZ = FloatField(default_value=0.0, writable=False)
    Pz = PZ


class DPdxPlugOperator(Float3CompoundBasePlugOperator["DPdxAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dPdxX", "dPdxx"),
        ("dPdxY", "dPdxy"),
        ("dPdxZ", "dPdxz"),
    )

    dPdxX = FloatField(default_value=0.0, writable=False)
    dPdxx = dPdxX

    dPdxY = FloatField(default_value=0.0, writable=False)
    dPdxy = dPdxY

    dPdxZ = FloatField(default_value=0.0, writable=False)
    dPdxz = dPdxZ


class DPdxAttrOperator(Float3CompoundBaseAttrOperator[DPdxPlugOperator]):
    __slots__ = ()

    dPdxX = FloatField(default_value=0.0, writable=False)
    dPdxx = dPdxX

    dPdxY = FloatField(default_value=0.0, writable=False)
    dPdxy = dPdxY

    dPdxZ = FloatField(default_value=0.0, writable=False)
    dPdxz = dPdxZ


class DPdxField(Float3CompoundBaseField[DPdxAttrOperator, DPdxPlugOperator]):
    __slots__ = ()

    ATTR_CLS = DPdxAttrOperator
    PLUG_CLS = DPdxPlugOperator

    dPdxX = FloatField(default_value=0.0, writable=False)
    dPdxx = dPdxX

    dPdxY = FloatField(default_value=0.0, writable=False)
    dPdxy = dPdxY

    dPdxZ = FloatField(default_value=0.0, writable=False)
    dPdxz = dPdxZ


class DPdyPlugOperator(Float3CompoundBasePlugOperator["DPdyAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dPdyX", "dPdyx"),
        ("dPdyY", "dPdyy"),
        ("dPdyZ", "dPdyz"),
    )

    dPdyX = FloatField(default_value=0.0, writable=False)
    dPdyx = dPdyX

    dPdyY = FloatField(default_value=0.0, writable=False)
    dPdyy = dPdyY

    dPdyZ = FloatField(default_value=0.0, writable=False)
    dPdyz = dPdyZ


class DPdyAttrOperator(Float3CompoundBaseAttrOperator[DPdyPlugOperator]):
    __slots__ = ()

    dPdyX = FloatField(default_value=0.0, writable=False)
    dPdyx = dPdyX

    dPdyY = FloatField(default_value=0.0, writable=False)
    dPdyy = dPdyY

    dPdyZ = FloatField(default_value=0.0, writable=False)
    dPdyz = dPdyZ


class DPdyField(Float3CompoundBaseField[DPdyAttrOperator, DPdyPlugOperator]):
    __slots__ = ()

    ATTR_CLS = DPdyAttrOperator
    PLUG_CLS = DPdyPlugOperator

    dPdyX = FloatField(default_value=0.0, writable=False)
    dPdyx = dPdyX

    dPdyY = FloatField(default_value=0.0, writable=False)
    dPdyy = dPdyY

    dPdyZ = FloatField(default_value=0.0, writable=False)
    dPdyz = dPdyZ


class NPlugOperator(Float3CompoundBasePlugOperator["NAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("NX", "Nx"),
        ("NY", "Ny"),
        ("NZ", "Nz"),
    )

    NX = FloatField(default_value=0.0, writable=False)
    Nx = NX

    NY = FloatField(default_value=0.0, writable=False)
    Ny = NY

    NZ = FloatField(default_value=0.0, writable=False)
    Nz = NZ


class NAttrOperator(Float3CompoundBaseAttrOperator[NPlugOperator]):
    __slots__ = ()

    NX = FloatField(default_value=0.0, writable=False)
    Nx = NX

    NY = FloatField(default_value=0.0, writable=False)
    Ny = NY

    NZ = FloatField(default_value=0.0, writable=False)
    Nz = NZ


class NField(Float3CompoundBaseField[NAttrOperator, NPlugOperator]):
    __slots__ = ()

    ATTR_CLS = NAttrOperator
    PLUG_CLS = NPlugOperator

    NX = FloatField(default_value=0.0, writable=False)
    Nx = NX

    NY = FloatField(default_value=0.0, writable=False)
    Ny = NY

    NZ = FloatField(default_value=0.0, writable=False)
    Nz = NZ


class NfPlugOperator(Float3CompoundBasePlugOperator["NfAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("NfX", "Nfx"),
        ("NfY", "Nfy"),
        ("NfZ", "Nfz"),
    )

    NfX = FloatField(default_value=0.0, writable=False)
    Nfx = NfX

    NfY = FloatField(default_value=0.0, writable=False)
    Nfy = NfY

    NfZ = FloatField(default_value=0.0, writable=False)
    Nfz = NfZ


class NfAttrOperator(Float3CompoundBaseAttrOperator[NfPlugOperator]):
    __slots__ = ()

    NfX = FloatField(default_value=0.0, writable=False)
    Nfx = NfX

    NfY = FloatField(default_value=0.0, writable=False)
    Nfy = NfY

    NfZ = FloatField(default_value=0.0, writable=False)
    Nfz = NfZ


class NfField(Float3CompoundBaseField[NfAttrOperator, NfPlugOperator]):
    __slots__ = ()

    ATTR_CLS = NfAttrOperator
    PLUG_CLS = NfPlugOperator

    NfX = FloatField(default_value=0.0, writable=False)
    Nfx = NfX

    NfY = FloatField(default_value=0.0, writable=False)
    Nfy = NfY

    NfZ = FloatField(default_value=0.0, writable=False)
    Nfz = NfZ


class NgPlugOperator(Float3CompoundBasePlugOperator["NgAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("NgX", "Ngx"),
        ("NgY", "Ngy"),
        ("NgZ", "Ngz"),
    )

    NgX = FloatField(default_value=0.0, writable=False)
    Ngx = NgX

    NgY = FloatField(default_value=0.0, writable=False)
    Ngy = NgY

    NgZ = FloatField(default_value=0.0, writable=False)
    Ngz = NgZ


class NgAttrOperator(Float3CompoundBaseAttrOperator[NgPlugOperator]):
    __slots__ = ()

    NgX = FloatField(default_value=0.0, writable=False)
    Ngx = NgX

    NgY = FloatField(default_value=0.0, writable=False)
    Ngy = NgY

    NgZ = FloatField(default_value=0.0, writable=False)
    Ngz = NgZ


class NgField(Float3CompoundBaseField[NgAttrOperator, NgPlugOperator]):
    __slots__ = ()

    ATTR_CLS = NgAttrOperator
    PLUG_CLS = NgPlugOperator

    NgX = FloatField(default_value=0.0, writable=False)
    Ngx = NgX

    NgY = FloatField(default_value=0.0, writable=False)
    Ngy = NgY

    NgZ = FloatField(default_value=0.0, writable=False)
    Ngz = NgZ


class NgfPlugOperator(Float3CompoundBasePlugOperator["NgfAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("NgfX", "Ngfx"),
        ("NgfY", "Ngfy"),
        ("NgfZ", "Ngfz"),
    )

    NgfX = FloatField(default_value=0.0, writable=False)
    Ngfx = NgfX

    NgfY = FloatField(default_value=0.0, writable=False)
    Ngfy = NgfY

    NgfZ = FloatField(default_value=0.0, writable=False)
    Ngfz = NgfZ


class NgfAttrOperator(Float3CompoundBaseAttrOperator[NgfPlugOperator]):
    __slots__ = ()

    NgfX = FloatField(default_value=0.0, writable=False)
    Ngfx = NgfX

    NgfY = FloatField(default_value=0.0, writable=False)
    Ngfy = NgfY

    NgfZ = FloatField(default_value=0.0, writable=False)
    Ngfz = NgfZ


class NgfField(Float3CompoundBaseField[NgfAttrOperator, NgfPlugOperator]):
    __slots__ = ()

    ATTR_CLS = NgfAttrOperator
    PLUG_CLS = NgfPlugOperator

    NgfX = FloatField(default_value=0.0, writable=False)
    Ngfx = NgfX

    NgfY = FloatField(default_value=0.0, writable=False)
    Ngfy = NgfY

    NgfZ = FloatField(default_value=0.0, writable=False)
    Ngfz = NgfZ


class NsPlugOperator(Float3CompoundBasePlugOperator["NsAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("NsX", "Nsx"),
        ("NsY", "Nsy"),
        ("NsZ", "Nsz"),
    )

    NsX = FloatField(default_value=0.0, writable=False)
    Nsx = NsX

    NsY = FloatField(default_value=0.0, writable=False)
    Nsy = NsY

    NsZ = FloatField(default_value=0.0, writable=False)
    Nsz = NsZ


class NsAttrOperator(Float3CompoundBaseAttrOperator[NsPlugOperator]):
    __slots__ = ()

    NsX = FloatField(default_value=0.0, writable=False)
    Nsx = NsX

    NsY = FloatField(default_value=0.0, writable=False)
    Nsy = NsY

    NsZ = FloatField(default_value=0.0, writable=False)
    Nsz = NsZ


class NsField(Float3CompoundBaseField[NsAttrOperator, NsPlugOperator]):
    __slots__ = ()

    ATTR_CLS = NsAttrOperator
    PLUG_CLS = NsPlugOperator

    NsX = FloatField(default_value=0.0, writable=False)
    Nsx = NsX

    NsY = FloatField(default_value=0.0, writable=False)
    Nsy = NsY

    NsZ = FloatField(default_value=0.0, writable=False)
    Nsz = NsZ


class DPduPlugOperator(Float3CompoundBasePlugOperator["DPduAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dPduX", "dPdux"),
        ("dPduY", "dPduy"),
        ("dPduZ", "dPduz"),
    )

    dPduX = FloatField(default_value=0.0, writable=False)
    dPdux = dPduX

    dPduY = FloatField(default_value=0.0, writable=False)
    dPduy = dPduY

    dPduZ = FloatField(default_value=0.0, writable=False)
    dPduz = dPduZ


class DPduAttrOperator(Float3CompoundBaseAttrOperator[DPduPlugOperator]):
    __slots__ = ()

    dPduX = FloatField(default_value=0.0, writable=False)
    dPdux = dPduX

    dPduY = FloatField(default_value=0.0, writable=False)
    dPduy = dPduY

    dPduZ = FloatField(default_value=0.0, writable=False)
    dPduz = dPduZ


class DPduField(Float3CompoundBaseField[DPduAttrOperator, DPduPlugOperator]):
    __slots__ = ()

    ATTR_CLS = DPduAttrOperator
    PLUG_CLS = DPduPlugOperator

    dPduX = FloatField(default_value=0.0, writable=False)
    dPdux = dPduX

    dPduY = FloatField(default_value=0.0, writable=False)
    dPduy = dPduY

    dPduZ = FloatField(default_value=0.0, writable=False)
    dPduz = dPduZ


class DPdvPlugOperator(Float3CompoundBasePlugOperator["DPdvAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dPdvX", "dPdvx"),
        ("dPdvY", "dPdvy"),
        ("dPdvZ", "dPdvz"),
    )

    dPdvX = FloatField(default_value=0.0, writable=False)
    dPdvx = dPdvX

    dPdvY = FloatField(default_value=0.0, writable=False)
    dPdvy = dPdvY

    dPdvZ = FloatField(default_value=0.0, writable=False)
    dPdvz = dPdvZ


class DPdvAttrOperator(Float3CompoundBaseAttrOperator[DPdvPlugOperator]):
    __slots__ = ()

    dPdvX = FloatField(default_value=0.0, writable=False)
    dPdvx = dPdvX

    dPdvY = FloatField(default_value=0.0, writable=False)
    dPdvy = dPdvY

    dPdvZ = FloatField(default_value=0.0, writable=False)
    dPdvz = dPdvZ


class DPdvField(Float3CompoundBaseField[DPdvAttrOperator, DPdvPlugOperator]):
    __slots__ = ()

    ATTR_CLS = DPdvAttrOperator
    PLUG_CLS = DPdvPlugOperator

    dPdvX = FloatField(default_value=0.0, writable=False)
    dPdvx = dPdvX

    dPdvY = FloatField(default_value=0.0, writable=False)
    dPdvy = dPdvY

    dPdvZ = FloatField(default_value=0.0, writable=False)
    dPdvz = dPdvZ


class DDdxPlugOperator(Float3CompoundBasePlugOperator["DDdxAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dDdxX", "dDdxx"),
        ("dDdxY", "dDdxy"),
        ("dDdxZ", "dDdxz"),
    )

    dDdxX = FloatField(default_value=0.0, writable=False)
    dDdxx = dDdxX

    dDdxY = FloatField(default_value=0.0, writable=False)
    dDdxy = dDdxY

    dDdxZ = FloatField(default_value=0.0, writable=False)
    dDdxz = dDdxZ


class DDdxAttrOperator(Float3CompoundBaseAttrOperator[DDdxPlugOperator]):
    __slots__ = ()

    dDdxX = FloatField(default_value=0.0, writable=False)
    dDdxx = dDdxX

    dDdxY = FloatField(default_value=0.0, writable=False)
    dDdxy = dDdxY

    dDdxZ = FloatField(default_value=0.0, writable=False)
    dDdxz = dDdxZ


class DDdxField(Float3CompoundBaseField[DDdxAttrOperator, DDdxPlugOperator]):
    __slots__ = ()

    ATTR_CLS = DDdxAttrOperator
    PLUG_CLS = DDdxPlugOperator

    dDdxX = FloatField(default_value=0.0, writable=False)
    dDdxx = dDdxX

    dDdxY = FloatField(default_value=0.0, writable=False)
    dDdxy = dDdxY

    dDdxZ = FloatField(default_value=0.0, writable=False)
    dDdxz = dDdxZ


class DDdyPlugOperator(Float3CompoundBasePlugOperator["DDdyAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dDdyX", "dDdyx"),
        ("dDdyY", "dDdyy"),
        ("dDdyZ", "dDdyz"),
    )

    dDdyX = FloatField(default_value=0.0, writable=False)
    dDdyx = dDdyX

    dDdyY = FloatField(default_value=0.0, writable=False)
    dDdyy = dDdyY

    dDdyZ = FloatField(default_value=0.0, writable=False)
    dDdyz = dDdyZ


class DDdyAttrOperator(Float3CompoundBaseAttrOperator[DDdyPlugOperator]):
    __slots__ = ()

    dDdyX = FloatField(default_value=0.0, writable=False)
    dDdyx = dDdyX

    dDdyY = FloatField(default_value=0.0, writable=False)
    dDdyy = dDdyY

    dDdyZ = FloatField(default_value=0.0, writable=False)
    dDdyz = dDdyZ


class DDdyField(Float3CompoundBaseField[DDdyAttrOperator, DDdyPlugOperator]):
    __slots__ = ()

    ATTR_CLS = DDdyAttrOperator
    PLUG_CLS = DDdyPlugOperator

    dDdyX = FloatField(default_value=0.0, writable=False)
    dDdyx = dDdyX

    dDdyY = FloatField(default_value=0.0, writable=False)
    dDdyy = dDdyY

    dDdyZ = FloatField(default_value=0.0, writable=False)
    dDdyz = dDdyZ


class DNdxPlugOperator(Float3CompoundBasePlugOperator["DNdxAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dNdxX", "dNdxx"),
        ("dNdxY", "dNdxy"),
        ("dNdxZ", "dNdxz"),
    )

    dNdxX = FloatField(default_value=0.0, writable=False)
    dNdxx = dNdxX

    dNdxY = FloatField(default_value=0.0, writable=False)
    dNdxy = dNdxY

    dNdxZ = FloatField(default_value=0.0, writable=False)
    dNdxz = dNdxZ


class DNdxAttrOperator(Float3CompoundBaseAttrOperator[DNdxPlugOperator]):
    __slots__ = ()

    dNdxX = FloatField(default_value=0.0, writable=False)
    dNdxx = dNdxX

    dNdxY = FloatField(default_value=0.0, writable=False)
    dNdxy = dNdxY

    dNdxZ = FloatField(default_value=0.0, writable=False)
    dNdxz = dNdxZ


class DNdxField(Float3CompoundBaseField[DNdxAttrOperator, DNdxPlugOperator]):
    __slots__ = ()

    ATTR_CLS = DNdxAttrOperator
    PLUG_CLS = DNdxPlugOperator

    dNdxX = FloatField(default_value=0.0, writable=False)
    dNdxx = dNdxX

    dNdxY = FloatField(default_value=0.0, writable=False)
    dNdxy = dNdxY

    dNdxZ = FloatField(default_value=0.0, writable=False)
    dNdxz = dNdxZ


class DNdyPlugOperator(Float3CompoundBasePlugOperator["DNdyAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dNdyX", "dNdyx"),
        ("dNdyY", "dNdyy"),
        ("dNdyZ", "dNdyz"),
    )

    dNdyX = FloatField(default_value=0.0, writable=False)
    dNdyx = dNdyX

    dNdyY = FloatField(default_value=0.0, writable=False)
    dNdyy = dNdyY

    dNdyZ = FloatField(default_value=0.0, writable=False)
    dNdyz = dNdyZ


class DNdyAttrOperator(Float3CompoundBaseAttrOperator[DNdyPlugOperator]):
    __slots__ = ()

    dNdyX = FloatField(default_value=0.0, writable=False)
    dNdyx = dNdyX

    dNdyY = FloatField(default_value=0.0, writable=False)
    dNdyy = dNdyY

    dNdyZ = FloatField(default_value=0.0, writable=False)
    dNdyz = dNdyZ


class DNdyField(Float3CompoundBaseField[DNdyAttrOperator, DNdyPlugOperator]):
    __slots__ = ()

    ATTR_CLS = DNdyAttrOperator
    PLUG_CLS = DNdyPlugOperator

    dNdyX = FloatField(default_value=0.0, writable=False)
    dNdyx = dNdyX

    dNdyY = FloatField(default_value=0.0, writable=False)
    dNdyy = dNdyY

    dNdyZ = FloatField(default_value=0.0, writable=False)
    dNdyz = dNdyZ
