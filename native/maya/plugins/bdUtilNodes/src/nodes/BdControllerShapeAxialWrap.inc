// 展開図の対称断面を周期的に合成し、主面と立ち上がりを同じ角度で曲げる。
struct AxialWrapEdge {
    double first;
    double last;
    double firstHeight;
    double lastHeight;

    double value(double position) const {
        return firstHeight + (lastHeight - firstHeight) * ((position - first) / (last - first));
    }
};

struct AxialWrapSpoke {
    double position;
    double height;
};

struct AxialWrapData {
    std::vector<AxialWrapEdge> main;
    std::vector<AxialWrapEdge> heads;
    std::vector<AxialWrapEdge> crest;
    std::vector<AxialWrapSpoke> spokes;
    std::vector<AxialWrapSpoke> crestSpokes;
    std::vector<double> slices;
};

double axialWrapPosition(double position) {
    double result = std::fmod(position, kPi);
    if (result < 0.0) result += kPi;
    return result < 1e-12 || kPi - result < 1e-12 ? 0.0 : result;
}

void addAxialWrapEdge(std::vector<AxialWrapEdge>& edges,
    std::vector<AxialWrapSpoke>& spokes, double first, double last,
    double firstHeight, double lastHeight) {
    if (!std::isfinite(first) || !std::isfinite(last) ||
        !std::isfinite(firstHeight) || !std::isfinite(lastHeight)) return;
    firstHeight = std::max(0.0, firstHeight);
    lastHeight = std::max(0.0, lastHeight);
    if (first > last) {
        std::swap(first, last);
        std::swap(firstHeight, lastHeight);
    }
    if (last - first < 1e-12) {
        const double height = std::max(firstHeight, lastHeight);
        if (height > 1e-12) spokes.push_back({axialWrapPosition(first), height});
        return;
    }
    // 一次関数の各周期では高い側が支配するため、長い辺も最大一周分で表せる。
    if (last - first > kPi) {
        const double slope = (lastHeight - firstHeight) / (last - first);
        if (lastHeight > firstHeight) {
            first = last - kPi;
            firstHeight = lastHeight - slope * kPi;
        } else {
            last = first + kPi;
            lastHeight = firstHeight + slope * kPi;
        }
    }
    const double length = last - first;
    const double begin = axialWrapPosition(first);
    const double finish = begin + length;
    const double split = std::min(finish, kPi);
    const double splitHeight = firstHeight + (lastHeight - firstHeight) * ((split - begin) / length);
    if (split - begin > 1e-12) edges.push_back({begin, split, firstHeight, splitHeight});
    if (finish > kPi + 1e-12) edges.push_back({0.0, finish - kPi, splitHeight, lastHeight});
}

void addAxialWrapProfile(std::vector<AxialWrapEdge>& edges,
    std::vector<AxialWrapSpoke>& spokes, const std::vector<MPoint>& profile) {
    for (std::size_t i = 0; i < profile.size(); ++i) {
        auto a = profile[i], b = profile[(i + 1) % profile.size()];
        if (a.y < -1e-12 && b.y < -1e-12) continue;
        if (a.y < 0.0 && b.y > 0.0) a = a + (b - a) * (-a.y / (b.y - a.y));
        else if (b.y < 0.0 && a.y > 0.0) b = b + (a - b) * (-b.y / (a.y - b.y));
        if (a.y < -1e-12 || b.y < -1e-12) continue;
        addAxialWrapEdge(edges, spokes, a.x, b.x, a.y, b.y);
    }
}

void appendAxialWrapCuts(std::vector<double>& cuts, const std::vector<AxialWrapEdge>& edges) {
    for (const auto& edge : edges) {
        cuts.push_back(edge.first);
        cuts.push_back(edge.last);
    }
    for (std::size_t i = 0; i < edges.size(); ++i) for (std::size_t j = i + 1; j < edges.size(); ++j) {
        const double first = std::max(edges[i].first, edges[j].first);
        const double last = std::min(edges[i].last, edges[j].last);
        if (last - first < 1e-12) continue;
        const double a = edges[i].value(first) - edges[j].value(first);
        const double b = edges[i].value(last) - edges[j].value(last);
        if ((a < -1e-12 && b > 1e-12) || (a > 1e-12 && b < -1e-12)) {
            cuts.push_back(first + (last - first) * (a / (a - b)));
        }
    }
}

AxialWrapData makeAxialWrapData(const ShapeSettings& settings) {
    AxialWrapData data;
    const double sweep = std::clamp(settings.circleAngle, 0.0, 2.0 * kPi);
    if (sweep < 1e-12) return data;
    const double first = (kPi - sweep) * 0.25;
    const double last = (kPi + sweep) * 0.25;
    const double length = partLength(settings);
    const double width = partWidth(settings);
    const double depth = settings.partShape <= 1 ? 0.1 * std::cos(kPi / 6.0) * length : 0.1 * length;
    const bool both = settings.partType == 1;
    double bodyFirst = first, bodyLast = last;
    if (settings.partShape <= 2 && depth > 0.0 && std::abs(width) > 1e-12) {
        bodyFirst += depth;
        if (both) bodyLast -= depth;
    }
    std::vector<AxialWrapSpoke> bodySpokes;
    if (bodyLast - bodyFirst > 1e-12) {
        addAxialWrapEdge(data.main, bodySpokes, bodyFirst, bodyLast,
            settings.wideWidth * 0.5, settings.wideWidth * 0.5);
    }
    for (int index = 0; index < (both ? 2 : 1); ++index) {
        const double anchor = index == 0 ? first : last;
        const double direction = index == 0 ? -1.0 : 1.0;
        std::vector<MPoint> profile;
        if (settings.partShape <= 1) {
            profile = {MPoint(anchor - direction * depth, 0.05 * width, 0),
                MPoint(anchor, 0, 0), MPoint(anchor - direction * depth, -0.05 * width, 0)};
        } else {
            const unsigned int kind = settings.partShape == 2 ? 3 : settings.partShape - 3;
            for (const auto& p : planarEndProfile(kind)) {
                const double along = (0.1 * p.x - (kind == 3 ? 0.05 : 0.0)) * length;
                profile.emplace_back(anchor + direction * along, 0.1 * p.y * width, 0);
            }
        }
        addAxialWrapProfile(data.heads, data.spokes, profile);
        if (settings.partShape == 1) {
            const double base = anchor - direction * depth;
            addAxialWrapProfile(data.crest, data.crestSpokes,
                {MPoint(base, 0, 0), MPoint(base, 0.05 * std::abs(width), 0), MPoint(anchor, 0, 0)});
        }
    }
    data.main.insert(data.main.end(), data.heads.begin(), data.heads.end());
    for (unsigned int i = 0; i <= kCircleSegments; ++i) data.slices.push_back(kPi * i / kCircleSegments);
    appendAxialWrapCuts(data.slices, data.main);
    appendAxialWrapCuts(data.slices, data.crest);
    for (const auto& spoke : data.spokes) data.slices.push_back(spoke.position);
    for (const auto& spoke : data.crestSpokes) data.slices.push_back(spoke.position);
    appendAxialJoinAngles(data.slices, settings, 0.0, kPi, 0.5);
    std::sort(data.slices.begin(), data.slices.end());
    data.slices.erase(std::unique(data.slices.begin(), data.slices.end(), [](double a, double b) {
        return std::abs(a - b) < 1e-12;
    }), data.slices.end());
    return data;
}

struct AxialWrapInterval {
    double first;
    double last;
    double firstHeight;
    double lastHeight;
    bool active;
};

std::vector<AxialWrapInterval> axialWrapIntervals(
    const std::vector<double>& slices, const std::vector<AxialWrapEdge>& edges
) {
    std::vector<AxialWrapInterval> intervals;
    for (std::size_t i = 1; i < slices.size(); ++i) {
        const double first = slices[i - 1], last = slices[i];
        const double middle = (first + last) * 0.5;
        const AxialWrapEdge* highest = nullptr;
        for (const auto& edge : edges) {
            if (middle < edge.first || middle > edge.last) continue;
            if (!highest || edge.value(middle) > highest->value(middle)) highest = &edge;
        }
        intervals.push_back({first, last, highest ? std::max(0.0, highest->value(first)) : 0.0,
            highest ? std::max(0.0, highest->value(last)) : 0.0, highest != nullptr});
    }
    return intervals;
}

MPoint axialWrapPoint(double position, double width, double height, const ShapeSettings& settings) {
    const auto radial = semicircleRadial(position * 2.0);
    return axialJoinedPoint(MPoint(width, radial.y * (0.5 + height), radial.x * (0.5 + height)),
        radial.y * 0.5, settings);
}

void appendAxialWrapFaces(PartBuilder& surface,
    const std::vector<AxialWrapInterval>& intervals, bool crest, const ShapeSettings& settings) {
    for (const auto& interval : intervals) {
        if (!interval.active) continue;
        const auto a = axialWrapPoint(interval.first, 0.0, 0.0, settings);
        const auto b = axialWrapPoint(interval.last, 0.0, 0.0, settings);
        if (crest) {
            surface.quad(a, b, axialWrapPoint(interval.last, 0.0, interval.lastHeight, settings),
                axialWrapPoint(interval.first, 0.0, interval.firstHeight, settings));
        } else {
            const auto firstSide = nativeAxis(0) * interval.firstHeight;
            const auto lastSide = nativeAxis(0) * interval.lastHeight;
            // 中央の母線を共有し、Arrow3Dの根元を面の内部へ浮かせない。
            surface.quad(a - firstSide, b - lastSide, b, a);
            surface.quad(a, b, b + lastSide, a + firstSide);
        }
    }
}

using AxialWrapSegments = std::vector<std::array<MPoint, 2>>;

void addAxialWrapSegment(AxialWrapSegments& segments, const MPoint& a, const MPoint& b) {
    if ((a - b).length() < 1e-10) return;
    for (const auto& segment : segments) {
        if (((a - segment[0]).length() < 1e-9 && (b - segment[1]).length() < 1e-9) ||
            ((a - segment[1]).length() < 1e-9 && (b - segment[0]).length() < 1e-9)) return;
    }
    segments.push_back({a, b});
}

void appendAxialWrapBoundary(AxialWrapSegments& segments,
    const std::vector<AxialWrapInterval>& intervals,
    const std::vector<AxialWrapSpoke>& spokes, bool crest, const ShapeSettings& settings) {
    if (intervals.empty()) return;
    const bool openArrow = !crest && !isWideArcOutline(outlinePresetIndex(settings.shape)) &&
        !settings.fill && settings.partShape <= 1;
    const auto point = [&](double position, double extent) {
        return crest ? axialWrapPoint(position, 0.0, extent, settings) : axialWrapPoint(position, extent, 0.0, settings);
    };
    for (const auto& interval : intervals) {
        if (!interval.active) continue;
        if (crest) {
            if (interval.firstHeight > 1e-12 || interval.lastHeight > 1e-12) {
                addAxialWrapSegment(segments, point(interval.first, interval.firstHeight),
                    point(interval.last, interval.lastHeight));
            }
        } else {
            addAxialWrapSegment(segments, point(interval.first, interval.firstHeight),
                point(interval.last, interval.lastHeight));
            if (interval.firstHeight > 1e-12 || interval.lastHeight > 1e-12) {
                addAxialWrapSegment(segments, point(interval.first, -interval.firstHeight),
                    point(interval.last, -interval.lastHeight));
            }
        }
    }
    for (std::size_t i = 0; i < intervals.size(); ++i) {
        const auto& previous = intervals[(i + intervals.size() - 1) % intervals.size()];
        const auto& next = intervals[i];
        const double before = previous.active ? previous.lastHeight : 0.0;
        const double after = next.active ? next.firstHeight : 0.0;
        const double low = std::min(before, after), high = std::max(before, after);
        if (!openArrow && high - low > 1e-12) {
            addAxialWrapSegment(segments, point(next.first, low), point(next.first, high));
            if (!crest) addAxialWrapSegment(segments, point(next.first, -low), point(next.first, -high));
        }
        double spokeHeight = high;
        for (const auto& spoke : spokes) {
            if (std::abs(spoke.position - next.first) < 1e-12) spokeHeight = std::max(spokeHeight, spoke.height);
        }
        if (spokeHeight - high > 1e-12) {
            addAxialWrapSegment(segments, point(next.first, high), point(next.first, spokeHeight));
            if (!crest) addAxialWrapSegment(segments, point(next.first, -high), point(next.first, -spokeHeight));
        }
    }
    if (openArrow) {
        // 薄線の矢印は根元を閉じず、円筒面の中央線を円周上の先端まで残す。
        for (const auto& interval : intervals) if (interval.active) {
            addAxialWrapSegment(segments, axialWrapPoint(interval.first, 0.0, 0.0, settings),
                axialWrapPoint(interval.last, 0.0, 0.0, settings));
        }
    }
}

void appendAxialWrapStrokes(PartBuilder& builder, AxialWrapSegments segments) {
    while (!segments.empty()) {
        std::vector<MPoint> stroke = {segments.back()[0], segments.back()[1]};
        segments.pop_back();
        while (true) {
            auto next = std::find_if(segments.begin(), segments.end(), [&](const auto& segment) {
                return (segment[0] - stroke.back()).length() < 1e-9 ||
                    (segment[1] - stroke.back()).length() < 1e-9;
            });
            if (next == segments.end()) break;
            stroke.push_back(((*next)[0] - stroke.back()).length() < 1e-9 ? (*next)[1] : (*next)[0]);
            segments.erase(next);
        }
        builder.stroke(stroke);
    }
}

PartGeometry makeAxialWrappedGeometry(const ShapeSettings& settings) {
    const auto data = makeAxialWrapData(settings);
    const auto main = axialWrapIntervals(data.slices, data.main);
    const auto crest = axialWrapIntervals(data.slices, data.crest);
    PartBuilder builder(settings.fill || settings.crossAxialJoinTop || settings.crossAxialJoinBottom);
    appendAxialWrapFaces(builder, main, false, settings);
    appendAxialWrapFaces(builder, crest, true, settings);
    AxialWrapSegments segments;
    appendAxialWrapBoundary(segments, main, data.spokes, false, settings);
    appendAxialWrapBoundary(segments, crest, data.crestSpokes, true, settings);
    appendAxialWrapStrokes(builder, std::move(segments));
    return std::move(builder.geometry);
}

std::vector<OptionClipVolume> axialWrappedPartClipVolumes(const ShapeSettings& settings) {
    const auto data = makeAxialWrapData(settings);
    PartBuilder parts(true);
    appendAxialWrapFaces(parts, axialWrapIntervals(data.slices, data.heads), false, settings);
    appendAxialWrapFaces(parts, axialWrapIntervals(data.slices, data.crest), true, settings);
    std::vector<OptionClipVolume> volumes;
    for (const auto& part : parts.geometry.fillParts) for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
        auto volume = optionPlanarVolume({part.triangles[i], part.triangles[i + 1], part.triangles[i + 2]});
        if (!volume.empty()) volumes.push_back(std::move(volume));
    }
    return volumes;
}
