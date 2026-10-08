// Static outline definitions extracted from the legacy ctrlshape.py.
// Coordinates remain in its original XY / +Z orientation until appendPresetComponent.
constexpr std::array<const char*, 90> kPresetNames = {
    "Gear",
    "GearFilled",
    "Line1st",
    "Line2nd",
    "Line3rd",
    "CrossLineXY",
    "CrossLineXYZ",
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
    "ColorCrossLine",
    "ColorSphere",
    "ColorSphereFilled",
    "ColorSphereCrossLine",
    "ColorSphereCrossLineFilled",
};

struct PresetInfo {
    short outlineIndex;
    bool filled;
};

constexpr std::array<PresetInfo, 90> kPresetInfo = {{
    {0, false},  // Gear
    {0, true},  // GearFilled
    {1, false},  // Line1st
    {2, false},  // Line2nd
    {3, false},  // Line3rd
    {4, false},  // CrossLineXY
    {5, false},  // CrossLineXYZ
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
    {45, false},  // ColorCrossLine
    {46, false},  // ColorSphere
    {46, true},  // ColorSphereFilled
    {47, false},  // ColorSphereCrossLine
    {47, true},  // ColorSphereCrossLineFilled
}};

short outlinePresetIndex(short shape) {
    return shape >= 0 && shape < static_cast<short>(kPresetInfo.size())
        ? kPresetInfo[shape].outlineIndex : 0;
}

bool isFilledPreset(short shape) {
    return shape >= 0 && shape < static_cast<short>(kPresetInfo.size())
        && kPresetInfo[shape].filled;
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

void appendPresetGeometry(short shape, const ShapeTransform& transform, Strokes& strokes, std::vector<StrokeStyle>& styles) {
    switch (outlinePresetIndex(shape)) {
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
        case 4:  // CrossLineXY
            appendPresetComponent(3, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 5:  // CrossLineXYZ
            appendPresetComponent(4, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
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
        case 45:  // ColorCrossLine
            appendPresetComponent(39, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::AxisX, transform, strokes, styles);
            appendPresetComponent(40, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::AxisY, transform, strokes, styles);
            appendPresetComponent(41, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::AxisZ, transform, strokes, styles);
            appendPresetComponent(42, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(43, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            appendPresetComponent(44, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::Normal, transform, strokes, styles);
            break;
        case 46:  // ColorSphere
            appendPresetComponent(1, {0, 0, 0}, {0, 0, 0}, {1, 1, 1}, StrokeStyle::AxisX, transform, strokes, styles);
            appendPresetComponent(1, {0, 0, 0}, {90, 0, 0}, {1, 1, 1}, StrokeStyle::AxisY, transform, strokes, styles);
            appendPresetComponent(1, {0, 0, 0}, {0, 90, 0}, {1, 1, 1}, StrokeStyle::AxisZ, transform, strokes, styles);
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
        default:
            break;
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
