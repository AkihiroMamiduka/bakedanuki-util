# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.typed import TypedField


class ForceActorSpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ForceActorSpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ForceActorSpaceEnumField(
    EnumField[ForceActorSpaceEnumAttrOperator, ForceActorSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ForceActorSpaceEnumAttrOperator
    PLUG_CLS = ForceActorSpaceEnumPlugOperator


class ScaleCompensationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AUTO = 1
    USER = 2


class ScaleCompensationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AUTO = 1
    USER = 2

    NAME_MAP = {
        OFF: "Off",
        AUTO: "Auto",
        USER: "User",
    }


class ScaleCompensationModeEnumField(
    EnumField[ScaleCompensationModeEnumAttrOperator, ScaleCompensationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleCompensationModeEnumAttrOperator
    PLUG_CLS = ScaleCompensationModeEnumPlugOperator


class MassCenterCompensationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class MassCenterCompensationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class MassCenterCompensationModeEnumField(
    EnumField[MassCenterCompensationModeEnumAttrOperator, MassCenterCompensationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MassCenterCompensationModeEnumAttrOperator
    PLUG_CLS = MassCenterCompensationModeEnumPlugOperator


class AnkleHeightCompensationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AUTO = 1
    USER = 2


class AnkleHeightCompensationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AUTO = 1
    USER = 2

    NAME_MAP = {
        OFF: "Off",
        AUTO: "Auto",
        USER: "User",
    }


class AnkleHeightCompensationModeEnumField(
    EnumField[AnkleHeightCompensationModeEnumAttrOperator, AnkleHeightCompensationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AnkleHeightCompensationModeEnumAttrOperator
    PLUG_CLS = AnkleHeightCompensationModeEnumPlugOperator


class AnkleProximityCompensationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AUTO = 1
    USER = 2


class AnkleProximityCompensationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AUTO = 1
    USER = 2

    NAME_MAP = {
        OFF: "Off",
        AUTO: "Auto",
        USER: "User",
    }


class AnkleProximityCompensationModeEnumField(
    EnumField[AnkleProximityCompensationModeEnumAttrOperator, AnkleProximityCompensationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AnkleProximityCompensationModeEnumAttrOperator
    PLUG_CLS = AnkleProximityCompensationModeEnumPlugOperator


class HipsHeightCompensationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AUTO = 1
    USER = 2


class HipsHeightCompensationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AUTO = 1
    USER = 2

    NAME_MAP = {
        OFF: "Off",
        AUTO: "Auto",
        USER: "User",
    }


class HipsHeightCompensationModeEnumField(
    EnumField[HipsHeightCompensationModeEnumAttrOperator, HipsHeightCompensationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsHeightCompensationModeEnumAttrOperator
    PLUG_CLS = HipsHeightCompensationModeEnumPlugOperator


class FloorContactEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class FloorContactEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class FloorContactEnumField(
    EnumField[FloorContactEnumAttrOperator, FloorContactEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FloorContactEnumAttrOperator
    PLUG_CLS = FloorContactEnumPlugOperator


class HandFloorContactEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class HandFloorContactEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class HandFloorContactEnumField(
    EnumField[HandFloorContactEnumAttrOperator, HandFloorContactEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HandFloorContactEnumAttrOperator
    PLUG_CLS = HandFloorContactEnumPlugOperator


class HandContactTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 0
    WRIST = 1
    FINGERBASE = 2
    HOOF = 3


class HandContactTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 0
    WRIST = 1
    FINGERBASE = 2
    HOOF = 3

    NAME_MAP = {
        NORMAL: "Normal",
        WRIST: "Wrist",
        FINGERBASE: "FingerBase",
        HOOF: "Hoof",
    }


class HandContactTypeEnumField(
    EnumField[HandContactTypeEnumAttrOperator, HandContactTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HandContactTypeEnumAttrOperator
    PLUG_CLS = HandContactTypeEnumPlugOperator


class HandFingerContactEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class HandFingerContactEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class HandFingerContactEnumField(
    EnumField[HandFingerContactEnumAttrOperator, HandFingerContactEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HandFingerContactEnumAttrOperator
    PLUG_CLS = HandFingerContactEnumPlugOperator


class HandFingerContactModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    STICKY = 0
    SPREAD = 1
    STICKY_AMP_SPREAD = 2


class HandFingerContactModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    STICKY = 0
    SPREAD = 1
    STICKY_AMP_SPREAD = 2

    NAME_MAP = {
        STICKY: "Sticky",
        SPREAD: "Spread",
        STICKY_AMP_SPREAD: "Sticky & Spread",
    }


class HandFingerContactModeEnumField(
    EnumField[HandFingerContactModeEnumAttrOperator, HandFingerContactModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HandFingerContactModeEnumAttrOperator
    PLUG_CLS = HandFingerContactModeEnumPlugOperator


class FootContactTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 0
    ANKLE = 1
    TOEBASE = 2
    HOOF = 3


class FootContactTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 0
    ANKLE = 1
    TOEBASE = 2
    HOOF = 3

    NAME_MAP = {
        NORMAL: "Normal",
        ANKLE: "Ankle",
        TOEBASE: "ToeBase",
        HOOF: "Hoof",
    }


class FootContactTypeEnumField(
    EnumField[FootContactTypeEnumAttrOperator, FootContactTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FootContactTypeEnumAttrOperator
    PLUG_CLS = FootContactTypeEnumPlugOperator


class FootFingerContactEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class FootFingerContactEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class FootFingerContactEnumField(
    EnumField[FootFingerContactEnumAttrOperator, FootFingerContactEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FootFingerContactEnumAttrOperator
    PLUG_CLS = FootFingerContactEnumPlugOperator


class FootFingerContactModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    STICKY = 0
    SPREAD = 1
    STICKY_AMP_SPREAD = 2


class FootFingerContactModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    STICKY = 0
    SPREAD = 1
    STICKY_AMP_SPREAD = 2

    NAME_MAP = {
        STICKY: "Sticky",
        SPREAD: "Spread",
        STICKY_AMP_SPREAD: "Sticky & Spread",
    }


class FootFingerContactModeEnumField(
    EnumField[FootFingerContactModeEnumAttrOperator, FootFingerContactModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FootFingerContactModeEnumAttrOperator
    PLUG_CLS = FootFingerContactModeEnumPlugOperator


class LeftUpLegRollModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LeftUpLegRollModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LeftUpLegRollModeEnumField(
    EnumField[LeftUpLegRollModeEnumAttrOperator, LeftUpLegRollModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftUpLegRollModeEnumAttrOperator
    PLUG_CLS = LeftUpLegRollModeEnumPlugOperator


class LeftLegRollModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LeftLegRollModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LeftLegRollModeEnumField(
    EnumField[LeftLegRollModeEnumAttrOperator, LeftLegRollModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftLegRollModeEnumAttrOperator
    PLUG_CLS = LeftLegRollModeEnumPlugOperator


class RightUpLegRollModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class RightUpLegRollModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class RightUpLegRollModeEnumField(
    EnumField[RightUpLegRollModeEnumAttrOperator, RightUpLegRollModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightUpLegRollModeEnumAttrOperator
    PLUG_CLS = RightUpLegRollModeEnumPlugOperator


class RightLegRollModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class RightLegRollModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class RightLegRollModeEnumField(
    EnumField[RightLegRollModeEnumAttrOperator, RightLegRollModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightLegRollModeEnumAttrOperator
    PLUG_CLS = RightLegRollModeEnumPlugOperator


class LeftArmRollModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LeftArmRollModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LeftArmRollModeEnumField(
    EnumField[LeftArmRollModeEnumAttrOperator, LeftArmRollModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftArmRollModeEnumAttrOperator
    PLUG_CLS = LeftArmRollModeEnumPlugOperator


class LeftForeArmRollModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LeftForeArmRollModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LeftForeArmRollModeEnumField(
    EnumField[LeftForeArmRollModeEnumAttrOperator, LeftForeArmRollModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftForeArmRollModeEnumAttrOperator
    PLUG_CLS = LeftForeArmRollModeEnumPlugOperator


class RightArmRollModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class RightArmRollModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class RightArmRollModeEnumField(
    EnumField[RightArmRollModeEnumAttrOperator, RightArmRollModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightArmRollModeEnumAttrOperator
    PLUG_CLS = RightArmRollModeEnumPlugOperator


class RightForeArmRollModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class RightForeArmRollModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class RightForeArmRollModeEnumField(
    EnumField[RightForeArmRollModeEnumAttrOperator, RightForeArmRollModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightForeArmRollModeEnumAttrOperator
    PLUG_CLS = RightForeArmRollModeEnumPlugOperator


class MirrorEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class MirrorEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class MirrorEnumField(
    EnumField[MirrorEnumAttrOperator, MirrorEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MirrorEnumAttrOperator
    PLUG_CLS = MirrorEnumPlugOperator


class LeftKneeKillPitchEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LeftKneeKillPitchEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LeftKneeKillPitchEnumField(
    EnumField[LeftKneeKillPitchEnumAttrOperator, LeftKneeKillPitchEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftKneeKillPitchEnumAttrOperator
    PLUG_CLS = LeftKneeKillPitchEnumPlugOperator


class RightKneeKillPitchEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class RightKneeKillPitchEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class RightKneeKillPitchEnumField(
    EnumField[RightKneeKillPitchEnumAttrOperator, RightKneeKillPitchEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightKneeKillPitchEnumAttrOperator
    PLUG_CLS = RightKneeKillPitchEnumPlugOperator


class LeftElbowKillPitchEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LeftElbowKillPitchEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LeftElbowKillPitchEnumField(
    EnumField[LeftElbowKillPitchEnumAttrOperator, LeftElbowKillPitchEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftElbowKillPitchEnumAttrOperator
    PLUG_CLS = LeftElbowKillPitchEnumPlugOperator


class RightElbowKillPitchEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class RightElbowKillPitchEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class RightElbowKillPitchEnumField(
    EnumField[RightElbowKillPitchEnumAttrOperator, RightElbowKillPitchEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightElbowKillPitchEnumAttrOperator
    PLUG_CLS = RightElbowKillPitchEnumPlugOperator


class AutomaticToesEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class AutomaticToesEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class AutomaticToesEnumField(
    EnumField[AutomaticToesEnumAttrOperator, AutomaticToesEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AutomaticToesEnumAttrOperator
    PLUG_CLS = AutomaticToesEnumPlugOperator


class FloorPivotEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTO = 0
    ANKLE = 1
    TOES = 2


class FloorPivotEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTO = 0
    ANKLE = 1
    TOES = 2

    NAME_MAP = {
        AUTO: "Auto",
        ANKLE: "Ankle",
        TOES: "Toes",
    }


class FloorPivotEnumField(
    EnumField[FloorPivotEnumAttrOperator, FloorPivotEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FloorPivotEnumAttrOperator
    PLUG_CLS = FloorPivotEnumPlugOperator


class PostureEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BIPED = 0
    QUADRUPED = 1


class PostureEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BIPED = 0
    QUADRUPED = 1

    NAME_MAP = {
        BIPED: "Biped",
        QUADRUPED: "Quadruped",
    }


class PostureEnumField(
    EnumField[PostureEnumAttrOperator, PostureEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PostureEnumAttrOperator
    PLUG_CLS = PostureEnumPlugOperator


class AutomaticFingersEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class AutomaticFingersEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class AutomaticFingersEnumField(
    EnumField[AutomaticFingersEnumAttrOperator, AutomaticFingersEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AutomaticFingersEnumAttrOperator
    PLUG_CLS = AutomaticFingersEnumPlugOperator


class HandFloorPivotEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTO = 0
    WRIST = 1
    FINGERS = 2


class HandFloorPivotEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTO = 0
    WRIST = 1
    FINGERS = 2

    NAME_MAP = {
        AUTO: "Auto",
        WRIST: "Wrist",
        FINGERS: "Fingers",
    }


class HandFloorPivotEnumField(
    EnumField[HandFloorPivotEnumAttrOperator, HandFloorPivotEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HandFloorPivotEnumAttrOperator
    PLUG_CLS = HandFloorPivotEnumPlugOperator


class HipsTranslationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD_RIGID = 0
    BODY_RIGID = 1
    TRAJECTORY = 2


class HipsTranslationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD_RIGID = 0
    BODY_RIGID = 1
    TRAJECTORY = 2

    NAME_MAP = {
        WORLD_RIGID: "World Rigid",
        BODY_RIGID: "Body Rigid",
        TRAJECTORY: "Trajectory",
    }


class HipsTranslationModeEnumField(
    EnumField[HipsTranslationModeEnumAttrOperator, HipsTranslationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsTranslationModeEnumAttrOperator
    PLUG_CLS = HipsTranslationModeEnumPlugOperator


class FingerSolvingEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class FingerSolvingEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class FingerSolvingEnumField(
    EnumField[FingerSolvingEnumAttrOperator, FingerSolvingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FingerSolvingEnumAttrOperator
    PLUG_CLS = FingerSolvingEnumPlugOperator


class RollExtractionModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RELATIVE = 0
    ABSOLUTE = 1


class RollExtractionModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RELATIVE = 0
    ABSOLUTE = 1

    NAME_MAP = {
        RELATIVE: "Relative",
        ABSOLUTE: "Absolute",
    }


class RollExtractionModeEnumField(
    EnumField[RollExtractionModeEnumAttrOperator, RollExtractionModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RollExtractionModeEnumAttrOperator
    PLUG_CLS = RollExtractionModeEnumPlugOperator


class FingerPropagationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class FingerPropagationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class FingerPropagationEnumField(
    EnumField[FingerPropagationEnumAttrOperator, FingerPropagationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FingerPropagationEnumAttrOperator
    PLUG_CLS = FingerPropagationEnumPlugOperator


class SnSSmoothReachEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class SnSSmoothReachEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class SnSSmoothReachEnumField(
    EnumField[SnSSmoothReachEnumAttrOperator, SnSSmoothReachEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SnSSmoothReachEnumAttrOperator
    PLUG_CLS = SnSSmoothReachEnumPlugOperator


class LockXEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LockXEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LockXEnumField(
    EnumField[LockXEnumAttrOperator, LockXEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LockXEnumAttrOperator
    PLUG_CLS = LockXEnumPlugOperator


class LockYEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LockYEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LockYEnumField(
    EnumField[LockYEnumAttrOperator, LockYEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LockYEnumAttrOperator
    PLUG_CLS = LockYEnumPlugOperator


class LockZEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LockZEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LockZEnumField(
    EnumField[LockZEnumAttrOperator, LockZEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LockZEnumAttrOperator
    PLUG_CLS = LockZEnumPlugOperator


class ParamRealisticArmSolvingEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamRealisticArmSolvingEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamRealisticArmSolvingEnumField(
    EnumField[ParamRealisticArmSolvingEnumAttrOperator, ParamRealisticArmSolvingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamRealisticArmSolvingEnumAttrOperator
    PLUG_CLS = ParamRealisticArmSolvingEnumPlugOperator


class ParamLeafLeftUpLegRoll1ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftUpLegRoll1ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftUpLegRoll1ModeEnumField(
    EnumField[ParamLeafLeftUpLegRoll1ModeEnumAttrOperator, ParamLeafLeftUpLegRoll1ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftUpLegRoll1ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftUpLegRoll1ModeEnumPlugOperator


class ParamLeafLeftLegRoll1ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftLegRoll1ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftLegRoll1ModeEnumField(
    EnumField[ParamLeafLeftLegRoll1ModeEnumAttrOperator, ParamLeafLeftLegRoll1ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftLegRoll1ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftLegRoll1ModeEnumPlugOperator


class ParamLeafRightUpLegRoll1ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightUpLegRoll1ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightUpLegRoll1ModeEnumField(
    EnumField[ParamLeafRightUpLegRoll1ModeEnumAttrOperator, ParamLeafRightUpLegRoll1ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightUpLegRoll1ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightUpLegRoll1ModeEnumPlugOperator


class ParamLeafRightLegRoll1ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightLegRoll1ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightLegRoll1ModeEnumField(
    EnumField[ParamLeafRightLegRoll1ModeEnumAttrOperator, ParamLeafRightLegRoll1ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightLegRoll1ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightLegRoll1ModeEnumPlugOperator


class ParamLeafLeftArmRoll1ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftArmRoll1ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftArmRoll1ModeEnumField(
    EnumField[ParamLeafLeftArmRoll1ModeEnumAttrOperator, ParamLeafLeftArmRoll1ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftArmRoll1ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftArmRoll1ModeEnumPlugOperator


class ParamLeafLeftForeArmRoll1ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftForeArmRoll1ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftForeArmRoll1ModeEnumField(
    EnumField[ParamLeafLeftForeArmRoll1ModeEnumAttrOperator, ParamLeafLeftForeArmRoll1ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftForeArmRoll1ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftForeArmRoll1ModeEnumPlugOperator


class ParamLeafRightArmRoll1ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightArmRoll1ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightArmRoll1ModeEnumField(
    EnumField[ParamLeafRightArmRoll1ModeEnumAttrOperator, ParamLeafRightArmRoll1ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightArmRoll1ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightArmRoll1ModeEnumPlugOperator


class ParamLeafRightForeArmRoll1ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightForeArmRoll1ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightForeArmRoll1ModeEnumField(
    EnumField[ParamLeafRightForeArmRoll1ModeEnumAttrOperator, ParamLeafRightForeArmRoll1ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightForeArmRoll1ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightForeArmRoll1ModeEnumPlugOperator


class ParamLeafLeftUpLegRoll2ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftUpLegRoll2ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftUpLegRoll2ModeEnumField(
    EnumField[ParamLeafLeftUpLegRoll2ModeEnumAttrOperator, ParamLeafLeftUpLegRoll2ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftUpLegRoll2ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftUpLegRoll2ModeEnumPlugOperator


class ParamLeafLeftLegRoll2ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftLegRoll2ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftLegRoll2ModeEnumField(
    EnumField[ParamLeafLeftLegRoll2ModeEnumAttrOperator, ParamLeafLeftLegRoll2ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftLegRoll2ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftLegRoll2ModeEnumPlugOperator


class ParamLeafRightUpLegRoll2ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightUpLegRoll2ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightUpLegRoll2ModeEnumField(
    EnumField[ParamLeafRightUpLegRoll2ModeEnumAttrOperator, ParamLeafRightUpLegRoll2ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightUpLegRoll2ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightUpLegRoll2ModeEnumPlugOperator


class ParamLeafRightLegRoll2ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightLegRoll2ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightLegRoll2ModeEnumField(
    EnumField[ParamLeafRightLegRoll2ModeEnumAttrOperator, ParamLeafRightLegRoll2ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightLegRoll2ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightLegRoll2ModeEnumPlugOperator


class ParamLeafLeftArmRoll2ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftArmRoll2ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftArmRoll2ModeEnumField(
    EnumField[ParamLeafLeftArmRoll2ModeEnumAttrOperator, ParamLeafLeftArmRoll2ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftArmRoll2ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftArmRoll2ModeEnumPlugOperator


class ParamLeafLeftForeArmRoll2ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftForeArmRoll2ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftForeArmRoll2ModeEnumField(
    EnumField[ParamLeafLeftForeArmRoll2ModeEnumAttrOperator, ParamLeafLeftForeArmRoll2ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftForeArmRoll2ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftForeArmRoll2ModeEnumPlugOperator


class ParamLeafRightArmRoll2ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightArmRoll2ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightArmRoll2ModeEnumField(
    EnumField[ParamLeafRightArmRoll2ModeEnumAttrOperator, ParamLeafRightArmRoll2ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightArmRoll2ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightArmRoll2ModeEnumPlugOperator


class ParamLeafRightForeArmRoll2ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightForeArmRoll2ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightForeArmRoll2ModeEnumField(
    EnumField[ParamLeafRightForeArmRoll2ModeEnumAttrOperator, ParamLeafRightForeArmRoll2ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightForeArmRoll2ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightForeArmRoll2ModeEnumPlugOperator


class ParamLeafLeftUpLegRoll3ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftUpLegRoll3ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftUpLegRoll3ModeEnumField(
    EnumField[ParamLeafLeftUpLegRoll3ModeEnumAttrOperator, ParamLeafLeftUpLegRoll3ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftUpLegRoll3ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftUpLegRoll3ModeEnumPlugOperator


class ParamLeafLeftLegRoll3ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftLegRoll3ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftLegRoll3ModeEnumField(
    EnumField[ParamLeafLeftLegRoll3ModeEnumAttrOperator, ParamLeafLeftLegRoll3ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftLegRoll3ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftLegRoll3ModeEnumPlugOperator


class ParamLeafRightUpLegRoll3ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightUpLegRoll3ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightUpLegRoll3ModeEnumField(
    EnumField[ParamLeafRightUpLegRoll3ModeEnumAttrOperator, ParamLeafRightUpLegRoll3ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightUpLegRoll3ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightUpLegRoll3ModeEnumPlugOperator


class ParamLeafRightLegRoll3ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightLegRoll3ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightLegRoll3ModeEnumField(
    EnumField[ParamLeafRightLegRoll3ModeEnumAttrOperator, ParamLeafRightLegRoll3ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightLegRoll3ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightLegRoll3ModeEnumPlugOperator


class ParamLeafLeftArmRoll3ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftArmRoll3ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftArmRoll3ModeEnumField(
    EnumField[ParamLeafLeftArmRoll3ModeEnumAttrOperator, ParamLeafLeftArmRoll3ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftArmRoll3ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftArmRoll3ModeEnumPlugOperator


class ParamLeafLeftForeArmRoll3ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftForeArmRoll3ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftForeArmRoll3ModeEnumField(
    EnumField[ParamLeafLeftForeArmRoll3ModeEnumAttrOperator, ParamLeafLeftForeArmRoll3ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftForeArmRoll3ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftForeArmRoll3ModeEnumPlugOperator


class ParamLeafRightArmRoll3ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightArmRoll3ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightArmRoll3ModeEnumField(
    EnumField[ParamLeafRightArmRoll3ModeEnumAttrOperator, ParamLeafRightArmRoll3ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightArmRoll3ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightArmRoll3ModeEnumPlugOperator


class ParamLeafRightForeArmRoll3ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightForeArmRoll3ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightForeArmRoll3ModeEnumField(
    EnumField[ParamLeafRightForeArmRoll3ModeEnumAttrOperator, ParamLeafRightForeArmRoll3ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightForeArmRoll3ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightForeArmRoll3ModeEnumPlugOperator


class ParamLeafLeftUpLegRoll4ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftUpLegRoll4ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftUpLegRoll4ModeEnumField(
    EnumField[ParamLeafLeftUpLegRoll4ModeEnumAttrOperator, ParamLeafLeftUpLegRoll4ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftUpLegRoll4ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftUpLegRoll4ModeEnumPlugOperator


class ParamLeafLeftLegRoll4ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftLegRoll4ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftLegRoll4ModeEnumField(
    EnumField[ParamLeafLeftLegRoll4ModeEnumAttrOperator, ParamLeafLeftLegRoll4ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftLegRoll4ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftLegRoll4ModeEnumPlugOperator


class ParamLeafRightUpLegRoll4ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightUpLegRoll4ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightUpLegRoll4ModeEnumField(
    EnumField[ParamLeafRightUpLegRoll4ModeEnumAttrOperator, ParamLeafRightUpLegRoll4ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightUpLegRoll4ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightUpLegRoll4ModeEnumPlugOperator


class ParamLeafRightLegRoll4ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightLegRoll4ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightLegRoll4ModeEnumField(
    EnumField[ParamLeafRightLegRoll4ModeEnumAttrOperator, ParamLeafRightLegRoll4ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightLegRoll4ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightLegRoll4ModeEnumPlugOperator


class ParamLeafLeftArmRoll4ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftArmRoll4ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftArmRoll4ModeEnumField(
    EnumField[ParamLeafLeftArmRoll4ModeEnumAttrOperator, ParamLeafLeftArmRoll4ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftArmRoll4ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftArmRoll4ModeEnumPlugOperator


class ParamLeafLeftForeArmRoll4ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftForeArmRoll4ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftForeArmRoll4ModeEnumField(
    EnumField[ParamLeafLeftForeArmRoll4ModeEnumAttrOperator, ParamLeafLeftForeArmRoll4ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftForeArmRoll4ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftForeArmRoll4ModeEnumPlugOperator


class ParamLeafRightArmRoll4ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightArmRoll4ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightArmRoll4ModeEnumField(
    EnumField[ParamLeafRightArmRoll4ModeEnumAttrOperator, ParamLeafRightArmRoll4ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightArmRoll4ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightArmRoll4ModeEnumPlugOperator


class ParamLeafRightForeArmRoll4ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightForeArmRoll4ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightForeArmRoll4ModeEnumField(
    EnumField[ParamLeafRightForeArmRoll4ModeEnumAttrOperator, ParamLeafRightForeArmRoll4ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightForeArmRoll4ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightForeArmRoll4ModeEnumPlugOperator


class ParamLeafLeftUpLegRoll5ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftUpLegRoll5ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftUpLegRoll5ModeEnumField(
    EnumField[ParamLeafLeftUpLegRoll5ModeEnumAttrOperator, ParamLeafLeftUpLegRoll5ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftUpLegRoll5ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftUpLegRoll5ModeEnumPlugOperator


class ParamLeafLeftLegRoll5ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftLegRoll5ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftLegRoll5ModeEnumField(
    EnumField[ParamLeafLeftLegRoll5ModeEnumAttrOperator, ParamLeafLeftLegRoll5ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftLegRoll5ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftLegRoll5ModeEnumPlugOperator


class ParamLeafRightUpLegRoll5ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightUpLegRoll5ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightUpLegRoll5ModeEnumField(
    EnumField[ParamLeafRightUpLegRoll5ModeEnumAttrOperator, ParamLeafRightUpLegRoll5ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightUpLegRoll5ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightUpLegRoll5ModeEnumPlugOperator


class ParamLeafRightLegRoll5ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightLegRoll5ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightLegRoll5ModeEnumField(
    EnumField[ParamLeafRightLegRoll5ModeEnumAttrOperator, ParamLeafRightLegRoll5ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightLegRoll5ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightLegRoll5ModeEnumPlugOperator


class ParamLeafLeftArmRoll5ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftArmRoll5ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftArmRoll5ModeEnumField(
    EnumField[ParamLeafLeftArmRoll5ModeEnumAttrOperator, ParamLeafLeftArmRoll5ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftArmRoll5ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftArmRoll5ModeEnumPlugOperator


class ParamLeafLeftForeArmRoll5ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftForeArmRoll5ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftForeArmRoll5ModeEnumField(
    EnumField[ParamLeafLeftForeArmRoll5ModeEnumAttrOperator, ParamLeafLeftForeArmRoll5ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftForeArmRoll5ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftForeArmRoll5ModeEnumPlugOperator


class ParamLeafRightArmRoll5ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightArmRoll5ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightArmRoll5ModeEnumField(
    EnumField[ParamLeafRightArmRoll5ModeEnumAttrOperator, ParamLeafRightArmRoll5ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightArmRoll5ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightArmRoll5ModeEnumPlugOperator


class ParamLeafRightForeArmRoll5ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightForeArmRoll5ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightForeArmRoll5ModeEnumField(
    EnumField[ParamLeafRightForeArmRoll5ModeEnumAttrOperator, ParamLeafRightForeArmRoll5ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightForeArmRoll5ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightForeArmRoll5ModeEnumPlugOperator


class LeftLegFullRollExtractionModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LeftLegFullRollExtractionModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LeftLegFullRollExtractionModeEnumField(
    EnumField[LeftLegFullRollExtractionModeEnumAttrOperator, LeftLegFullRollExtractionModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftLegFullRollExtractionModeEnumAttrOperator
    PLUG_CLS = LeftLegFullRollExtractionModeEnumPlugOperator


class RightLegFullRollExtractionModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class RightLegFullRollExtractionModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class RightLegFullRollExtractionModeEnumField(
    EnumField[RightLegFullRollExtractionModeEnumAttrOperator, RightLegFullRollExtractionModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightLegFullRollExtractionModeEnumAttrOperator
    PLUG_CLS = RightLegFullRollExtractionModeEnumPlugOperator


class LeftArmFullRollExtractionModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LeftArmFullRollExtractionModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LeftArmFullRollExtractionModeEnumField(
    EnumField[LeftArmFullRollExtractionModeEnumAttrOperator, LeftArmFullRollExtractionModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftArmFullRollExtractionModeEnumAttrOperator
    PLUG_CLS = LeftArmFullRollExtractionModeEnumPlugOperator


class RightArmFullRollExtractionModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class RightArmFullRollExtractionModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class RightArmFullRollExtractionModeEnumField(
    EnumField[RightArmFullRollExtractionModeEnumAttrOperator, RightArmFullRollExtractionModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightArmFullRollExtractionModeEnumAttrOperator
    PLUG_CLS = RightArmFullRollExtractionModeEnumPlugOperator


class _GeneratedHIKProperty2State(DG):
    __slots__ = ()

    NODE_TYPE = "HIKProperty2State"

    OutputPropertySetState = TypedField()

    rigAlign = BoolField(default_value=True)
    ra = rigAlign

    leftHipRoll = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    lhr = leftHipRoll

    leftKneeRoll = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    lkr = leftKneeRoll

    rightHipRoll = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rhr = rightHipRoll

    rightKneeRoll = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rkr = rightKneeRoll

    leftShoulderRoll = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    lsr = leftShoulderRoll

    leftElbowRoll = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ler = leftElbowRoll

    rightShoulderRoll = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rsr = rightShoulderRoll

    rightElbowRoll = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rer = rightElbowRoll

    ForceActorSpace = ForceActorSpaceEnumField(default_value=0)

    ScaleCompensationMode = ScaleCompensationModeEnumField(default_value=1)

    ScaleCompensation = DoubleField(default_value=100.0)

    MassCenterCompensationMode = MassCenterCompensationModeEnumField(default_value=1)

    MassCenterCompensation = DoubleField(default_value=80.0, min_value=0.0, max_value=120.0)

    AnkleHeightCompensationMode = AnkleHeightCompensationModeEnumField(default_value=1)

    AnkleHeightCompensation = DoubleField(default_value=0.0)

    AnkleProximityCompensationMode = AnkleProximityCompensationModeEnumField(default_value=1)

    AnkleProximityCompensation = DoubleField(default_value=0.0)

    HipsHeightCompensationMode = HipsHeightCompensationModeEnumField(default_value=1)

    HipsHeightCompensation = DoubleField(default_value=0.0)

    ReachActorLeftAnkle = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)

    ReachActorRightAnkle = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)

    ReachActorChest = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftWrist = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightWrist = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftKnee = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightKnee = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorHead = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftElbow = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightElbow = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftAnkleRotationRotation = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)

    ReachActorRightAnkleRotation = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)

    ReachActorHeadRotation = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftWristRotation = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightWristRotation = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftFingerBase = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightFingerBase = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftToesBase = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightToesBase = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftFingerBaseRotation = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightFingerBaseRotation = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftToesBaseRotation = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightToesBaseRotation = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorChestRotation = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLowerChestRotation = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftHandThumb = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftHandIndex = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftHandMiddle = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftHandRing = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftHandPinky = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftHandExtraFinger = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightHandThumb = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightHandIndex = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightHandMiddle = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightHandRing = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightHandPinky = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightHandExtraFinger = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftFootThumb = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftFootIndex = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftFootMiddle = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftFootRing = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftFootPinky = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorLeftFootExtraFinger = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightFootThumb = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightFootIndex = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightFootMiddle = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightFootRing = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightFootPinky = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightFootExtraFinger = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    FloorContact = FloorContactEnumField(default_value=0)

    FootBottomToAnkle = DoubleField(default_value=0.0)

    FootBackToAnkle = DoubleField(default_value=4.5)

    FootMiddleToAnkle = DoubleField(default_value=13.0)

    FootFrontToMiddle = DoubleField(default_value=7.0)

    FootInToAnkle = DoubleField(default_value=5.0)

    FootOutToAnkle = DoubleField(default_value=5.0)

    HandFloorContact = HandFloorContactEnumField(default_value=0)

    HandBottomToWrist = DoubleField(default_value=0.0)

    HandBackToWrist = DoubleField(default_value=4.5)

    HandMiddleToWrist = DoubleField(default_value=13.0)

    HandFrontToMiddle = DoubleField(default_value=7.0)

    HandInToWrist = DoubleField(default_value=5.0)

    HandOutToWrist = DoubleField(default_value=5.0)

    HandContactType = HandContactTypeEnumField(default_value=0)

    HandFingerContact = HandFingerContactEnumField(default_value=0)

    HandFingerContactMode = HandFingerContactModeEnumField(default_value=1)

    FootContactType = FootContactTypeEnumField(default_value=0)

    FootFingerContact = FootFingerContactEnumField(default_value=0)

    FootFingerContactMode = FootFingerContactModeEnumField(default_value=1)

    LeftUpLegRollMode = LeftUpLegRollModeEnumField(default_value=0)

    LeftUpLegRoll = DoubleField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)

    LeftLegRollMode = LeftLegRollModeEnumField(default_value=0)

    LeftLegRoll = DoubleField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)

    RightUpLegRollMode = RightUpLegRollModeEnumField(default_value=0)

    RightUpLegRoll = DoubleField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)

    RightLegRollMode = RightLegRollModeEnumField(default_value=0)

    RightLegRoll = DoubleField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)

    LeftArmRollMode = LeftArmRollModeEnumField(default_value=0)

    LeftArmRoll = DoubleField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)

    LeftForeArmRollMode = LeftForeArmRollModeEnumField(default_value=0)

    LeftForeArmRoll = DoubleField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)

    RightArmRollMode = RightArmRollModeEnumField(default_value=0)

    RightArmRoll = DoubleField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)

    RightForeArmRollMode = RightForeArmRollModeEnumField(default_value=0)

    RightForeArmRoll = DoubleField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)

    Mirror = MirrorEnumField(default_value=0)

    LeftKneeKillPitch = LeftKneeKillPitchEnumField(default_value=0)

    RightKneeKillPitch = RightKneeKillPitchEnumField(default_value=0)

    LeftElbowKillPitch = LeftElbowKillPitchEnumField(default_value=0)

    RightElbowKillPitch = RightElbowKillPitchEnumField(default_value=0)

    CtrlPullLeftFoot = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)

    CtrlPullRightFoot = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)

    CtrlPullLeftHand = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)

    CtrlPullRightHand = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)

    CtrlPullHead = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    CtrlPullLeftToeBase = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    CtrlPullLeftKnee = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    CtrlPullRightToeBase = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    CtrlPullRightKnee = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    CtrlPullLeftFingerBase = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    CtrlPullLeftElbow = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    CtrlPullRightFingerBase = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    CtrlPullRightElbow = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    CtrlChestPullLeftHand = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)

    CtrlChestPullRightHand = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)

    CtrlResistHipsPosition = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    CtrlEnforceGravity = DoubleField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)

    CtrlResistHipsOrientation = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    CtrlResistChestPosition = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    CtrlResistChestOrientation = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    CtrlResistLeftCollar = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    CtrlResistRightCollar = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    CtrlResistLeftKnee = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    CtrlResistRightKnee = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    CtrlResistLeftElbow = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    CtrlResistRightElbow = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamCtrlSpineStiffness = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    HipsTOffsetX = DoubleField(default_value=0.0)

    HipsTOffsetY = DoubleField(default_value=0.0)

    HipsTOffsetZ = DoubleField(default_value=0.0)

    ChestTOffsetX = DoubleField(default_value=0.0)

    ChestTOffsetY = DoubleField(default_value=0.0)

    ChestTOffsetZ = DoubleField(default_value=0.0)

    AutomaticToes = AutomaticToesEnumField(default_value=0)

    FloorPivot = FloorPivotEnumField(default_value=0)

    Posture = PostureEnumField(default_value=0)

    AutomaticFingers = AutomaticFingersEnumField(default_value=0)

    HandFloorPivot = HandFloorPivotEnumField(default_value=0)

    ParamCtrlNeckStiffness = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    HipsTranslationMode = HipsTranslationModeEnumField(default_value=0)

    FingerSolving = FingerSolvingEnumField(default_value=1)

    ParamFootContactStiffness = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    CtrlResistMaximumExtensionLeftKnee = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    CtrlResistMaximumExtensionRightKnee = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    CtrlResistMaximumExtensionLeftElbow = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    CtrlResistMaximumExtensionRightElbow = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    CtrlResistCompressionFactorLeftKnee = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    CtrlResistCompressionFactorRightKnee = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    CtrlResistCompressionFactorLeftElbow = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    CtrlResistCompressionFactorRightElbow = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamHandFingerContactRollStiffness = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ParamFootFingerContactRollStiffness = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ParamHandContactStiffness = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    RollExtractionMode = RollExtractionModeEnumField(default_value=0)

    PullIterationCount = DoubleField(default_value=10.0, min_value=0.0, max_value=30.0)

    LeftHandThumbTip = DoubleField(default_value=0.5)

    LeftHandIndexTip = DoubleField(default_value=0.5)

    LeftHandMiddleTip = DoubleField(default_value=0.5)

    LeftHandRingTip = DoubleField(default_value=0.5)

    LeftHandPinkyTip = DoubleField(default_value=0.5)

    LeftHandExtraFingerTip = DoubleField(default_value=0.5)

    RightHandThumbTip = DoubleField(default_value=0.5)

    RightHandIndexTip = DoubleField(default_value=0.5)

    RightHandMiddleTip = DoubleField(default_value=0.5)

    RightHandRingTip = DoubleField(default_value=0.5)

    RightHandPinkyTip = DoubleField(default_value=0.5)

    RightHandExtraFingerTip = DoubleField(default_value=0.5)

    LeftFootThumbTip = DoubleField(default_value=0.5)

    LeftFootIndexTip = DoubleField(default_value=0.5)

    LeftFootMiddleTip = DoubleField(default_value=0.5)

    LeftFootRingTip = DoubleField(default_value=0.5)

    LeftFootPinkyTip = DoubleField(default_value=0.5)

    LeftFootExtraFingerTip = DoubleField(default_value=0.5)

    RightFootThumbTip = DoubleField(default_value=0.5)

    RightFootIndexTip = DoubleField(default_value=0.5)

    RightFootMiddleTip = DoubleField(default_value=0.5)

    RightFootRingTip = DoubleField(default_value=0.5)

    RightFootPinkyTip = DoubleField(default_value=0.5)

    RightFootExtraFingerTip = DoubleField(default_value=0.5)

    ShoulderCorrection = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    LeftLegMaxExtensionAngle = DoubleField(default_value=180.0, min_value=0.0, max_value=180.0)

    RightLegMaxExtensionAngle = DoubleField(default_value=180.0, min_value=0.0, max_value=180.0)

    LeftArmMaxExtensionAngle = DoubleField(default_value=180.0, min_value=0.0, max_value=180.0)

    RightArmMaxExtensionAngle = DoubleField(default_value=180.0, min_value=0.0, max_value=180.0)

    ExtraCollarRatio = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    CollarStiffnessX = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)

    CollarStiffnessY = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)

    CollarStiffnessZ = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)

    ReachActorLeftShoulder = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    ReachActorRightShoulder = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    FingerPropagation = FingerPropagationEnumField(default_value=0)

    RealisticLeftKneeSolving = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    RealisticRightKneeSolving = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    SnSScaleArmsAndLegs = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    SnSReachLeftWrist = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    SnSReachRightWrist = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    SnSReachLeftAnkle = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    SnSReachRightAnkle = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    SnSScaleSpine = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    SnSScaleSpineChildren = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    SnSReachChestEnd = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    SnSScaleNeck = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    SnSReachHead = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    LeftUpLegRollEx = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    LeftLegRollEx = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    RightUpLegRollEx = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    RightLegRollEx = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    LeftArmRollEx = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    LeftForeArmRollEx = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    RightArmRollEx = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    RightForeArmRollEx = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    TopSpineCorrection = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    LowerSpineCorrection = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    SnSSmoothReach = SnSSmoothReachEnumField(default_value=0)

    LockX = LockXEnumField(default_value=0)

    LockY = LockYEnumField(default_value=0)

    LockZ = LockZEnumField(default_value=0)

    ParamRealisticArmSolving = ParamRealisticArmSolvingEnumField(default_value=0)

    ParamLeafLeftUpLegRoll1Mode = ParamLeafLeftUpLegRoll1ModeEnumField(default_value=1)

    ParamLeafLeftUpLegRoll1 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftLegRoll1Mode = ParamLeafLeftLegRoll1ModeEnumField(default_value=1)

    ParamLeafLeftLegRoll1 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightUpLegRoll1Mode = ParamLeafRightUpLegRoll1ModeEnumField(default_value=1)

    ParamLeafRightUpLegRoll1 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightLegRoll1Mode = ParamLeafRightLegRoll1ModeEnumField(default_value=1)

    ParamLeafRightLegRoll1 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftArmRoll1Mode = ParamLeafLeftArmRoll1ModeEnumField(default_value=1)

    ParamLeafLeftArmRoll1 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftForeArmRoll1Mode = ParamLeafLeftForeArmRoll1ModeEnumField(default_value=1)

    ParamLeafLeftForeArmRoll1 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightArmRoll1Mode = ParamLeafRightArmRoll1ModeEnumField(default_value=1)

    ParamLeafRightArmRoll1 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightForeArmRoll1Mode = ParamLeafRightForeArmRoll1ModeEnumField(default_value=1)

    ParamLeafRightForeArmRoll1 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftUpLegRoll2Mode = ParamLeafLeftUpLegRoll2ModeEnumField(default_value=1)

    ParamLeafLeftUpLegRoll2 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftLegRoll2Mode = ParamLeafLeftLegRoll2ModeEnumField(default_value=1)

    ParamLeafLeftLegRoll2 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightUpLegRoll2Mode = ParamLeafRightUpLegRoll2ModeEnumField(default_value=1)

    ParamLeafRightUpLegRoll2 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightLegRoll2Mode = ParamLeafRightLegRoll2ModeEnumField(default_value=1)

    ParamLeafRightLegRoll2 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftArmRoll2Mode = ParamLeafLeftArmRoll2ModeEnumField(default_value=1)

    ParamLeafLeftArmRoll2 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftForeArmRoll2Mode = ParamLeafLeftForeArmRoll2ModeEnumField(default_value=1)

    ParamLeafLeftForeArmRoll2 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightArmRoll2Mode = ParamLeafRightArmRoll2ModeEnumField(default_value=1)

    ParamLeafRightArmRoll2 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightForeArmRoll2Mode = ParamLeafRightForeArmRoll2ModeEnumField(default_value=1)

    ParamLeafRightForeArmRoll2 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftUpLegRoll3Mode = ParamLeafLeftUpLegRoll3ModeEnumField(default_value=1)

    ParamLeafLeftUpLegRoll3 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftLegRoll3Mode = ParamLeafLeftLegRoll3ModeEnumField(default_value=1)

    ParamLeafLeftLegRoll3 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightUpLegRoll3Mode = ParamLeafRightUpLegRoll3ModeEnumField(default_value=1)

    ParamLeafRightUpLegRoll3 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightLegRoll3Mode = ParamLeafRightLegRoll3ModeEnumField(default_value=1)

    ParamLeafRightLegRoll3 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftArmRoll3Mode = ParamLeafLeftArmRoll3ModeEnumField(default_value=1)

    ParamLeafLeftArmRoll3 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftForeArmRoll3Mode = ParamLeafLeftForeArmRoll3ModeEnumField(default_value=1)

    ParamLeafLeftForeArmRoll3 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightArmRoll3Mode = ParamLeafRightArmRoll3ModeEnumField(default_value=1)

    ParamLeafRightArmRoll3 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightForeArmRoll3Mode = ParamLeafRightForeArmRoll3ModeEnumField(default_value=1)

    ParamLeafRightForeArmRoll3 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftUpLegRoll4Mode = ParamLeafLeftUpLegRoll4ModeEnumField(default_value=1)

    ParamLeafLeftUpLegRoll4 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftLegRoll4Mode = ParamLeafLeftLegRoll4ModeEnumField(default_value=1)

    ParamLeafLeftLegRoll4 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightUpLegRoll4Mode = ParamLeafRightUpLegRoll4ModeEnumField(default_value=1)

    ParamLeafRightUpLegRoll4 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightLegRoll4Mode = ParamLeafRightLegRoll4ModeEnumField(default_value=1)

    ParamLeafRightLegRoll4 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftArmRoll4Mode = ParamLeafLeftArmRoll4ModeEnumField(default_value=1)

    ParamLeafLeftArmRoll4 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftForeArmRoll4Mode = ParamLeafLeftForeArmRoll4ModeEnumField(default_value=1)

    ParamLeafLeftForeArmRoll4 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightArmRoll4Mode = ParamLeafRightArmRoll4ModeEnumField(default_value=1)

    ParamLeafRightArmRoll4 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightForeArmRoll4Mode = ParamLeafRightForeArmRoll4ModeEnumField(default_value=1)

    ParamLeafRightForeArmRoll4 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftUpLegRoll5Mode = ParamLeafLeftUpLegRoll5ModeEnumField(default_value=1)

    ParamLeafLeftUpLegRoll5 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftLegRoll5Mode = ParamLeafLeftLegRoll5ModeEnumField(default_value=1)

    ParamLeafLeftLegRoll5 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightUpLegRoll5Mode = ParamLeafRightUpLegRoll5ModeEnumField(default_value=1)

    ParamLeafRightUpLegRoll5 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightLegRoll5Mode = ParamLeafRightLegRoll5ModeEnumField(default_value=1)

    ParamLeafRightLegRoll5 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftArmRoll5Mode = ParamLeafLeftArmRoll5ModeEnumField(default_value=1)

    ParamLeafLeftArmRoll5 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafLeftForeArmRoll5Mode = ParamLeafLeftForeArmRoll5ModeEnumField(default_value=1)

    ParamLeafLeftForeArmRoll5 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightArmRoll5Mode = ParamLeafRightArmRoll5ModeEnumField(default_value=1)

    ParamLeafRightArmRoll5 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    ParamLeafRightForeArmRoll5Mode = ParamLeafRightForeArmRoll5ModeEnumField(default_value=1)

    ParamLeafRightForeArmRoll5 = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)

    LeftLegFullRollExtractionMode = LeftLegFullRollExtractionModeEnumField(default_value=1)

    LeftLegFullRollExtraction = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    RightLegFullRollExtractionMode = RightLegFullRollExtractionModeEnumField(default_value=1)

    RightLegFullRollExtraction = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    LeftArmFullRollExtractionMode = LeftArmFullRollExtractionModeEnumField(default_value=1)

    LeftArmFullRollExtraction = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    RightArmFullRollExtractionMode = RightArmFullRollExtractionModeEnumField(default_value=1)

    RightArmFullRollExtraction = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)

    NeckMotionReduction = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
