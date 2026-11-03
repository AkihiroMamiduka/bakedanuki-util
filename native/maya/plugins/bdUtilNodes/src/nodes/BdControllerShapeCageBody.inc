// 本体の原型は既存の生成器から取り、面倍率だけを別の変形層として組み立てる。
ShapeSettings cageCanonicalSettings(const ShapeSettings& settings) {
    auto result = untransformedShapeSettings(settings);
    result.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
    result.baseSpacePlus = MVector(0.5, 0.5, 0.5);
    result.baseSpaceFaceScale.fill(1.0);
    result.axisSwap = result.wide = result.part = result.fin = result.guideLine = false;
    result.templateLine = result.templateFill = result.partTemplate = false;
    result.baseSpaceCrossPlane = result.baseSpaceBodyPart = false;
    result.showOffsetLine = false;
    result.fill = true;
    if (outlinePresetIndex(settings.shape) == 51) result.shape = partPreset(19);
    normalizeShapeSettings(result);
    return result;
}

PartGeometry cageCanonicalBodyGeometry(const ShapeSettings& settings) {
    auto source = cageCanonicalSettings(settings);
    PartGeometry result;
    if (!makeOptionShapeGeometry(source, result) && !makeAdjustedPartGeometry(source, result)) {
        result.fillParts = makeFillParts(ShapeTransform(source));
    }
    source.fill = false;
    PartGeometry lines;
    if (!makeOptionShapeGeometry(source, lines) && !makeAdjustedPartGeometry(source, lines)) {
        lines.strokes = makeStrokes(ShapeTransform(source), lines.strokeStyles);
    }
    result.strokes = std::move(lines.strokes);
    result.strokeStyles = std::move(lines.strokeStyles);
    return result;
}

bool cageCurvedSolid(short outline) {
    return outline == 33 || outline == 46 || outline == 36 || outline == 43;
}

MPoint cageProjectedPoint(MPoint point, const ShapeSettings& settings, bool curvedSurface, bool stroke = false) {
    const short outline = outlinePresetIndex(settings.shape);
    if (outline == 33 || outline == 46 || (stroke &&
        (isPlanarCircleOutline(outline) || isArcOutline(outline)))) {
        const double length = std::hypot(point.x, point.y, point.z);
        if (length != 0.0) return MPoint::origin + (point - MPoint::origin) * (0.5 / length);
    } else if ((outline == 36 || outline == 43) && curvedSurface) {
        const double radius = outline == 36 ? 0.5 : 0.5 * (0.5 - point.x);
        const double length = std::hypot(point.y, point.z);
        if (length != 0.0) { point.y *= radius / length; point.z *= radius / length; }
    }
    return point;
}

bool cageBaseReverses(const MPoint& canonical, const ShapeSettings& settings) {
    const auto span = settings.baseSpacePlus - settings.baseSpaceMinus;
    if (!isArrowBody(settings)) return span.x * span.y * span.z < 0.0;
    const unsigned int axis = settings.axisSwap ? 1 : 0;
    const double minus = settings.baseSpaceMinus[axis], plus = settings.baseSpacePlus[axis];
    const double direction = plus >= minus ? 1.0 : -1.0;
    const double depth = arrowBodyFixedLength(settings);
    const double derivative = canonical.x <= -0.5 + depth ? direction :
        (plus - minus - direction * depth) / (1.0 - depth);
    return derivative * span[settings.axisSwap ? 0 : 1] * span.z < 0.0;
}

void appendCageBodyTriangle(PartGeometry::FillPart& part, const std::array<MPoint, 3>& triangle,
    const ShapeSettings& settings, bool deformed, bool curvedSurface, unsigned int depth) {
    if (depth != 0) {
        const auto a = cageProjectedPoint(triangle[0] + (triangle[1] - triangle[0]) * 0.5, settings, curvedSurface);
        const auto b = cageProjectedPoint(triangle[1] + (triangle[2] - triangle[1]) * 0.5, settings, curvedSurface);
        const auto c = cageProjectedPoint(triangle[2] + (triangle[0] - triangle[2]) * 0.5, settings, curvedSurface);
        appendCageBodyTriangle(part, {triangle[0], a, c}, settings, deformed, curvedSurface, depth - 1);
        appendCageBodyTriangle(part, {a, triangle[1], b}, settings, deformed, curvedSurface, depth - 1);
        appendCageBodyTriangle(part, {c, b, triangle[2]}, settings, deformed, curvedSurface, depth - 1);
        appendCageBodyTriangle(part, {a, b, c}, settings, deformed, curvedSurface, depth - 1);
        return;
    }
    std::array<MPoint, 3> points;
    for (unsigned int i = 0; i < 3; ++i) points[i] = deformed
        ? cageBodyPoint(triangle[i], settings) : cageBaseBodyPoint(triangle[i], settings);
    const auto center = triangle[0] + ((triangle[1] - triangle[0]) + (triangle[2] - triangle[0])) / 3.0;
    if (part.singleSided && (cageBaseReverses(center, settings) !=
        (deformed && cageDeterminant(cageBaseBodyPoint(center, settings), settings) < 0.0))) {
        std::swap(points[1], points[2]);
    }
    for (const auto& point : points) part.triangles.append(point);
}

PartGeometry cageMappedBodyGeometry(const PartGeometry& canonical, const ShapeSettings& settings,
    bool deformed = true) {
    PartGeometry result;
    const short outline = outlinePresetIndex(settings.shape);
    for (std::size_t index = 0; index < canonical.strokes.size(); ++index) {
        const auto& stroke = canonical.strokes[index];
        if (stroke.length() < 2) continue;
        MPointArray points;
        for (unsigned int segment = 1; segment < stroke.length(); ++segment) {
            const bool curved = outline == 36 || outline == 43;
            for (unsigned int step = 0; step < 8; ++step) {
                auto point = stroke[segment - 1] + (stroke[segment] - stroke[segment - 1]) *
                    (static_cast<double>(step) / 8.0);
                point = cageProjectedPoint(point, settings, curved, true);
                points.append(deformed ? cageBodyPoint(point, settings) : cageBaseBodyPoint(point, settings));
            }
        }
        points.append(deformed ? cageBodyPoint(stroke[stroke.length() - 1], settings) :
            cageBaseBodyPoint(stroke[stroke.length() - 1], settings));
        result.strokes.push_back(std::move(points));
        result.strokeStyles.push_back(canonical.strokeStyles[index]);
    }
    for (const auto& source : canonical.fillParts) {
        auto part = source;
        part.triangles.clear();
        for (unsigned int i = 0; i + 2 < source.triangles.length(); i += 3) {
            const std::array<MPoint, 3> triangle = {source.triangles[i], source.triangles[i + 1], source.triangles[i + 2]};
            const bool curvedSurface = (outline == 33 || outline == 46) ||
                ((outline == 36 || outline == 43) &&
                    !(triangle[0].x == triangle[1].x && triangle[0].x == triangle[2].x));
            appendCageBodyTriangle(part, triangle, settings, deformed, curvedSurface,
                cageCurvedSolid(outline) ? 1 : 2);
        }
        result.fillParts.push_back(std::move(part));
    }
    result.bounds = boundsForGeometry(result.strokes, result.fillParts);
    return result;
}

bool cageAffineSettings(const ShapeSettings& settings, ShapeSettings& result) {
    if (isArrowBody(settings)) return false;
    MVector scale(1, 1, 1);
    for (unsigned int normal = 0; normal < 3; ++normal) for (unsigned int axis = 0; axis < 3; ++axis) {
        if (axis == normal) continue;
        const double plus = cageFaceScale(normal, axis, true, settings);
        if (plus != cageFaceScale(normal, axis, false, settings)) return false;
        scale[axis] *= plus;
    }
    result = settings;
    const auto center = (settings.baseSpaceMinus + settings.baseSpacePlus) * 0.5;
    for (unsigned int axis = 0; axis < 3; ++axis) {
        result.baseSpaceMinus[axis] = center[axis] + (settings.baseSpaceMinus[axis] - center[axis]) * scale[axis];
        result.baseSpacePlus[axis] = center[axis] + (settings.baseSpacePlus[axis] - center[axis]) * scale[axis];
    }
    result.baseSpaceFaceScale.fill(1.0);
    return true;
}
