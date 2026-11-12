using DrawPointBits = std::array<std::uint64_t, 4>;

DrawPointBits drawPointBits(const MPoint& point) {
    DrawPointBits result;
    std::memcpy(&result[0], &point.x, sizeof(double));
    std::memcpy(&result[1], &point.y, sizeof(double));
    std::memcpy(&result[2], &point.z, sizeof(double));
    std::memcpy(&result[3], &point.w, sizeof(double));
    return result;
}

struct DrawPointBitsHash {
    std::size_t operator()(const DrawPointBits& point) const {
        std::size_t result = 0;
        for (const auto bits : point) {
            result ^= std::hash<std::uint64_t>{}(bits) + 0x9e3779b97f4a7c15ULL +
                (result << 6) + (result >> 2);
        }
        return result;
    }
};

// 同一bitの点だけを共有し、primitiveの順序と重複はindexに残す。
void uniqueDrawPoints(const MPointArray& source, MPointArray& unique, MUintArray& indices) {
    std::unordered_map<DrawPointBits, unsigned int, DrawPointBitsHash> lookup;
    lookup.reserve(source.length());
    std::vector<MPoint> points;
    points.reserve(source.length());
    indices.setLength(source.length());
    for (unsigned int i = 0; i < source.length(); ++i) {
        const auto inserted = lookup.emplace(drawPointBits(source[i]), static_cast<unsigned int>(points.size()));
        if (inserted.second) points.push_back(source[i]);
        indices[i] = inserted.first->second;
    }
    unique.setLength(static_cast<unsigned int>(points.size()));
    for (unsigned int i = 0; i < unique.length(); ++i) unique[i] = points[i];
}

std::shared_ptr<const BdControllerShapeNode::Geometry> bakeDrawGeometry(
    const BdControllerShapeNode::Geometry& generated
) {
    auto result = std::make_shared<BdControllerShapeNode::Geometry>();
    auto draw = std::make_shared<BdControllerShapeDrawGeometry>();
    auto topology = std::make_shared<BdControllerShapeDrawGeometry::Topology>();
    for (std::size_t i = 0; i < generated.strokes.size(); ++i) {
        const auto& stroke = generated.strokes[i];
        const auto style = generated.strokeStyles[i];
        topology->templateStyled = topology->templateStyled || style == StrokeStyle::Template;
        // 描画順と連続輪郭を保ち、同じ状態の独立線だけをまとめる。
        if (stroke.length() == 2 && !topology->strokes.empty() &&
            topology->strokes.back().lineList && topology->strokes.back().style == style) {
            draw->strokes.back().append(stroke[0]);
            draw->strokes.back().append(stroke[1]);
            continue;
        }
        BdControllerShapeDrawGeometry::StrokeInfo info;
        info.style = style;
        info.lineList = stroke.length() == 2;
        if (!info.lineList && stroke.length() > 1) {
            info.lineIndices.setLength((stroke.length() - 1) * 2);
            for (unsigned int j = 1; j < stroke.length(); ++j) {
                info.lineIndices[(j - 1) * 2] = j - 1;
                info.lineIndices[(j - 1) * 2 + 1] = j;
            }
        }
        draw->strokes.push_back(stroke);
        topology->strokes.push_back(std::move(info));
    }
    for (std::size_t i = 0; i < draw->strokes.size(); ++i) {
        auto& info = topology->strokes[i];
        if (!info.lineList) continue;
        MPointArray points;
        uniqueDrawPoints(draw->strokes[i], points, info.lineIndices);
        draw->strokes[i] = std::move(points);
    }
    draw->fillParts.resize(generated.fillParts.size());
    topology->fillParts.resize(generated.fillParts.size());
    for (std::size_t i = 0; i < generated.fillParts.size(); ++i) {
        const auto& part = generated.fillParts[i];
        auto& info = topology->fillParts[i];
        info.style = part.style;
        topology->templateStyled = topology->templateStyled || part.style == StrokeStyle::Template;
        info.marker = part.marker;
        info.singleSided = part.singleSided;
        uniqueDrawPoints(part.triangles, draw->fillParts[i], info.triangleIndices);
        if (!part.singleSided) continue;
        topology->singleSided = true;
        info.reversedTriangleIndices = info.triangleIndices;
        for (unsigned int j = 0; j + 2 < info.reversedTriangleIndices.length(); j += 3) {
            std::swap(info.reversedTriangleIndices[j + 1], info.reversedTriangleIndices[j + 2]);
        }
        auto& planes = info.planes;
        planes.reserve(part.triangles.length() / 3);
        for (unsigned int j = 0; j + 2 < part.triangles.length(); j += 3) {
            const auto& a = part.triangles[j];
            const auto normal = (part.triangles[j + 1] - a) ^ (part.triangles[j + 2] - a);
            planes.push_back({normal, -(normal * (a - MPoint::origin)), normal.length()});
        }
    }
    draw->topology = std::move(topology);
    result->drawGeometry = std::move(draw);
    result->bounds = generated.bounds;
    result->offsetLine = generated.offsetLine;
    result->offsetLineEndpoint = generated.offsetLineEndpoint;
    result->offsetLineTemplate = generated.offsetLineTemplate;
    if (generated.wireframeGeometry) {
        result->wireframeGeometry = bakeDrawGeometry(*generated.wireframeGeometry);
    }
    return result;
}

std::shared_ptr<const BdControllerShapeNode::Geometry> transformGeometry(
    const BdControllerShapeNode::Geometry& base,
    const MMatrix& matrix,
    bool showOffsetLine
) {
    auto result = std::make_shared<BdControllerShapeNode::Geometry>();
    auto draw = std::make_shared<BdControllerShapeDrawGeometry>();
    const auto& source = *base.drawGeometry;
    draw->topology = source.topology;
    draw->animationMatrix = matrix;
    draw->reversed = matrix.det3x3() < 0.0;
    bool hasPoint = false;
    const auto transformArrays = [&](const std::vector<MPointArray>& sources, std::vector<MPointArray>& targets) {
        targets.resize(sources.size());
        for (std::size_t i = 0; i < sources.size(); ++i) {
            targets[i].setLength(sources[i].length());
            for (unsigned int j = 0; j < sources[i].length(); ++j) {
                targets[i][j] = sources[i][j] * matrix;
                result->bounds.expand(targets[i][j]);
                hasPoint = true;
            }
        }
    };
    transformArrays(source.strokes, draw->strokes);
    transformArrays(source.fillParts, draw->fillParts);
    if (!hasPoint) result->bounds = MBoundingBox(MPoint::origin, MPoint::origin);
    result->drawGeometry = std::move(draw);
    result->offsetLineTemplate = base.offsetLineTemplate;
    result->offsetLineEndpoint = base.offsetLineEndpoint * matrix;
    if (showOffsetLine && hasOffsetLine(result->offsetLineEndpoint)) {
        result->offsetLine.setLength(2);
        result->offsetLine[0] = MPoint::origin;
        result->offsetLine[1] = result->offsetLineEndpoint;
        result->bounds.expand(MPoint::origin);
        result->bounds.expand(result->offsetLineEndpoint);
    }
    if (base.wireframeGeometry) {
        result->wireframeGeometry = transformGeometry(*base.wireframeGeometry, matrix, showOffsetLine);
    }
    return result;
}
