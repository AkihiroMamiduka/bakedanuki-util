# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.rigid_solver import (
    ConstraintRotateField,
    ConstraintTranslateField,
    GeneralForceField,
    RotateField,
    TranslateField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar.time import TimeField


class SolverMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MIDPOINT = 0
    RUNGE_KUTTA = 1
    RUNGE_KUTTA_ADAPTIVE = 2


class SolverMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MIDPOINT = 0
    RUNGE_KUTTA = 1
    RUNGE_KUTTA_ADAPTIVE = 2

    NAME_MAP = {
        MIDPOINT: "MidPoint",
        RUNGE_KUTTA: "Runge Kutta",
        RUNGE_KUTTA_ADAPTIVE: "Runge Kutta Adaptive",
    }


class SolverMethodEnumField(
    EnumField[SolverMethodEnumAttrOperator, SolverMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SolverMethodEnumAttrOperator
    PLUG_CLS = SolverMethodEnumPlugOperator


class RigidSolver(DG):
    __slots__ = ()

    NODE_TYPE = "rigidSolver"

    currentTime = TimeField(default_value=0.0)
    ct = currentTime

    startTime = TimeField(default_value=0.0)
    stm = startTime

    deltaTime = TimeField(default_value=0.0)
    dtm = deltaTime

    lastSceneTime = TimeField(default_value=0.0)
    lst = lastSceneTime

    generalForce = GeneralForceField(multi=True)
    gfr = generalForce

    translate = TranslateField(multi=True, default_value=(0.0, 0.0, 0.0))
    t = translate

    rotate = RotateField(multi=True, default_value=(0.0, 0.0, 0.0))
    r = rotate

    constraintTranslate = ConstraintTranslateField(multi=True, default_value=(0.0, 0.0, 0.0))
    ctr = constraintTranslate

    constraintRotate = ConstraintRotateField(multi=True, default_value=(0.0, 0.0, 0.0))
    cr = constraintRotate

    collisionTolerance = DoubleField(default_value=0.02)
    ctl = collisionTolerance

    stepSize = DoubleField(default_value=0.03)
    ss = stepSize

    scaleVelocity = DoubleField(default_value=1.0)
    svv = scaleVelocity

    rigidBodyCount = LongField(default_value=0, writable=False)
    rbc = rigidBodyCount

    solverMethod = SolverMethodEnumField(default_value=2)
    slm = solverMethod

    friction = BoolField(default_value=True)
    f = friction

    bounciness = BoolField(default_value=True)
    b = bounciness

    dynamics = BoolField(default_value=True)
    dyn = dynamics

    autoSolverTolerances = BoolField(default_value=False)
    ast = autoSolverTolerances

    displayVelocity = BoolField(default_value=False)
    dv = displayVelocity

    displayCenterOfMass = BoolField(default_value=True)
    dcom = displayCenterOfMass

    displayConstraint = BoolField(default_value=True)
    dc = displayConstraint

    displayLabel = BoolField(default_value=False)
    dl = displayLabel

    cacheData = BoolField(default_value=False)
    cd = cacheData

    contactData = BoolField(default_value=False)
    ctd = contactData

    state = BoolField(default_value=True)
    stt = state

    current = BoolField(default_value=False)
    cur = current

    forceDynamics = BoolField(default_value=False)
    fdn = forceDynamics

    allowDisconnection = BoolField(default_value=False)
    ad = allowDisconnection

    solving = BoolField(default_value=False)
    sol = solving

    statistics = BoolField(default_value=False)
    st = statistics
