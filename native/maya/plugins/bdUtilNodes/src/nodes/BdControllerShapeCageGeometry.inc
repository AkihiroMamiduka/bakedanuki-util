// 寸法を保つ要素は本体の変形後に作り、共通TRSは全体へ一度だけ適用する。
std::shared_ptr<BdControllerShapeNode::Geometry> assembleCageGeometry(const ShapeSettings& settings,
    const PartGeometry& canonical, const PartGeometry& baseBody, const PartGeometry& actualBody) {
    const auto source = untransformedShapeSettings(settings);
    auto result = std::make_shared<BdControllerShapeNode::Geometry>(actualBody);
    if (!source.fill) result->fillParts.clear();
    if (outlinePresetIndex(source.shape) == 36 && source.fill && !source.wide) {
        result->strokes.resize(std::min<std::size_t>(2, result->strokes.size()));
        result->strokeStyles.resize(result->strokes.size());
    }
    makeCageWideBody(source, canonical, baseBody, actualBody, *result);
    appendCageAttachments(source, *result, baseBody, actualBody);
    const ShapeTransform transform(settings);
    for (auto& stroke : result->strokes) for (auto& point : stroke) point = transformPoint(point, transform);
    for (auto& part : result->fillParts) for (auto& point : part.triangles) point = transformPoint(point, transform);
    if (reversesSolidFillWinding(transform)) reverseSolidFillWinding(*result);
    result->bounds = boundsForGeometry(result->strokes, result->fillParts);
    result->offsetLineTemplate = settings.offsetLineTemplate;
    result->offsetLineEndpoint = transformPoint(cagePoint(baseSpacePoint(MPoint::origin, source), source), transform);
    if (settings.showOffsetLine && hasOffsetLine(result->offsetLineEndpoint)) {
        result->offsetLine.append(MPoint::origin);
        result->offsetLine.append(result->offsetLineEndpoint);
        result->bounds.expand(MPoint::origin);
        result->bounds.expand(result->offsetLineEndpoint);
    }
    return result;
}

std::shared_ptr<const BdControllerShapeNode::Geometry> makeCageGeometry(const ShapeSettings& settings) {
    ShapeSettings affine;
    if (cageAffineSettings(settings, affine)) return makeBaseGeometry(affine);
    const auto source = untransformedShapeSettings(settings);
    const auto canonical = cageCanonicalBodyGeometry(source);
    const auto baseBody = cageMappedBodyGeometry(canonical, source, false);
    const auto actualBody = cageMappedBodyGeometry(canonical, source);
    auto result = assembleCageGeometry(settings, canonical, baseBody, actualBody);
    if (settings.fill) {
        auto wireframe = settings;
        wireframe.fill = false;
        result->wireframeGeometry = assembleCageGeometry(wireframe, canonical, baseBody, actualBody);
    }
    return result;
}
