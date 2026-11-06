// 一般曲面は変形後の三角形上で距離を測り、帯とマーカーの寸法を保つ。
struct CageWideVertex {
    MPoint source;
    MPoint point;
    std::vector<std::size_t> triangles;
};

struct CageWideTriangle {
    std::array<std::size_t, 3> vertices;
    StrokeStyle style = StrokeStyle::Normal;
    int face = -1;
};

struct CageWideMesh {
    std::vector<CageWideVertex> vertices;
    std::vector<CageWideTriangle> triangles;
};

template<typename Mapper, typename Projector>
CageWideMesh makeCageWideMesh(const PartGeometry& surface, const Mapper& map,
    const Projector& project, unsigned int divisions = 8) {
    CageWideMesh result;
    for (const auto& part : surface.fillParts) {
        if (part.marker) continue;
        for (unsigned int index = 0; index + 2 < part.triangles.length(); index += 3) {
            const auto a = part.triangles[index], b = part.triangles[index + 1], c = part.triangles[index + 2];
            int face = -1;
            for (unsigned int axis = 0; axis < 3; ++axis) {
                if (std::abs(a[axis] - b[axis]) > 1e-10 || std::abs(a[axis] - c[axis]) > 1e-10) continue;
                if (std::abs(std::abs(a[axis]) - 0.5) < 1e-10) face = static_cast<int>(axis * 2 + (a[axis] < 0.0 ? 1 : 0));
            }
            std::vector<std::vector<std::size_t>> indices(divisions + 1);
            for (unsigned int i = 0; i <= divisions; ++i) {
                indices[i].resize(divisions + 1 - i);
                for (unsigned int j = 0; j <= divisions - i; ++j) {
                    const auto source = project(a + (b - a) * (static_cast<double>(i) / divisions) +
                        (c - a) * (static_cast<double>(j) / divisions), a, b, c);
                    indices[i][j] = result.vertices.size();
                    result.vertices.push_back({source, map(source), {}});
                }
            }
            for (unsigned int i = 0; i < divisions; ++i) for (unsigned int j = 0; j < divisions - i; ++j) {
                result.triangles.push_back({{indices[i][j], indices[i + 1][j], indices[i][j + 1]}, part.style, face});
                if (i + j + 1 < divisions) result.triangles.push_back(
                    {{indices[i + 1][j], indices[i + 1][j + 1], indices[i][j + 1]}, part.style, face});
            }
        }
    }
    std::vector<std::size_t> order(result.vertices.size());
    for (std::size_t i = 0; i < order.size(); ++i) order[i] = i;
    const auto key = [&](std::size_t index) {
        const auto& point = result.vertices[index].source;
        return std::array<double, 3>{std::round(point.x * 1e10), std::round(point.y * 1e10), std::round(point.z * 1e10)};
    };
    std::sort(order.begin(), order.end(), [&](auto a, auto b) { return key(a) < key(b); });
    std::vector<CageWideVertex> vertices;
    std::vector<std::size_t> remap(order.size());
    std::array<double, 3> previous{};
    for (const auto index : order) {
        const auto next = key(index);
        if (vertices.empty() || next != previous) {
            vertices.push_back(std::move(result.vertices[index]));
            previous = next;
        }
        remap[index] = vertices.size() - 1;
    }
    result.vertices = std::move(vertices);
    for (std::size_t i = 0; i < result.triangles.size(); ++i) for (auto& vertex : result.triangles[i].vertices) {
        vertex = remap[vertex];
        result.vertices[vertex].triangles.push_back(i);
    }
    return result;
}

template<typename Seed, typename Allowed>
std::vector<double> cageWideDistances(const CageWideMesh& mesh, const Seed& seed, const Allowed& allowed) {
    std::vector<double> distances(mesh.vertices.size(), 1e100);
    std::vector<bool> known(mesh.vertices.size(), false);
    std::vector<std::pair<double, std::size_t>> queue;
    const auto compare = [](const auto& a, const auto& b) { return a.first > b.first; };
    const auto push = [&](std::size_t vertex, double value) {
        distances[vertex] = value;
        queue.push_back({value, vertex});
        std::push_heap(queue.begin(), queue.end(), compare);
    };
    for (std::size_t i = 0; i < mesh.vertices.size(); ++i) if (seed(mesh.vertices[i].source)) push(i, 0.0);
    while (!queue.empty()) {
        std::pop_heap(queue.begin(), queue.end(), compare);
        const auto item = queue.back();
        queue.pop_back();
        if (known[item.second] || item.first > distances[item.second]) continue;
        known[item.second] = true;
        for (const auto triangleIndex : mesh.vertices[item.second].triangles) {
            const auto& triangle = mesh.triangles[triangleIndex];
            if (!allowed(triangle)) continue;
            for (unsigned int slot = 0; slot < 3; ++slot) {
                const auto target = triangle.vertices[slot];
                if (known[target]) continue;
                const auto first = triangle.vertices[(slot + 1) % 3], last = triangle.vertices[(slot + 2) % 3];
                const auto& p = mesh.vertices[target].point;
                const auto& a = mesh.vertices[first].point;
                const auto& b = mesh.vertices[last].point;
                double best = distances[target];
                if (known[first]) best = std::min(best, distances[first] + (p - a).length());
                if (known[last]) best = std::min(best, distances[last] + (p - b).length());
                if (known[first] && known[last]) {
                    const auto edge = b - a;
                    const double length = edge.length();
                    if (length > 1e-14) {
                        const double slope = (distances[last] - distances[first]) / length;
                        if (std::abs(slope) < 1.0 - 1e-12) {
                            const double projection = ((p - a) * edge) / length;
                            const double height = std::sqrt(std::max(0.0, (p - a) * (p - a) - projection * projection));
                            const double position = std::clamp(projection - slope * height / std::sqrt(1.0 - slope * slope), 0.0, length);
                            const double value = distances[first] + slope * position + std::hypot(position - projection, height);
                            if (value >= std::max(distances[first], distances[last]) - 1e-12) best = std::min(best, value);
                        }
                    }
                }
                if (best + 1e-12 < distances[target]) push(target, best);
            }
        }
    }
    return distances;
}

struct CageWidePath {
    std::vector<MPoint> points;
    StrokeStyle style = StrokeStyle::Normal;
    MPoint center;
    MVector u;
    MVector v;
    MVector normal;
    double radius = 0.0;
    double first = 0.0;
    double last = 0.0;

    CageWidePath(const MPointArray& source, StrokeStyle sourceStyle, bool curved) : style(sourceStyle) {
        for (const auto& point : source) points.push_back(point);
        if (!curved || points.size() < 5) return;
        const auto a = points.front(), b = points[points.size() / 3], c = points[2 * points.size() / 3];
        const auto firstEdge = b - a, lastEdge = c - a;
        const auto cross = firstEdge ^ lastEdge;
        const double squared = cross * cross;
        if (squared < 1e-18) return;
        center = a + ((cross ^ firstEdge) * (lastEdge * lastEdge) +
            (lastEdge ^ cross) * (firstEdge * firstEdge)) / (2.0 * squared);
        radius = (a - center).length();
        normal = baseSpaceNormalized(cross);
        u = baseSpaceNormalized(a - center);
        v = normal ^ u;
        for (const auto& point : points) if (std::abs((point - center).length() - radius) > 1e-7 ||
            std::abs((point - center) * normal) > 1e-7) { radius = 0.0; return; }
        double previous = 0.0;
        for (std::size_t i = 1; i < points.size(); ++i) {
            const auto delta = points[i] - center;
            const double angle = std::atan2(delta * v, delta * u);
            last += std::remainder(angle - previous, 2.0 * kPi);
            previous = angle;
        }
        if (last < first) std::swap(first, last);
    }

    bool contains(const MPoint& point) const {
        if (radius > 0.0) {
            const auto delta = point - center;
            if (std::abs(delta * normal) > 1e-8 || std::abs(delta.length() - radius) > 1e-8) return false;
            const double angle = std::atan2(delta * v, delta * u);
            for (int turn = -2; turn <= 2; ++turn) if (angle + turn * 2.0 * kPi >= first - 1e-8 &&
                angle + turn * 2.0 * kPi <= last + 1e-8) return true;
            return false;
        }
        for (std::size_t i = 1; i < points.size(); ++i) {
            const auto edge = points[i] - points[i - 1];
            const double squared = edge * edge;
            const double t = squared <= 1e-24 ? 0.0 : std::clamp(((point - points[i - 1]) * edge) / squared, 0.0, 1.0);
            if ((point - (points[i - 1] + edge * t)).length() < 1e-8) return true;
        }
        return false;
    }
};

struct CageWideClipPoint {
    MPoint source;
    MPoint point;
    std::vector<double> values;
};

CageWideClipPoint interpolateCageWidePoint(const CageWideClipPoint& a, const CageWideClipPoint& b, double t) {
    CageWideClipPoint result{a.source + (b.source - a.source) * t, a.point + (b.point - a.point) * t, {}};
    for (std::size_t i = 0; i < a.values.size(); ++i) result.values.push_back(a.values[i] + (b.values[i] - a.values[i]) * t);
    return result;
}

std::vector<CageWideClipPoint> clipCageWidePolygon(const std::vector<CageWideClipPoint>& polygon,
    std::size_t field, double limit, bool inside) {
    std::vector<CageWideClipPoint> result;
    for (std::size_t i = 0; i < polygon.size(); ++i) {
        const auto& a = polygon[i];
        const auto& b = polygon[(i + 1) % polygon.size()];
        const double first = (a.values[field] - limit) * (inside ? -1.0 : 1.0);
        const double last = (b.values[field] - limit) * (inside ? -1.0 : 1.0);
        if (first >= -1e-12) result.push_back(a);
        if ((first < -1e-12 && last > 1e-12) || (first > 1e-12 && last < -1e-12)) {
            result.push_back(interpolateCageWidePoint(a, b, first / (first - last)));
        }
    }
    return result;
}

std::vector<std::vector<CageWideClipPoint>> cageWideOutsideCorner(
    const std::vector<CageWideClipPoint>& polygon, std::size_t markerField) {
    std::vector<std::vector<CageWideClipPoint>> result;
    auto first = clipCageWidePolygon(polygon, markerField, kCornerSquareSize, false);
    auto second = clipCageWidePolygon(clipCageWidePolygon(polygon, markerField, kCornerSquareSize, true),
        markerField + 1, kCornerSquareSize, false);
    if (first.size() >= 3) result.push_back(std::move(first));
    if (second.size() >= 3) result.push_back(std::move(second));
    return result;
}

void appendCageWidePolygon(PartBuilder& builder, const std::vector<CageWideClipPoint>& polygon,
    StrokeStyle style, bool marker, const ShapeSettings& settings) {
    if (polygon.size() < 3) return;
    for (std::size_t i = 1; i + 1 < polygon.size(); ++i) {
        auto b = polygon[i].point, c = polygon[i + 1].point;
        if (builder.singleSided) {
            const auto source = polygon[0].source + ((polygon[i].source - polygon[0].source) +
                (polygon[i + 1].source - polygon[0].source)) / 3.0;
            constexpr double epsilon = 1e-5;
            const auto origin = cageBodyPoint(source, settings);
            const auto x = cageBodyPoint(source + nativeAxis(0) * epsilon, settings) - origin;
            const auto y = cageBodyPoint(source + nativeAxis(1) * epsilon, settings) - origin;
            const auto z = cageBodyPoint(source + nativeAxis(2) * epsilon, settings) - origin;
            if ((x ^ y) * z < 0.0) std::swap(b, c);
        }
        const auto start = builder.geometry.fillParts.size();
        builder.triangle(polygon[0].point, b, c, style);
        if (builder.geometry.fillParts.size() > start) builder.geometry.fillParts.back().marker = marker;
        else if (!builder.geometry.fillParts.empty()) builder.geometry.fillParts.back().marker = marker;
    }
}

void appendCageWideBoundary(PartGeometry& geometry, const CageWideClipPoint& a, const CageWideClipPoint& b,
    std::size_t field, std::size_t groups, double halfWidth, int face, bool corner, StrokeStyle style) {
    std::vector<double> cuts = {0.0, 1.0};
    const auto cut = [&](std::size_t index, double value) {
        const double first = a.values[index] - value, last = b.values[index] - value;
        if ((first < 0.0) != (last < 0.0)) cuts.push_back(first / (first - last));
    };
    for (std::size_t i = 0; i < groups; ++i) if (i != field) cut(i, halfWidth);
    const bool marker = corner && face >= 0 && face % 2 == 0;
    const auto markerField = groups + static_cast<std::size_t>(std::max(face, 0));
    if (marker) { cut(markerField, kCornerSquareSize); cut(markerField + 1, kCornerSquareSize); }
    std::sort(cuts.begin(), cuts.end());
    for (std::size_t i = 1; i < cuts.size(); ++i) {
        const auto middle = interpolateCageWidePoint(a, b, (cuts[i - 1] + cuts[i]) * 0.5);
        bool hidden = false;
        for (std::size_t other = 0; other < groups; ++other) if (other != field &&
            middle.values[other] < halfWidth - 1e-10) hidden = true;
        if (marker && middle.values[markerField] < kCornerSquareSize + 1e-10 &&
            middle.values[markerField + 1] < kCornerSquareSize + 1e-10) hidden = true;
        if (hidden) continue;
        Stroke stroke;
        stroke.append(interpolateCageWidePoint(a, b, cuts[i - 1]).point);
        stroke.append(interpolateCageWidePoint(a, b, cuts[i]).point);
        if ((stroke[1] - stroke[0]).length() > 1e-12) {
            geometry.strokes.push_back(std::move(stroke));
            geometry.strokeStyles.push_back(style);
        }
    }
}

MPoint cageWideSurfacePoint(const MPoint& point, const MPoint& a, const MPoint& b,
    const MPoint& c, short outline) {
    if (outline == 33 || outline == 46) return genericWideSpherePoint(point - MPoint::origin);
    if (outline != 36 && outline != 43) return point;
    if (std::abs(a.x - b.x) < 1e-10 && std::abs(a.x - c.x) < 1e-10) {
        bool rim = false;
        const std::array<MPoint, 3> vertices = {a, b, c};
        for (unsigned int i = 0; i < 3; ++i) {
            const auto first = vertices[i], last = vertices[(i + 1) % 3];
            if (std::abs(std::hypot(first.y, first.z) - 0.5) > 1e-10 ||
                std::abs(std::hypot(last.y, last.z) - 0.5) > 1e-10) continue;
            const auto edge = last - first;
            const double squared = edge * edge;
            const double t = squared <= 1e-24 ? 0.0 : std::clamp(((point - first) * edge) / squared, 0.0, 1.0);
            if ((point - (first + edge * t)).length() < 1e-10) rim = true;
        }
        if (!rim) return point;
    }
    const double radius = outline == 36 ? 0.5 : std::max(0.0, 0.5 - point.x) * 0.5;
    const double current = std::hypot(point.y, point.z);
    return current <= 1e-14 ? point : MPoint(point.x, point.y * radius / current, point.z * radius / current);
}

MPoint cageWidePathPoint(const CageWidePath& path, std::size_t segment, double t) {
    const auto a = path.points[segment - 1], b = path.points[segment];
    if (path.radius <= 0.0) return a + (b - a) * t;
    const auto first = a - path.center, last = b - path.center;
    const double angle = std::atan2(first * path.v, first * path.u);
    const double delta = std::remainder(std::atan2(last * path.v, last * path.u) - angle, 2.0 * kPi);
    return path.center + (path.u * std::cos(angle + delta * t) + path.v * std::sin(angle + delta * t)) * path.radius;
}

void appendCageWideReference(PartGeometry& geometry, const std::vector<CageWidePath>& paths,
    const ShapeSettings& settings, short outline, bool corner) {
    if (settings.wide && settings.wideWidth > 1e-12 && (outline == 33 || outline == 46)) return;
    for (const auto& path : paths) {
        if (settings.wide && settings.wideWidth > 1e-12 && outline == 36 &&
            !std::all_of(path.points.begin(), path.points.end(), [&](const auto& point) {
                return std::abs(point.x - path.points.front().x) < 1e-10;
            })) continue;
        for (std::size_t segment = 1; segment < path.points.size(); ++segment) {
            const auto a = path.points[segment - 1], b = path.points[segment];
            unsigned int along = 0;
            while (along < 2 && std::abs(a[along] - b[along]) < 1e-10) ++along;
            bool cornerEdge = corner;
            for (unsigned int axis = 0; axis < 3; ++axis) if (axis != along &&
                (std::abs(a[axis] - 0.5) > 1e-10 || std::abs(b[axis] - 0.5) > 1e-10)) cornerEdge = false;
            double limit = 0.0;
            const bool aPositive = a[along] >= b[along];
            if (cornerEdge) {
                double distance = 0.0;
                auto previous = cageBodyPoint(aPositive ? a : b, settings);
                for (unsigned int step = 1; step <= 64; ++step) {
                    const double t = static_cast<double>(step) / 64;
                    const auto next = cageBodyPoint(a + (b - a) * (aPositive ? t : 1.0 - t), settings);
                    const double length = (next - previous).length();
                    if (distance + length >= kCornerSquareSize && length > 1e-14) {
                        limit = (step - 1 + (kCornerSquareSize - distance) / length) / 64.0;
                        break;
                    }
                    distance += length;
                    previous = next;
                    limit = 1.0;
                }
            }
            if (cornerEdge && limit >= 1.0 - 1e-12) continue;
            Stroke stroke;
            for (unsigned int step = 0; step <= 16; ++step) {
                const double t = static_cast<double>(step) / 16;
                if (cornerEdge && (aPositive ? t < limit : t > 1.0 - limit)) continue;
                if (stroke.length() == 0 && cornerEdge) {
                    const double boundary = aPositive ? limit : 0.0;
                    stroke.append(cageBodyPoint(cageWidePathPoint(path, segment, boundary), settings));
                }
                stroke.append(cageBodyPoint(cageWidePathPoint(path, segment, t), settings));
            }
            if (cornerEdge && !aPositive && limit < 1.0) stroke.append(cageBodyPoint(
                cageWidePathPoint(path, segment, 1.0 - limit), settings));
            if (stroke.length() >= 2) {
                geometry.strokes.push_back(std::move(stroke));
                geometry.strokeStyles.push_back(path.style);
            }
        }
    }
}

void makeCagePlanarWide(const ShapeSettings& settings, const std::vector<CageWidePath>& paths,
    PartGeometry& geometry) {
    PartGeometry lines;
    for (const auto& path : paths) {
        Stroke stroke;
        for (std::size_t segment = 1; segment < path.points.size(); ++segment) {
            for (unsigned int step = 0; step < 8; ++step) stroke.append(cageBodyPoint(
                cageWidePathPoint(path, segment, static_cast<double>(step) / 8), settings));
        }
        if (!path.points.empty()) stroke.append(cageBodyPoint(path.points.back(), settings));
        if (stroke.length() >= 2) { lines.strokes.push_back(std::move(stroke)); lines.strokeStyles.push_back(path.style); }
    }
    PartPlane plane;
    MVector normal;
    if (!genericWidePlane(lines, plane, normal)) {
        const auto center = cageBodyPoint(MPoint::origin, settings);
        const auto first = cageBodyPoint(MPoint(0.5, 0, 0), settings) - center;
        const auto second = cageBodyPoint(MPoint(0, 0, 0.5), settings) - center;
        normal = baseSpaceNormalized(first ^ second);
        if (normal.length() == 0.0) normal = MVector(0, 1, 0);
        plane = {center, baseSpaceNormalized(first.length() > 0.0 ? first : MVector(1, 0, 0)),
            baseSpaceNormalized(normal ^ (first.length() > 0.0 ? first : MVector(1, 0, 0)))};
    }
    const auto center = lines.strokes.empty() ? cageBodyPoint(MPoint::origin, settings) : lines.strokes.front()[0];
    for (auto& stroke : lines.strokes) for (auto& point : stroke) point -= center - MPoint::origin;
    plane.origin = MPoint::origin;
    WideEndArrowGeometry band;
    const short outline = baseOutlineIndex(outlinePresetIndex(settings.shape));
    const auto joint = (cageBodyPoint(MPoint(-0.25, 0, -0.5), settings) +
        (cageBodyPoint(MPoint(-0.25, 0, 0.5), settings) - cageBodyPoint(MPoint(-0.25, 0, -0.5), settings)) * 0.5) -
        (center - MPoint::origin);
    for (const auto& stroke : lines.strokes) appendGenericWideBand(band, stroke, normal,
        settings.wideWidth * 0.5, outline == 39, outline == 39 ? &joint : nullptr);
    PartBuilder builder(settings.fill);
    appendPartTriangleUnion(builder, band, plane);
    geometry = std::move(builder.geometry);
    for (auto& stroke : geometry.strokes) for (auto& point : stroke) point += center - MPoint::origin;
    for (auto& part : geometry.fillParts) for (auto& point : part.triangles) point += center - MPoint::origin;
}

struct CageArcWideJoin {
    MPoint center;
    MVector major;
    MVector first;
    MVector second;
    double topHeight = 0.0;
    double bottomHeight = 0.0;
    bool top = false;
    bool bottom = false;
};

CageArcWideJoin cageArcWideJoin(const ShapeSettings& settings) {
    CageArcWideJoin result;
    const auto outline = outlinePresetIndex(settings.shape);
    if (!settings.wide || !isAxialArcOutline(outline) || crossCircleBaseOutline(outline) < 0 ||
        settings.wideWidth <= 1e-12) return result;
    const CageArcMetric first(settings), second(settings, true);
    result.center = cageBodyPoint(MPoint::origin, settings);
    result.major = baseSpaceNormalized(first.point(kPi * 0.5) - result.center);
    if (result.major.length() == 0.0) return result;
    result.first = first.binormal(kPi * 0.5);
    result.first -= result.major * (result.first * result.major);
    result.first = baseSpaceNormalized(result.first);
    if (result.first.length() == 0.0) return result;
    result.second = result.first ^ result.major;
    const double sweep = std::clamp(settings.circleAngle, 0.0, 2.0 * kPi);
    const double start = (kPi - sweep) * 0.5, end = (kPi + sweep) * 0.5;
    const double halfWidth = settings.wideWidth * 0.5;
    const auto heightFor = [&](bool top, double& height) {
        const double apex = top ? kPi * 0.5 : kPi * 1.5;
        const double sign = top ? 1.0 : -1.0;
        double minimum = 1e100;
        for (const auto* metric : {&first, &second}) for (double side : {-1.0, 1.0}) {
            const auto distance = [&](double angle) {
                const auto delta = metric->point(angle) - result.center;
                return (delta - result.major * (delta * result.major)).length();
            };
            double previous = apex;
            bool found = false;
            for (unsigned int i = 1; i <= 128; ++i) {
                const double angle = apex + side * kPi * 0.5 * i / 128;
                if (distance(angle) < halfWidth) { previous = angle; continue; }
                double low = 0.0, high = 1.0;
                for (unsigned int step = 0; step < 36; ++step) {
                    const double middle = (low + high) * 0.5;
                    if (distance(previous + (angle - previous) * middle) < halfWidth) low = middle;
                    else high = middle;
                }
                const double intersection = previous + (angle - previous) * ((low + high) * 0.5);
                if (top && (intersection < start - 1e-10 || intersection > end + 1e-10)) return false;
                minimum = std::min(minimum, sign * ((metric->point(intersection) - result.center) * result.major));
                found = true;
                break;
            }
            if (!found) return false;
        }
        if (!(minimum > 0.0)) return false;
        height = sign * minimum;
        return true;
    };
    result.top = heightFor(true, result.topHeight);
    result.bottom = sweep >= 2.0 * kPi - 1e-12 && heightFor(false, result.bottomHeight);
    return result;
}

MPoint cageArcWideJoinedPoint(MPoint point, const CageArcWideJoin& join) {
    const double height = (point - join.center) * join.major;
    if (join.top && height > join.topHeight) point -= join.major * (height - join.topHeight);
    if (join.bottom && height < join.bottomHeight) point -= join.major * (height - join.bottomHeight);
    return point;
}

void appendCageArcWideJoinAngles(std::vector<double>& angles, const CageArcMetric& metric,
    const CageArcWideJoin& join, double first, double last) {
    for (bool top : {false, true}) {
        if (!(top ? join.top : join.bottom)) continue;
        const double height = top ? join.topHeight : join.bottomHeight;
        const auto value = [&](double angle) { return (metric.point(angle) - join.center) * join.major - height; };
        double a = first, va = value(a);
        for (unsigned int i = 1; i <= 256; ++i) {
            const double b = first + (last - first) * i / 256, vb = value(b);
            if ((va < 0.0) != (vb < 0.0)) {
                double low = a, high = b;
                for (unsigned int step = 0; step < 36; ++step) {
                    const double middle = (low + high) * 0.5;
                    if ((value(middle) < 0.0) == (va < 0.0)) low = middle;
                    else high = middle;
                }
                angles.push_back((low + high) * 0.5);
            }
            a = b;
            va = vb;
        }
    }
}

void finishCageArcWideJoin(PartGeometry& geometry, const CageArcWideJoin& join) {
    if (!join.top && !join.bottom) return;
    const auto local = [&](const MPoint& point) {
        const auto delta = point - join.center;
        return MPoint(delta * join.first, delta * join.major, delta * join.second);
    };
    const auto physical = [&](const MPoint& point) {
        return join.center + join.first * point.x + join.major * point.y + join.second * point.z;
    };
    for (auto& stroke : geometry.strokes) for (auto& point : stroke) point = local(point);
    for (auto& part : geometry.fillParts) for (auto& point : part.triangles) point = local(point);
    if (join.top) joinCrossAxialPlane(geometry, join.topHeight);
    if (join.bottom) joinCrossAxialPlane(geometry, join.bottomHeight);
    for (auto& stroke : geometry.strokes) for (auto& point : stroke) point = physical(point);
    for (auto& part : geometry.fillParts) for (auto& point : part.triangles) point = physical(point);
}

void makeCageArcWide(const ShapeSettings& settings, PartGeometry& geometry) {
    const short outline = outlinePresetIndex(settings.shape);
    const bool cross = crossCircleBaseOutline(outline) >= 0;
    const bool axial = isAxialArcOutline(outline);
    const double sweep = std::clamp(settings.circleAngle, 0.0, 2.0 * kPi);
    if (sweep <= 1e-12) { geometry = {}; return; }
    const auto join = cageArcWideJoin(settings);
    PartBuilder builder(settings.fill || join.top || join.bottom);
    const double first = (kPi - sweep) * 0.5, last = (kPi + sweep) * 0.5;
    const unsigned int divisions = std::max(1u, static_cast<unsigned int>(std::ceil(sweep * 64.0 / kPi)));
    for (unsigned int plane = 0; plane < (cross ? 2u : 1u); ++plane) {
        CageArcMetric metric(settings, plane != 0);
        std::vector<double> angles;
        for (unsigned int i = 0; i <= divisions; ++i) angles.push_back(first + (last - first) * i / divisions);
        appendCageArcWideJoinAngles(angles, metric, join, first, last);
        std::sort(angles.begin(), angles.end());
        angles.erase(std::unique(angles.begin(), angles.end(), [](double a, double b) {
            return std::abs(a - b) < 1e-12;
        }), angles.end());
        std::vector<MPoint> outer, inner;
        for (std::size_t i = 0; i < angles.size(); ++i) {
            const double angle = angles[i];
            const auto center = cageArcWideJoinedPoint(metric.point(angle), join);
            const auto normal = axial ? metric.binormal(angle) : metric.normal(angle);
            const auto offset = normal * (settings.wideWidth * 0.5);
            outer.push_back(center + offset);
            const auto origin = cageBodyPoint(MPoint::origin, settings);
            const double inward = axial ? settings.wideWidth * 0.5 : std::min(settings.wideWidth * 0.5,
                std::max(0.0, (center - origin) * normal));
            inner.push_back(center - normal * inward);
            if (i != 0) builder.quad(outer[i - 1], outer[i], inner[i], inner[i - 1]);
        }
        if (settings.wideWidth <= 1e-12) {
            builder.stroke(outer);
            continue;
        }
        builder.stroke(outer);
        builder.stroke(inner);
        if (sweep < 2.0 * kPi - 1e-12) {
            builder.stroke({outer.front(), inner.front()});
            builder.stroke({outer.back(), inner.back()});
        }
    }
    geometry = std::move(builder.geometry);
    finishCageArcWideJoin(geometry, join);
    if (!settings.fill) geometry.fillParts.clear();
}

void makeCageCross3AxisWide(const ShapeSettings& settings, PartGeometry& geometry) {
    const auto center = cageBodyPoint(MPoint::origin, settings);
    std::vector<OptionSite> sites;
    OptionHeads heads;
    for (unsigned int axis = 0; axis < 3; ++axis) for (double sign : {-1.0, 1.0}) {
        const auto endpoint = cageBodyPoint(MPoint::origin + nativeAxis(axis) * (sign * 0.5), settings);
        const auto delta = endpoint - center;
        const auto along = baseSpaceNormalized(delta.length() > 0.0 ? delta : nativeAxis(axis) * sign);
        sites.push_back({MPoint::origin + delta, along, directionalPartSide(axis), false});
        heads.stops.push_back(delta.length());
    }
    auto physical = settings;
    const auto outline = baseOutlineIndex(outlinePresetIndex(settings.shape));
    physical.shape = partPreset(outline == 45 ? 119 : 118);
    physical.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
    physical.baseSpacePlus = MVector(0.5, 0.5, 0.5);
    physical.axisSwap = false;
    physical.partShape = 0;
    PartBuilder builder(settings.fill);
    std::vector<OptionClipVolume> volumes;
    appendOptionWideCross3Axis(builder, physical, heads, sites, volumes);
    geometry = std::move(builder.geometry);
    for (auto& stroke : geometry.strokes) for (auto& point : stroke) point += center - MPoint::origin;
    for (auto& part : geometry.fillParts) for (auto& point : part.triangles) point += center - MPoint::origin;
    for (auto& cap : geometry.bodyCaps) cap.center += center - MPoint::origin;
}

void makeCageSurfaceWide(const ShapeSettings& settings, const PartGeometry& canonical,
    const std::vector<CageWidePath>& paths, PartGeometry& geometry, bool corner) {
    const short outline = baseOutlineIndex(outlinePresetIndex(settings.shape));
    const auto mesh = makeCageWideMesh(canonical,
        [&](const MPoint& point) { return cageBodyPoint(point, settings); },
        [&](const MPoint& point, const MPoint& a, const MPoint& b, const MPoint& c) {
            return cageWideSurfacePoint(point, a, b, c, outline);
        });
    std::vector<std::vector<std::size_t>> pathGroups(outline == 46 ? 3 : 1);
    for (std::size_t i = 0; i < paths.size(); ++i) {
        std::size_t group = 0;
        if (outline == 46) {
            if (paths[i].style == StrokeStyle::AxisY) group = 1;
            else if (paths[i].style == StrokeStyle::AxisZ) group = 2;
        }
        pathGroups[group].push_back(i);
    }
    std::vector<std::vector<double>> fields;
    for (const auto& group : pathGroups) fields.push_back(cageWideDistances(mesh,
        [&](const MPoint& point) {
            if (outline == 50) {
                // 色付き表示線の微小な内寄せではなく、本体の稜線から帯幅を測る。
                unsigned int boundaries = 0;
                for (unsigned int axis = 0; axis < 3; ++axis) {
                    if (std::abs(std::abs(point[axis]) - 0.5) < 1e-8) ++boundaries;
                }
                return boundaries >= 2;
            }
            return std::any_of(group.begin(), group.end(), [&](auto index) { return paths[index].contains(point); });
        }, [](const CageWideTriangle&) { return true; }));
    const auto groups = fields.size();
    if (corner) for (unsigned int axis = 0; axis < 3; ++axis) for (unsigned int component = 0; component < 2; ++component) {
        const auto other = (axis + component + 1) % 3;
        fields.push_back(cageWideDistances(mesh, [&](const MPoint& point) {
            return std::abs(point[axis] - 0.5) < 1e-8 && std::abs(point[other] - 0.5) < 1e-8;
        }, [&](const CageWideTriangle& triangle) { return triangle.face == static_cast<int>(axis * 2); }));
    }
    const auto vertex = [&](std::size_t index) {
        CageWideClipPoint result{mesh.vertices[index].source, mesh.vertices[index].point, {}};
        for (const auto& field : fields) result.values.push_back(std::min(field[index], 1e30));
        return result;
    };
    PartGeometry result;
    appendCageWideReference(result, paths, settings, outline, corner);
    PartBuilder fills(settings.fill), markers(true);
    markers.singleSided = true;
    fills.singleSided = corner && !settings.wide;
    const double halfWidth = settings.wideWidth * 0.5;
    constexpr std::array<StrokeStyle, 8> palette = {StrokeStyle::Normal, StrokeStyle::AxisX,
        StrokeStyle::AxisY, StrokeStyle::AxisXY, StrokeStyle::AxisZ, StrokeStyle::AxisXZ, StrokeStyle::AxisYZ, StrokeStyle::AxisXYZ};
    struct Piece { std::vector<CageWideClipPoint> points; unsigned int mask; };
    for (const auto& triangle : mesh.triangles) {
        std::vector<CageWideClipPoint> points;
        for (const auto index : triangle.vertices) points.push_back(vertex(index));
        const bool marker = corner && triangle.face >= 0 && triangle.face % 2 == 0;
        const auto markerField = groups + static_cast<std::size_t>(std::max(triangle.face, 0));
        if (marker) {
            auto patch = clipCageWidePolygon(clipCageWidePolygon(points, markerField, kCornerSquareSize, true),
                markerField + 1, kCornerSquareSize, true);
            appendCageWidePolygon(markers, patch, kAxisStyles[static_cast<unsigned int>(triangle.face) / 2], true, settings);
        }
        if (!settings.wide || halfWidth <= 1e-12) {
            if (!settings.wide && settings.fill) {
                if (marker) for (const auto& outside : cageWideOutsideCorner(points, markerField)) {
                    appendCageWidePolygon(fills, outside, triangle.style, false, settings);
                } else appendCageWidePolygon(fills, points, triangle.style, false, settings);
            }
            continue;
        }
        std::vector<Piece> pieces = {{points, 0}};
        for (std::size_t group = 0; group < groups; ++group) {
            std::vector<Piece> next;
            for (const auto& piece : pieces) {
                auto outside = clipCageWidePolygon(piece.points, group, halfWidth, false);
                auto inside = clipCageWidePolygon(piece.points, group, halfWidth, true);
                if (outside.size() >= 3) next.push_back({std::move(outside), piece.mask});
                if (inside.size() >= 3) next.push_back({std::move(inside), piece.mask | (1u << group)});
            }
            pieces = std::move(next);
            std::vector<CageWideClipPoint> cuts;
            for (unsigned int edge = 0; edge < 3; ++edge) {
                const auto& a = points[edge];
                const auto& b = points[(edge + 1) % 3];
                const double first = a.values[group] - halfWidth, last = b.values[group] - halfWidth;
                if ((first < 0.0) != (last < 0.0)) cuts.push_back(interpolateCageWidePoint(a, b, first / (first - last)));
            }
            if (cuts.size() == 2) appendCageWideBoundary(result, cuts[0], cuts[1], group, groups, halfWidth,
                triangle.face, corner, outline == 46 ? kAxisStyles[group] : triangle.style);
        }
        if (settings.fill) for (const auto& piece : pieces) {
            if (piece.mask == 0) continue;
            const auto style = outline == 46 ? palette[piece.mask] : triangle.style;
            if (marker) for (const auto& outside : cageWideOutsideCorner(piece.points, markerField)) {
                appendCageWidePolygon(fills, outside, style, false, settings);
            } else appendCageWidePolygon(fills, piece.points, style, false, settings);
        }
    }
    mergeOptionGeometry(result, std::move(fills.geometry));
    mergeOptionGeometry(result, std::move(markers.geometry));
    geometry = std::move(result);
}

void makeCageWideBody(const ShapeSettings& settings, const PartGeometry& canonicalFullGeometry,
    const PartGeometry& baseBodyPhysical, const PartGeometry& actualBodyPhysical, PartGeometry& geometry) {
    static_cast<void>(baseBodyPhysical);
    static_cast<void>(actualBodyPhysical);
    const short outline = baseOutlineIndex(outlinePresetIndex(settings.shape));
    const bool corner = outline == 51;
    if (!settings.wide && !corner) return;
    // 四角形の4頂点も同一円周に乗るため、曲線を持つ本体だけで円弧を推定する。
    const bool curved = outline == 0 || outline == 33 || outline == 36 || outline == 43 ||
        outline == 46 || isPlanarCircleOutline(outline) || isArcOutline(outline);
    std::vector<CageWidePath> paths;
    for (std::size_t i = 0; i < canonicalFullGeometry.strokes.size(); ++i) paths.emplace_back(
        canonicalFullGeometry.strokes[i], canonicalFullGeometry.strokeStyles[i], curved);
    if (outline == 5 || outline == 45) { makeCageCross3AxisWide(settings, geometry); return; }
    if (isArcOutline(outline)) { makeCageArcWide(settings, geometry); return; }
    if (genericWidePlanarOutline(outline) || outline == 1 || outline == 4 || outline == 52 || outline == 53 || outline == 116) {
        if (settings.wideWidth <= 1e-12) {
            geometry = {};
            appendCageWideReference(geometry, paths, settings, outline, false);
        } else makeCagePlanarWide(settings, paths, geometry);
        return;
    }
    makeCageSurfaceWide(settings, canonicalFullGeometry, paths, geometry, corner);
}
