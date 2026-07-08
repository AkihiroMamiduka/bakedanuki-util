# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_state_vector import (
    DDdxField,
    DDdyField,
    DNdxField,
    DNdyField,
    DPduField,
    DPdvField,
    DPdxField,
    DPdyField,
    NField,
    NfField,
    NgField,
    NgfField,
    NsField,
    OutValueField,
    PField,
    PoField,
    RdField,
    RoField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)


class VariableEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RO = 0
    RD = 1
    PO = 2
    P = 3
    DPDX = 4
    DPDY = 5
    N = 6
    NF = 7
    NG = 8
    NGF = 9
    NS = 10
    DPDU = 11
    DPDV = 12
    DDDX = 13
    DDDY = 14
    DNDX = 15
    DNDY = 16


class VariableEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RO = 0
    RD = 1
    PO = 2
    P = 3
    DPDX = 4
    DPDY = 5
    N = 6
    NF = 7
    NG = 8
    NGF = 9
    NS = 10
    DPDU = 11
    DPDV = 12
    DDDX = 13
    DDDY = 14
    DNDX = 15
    DNDY = 16

    NAME_MAP = {
        RO: "Ro",
        RD: "Rd",
        PO: "Po",
        P: "P",
        DPDX: "dPdx",
        DPDY: "dPdy",
        N: "N",
        NF: "Nf",
        NG: "Ng",
        NGF: "Ngf",
        NS: "Ns",
        DPDU: "dPdu",
        DPDV: "dPdv",
        DDDX: "dDdx",
        DDDY: "dDdy",
        DNDX: "dNdx",
        DNDY: "dNdy",
    }


class VariableEnumField(
    EnumField[VariableEnumAttrOperator, VariableEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VariableEnumAttrOperator
    PLUG_CLS = VariableEnumPlugOperator


class AiStateVector(DG):
    __slots__ = ()

    NODE_TYPE = "aiStateVector"

    outValue = OutValueField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outValue
    outValueX = outValue.outValueX
    outx = outValueX
    outValueY = outValue.outValueY
    outy = outValueY
    outValueZ = outValue.outValueZ
    outz = outValueZ

    Ro = RoField(default_value=(0.0, 0.0, 0.0), writable=False)
    RoX = Ro.RoX
    Rox = RoX
    RoY = Ro.RoY
    Roy = RoY
    RoZ = Ro.RoZ
    Roz = RoZ

    Rd = RdField(default_value=(0.0, 0.0, 0.0), writable=False)
    RdX = Rd.RdX
    Rdx = RdX
    RdY = Rd.RdY
    Rdy = RdY
    RdZ = Rd.RdZ
    Rdz = RdZ

    Po = PoField(default_value=(0.0, 0.0, 0.0), writable=False)
    PoX = Po.PoX
    Pox = PoX
    PoY = Po.PoY
    Poy = PoY
    PoZ = Po.PoZ
    Poz = PoZ

    P = PField(default_value=(0.0, 0.0, 0.0), writable=False)
    PX = P.PX
    Px = PX
    PY = P.PY
    Py = PY
    PZ = P.PZ
    Pz = PZ

    dPdx = DPdxField(default_value=(0.0, 0.0, 0.0), writable=False)
    dPdxX = dPdx.dPdxX
    dPdxx = dPdxX
    dPdxY = dPdx.dPdxY
    dPdxy = dPdxY
    dPdxZ = dPdx.dPdxZ
    dPdxz = dPdxZ

    dPdy = DPdyField(default_value=(0.0, 0.0, 0.0), writable=False)
    dPdyX = dPdy.dPdyX
    dPdyx = dPdyX
    dPdyY = dPdy.dPdyY
    dPdyy = dPdyY
    dPdyZ = dPdy.dPdyZ
    dPdyz = dPdyZ

    N = NField(default_value=(0.0, 0.0, 0.0), writable=False)
    NX = N.NX
    Nx = NX
    NY = N.NY
    Ny = NY
    NZ = N.NZ
    Nz = NZ

    Nf = NfField(default_value=(0.0, 0.0, 0.0), writable=False)
    NfX = Nf.NfX
    Nfx = NfX
    NfY = Nf.NfY
    Nfy = NfY
    NfZ = Nf.NfZ
    Nfz = NfZ

    Ng = NgField(default_value=(0.0, 0.0, 0.0), writable=False)
    NgX = Ng.NgX
    Ngx = NgX
    NgY = Ng.NgY
    Ngy = NgY
    NgZ = Ng.NgZ
    Ngz = NgZ

    Ngf = NgfField(default_value=(0.0, 0.0, 0.0), writable=False)
    NgfX = Ngf.NgfX
    Ngfx = NgfX
    NgfY = Ngf.NgfY
    Ngfy = NgfY
    NgfZ = Ngf.NgfZ
    Ngfz = NgfZ

    Ns = NsField(default_value=(0.0, 0.0, 0.0), writable=False)
    NsX = Ns.NsX
    Nsx = NsX
    NsY = Ns.NsY
    Nsy = NsY
    NsZ = Ns.NsZ
    Nsz = NsZ

    dPdu = DPduField(default_value=(0.0, 0.0, 0.0), writable=False)
    dPduX = dPdu.dPduX
    dPdux = dPduX
    dPduY = dPdu.dPduY
    dPduy = dPduY
    dPduZ = dPdu.dPduZ
    dPduz = dPduZ

    dPdv = DPdvField(default_value=(0.0, 0.0, 0.0), writable=False)
    dPdvX = dPdv.dPdvX
    dPdvx = dPdvX
    dPdvY = dPdv.dPdvY
    dPdvy = dPdvY
    dPdvZ = dPdv.dPdvZ
    dPdvz = dPdvZ

    dDdx = DDdxField(default_value=(0.0, 0.0, 0.0), writable=False)
    dDdxX = dDdx.dDdxX
    dDdxx = dDdxX
    dDdxY = dDdx.dDdxY
    dDdxy = dDdxY
    dDdxZ = dDdx.dDdxZ
    dDdxz = dDdxZ

    dDdy = DDdyField(default_value=(0.0, 0.0, 0.0), writable=False)
    dDdyX = dDdy.dDdyX
    dDdyx = dDdyX
    dDdyY = dDdy.dDdyY
    dDdyy = dDdyY
    dDdyZ = dDdy.dDdyZ
    dDdyz = dDdyZ

    dNdx = DNdxField(default_value=(0.0, 0.0, 0.0), writable=False)
    dNdxX = dNdx.dNdxX
    dNdxx = dNdxX
    dNdxY = dNdx.dNdxY
    dNdxy = dNdxY
    dNdxZ = dNdx.dNdxZ
    dNdxz = dNdxZ

    dNdy = DNdyField(default_value=(0.0, 0.0, 0.0), writable=False)
    dNdyX = dNdy.dNdyX
    dNdyx = dNdyX
    dNdyY = dNdy.dNdyY
    dNdyy = dNdyY
    dNdyZ = dNdy.dNdyZ
    dNdyz = dNdyZ

    variable = VariableEnumField(default_value=0)
