"""コントローラの公開形状と、回帰検証用オプションの組合せを定義する。"""

SHAPE_NAMES = (
    "Gear",
    "Line",
    "CrossLine",
    "Triangle",
    "Square",
    "Diamond",
    "Circle",
    "ArcRadial",
    "ArcAxial",
    "CrossArcRadial",
    "CrossArcAxial",
    "CrossLine3Axis",
    "Cube",
    "Octahedron",
    "OctahedronArrow",
    "Sphere",
    "Cylinder",
    "Arrow",
    "Pyramid",
    "Cone",
    "ColorCrossLine3Axis",
    "ColorCube",
    "ColorCornerCube",
    "ColorSphere",
)

VARIANT_NAMES = (
    "Gear",
    "GearSwapped",
    "Line",
    "WideLine",
    "CrossLine",
    "WideCrossLine",
    "Triangle",
    "Square",
    "SquareTemplate",
    "Diamond",
    "Circle",
    "WideCircle",
    "ArcRadial",
    "WideArcRadial",
    "ArcAxial",
    "WideArcAxial",
    "CrossArcRadial",
    "WideCrossArcRadial",
    "CrossArcAxial",
    "WideCrossArcAxial",
    "CrossLineSwapped",
    "WideCrossLineSwapped",
    "TriangleSwapped",
    "SquareSwapped",
    "SquareTemplateSwapped",
    "DiamondSwapped",
    "CircleSwapped",
    "WideCircleSwapped",
    "ArcRadialSwapped",
    "WideArcRadialSwapped",
    "ArcAxialSwapped",
    "WideArcAxialSwapped",
    "CrossArcRadialSwapped",
    "WideCrossArcRadialSwapped",
    "CrossArcAxialSwapped",
    "WideCrossArcAxialSwapped",
    "CrossLine3Axis",
    "WideCrossLine3Axis",
    "Cube",
    "Octahedron",
    "OctahedronArrow",
    "Sphere",
    "Cylinder",
    "Arrow",
    "Pyramid",
    "Cone",
    "ColorCrossLine3Axis",
    "ColorWideCrossLine3Axis",
    "ColorCube",
    "ColorCornerCube",
    "ColorSphere",
)


def preset_options(preset):
    """回帰ケース名を公開enumと本体のオプションへ解決する。"""
    swapped = preset.endswith("Swapped")
    base = preset.removesuffix("Swapped")
    wide = base.startswith("Wide") or base.startswith("ColorWide")
    base = (
        base.replace("ColorWide", "Color", 1)
        if base.startswith("ColorWide")
        else base.removeprefix("Wide")
    )
    template = base == "SquareTemplate"
    if template:
        base = "Square"
    base = {"Arc": "ArcRadial", "CrossArc": "CrossArcRadial"}.get(base, base)
    return {
        "shape": SHAPE_NAMES.index(base),
        "shapeAxisSwap": swapped,
        "shapeWide": wide,
        "shapeTemplateLine": template,
        "shapeTemplateLineRate": 0.7,
        "shapeTemplateFill": template,
    }


def set_preset(cmds, shape, preset):
    """Part・Finの設定を保持して本体の回帰ケースだけを切り替える。"""
    for attribute, value in preset_options(preset).items():
        cmds.setAttr(f"{shape}.{attribute}", value)
