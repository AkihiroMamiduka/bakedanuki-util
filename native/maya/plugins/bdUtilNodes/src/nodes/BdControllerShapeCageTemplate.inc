// 元の論理区間を変形後の曲線へ移し、帯と部品の境界でも表示ラベルを保つ。
struct CageTemplatePath {
    MPointArray points;
    bool templated = false;
};

struct CageTemplateSegment {
    std::array<double, 3> first;
    std::array<double, 3> edge;
    std::array<double, 3> minimum;
    std::array<double, 3> maximum;
    double squared = 0.0;
    std::size_t order = 0;
    bool templated = false;
};

struct CageTemplateNode {
    std::array<double, 3> minimum;
    std::array<double, 3> maximum;
    std::size_t first = 0;
    std::size_t last = 0;
    std::size_t second = 0;
    std::size_t order = 0;
};

struct CageTemplateIndex {
    std::vector<CageTemplateSegment> segments;
    std::vector<CageTemplateNode> nodes;
};

std::size_t appendCageTemplateNode(CageTemplateIndex& index, std::size_t first, std::size_t last) {
    const auto nodeIndex = index.nodes.size();
    index.nodes.emplace_back();
    CageTemplateNode node;
    node.first = first;
    node.last = last;
    node.minimum = index.segments[first].minimum;
    node.maximum = index.segments[first].maximum;
    node.order = index.segments[first].order;
    for (std::size_t i = first + 1; i < last; ++i) {
        const auto& segment = index.segments[i];
        node.order = std::min(node.order, segment.order);
        for (unsigned int axis = 0; axis < 3; ++axis) {
            node.minimum[axis] = std::min(node.minimum[axis], segment.minimum[axis]);
            node.maximum[axis] = std::max(node.maximum[axis], segment.maximum[axis]);
        }
    }
    if (last - first > 8) {
        unsigned int axis = 0;
        for (unsigned int candidate = 1; candidate < 3; ++candidate) {
            if (node.maximum[candidate] - node.minimum[candidate] >
                node.maximum[axis] - node.minimum[axis]) axis = candidate;
        }
        const auto middle = first + (last - first) / 2;
        std::nth_element(index.segments.begin() + first, index.segments.begin() + middle,
            index.segments.begin() + last, [&](const auto& a, const auto& b) {
                const double x = a.minimum[axis] + (a.maximum[axis] - a.minimum[axis]) * 0.5;
                const double y = b.minimum[axis] + (b.maximum[axis] - b.minimum[axis]) * 0.5;
                return x == y ? a.order < b.order : x < y;
            });
        appendCageTemplateNode(index, first, middle);
        node.second = appendCageTemplateNode(index, middle, last);
    }
    index.nodes[nodeIndex] = node;
    return nodeIndex;
}

CageTemplateIndex makeCageTemplateIndex(const std::vector<CageTemplatePath>& paths) {
    CageTemplateIndex result;
    std::size_t count = 0;
    for (const auto& path : paths) count += path.points.length() - 1;
    result.segments.reserve(count);
    for (const auto& path : paths) for (unsigned int i = 1; i < path.points.length(); ++i) {
        const auto a = path.points[i - 1], b = path.points[i];
        CageTemplateSegment segment;
        segment.first = {a.x, a.y, a.z};
        segment.edge = {b.x - a.x, b.y - a.y, b.z - a.z};
        for (unsigned int axis = 0; axis < 3; ++axis) {
            segment.minimum[axis] = std::min(a[axis], b[axis]);
            segment.maximum[axis] = std::max(a[axis], b[axis]);
        }
        segment.squared = segment.edge[0] * segment.edge[0] + segment.edge[1] * segment.edge[1] +
            segment.edge[2] * segment.edge[2];
        segment.order = result.segments.size();
        segment.templated = path.templated;
        result.segments.push_back(segment);
    }
    result.nodes.reserve(count / 2 + 1);
    if (!result.segments.empty()) appendCageTemplateNode(result, 0, result.segments.size());
    return result;
}

double cageTemplateNodeDistanceSquared(const CageTemplateNode& node, const std::array<double, 3>& point) {
    double result = 0.0;
    for (unsigned int axis = 0; axis < 3; ++axis) {
        const double distance = point[axis] - std::clamp(point[axis], node.minimum[axis], node.maximum[axis]);
        result += distance * distance;
    }
    return result;
}

double cageTemplateSegmentDistanceSquared(const CageTemplateSegment& segment,
    const std::array<double, 3>& point) {
    const double x = point[0] - segment.first[0], y = point[1] - segment.first[1],
        z = point[2] - segment.first[2];
    const double parameter = segment.squared == 0.0 ? 0.0 :
        std::clamp((x * segment.edge[0] + y * segment.edge[1] + z * segment.edge[2]) /
            segment.squared, 0.0, 1.0);
    const double dx = point[0] - (segment.first[0] + segment.edge[0] * parameter),
        dy = point[1] - (segment.first[1] + segment.edge[1] * parameter),
        dz = point[2] - (segment.first[2] + segment.edge[2] * parameter);
    return dx * dx + dy * dy + dz * dz;
}

void cageTemplateNearestDistance(const CageTemplateIndex& index, std::size_t nodeIndex,
    const std::array<double, 3>& point, double& closest) {
    const auto& node = index.nodes[nodeIndex];
    if (cageTemplateNodeDistanceSquared(node, point) > closest) return;
    if (node.second == 0) {
        for (std::size_t i = node.first; i < node.last; ++i) {
            closest = std::min(closest, cageTemplateSegmentDistanceSquared(index.segments[i], point));
        }
        return;
    }
    const auto first = nodeIndex + 1;
    if (cageTemplateNodeDistanceSquared(index.nodes[first], point) <=
        cageTemplateNodeDistanceSquared(index.nodes[node.second], point)) {
        cageTemplateNearestDistance(index, first, point, closest);
        cageTemplateNearestDistance(index, node.second, point, closest);
    } else {
        cageTemplateNearestDistance(index, node.second, point, closest);
        cageTemplateNearestDistance(index, first, point, closest);
    }
}

void cageTemplateNearestOrder(const CageTemplateIndex& index, std::size_t nodeIndex,
    const std::array<double, 3>& point, double limit, std::size_t& order, bool& templated) {
    const auto& node = index.nodes[nodeIndex];
    if (node.order >= order || cageTemplateNodeDistanceSquared(node, point) > limit) return;
    if (node.second == 0) {
        for (std::size_t i = node.first; i < node.last; ++i) {
            const auto& segment = index.segments[i];
            if (segment.order < order && cageTemplateSegmentDistanceSquared(segment, point) <= limit) {
                order = segment.order;
                templated = segment.templated;
            }
        }
        return;
    }
    const auto first = nodeIndex + 1;
    if (index.nodes[first].order < index.nodes[node.second].order) {
        cageTemplateNearestOrder(index, first, point, limit, order, templated);
        cageTemplateNearestOrder(index, node.second, point, limit, order, templated);
    } else {
        cageTemplateNearestOrder(index, node.second, point, limit, order, templated);
        cageTemplateNearestOrder(index, first, point, limit, order, templated);
    }
}

bool cageTemplateNearest(const CageTemplateIndex& index, const MPoint& point) {
    if (index.nodes.empty()) return false;
    const std::array<double, 3> coordinates = {point.x, point.y, point.z};
    double closest = 1e100;
    cageTemplateNearestDistance(index, 0, coordinates, closest);
    auto order = index.segments.size();
    bool templated = false;
    // 数値的に同距離の区間は、空間分割順ではなく元の区間順で選ぶ。
    cageTemplateNearestOrder(index, 0, coordinates, closest + 1e-16, order, templated);
    return templated;
}

bool cageTemplateProtected(const MPoint& point, const std::vector<OptionClipVolume>& volumes) {
    return std::any_of(volumes.begin(), volumes.end(), [&](const auto& volume) {
        return !volume.empty() && std::all_of(volume.begin(), volume.end(), [&](const auto& plane) {
            return plane.value(point) <= 1e-9;
        });
    });
}

std::vector<CageTemplatePath> cageTemplatePaths(const ShapeSettings& settings) {
    auto canonical = cageCanonicalBodyGeometry(settings);
    const auto reference = canonical;
    auto source = cageCanonicalSettings(settings);
    source.part = settings.part;
    source.partType = settings.partType;
    source.templateLine = true;
    source.templateLineRate = settings.templateLineRate;
    source.templateLineInvert = settings.templateLineInvert;
    applyBodyTemplate(source, canonical, reference);
    canonical.fillParts.clear();
    auto mapped = cageMappedBodyGeometry(canonical, settings);
    std::vector<CageTemplatePath> result;
    for (std::size_t i = 0; i < mapped.strokes.size(); ++i) {
        CageTemplatePath path;
        path.points = std::move(mapped.strokes[i]);
        path.templated = mapped.strokeStyles[i] == StrokeStyle::Template;
        if (path.points.length() < 2) continue;
        result.push_back(std::move(path));
    }
    return result;
}

void applyCageBodyTemplate(const ShapeSettings& settings, PartGeometry& geometry,
    const PartGeometry&, const std::vector<OptionClipVolume>& protectedParts = {}) {
    if (settings.templateLine) {
        const auto paths = cageTemplatePaths(settings);
        const auto nearest = makeCageTemplateIndex(paths);
        Strokes strokes;
        std::vector<StrokeStyle> styles;
        const auto append = [&](const MPoint& a, const MPoint& b, StrokeStyle style) {
            if ((b - a).length() <= 1e-12) return;
            if (!strokes.empty() && styles.back() == style &&
                (strokes.back()[strokes.back().length() - 1] - a).length() < 1e-9) {
                strokes.back().append(b);
            } else {
                MPointArray stroke;
                stroke.append(a);
                stroke.append(b);
                strokes.push_back(std::move(stroke));
                styles.push_back(style);
            }
        };
        for (std::size_t index = 0; index < geometry.strokes.size(); ++index) {
            const auto& stroke = geometry.strokes[index];
            const auto original = geometry.strokeStyles[index];
            for (unsigned int segment = 1; segment < stroke.length(); ++segment) {
                const auto a = stroke[segment - 1], b = stroke[segment];
                const auto edge = b - a;
                std::vector<double> cuts = {0.0, 1.0};
                for (unsigned int sample = 1; sample < 8; ++sample) cuts.push_back(sample / 8.0);
                const auto planeCut = [&](const MPoint& point, const MVector& normal) {
                    const double difference = edge * normal;
                    if (std::abs(difference) <= 1e-14) return;
                    const double parameter = ((point - a) * normal) / difference;
                    if (parameter > 1e-9 && parameter < 1.0 - 1e-9) cuts.push_back(parameter);
                };
                for (const auto& path : paths) {
                    planeCut(path.points[0], path.points[1] - path.points[0]);
                    const unsigned int last = path.points.length() - 1;
                    planeCut(path.points[last], path.points[last] - path.points[last - 1]);
                }
                for (const auto& volume : protectedParts) for (const auto& plane : volume) {
                    const double difference = edge * plane.normal;
                    if (std::abs(difference) <= 1e-14) continue;
                    const double parameter = -plane.value(a) / difference;
                    if (parameter > 1e-9 && parameter < 1.0 - 1e-9) cuts.push_back(parameter);
                }
                std::sort(cuts.begin(), cuts.end());
                cuts.erase(std::unique(cuts.begin(), cuts.end(), [](double x, double y) {
                    return std::abs(x - y) < 1e-10;
                }), cuts.end());
                const auto styleAt = [&](double parameter) {
                    const auto point = a + edge * parameter;
                    if (cageTemplateProtected(point, protectedParts)) return original;
                    return cageTemplateNearest(nearest, point) ? StrokeStyle::Template : original;
                };
                double first = 0.0, previousMid = (cuts[0] + cuts[1]) * 0.5;
                auto previous = styleAt(previousMid);
                for (std::size_t i = 2; i < cuts.size(); ++i) {
                    const double middle = (cuts[i - 1] + cuts[i]) * 0.5;
                    const auto current = styleAt(middle);
                    if (current != previous) {
                        double low = previousMid, high = middle;
                        for (unsigned int step = 0; step < 24; ++step) {
                            const double parameter = (low + high) * 0.5;
                            if (styleAt(parameter) == previous) low = parameter;
                            else high = parameter;
                        }
                        const double boundary = (low + high) * 0.5;
                        append(a + edge * first, a + edge * boundary, previous);
                        first = boundary;
                        previous = current;
                    }
                    previousMid = middle;
                }
                append(a + edge * first, b, previous);
            }
        }
        geometry.strokes = std::move(strokes);
        geometry.strokeStyles = std::move(styles);
    }
    if (settings.templateFill) applyBodyTemplateFill(settings, geometry, protectedParts);
}
