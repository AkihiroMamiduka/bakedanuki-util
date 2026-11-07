// 後端が固定長の矢印は、完成した本体の表面からWide・Fin・Guideを組み立てる。
void mapArrowBodyGeometry(PartGeometry& geometry, const ShapeSettings& settings) {
    const auto span = baseSpaceScale(settings);
    const unsigned int axis = settings.axisSwap ? 1 : 0;
    const double minus = settings.baseSpaceMinus[axis];
    const double plus = settings.baseSpacePlus[axis];
    const double direction = plus >= minus ? 1.0 : -1.0;
    const double joint = minus + direction * arrowBodyFixedLength(settings);
    const double frontScale = (plus - joint) / (1.0 - arrowBodyFixedLength(settings));
    for (auto& stroke : geometry.strokes) for (auto& point : stroke) point = bodyBaseSpacePoint(point, settings);
    for (auto& part : geometry.fillParts) {
        for (unsigned int i = 0; i + 2 < part.triangles.length(); i += 3) {
            const double center = (part.triangles[i].x + part.triangles[i + 1].x + part.triangles[i + 2].x) / 3.0;
            const double slope = isCenteredArrowBody(settings)
                ? direction * 2.0 * (center < 0.0 ? bodyAxisRadius(settings, false) : bulkArrowFront(settings))
                : center > -0.5 + arrowBodyFixedLength(settings) ? frontScale : direction;
            const bool reverse = part.singleSided && slope * span.y * span.z < 0.0;
            for (unsigned int vertex = 0; vertex < 3; ++vertex) {
                part.triangles[i + vertex] = bodyBaseSpacePoint(part.triangles[i + vertex], settings);
            }
            if (reverse) std::swap(part.triangles[i + 1], part.triangles[i + 2]);
        }
    }
}

PartGeometry makeArrowFinGeometry(const ShapeSettings& source, const ShapeSettings& raw) {
    PartGeometry fin;
    if (!source.fin || partFinHeight(source) == 0.0) return fin;
    auto finSettings = raw;
    finSettings.fin = true;
    appendShapeFin(finSettings, fin);
    const auto span = baseSpaceScale(source);
    const double direction = span.y < 0.0 ? -1.0 : 1.0;
    const auto publicHeight = presetOrientedPoint(MPoint(0, direction, 0), source.shape,
        source.axisSwap) - MPoint::origin;
    const bool octahedron = outlinePresetIndex(source.shape) == 25;
    const auto mapped = [&](const MPoint& point) {
        const double surface = octahedron ? std::max(0.0, 0.5 - std::abs(point.x)) : 0.0;
        // 本体との切取りで生じた頂点は、その表面自体へ追従させる。
        const bool onBody = octahedron && std::abs(point.x) <= 0.5 + 1e-10 &&
            std::abs(point.y) <= surface + 1e-10;
        const double distance = onBody ? 0.0 : point.y - surface;
        const auto root = point - nativeAxis(1) * distance;
        return bodyBaseSpacePoint(root, source) + publicHeight * distance;
    };
    for (auto& stroke : fin.strokes) for (auto& point : stroke) point = mapped(point);
    for (auto& part : fin.fillParts) for (auto& point : part.triangles) point = mapped(point);
    return fin;
}

void translateArrowGeometry(PartGeometry& geometry, const MVector& translation) {
    for (auto& stroke : geometry.strokes) for (auto& point : stroke) point += translation;
    for (auto& part : geometry.fillParts) for (auto& point : part.triangles) point += translation;
}

std::shared_ptr<const BdControllerShapeNode::Geometry> makeArrowBaseGeometry(
    const ShapeSettings& settings
) {
    const auto source = untransformedShapeSettings(settings);
    auto raw = source;
    raw.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
    raw.baseSpacePlus = MVector(0.5, 0.5, 0.5);
    raw.axisSwap = raw.wide = raw.part = raw.fin = raw.guideLine = false;
    raw.templateLine = raw.templateFill = raw.partTemplate = false;
    raw.fill = true;
    const ShapeTransform rawTransform(raw);
    PartGeometry reference;
    reference.strokes = makeStrokes(rawTransform, reference.strokeStyles);
    reference.fillParts = makeFillParts(rawTransform);
    mapArrowBodyGeometry(reference, source);

    auto result = std::make_shared<BdControllerShapeNode::Geometry>(reference);
    if (!settings.fill) result->fillParts.clear();
    auto physical = source;
    physical.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
    physical.baseSpacePlus = MVector(0.5, 0.5, 0.5);
    physical.axisSwap = physical.part = physical.fin = physical.guideLine = physical.partTemplate = false;
    if (source.axisSwap) {
        physical.firstAxis = 2;
        physical.secondAxis = 0;
    }
    if (physical.wide) {
        // 平面の帯生成は原点を含む平面で行い、法線方向の基準位置を保つ。
        const auto center = baseSpacePoint(MPoint::origin, source) - MPoint::origin;
        auto wideReference = reference;
        translateArrowGeometry(*result, -center);
        translateArrowGeometry(wideReference, -center);
        applyGenericWideBody(physical, *result, nullptr, &wideReference);
        translateArrowGeometry(*result, center);
    }
    if (physical.templateLine || physical.templateFill) {
        applyBodyTemplate(physical, *result, reference);
    }

    raw.fill = settings.fill;
    const auto bodyFills = result->fillParts;
    mergeOptionGeometry(*result, makeArrowFinGeometry(source, raw));
    if (settings.fill && source.fin) removeFinFillOverlaps(*result, bodyFills);
    if (source.guideLine) {
        auto guideSettings = raw;
        guideSettings.guideLine = true;
        PartGeometry guides;
        appendShapeGuide(guideSettings, guides, GuideBodyGeometry{});
        for (std::size_t stroke = 0; stroke < guides.strokes.size(); ++stroke) {
            const auto& points = guides.strokes[stroke];
            for (unsigned int i = 1; i < points.length(); ++i) {
                appendGuideSegment(*result, bodyBaseSpacePoint(points[i], source), guides.strokeStyles[stroke],
                    bodyBaseSpacePoint(points[i - 1], source));
            }
        }
    }

    const ShapeTransform transform(settings);
    for (auto& stroke : result->strokes) for (auto& point : stroke) point = transformPoint(point, transform);
    for (auto& part : result->fillParts) for (auto& point : part.triangles) point = transformPoint(point, transform);
    if (reversesSolidFillWinding(transform)) reverseSolidFillWinding(*result);
    result->bounds = boundsForGeometry(result->strokes, result->fillParts);
    result->offsetLineTemplate = settings.offsetLineTemplate;
    result->offsetLineEndpoint = transformPoint(baseSpacePoint(MPoint::origin, settings), transform);
    if (settings.showOffsetLine && hasOffsetLine(result->offsetLineEndpoint)) {
        result->offsetLine.append(MPoint::origin);
        result->offsetLine.append(result->offsetLineEndpoint);
        result->bounds.expand(MPoint::origin);
        result->bounds.expand(result->offsetLineEndpoint);
    }
    if (settings.fill) {
        auto wireframe = settings;
        wireframe.fill = false;
        result->wireframeGeometry = makeArrowBaseGeometry(wireframe);
    }
    return result;
}
