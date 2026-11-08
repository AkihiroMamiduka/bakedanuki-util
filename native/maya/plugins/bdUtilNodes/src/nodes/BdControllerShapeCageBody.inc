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
    if (isCapsuleBody(settings)) return capsuleCanonicalBodyGeometry(settings);
    if (isBulkArrowBody(settings)) return bulkArrowCanonicalBodyGeometry(settings);
    if (isNotchedArrowBody(settings)) return notchedArrowCanonicalBodyGeometry(settings);
    if (outlinePresetIndex(settings.shape) == kDiamondArrowAxialOutline) return diamondAxialCanonicalBodyGeometry();
    if (outlinePresetIndex(settings.shape) == kDiamondArrowOutline) return diamondArrowCanonicalBodyGeometry();
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
    return outline == 33 || outline == 46 || outline == 36 || outline == 43 ||
        outline == kCapsuleOutline || outline == kSphereArrowOutline;
}

bool cageBaseReverses(const MPoint& canonical, const ShapeSettings& settings) {
    const auto span = settings.baseSpacePlus - settings.baseSpaceMinus;
    if (isCapsuleBody(settings) || isCenteredArrowBody(settings)) {
        const unsigned int axis = settings.axisSwap ? 1 : 0;
        return (span[axis] >= 0.0 ? 1.0 : -1.0) * span[settings.axisSwap ? 0 : 1] * span.z < 0.0;
    }
    if (!isArrowBody(settings)) return span.x * span.y * span.z < 0.0;
    const unsigned int axis = settings.axisSwap ? 1 : 0;
    const double minus = settings.baseSpaceMinus[axis], plus = settings.baseSpacePlus[axis];
    const double direction = plus >= minus ? 1.0 : -1.0;
    const double depth = arrowBodyFixedLength(settings);
    const double derivative = canonical.x <= -0.5 + depth ? direction :
        (plus - minus - direction * depth) / (1.0 - depth);
    return derivative * span[settings.axisSwap ? 0 : 1] * span.z < 0.0;
}

double cageBodyDeformationDeterminant(const MPoint& canonical, const ShapeSettings& settings) {
    const auto point = cageBaseBodyPoint(canonical, settings);
    if (!isCapsuleBody(settings)) return cageDeterminant(point, settings);
    const auto x = cageCapsuleVector(point, MVector(1, 0, 0), canonical.x, settings);
    const auto y = cageCapsuleVector(point, MVector(0, 1, 0), canonical.x, settings);
    const auto z = cageCapsuleVector(point, MVector(0, 0, 1), canonical.x, settings);
    return (x ^ y) * z;
}

void appendCageBodyTriangle(PartGeometry::FillPart& part, const std::array<MPoint, 3>& triangle,
    const ShapeSettings& settings, bool deformed) {
    std::array<MPoint, 3> points;
    for (unsigned int i = 0; i < 3; ++i) points[i] = deformed
        ? cageBodyPoint(triangle[i], settings) : cageBaseBodyPoint(triangle[i], settings);
    const auto center = triangle[0] + ((triangle[1] - triangle[0]) + (triangle[2] - triangle[0])) / 3.0;
    if (part.singleSided && (cageBaseReverses(center, settings) !=
        (deformed && cageBodyDeformationDeterminant(center, settings) < 0.0))) {
        std::swap(points[1], points[2]);
    }
    for (const auto& point : points) part.triangles.append(point);
}

PartGeometry cageMappedBodyGeometry(const PartGeometry& canonical, const ShapeSettings& settings,
    bool deformed = true) {
    PartGeometry result;
    for (std::size_t index = 0; index < canonical.strokes.size(); ++index) {
        const auto& stroke = canonical.strokes[index];
        if (stroke.length() < 2) continue;
        MPointArray points;
        // 曲線も原型のサンプル頂点を保ち、元辺の途中をCageで曲げ直さない。
        for (const auto& point : stroke) points.append(
            deformed ? cageBodyPoint(point, settings) : cageBaseBodyPoint(point, settings));
        result.strokes.push_back(std::move(points));
        result.strokeStyles.push_back(canonical.strokeStyles[index]);
    }
    for (const auto& source : canonical.fillParts) {
        auto part = source;
        part.triangles.clear();
        for (unsigned int i = 0; i + 2 < source.triangles.length(); i += 3) {
            const std::array<MPoint, 3> triangle = {source.triangles[i], source.triangles[i + 1], source.triangles[i + 2]};
            appendCageBodyTriangle(part, triangle, settings, deformed);
        }
        result.fillParts.push_back(std::move(part));
    }
    result.bounds = boundsForGeometry(result.strokes, result.fillParts);
    return result;
}

bool cageAffineSettings(const ShapeSettings& settings, ShapeSettings& result) {
    if (isCenteredArrowBody(settings) || isCapsuleBody(settings) ||
        outlinePresetIndex(settings.shape) == kDiamondArrowAxialOutline) return false;
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

bool makeAffineCageWideBody(const ShapeSettings& settings, PartGeometry& geometry) {
    if (isCapsuleBody(settings) || isCenteredArrowBody(settings) ||
        outlinePresetIndex(settings.shape) == kDiamondArrowAxialOutline) return false;
    if (!settings.wide) return false;
    auto body = untransformedShapeSettings(settings);
    if (hasCageMapping(body)) {
        ShapeSettings affine;
        if (!cageAffineSettings(body, affine)) return false;
        body = affine;
    }
    // Partの有無で本体の角や穴が変わらないよう、既存の正確な帯生成を使う。
    body.part = body.fin = body.guideLine = body.showOffsetLine = false;
    body.templateLine = body.templateFill = body.partTemplate = false;
    body.baseSpaceBodyPart = false;
    geometry = *makeBaseGeometry(body);
    return true;
}
