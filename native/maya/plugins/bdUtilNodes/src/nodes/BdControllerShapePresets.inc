// Static outline definitions extracted from the legacy ctrlshape.py.
// Coordinates remain in its original XY / +Z orientation until appendPresetComponent.
constexpr std::array<const char*, 274> kPresetNames = {
    "Gear",
    "GearFilled",
    "Line1st",
    "Line1stArrowAtEnd",
    "Line1stArrowAtEndFilled",
    "Line1stArrowAtEnds",
    "Line1stArrowAtEndsFilled",
    "Line1stWideArrowAtEnd",
    "Line1stWideArrowAtEndFilled",
    "Line1stWideArrowAtEnds",
    "Line1stWideArrowAtEndsFilled",
    "Line1stSquareAtEnd",
    "Line1stSquareAtEndFilled",
    "Line1stSquareAtEnds",
    "Line1stSquareAtEndsFilled",
    "Line1stDiamondAtEnd",
    "Line1stDiamondAtEndFilled",
    "Line1stDiamondAtEnds",
    "Line1stDiamondAtEndsFilled",
    "Line1stCircleAtEnd",
    "Line1stCircleAtEndFilled",
    "Line1stCircleAtEnds",
    "Line1stCircleAtEndsFilled",
    "Line1stTriangleAtEnd",
    "Line1stTriangleAtEndFilled",
    "Line1stTriangleAtEnds",
    "Line1stTriangleAtEndsFilled",
    "Line2nd",
    "Line2ndArrowAtEnd",
    "Line2ndArrowAtEndFilled",
    "Line2ndArrowAtEnds",
    "Line2ndArrowAtEndsFilled",
    "Line2ndWideArrowAtEnd",
    "Line2ndWideArrowAtEndFilled",
    "Line2ndWideArrowAtEnds",
    "Line2ndWideArrowAtEndsFilled",
    "Line2ndSquareAtEnd",
    "Line2ndSquareAtEndFilled",
    "Line2ndSquareAtEnds",
    "Line2ndSquareAtEndsFilled",
    "Line2ndDiamondAtEnd",
    "Line2ndDiamondAtEndFilled",
    "Line2ndDiamondAtEnds",
    "Line2ndDiamondAtEndsFilled",
    "Line2ndCircleAtEnd",
    "Line2ndCircleAtEndFilled",
    "Line2ndCircleAtEnds",
    "Line2ndCircleAtEndsFilled",
    "Line2ndTriangleAtEnd",
    "Line2ndTriangleAtEndFilled",
    "Line2ndTriangleAtEnds",
    "Line2ndTriangleAtEndsFilled",
    "Line3rd",
    "Line3rdArrowAtEnd",
    "Line3rdArrowAtEndFilled",
    "Line3rdArrowAtEnds",
    "Line3rdArrowAtEndsFilled",
    "Line3rdWideArrowAtEnd",
    "Line3rdWideArrowAtEndFilled",
    "Line3rdWideArrowAtEnds",
    "Line3rdWideArrowAtEndsFilled",
    "Line3rdSquareAtEnd",
    "Line3rdSquareAtEndFilled",
    "Line3rdSquareAtEnds",
    "Line3rdSquareAtEndsFilled",
    "Line3rdDiamondAtEnd",
    "Line3rdDiamondAtEndFilled",
    "Line3rdDiamondAtEnds",
    "Line3rdDiamondAtEndsFilled",
    "Line3rdCircleAtEnd",
    "Line3rdCircleAtEndFilled",
    "Line3rdCircleAtEnds",
    "Line3rdCircleAtEndsFilled",
    "Line3rdTriangleAtEnd",
    "Line3rdTriangleAtEndFilled",
    "Line3rdTriangleAtEnds",
    "Line3rdTriangleAtEndsFilled",
    "CrossLine1st2nd",
    "CrossLine1st2ndArrowAtEnd",
    "CrossLine1st2ndArrowAtEndFilled",
    "CrossLine1st2ndArrowAtEnds",
    "CrossLine1st2ndArrowAtEndsFilled",
    "CrossLine1st2ndWideArrowAtEnd",
    "CrossLine1st2ndWideArrowAtEndFilled",
    "CrossLine1st2ndWideArrowAtEnds",
    "CrossLine1st2ndWideArrowAtEndsFilled",
    "CrossLine1st2ndSquareAtEnd",
    "CrossLine1st2ndSquareAtEndFilled",
    "CrossLine1st2ndSquareAtEnds",
    "CrossLine1st2ndSquareAtEndsFilled",
    "CrossLine1st2ndDiamondAtEnd",
    "CrossLine1st2ndDiamondAtEndFilled",
    "CrossLine1st2ndDiamondAtEnds",
    "CrossLine1st2ndDiamondAtEndsFilled",
    "CrossLine1st2ndCircleAtEnd",
    "CrossLine1st2ndCircleAtEndFilled",
    "CrossLine1st2ndCircleAtEnds",
    "CrossLine1st2ndCircleAtEndsFilled",
    "CrossLine1st2ndTriangleAtEnd",
    "CrossLine1st2ndTriangleAtEndFilled",
    "CrossLine1st2ndTriangleAtEnds",
    "CrossLine1st2ndTriangleAtEndsFilled",
    "CrossLine1st3rd",
    "CrossLine1st3rdArrowAtEnd",
    "CrossLine1st3rdArrowAtEndFilled",
    "CrossLine1st3rdArrowAtEnds",
    "CrossLine1st3rdArrowAtEndsFilled",
    "CrossLine1st3rdWideArrowAtEnd",
    "CrossLine1st3rdWideArrowAtEndFilled",
    "CrossLine1st3rdWideArrowAtEnds",
    "CrossLine1st3rdWideArrowAtEndsFilled",
    "CrossLine1st3rdSquareAtEnd",
    "CrossLine1st3rdSquareAtEndFilled",
    "CrossLine1st3rdSquareAtEnds",
    "CrossLine1st3rdSquareAtEndsFilled",
    "CrossLine1st3rdDiamondAtEnd",
    "CrossLine1st3rdDiamondAtEndFilled",
    "CrossLine1st3rdDiamondAtEnds",
    "CrossLine1st3rdDiamondAtEndsFilled",
    "CrossLine1st3rdCircleAtEnd",
    "CrossLine1st3rdCircleAtEndFilled",
    "CrossLine1st3rdCircleAtEnds",
    "CrossLine1st3rdCircleAtEndsFilled",
    "CrossLine1st3rdTriangleAtEnd",
    "CrossLine1st3rdTriangleAtEndFilled",
    "CrossLine1st3rdTriangleAtEnds",
    "CrossLine1st3rdTriangleAtEndsFilled",
    "CrossLine2nd3rd",
    "CrossLine2nd3rdArrowAtEnd",
    "CrossLine2nd3rdArrowAtEndFilled",
    "CrossLine2nd3rdArrowAtEnds",
    "CrossLine2nd3rdArrowAtEndsFilled",
    "CrossLine2nd3rdWideArrowAtEnd",
    "CrossLine2nd3rdWideArrowAtEndFilled",
    "CrossLine2nd3rdWideArrowAtEnds",
    "CrossLine2nd3rdWideArrowAtEndsFilled",
    "CrossLine2nd3rdSquareAtEnd",
    "CrossLine2nd3rdSquareAtEndFilled",
    "CrossLine2nd3rdSquareAtEnds",
    "CrossLine2nd3rdSquareAtEndsFilled",
    "CrossLine2nd3rdDiamondAtEnd",
    "CrossLine2nd3rdDiamondAtEndFilled",
    "CrossLine2nd3rdDiamondAtEnds",
    "CrossLine2nd3rdDiamondAtEndsFilled",
    "CrossLine2nd3rdCircleAtEnd",
    "CrossLine2nd3rdCircleAtEndFilled",
    "CrossLine2nd3rdCircleAtEnds",
    "CrossLine2nd3rdCircleAtEndsFilled",
    "CrossLine2nd3rdTriangleAtEnd",
    "CrossLine2nd3rdTriangleAtEndFilled",
    "CrossLine2nd3rdTriangleAtEnds",
    "CrossLine2nd3rdTriangleAtEndsFilled",
    "CrossLine3Axis",
    "CrossLine3AxisEndCube",
    "CrossLine3AxisEndCubeFilled",
    "CrossLine3AxisEndOctahedron",
    "CrossLine3AxisEndOctahedronFilled",
    "CrossLine3AxisEndSphere",
    "CrossLine3AxisEndSphereFilled",
    "CrossLine3AxisEndPyramid",
    "CrossLine3AxisEndPyramidFilled",
    "CrossLine3AxisEndCone",
    "CrossLine3AxisEndConeFilled",
    "Triangle",
    "TriangleFilled",
    "TriangleArrow3D",
    "TriangleArrow3DFilled",
    "Square",
    "SquareFilled",
    "SquareArrow2D",
    "SquareArrow2DFilled",
    "SquareArrow3D",
    "SquareArrow3DFilled",
    "SquareArrowCrossLine2D",
    "SquareArrowCrossLine2DFilled",
    "SquareArrowCrossLine3D",
    "SquareArrowCrossLine3DFilled",
    "SquareArrowCrossLineTemplate2D",
    "SquareArrowCrossLineTemplate2DFilled",
    "SquareArrowCrossLineTemplate3D",
    "SquareArrowCrossLineTemplate3DFilled",
    "SquareArrow4Way2D",
    "SquareArrow4Way2DFilled",
    "SquareArrow4Way3D",
    "SquareArrow4Way3DFilled",
    "SquareTemplateArrow4Way2D",
    "SquareTemplateArrow4Way2DFilled",
    "SquareTemplateArrow4Way3D",
    "SquareTemplateArrow4Way3DFilled",
    "Diamond",
    "DiamondFilled",
    "Cube",
    "CubeFilled",
    "CubeArrow2D",
    "CubeArrow2DFilled",
    "CubeArrow3D",
    "CubeArrow3DFilled",
    "CubeFin",
    "CubeFinFilled",
    "CubeFinArrow",
    "CubeFinArrowFilled",
    "Octahedron",
    "OctahedronFilled",
    "OctahedronArrow",
    "OctahedronArrowFilled",
    "OctahedronArrowFin",
    "OctahedronArrowFinFilled",
    "Circle",
    "CircleFilled",
    "CircleArrow2D",
    "CircleArrow2DFilled",
    "CircleArrow3D",
    "CircleArrow3DFilled",
    "Semicircle",
    "SemicircleFilled",
    "SemicircleArrowAtEnd",
    "SemicircleArrowAtEndFilled",
    "SemicircleArrowAtEnds",
    "SemicircleArrowAtEndsFilled",
    "SemicircleWideArrowAtEnd",
    "SemicircleWideArrowAtEndFilled",
    "SemicircleWideArrowAtEnds",
    "SemicircleWideArrowAtEndsFilled",
    "SemicircleArrow2D",
    "SemicircleArrow2DFilled",
    "SemicircleArrow3D",
    "SemicircleArrow3DFilled",
    "Sphere",
    "SphereFilled",
    "SphereArrow2D",
    "SphereArrow2DFilled",
    "SphereArrow3D",
    "SphereArrow3DFilled",
    "Cylinder",
    "CylinderFilled",
    "CylinderFin",
    "CylinderFinFilled",
    "CylinderFinArrow",
    "CylinderFinArrowFilled",
    "Arrow",
    "ArrowFilled",
    "ArrowFin",
    "ArrowFinFilled",
    "Pyramid",
    "PyramidFilled",
    "PyramidFin",
    "PyramidFinFilled",
    "Cone",
    "ConeFilled",
    "ConeFin",
    "ConeFinFilled",
    "ColorCrossLine3Axis",
    "ColorCrossLine3AxisEndCube",
    "ColorCrossLine3AxisEndCubeFilled",
    "ColorCrossLine3AxisEndOctahedron",
    "ColorCrossLine3AxisEndOctahedronFilled",
    "ColorCrossLine3AxisEndSphere",
    "ColorCrossLine3AxisEndSphereFilled",
    "ColorCrossLine3AxisEndPyramid",
    "ColorCrossLine3AxisEndPyramidFilled",
    "ColorCrossLine3AxisEndCone",
    "ColorCrossLine3AxisEndConeFilled",
    "ColorCube",
    "ColorCubeFilled",
    "ColorCornerCube",
    "ColorCornerCubeFilled",
    "ColorSphere",
    "ColorSphereFilled",
    "ColorSphereArrow2D",
    "ColorSphereArrow2DFilled",
    "ColorSphereArrow3D",
    "ColorSphereArrow3DFilled",
    "ColorSphereCrossLine",
    "ColorSphereCrossLineFilled",
};

enum class PartEnds { Both, End };

struct PresetInfo {
    short outlineIndex;
    bool filled;
    PartEnds partEnds = PartEnds::Both;
    short partAxis = -1;
};

constexpr std::array<PresetInfo, 274> kPresetInfo = {{
    {0, false},  // Gear
    {0, true},  // GearFilled
    {1, false},  // Line1st
    {54, false, PartEnds::End},  // Line1stArrowAtEnd
    {54, true, PartEnds::End},  // Line1stArrowAtEndFilled
    {54, false},  // Line1stArrowAtEnds
    {54, true},  // Line1stArrowAtEndsFilled
    {62, false, PartEnds::End},  // Line1stWideArrowAtEnd
    {62, true, PartEnds::End},  // Line1stWideArrowAtEndFilled
    {62, false},  // Line1stWideArrowAtEnds
    {62, true},  // Line1stWideArrowAtEndsFilled
    {80, false, PartEnds::End},  // Line1stSquareAtEnd
    {80, true, PartEnds::End},  // Line1stSquareAtEndFilled
    {80, false},  // Line1stSquareAtEnds
    {80, true},  // Line1stSquareAtEndsFilled
    {81, false, PartEnds::End},  // Line1stDiamondAtEnd
    {81, true, PartEnds::End},  // Line1stDiamondAtEndFilled
    {81, false},  // Line1stDiamondAtEnds
    {81, true},  // Line1stDiamondAtEndsFilled
    {82, false, PartEnds::End},  // Line1stCircleAtEnd
    {82, true, PartEnds::End},  // Line1stCircleAtEndFilled
    {82, false},  // Line1stCircleAtEnds
    {82, true},  // Line1stCircleAtEndsFilled
    {83, false, PartEnds::End},  // Line1stTriangleAtEnd
    {83, true, PartEnds::End},  // Line1stTriangleAtEndFilled
    {83, false},  // Line1stTriangleAtEnds
    {83, true},  // Line1stTriangleAtEndsFilled
    {2, false},  // Line2nd
    {55, false, PartEnds::End},  // Line2ndArrowAtEnd
    {55, true, PartEnds::End},  // Line2ndArrowAtEndFilled
    {55, false},  // Line2ndArrowAtEnds
    {55, true},  // Line2ndArrowAtEndsFilled
    {63, false, PartEnds::End},  // Line2ndWideArrowAtEnd
    {63, true, PartEnds::End},  // Line2ndWideArrowAtEndFilled
    {63, false},  // Line2ndWideArrowAtEnds
    {63, true},  // Line2ndWideArrowAtEndsFilled
    {84, false, PartEnds::End},  // Line2ndSquareAtEnd
    {84, true, PartEnds::End},  // Line2ndSquareAtEndFilled
    {84, false},  // Line2ndSquareAtEnds
    {84, true},  // Line2ndSquareAtEndsFilled
    {85, false, PartEnds::End},  // Line2ndDiamondAtEnd
    {85, true, PartEnds::End},  // Line2ndDiamondAtEndFilled
    {85, false},  // Line2ndDiamondAtEnds
    {85, true},  // Line2ndDiamondAtEndsFilled
    {86, false, PartEnds::End},  // Line2ndCircleAtEnd
    {86, true, PartEnds::End},  // Line2ndCircleAtEndFilled
    {86, false},  // Line2ndCircleAtEnds
    {86, true},  // Line2ndCircleAtEndsFilled
    {87, false, PartEnds::End},  // Line2ndTriangleAtEnd
    {87, true, PartEnds::End},  // Line2ndTriangleAtEndFilled
    {87, false},  // Line2ndTriangleAtEnds
    {87, true},  // Line2ndTriangleAtEndsFilled
    {3, false},  // Line3rd
    {56, false, PartEnds::End},  // Line3rdArrowAtEnd
    {56, true, PartEnds::End},  // Line3rdArrowAtEndFilled
    {56, false},  // Line3rdArrowAtEnds
    {56, true},  // Line3rdArrowAtEndsFilled
    {64, false, PartEnds::End},  // Line3rdWideArrowAtEnd
    {64, true, PartEnds::End},  // Line3rdWideArrowAtEndFilled
    {64, false},  // Line3rdWideArrowAtEnds
    {64, true},  // Line3rdWideArrowAtEndsFilled
    {88, false, PartEnds::End},  // Line3rdSquareAtEnd
    {88, true, PartEnds::End},  // Line3rdSquareAtEndFilled
    {88, false},  // Line3rdSquareAtEnds
    {88, true},  // Line3rdSquareAtEndsFilled
    {89, false, PartEnds::End},  // Line3rdDiamondAtEnd
    {89, true, PartEnds::End},  // Line3rdDiamondAtEndFilled
    {89, false},  // Line3rdDiamondAtEnds
    {89, true},  // Line3rdDiamondAtEndsFilled
    {90, false, PartEnds::End},  // Line3rdCircleAtEnd
    {90, true, PartEnds::End},  // Line3rdCircleAtEndFilled
    {90, false},  // Line3rdCircleAtEnds
    {90, true},  // Line3rdCircleAtEndsFilled
    {91, false, PartEnds::End},  // Line3rdTriangleAtEnd
    {91, true, PartEnds::End},  // Line3rdTriangleAtEndFilled
    {91, false},  // Line3rdTriangleAtEnds
    {91, true},  // Line3rdTriangleAtEndsFilled
    {52, false},  // CrossLine1st2nd
    {57, false, PartEnds::End, 0},  // CrossLine1st2ndArrowAtEnd
    {57, true, PartEnds::End, 0},  // CrossLine1st2ndArrowAtEndFilled
    {57, false},  // CrossLine1st2ndArrowAtEnds
    {57, true},  // CrossLine1st2ndArrowAtEndsFilled
    {65, false, PartEnds::End, 0},  // CrossLine1st2ndWideArrowAtEnd
    {65, true, PartEnds::End, 0},  // CrossLine1st2ndWideArrowAtEndFilled
    {65, false},  // CrossLine1st2ndWideArrowAtEnds
    {65, true},  // CrossLine1st2ndWideArrowAtEndsFilled
    {92, false, PartEnds::End, 0},  // CrossLine1st2ndSquareAtEnd
    {92, true, PartEnds::End, 0},  // CrossLine1st2ndSquareAtEndFilled
    {92, false},  // CrossLine1st2ndSquareAtEnds
    {92, true},  // CrossLine1st2ndSquareAtEndsFilled
    {93, false, PartEnds::End, 0},  // CrossLine1st2ndDiamondAtEnd
    {93, true, PartEnds::End, 0},  // CrossLine1st2ndDiamondAtEndFilled
    {93, false},  // CrossLine1st2ndDiamondAtEnds
    {93, true},  // CrossLine1st2ndDiamondAtEndsFilled
    {94, false, PartEnds::End, 0},  // CrossLine1st2ndCircleAtEnd
    {94, true, PartEnds::End, 0},  // CrossLine1st2ndCircleAtEndFilled
    {94, false},  // CrossLine1st2ndCircleAtEnds
    {94, true},  // CrossLine1st2ndCircleAtEndsFilled
    {95, false, PartEnds::End, 0},  // CrossLine1st2ndTriangleAtEnd
    {95, true, PartEnds::End, 0},  // CrossLine1st2ndTriangleAtEndFilled
    {95, false},  // CrossLine1st2ndTriangleAtEnds
    {95, true},  // CrossLine1st2ndTriangleAtEndsFilled
    {53, false},  // CrossLine1st3rd
    {58, false, PartEnds::End, 0},  // CrossLine1st3rdArrowAtEnd
    {58, true, PartEnds::End, 0},  // CrossLine1st3rdArrowAtEndFilled
    {58, false},  // CrossLine1st3rdArrowAtEnds
    {58, true},  // CrossLine1st3rdArrowAtEndsFilled
    {66, false, PartEnds::End, 0},  // CrossLine1st3rdWideArrowAtEnd
    {66, true, PartEnds::End, 0},  // CrossLine1st3rdWideArrowAtEndFilled
    {66, false},  // CrossLine1st3rdWideArrowAtEnds
    {66, true},  // CrossLine1st3rdWideArrowAtEndsFilled
    {96, false, PartEnds::End, 0},  // CrossLine1st3rdSquareAtEnd
    {96, true, PartEnds::End, 0},  // CrossLine1st3rdSquareAtEndFilled
    {96, false},  // CrossLine1st3rdSquareAtEnds
    {96, true},  // CrossLine1st3rdSquareAtEndsFilled
    {97, false, PartEnds::End, 0},  // CrossLine1st3rdDiamondAtEnd
    {97, true, PartEnds::End, 0},  // CrossLine1st3rdDiamondAtEndFilled
    {97, false},  // CrossLine1st3rdDiamondAtEnds
    {97, true},  // CrossLine1st3rdDiamondAtEndsFilled
    {98, false, PartEnds::End, 0},  // CrossLine1st3rdCircleAtEnd
    {98, true, PartEnds::End, 0},  // CrossLine1st3rdCircleAtEndFilled
    {98, false},  // CrossLine1st3rdCircleAtEnds
    {98, true},  // CrossLine1st3rdCircleAtEndsFilled
    {99, false, PartEnds::End, 0},  // CrossLine1st3rdTriangleAtEnd
    {99, true, PartEnds::End, 0},  // CrossLine1st3rdTriangleAtEndFilled
    {99, false},  // CrossLine1st3rdTriangleAtEnds
    {99, true},  // CrossLine1st3rdTriangleAtEndsFilled
    {4, false},  // CrossLine2nd3rd
    {59, false, PartEnds::End, 1},  // CrossLine2nd3rdArrowAtEnd
    {59, true, PartEnds::End, 1},  // CrossLine2nd3rdArrowAtEndFilled
    {59, false},  // CrossLine2nd3rdArrowAtEnds
    {59, true},  // CrossLine2nd3rdArrowAtEndsFilled
    {67, false, PartEnds::End, 1},  // CrossLine2nd3rdWideArrowAtEnd
    {67, true, PartEnds::End, 1},  // CrossLine2nd3rdWideArrowAtEndFilled
    {67, false},  // CrossLine2nd3rdWideArrowAtEnds
    {67, true},  // CrossLine2nd3rdWideArrowAtEndsFilled
    {100, false, PartEnds::End, 1},  // CrossLine2nd3rdSquareAtEnd
    {100, true, PartEnds::End, 1},  // CrossLine2nd3rdSquareAtEndFilled
    {100, false},  // CrossLine2nd3rdSquareAtEnds
    {100, true},  // CrossLine2nd3rdSquareAtEndsFilled
    {101, false, PartEnds::End, 1},  // CrossLine2nd3rdDiamondAtEnd
    {101, true, PartEnds::End, 1},  // CrossLine2nd3rdDiamondAtEndFilled
    {101, false},  // CrossLine2nd3rdDiamondAtEnds
    {101, true},  // CrossLine2nd3rdDiamondAtEndsFilled
    {102, false, PartEnds::End, 1},  // CrossLine2nd3rdCircleAtEnd
    {102, true, PartEnds::End, 1},  // CrossLine2nd3rdCircleAtEndFilled
    {102, false},  // CrossLine2nd3rdCircleAtEnds
    {102, true},  // CrossLine2nd3rdCircleAtEndsFilled
    {103, false, PartEnds::End, 1},  // CrossLine2nd3rdTriangleAtEnd
    {103, true, PartEnds::End, 1},  // CrossLine2nd3rdTriangleAtEndFilled
    {103, false},  // CrossLine2nd3rdTriangleAtEnds
    {103, true},  // CrossLine2nd3rdTriangleAtEndsFilled
    {5, false},  // CrossLine3Axis
    {69, false},  // CrossLine3AxisEndCube
    {69, true},  // CrossLine3AxisEndCubeFilled
    {70, false},  // CrossLine3AxisEndOctahedron
    {70, true},  // CrossLine3AxisEndOctahedronFilled
    {71, false},  // CrossLine3AxisEndSphere
    {71, true},  // CrossLine3AxisEndSphereFilled
    {72, false},  // CrossLine3AxisEndPyramid
    {72, true},  // CrossLine3AxisEndPyramidFilled
    {73, false},  // CrossLine3AxisEndCone
    {73, true},  // CrossLine3AxisEndConeFilled
    {6, false},  // Triangle
    {6, true},  // TriangleFilled
    {7, false},  // TriangleArrow3D
    {7, true},  // TriangleArrow3DFilled
    {8, false},  // Square
    {8, true},  // SquareFilled
    {9, false},  // SquareArrow2D
    {9, true},  // SquareArrow2DFilled
    {10, false},  // SquareArrow3D
    {10, true},  // SquareArrow3DFilled
    {11, false},  // SquareArrowCrossLine2D
    {11, true},  // SquareArrowCrossLine2DFilled
    {12, false},  // SquareArrowCrossLine3D
    {12, true},  // SquareArrowCrossLine3DFilled
    {13, false},  // SquareArrowCrossLineTemplate2D
    {13, true},  // SquareArrowCrossLineTemplate2DFilled
    {14, false},  // SquareArrowCrossLineTemplate3D
    {14, true},  // SquareArrowCrossLineTemplate3DFilled
    {15, false},  // SquareArrow4Way2D
    {15, true},  // SquareArrow4Way2DFilled
    {16, false},  // SquareArrow4Way3D
    {16, true},  // SquareArrow4Way3DFilled
    {17, false},  // SquareTemplateArrow4Way2D
    {17, true},  // SquareTemplateArrow4Way2DFilled
    {18, false},  // SquareTemplateArrow4Way3D
    {18, true},  // SquareTemplateArrow4Way3DFilled
    {79, false},  // Diamond
    {79, true},  // DiamondFilled
    {19, false},  // Cube
    {19, true},  // CubeFilled
    {20, false},  // CubeArrow2D
    {20, true},  // CubeArrow2DFilled
    {21, false},  // CubeArrow3D
    {21, true},  // CubeArrow3DFilled
    {22, false},  // CubeFin
    {22, true},  // CubeFinFilled
    {23, false},  // CubeFinArrow
    {23, true},  // CubeFinArrowFilled
    {24, false},  // Octahedron
    {24, true},  // OctahedronFilled
    {25, false},  // OctahedronArrow
    {25, true},  // OctahedronArrowFilled
    {26, false},  // OctahedronArrowFin
    {26, true},  // OctahedronArrowFinFilled
    {27, false},  // Circle
    {27, true},  // CircleFilled
    {28, false},  // CircleArrow2D
    {28, true},  // CircleArrow2DFilled
    {29, false},  // CircleArrow3D
    {29, true},  // CircleArrow3DFilled
    {30, false},  // Semicircle
    {30, true},  // SemicircleFilled
    {61, false, PartEnds::End},  // SemicircleArrowAtEnd
    {61, true, PartEnds::End},  // SemicircleArrowAtEndFilled
    {61, false},  // SemicircleArrowAtEnds
    {61, true},  // SemicircleArrowAtEndsFilled
    {68, false, PartEnds::End},  // SemicircleWideArrowAtEnd
    {68, true, PartEnds::End},  // SemicircleWideArrowAtEndFilled
    {68, false},  // SemicircleWideArrowAtEnds
    {68, true},  // SemicircleWideArrowAtEndsFilled
    {31, false},  // SemicircleArrow2D
    {31, true},  // SemicircleArrow2DFilled
    {32, false},  // SemicircleArrow3D
    {32, true},  // SemicircleArrow3DFilled
    {33, false},  // Sphere
    {33, true},  // SphereFilled
    {34, false},  // SphereArrow2D
    {34, true},  // SphereArrow2DFilled
    {35, false},  // SphereArrow3D
    {35, true},  // SphereArrow3DFilled
    {36, false},  // Cylinder
    {36, true},  // CylinderFilled
    {37, false},  // CylinderFin
    {37, true},  // CylinderFinFilled
    {38, false},  // CylinderFinArrow
    {38, true},  // CylinderFinArrowFilled
    {39, false},  // Arrow
    {39, true},  // ArrowFilled
    {40, false},  // ArrowFin
    {40, true},  // ArrowFinFilled
    {41, false},  // Pyramid
    {41, true},  // PyramidFilled
    {42, false},  // PyramidFin
    {42, true},  // PyramidFinFilled
    {43, false},  // Cone
    {43, true},  // ConeFilled
    {44, false},  // ConeFin
    {44, true},  // ConeFinFilled
    {45, false},  // ColorCrossLine3Axis
    {74, false},  // ColorCrossLine3AxisEndCube
    {74, true},  // ColorCrossLine3AxisEndCubeFilled
    {75, false},  // ColorCrossLine3AxisEndOctahedron
    {75, true},  // ColorCrossLine3AxisEndOctahedronFilled
    {76, false},  // ColorCrossLine3AxisEndSphere
    {76, true},  // ColorCrossLine3AxisEndSphereFilled
    {77, false},  // ColorCrossLine3AxisEndPyramid
    {77, true},  // ColorCrossLine3AxisEndPyramidFilled
    {78, false},  // ColorCrossLine3AxisEndCone
    {78, true},  // ColorCrossLine3AxisEndConeFilled
    {50, false},  // ColorCube
    {50, true},  // ColorCubeFilled
    {51, false},  // ColorCornerCube
    {51, true},  // ColorCornerCubeFilled
    {46, false},  // ColorSphere
    {46, true},  // ColorSphereFilled
    {48, false},  // ColorSphereArrow2D
    {48, true},  // ColorSphereArrow2DFilled
    {49, false},  // ColorSphereArrow3D
    {49, true},  // ColorSphereArrow3DFilled
    {47, false},  // ColorSphereCrossLine
    {47, true},  // ColorSphereCrossLineFilled
}};

constexpr short cubePresetIndex() {
    for (short index = 0; index < static_cast<short>(kPresetInfo.size()); ++index) {
        if (kPresetInfo[index].outlineIndex == 19 && !kPresetInfo[index].filled) {
            return index;
        }
    }
    return 0;
}

short outlinePresetIndex(short shape) {
    return shape >= 0 && shape < static_cast<short>(kPresetInfo.size())
        ? kPresetInfo[shape].outlineIndex : 0;
}

bool isFilledPreset(short shape) {
    return shape >= 0 && shape < static_cast<short>(kPresetInfo.size())
        && kPresetInfo[shape].filled;
}

short presetPartAxis(short shape) {
    return shape >= 0 && shape < static_cast<short>(kPresetInfo.size())
        ? kPresetInfo[shape].partAxis : -1;
}

bool hasPartAtEnd(short shape, bool start, short axis = -1) {
    if (shape < 0 || shape >= static_cast<short>(kPresetInfo.size())) return true;
    const auto& info = kPresetInfo[shape];
    if (axis >= 0 && info.partAxis >= 0 && axis != info.partAxis) return false;
    return info.partEnds == PartEnds::Both || !start;
}

constexpr std::array<RawPoint, 2> kPrimitive2 = {{
    {0, 0, 0.5},
    {0, 0, -0.5},
}};

constexpr std::array<RawPoint, 5> kPrimitive3 = {{
    {0.5, 0, 0},
    {-0.5, 0, 0},
    {0, 0, 0},
    {0, 0.5, 0},
    {0, -0.5, 0},
}};

constexpr std::array<RawPoint, 9> kPrimitive4 = {{
    {0, 0, 0},
    {0, 0, 0.5},
    {0, 0, -0.5},
    {0, 0, 0},
    {0.5, 0, 0},
    {-0.5, 0, 0},
    {0, 0, 0},
    {0, 0.5, 0},
    {0, -0.5, 0},
}};

constexpr std::array<RawPoint, 4> kPrimitive5 = {{
    {0, 0.5, 0},
    {0.5, -0.37, 0},
    {-0.5, -0.37, 0},
    {0, 0.5, 0},
}};

constexpr std::array<RawPoint, 6> kPrimitive6 = {{
    {0, 0.5, 0},
    {0.5, -0.37, 0},
    {-0.5, -0.37, 0},
    {0, 0.5, 0},
    {0, -0.37, 0.5},
    {0, -0.37, 0},
}};

constexpr std::array<RawPoint, 5> kPrimitive7 = {{
    {0.5, 0.5, 0},
    {-0.5, 0.5, 0},
    {-0.5, -0.5, 0},
    {0.5, -0.5, 0},
    {0.5, 0.5, 0},
}};

constexpr std::array<RawPoint, 8> kPrimitive8 = {{
    {0, 0.625, 0},
    {-0.072, 0.5, 0},
    {-0.5, 0.5, 0},
    {-0.5, -0.5, 0},
    {0.5, -0.5, 0},
    {0.5, 0.5, 0},
    {0.072, 0.5, 0},
    {0, 0.625, 0},
}};

constexpr std::array<RawPoint, 10> kPrimitive9 = {{
    {0, 0.625, 0},
    {-0.072, 0.5, 0},
    {-0.5, 0.5, 0},
    {-0.5, -0.5, 0},
    {0.5, -0.5, 0},
    {0.5, 0.5, 0},
    {0.072, 0.5, 0},
    {0, 0.625, 0},
    {0, 0.5, 0.0625},
    {0, 0.5, 0},
}};

constexpr std::array<RawPoint, 12> kPrimitive10 = {{
    {0, 0.625, 0},
    {-0.072, 0.5, 0},
    {-0.5, 0.5, 0},
    {-0.5, -0.5, 0},
    {0.5, -0.5, 0},
    {0.5, 0.5, 0},
    {0.072, 0.5, 0},
    {0, 0.625, 0},
    {0, -0.5, 0},
    {0, 0, 0},
    {0.5, 0, 0},
    {-0.5, 0, 0},
}};

constexpr std::array<RawPoint, 15> kPrimitive11 = {{
    {0, 0.625, 0},
    {-0.072, 0.5, 0},
    {-0.5, 0.5, 0},
    {-0.5, -0.5, 0},
    {0.5, -0.5, 0},
    {0.5, 0.5, 0},
    {0.072, 0.5, 0},
    {0, 0.625, 0},
    {0, 0.5, 0.0625},
    {0, 0.5, 0},
    {0, 0.625, 0},
    {0, -0.5, 0},
    {0, 0, 0},
    {0.5, 0, 0},
    {-0.5, 0, 0},
}};

constexpr std::array<RawPoint, 5> kPrimitive12 = {{
    {0, 0.625, 0},
    {0, -0.5, 0},
    {0, 0, 0},
    {0.5, 0, 0},
    {-0.5, 0, 0},
}};

constexpr std::array<RawPoint, 17> kPrimitive13 = {{
    {0.5, 0.5, 0},
    {0.072, 0.5, 0},
    {0, 0.625, 0},
    {-0.072, 0.5, 0},
    {-0.5, 0.5, 0},
    {-0.5, 0.036, 0},
    {-0.5625, 0, 0},
    {-0.5, -0.036, 0},
    {-0.5, -0.5, 0},
    {-0.036, -0.5, 0},
    {0, -0.5625, 0},
    {0.036, -0.5, 0},
    {0.5, -0.5, 0},
    {0.5, -0.036, 0},
    {0.5625, 0, 0},
    {0.5, 0.036, 0},
    {0.5, 0.5, 0},
}};

constexpr std::array<RawPoint, 33> kPrimitive14 = {{
    {0.5, 0.5, 0},
    {0.072, 0.5, 0},
    {0, 0.625, 0},
    {0, 0.5, 0.0625},
    {0, 0.5, 0},
    {0, 0.5, 0.0625},
    {0, 0.625, 0},
    {-0.072, 0.5, 0},
    {-0.5, 0.5, 0},
    {-0.5, 0.036, 0},
    {-0.5625, 0, 0},
    {-0.5, 0, 0.03125},
    {-0.5, 0, 0},
    {-0.5, 0, 0.03125},
    {-0.5625, 0, 0},
    {-0.5, -0.036, 0},
    {-0.5, -0.5, 0},
    {-0.036, -0.5, 0},
    {0, -0.5625, 0},
    {0, -0.5, 0.03125},
    {0, -0.5, 0},
    {0, -0.5, 0.03125},
    {0, -0.5625, 0},
    {0.036, -0.5, 0},
    {0.5, -0.5, 0},
    {0.5, -0.036, 0},
    {0.5625, 0, 0},
    {0.5, 0, 0.03125},
    {0.5, 0, 0},
    {0.5, 0, 0.03125},
    {0.5625, 0, 0},
    {0.5, 0.036, 0},
    {0.5, 0.5, 0},
}};

constexpr std::array<RawPoint, 3> kPrimitive15 = {{
    {0.5, 0.15, 0},
    {0.5, 0.5, 0},
    {0.15, 0.5, 0},
}};

constexpr std::array<RawPoint, 5> kPrimitive16 = {{
    {0.15, 0.5, 0},
    {0.072, 0.5, 0},
    {0, 0.625, 0},
    {-0.072, 0.5, 0},
    {-0.15, 0.5, 0},
}};

constexpr std::array<RawPoint, 5> kPrimitive17 = {{
    {0.15, 0.5, 0},
    {0.036, 0.5, 0},
    {0, 0.5625, 0},
    {-0.036, 0.5, 0},
    {-0.15, 0.5, 0},
}};

constexpr std::array<RawPoint, 9> kPrimitive18 = {{
    {0.15, 0.5, 0},
    {0.072, 0.5, 0},
    {0, 0.625, 0},
    {0, 0.5, 0.0625},
    {0, 0.5, 0},
    {0, 0.5, 0.0625},
    {0, 0.625, 0},
    {-0.072, 0.5, 0},
    {-0.15, 0.5, 0},
}};

constexpr std::array<RawPoint, 9> kPrimitive19 = {{
    {0.15, 0.5, 0},
    {0.036, 0.5, 0},
    {0, 0.5625, 0},
    {0, 0.5, 0.03125},
    {0, 0.5, 0},
    {0, 0.5, 0.03125},
    {0, 0.5625, 0},
    {-0.036, 0.5, 0},
    {-0.15, 0.5, 0},
}};

constexpr std::array<RawPoint, 17> kPrimitive20 = {{
    {0.5, 0.5, 0.5},
    {-0.5, 0.5, 0.5},
    {-0.5, -0.5, 0.5},
    {0.5, -0.5, 0.5},
    {0.5, 0.5, 0.5},
    {0.5, 0.5, -0.5},
    {0.5, -0.5, -0.5},
    {0.5, -0.5, 0.5},
    {0.5, 0.5, 0.5},
    {-0.5, 0.5, 0.5},
    {-0.5, 0.5, -0.5},
    {-0.5, -0.5, -0.5},
    {-0.5, -0.5, 0.5},
    {-0.5, -0.5, -0.5},
    {0.5, -0.5, -0.5},
    {0.5, 0.5, -0.5},
    {-0.5, 0.5, -0.5},
}};

constexpr std::array<RawPoint, 5> kPrimitive21 = {{
    {0.15, 0, 0.5},
    {0.072, 0, 0.5},
    {0, 0, 0.625},
    {-0.072, 0, 0.5},
    {-0.15, 0, 0.5},
}};

constexpr std::array<RawPoint, 9> kPrimitive22 = {{
    {0.15, 0, 0.5},
    {0.072, 0, 0.5},
    {0, 0, 0.625},
    {0, 0.0625, 0.5},
    {0, 0, 0.5},
    {0, 0.0625, 0.5},
    {0, 0, 0.625},
    {-0.072, 0, 0.5},
    {-0.15, 0, 0.5},
}};

constexpr std::array<RawPoint, 21> kPrimitive23 = {{
    {0.5, 0.5, 0.5},
    {-0.5, 0.5, 0.5},
    {-0.5, -0.5, 0.5},
    {0.5, -0.5, 0.5},
    {0.5, 0.5, 0.5},
    {0.5, 0.5, -0.5},
    {0.5, -0.5, -0.5},
    {0.5, -0.5, 0.5},
    {0.5, 0.5, 0.5},
    {-0.5, 0.5, 0.5},
    {-0.5, 0.5, -0.5},
    {-0.5, -0.5, -0.5},
    {-0.5, -0.5, 0.5},
    {-0.5, -0.5, -0.5},
    {0.5, -0.5, -0.5},
    {0.5, 0.5, -0.5},
    {-0.5, 0.5, -0.5},
    {0, 0.5, -0.5},
    {0, 1, -0.5},
    {0, 1, 0.5},
    {0, 0.5, 0.5},
}};

constexpr std::array<RawPoint, 16> kPrimitive24 = {{
    {0, 0, 0.5},
    {0.5, 0, 0},
    {0, 0.5, 0},
    {0, 0, 0.5},
    {-0.5, 0, 0},
    {0, 0.5, 0},
    {0, 0, -0.5},
    {0.5, 0, 0},
    {0, 0.5, 0},
    {-0.5, 0, 0},
    {0, 0, -0.5},
    {0, -0.5, 0},
    {0, 0, 0.5},
    {0.5, 0, 0},
    {0, -0.5, 0},
    {-0.5, 0, 0},
}};

constexpr std::array<RawPoint, 16> kPrimitive25 = {{
    {0, 0, 1.5},
    {0.5, 0, 0},
    {0, 0.5, 0},
    {0, 0, 1.5},
    {-0.5, 0, 0},
    {0, 0.5, 0},
    {0, 0, -0.5},
    {0.5, 0, 0},
    {0, 0.5, 0},
    {-0.5, 0, 0},
    {0, 0, -0.5},
    {0, -0.5, 0},
    {0, 0, 1.5},
    {0.5, 0, 0},
    {0, -0.5, 0},
    {-0.5, 0, 0},
}};

constexpr std::array<RawPoint, 4> kPrimitive26 = {{
    {0, 0, 1.5},
    {0, 0.5, 1.5},
    {0, 0.5, -0.5},
    {0, 0, -0.5},
}};

constexpr std::array<RawPoint, 3> kPrimitive27 = {{
    {0.075, 0.495096189432, 0},
    {0, 0.625, 0},
    {-0.075, 0.495096189432, 0},
}};

constexpr std::array<RawPoint, 7> kPrimitive28 = {{
    {0.075, 0.495096189432, 0},
    {0, 0.625, 0},
    {0, 0.5, 0.0625},
    {0, 0.5, 0},
    {0, 0.5, 0.0625},
    {0, 0.625, 0},
    {-0.075, 0.495096189432, 0},
}};

constexpr std::array<RawPoint, 3> kPrimitive30 = {{
    {0.075, 0, 0.495096189432},
    {0, 0, 0.625},
    {-0.075, 0, 0.495096189432},
}};

constexpr std::array<RawPoint, 7> kPrimitive31 = {{
    {0.075, 0, 0.495096189432},
    {0, 0, 0.625},
    {0, 0.0625, 0.5},
    {0, 0, 0.5},
    {0, 0.0625, 0.5},
    {0, 0, 0.625},
    {-0.075, 0, 0.495096189432},
}};

constexpr std::array<RawPoint, 4> kPrimitive32 = {{
    {0, 0.5, 0.5},
    {0, 1, 0.5},
    {0, 1, -0.5},
    {0, 0.5, -0.5},
}};

constexpr std::array<RawPoint, 7> kPrimitive33 = {{
    {0, 0, 0.5},
    {0.5, 0, -0.25},
    {0.25, 0, -0.5},
    {0, 0, -0.25},
    {-0.25, 0, -0.5},
    {-0.5, 0, -0.25},
    {0, 0, 0.5},
}};

constexpr std::array<RawPoint, 10> kPrimitive34 = {{
    {0, 0, 0.5},
    {0.5, 0, -0.25},
    {0.25, 0, -0.5},
    {0, 0, -0.25},
    {-0.25, 0, -0.5},
    {-0.5, 0, -0.25},
    {0, 0, 0.5},
    {0, 0.5, -0.25},
    {0, 0.25, -0.5},
    {0, 0, -0.25},
}};

constexpr std::array<RawPoint, 13> kPrimitive35 = {{
    {0, 0, 0.5},
    {0.5, 0.5, -0.5},
    {-0.5, 0.5, -0.5},
    {0, 0, 0.5},
    {0.5, 0.5, -0.5},
    {0.5, -0.5, -0.5},
    {0, 0, 0.5},
    {-0.5, 0.5, -0.5},
    {-0.5, -0.5, -0.5},
    {0, 0, 0.5},
    {0.5, -0.5, -0.5},
    {-0.5, -0.5, -0.5},
    {0, 0, 0.5},
}};

constexpr std::array<RawPoint, 15> kPrimitive36 = {{
    {0, 0, 0.5},
    {0.5, 0.5, -0.5},
    {-0.5, 0.5, -0.5},
    {0, 0, 0.5},
    {0.5, 0.5, -0.5},
    {0.5, -0.5, -0.5},
    {0, 0, 0.5},
    {-0.5, 0.5, -0.5},
    {-0.5, -0.5, -0.5},
    {0, 0, 0.5},
    {0.5, -0.5, -0.5},
    {-0.5, -0.5, -0.5},
    {0, 0, 0.5},
    {0, 0.5, 0.5},
    {0, 0.5, -0.5},
}};

constexpr std::array<RawPoint, 8> kPrimitive37 = {{
    {0, 0, 0.5},
    {0, 0.5, -0.5},
    {0, 0, 0.5},
    {0, -0.5, -0.5},
    {0, 0, 0.5},
    {0.5, 0, -0.5},
    {0, 0, 0.5},
    {-0.5, 0, -0.5},
}};

constexpr std::array<RawPoint, 11> kPrimitive38 = {{
    {0, 0, 0.5},
    {0, 0.5, -0.5},
    {0, 0, 0.5},
    {0, -0.5, -0.5},
    {0, 0, 0.5},
    {0.5, 0, -0.5},
    {0, 0, 0.5},
    {-0.5, 0, -0.5},
    {0, 0, 0.5},
    {0, 0.5, 0.5},
    {0, 0.5, -0.5},
}};

constexpr std::array<RawPoint, 2> kPrimitive39 = {{
    {0, 0, 0},
    {0, 0, 0.5},
}};

constexpr std::array<RawPoint, 2> kPrimitive40 = {{
    {0, 0, 0},
    {0, 0.5, 0},
}};

constexpr std::array<RawPoint, 2> kPrimitive41 = {{
    {0, 0, 0},
    {-0.5, 0, 0},
}};

constexpr std::array<RawPoint, 2> kPrimitive42 = {{
    {0, 0, 0},
    {0, 0, -0.5},
}};

constexpr std::array<RawPoint, 2> kPrimitive43 = {{
    {0, 0, 0},
    {0, -0.5, 0},
}};

constexpr std::array<RawPoint, 2> kPrimitive44 = {{
    {0, 0, 0},
    {0.5, 0, 0},
}};

constexpr std::array<RawPoint, 2> kPrimitive45 = {{
    {0, 0.5, 0},
    {0, -0.5, 0},
}};

constexpr std::array<RawPoint, 2> kPrimitive46 = {{
    {-0.5, 0, 0},
    {0.5, 0, 0},
}};

constexpr std::array<RawPoint, 3> kPrimitive47 = {{
    {0, 0.5, -0.5},
    {0, 1, -0.5},
    {0, 0.5, 0.5},
}};

constexpr double kColorCubeInset = 0.005;
constexpr double kCornerSquareMin = 0.3;
constexpr std::array<StrokeStyle, 3> kAxisStyles = {
    StrokeStyle::AxisX, StrokeStyle::AxisY, StrokeStyle::AxisZ,
};

MPoint cubeFacePoint(unsigned int axis, double position, double u, double v) {
    switch (axis) {
        case 0: return MPoint(position, u, v);
        case 1: return MPoint(v, position, u);
        default: return MPoint(u, v, position);
    }
}

void appendNativeStroke(
    const std::vector<MPoint>& points, StrokeStyle style,
    const ShapeTransform& transform, Strokes& strokes,
    std::vector<StrokeStyle>& styles
) {
    Stroke stroke;
    for (const MPoint& point : points) {
        stroke.append(transformPoint(point, transform));
    }
    strokes.push_back(std::move(stroke));
    styles.push_back(style);
}

void appendColorCubeGeometry(
    bool corner, const ShapeTransform& transform, Strokes& strokes,
    std::vector<StrokeStyle>& styles
) {
    for (unsigned int axis = 0; axis < 3; ++axis) {
        if (corner) {
            for (double u : {-0.5, 0.5}) {
                for (double v : {-0.5, 0.5}) {
                    // Stop the three corner edges at the marker boundary.
                    const double end = u == 0.5 && v == 0.5
                        ? kCornerSquareMin : 0.5;
                    appendNativeStroke({
                        cubeFacePoint(axis, -0.5, u, v),
                        cubeFacePoint(axis, end, u, v),
                    }, StrokeStyle::Normal, transform, strokes, styles);
                }
            }
        } else {
            const double low = -0.5 + kColorCubeInset;
            const double high = 0.5 - kColorCubeInset;
            appendNativeStroke({
                cubeFacePoint(axis, 0.5, low, low),
                cubeFacePoint(axis, 0.5, high, low),
                cubeFacePoint(axis, 0.5, high, high),
                cubeFacePoint(axis, 0.5, low, high),
                cubeFacePoint(axis, 0.5, low, low),
            }, kAxisStyles[axis], transform, strokes, styles);
            appendNativeStroke({
                MPoint(-0.5, -0.5, -0.5),
                cubeFacePoint(axis, 0.5, -0.5, -0.5),
            }, StrokeStyle::Normal, transform, strokes, styles);
        }
    }
}

short endArrowBaseOutline(short outline) {
    constexpr std::array<short, 6> straightBases = {1, 2, 3, 52, 53, 4};
    if (outline >= 54 && outline <= 59) return straightBases[outline - 54];
    if (outline == 61) return 30;
    return outline;
}

std::vector<unsigned int> straightLineAxes(short outline) {
    switch (outline) {
        case 1: return {0};
        case 2: return {1};
        case 3: return {2};
        case 52: return {0, 1};
        case 53: return {0, 2};
        case 4: return {1, 2};
        default: return {};
    }
}

MVector nativeAxis(unsigned int axis) {
    switch (axis) {
        case 0: return MVector(1.0, 0.0, 0.0);
        case 1: return MVector(0.0, 1.0, 0.0);
        default: return MVector(0.0, 0.0, 1.0);
    }
}

using ArrowHead = std::array<MPoint, 3>;

std::vector<ArrowHead> endArrowHeads(short outline, const ShapeSettings& settings) {
    std::vector<ArrowHead> heads;
    const double depth = 0.1 * std::cos(kPi / 6.0) * settings.partLengthScale * settings.partSize;
    const double halfWidth = 0.05 * settings.partWidthScale * settings.partSize;
    const auto append = [&](const MPoint& tip, const MVector& direction,
                            const MVector& side) {
        const MPoint movedTip = tip + direction * settings.partOffset;
        const MPoint base = movedTip - direction * depth;
        heads.push_back({base + side * halfWidth, movedTip, base - side * halfWidth});
    };
    const short base = endArrowBaseOutline(outline);
    const auto axes = straightLineAxes(base);
    for (unsigned int axis : axes) {
        for (double sign : {-1.0, 1.0}) {
            if (!hasPartAtEnd(settings.shape, sign < 0.0, static_cast<short>(axis))) continue;
            const MVector direction = nativeAxis(axis) * sign;
            const MPoint tip = MPoint::origin + direction * 0.5;
            if (axes.size() == 1) {
                append(tip, direction, nativeAxis(axis == 0 ? 1 : 0));
            } else {
                for (unsigned int side : axes) {
                    if (side != axis) append(tip, direction, nativeAxis(side));
                }
            }
        }
    }
    if (base == 30) {
        for (double z : {-0.5, 0.5}) {
            if (!hasPartAtEnd(settings.shape, z < 0.0)) continue;
            const MPoint tip(0.0, 0.0, z);
            const MVector direction(0.0, -1.0, 0.0);
            append(tip, direction, nativeAxis(2));
        }
    }
    return heads;
}

void appendStraightLines(
    short outline, const ShapeTransform& transform, Strokes& strokes,
    std::vector<StrokeStyle>& styles
) {
    for (unsigned int axis : straightLineAxes(outline)) {
        const MVector direction = nativeAxis(axis);
        appendNativeStroke({
            MPoint::origin - direction * 0.5,
            MPoint::origin + direction * 0.5,
        }, StrokeStyle::Normal, transform, strokes, styles);
    }
}

struct WideEndArrowGeometry {
    std::vector<MPoint> outline;
    std::vector<ArrowHead> triangles;
};

WideEndArrowGeometry wideEndArrowGeometry(short outline, const ShapeSettings& settings) {
    WideEndArrowGeometry geometry;
    const double shaftHalfWidth = 0.025 * std::abs(settings.partWidthScale * settings.partSize);
    const double headHalfWidth = 0.05 * std::abs(settings.partWidthScale * settings.partSize);
    const double depth = 0.1 * std::cos(kPi / 6.0) * settings.partLengthScale * settings.partSize;
    const double tip = 0.5 + settings.partOffset;
    const double shoulder = tip - depth;
    const auto triangle = [&](MPoint first, MPoint second, MPoint third) {
        const MVector normal = (second - first) ^ (third - first);
        if (normal.length() < 1.0e-12) return;
        if (normal.z < 0.0) {
            std::swap(second, third);
        }
        geometry.triangles.push_back({first, second, third});
    };
    const auto quad = [&](MPoint first, MPoint second, MPoint third, MPoint fourth) {
        triangle(first, second, third);
        triangle(first, third, fourth);
    };
    // Split each head base at the shaft joins to keep triangle edges aligned.
    const auto head = [&](MPoint tip, const std::array<MPoint, 4>& base) {
        for (std::size_t index = 0; index + 1 < base.size(); ++index) {
            triangle(tip, base[index], base[index + 1]);
        }
    };

    if (outline == 68) {
        const double outerRadius = 0.5 + shaftHalfWidth;
        const double innerRadius = std::max(0.0, 0.5 - shaftHalfWidth);
        const double baseY = depth - settings.partOffset;
        const double joinY = std::clamp(baseY, 0.0, innerRadius);
        const double outerJoin = std::sqrt(std::max(0.0, outerRadius * outerRadius - joinY * joinY));
        const double innerJoin = std::sqrt(std::max(0.0, innerRadius * innerRadius - joinY * joinY));
        std::vector<MPoint> outer = {MPoint(outerJoin, joinY, 0.0)};
        std::vector<MPoint> inner = {MPoint(innerJoin, joinY, 0.0)};
        // Clip both arc edges at the head bases and sample their remaining angles together.
        for (unsigned int index = 1; index < kCircleSegments / 2; ++index) {
            const double angle = 2.0 * kPi * index / kCircleSegments;
            const bool collapsedInner = joinY >= innerRadius;
            if ((collapsedInner ? outerRadius : innerRadius) * std::sin(angle) <= joinY) continue;
            outer.emplace_back(outerRadius * std::cos(angle), outerRadius * std::sin(angle), 0.0);
            if (collapsedInner) inner.emplace_back(0.0, joinY, 0.0);
            else inner.emplace_back(innerRadius * std::cos(angle), innerRadius * std::sin(angle), 0.0);
        }
        outer.emplace_back(-outerJoin, joinY, 0.0);
        inner.emplace_back(-innerJoin, joinY, 0.0);
        const MPoint rightTip(0.5, -settings.partOffset, 0.0);
        const MPoint leftTip(-0.5, -settings.partOffset, 0.0);
        const MPoint rightOuter(0.5 + headHalfWidth, baseY, 0.0);
        const MPoint rightInner(0.5 - headHalfWidth, baseY, 0.0);
        const MPoint leftOuter(-0.5 - headHalfWidth, baseY, 0.0);
        const MPoint leftInner(-0.5 + headHalfWidth, baseY, 0.0);
        geometry.outline = {rightTip, rightOuter};
        geometry.outline.insert(geometry.outline.end(), outer.begin(), outer.end());
        geometry.outline.insert(geometry.outline.end(), {
            leftOuter, leftTip, leftInner,
        });
        geometry.outline.insert(geometry.outline.end(), inner.rbegin(), inner.rend());
        geometry.outline.push_back(rightInner);
        for (std::size_t index = 0; index + 1 < outer.size(); ++index) {
            quad(outer[index], outer[index + 1], inner[index + 1], inner[index]);
        }
        head(rightTip, {{
            rightOuter, outer.front(), inner.front(), rightInner,
        }});
        head(leftTip, {{
            leftInner, inner.back(), outer.back(), leftOuter,
        }});
    } else if (outline >= 65 && presetPartAxis(settings.shape) >= 0) {
        constexpr std::array<std::array<short, 2>, 3> planes = {{{0, 1}, {0, 2}, {1, 2}}};
        const auto& plane = planes[outline - 65];
        for (unsigned int axis = 0; axis < 2; ++axis) {
            const bool startArrow = hasPartAtEnd(settings.shape, true, plane[axis]);
            const bool endArrow = hasPartAtEnd(settings.shape, false, plane[axis]);
            const double start = startArrow ? -shoulder : -0.5;
            const double end = endArrow ? shoulder : 0.5;
            const auto point = [axis](double along, double side) {
                return axis == 0 ? MPoint(along, side, 0) : MPoint(side, along, 0);
            };
            quad(point(start, -shaftHalfWidth), point(end, -shaftHalfWidth),
                point(end, shaftHalfWidth), point(start, shaftHalfWidth));
        }
        // 4本の腕を順にたどり、矢印のない端は平らに閉じる。
        for (unsigned int arm = 0; arm < 4; ++arm) {
            const unsigned int axis = arm % 2;
            const double sign = arm < 2 ? 1.0 : -1.0;
            const bool arrow = hasPartAtEnd(settings.shape, sign < 0.0, plane[axis]);
            const MVector direction = nativeAxis(axis) * sign;
            const MVector side(-direction.y, direction.x, 0);
            const MPoint base = MPoint::origin + direction * (arrow ? shoulder : 0.5);
            geometry.outline.push_back(base - side * shaftHalfWidth);
            if (arrow) {
                const MPoint apex = MPoint::origin + direction * tip;
                head(apex, {{base - side * headHalfWidth, base - side * shaftHalfWidth,
                    base + side * shaftHalfWidth, base + side * headHalfWidth}});
                geometry.outline.insert(geometry.outline.end(), {
                    base - side * headHalfWidth, apex, base + side * headHalfWidth});
            }
            geometry.outline.push_back(base + side * shaftHalfWidth);
            geometry.outline.push_back(MPoint::origin + (direction + side) * shaftHalfWidth);
        }
    } else {
        const bool cross = outline >= 65;
        const bool startArrow = hasPartAtEnd(settings.shape, true);
        const bool endArrow = hasPartAtEnd(settings.shape, false);
        const double startJoin = startArrow ? -shoulder : -0.5;
        const double endJoin = endArrow ? shoulder : 0.5;
        const auto point = [](double along, double side, unsigned int axis) {
            return axis == 0 ? MPoint(along, side, 0.0) : MPoint(side, along, 0.0);
        };
        if (cross) {
            quad(MPoint(-shaftHalfWidth, -shaftHalfWidth, 0.0),
                MPoint(shaftHalfWidth, -shaftHalfWidth, 0.0),
                MPoint(shaftHalfWidth, shaftHalfWidth, 0.0),
                MPoint(-shaftHalfWidth, shaftHalfWidth, 0.0));
        } else {
            quad(MPoint(startJoin, -shaftHalfWidth, 0.0),
                MPoint(endJoin, -shaftHalfWidth, 0.0),
                MPoint(endJoin, shaftHalfWidth, 0.0),
                MPoint(startJoin, shaftHalfWidth, 0.0));
        }
        for (unsigned int axis = 0; axis < (cross ? 2u : 1u); ++axis) {
            for (double sign : {-1.0, 1.0}) {
                if (!hasPartAtEnd(settings.shape, sign < 0.0)) continue;
                if (cross) {
                    const double start = sign * shaftHalfWidth;
                    quad(point(start, -shaftHalfWidth, axis),
                        point(sign * shoulder, -shaftHalfWidth, axis),
                        point(sign * shoulder, shaftHalfWidth, axis),
                        point(start, shaftHalfWidth, axis));
                }
                head(point(sign * tip, 0.0, axis), {{
                    point(sign * shoulder, -headHalfWidth, axis),
                    point(sign * shoulder, -shaftHalfWidth, axis),
                    point(sign * shoulder, shaftHalfWidth, axis),
                    point(sign * shoulder, headHalfWidth, axis),
                }});
            }
        }
        if (cross) {
            geometry.outline = {
                MPoint(tip, 0.0, 0.0),
                MPoint(shoulder, headHalfWidth, 0.0), MPoint(shoulder, shaftHalfWidth, 0.0),
                MPoint(shaftHalfWidth, shaftHalfWidth, 0.0),
                MPoint(shaftHalfWidth, shoulder, 0.0), MPoint(headHalfWidth, shoulder, 0.0),
                MPoint(0.0, tip, 0.0),
                MPoint(-headHalfWidth, shoulder, 0.0), MPoint(-shaftHalfWidth, shoulder, 0.0),
                MPoint(-shaftHalfWidth, shaftHalfWidth, 0.0),
                MPoint(-shoulder, shaftHalfWidth, 0.0), MPoint(-shoulder, headHalfWidth, 0.0),
                MPoint(-tip, 0.0, 0.0),
                MPoint(-shoulder, -headHalfWidth, 0.0), MPoint(-shoulder, -shaftHalfWidth, 0.0),
                MPoint(-shaftHalfWidth, -shaftHalfWidth, 0.0),
                MPoint(-shaftHalfWidth, -shoulder, 0.0), MPoint(-headHalfWidth, -shoulder, 0.0),
                MPoint(0.0, -tip, 0.0),
                MPoint(headHalfWidth, -shoulder, 0.0), MPoint(shaftHalfWidth, -shoulder, 0.0),
                MPoint(shaftHalfWidth, -shaftHalfWidth, 0.0),
                MPoint(shoulder, -shaftHalfWidth, 0.0), MPoint(shoulder, -headHalfWidth, 0.0),
            };
        } else if (startArrow && endArrow) {
            geometry.outline = {
                MPoint(-tip, 0.0, 0.0),
                MPoint(-shoulder, -headHalfWidth, 0.0), MPoint(-shoulder, -shaftHalfWidth, 0.0),
                MPoint(shoulder, -shaftHalfWidth, 0.0), MPoint(shoulder, -headHalfWidth, 0.0),
                MPoint(tip, 0.0, 0.0),
                MPoint(shoulder, headHalfWidth, 0.0), MPoint(shoulder, shaftHalfWidth, 0.0),
                MPoint(-shoulder, shaftHalfWidth, 0.0), MPoint(-shoulder, headHalfWidth, 0.0),
            };
        } else {
            if (startArrow) {
                geometry.outline = {MPoint(-tip, 0, 0), MPoint(-shoulder, -headHalfWidth, 0),
                    MPoint(-shoulder, -shaftHalfWidth, 0)};
            } else {
                geometry.outline = {MPoint(-0.5, -shaftHalfWidth, 0)};
            }
            if (endArrow) {
                geometry.outline.insert(geometry.outline.end(), {
                    MPoint(shoulder, -shaftHalfWidth, 0), MPoint(shoulder, -headHalfWidth, 0),
                    MPoint(tip, 0, 0), MPoint(shoulder, headHalfWidth, 0), MPoint(shoulder, shaftHalfWidth, 0)});
            } else {
                geometry.outline.insert(geometry.outline.end(), {MPoint(0.5, -shaftHalfWidth, 0), MPoint(0.5, shaftHalfWidth, 0)});
            }
            geometry.outline.push_back(MPoint(startJoin, shaftHalfWidth, 0));
            if (startArrow) geometry.outline.push_back(MPoint(-shoulder, headHalfWidth, 0));
        }
    }
    geometry.outline.push_back(geometry.outline.front());
    constexpr std::array<std::array<unsigned int, 2>, 7> planes = {{{0, 1}, {1, 0}, {2, 0},
        {0, 1}, {0, 2}, {1, 2}, {2, 1}}};
    const auto& plane = planes[outline - 62];
    const auto nativePoint = [&](const MPoint& point) {
        return MPoint::origin + nativeAxis(plane[0]) * point.x + nativeAxis(plane[1]) * point.y;
    };
    for (auto& point : geometry.outline) point = nativePoint(point);
    for (auto& face : geometry.triangles) {
        for (auto& point : face) point = nativePoint(point);
    }
    return geometry;
}

bool hasCrossLineEndSolids(short outline) {
    return outline >= 69 && outline <= 78;
}

short crossLineEndSolidPreset(short outline, bool filled) {
    constexpr std::array<short, 5> bases = {19, 24, 33, 41, 43};
    const short base = bases[(outline - 69) % bases.size()];
    for (short index = 0; index < static_cast<short>(kPresetInfo.size()); ++index) {
        if (kPresetInfo[index].outlineIndex == base && kPresetInfo[index].filled == filled) {
            return index;
        }
    }
    return 0;
}

double crossLineEndSolidOffset(short outline) {
    return (outline - 69) % 5 >= 3 ? 0.45 : 0.5;
}

double crossLineEndSolidAlong(double coordinate, short outline, const ShapeSettings& settings) {
    double along = crossLineEndSolidOffset(outline) + 0.1 * coordinate;
    const double length = settings.partLengthScale * settings.partSize;
    if (length != 1.0) {
        along = 0.5 + (along - 0.5) * length;
    }
    return along + settings.partOffset;
}

MPoint crossLineEndSolidPoint(
    const MPoint& point, short outline, unsigned int axis, double sign,
    const ShapeSettings& settings
) {
    const MVector direction = nativeAxis(axis) * sign;
    const MVector side = nativeAxis((axis + 1) % 3);
    const MVector up = direction ^ side;
    return MPoint::origin + direction * crossLineEndSolidAlong(point.x, outline, settings)
        + side * (0.1 * point.y * settings.partWidthScale * settings.partSize)
        + up * (0.1 * point.z * settings.partWidthScale * settings.partSize);
}

void appendCrossLineEndSolids(
    short outline, const ShapeTransform& transform, Strokes& strokes,
    std::vector<StrokeStyle>& styles
);

void appendPresetGeometry(short shape, const ShapeTransform& transform, Strokes& strokes, std::vector<StrokeStyle>& styles) {
    const short outline = outlinePresetIndex(shape);
    if (hasCrossLineEndSolids(outline)) {
        appendCrossLineEndSolids(outline, transform, strokes, styles);
        return;
    }
    if (outline >= 62 && outline <= 68) {
        appendNativeStroke(wideEndArrowGeometry(outline, transform.settings).outline,
            StrokeStyle::Normal, transform, strokes, styles);
        return;
    }
    if ((outline >= 54 && outline <= 59) || outline == 61) {
        for (const auto& head : endArrowHeads(outline, transform.settings)) {
            appendNativeStroke({head[0], head[1], head[2]},
                StrokeStyle::Normal, transform, strokes, styles);
        }
        if (transform.settings.partOffset != 0.0) {
            const auto axes = straightLineAxes(endArrowBaseOutline(outline));
            for (auto axis : axes) {
                const bool startArrow = hasPartAtEnd(shape, true, static_cast<short>(axis));
                const bool endArrow = hasPartAtEnd(shape, false, static_cast<short>(axis));
                const double moved = startArrow && endArrow
                    ? std::max(0.0, 0.5 + transform.settings.partOffset) : 0.5 + transform.settings.partOffset;
                const MVector direction = nativeAxis(axis);
                appendNativeStroke({MPoint::origin - direction * (startArrow ? moved : 0.5),
                    MPoint::origin + direction * (endArrow ? moved : 0.5)},
                    StrokeStyle::Normal, transform, strokes, styles);
            }
            if (!axes.empty()) return;
            appendPresetComponent(29, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            for (double z : {-0.5, 0.5}) {
                if (!hasPartAtEnd(shape, z < 0.0)) continue;
                appendNativeStroke({MPoint(0, 0, z), MPoint(0, -transform.settings.partOffset, z)},
                    StrokeStyle::Normal, transform, strokes, styles);
            }
            return;
        }
    }
    switch (endArrowBaseOutline(outline)) {
        case 0:  // Gear
            appendPresetComponent(0, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(1, {0, 0, 0}, {0, 0, 0}, {0.275, 0.275, 0.275}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 1:  // Line1st
            appendPresetComponent(2, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 2:  // Line2nd
            appendPresetComponent(45, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 3:  // Line3rd
            appendPresetComponent(46, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 4:  // CrossLine2nd3rd
            appendPresetComponent(3, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 5:  // CrossLine3Axis
            appendPresetComponent(4, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 52:  // CrossLine1st2nd
        case 53:  // CrossLine1st3rd
            appendStraightLines(endArrowBaseOutline(outline), transform, strokes, styles);
            break;
        case 6:  // Triangle
            appendPresetComponent(5, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 7:  // TriangleArrow3D
            appendPresetComponent(6, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 8:  // Square
            appendPresetComponent(7, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 9:  // SquareArrow2D
            appendPresetComponent(8, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 10:  // SquareArrow3D
            appendPresetComponent(9, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 11:  // SquareArrowCrossLine2D
            appendPresetComponent(10, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 12:  // SquareArrowCrossLine3D
            appendPresetComponent(11, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 13:  // SquareArrowCrossLineTemplate2D
            appendPresetComponent(8, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(12, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Template, transform, strokes, styles);
            break;
        case 14:  // SquareArrowCrossLineTemplate3D
            appendPresetComponent(9, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(12, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Template, transform, strokes, styles);
            break;
        case 15:  // SquareArrow4Way2D
            appendPresetComponent(13, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 16:  // SquareArrow4Way3D
            appendPresetComponent(14, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 17:  // SquareTemplateArrow4Way2D
            appendPresetComponent(15, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Template, transform, strokes, styles);
            appendPresetComponent(15, {0, 0, 0}, {0, 0, -90}, {1, 1, 1}, StrokeStyle::Template, transform, strokes, styles);
            appendPresetComponent(15, {0, 0, 0}, {0, 0, 90}, {1, 1, 1}, StrokeStyle::Template, transform, strokes, styles);
            appendPresetComponent(15, {0, 0, 0}, {0, 0, 180}, {1, 1, 1}, StrokeStyle::Template, transform, strokes, styles);
            appendPresetComponent(16, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(17, {0, 0, 0}, {0, 0, 180}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(17, {0, 0, 0}, {0, 0, -90}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(17, {0, 0, 0}, {0, 0, 90}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 18:  // SquareTemplateArrow4Way3D
            appendPresetComponent(15, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Template, transform, strokes, styles);
            appendPresetComponent(15, {0, 0, 0}, {0, 0, -90}, {1, 1, 1}, StrokeStyle::Template, transform, strokes, styles);
            appendPresetComponent(15, {0, 0, 0}, {0, 0, 90}, {1, 1, 1}, StrokeStyle::Template, transform, strokes, styles);
            appendPresetComponent(15, {0, 0, 0}, {0, 0, 180}, {1, 1, 1}, StrokeStyle::Template, transform, strokes, styles);
            appendPresetComponent(18, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(19, {0, 0, 0}, {0, 0, 180}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(19, {0, 0, 0}, {0, 0, -90}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(19, {0, 0, 0}, {0, 0, 90}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 19:  // Cube
            appendPresetComponent(20, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 20:  // CubeArrow2D
            appendPresetComponent(20, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(21, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 21:  // CubeArrow3D
            appendPresetComponent(20, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(22, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 22:  // CubeFin
            appendPresetComponent(23, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 23:  // CubeFinArrow
            appendPresetComponent(20, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(47, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 24:  // Octahedron
            appendPresetComponent(24, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 25:  // OctahedronArrow
            appendPresetComponent(25, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 26:  // OctahedronArrowFin
            appendPresetComponent(25, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(26, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 27:  // Circle
            appendPresetComponent(1, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 28:  // CircleArrow2D
            appendPresetComponent(1, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(27, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 29:  // CircleArrow3D
            appendPresetComponent(1, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(28, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 30:  // Semicircle
            appendPresetComponent(29, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 31:  // SemicircleArrow2D
            appendPresetComponent(29, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(27, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 32:  // SemicircleArrow3D
            appendPresetComponent(29, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(28, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 33:  // Sphere
            appendPresetComponent(1, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(1, {0, 0, 0}, {90, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(1, {0, 0, 0}, {0, 90, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 34:  // SphereArrow2D
            appendPresetComponent(1, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(1, {0, 0, 0}, {90, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(1, {0, 0, 0}, {0, 90, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(30, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 35:  // SphereArrow3D
            appendPresetComponent(1, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(1, {0, 0, 0}, {90, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(1, {0, 0, 0}, {0, 90, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(31, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 36:  // Cylinder
            appendPresetComponent(1, {0, 0, 0.5}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(1, {0, 0, -0.5}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(2, {0.5, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(2, {-0.5, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(2, {0, 0.5, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(2, {0, -0.5, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 37:  // CylinderFin
            appendPresetComponent(1, {0, 0, 0.5}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(1, {0, 0, -0.5}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(2, {0.5, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(2, {-0.5, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(2, {0, -0.5, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(32, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 38:  // CylinderFinArrow
            appendPresetComponent(1, {0, 0, 0.5}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(1, {0, 0, -0.5}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(2, {0.5, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(2, {-0.5, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(2, {0, -0.5, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(47, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 39:  // Arrow
            appendPresetComponent(33, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 40:  // ArrowFin
            appendPresetComponent(34, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 41:  // Pyramid
            appendPresetComponent(35, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 42:  // PyramidFin
            appendPresetComponent(36, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 43:  // Cone
            appendPresetComponent(1, {0, 0, -0.5}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(37, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 44:  // ConeFin
            appendPresetComponent(1, {0, 0, -0.5}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(38, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 45:  // ColorCrossLine3Axis
            appendPresetComponent(39, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::AxisX, transform, strokes, styles);
            appendPresetComponent(40, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::AxisY, transform, strokes, styles);
            appendPresetComponent(41, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::AxisZ, transform, strokes, styles);
            appendPresetComponent(42, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(43, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(44, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 46:  // ColorSphere
        case 48:  // ColorSphereArrow2D
        case 49:  // ColorSphereArrow3D
            appendPresetComponent(1, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::AxisX, transform, strokes, styles);
            appendPresetComponent(1, {0, 0, 0}, {90, 0, 0}, {1, 1, 1}, StrokeStyle::AxisY, transform, strokes, styles);
            appendPresetComponent(1, {0, 0, 0}, {0, 90, 0}, {1, 1, 1}, StrokeStyle::AxisZ, transform, strokes, styles);
            if (outline == 48 || outline == 49) {
                appendPresetComponent(outline == 48 ? 30 : 31, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            }
            break;
        case 47:  // ColorSphereCrossLine
            appendPresetComponent(1, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::AxisX, transform, strokes, styles);
            appendPresetComponent(1, {0, 0, 0}, {90, 0, 0}, {1, 1, 1}, StrokeStyle::AxisY, transform, strokes, styles);
            appendPresetComponent(1, {0, 0, 0}, {0, 90, 0}, {1, 1, 1}, StrokeStyle::AxisZ, transform, strokes, styles);
            appendPresetComponent(39, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::AxisX, transform, strokes, styles);
            appendPresetComponent(40, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::AxisY, transform, strokes, styles);
            appendPresetComponent(41, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::AxisZ, transform, strokes, styles);
            appendPresetComponent(42, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(43, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(44, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 50:  // ColorCube
        case 51:  // ColorCornerCube
            appendColorCubeGeometry(outline == 51, transform, strokes, styles);
            break;
        default:
            break;
    }
}

void appendCrossLineEndSolids(
    short outline, const ShapeTransform& transform, Strokes& strokes,
    std::vector<StrokeStyle>& styles
) {
    ShapeSettings componentSettings;
    componentSettings.shape = crossLineEndSolidPreset(outline, false);
    Strokes componentStrokes;
    std::vector<StrokeStyle> componentStyles;
    appendPresetGeometry(componentSettings.shape, ShapeTransform(componentSettings),
        componentStrokes, componentStyles);
    const double lineEnd = std::max(0.0, std::min(
        crossLineEndSolidAlong(-0.5, outline, transform.settings),
        crossLineEndSolidAlong(0.5, outline, transform.settings)));
    for (unsigned int axis = 0; axis < 3; ++axis) {
        for (double sign : {-1.0, 1.0}) {
            const StrokeStyle lineStyle = outline >= 74 && sign > 0.0
                ? kAxisStyles[axis] : StrokeStyle::Normal;
            if (lineEnd > 0.0) {
                appendNativeStroke({MPoint::origin, MPoint::origin + nativeAxis(axis) * (sign * lineEnd)},
                    lineStyle, transform, strokes, styles);
            }
            for (const auto& component : componentStrokes) {
                std::vector<MPoint> points;
                points.reserve(component.length());
                for (unsigned int index = 0; index < component.length(); ++index) {
                    points.push_back(crossLineEndSolidPoint(component[index], outline, axis, sign, transform.settings));
                }
                appendNativeStroke(points, StrokeStyle::Normal, transform, strokes, styles);
            }
        }
    }
}

const std::vector<RawPoint>& presetPrimitive(int id) {
    static const std::vector<RawPoint> empty;
    switch (id) {
        case 2: {
            static const std::vector<RawPoint> points(kPrimitive2.begin(), kPrimitive2.end());
            return points;
        }
        case 3: {
            static const std::vector<RawPoint> points(kPrimitive3.begin(), kPrimitive3.end());
            return points;
        }
        case 4: {
            static const std::vector<RawPoint> points(kPrimitive4.begin(), kPrimitive4.end());
            return points;
        }
        case 5: {
            static const std::vector<RawPoint> points(kPrimitive5.begin(), kPrimitive5.end());
            return points;
        }
        case 6: {
            static const std::vector<RawPoint> points(kPrimitive6.begin(), kPrimitive6.end());
            return points;
        }
        case 7: {
            static const std::vector<RawPoint> points(kPrimitive7.begin(), kPrimitive7.end());
            return points;
        }
        case 8: {
            static const std::vector<RawPoint> points(kPrimitive8.begin(), kPrimitive8.end());
            return points;
        }
        case 9: {
            static const std::vector<RawPoint> points(kPrimitive9.begin(), kPrimitive9.end());
            return points;
        }
        case 10: {
            static const std::vector<RawPoint> points(kPrimitive10.begin(), kPrimitive10.end());
            return points;
        }
        case 11: {
            static const std::vector<RawPoint> points(kPrimitive11.begin(), kPrimitive11.end());
            return points;
        }
        case 12: {
            static const std::vector<RawPoint> points(kPrimitive12.begin(), kPrimitive12.end());
            return points;
        }
        case 13: {
            static const std::vector<RawPoint> points(kPrimitive13.begin(), kPrimitive13.end());
            return points;
        }
        case 14: {
            static const std::vector<RawPoint> points(kPrimitive14.begin(), kPrimitive14.end());
            return points;
        }
        case 15: {
            static const std::vector<RawPoint> points(kPrimitive15.begin(), kPrimitive15.end());
            return points;
        }
        case 16: {
            static const std::vector<RawPoint> points(kPrimitive16.begin(), kPrimitive16.end());
            return points;
        }
        case 17: {
            static const std::vector<RawPoint> points(kPrimitive17.begin(), kPrimitive17.end());
            return points;
        }
        case 18: {
            static const std::vector<RawPoint> points(kPrimitive18.begin(), kPrimitive18.end());
            return points;
        }
        case 19: {
            static const std::vector<RawPoint> points(kPrimitive19.begin(), kPrimitive19.end());
            return points;
        }
        case 20: {
            static const std::vector<RawPoint> points(kPrimitive20.begin(), kPrimitive20.end());
            return points;
        }
        case 21: {
            static const std::vector<RawPoint> points(kPrimitive21.begin(), kPrimitive21.end());
            return points;
        }
        case 22: {
            static const std::vector<RawPoint> points(kPrimitive22.begin(), kPrimitive22.end());
            return points;
        }
        case 23: {
            static const std::vector<RawPoint> points(kPrimitive23.begin(), kPrimitive23.end());
            return points;
        }
        case 24: {
            static const std::vector<RawPoint> points(kPrimitive24.begin(), kPrimitive24.end());
            return points;
        }
        case 25: {
            static const std::vector<RawPoint> points(kPrimitive25.begin(), kPrimitive25.end());
            return points;
        }
        case 26: {
            static const std::vector<RawPoint> points(kPrimitive26.begin(), kPrimitive26.end());
            return points;
        }
        case 27: {
            static const std::vector<RawPoint> points(kPrimitive27.begin(), kPrimitive27.end());
            return points;
        }
        case 28: {
            static const std::vector<RawPoint> points(kPrimitive28.begin(), kPrimitive28.end());
            return points;
        }
        case 30: {
            static const std::vector<RawPoint> points(kPrimitive30.begin(), kPrimitive30.end());
            return points;
        }
        case 31: {
            static const std::vector<RawPoint> points(kPrimitive31.begin(), kPrimitive31.end());
            return points;
        }
        case 32: {
            static const std::vector<RawPoint> points(kPrimitive32.begin(), kPrimitive32.end());
            return points;
        }
        case 33: {
            static const std::vector<RawPoint> points(kPrimitive33.begin(), kPrimitive33.end());
            return points;
        }
        case 34: {
            static const std::vector<RawPoint> points(kPrimitive34.begin(), kPrimitive34.end());
            return points;
        }
        case 35: {
            static const std::vector<RawPoint> points(kPrimitive35.begin(), kPrimitive35.end());
            return points;
        }
        case 36: {
            static const std::vector<RawPoint> points(kPrimitive36.begin(), kPrimitive36.end());
            return points;
        }
        case 37: {
            static const std::vector<RawPoint> points(kPrimitive37.begin(), kPrimitive37.end());
            return points;
        }
        case 38: {
            static const std::vector<RawPoint> points(kPrimitive38.begin(), kPrimitive38.end());
            return points;
        }
        case 39: {
            static const std::vector<RawPoint> points(kPrimitive39.begin(), kPrimitive39.end());
            return points;
        }
        case 40: {
            static const std::vector<RawPoint> points(kPrimitive40.begin(), kPrimitive40.end());
            return points;
        }
        case 41: {
            static const std::vector<RawPoint> points(kPrimitive41.begin(), kPrimitive41.end());
            return points;
        }
        case 42: {
            static const std::vector<RawPoint> points(kPrimitive42.begin(), kPrimitive42.end());
            return points;
        }
        case 43: {
            static const std::vector<RawPoint> points(kPrimitive43.begin(), kPrimitive43.end());
            return points;
        }
        case 44: {
            static const std::vector<RawPoint> points(kPrimitive44.begin(), kPrimitive44.end());
            return points;
        }
        case 45: {
            static const std::vector<RawPoint> points(kPrimitive45.begin(), kPrimitive45.end());
            return points;
        }
        case 46: {
            static const std::vector<RawPoint> points(kPrimitive46.begin(), kPrimitive46.end());
            return points;
        }
        case 47: {
            static const std::vector<RawPoint> points(kPrimitive47.begin(), kPrimitive47.end());
            return points;
        }
        default:
            return empty;
    }
}
constexpr int kCirclePrimitive = 1;
constexpr int kSemicirclePrimitive = 29;
constexpr int kGearPrimitive = 0;
