// 自己交差しないGearの帯は、面の和集合を求めず輪郭から直接生成する。
struct SimpleWideLoop {
    std::vector<MPoint> left;
    std::vector<MPoint> right;
    std::vector<MPoint> outer;
    std::vector<MPoint> inner;
    StrokeStyle style;
};

bool simpleWideSegmentsTouch(const MPoint& a, const MPoint& b, const MPoint& c, const MPoint& d) {
    constexpr double epsilon = 1e-10;
    if (std::max(a.x, b.x) < std::min(c.x, d.x) - epsilon ||
        std::max(c.x, d.x) < std::min(a.x, b.x) - epsilon ||
        std::max(a.y, b.y) < std::min(c.y, d.y) - epsilon ||
        std::max(c.y, d.y) < std::min(a.y, b.y) - epsilon) return false;
    const auto side = [](const MPoint& p, const MPoint& q, const MPoint& r) {
        return (q.x - p.x) * (r.y - p.y) - (q.y - p.y) * (r.x - p.x);
    };
    const double first = side(a, b, c), second = side(a, b, d);
    const double third = side(c, d, a), fourth = side(c, d, b);
    return !((first > epsilon && second > epsilon) || (first < -epsilon && second < -epsilon) ||
        (third > epsilon && fourth > epsilon) || (third < -epsilon && fourth < -epsilon));
}

bool simpleWideLoopIntersects(const std::vector<MPoint>& first, const std::vector<MPoint>& second,
    bool same = false) {
    for (std::size_t i = 0; i < first.size(); ++i) {
        for (std::size_t j = same ? i + 1 : 0; j < second.size(); ++j) {
            if (same && (j == i + 1 || (i == 0 && j + 1 == first.size()))) continue;
            if (simpleWideSegmentsTouch(first[i], first[(i + 1) % first.size()],
                second[j], second[(j + 1) % second.size()])) return true;
        }
    }
    return false;
}

bool simpleWideContains(const std::vector<MPoint>& polygon, const MPoint& point) {
    bool inside = false;
    for (std::size_t i = 0, j = polygon.size() - 1; i < polygon.size(); j = i++) {
        const auto& a = polygon[i];
        const auto& b = polygon[j];
        if ((a.y > point.y) != (b.y > point.y) &&
            point.x < a.x + (b.x - a.x) * (point.y - a.y) / (b.y - a.y)) inside = !inside;
    }
    return inside;
}

bool makeSimpleWideGearBody(const ShapeSettings& settings, PartGeometry& geometry,
    const PartPlane& plane, const MVector& normal, double halfWidth,
    std::vector<OptionClipVolume>* bodyVolumes) {
    if (outlinePresetIndex(settings.shape) != 0 || geometry.strokes.size() != 2) return false;
    const auto project = [&](const MPoint& point) {
        const auto delta = point - plane.origin;
        return MPoint(delta * plane.side, delta * plane.along, 0);
    };
    std::vector<SimpleWideLoop> loops;
    for (std::size_t strokeIndex = 0; strokeIndex < geometry.strokes.size(); ++strokeIndex) {
        const auto& stroke = geometry.strokes[strokeIndex];
        if (stroke.length() < 4 || (stroke[0] - stroke[stroke.length() - 1]).length() > 1e-10) return false;
        const std::size_t count = stroke.length() - 1;
        SimpleWideLoop loop;
        loop.style = geometry.strokeStyles[strokeIndex];
        for (std::size_t i = 0; i < count; ++i) {
            const auto& point = stroke[static_cast<unsigned int>(i)];
            const auto before = point - stroke[static_cast<unsigned int>((i + count - 1) % count)];
            const auto after = stroke[static_cast<unsigned int>((i + 1) % count)] - point;
            if (before.length() < 1e-10 || after.length() < 1e-10) return false;
            const auto first = normal ^ before.normal(), second = normal ^ after.normal();
            const double denominator = 1.0 + first * second;
            if (denominator <= 1e-10) return false;
            const auto offset = (first + second) * (halfWidth / denominator);
            if (offset.length() > halfWidth * 4.0) return false;
            loop.left.push_back(point + offset);
            loop.right.push_back(point - offset);
        }
        std::vector<MPoint> left, right;
        for (std::size_t i = 0; i < count; ++i) {
            const auto next = (i + 1) % count;
            const auto direction = stroke[static_cast<unsigned int>(next)] - stroke[static_cast<unsigned int>(i)];
            if ((loop.left[next] - loop.left[i]) * direction <= 1e-12 ||
                (loop.right[next] - loop.right[i]) * direction <= 1e-12) return false;
            left.push_back(project(loop.left[i]));
            right.push_back(project(loop.right[i]));
        }
        const double leftArea = partPolygonArea(left), rightArea = partPolygonArea(right);
        if (leftArea * rightArea <= 1e-20 || simpleWideLoopIntersects(left, left, true) ||
            simpleWideLoopIntersects(right, right, true) || simpleWideLoopIntersects(left, right)) return false;
        if (std::abs(leftArea) > std::abs(rightArea)) {
            loop.outer = std::move(left);
            loop.inner = std::move(right);
        } else {
            loop.outer = std::move(right);
            loop.inner = std::move(left);
        }
        if (!simpleWideContains(loop.outer, loop.inner.front()) ||
            !simpleWideContains(loop.inner, project(MPoint::origin))) return false;
        loops.push_back(std::move(loop));
    }
    // 外周の帯と内円の帯が離れている通常幅だけを、この経路で扱う。
    const auto& outer = std::abs(partPolygonArea(loops[0].outer)) > std::abs(partPolygonArea(loops[1].outer))
        ? loops[0] : loops[1];
    const auto& inner = &outer == &loops[0] ? loops[1] : loops[0];
    if (simpleWideLoopIntersects(outer.inner, inner.outer) ||
        !std::all_of(inner.outer.begin(), inner.outer.end(), [&](const auto& point) {
            return simpleWideContains(outer.inner, point);
        })) return false;
    PartBuilder result(settings.fill || bodyVolumes != nullptr);
    for (const auto& loop : loops) {
        auto left = loop.left, right = loop.right;
        left.push_back(left.front());
        right.push_back(right.front());
        result.stroke(left, loop.style);
        result.stroke(right, loop.style);
        if (result.filled) for (std::size_t i = 0; i < loop.left.size(); ++i) {
            const auto next = (i + 1) % loop.left.size();
            result.quad(loop.left[i], loop.left[next], loop.right[next], loop.right[i], loop.style);
        }
    }
    if (bodyVolumes) for (const auto& fill : result.geometry.fillParts) {
        for (unsigned int i = 0; i + 2 < fill.triangles.length(); i += 3) {
            auto volume = optionPlanarVolume({fill.triangles[i], fill.triangles[i + 1], fill.triangles[i + 2]});
            if (!volume.empty()) bodyVolumes->push_back(std::move(volume));
        }
    }
    if (!settings.fill) result.geometry.fillParts.clear();
    geometry = std::move(result.geometry);
    return true;
}
