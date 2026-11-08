// 新しい矢印本体の断面から、Finの幅と物理距離の高さを組み立てる。
PartGeometry makeExtendedArrowFinGeometry(const ShapeSettings& settings) {
    const short outline = outlinePresetIndex(settings.shape);
    const auto profile = isNotchedArrowBody(settings) ? notchedArrowProfilePoints()
        : outline == kDiamondArrowOutline || outline == 25
            ? std::vector<MPoint>{MPoint(0.5, 0, 0), MPoint(0, 0.5, 0),
                MPoint(-0.5, 0, 0), MPoint(0, -0.5, 0), MPoint(0.5, 0, 0)}
        : outline == kDiamondArrowAxialOutline
            ? std::vector<MPoint>{MPoint(-0.5, -0.5, 0), MPoint(0.5, 0, 0),
                MPoint(-0.5, 0.5, 0), MPoint(-0.5, -0.5, 0)}
        : bulkArrowProfilePoints(settings);
    PartBuilder builder(settings.fill);
    auto physical = settings;
    physical.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
    physical.baseSpacePlus = MVector(0.5, 0.5, 0.5);
    const unsigned int alongAxis = settings.axisSwap ? 1 : 0;
    const unsigned int heightAxis = settings.axisSwap ? 0 : 1;
    const double alongSign = settings.baseSpacePlus[alongAxis] >= settings.baseSpaceMinus[alongAxis] ? 1.0 : -1.0;
    const double heightSign = settings.baseSpacePlus[heightAxis] >= settings.baseSpaceMinus[heightAxis] ? 1.0 : -1.0;
    const auto center = bodyBaseSpacePoint(bodyNativeCenter(settings), settings);
    std::vector<MPoint> section;
    if (isPlanarArrowBody(settings)) {
        double low = 1e100, high = -1e100;
        for (const auto& point : profile) {
            const double along = (bodyBaseSpacePoint(point, settings)[alongAxis] - center[alongAxis]) * alongSign;
            low = std::min(low, along);
            high = std::max(high, along);
        }
        if (outline == 39 && settings.finType == 0) low = 0.0;
        section = {MPoint(low, 0, 0), MPoint(high, 0, 0)};
    } else {
        for (const auto& point : profile) {
            const auto mapped = bodyBaseSpacePoint(point, settings) - center;
            section.emplace_back(mapped[alongAxis] * alongSign, mapped[heightAxis] * heightSign, 0);
        }
    }
    if (section.empty()) return {};
    if (partPolygonArea(section) < 0.0) std::reverse(section.begin(), section.end());
    double low = section.front().x, high = low;
    for (const auto& point : section) {
        low = std::min(low, point.x);
        high = std::max(high, point.x);
    }
    if (high - low < 1e-12) return {};
    appendFinPart(builder, physical, section, {MPoint(low, 0, 0), MPoint(high, 0, 0)},
        settings.finType == 1 ? std::vector<double>{0.5, 0} : std::vector<double>{0.5, 0.5}, 0,
        settings.finTemplate ? StrokeStyle::Template : StrokeStyle::Normal);
    const auto map = [&](const MPoint& point) {
        auto result = center;
        result[alongAxis] += point.x * alongSign;
        result[heightAxis] += point.y * heightSign;
        return result;
    };
    for (auto& stroke : builder.geometry.strokes) for (auto& point : stroke) point = map(point);
    for (auto& part : builder.geometry.fillParts) for (auto& point : part.triangles) point = map(point);
    return std::move(builder.geometry);
}
