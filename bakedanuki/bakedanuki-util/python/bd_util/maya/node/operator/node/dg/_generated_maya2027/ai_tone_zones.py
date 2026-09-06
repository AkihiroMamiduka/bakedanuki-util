# coding: utf-8
from .._core import DG
from ....attr.define.node_attr_maya2027.ai_tone_zones import (
    InputField,
    OutColorField,
    Out_1Field,
    Out_2Field,
    Out_3Field,
    Out_4Field,
    Out_5Field,
    Out_6Field,
    Out_7Field,
    Out_8Field,
    Tint1Field,
    Tint2Field,
    Tint3Field,
    Tint4Field,
    Tint5Field,
    Tint6Field,
    Tint7Field,
    Tint8Field,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class GeneratedAiToneZones(DG):
    __slots__ = ()

    NODE_TYPE = "aiToneZones"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    out_1 = Out_1Field(default_value=(0.0, 0.0, 0.0), writable=False)
    out_1R = out_1.out_1R
    out_1r = out_1R
    out_1G = out_1.out_1G
    out_1g = out_1G
    out_1B = out_1.out_1B
    out_1b = out_1B

    out_2 = Out_2Field(default_value=(0.0, 0.0, 0.0), writable=False)
    out_2R = out_2.out_2R
    out_2r = out_2R
    out_2G = out_2.out_2G
    out_2g = out_2G
    out_2B = out_2.out_2B
    out_2b = out_2B

    out_3 = Out_3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    out_3R = out_3.out_3R
    out_3r = out_3R
    out_3G = out_3.out_3G
    out_3g = out_3G
    out_3B = out_3.out_3B
    out_3b = out_3B

    out_4 = Out_4Field(default_value=(0.0, 0.0, 0.0), writable=False)
    out_4R = out_4.out_4R
    out_4r = out_4R
    out_4G = out_4.out_4G
    out_4g = out_4G
    out_4B = out_4.out_4B
    out_4b = out_4B

    out_5 = Out_5Field(default_value=(0.0, 0.0, 0.0), writable=False)
    out_5R = out_5.out_5R
    out_5r = out_5R
    out_5G = out_5.out_5G
    out_5g = out_5G
    out_5B = out_5.out_5B
    out_5b = out_5B

    out_6 = Out_6Field(default_value=(0.0, 0.0, 0.0), writable=False)
    out_6R = out_6.out_6R
    out_6r = out_6R
    out_6G = out_6.out_6G
    out_6g = out_6G
    out_6B = out_6.out_6B
    out_6b = out_6B

    out_7 = Out_7Field(default_value=(0.0, 0.0, 0.0), writable=False)
    out_7R = out_7.out_7R
    out_7r = out_7R
    out_7G = out_7.out_7G
    out_7g = out_7G
    out_7B = out_7.out_7B
    out_7b = out_7B

    out_8 = Out_8Field(default_value=(0.0, 0.0, 0.0), writable=False)
    out_8R = out_8.out_8R
    out_8r = out_8R
    out_8G = out_8.out_8G
    out_8g = out_8G
    out_8B = out_8.out_8B
    out_8b = out_8B

    out_1_a = FloatField(default_value=0.0, writable=False)

    out_2_a = FloatField(default_value=0.0, writable=False)

    out_3_a = FloatField(default_value=0.0, writable=False)

    out_4_a = FloatField(default_value=0.0, writable=False)

    out_5_a = FloatField(default_value=0.0, writable=False)

    out_6_a = FloatField(default_value=0.0, writable=False)

    out_7_a = FloatField(default_value=0.0, writable=False)

    out_8_a = FloatField(default_value=0.0, writable=False)

    out_1_n = FloatField(default_value=0.0, writable=False)

    out_2_n = FloatField(default_value=0.0, writable=False)

    out_3_n = FloatField(default_value=0.0, writable=False)

    out_4_n = FloatField(default_value=0.0, writable=False)

    out_5_n = FloatField(default_value=0.0, writable=False)

    out_6_n = FloatField(default_value=0.0, writable=False)

    out_7_n = FloatField(default_value=0.0, writable=False)

    out_8_n = FloatField(default_value=0.0, writable=False)

    input = InputField(default_value=(0.0, 0.0, 0.0))
    inputR = input.inputR
    inputr = inputR
    inputG = input.inputG
    inputg = inputG
    inputB = input.inputB
    inputb = inputB

    luminanceRange = FloatField(
        default_value=1.0,
        min_value=9.999999747378752e-05,
        soft_min_value=0.10000000149011612,
        soft_max_value=10.0,
    )
    luminance_range = luminanceRange

    weight1 = FloatField(default_value=0.25, min_value=0.0, soft_max_value=1.0)
    weight_1 = weight1

    weight2 = FloatField(default_value=0.25, min_value=0.0, soft_max_value=1.0)
    weight_2 = weight2

    weight3 = FloatField(default_value=0.25, min_value=0.0, soft_max_value=1.0)
    weight_3 = weight3

    weight4 = FloatField(default_value=0.25, min_value=0.0, soft_max_value=1.0)
    weight_4 = weight4

    weight5 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    weight_5 = weight5

    weight6 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    weight_6 = weight6

    weight7 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    weight_7 = weight7

    weight8 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    weight_8 = weight8

    tint1 = Tint1Field(default_value=(1.0, 1.0, 1.0))
    tint_1 = tint1
    tint1R = tint1.tint1R
    tint_1r = tint1R
    tint1G = tint1.tint1G
    tint_1g = tint1G
    tint1B = tint1.tint1B
    tint_1b = tint1B

    tint2 = Tint2Field(default_value=(0.75, 0.75, 0.75))
    tint_2 = tint2
    tint2R = tint2.tint2R
    tint_2r = tint2R
    tint2G = tint2.tint2G
    tint_2g = tint2G
    tint2B = tint2.tint2B
    tint_2b = tint2B

    tint3 = Tint3Field(default_value=(0.5, 0.5, 0.5))
    tint_3 = tint3
    tint3R = tint3.tint3R
    tint_3r = tint3R
    tint3G = tint3.tint3G
    tint_3g = tint3G
    tint3B = tint3.tint3B
    tint_3b = tint3B

    tint4 = Tint4Field(default_value=(0.25, 0.25, 0.25))
    tint_4 = tint4
    tint4R = tint4.tint4R
    tint_4r = tint4R
    tint4G = tint4.tint4G
    tint_4g = tint4G
    tint4B = tint4.tint4B
    tint_4b = tint4B

    tint5 = Tint5Field(default_value=(0.0, 0.0, 0.0))
    tint_5 = tint5
    tint5R = tint5.tint5R
    tint_5r = tint5R
    tint5G = tint5.tint5G
    tint_5g = tint5G
    tint5B = tint5.tint5B
    tint_5b = tint5B

    tint6 = Tint6Field(default_value=(0.0, 0.0, 0.0))
    tint_6 = tint6
    tint6R = tint6.tint6R
    tint_6r = tint6R
    tint6G = tint6.tint6G
    tint_6g = tint6G
    tint6B = tint6.tint6B
    tint_6b = tint6B

    tint7 = Tint7Field(default_value=(0.0, 0.0, 0.0))
    tint_7 = tint7
    tint7R = tint7.tint7R
    tint_7r = tint7R
    tint7G = tint7.tint7G
    tint_7g = tint7G
    tint7B = tint7.tint7B
    tint_7b = tint7B

    tint8 = Tint8Field(default_value=(0.0, 0.0, 0.0))
    tint_8 = tint8
    tint8R = tint8.tint8R
    tint_8r = tint8R
    tint8G = tint8.tint8G
    tint_8g = tint8G
    tint8B = tint8.tint8B
    tint_8b = tint8B

    edgeSoftness1 = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    edge_softness_1 = edgeSoftness1

    edgeSoftness2 = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    edge_softness_2 = edgeSoftness2

    edgeSoftness3 = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    edge_softness_3 = edgeSoftness3

    edgeSoftness4 = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    edge_softness_4 = edgeSoftness4

    edgeSoftness5 = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    edge_softness_5 = edgeSoftness5

    edgeSoftness6 = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    edge_softness_6 = edgeSoftness6

    edgeSoftness7 = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    edge_softness_7 = edgeSoftness7

    aov1 = DataStringField()
    aov_1 = aov1

    aov2 = DataStringField()
    aov_2 = aov2

    aov3 = DataStringField()
    aov_3 = aov3

    aov4 = DataStringField()
    aov_4 = aov4

    aov5 = DataStringField()
    aov_5 = aov5

    aov6 = DataStringField()
    aov_6 = aov6

    aov7 = DataStringField()
    aov_7 = aov7

    aov8 = DataStringField()
    aov_8 = aov8
