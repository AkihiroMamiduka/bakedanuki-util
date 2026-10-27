// 直方体の共有格子から外殻を作り、中心の内部面と重複する稜線を除く。
struct WideCross3AxisBox {
    std::array<double, 3> minimum;
    std::array<double, 3> maximum;
    unsigned int axis;
    StrokeStyle style;

    bool contains(const std::array<double, 3>& point) const {
        for (unsigned int i = 0; i < 3; ++i) {
            if (point[i] < minimum[i] || point[i] > maximum[i]) return false;
        }
        return true;
    }
};

struct WideCross3AxisEdge {
    std::array<std::size_t, 2> vertices;
    std::array<MPoint, 2> points;
    unsigned int normal;
    StrokeStyle style;
    bool crease = false;
};

std::vector<WideCross3AxisBox> wideCross3AxisBoxes(
    const ShapeSettings& settings, const OptionHeads& heads, const std::vector<OptionSite>& sites
) {
    const bool colored = outlinePresetIndex(settings.shape) == 119;
    const double halfWidth = settings.wideWidth * 0.5;
    std::vector<WideCross3AxisBox> boxes;
    for (unsigned int axis = 0; axis < 3; ++axis) for (double sign : {-1.0, 1.0}) {
        const auto direction = nativeAxis(axis) * sign;
        double stop = 0.5;
        for (std::size_t i = 0; i < sites.size(); ++i) {
            if ((sites[i].along - direction).length() >= 1e-10) continue;
            double join = heads.stops[i];
            if (settings.partShape >= 6) {
                // 尖った最内点ではなく、中心または広い底面まで重ねて実交差で接合する。
                join = (sites[i].endpoint - MPoint::origin) * direction + settings.partOffset;
                if (settings.partShape >= 9) join -= 0.1 * partLength(settings);
            }
            stop = std::max(0.0, join);
        }
        if (stop <= 1e-12) continue;
        WideCross3AxisBox box = {{-halfWidth, -halfWidth, -halfWidth},
            {halfWidth, halfWidth, halfWidth}, axis,
            colored && sign > 0 ? kAxisStyles[axis] : StrokeStyle::Normal};
        box.minimum[axis] = sign < 0 ? -stop : 0.0;
        box.maximum[axis] = sign > 0 ? stop : 0.0;
        boxes.push_back(box);
    }
    return boxes;
}

std::vector<OptionClipVolume> wideCross3AxisVolumes(const std::vector<WideCross3AxisBox>& boxes) {
    std::vector<OptionClipVolume> volumes;
    for (const auto& box : boxes) {
        OptionClipVolume volume;
        for (unsigned int axis = 0; axis < 3; ++axis) {
            volume.push_back({nativeAxis(axis), box.maximum[axis]});
            volume.push_back({-nativeAxis(axis), -box.minimum[axis]});
        }
        volumes.push_back(std::move(volume));
    }
    return volumes;
}

void trimWideCross3AxisFin(const ShapeSettings& settings, PartGeometry& fin) {
    const short outline = outlinePresetIndex(settings.shape);
    if ((outline != 118 && outline != 119) || settings.wideWidth <= 2e-12) return;
    // Finの付け根はPartの有無や寸法に追従させず、元の本体へ接合する。
    const auto boxes = wideCross3AxisBoxes(settings, OptionHeads{}, {});
    trimOptionGeometry(fin, wideCross3AxisVolumes(boxes), settings.fill);
}

StrokeStyle wideCross3AxisFaceStyle(
    const std::vector<WideCross3AxisBox>& boxes, const std::array<double, 3>& center,
    unsigned int axis, bool positive, double position
) {
    // 幅1では3本の直方体が同じCubeになるため、端面の軸色を優先する。
    for (const auto& box : boxes) {
        if (box.axis == axis && box.contains(center) &&
            (positive ? box.maximum[axis] : box.minimum[axis]) == position) return box.style;
    }
    StrokeStyle style = StrokeStyle::Normal;
    bool assigned = false;
    for (const auto& box : boxes) {
        if (!box.contains(center) || (positive ? box.maximum[axis] : box.minimum[axis]) != position) continue;
        if (!assigned) {
            style = box.style;
            assigned = true;
        } else if (style != box.style) {
            return StrokeStyle::Normal;
        }
    }
    return style;
}

void appendWideCross3AxisEdges(PartBuilder& builder, std::vector<WideCross3AxisEdge> edges) {
    edges.erase(std::remove_if(edges.begin(), edges.end(), [](const auto& edge) {
        return !edge.crease;
    }), edges.end());
    while (!edges.empty()) {
        const auto first = edges.back();
        edges.pop_back();
        auto start = first.points[0];
        auto end = first.points[1];
        unsigned int axis = 0;
        while (axis < 2 && start[axis] == end[axis]) ++axis;
        bool extended = true;
        while (extended) {
            extended = false;
            for (auto it = edges.begin(); it != edges.end(); ++it) {
                if (it->style != first.style) continue;
                bool sameLine = true;
                for (unsigned int other = 0; other < 3; ++other) {
                    if (other != axis && (it->points[0][other] != start[other] ||
                        it->points[1][other] != start[other])) sameLine = false;
                }
                if (!sameLine) continue;
                if ((it->points[1] - start).length() < 1e-12) start = it->points[0];
                else if ((it->points[0] - end).length() < 1e-12) end = it->points[1];
                else continue;
                edges.erase(it);
                extended = true;
                break;
            }
        }
        builder.stroke({start, end}, first.style);
    }
}

void appendOptionWideCross3Axis(
    PartBuilder& builder, const ShapeSettings& settings, const OptionHeads& heads,
    const std::vector<OptionSite>& sites, std::vector<OptionClipVolume>& bodyVolumes
) {
    const auto boxes = wideCross3AxisBoxes(settings, heads, sites);
    if (settings.wideWidth <= 2e-12) {
        for (const auto& box : boxes) {
            const double end = box.minimum[box.axis] < 0 ? box.minimum[box.axis] : box.maximum[box.axis];
            builder.stroke({MPoint::origin, MPoint::origin + nativeAxis(box.axis) * end}, box.style);
        }
        return;
    }
    for (auto& volume : wideCross3AxisVolumes(boxes)) {
        bodyVolumes.push_back(std::move(volume));
    }
    if (boxes.empty()) return;

    std::array<std::vector<double>, 3> coordinates;
    for (const auto& box : boxes) for (unsigned int axis = 0; axis < 3; ++axis) {
        coordinates[axis].push_back(box.minimum[axis]);
        coordinates[axis].push_back(box.maximum[axis]);
    }
    std::array<std::size_t, 3> count;
    for (unsigned int axis = 0; axis < 3; ++axis) {
        auto& values = coordinates[axis];
        std::sort(values.begin(), values.end());
        values.erase(std::unique(values.begin(), values.end()), values.end());
        count[axis] = values.size() - 1;
    }
    const auto cellIndex = [&](const std::array<std::size_t, 3>& cell) {
        return (cell[0] * count[1] + cell[1]) * count[2] + cell[2];
    };
    const auto cellCenter = [&](const std::array<std::size_t, 3>& cell) {
        std::array<double, 3> center;
        for (unsigned int axis = 0; axis < 3; ++axis) {
            center[axis] = (coordinates[axis][cell[axis]] + coordinates[axis][cell[axis] + 1]) * 0.5;
        }
        return center;
    };
    std::vector<bool> occupied(count[0] * count[1] * count[2], false);
    for (std::size_t x = 0; x < count[0]; ++x) for (std::size_t y = 0; y < count[1]; ++y) {
        for (std::size_t z = 0; z < count[2]; ++z) {
            const std::array<std::size_t, 3> cell = {x, y, z};
            const auto center = cellCenter(cell);
            occupied[cellIndex(cell)] = std::any_of(boxes.begin(), boxes.end(), [&](const auto& box) {
                return box.contains(center);
            });
        }
    }
    const auto vertexIndex = [&](const std::array<std::size_t, 3>& vertex) {
        return (vertex[0] * coordinates[1].size() + vertex[1]) * coordinates[2].size() + vertex[2];
    };
    const auto isConcaveEdge = [&](const std::array<std::size_t, 3>& first,
        const std::array<std::size_t, 3>& last) {
        unsigned int along = 0;
        while (along < 2 && first[along] == last[along]) ++along;
        const unsigned int side = (along + 1) % 3;
        const unsigned int up = (along + 2) % 3;
        unsigned int occupiedCount = 0;
        for (bool beforeSide : {false, true}) for (bool beforeUp : {false, true}) {
            auto neighbor = first;
            neighbor[along] = std::min(first[along], last[along]);
            if (beforeSide) {
                if (neighbor[side] == 0) continue;
                --neighbor[side];
            } else if (neighbor[side] >= count[side]) continue;
            if (beforeUp) {
                if (neighbor[up] == 0) continue;
                --neighbor[up];
            } else if (neighbor[up] >= count[up]) continue;
            if (occupied[cellIndex(neighbor)]) ++occupiedCount;
        }
        // 辺の周囲4セルのうち3セルを本体が占める接合部だけを隠す。
        return occupiedCount == 3;
    };
    std::vector<WideCross3AxisEdge> edges;
    const bool previousSingleSided = builder.singleSided;
    builder.singleSided = true;
    for (std::size_t x = 0; x < count[0]; ++x) for (std::size_t y = 0; y < count[1]; ++y) {
        for (std::size_t z = 0; z < count[2]; ++z) {
            const std::array<std::size_t, 3> cell = {x, y, z};
            if (!occupied[cellIndex(cell)]) continue;
            for (unsigned int axis = 0; axis < 3; ++axis) for (bool positive : {false, true}) {
                auto neighbor = cell;
                if (positive && cell[axis] + 1 < count[axis]) {
                    ++neighbor[axis];
                    if (occupied[cellIndex(neighbor)]) continue;
                } else if (!positive && cell[axis] != 0) {
                    --neighbor[axis];
                    if (occupied[cellIndex(neighbor)]) continue;
                }
                const unsigned int side = (axis + 1) % 3;
                const unsigned int up = (axis + 2) % 3;
                std::array<std::array<std::size_t, 3>, 4> vertices = {cell, cell, cell, cell};
                for (auto& vertex : vertices) vertex[axis] += positive ? 1 : 0;
                ++vertices[1][side];
                ++vertices[2][side];
                ++vertices[2][up];
                ++vertices[3][up];
                if (!positive) std::swap(vertices[1], vertices[3]);
                std::array<MPoint, 4> points;
                for (unsigned int i = 0; i < 4; ++i) {
                    points[i] = MPoint(coordinates[0][vertices[i][0]],
                        coordinates[1][vertices[i][1]], coordinates[2][vertices[i][2]]);
                }
                const auto style = wideCross3AxisFaceStyle(boxes, cellCenter(cell), axis, positive,
                    coordinates[axis][vertices[0][axis]]);
                builder.quad(points[0], points[1], points[2], points[3], style);
                const unsigned int normal = axis * 2 + static_cast<unsigned int>(positive);
                for (unsigned int i = 0; i < 4; ++i) {
                    unsigned int first = i, last = (i + 1) % 4;
                    if (vertexIndex(vertices[first]) > vertexIndex(vertices[last])) std::swap(first, last);
                    const std::array<std::size_t, 2> key = {
                        vertexIndex(vertices[first]), vertexIndex(vertices[last])};
                    const auto found = std::find_if(edges.begin(), edges.end(), [&](const auto& edge) {
                        return edge.vertices == key;
                    });
                    if (found == edges.end()) {
                        edges.push_back({key, {points[first], points[last]}, normal, style});
                    } else {
                        if (found->normal != normal && !isConcaveEdge(vertices[first], vertices[last])) {
                            found->crease = true;
                        }
                        if (found->style != style) found->style = StrokeStyle::Normal;
                    }
                }
            }
        }
    }
    builder.singleSided = previousSingleSided;
    appendWideCross3AxisEdges(builder, std::move(edges));
}
