// 円周上の弧長と半径方向の幅から主面を作り、立ち上がりを円平面の法線へ向ける。
struct RadialWrapData {
    AxialWrapData profile;
};

bool radialWrapWide(const ShapeSettings& settings) {
    const short outline = outlinePresetIndex(settings.shape);
    return outline == 111 || crossCircleBaseOutline(outline) == 111;
}

void appendRadialWrapLevelCuts(std::vector<double>& cuts,
    const std::vector<AxialWrapEdge>& edges, double level) {
    for (const auto& edge : edges) {
        const double a = edge.firstHeight - level, b = edge.lastHeight - level;
        if ((a < -1e-12 && b > 1e-12) || (a > 1e-12 && b < -1e-12)) {
            cuts.push_back(edge.first + (edge.last - edge.first) * (a / (a - b)));
        }
    }
}

RadialWrapData makeRadialWrapData(const ShapeSettings& settings) {
    RadialWrapData data;
    auto source = settings;
    const bool wide = radialWrapWide(settings);
    source.wideWidth = wide ? std::max(0.0, settings.wideWidth) : 0.0;
    data.profile = makeAxialWrapData(source);
    if (data.profile.slices.empty()) return data;
    // 内周が中心へ達する位置も輪郭と面で共有する。
    appendRadialWrapLevelCuts(data.profile.slices, data.profile.main, 0.5);
    std::sort(data.profile.slices.begin(), data.profile.slices.end());
    data.profile.slices.erase(std::unique(data.profile.slices.begin(), data.profile.slices.end(),
        [](double a, double b) { return std::abs(a - b) < 1e-12; }), data.profile.slices.end());
    return data;
}

MPoint radialWrapPoint(double position, double radius, double height = 0.0) {
    const auto radial = semicircleRadial(position * 2.0);
    return MPoint(height, radial.y * std::max(0.0, radius), radial.x * std::max(0.0, radius));
}

void appendRadialWrapFaces(PartBuilder& surface,
    const std::vector<AxialWrapInterval>& intervals, bool crest, const ShapeSettings& settings) {
    for (std::size_t i = 0; i < intervals.size(); ++i) {
        const auto& interval = intervals[i];
        if (!interval.active) continue;
        const auto a = radialWrapPoint(interval.first, 0.5);
        const auto b = radialWrapPoint(interval.last, 0.5);
        if (crest) {
            const double sign = partHeight(settings) < 0.0 ? -1.0 : 1.0;
            surface.quad(a, b, radialWrapPoint(interval.last, 0.5, interval.lastHeight * sign),
                radialWrapPoint(interval.first, 0.5, interval.firstHeight * sign));
        } else {
            const double firstInner = std::max(0.0, 0.5 - interval.firstHeight);
            const double lastInner = std::max(0.0, 0.5 - interval.lastHeight);
            // 半径0.5を共有辺にし、追加面の根元と主面を同じ頂点でつなぐ。
            surface.quad(radialWrapPoint(interval.first, firstInner),
                radialWrapPoint(interval.last, lastInner), b, a);
            surface.quad(a, b, radialWrapPoint(interval.last, 0.5 + interval.lastHeight),
                radialWrapPoint(interval.first, 0.5 + interval.firstHeight));
        }
    }
}

void appendRadialWrapBoundary(AxialWrapSegments& segments,
    const std::vector<AxialWrapInterval>& intervals,
    const std::vector<AxialWrapSpoke>& spokes,
    bool crest, bool openArrow, const ShapeSettings& settings) {
    if (intervals.empty()) return;
    const double sign = partHeight(settings) < 0.0 ? -1.0 : 1.0;
    const auto point = [&](double position, double extent) {
        return crest ? radialWrapPoint(position, 0.5, extent * sign)
            : radialWrapPoint(position, 0.5 + extent);
    };
    for (std::size_t i = 0; i < intervals.size(); ++i) {
        const auto& interval = intervals[i];
        if (!interval.active) continue;
        if (crest) {
            if (interval.firstHeight > 1e-12 || interval.lastHeight > 1e-12) {
                addAxialWrapSegment(segments, point(interval.first, interval.firstHeight),
                    point(interval.last, interval.lastHeight));
            }
        } else {
            addAxialWrapSegment(segments, point(interval.first, interval.firstHeight),
                point(interval.last, interval.lastHeight));
            if (interval.firstHeight <= 1e-12 && interval.lastHeight <= 1e-12) continue;
            addAxialWrapSegment(segments, point(interval.first, -interval.firstHeight),
                point(interval.last, -interval.lastHeight));
        }
    }
    for (std::size_t i = 0; i < intervals.size(); ++i) {
        const auto previousIndex = (i + intervals.size() - 1) % intervals.size();
        const auto& previous = intervals[previousIndex];
        const auto& next = intervals[i];
        const double before = previous.active ? previous.lastHeight : 0.0;
        const double after = next.active ? next.firstHeight : 0.0;
        const double low = std::min(before, after), high = std::max(before, after);
        if (!openArrow && high - low > 1e-12) {
            addAxialWrapSegment(segments, point(next.first, low), point(next.first, high));
            if (!crest) {
                addAxialWrapSegment(segments, point(next.first, -low), point(next.first, -high));
            }
        }
        double spokeHeight = high;
        for (const auto& spoke : spokes) {
            if (std::abs(spoke.position - next.first) < 1e-12) spokeHeight = std::max(spokeHeight, spoke.height);
        }
        if (spokeHeight - high > 1e-12) {
            addAxialWrapSegment(segments, point(next.first, high), point(next.first, spokeHeight));
            if (!crest) {
                addAxialWrapSegment(segments, point(next.first, -high), point(next.first, -spokeHeight));
            }
        }
    }
    if (openArrow) {
        // 開いた矢印の軸線も直線へ戻さず、同じ円周の弧として先端まで残す。
        for (const auto& interval : intervals) if (interval.active) {
            addAxialWrapSegment(segments, radialWrapPoint(interval.first, 0.5),
                radialWrapPoint(interval.last, 0.5));
        }
    }
}

PartGeometry makeRadialWrappedGeometry(const ShapeSettings& settings) {
    const auto data = makeRadialWrapData(settings);
    const auto main = axialWrapIntervals(data.profile.slices, data.profile.main);
    const auto crest = axialWrapIntervals(data.profile.slices, data.profile.crest);
    PartBuilder builder(settings.fill);
    appendRadialWrapFaces(builder, main, false, settings);
    appendRadialWrapFaces(builder, crest, true, settings);
    AxialWrapSegments segments;
    const bool openArrow = !radialWrapWide(settings) && !settings.fill && settings.partShape <= 1;
    appendRadialWrapBoundary(segments, main, data.profile.spokes, false, openArrow, settings);
    appendRadialWrapBoundary(segments, crest, data.profile.crestSpokes, true, false, settings);
    appendAxialWrapStrokes(builder, std::move(segments));
    return std::move(builder.geometry);
}

std::vector<OptionClipVolume> radialWrappedPartClipVolumes(const ShapeSettings& settings) {
    const auto data = makeRadialWrapData(settings);
    PartBuilder parts(true);
    appendRadialWrapFaces(parts, axialWrapIntervals(data.profile.slices, data.profile.heads), false, settings);
    appendRadialWrapFaces(parts, axialWrapIntervals(data.profile.slices, data.profile.crest), true, settings);
    std::vector<OptionClipVolume> volumes;
    for (const auto& part : parts.geometry.fillParts) for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
        auto volume = optionPlanarVolume({part.triangles[i], part.triangles[i + 1], part.triangles[i + 2]});
        if (!volume.empty()) volumes.push_back(std::move(volume));
    }
    return volumes;
}
