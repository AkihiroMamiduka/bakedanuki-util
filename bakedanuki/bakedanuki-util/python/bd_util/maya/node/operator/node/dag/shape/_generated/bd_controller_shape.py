# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.bd_controller_shape import (
    CompInstObjGroupsField,
    ComponentTagsField,
    CustomBoundsAxisRotateField,
    CustomBoundsAxisScaleField,
    CustomBoundsAxisTranslateField,
    CustomBoundsRotateField,
    CustomBoundsScaleField,
    CustomBoundsTranslateField,
    LocalPositionField,
    LocalScaleField,
    ShapeAxisRotateField,
    ShapeAxisScaleField,
    ShapeAxisTranslateField,
    ShapeRotateField,
    ShapeScaleField,
    ShapeTranslateField,
    WorldPositionField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.float import FloatField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.numeric.range.short import ShortField
from .....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)
from .....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)
from .....attr.define.std.dt.matrix import DataMatrixField


class ShapeEnumPlugOperator(EnumPlugOperator["ShapeEnumAttrOperator"]):
    __slots__ = ()

    GEAR = 0
    GEARFILLED = 1
    LINE = 2
    LINEARROWATEND = 3
    LINEARROWATENDFILLED = 4
    LINEARROWATENDS = 5
    LINEARROWATENDSFILLED = 6
    LINEWIDEARROWATEND = 7
    LINEWIDEARROWATENDFILLED = 8
    LINEWIDEARROWATENDS = 9
    LINEWIDEARROWATENDSFILLED = 10
    LINESQUAREATEND = 11
    LINESQUAREATENDFILLED = 12
    LINESQUAREATENDS = 13
    LINESQUAREATENDSFILLED = 14
    LINEDIAMONDATEND = 15
    LINEDIAMONDATENDFILLED = 16
    LINEDIAMONDATENDS = 17
    LINEDIAMONDATENDSFILLED = 18
    LINECIRCLEATEND = 19
    LINECIRCLEATENDFILLED = 20
    LINECIRCLEATENDS = 21
    LINECIRCLEATENDSFILLED = 22
    LINETRIANGLEATEND = 23
    LINETRIANGLEATENDFILLED = 24
    LINETRIANGLEATENDS = 25
    LINETRIANGLEATENDSFILLED = 26
    CROSSLINE1ST2ND = 27
    CROSSLINE1ST2NDARROWATEND = 28
    CROSSLINE1ST2NDARROWATENDFILLED = 29
    CROSSLINE1ST2NDARROWATENDS = 30
    CROSSLINE1ST2NDARROWATENDSFILLED = 31
    CROSSLINE1ST2NDWIDEARROWATEND = 32
    CROSSLINE1ST2NDWIDEARROWATENDFILLED = 33
    CROSSLINE1ST2NDWIDEARROWATENDS = 34
    CROSSLINE1ST2NDWIDEARROWATENDSFILLED = 35
    CROSSLINE1ST2NDSQUAREATEND = 36
    CROSSLINE1ST2NDSQUAREATENDFILLED = 37
    CROSSLINE1ST2NDSQUAREATENDS = 38
    CROSSLINE1ST2NDSQUAREATENDSFILLED = 39
    CROSSLINE1ST2NDDIAMONDATEND = 40
    CROSSLINE1ST2NDDIAMONDATENDFILLED = 41
    CROSSLINE1ST2NDDIAMONDATENDS = 42
    CROSSLINE1ST2NDDIAMONDATENDSFILLED = 43
    CROSSLINE1ST2NDCIRCLEATEND = 44
    CROSSLINE1ST2NDCIRCLEATENDFILLED = 45
    CROSSLINE1ST2NDCIRCLEATENDS = 46
    CROSSLINE1ST2NDCIRCLEATENDSFILLED = 47
    CROSSLINE1ST2NDTRIANGLEATEND = 48
    CROSSLINE1ST2NDTRIANGLEATENDFILLED = 49
    CROSSLINE1ST2NDTRIANGLEATENDS = 50
    CROSSLINE1ST2NDTRIANGLEATENDSFILLED = 51
    CROSSLINE1ST3RD = 52
    CROSSLINE1ST3RDARROWATEND = 53
    CROSSLINE1ST3RDARROWATENDFILLED = 54
    CROSSLINE1ST3RDARROWATENDS = 55
    CROSSLINE1ST3RDARROWATENDSFILLED = 56
    CROSSLINE1ST3RDWIDEARROWATEND = 57
    CROSSLINE1ST3RDWIDEARROWATENDFILLED = 58
    CROSSLINE1ST3RDWIDEARROWATENDS = 59
    CROSSLINE1ST3RDWIDEARROWATENDSFILLED = 60
    CROSSLINE1ST3RDSQUAREATEND = 61
    CROSSLINE1ST3RDSQUAREATENDFILLED = 62
    CROSSLINE1ST3RDSQUAREATENDS = 63
    CROSSLINE1ST3RDSQUAREATENDSFILLED = 64
    CROSSLINE1ST3RDDIAMONDATEND = 65
    CROSSLINE1ST3RDDIAMONDATENDFILLED = 66
    CROSSLINE1ST3RDDIAMONDATENDS = 67
    CROSSLINE1ST3RDDIAMONDATENDSFILLED = 68
    CROSSLINE1ST3RDCIRCLEATEND = 69
    CROSSLINE1ST3RDCIRCLEATENDFILLED = 70
    CROSSLINE1ST3RDCIRCLEATENDS = 71
    CROSSLINE1ST3RDCIRCLEATENDSFILLED = 72
    CROSSLINE1ST3RDTRIANGLEATEND = 73
    CROSSLINE1ST3RDTRIANGLEATENDFILLED = 74
    CROSSLINE1ST3RDTRIANGLEATENDS = 75
    CROSSLINE1ST3RDTRIANGLEATENDSFILLED = 76
    CROSSLINE2ND3RD = 77
    CROSSLINE2ND3RDARROWATEND = 78
    CROSSLINE2ND3RDARROWATENDFILLED = 79
    CROSSLINE2ND3RDARROWATENDS = 80
    CROSSLINE2ND3RDARROWATENDSFILLED = 81
    CROSSLINE2ND3RDWIDEARROWATEND = 82
    CROSSLINE2ND3RDWIDEARROWATENDFILLED = 83
    CROSSLINE2ND3RDWIDEARROWATENDS = 84
    CROSSLINE2ND3RDWIDEARROWATENDSFILLED = 85
    CROSSLINE2ND3RDSQUAREATEND = 86
    CROSSLINE2ND3RDSQUAREATENDFILLED = 87
    CROSSLINE2ND3RDSQUAREATENDS = 88
    CROSSLINE2ND3RDSQUAREATENDSFILLED = 89
    CROSSLINE2ND3RDDIAMONDATEND = 90
    CROSSLINE2ND3RDDIAMONDATENDFILLED = 91
    CROSSLINE2ND3RDDIAMONDATENDS = 92
    CROSSLINE2ND3RDDIAMONDATENDSFILLED = 93
    CROSSLINE2ND3RDCIRCLEATEND = 94
    CROSSLINE2ND3RDCIRCLEATENDFILLED = 95
    CROSSLINE2ND3RDCIRCLEATENDS = 96
    CROSSLINE2ND3RDCIRCLEATENDSFILLED = 97
    CROSSLINE2ND3RDTRIANGLEATEND = 98
    CROSSLINE2ND3RDTRIANGLEATENDFILLED = 99
    CROSSLINE2ND3RDTRIANGLEATENDS = 100
    CROSSLINE2ND3RDTRIANGLEATENDSFILLED = 101
    CROSSLINE3AXIS = 102
    CROSSLINE3AXISENDCUBE = 103
    CROSSLINE3AXISENDCUBEFILLED = 104
    CROSSLINE3AXISENDOCTAHEDRON = 105
    CROSSLINE3AXISENDOCTAHEDRONFILLED = 106
    CROSSLINE3AXISENDSPHERE = 107
    CROSSLINE3AXISENDSPHEREFILLED = 108
    CROSSLINE3AXISENDPYRAMID = 109
    CROSSLINE3AXISENDPYRAMIDFILLED = 110
    CROSSLINE3AXISENDCONE = 111
    CROSSLINE3AXISENDCONEFILLED = 112
    TRIANGLE = 113
    TRIANGLEFILLED = 114
    TRIANGLEARROW3D = 115
    TRIANGLEARROW3DFILLED = 116
    SQUARE = 117
    SQUAREFILLED = 118
    SQUAREARROW2D = 119
    SQUAREARROW2DFILLED = 120
    SQUAREARROW3D = 121
    SQUAREARROW3DFILLED = 122
    SQUAREARROWCROSSLINE2D = 123
    SQUAREARROWCROSSLINE2DFILLED = 124
    SQUAREARROWCROSSLINE3D = 125
    SQUAREARROWCROSSLINE3DFILLED = 126
    SQUAREARROWCROSSLINETEMPLATE2D = 127
    SQUAREARROWCROSSLINETEMPLATE2DFILLED = 128
    SQUAREARROWCROSSLINETEMPLATE3D = 129
    SQUAREARROWCROSSLINETEMPLATE3DFILLED = 130
    SQUAREARROW4WAY2D = 131
    SQUAREARROW4WAY2DFILLED = 132
    SQUAREARROW4WAY3D = 133
    SQUAREARROW4WAY3DFILLED = 134
    SQUARETEMPLATEARROW4WAY2D = 135
    SQUARETEMPLATEARROW4WAY2DFILLED = 136
    SQUARETEMPLATEARROW4WAY3D = 137
    SQUARETEMPLATEARROW4WAY3DFILLED = 138
    DIAMOND = 139
    DIAMONDFILLED = 140
    CUBE = 141
    CUBEFILLED = 142
    CUBEARROW2D = 143
    CUBEARROW2DFILLED = 144
    CUBEARROW3D = 145
    CUBEARROW3DFILLED = 146
    CUBEFIN = 147
    CUBEFINFILLED = 148
    CUBEFINARROW = 149
    CUBEFINARROWFILLED = 150
    OCTAHEDRON = 151
    OCTAHEDRONFILLED = 152
    OCTAHEDRONARROW = 153
    OCTAHEDRONARROWFILLED = 154
    OCTAHEDRONARROWFIN = 155
    OCTAHEDRONARROWFINFILLED = 156
    CIRCLE = 157
    CIRCLEFILLED = 158
    CIRCLEARROW2D = 159
    CIRCLEARROW2DFILLED = 160
    CIRCLEARROW3D = 161
    CIRCLEARROW3DFILLED = 162
    SEMICIRCLE = 163
    SEMICIRCLEFILLED = 164
    SEMICIRCLEARROWATEND = 165
    SEMICIRCLEARROWATENDFILLED = 166
    SEMICIRCLEARROWATENDS = 167
    SEMICIRCLEARROWATENDSFILLED = 168
    SEMICIRCLEWIDEARROWATEND = 169
    SEMICIRCLEWIDEARROWATENDFILLED = 170
    SEMICIRCLEWIDEARROWATENDS = 171
    SEMICIRCLEWIDEARROWATENDSFILLED = 172
    SEMICIRCLEARROW2D = 173
    SEMICIRCLEARROW2DFILLED = 174
    SEMICIRCLEARROW3D = 175
    SEMICIRCLEARROW3DFILLED = 176
    SPHERE = 177
    SPHEREFILLED = 178
    SPHEREARROW2D = 179
    SPHEREARROW2DFILLED = 180
    SPHEREARROW3D = 181
    SPHEREARROW3DFILLED = 182
    CYLINDER = 183
    CYLINDERFILLED = 184
    CYLINDERFIN = 185
    CYLINDERFINFILLED = 186
    CYLINDERFINARROW = 187
    CYLINDERFINARROWFILLED = 188
    ARROW = 189
    ARROWFILLED = 190
    ARROWFIN = 191
    ARROWFINFILLED = 192
    PYRAMID = 193
    PYRAMIDFILLED = 194
    PYRAMIDFIN = 195
    PYRAMIDFINFILLED = 196
    CONE = 197
    CONEFILLED = 198
    CONEFIN = 199
    CONEFINFILLED = 200
    COLORCROSSLINE3AXIS = 201
    COLORCROSSLINE3AXISENDCUBE = 202
    COLORCROSSLINE3AXISENDCUBEFILLED = 203
    COLORCROSSLINE3AXISENDOCTAHEDRON = 204
    COLORCROSSLINE3AXISENDOCTAHEDRONFILLED = 205
    COLORCROSSLINE3AXISENDSPHERE = 206
    COLORCROSSLINE3AXISENDSPHEREFILLED = 207
    COLORCROSSLINE3AXISENDPYRAMID = 208
    COLORCROSSLINE3AXISENDPYRAMIDFILLED = 209
    COLORCROSSLINE3AXISENDCONE = 210
    COLORCROSSLINE3AXISENDCONEFILLED = 211
    COLORCUBE = 212
    COLORCUBEFILLED = 213
    COLORCORNERCUBE = 214
    COLORCORNERCUBEFILLED = 215
    COLORSPHERE = 216
    COLORSPHEREFILLED = 217
    COLORSPHEREARROW2D = 218
    COLORSPHEREARROW2DFILLED = 219
    COLORSPHEREARROW3D = 220
    COLORSPHEREARROW3DFILLED = 221
    COLORSPHERECROSSLINE = 222
    COLORSPHERECROSSLINEFILLED = 223


class ShapeEnumAttrOperator(EnumAttrOperator[ShapeEnumPlugOperator]):
    __slots__ = ()

    GEAR = 0
    GEARFILLED = 1
    LINE = 2
    LINEARROWATEND = 3
    LINEARROWATENDFILLED = 4
    LINEARROWATENDS = 5
    LINEARROWATENDSFILLED = 6
    LINEWIDEARROWATEND = 7
    LINEWIDEARROWATENDFILLED = 8
    LINEWIDEARROWATENDS = 9
    LINEWIDEARROWATENDSFILLED = 10
    LINESQUAREATEND = 11
    LINESQUAREATENDFILLED = 12
    LINESQUAREATENDS = 13
    LINESQUAREATENDSFILLED = 14
    LINEDIAMONDATEND = 15
    LINEDIAMONDATENDFILLED = 16
    LINEDIAMONDATENDS = 17
    LINEDIAMONDATENDSFILLED = 18
    LINECIRCLEATEND = 19
    LINECIRCLEATENDFILLED = 20
    LINECIRCLEATENDS = 21
    LINECIRCLEATENDSFILLED = 22
    LINETRIANGLEATEND = 23
    LINETRIANGLEATENDFILLED = 24
    LINETRIANGLEATENDS = 25
    LINETRIANGLEATENDSFILLED = 26
    CROSSLINE1ST2ND = 27
    CROSSLINE1ST2NDARROWATEND = 28
    CROSSLINE1ST2NDARROWATENDFILLED = 29
    CROSSLINE1ST2NDARROWATENDS = 30
    CROSSLINE1ST2NDARROWATENDSFILLED = 31
    CROSSLINE1ST2NDWIDEARROWATEND = 32
    CROSSLINE1ST2NDWIDEARROWATENDFILLED = 33
    CROSSLINE1ST2NDWIDEARROWATENDS = 34
    CROSSLINE1ST2NDWIDEARROWATENDSFILLED = 35
    CROSSLINE1ST2NDSQUAREATEND = 36
    CROSSLINE1ST2NDSQUAREATENDFILLED = 37
    CROSSLINE1ST2NDSQUAREATENDS = 38
    CROSSLINE1ST2NDSQUAREATENDSFILLED = 39
    CROSSLINE1ST2NDDIAMONDATEND = 40
    CROSSLINE1ST2NDDIAMONDATENDFILLED = 41
    CROSSLINE1ST2NDDIAMONDATENDS = 42
    CROSSLINE1ST2NDDIAMONDATENDSFILLED = 43
    CROSSLINE1ST2NDCIRCLEATEND = 44
    CROSSLINE1ST2NDCIRCLEATENDFILLED = 45
    CROSSLINE1ST2NDCIRCLEATENDS = 46
    CROSSLINE1ST2NDCIRCLEATENDSFILLED = 47
    CROSSLINE1ST2NDTRIANGLEATEND = 48
    CROSSLINE1ST2NDTRIANGLEATENDFILLED = 49
    CROSSLINE1ST2NDTRIANGLEATENDS = 50
    CROSSLINE1ST2NDTRIANGLEATENDSFILLED = 51
    CROSSLINE1ST3RD = 52
    CROSSLINE1ST3RDARROWATEND = 53
    CROSSLINE1ST3RDARROWATENDFILLED = 54
    CROSSLINE1ST3RDARROWATENDS = 55
    CROSSLINE1ST3RDARROWATENDSFILLED = 56
    CROSSLINE1ST3RDWIDEARROWATEND = 57
    CROSSLINE1ST3RDWIDEARROWATENDFILLED = 58
    CROSSLINE1ST3RDWIDEARROWATENDS = 59
    CROSSLINE1ST3RDWIDEARROWATENDSFILLED = 60
    CROSSLINE1ST3RDSQUAREATEND = 61
    CROSSLINE1ST3RDSQUAREATENDFILLED = 62
    CROSSLINE1ST3RDSQUAREATENDS = 63
    CROSSLINE1ST3RDSQUAREATENDSFILLED = 64
    CROSSLINE1ST3RDDIAMONDATEND = 65
    CROSSLINE1ST3RDDIAMONDATENDFILLED = 66
    CROSSLINE1ST3RDDIAMONDATENDS = 67
    CROSSLINE1ST3RDDIAMONDATENDSFILLED = 68
    CROSSLINE1ST3RDCIRCLEATEND = 69
    CROSSLINE1ST3RDCIRCLEATENDFILLED = 70
    CROSSLINE1ST3RDCIRCLEATENDS = 71
    CROSSLINE1ST3RDCIRCLEATENDSFILLED = 72
    CROSSLINE1ST3RDTRIANGLEATEND = 73
    CROSSLINE1ST3RDTRIANGLEATENDFILLED = 74
    CROSSLINE1ST3RDTRIANGLEATENDS = 75
    CROSSLINE1ST3RDTRIANGLEATENDSFILLED = 76
    CROSSLINE2ND3RD = 77
    CROSSLINE2ND3RDARROWATEND = 78
    CROSSLINE2ND3RDARROWATENDFILLED = 79
    CROSSLINE2ND3RDARROWATENDS = 80
    CROSSLINE2ND3RDARROWATENDSFILLED = 81
    CROSSLINE2ND3RDWIDEARROWATEND = 82
    CROSSLINE2ND3RDWIDEARROWATENDFILLED = 83
    CROSSLINE2ND3RDWIDEARROWATENDS = 84
    CROSSLINE2ND3RDWIDEARROWATENDSFILLED = 85
    CROSSLINE2ND3RDSQUAREATEND = 86
    CROSSLINE2ND3RDSQUAREATENDFILLED = 87
    CROSSLINE2ND3RDSQUAREATENDS = 88
    CROSSLINE2ND3RDSQUAREATENDSFILLED = 89
    CROSSLINE2ND3RDDIAMONDATEND = 90
    CROSSLINE2ND3RDDIAMONDATENDFILLED = 91
    CROSSLINE2ND3RDDIAMONDATENDS = 92
    CROSSLINE2ND3RDDIAMONDATENDSFILLED = 93
    CROSSLINE2ND3RDCIRCLEATEND = 94
    CROSSLINE2ND3RDCIRCLEATENDFILLED = 95
    CROSSLINE2ND3RDCIRCLEATENDS = 96
    CROSSLINE2ND3RDCIRCLEATENDSFILLED = 97
    CROSSLINE2ND3RDTRIANGLEATEND = 98
    CROSSLINE2ND3RDTRIANGLEATENDFILLED = 99
    CROSSLINE2ND3RDTRIANGLEATENDS = 100
    CROSSLINE2ND3RDTRIANGLEATENDSFILLED = 101
    CROSSLINE3AXIS = 102
    CROSSLINE3AXISENDCUBE = 103
    CROSSLINE3AXISENDCUBEFILLED = 104
    CROSSLINE3AXISENDOCTAHEDRON = 105
    CROSSLINE3AXISENDOCTAHEDRONFILLED = 106
    CROSSLINE3AXISENDSPHERE = 107
    CROSSLINE3AXISENDSPHEREFILLED = 108
    CROSSLINE3AXISENDPYRAMID = 109
    CROSSLINE3AXISENDPYRAMIDFILLED = 110
    CROSSLINE3AXISENDCONE = 111
    CROSSLINE3AXISENDCONEFILLED = 112
    TRIANGLE = 113
    TRIANGLEFILLED = 114
    TRIANGLEARROW3D = 115
    TRIANGLEARROW3DFILLED = 116
    SQUARE = 117
    SQUAREFILLED = 118
    SQUAREARROW2D = 119
    SQUAREARROW2DFILLED = 120
    SQUAREARROW3D = 121
    SQUAREARROW3DFILLED = 122
    SQUAREARROWCROSSLINE2D = 123
    SQUAREARROWCROSSLINE2DFILLED = 124
    SQUAREARROWCROSSLINE3D = 125
    SQUAREARROWCROSSLINE3DFILLED = 126
    SQUAREARROWCROSSLINETEMPLATE2D = 127
    SQUAREARROWCROSSLINETEMPLATE2DFILLED = 128
    SQUAREARROWCROSSLINETEMPLATE3D = 129
    SQUAREARROWCROSSLINETEMPLATE3DFILLED = 130
    SQUAREARROW4WAY2D = 131
    SQUAREARROW4WAY2DFILLED = 132
    SQUAREARROW4WAY3D = 133
    SQUAREARROW4WAY3DFILLED = 134
    SQUARETEMPLATEARROW4WAY2D = 135
    SQUARETEMPLATEARROW4WAY2DFILLED = 136
    SQUARETEMPLATEARROW4WAY3D = 137
    SQUARETEMPLATEARROW4WAY3DFILLED = 138
    DIAMOND = 139
    DIAMONDFILLED = 140
    CUBE = 141
    CUBEFILLED = 142
    CUBEARROW2D = 143
    CUBEARROW2DFILLED = 144
    CUBEARROW3D = 145
    CUBEARROW3DFILLED = 146
    CUBEFIN = 147
    CUBEFINFILLED = 148
    CUBEFINARROW = 149
    CUBEFINARROWFILLED = 150
    OCTAHEDRON = 151
    OCTAHEDRONFILLED = 152
    OCTAHEDRONARROW = 153
    OCTAHEDRONARROWFILLED = 154
    OCTAHEDRONARROWFIN = 155
    OCTAHEDRONARROWFINFILLED = 156
    CIRCLE = 157
    CIRCLEFILLED = 158
    CIRCLEARROW2D = 159
    CIRCLEARROW2DFILLED = 160
    CIRCLEARROW3D = 161
    CIRCLEARROW3DFILLED = 162
    SEMICIRCLE = 163
    SEMICIRCLEFILLED = 164
    SEMICIRCLEARROWATEND = 165
    SEMICIRCLEARROWATENDFILLED = 166
    SEMICIRCLEARROWATENDS = 167
    SEMICIRCLEARROWATENDSFILLED = 168
    SEMICIRCLEWIDEARROWATEND = 169
    SEMICIRCLEWIDEARROWATENDFILLED = 170
    SEMICIRCLEWIDEARROWATENDS = 171
    SEMICIRCLEWIDEARROWATENDSFILLED = 172
    SEMICIRCLEARROW2D = 173
    SEMICIRCLEARROW2DFILLED = 174
    SEMICIRCLEARROW3D = 175
    SEMICIRCLEARROW3DFILLED = 176
    SPHERE = 177
    SPHEREFILLED = 178
    SPHEREARROW2D = 179
    SPHEREARROW2DFILLED = 180
    SPHEREARROW3D = 181
    SPHEREARROW3DFILLED = 182
    CYLINDER = 183
    CYLINDERFILLED = 184
    CYLINDERFIN = 185
    CYLINDERFINFILLED = 186
    CYLINDERFINARROW = 187
    CYLINDERFINARROWFILLED = 188
    ARROW = 189
    ARROWFILLED = 190
    ARROWFIN = 191
    ARROWFINFILLED = 192
    PYRAMID = 193
    PYRAMIDFILLED = 194
    PYRAMIDFIN = 195
    PYRAMIDFINFILLED = 196
    CONE = 197
    CONEFILLED = 198
    CONEFIN = 199
    CONEFINFILLED = 200
    COLORCROSSLINE3AXIS = 201
    COLORCROSSLINE3AXISENDCUBE = 202
    COLORCROSSLINE3AXISENDCUBEFILLED = 203
    COLORCROSSLINE3AXISENDOCTAHEDRON = 204
    COLORCROSSLINE3AXISENDOCTAHEDRONFILLED = 205
    COLORCROSSLINE3AXISENDSPHERE = 206
    COLORCROSSLINE3AXISENDSPHEREFILLED = 207
    COLORCROSSLINE3AXISENDPYRAMID = 208
    COLORCROSSLINE3AXISENDPYRAMIDFILLED = 209
    COLORCROSSLINE3AXISENDCONE = 210
    COLORCROSSLINE3AXISENDCONEFILLED = 211
    COLORCUBE = 212
    COLORCUBEFILLED = 213
    COLORCORNERCUBE = 214
    COLORCORNERCUBEFILLED = 215
    COLORSPHERE = 216
    COLORSPHEREFILLED = 217
    COLORSPHEREARROW2D = 218
    COLORSPHEREARROW2DFILLED = 219
    COLORSPHEREARROW3D = 220
    COLORSPHEREARROW3DFILLED = 221
    COLORSPHERECROSSLINE = 222
    COLORSPHERECROSSLINEFILLED = 223

    NAME_MAP = {
        GEAR: "Gear",
        GEARFILLED: "GearFilled",
        LINE: "Line",
        LINEARROWATEND: "LineArrowAtEnd",
        LINEARROWATENDFILLED: "LineArrowAtEndFilled",
        LINEARROWATENDS: "LineArrowAtEnds",
        LINEARROWATENDSFILLED: "LineArrowAtEndsFilled",
        LINEWIDEARROWATEND: "LineWideArrowAtEnd",
        LINEWIDEARROWATENDFILLED: "LineWideArrowAtEndFilled",
        LINEWIDEARROWATENDS: "LineWideArrowAtEnds",
        LINEWIDEARROWATENDSFILLED: "LineWideArrowAtEndsFilled",
        LINESQUAREATEND: "LineSquareAtEnd",
        LINESQUAREATENDFILLED: "LineSquareAtEndFilled",
        LINESQUAREATENDS: "LineSquareAtEnds",
        LINESQUAREATENDSFILLED: "LineSquareAtEndsFilled",
        LINEDIAMONDATEND: "LineDiamondAtEnd",
        LINEDIAMONDATENDFILLED: "LineDiamondAtEndFilled",
        LINEDIAMONDATENDS: "LineDiamondAtEnds",
        LINEDIAMONDATENDSFILLED: "LineDiamondAtEndsFilled",
        LINECIRCLEATEND: "LineCircleAtEnd",
        LINECIRCLEATENDFILLED: "LineCircleAtEndFilled",
        LINECIRCLEATENDS: "LineCircleAtEnds",
        LINECIRCLEATENDSFILLED: "LineCircleAtEndsFilled",
        LINETRIANGLEATEND: "LineTriangleAtEnd",
        LINETRIANGLEATENDFILLED: "LineTriangleAtEndFilled",
        LINETRIANGLEATENDS: "LineTriangleAtEnds",
        LINETRIANGLEATENDSFILLED: "LineTriangleAtEndsFilled",
        CROSSLINE1ST2ND: "CrossLine1st2nd",
        CROSSLINE1ST2NDARROWATEND: "CrossLine1st2ndArrowAtEnd",
        CROSSLINE1ST2NDARROWATENDFILLED: "CrossLine1st2ndArrowAtEndFilled",
        CROSSLINE1ST2NDARROWATENDS: "CrossLine1st2ndArrowAtEnds",
        CROSSLINE1ST2NDARROWATENDSFILLED: "CrossLine1st2ndArrowAtEndsFilled",
        CROSSLINE1ST2NDWIDEARROWATEND: "CrossLine1st2ndWideArrowAtEnd",
        CROSSLINE1ST2NDWIDEARROWATENDFILLED: (
            "CrossLine1st2ndWideArrowAtEndFilled"
        ),
        CROSSLINE1ST2NDWIDEARROWATENDS: "CrossLine1st2ndWideArrowAtEnds",
        CROSSLINE1ST2NDWIDEARROWATENDSFILLED: (
            "CrossLine1st2ndWideArrowAtEndsFilled"
        ),
        CROSSLINE1ST2NDSQUAREATEND: "CrossLine1st2ndSquareAtEnd",
        CROSSLINE1ST2NDSQUAREATENDFILLED: "CrossLine1st2ndSquareAtEndFilled",
        CROSSLINE1ST2NDSQUAREATENDS: "CrossLine1st2ndSquareAtEnds",
        CROSSLINE1ST2NDSQUAREATENDSFILLED: "CrossLine1st2ndSquareAtEndsFilled",
        CROSSLINE1ST2NDDIAMONDATEND: "CrossLine1st2ndDiamondAtEnd",
        CROSSLINE1ST2NDDIAMONDATENDFILLED: "CrossLine1st2ndDiamondAtEndFilled",
        CROSSLINE1ST2NDDIAMONDATENDS: "CrossLine1st2ndDiamondAtEnds",
        CROSSLINE1ST2NDDIAMONDATENDSFILLED: (
            "CrossLine1st2ndDiamondAtEndsFilled"
        ),
        CROSSLINE1ST2NDCIRCLEATEND: "CrossLine1st2ndCircleAtEnd",
        CROSSLINE1ST2NDCIRCLEATENDFILLED: "CrossLine1st2ndCircleAtEndFilled",
        CROSSLINE1ST2NDCIRCLEATENDS: "CrossLine1st2ndCircleAtEnds",
        CROSSLINE1ST2NDCIRCLEATENDSFILLED: "CrossLine1st2ndCircleAtEndsFilled",
        CROSSLINE1ST2NDTRIANGLEATEND: "CrossLine1st2ndTriangleAtEnd",
        CROSSLINE1ST2NDTRIANGLEATENDFILLED: (
            "CrossLine1st2ndTriangleAtEndFilled"
        ),
        CROSSLINE1ST2NDTRIANGLEATENDS: "CrossLine1st2ndTriangleAtEnds",
        CROSSLINE1ST2NDTRIANGLEATENDSFILLED: (
            "CrossLine1st2ndTriangleAtEndsFilled"
        ),
        CROSSLINE1ST3RD: "CrossLine1st3rd",
        CROSSLINE1ST3RDARROWATEND: "CrossLine1st3rdArrowAtEnd",
        CROSSLINE1ST3RDARROWATENDFILLED: "CrossLine1st3rdArrowAtEndFilled",
        CROSSLINE1ST3RDARROWATENDS: "CrossLine1st3rdArrowAtEnds",
        CROSSLINE1ST3RDARROWATENDSFILLED: "CrossLine1st3rdArrowAtEndsFilled",
        CROSSLINE1ST3RDWIDEARROWATEND: "CrossLine1st3rdWideArrowAtEnd",
        CROSSLINE1ST3RDWIDEARROWATENDFILLED: (
            "CrossLine1st3rdWideArrowAtEndFilled"
        ),
        CROSSLINE1ST3RDWIDEARROWATENDS: "CrossLine1st3rdWideArrowAtEnds",
        CROSSLINE1ST3RDWIDEARROWATENDSFILLED: (
            "CrossLine1st3rdWideArrowAtEndsFilled"
        ),
        CROSSLINE1ST3RDSQUAREATEND: "CrossLine1st3rdSquareAtEnd",
        CROSSLINE1ST3RDSQUAREATENDFILLED: "CrossLine1st3rdSquareAtEndFilled",
        CROSSLINE1ST3RDSQUAREATENDS: "CrossLine1st3rdSquareAtEnds",
        CROSSLINE1ST3RDSQUAREATENDSFILLED: "CrossLine1st3rdSquareAtEndsFilled",
        CROSSLINE1ST3RDDIAMONDATEND: "CrossLine1st3rdDiamondAtEnd",
        CROSSLINE1ST3RDDIAMONDATENDFILLED: "CrossLine1st3rdDiamondAtEndFilled",
        CROSSLINE1ST3RDDIAMONDATENDS: "CrossLine1st3rdDiamondAtEnds",
        CROSSLINE1ST3RDDIAMONDATENDSFILLED: (
            "CrossLine1st3rdDiamondAtEndsFilled"
        ),
        CROSSLINE1ST3RDCIRCLEATEND: "CrossLine1st3rdCircleAtEnd",
        CROSSLINE1ST3RDCIRCLEATENDFILLED: "CrossLine1st3rdCircleAtEndFilled",
        CROSSLINE1ST3RDCIRCLEATENDS: "CrossLine1st3rdCircleAtEnds",
        CROSSLINE1ST3RDCIRCLEATENDSFILLED: "CrossLine1st3rdCircleAtEndsFilled",
        CROSSLINE1ST3RDTRIANGLEATEND: "CrossLine1st3rdTriangleAtEnd",
        CROSSLINE1ST3RDTRIANGLEATENDFILLED: (
            "CrossLine1st3rdTriangleAtEndFilled"
        ),
        CROSSLINE1ST3RDTRIANGLEATENDS: "CrossLine1st3rdTriangleAtEnds",
        CROSSLINE1ST3RDTRIANGLEATENDSFILLED: (
            "CrossLine1st3rdTriangleAtEndsFilled"
        ),
        CROSSLINE2ND3RD: "CrossLine2nd3rd",
        CROSSLINE2ND3RDARROWATEND: "CrossLine2nd3rdArrowAtEnd",
        CROSSLINE2ND3RDARROWATENDFILLED: "CrossLine2nd3rdArrowAtEndFilled",
        CROSSLINE2ND3RDARROWATENDS: "CrossLine2nd3rdArrowAtEnds",
        CROSSLINE2ND3RDARROWATENDSFILLED: "CrossLine2nd3rdArrowAtEndsFilled",
        CROSSLINE2ND3RDWIDEARROWATEND: "CrossLine2nd3rdWideArrowAtEnd",
        CROSSLINE2ND3RDWIDEARROWATENDFILLED: (
            "CrossLine2nd3rdWideArrowAtEndFilled"
        ),
        CROSSLINE2ND3RDWIDEARROWATENDS: "CrossLine2nd3rdWideArrowAtEnds",
        CROSSLINE2ND3RDWIDEARROWATENDSFILLED: (
            "CrossLine2nd3rdWideArrowAtEndsFilled"
        ),
        CROSSLINE2ND3RDSQUAREATEND: "CrossLine2nd3rdSquareAtEnd",
        CROSSLINE2ND3RDSQUAREATENDFILLED: "CrossLine2nd3rdSquareAtEndFilled",
        CROSSLINE2ND3RDSQUAREATENDS: "CrossLine2nd3rdSquareAtEnds",
        CROSSLINE2ND3RDSQUAREATENDSFILLED: "CrossLine2nd3rdSquareAtEndsFilled",
        CROSSLINE2ND3RDDIAMONDATEND: "CrossLine2nd3rdDiamondAtEnd",
        CROSSLINE2ND3RDDIAMONDATENDFILLED: "CrossLine2nd3rdDiamondAtEndFilled",
        CROSSLINE2ND3RDDIAMONDATENDS: "CrossLine2nd3rdDiamondAtEnds",
        CROSSLINE2ND3RDDIAMONDATENDSFILLED: (
            "CrossLine2nd3rdDiamondAtEndsFilled"
        ),
        CROSSLINE2ND3RDCIRCLEATEND: "CrossLine2nd3rdCircleAtEnd",
        CROSSLINE2ND3RDCIRCLEATENDFILLED: "CrossLine2nd3rdCircleAtEndFilled",
        CROSSLINE2ND3RDCIRCLEATENDS: "CrossLine2nd3rdCircleAtEnds",
        CROSSLINE2ND3RDCIRCLEATENDSFILLED: "CrossLine2nd3rdCircleAtEndsFilled",
        CROSSLINE2ND3RDTRIANGLEATEND: "CrossLine2nd3rdTriangleAtEnd",
        CROSSLINE2ND3RDTRIANGLEATENDFILLED: (
            "CrossLine2nd3rdTriangleAtEndFilled"
        ),
        CROSSLINE2ND3RDTRIANGLEATENDS: "CrossLine2nd3rdTriangleAtEnds",
        CROSSLINE2ND3RDTRIANGLEATENDSFILLED: (
            "CrossLine2nd3rdTriangleAtEndsFilled"
        ),
        CROSSLINE3AXIS: "CrossLine3Axis",
        CROSSLINE3AXISENDCUBE: "CrossLine3AxisEndCube",
        CROSSLINE3AXISENDCUBEFILLED: "CrossLine3AxisEndCubeFilled",
        CROSSLINE3AXISENDOCTAHEDRON: "CrossLine3AxisEndOctahedron",
        CROSSLINE3AXISENDOCTAHEDRONFILLED: "CrossLine3AxisEndOctahedronFilled",
        CROSSLINE3AXISENDSPHERE: "CrossLine3AxisEndSphere",
        CROSSLINE3AXISENDSPHEREFILLED: "CrossLine3AxisEndSphereFilled",
        CROSSLINE3AXISENDPYRAMID: "CrossLine3AxisEndPyramid",
        CROSSLINE3AXISENDPYRAMIDFILLED: "CrossLine3AxisEndPyramidFilled",
        CROSSLINE3AXISENDCONE: "CrossLine3AxisEndCone",
        CROSSLINE3AXISENDCONEFILLED: "CrossLine3AxisEndConeFilled",
        TRIANGLE: "Triangle",
        TRIANGLEFILLED: "TriangleFilled",
        TRIANGLEARROW3D: "TriangleArrow3D",
        TRIANGLEARROW3DFILLED: "TriangleArrow3DFilled",
        SQUARE: "Square",
        SQUAREFILLED: "SquareFilled",
        SQUAREARROW2D: "SquareArrow2D",
        SQUAREARROW2DFILLED: "SquareArrow2DFilled",
        SQUAREARROW3D: "SquareArrow3D",
        SQUAREARROW3DFILLED: "SquareArrow3DFilled",
        SQUAREARROWCROSSLINE2D: "SquareArrowCrossLine2D",
        SQUAREARROWCROSSLINE2DFILLED: "SquareArrowCrossLine2DFilled",
        SQUAREARROWCROSSLINE3D: "SquareArrowCrossLine3D",
        SQUAREARROWCROSSLINE3DFILLED: "SquareArrowCrossLine3DFilled",
        SQUAREARROWCROSSLINETEMPLATE2D: "SquareArrowCrossLineTemplate2D",
        SQUAREARROWCROSSLINETEMPLATE2DFILLED: (
            "SquareArrowCrossLineTemplate2DFilled"
        ),
        SQUAREARROWCROSSLINETEMPLATE3D: "SquareArrowCrossLineTemplate3D",
        SQUAREARROWCROSSLINETEMPLATE3DFILLED: (
            "SquareArrowCrossLineTemplate3DFilled"
        ),
        SQUAREARROW4WAY2D: "SquareArrow4Way2D",
        SQUAREARROW4WAY2DFILLED: "SquareArrow4Way2DFilled",
        SQUAREARROW4WAY3D: "SquareArrow4Way3D",
        SQUAREARROW4WAY3DFILLED: "SquareArrow4Way3DFilled",
        SQUARETEMPLATEARROW4WAY2D: "SquareTemplateArrow4Way2D",
        SQUARETEMPLATEARROW4WAY2DFILLED: "SquareTemplateArrow4Way2DFilled",
        SQUARETEMPLATEARROW4WAY3D: "SquareTemplateArrow4Way3D",
        SQUARETEMPLATEARROW4WAY3DFILLED: "SquareTemplateArrow4Way3DFilled",
        DIAMOND: "Diamond",
        DIAMONDFILLED: "DiamondFilled",
        CUBE: "Cube",
        CUBEFILLED: "CubeFilled",
        CUBEARROW2D: "CubeArrow2D",
        CUBEARROW2DFILLED: "CubeArrow2DFilled",
        CUBEARROW3D: "CubeArrow3D",
        CUBEARROW3DFILLED: "CubeArrow3DFilled",
        CUBEFIN: "CubeFin",
        CUBEFINFILLED: "CubeFinFilled",
        CUBEFINARROW: "CubeFinArrow",
        CUBEFINARROWFILLED: "CubeFinArrowFilled",
        OCTAHEDRON: "Octahedron",
        OCTAHEDRONFILLED: "OctahedronFilled",
        OCTAHEDRONARROW: "OctahedronArrow",
        OCTAHEDRONARROWFILLED: "OctahedronArrowFilled",
        OCTAHEDRONARROWFIN: "OctahedronArrowFin",
        OCTAHEDRONARROWFINFILLED: "OctahedronArrowFinFilled",
        CIRCLE: "Circle",
        CIRCLEFILLED: "CircleFilled",
        CIRCLEARROW2D: "CircleArrow2D",
        CIRCLEARROW2DFILLED: "CircleArrow2DFilled",
        CIRCLEARROW3D: "CircleArrow3D",
        CIRCLEARROW3DFILLED: "CircleArrow3DFilled",
        SEMICIRCLE: "Semicircle",
        SEMICIRCLEFILLED: "SemicircleFilled",
        SEMICIRCLEARROWATEND: "SemicircleArrowAtEnd",
        SEMICIRCLEARROWATENDFILLED: "SemicircleArrowAtEndFilled",
        SEMICIRCLEARROWATENDS: "SemicircleArrowAtEnds",
        SEMICIRCLEARROWATENDSFILLED: "SemicircleArrowAtEndsFilled",
        SEMICIRCLEWIDEARROWATEND: "SemicircleWideArrowAtEnd",
        SEMICIRCLEWIDEARROWATENDFILLED: "SemicircleWideArrowAtEndFilled",
        SEMICIRCLEWIDEARROWATENDS: "SemicircleWideArrowAtEnds",
        SEMICIRCLEWIDEARROWATENDSFILLED: "SemicircleWideArrowAtEndsFilled",
        SEMICIRCLEARROW2D: "SemicircleArrow2D",
        SEMICIRCLEARROW2DFILLED: "SemicircleArrow2DFilled",
        SEMICIRCLEARROW3D: "SemicircleArrow3D",
        SEMICIRCLEARROW3DFILLED: "SemicircleArrow3DFilled",
        SPHERE: "Sphere",
        SPHEREFILLED: "SphereFilled",
        SPHEREARROW2D: "SphereArrow2D",
        SPHEREARROW2DFILLED: "SphereArrow2DFilled",
        SPHEREARROW3D: "SphereArrow3D",
        SPHEREARROW3DFILLED: "SphereArrow3DFilled",
        CYLINDER: "Cylinder",
        CYLINDERFILLED: "CylinderFilled",
        CYLINDERFIN: "CylinderFin",
        CYLINDERFINFILLED: "CylinderFinFilled",
        CYLINDERFINARROW: "CylinderFinArrow",
        CYLINDERFINARROWFILLED: "CylinderFinArrowFilled",
        ARROW: "Arrow",
        ARROWFILLED: "ArrowFilled",
        ARROWFIN: "ArrowFin",
        ARROWFINFILLED: "ArrowFinFilled",
        PYRAMID: "Pyramid",
        PYRAMIDFILLED: "PyramidFilled",
        PYRAMIDFIN: "PyramidFin",
        PYRAMIDFINFILLED: "PyramidFinFilled",
        CONE: "Cone",
        CONEFILLED: "ConeFilled",
        CONEFIN: "ConeFin",
        CONEFINFILLED: "ConeFinFilled",
        COLORCROSSLINE3AXIS: "ColorCrossLine3Axis",
        COLORCROSSLINE3AXISENDCUBE: "ColorCrossLine3AxisEndCube",
        COLORCROSSLINE3AXISENDCUBEFILLED: "ColorCrossLine3AxisEndCubeFilled",
        COLORCROSSLINE3AXISENDOCTAHEDRON: "ColorCrossLine3AxisEndOctahedron",
        COLORCROSSLINE3AXISENDOCTAHEDRONFILLED: (
            "ColorCrossLine3AxisEndOctahedronFilled"
        ),
        COLORCROSSLINE3AXISENDSPHERE: "ColorCrossLine3AxisEndSphere",
        COLORCROSSLINE3AXISENDSPHEREFILLED: (
            "ColorCrossLine3AxisEndSphereFilled"
        ),
        COLORCROSSLINE3AXISENDPYRAMID: "ColorCrossLine3AxisEndPyramid",
        COLORCROSSLINE3AXISENDPYRAMIDFILLED: (
            "ColorCrossLine3AxisEndPyramidFilled"
        ),
        COLORCROSSLINE3AXISENDCONE: "ColorCrossLine3AxisEndCone",
        COLORCROSSLINE3AXISENDCONEFILLED: "ColorCrossLine3AxisEndConeFilled",
        COLORCUBE: "ColorCube",
        COLORCUBEFILLED: "ColorCubeFilled",
        COLORCORNERCUBE: "ColorCornerCube",
        COLORCORNERCUBEFILLED: "ColorCornerCubeFilled",
        COLORSPHERE: "ColorSphere",
        COLORSPHEREFILLED: "ColorSphereFilled",
        COLORSPHEREARROW2D: "ColorSphereArrow2D",
        COLORSPHEREARROW2DFILLED: "ColorSphereArrow2DFilled",
        COLORSPHEREARROW3D: "ColorSphereArrow3D",
        COLORSPHEREARROW3DFILLED: "ColorSphereArrow3DFilled",
        COLORSPHERECROSSLINE: "ColorSphereCrossLine",
        COLORSPHERECROSSLINEFILLED: "ColorSphereCrossLineFilled",
    }


class ShapeEnumField(EnumField[ShapeEnumAttrOperator, ShapeEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ShapeEnumAttrOperator
    PLUG_CLS = ShapeEnumPlugOperator


class Shape1stAxisEnumPlugOperator(
    EnumPlugOperator["Shape1stAxisEnumAttrOperator"]
):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5


class Shape1stAxisEnumAttrOperator(
    EnumAttrOperator[Shape1stAxisEnumPlugOperator]
):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5

    NAME_MAP = {
        PLUS_X: "+X",
        MINUS_X: "-X",
        PLUS_Y: "+Y",
        MINUS_Y: "-Y",
        PLUS_Z: "+Z",
        MINUS_Z: "-Z",
    }


class Shape1stAxisEnumField(
    EnumField[Shape1stAxisEnumAttrOperator, Shape1stAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Shape1stAxisEnumAttrOperator
    PLUG_CLS = Shape1stAxisEnumPlugOperator


class Shape2ndAxisEnumPlugOperator(
    EnumPlugOperator["Shape2ndAxisEnumAttrOperator"]
):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5


class Shape2ndAxisEnumAttrOperator(
    EnumAttrOperator[Shape2ndAxisEnumPlugOperator]
):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5

    NAME_MAP = {
        PLUS_X: "+X",
        MINUS_X: "-X",
        PLUS_Y: "+Y",
        MINUS_Y: "-Y",
        PLUS_Z: "+Z",
        MINUS_Z: "-Z",
    }


class Shape2ndAxisEnumField(
    EnumField[Shape2ndAxisEnumAttrOperator, Shape2ndAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Shape2ndAxisEnumAttrOperator
    PLUG_CLS = Shape2ndAxisEnumPlugOperator


class ShapeAxisOffsetDirectionEnumPlugOperator(
    EnumPlugOperator["ShapeAxisOffsetDirectionEnumAttrOperator"]
):
    __slots__ = ()

    PLUS_1STAXIS = 0
    MINUS_1STAXIS = 1
    PLUS_2NDAXIS = 2
    MINUS_2NDAXIS = 3
    PLUS_3RDAXIS = 4
    MINUS_3RDAXIS = 5


class ShapeAxisOffsetDirectionEnumAttrOperator(
    EnumAttrOperator[ShapeAxisOffsetDirectionEnumPlugOperator]
):
    __slots__ = ()

    PLUS_1STAXIS = 0
    MINUS_1STAXIS = 1
    PLUS_2NDAXIS = 2
    MINUS_2NDAXIS = 3
    PLUS_3RDAXIS = 4
    MINUS_3RDAXIS = 5

    NAME_MAP = {
        PLUS_1STAXIS: "+1stAxis",
        MINUS_1STAXIS: "-1stAxis",
        PLUS_2NDAXIS: "+2ndAxis",
        MINUS_2NDAXIS: "-2ndAxis",
        PLUS_3RDAXIS: "+3rdAxis",
        MINUS_3RDAXIS: "-3rdAxis",
    }


class ShapeAxisOffsetDirectionEnumField(
    EnumField[
        ShapeAxisOffsetDirectionEnumAttrOperator,
        ShapeAxisOffsetDirectionEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ShapeAxisOffsetDirectionEnumAttrOperator
    PLUG_CLS = ShapeAxisOffsetDirectionEnumPlugOperator


class BoundsModeEnumPlugOperator(
    EnumPlugOperator["BoundsModeEnumAttrOperator"]
):
    __slots__ = ()

    SHAPE = 0
    SHAPECENTERED = 1
    CUSTOM = 2


class BoundsModeEnumAttrOperator(EnumAttrOperator[BoundsModeEnumPlugOperator]):
    __slots__ = ()

    SHAPE = 0
    SHAPECENTERED = 1
    CUSTOM = 2

    NAME_MAP = {
        SHAPE: "Shape",
        SHAPECENTERED: "ShapeCentered",
        CUSTOM: "Custom",
    }


class BoundsModeEnumField(
    EnumField[BoundsModeEnumAttrOperator, BoundsModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoundsModeEnumAttrOperator
    PLUG_CLS = BoundsModeEnumPlugOperator


class CustomBounds1stAxisEnumPlugOperator(
    EnumPlugOperator["CustomBounds1stAxisEnumAttrOperator"]
):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5


class CustomBounds1stAxisEnumAttrOperator(
    EnumAttrOperator[CustomBounds1stAxisEnumPlugOperator]
):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5

    NAME_MAP = {
        PLUS_X: "+X",
        MINUS_X: "-X",
        PLUS_Y: "+Y",
        MINUS_Y: "-Y",
        PLUS_Z: "+Z",
        MINUS_Z: "-Z",
    }


class CustomBounds1stAxisEnumField(
    EnumField[
        CustomBounds1stAxisEnumAttrOperator,
        CustomBounds1stAxisEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CustomBounds1stAxisEnumAttrOperator
    PLUG_CLS = CustomBounds1stAxisEnumPlugOperator


class CustomBounds2ndAxisEnumPlugOperator(
    EnumPlugOperator["CustomBounds2ndAxisEnumAttrOperator"]
):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5


class CustomBounds2ndAxisEnumAttrOperator(
    EnumAttrOperator[CustomBounds2ndAxisEnumPlugOperator]
):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5

    NAME_MAP = {
        PLUS_X: "+X",
        MINUS_X: "-X",
        PLUS_Y: "+Y",
        MINUS_Y: "-Y",
        PLUS_Z: "+Z",
        MINUS_Z: "-Z",
    }


class CustomBounds2ndAxisEnumField(
    EnumField[
        CustomBounds2ndAxisEnumAttrOperator,
        CustomBounds2ndAxisEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CustomBounds2ndAxisEnumAttrOperator
    PLUG_CLS = CustomBounds2ndAxisEnumPlugOperator


class CustomBoundsAxisOffsetDirectionEnumPlugOperator(
    EnumPlugOperator["CustomBoundsAxisOffsetDirectionEnumAttrOperator"]
):
    __slots__ = ()

    PLUS_1STAXIS = 0
    MINUS_1STAXIS = 1
    PLUS_2NDAXIS = 2
    MINUS_2NDAXIS = 3
    PLUS_3RDAXIS = 4
    MINUS_3RDAXIS = 5


class CustomBoundsAxisOffsetDirectionEnumAttrOperator(
    EnumAttrOperator[CustomBoundsAxisOffsetDirectionEnumPlugOperator]
):
    __slots__ = ()

    PLUS_1STAXIS = 0
    MINUS_1STAXIS = 1
    PLUS_2NDAXIS = 2
    MINUS_2NDAXIS = 3
    PLUS_3RDAXIS = 4
    MINUS_3RDAXIS = 5

    NAME_MAP = {
        PLUS_1STAXIS: "+1stAxis",
        MINUS_1STAXIS: "-1stAxis",
        PLUS_2NDAXIS: "+2ndAxis",
        MINUS_2NDAXIS: "-2ndAxis",
        PLUS_3RDAXIS: "+3rdAxis",
        MINUS_3RDAXIS: "-3rdAxis",
    }


class CustomBoundsAxisOffsetDirectionEnumField(
    EnumField[
        CustomBoundsAxisOffsetDirectionEnumAttrOperator,
        CustomBoundsAxisOffsetDirectionEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CustomBoundsAxisOffsetDirectionEnumAttrOperator
    PLUG_CLS = CustomBoundsAxisOffsetDirectionEnumPlugOperator


class GeneratedBdControllerShape(Shape):
    __slots__ = ()

    NODE_TYPE = "bdControllerShape"

    renderType = ShortField(default_value=0)
    rt = renderType

    renderVolume = BoolField(default_value=False)
    rv = renderVolume

    visibleFraction = FloatField(default_value=1.0)
    vf = visibleFraction

    hardwareFogMultiplier = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    hfm = hardwareFogMultiplier

    motionBlur = BoolField(default_value=True)
    mb = motionBlur

    visibleInReflections = BoolField(default_value=False)
    vir = visibleInReflections

    visibleInRefractions = BoolField(default_value=False)
    vif = visibleInRefractions

    castsShadows = BoolField(default_value=True)
    csh = castsShadows

    receiveShadows = BoolField(default_value=True)
    rcsh = receiveShadows

    asBackground = BoolField(default_value=False)
    asbg = asBackground

    maxVisibilitySamplesOverride = BoolField(default_value=False)
    vbo = maxVisibilitySamplesOverride

    maxVisibilitySamples = LongField(
        default_value=1, min_value=1, max_value=32, soft_max_value=20
    )
    mvs = maxVisibilitySamples

    geometryAntialiasingOverride = BoolField(default_value=False)
    gao = geometryAntialiasingOverride

    antialiasingLevel = LongField(
        default_value=1, min_value=1, max_value=5, soft_max_value=5
    )
    gal = antialiasingLevel

    shadingSamplesOverride = BoolField(default_value=False)
    sso = shadingSamplesOverride

    shadingSamples = LongField(default_value=1, min_value=1, max_value=32)
    ssa = shadingSamples

    maxShadingSamples = LongField(
        default_value=1, min_value=1, max_value=32, soft_max_value=20
    )
    msa = maxShadingSamples

    volumeSamplesOverride = BoolField(default_value=False)
    vso = volumeSamplesOverride

    volumeSamples = LongField(default_value=1, soft_max_value=20)
    vss = volumeSamples

    depthJitter = BoolField(default_value=False)
    dej = depthJitter

    ignoreSelfShadowing = BoolField(default_value=False)
    iss = ignoreSelfShadowing

    primaryVisibility = BoolField(default_value=True)
    vis = primaryVisibility

    referenceObject = MessageField()
    rob = referenceObject

    compInstObjGroups = CompInstObjGroupsField(multi=True)
    ciog = compInstObjGroups

    componentTags = ComponentTagsField(multi=True)
    gtag = componentTags

    instMaterialAssign = MessageField(multi=True)
    imtla = instMaterialAssign

    pickTexture = MessageField()
    pte = pickTexture

    underWorldObject = BoolField(default_value=False)
    uwo = underWorldObject

    localPosition = LocalPositionField(default_value=(0.0, 0.0, 0.0))
    lp = localPosition
    localPositionX = localPosition.localPositionX
    lpx = localPositionX
    localPositionY = localPosition.localPositionY
    lpy = localPositionY
    localPositionZ = localPosition.localPositionZ
    lpz = localPositionZ

    worldPosition = WorldPositionField(
        multi=True, default_value=(0.0, 0.0, 0.0), writable=False
    )
    wp = worldPosition

    localScale = LocalScaleField(default_value=(1.0, 1.0, 1.0))
    los = localScale
    localScaleX = localScale.localScaleX
    lsx = localScaleX
    localScaleY = localScale.localScaleY
    lsy = localScaleY
    localScaleZ = localScale.localScaleZ
    lsz = localScaleZ

    shape = ShapeEnumField(default_value=141)
    sh = shape

    shapeAnimationTransformMatrix = DataMatrixField()
    satm = shapeAnimationTransformMatrix

    shapeDrawOnTop = BoolField(default_value=False)
    sdot = shapeDrawOnTop

    shapeLineWidth = FloatField(default_value=1.0, min_value=1.0)
    slw = shapeLineWidth

    shapeTransparency = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    stp = shapeTransparency

    shapeFillTransparency = FloatField(
        default_value=0.8500000238418579, min_value=0.0, max_value=1.0
    )
    sftp = shapeFillTransparency

    showShapeOffsetLine = BoolField(default_value=False)
    ssol = showShapeOffsetLine

    shapeOffsetLineTemplate = BoolField(default_value=False)
    solt = shapeOffsetLineTemplate

    shape1stAxis = Shape1stAxisEnumField(default_value=0)
    s1a = shape1stAxis

    shape2ndAxis = Shape2ndAxisEnumField(default_value=2)
    s2a = shape2ndAxis

    shapeAxisOffset = BoolField(default_value=False)
    sao = shapeAxisOffset

    shapeAxisOffsetDirection = ShapeAxisOffsetDirectionEnumField(
        default_value=0
    )
    saod = shapeAxisOffsetDirection

    shapeAxisOffsetLength = DoubleLinearField(default_value=1.0, min_value=0.0)
    saol = shapeAxisOffsetLength

    shapeRootSize = DoubleField(default_value=1.0)
    srs = shapeRootSize

    shapeTranslate = ShapeTranslateField(default_value=(0.0, 0.0, 0.0))
    st = shapeTranslate
    shapeTranslateX = shapeTranslate.shapeTranslateX
    stx = shapeTranslateX
    shapeTranslateY = shapeTranslate.shapeTranslateY
    sty = shapeTranslateY
    shapeTranslateZ = shapeTranslate.shapeTranslateZ
    stz = shapeTranslateZ

    shapeRotate = ShapeRotateField(default_value=(0.0, 0.0, 0.0))
    sr = shapeRotate
    shapeRotateX = shapeRotate.shapeRotateX
    srx = shapeRotateX
    shapeRotateY = shapeRotate.shapeRotateY
    sry = shapeRotateY
    shapeRotateZ = shapeRotate.shapeRotateZ
    srz = shapeRotateZ

    shapeScale = ShapeScaleField(default_value=(1.0, 1.0, 1.0))
    ssc = shapeScale
    shapeScaleX = shapeScale.shapeScaleX
    sscx = shapeScaleX
    shapeScaleY = shapeScale.shapeScaleY
    sscy = shapeScaleY
    shapeScaleZ = shapeScale.shapeScaleZ
    sscz = shapeScaleZ

    shapeAxisTranslate = ShapeAxisTranslateField(default_value=(0.0, 0.0, 0.0))
    sat = shapeAxisTranslate
    shapeAxisTranslateX = shapeAxisTranslate.shapeAxisTranslateX
    satx = shapeAxisTranslateX
    shapeAxisTranslateY = shapeAxisTranslate.shapeAxisTranslateY
    saty = shapeAxisTranslateY
    shapeAxisTranslateZ = shapeAxisTranslate.shapeAxisTranslateZ
    satz = shapeAxisTranslateZ

    shapeAxisRotate = ShapeAxisRotateField(default_value=(0.0, 0.0, 0.0))
    sar = shapeAxisRotate
    shapeAxisRotateX = shapeAxisRotate.shapeAxisRotateX
    sarx = shapeAxisRotateX
    shapeAxisRotateY = shapeAxisRotate.shapeAxisRotateY
    sary = shapeAxisRotateY
    shapeAxisRotateZ = shapeAxisRotate.shapeAxisRotateZ
    sarz = shapeAxisRotateZ

    shapeAxisScale = ShapeAxisScaleField(default_value=(1.0, 1.0, 1.0))
    sasc = shapeAxisScale
    shapeAxisScaleX = shapeAxisScale.shapeAxisScaleX
    sascx = shapeAxisScaleX
    shapeAxisScaleY = shapeAxisScale.shapeAxisScaleY
    sascy = shapeAxisScaleY
    shapeAxisScaleZ = shapeAxisScale.shapeAxisScaleZ
    sascz = shapeAxisScaleZ

    shapeSize = DoubleField(default_value=1.0)
    ss = shapeSize

    shapePartOffset = DoubleLinearField(default_value=0.0)
    spo = shapePartOffset

    shapePartOffsetAngle = DoubleAngleField(
        default_value=0.0, min_value=-90.0, max_value=90.0
    )
    spoa = shapePartOffsetAngle

    shapePartFinHeight = DoubleLinearField(default_value=0.5)
    spfh = shapePartFinHeight

    shapePartSize = DoubleField(default_value=1.0)
    sps = shapePartSize

    shapePartLengthScale = DoubleField(default_value=1.0)
    spls = shapePartLengthScale

    shapePartWidthScale = DoubleField(default_value=1.0)
    spws = shapePartWidthScale

    boundsMode = BoundsModeEnumField(default_value=1)
    bdm = boundsMode

    showBoundsPreview = BoolField(default_value=False)
    sbp = showBoundsPreview

    customBounds1stAxis = CustomBounds1stAxisEnumField(default_value=0)
    cb1a = customBounds1stAxis

    customBounds2ndAxis = CustomBounds2ndAxisEnumField(default_value=2)
    cb2a = customBounds2ndAxis

    customBoundsAxisOffset = BoolField(default_value=False)
    cbao = customBoundsAxisOffset

    customBoundsAxisOffsetDirection = CustomBoundsAxisOffsetDirectionEnumField(
        default_value=0
    )
    cbaod = customBoundsAxisOffsetDirection

    customBoundsAxisOffsetLength = DoubleLinearField(
        default_value=1.0, min_value=0.0
    )
    cbaol = customBoundsAxisOffsetLength

    customBoundsRootSize = DoubleField(default_value=1.0)
    cbrs = customBoundsRootSize

    customBoundsTranslate = CustomBoundsTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    cbt = customBoundsTranslate
    customBoundsTranslateX = customBoundsTranslate.customBoundsTranslateX
    cbtx = customBoundsTranslateX
    customBoundsTranslateY = customBoundsTranslate.customBoundsTranslateY
    cbty = customBoundsTranslateY
    customBoundsTranslateZ = customBoundsTranslate.customBoundsTranslateZ
    cbtz = customBoundsTranslateZ

    customBoundsRotate = CustomBoundsRotateField(default_value=(0.0, 0.0, 0.0))
    cbr = customBoundsRotate
    customBoundsRotateX = customBoundsRotate.customBoundsRotateX
    cbrx = customBoundsRotateX
    customBoundsRotateY = customBoundsRotate.customBoundsRotateY
    cbry = customBoundsRotateY
    customBoundsRotateZ = customBoundsRotate.customBoundsRotateZ
    cbrz = customBoundsRotateZ

    customBoundsScale = CustomBoundsScaleField(default_value=(1.0, 1.0, 1.0))
    cbsc = customBoundsScale
    customBoundsScaleX = customBoundsScale.customBoundsScaleX
    cbscx = customBoundsScaleX
    customBoundsScaleY = customBoundsScale.customBoundsScaleY
    cbscy = customBoundsScaleY
    customBoundsScaleZ = customBoundsScale.customBoundsScaleZ
    cbscz = customBoundsScaleZ

    customBoundsAxisTranslate = CustomBoundsAxisTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    cbat = customBoundsAxisTranslate
    customBoundsAxisTranslateX = (
        customBoundsAxisTranslate.customBoundsAxisTranslateX
    )
    cbatx = customBoundsAxisTranslateX
    customBoundsAxisTranslateY = (
        customBoundsAxisTranslate.customBoundsAxisTranslateY
    )
    cbaty = customBoundsAxisTranslateY
    customBoundsAxisTranslateZ = (
        customBoundsAxisTranslate.customBoundsAxisTranslateZ
    )
    cbatz = customBoundsAxisTranslateZ

    customBoundsAxisRotate = CustomBoundsAxisRotateField(
        default_value=(0.0, 0.0, 0.0)
    )
    cbar = customBoundsAxisRotate
    customBoundsAxisRotateX = customBoundsAxisRotate.customBoundsAxisRotateX
    cbarx = customBoundsAxisRotateX
    customBoundsAxisRotateY = customBoundsAxisRotate.customBoundsAxisRotateY
    cbary = customBoundsAxisRotateY
    customBoundsAxisRotateZ = customBoundsAxisRotate.customBoundsAxisRotateZ
    cbarz = customBoundsAxisRotateZ

    customBoundsAxisScale = CustomBoundsAxisScaleField(
        default_value=(1.0, 1.0, 1.0)
    )
    cbasc = customBoundsAxisScale
    customBoundsAxisScaleX = customBoundsAxisScale.customBoundsAxisScaleX
    cbascx = customBoundsAxisScaleX
    customBoundsAxisScaleY = customBoundsAxisScale.customBoundsAxisScaleY
    cbascy = customBoundsAxisScaleY
    customBoundsAxisScaleZ = customBoundsAxisScale.customBoundsAxisScaleZ
    cbascz = customBoundsAxisScaleZ

    customBoundsSize = DoubleField(default_value=1.0)
    cbs = customBoundsSize
