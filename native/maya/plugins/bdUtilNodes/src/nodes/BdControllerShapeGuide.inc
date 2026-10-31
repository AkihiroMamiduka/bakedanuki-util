// 本体座標で中央ガイドを作り、既存の輪郭と同一直線の重複区間を除く。
bool isGuideShape(short outline) {
    switch (outline) {
        case 6: case 8: case 19: case 24: case 25: case 33:
        case 36: case 41: case 43: case 46: case 50: case 51:
        case 79: case 104: case 106: case 110: case 116:
        case 117: case 118: case 119:
            return true;
        default:
            return false;
    }
}

void appendGuideSegment(PartGeometry& geometry, const MPoint& endpoint, StrokeStyle style,
    const MPoint& start = MPoint::origin) {
    const MVector direction = endpoint - start;
    const double squared = direction * direction;
    if (squared < 1e-20) return;
    std::vector<std::array<double, 2>> remaining = {{{0.0, 1.0}}};
    for (const auto& stroke : geometry.strokes) {
        for (unsigned int i = 1; i < stroke.length() && !remaining.empty(); ++i) {
            const MVector first = stroke[i - 1] - start;
            const MVector last = stroke[i] - start;
            const double a = (first * direction) / squared;
            const double b = (last * direction) / squared;
            if ((first - direction * a).length() > 1e-9 ||
                (last - direction * b).length() > 1e-9) continue;
            const double low = std::max(0.0, std::min(a, b));
            const double high = std::min(1.0, std::max(a, b));
            if (high - low < 1e-10) continue;
            std::vector<std::array<double, 2>> outside;
            for (const auto& interval : remaining) {
                const double enter = std::max(interval[0], low);
                const double leave = std::min(interval[1], high);
                if (leave - enter < 1e-10) {
                    outside.push_back(interval);
                    continue;
                }
                if (enter - interval[0] > 1e-10) outside.push_back({interval[0], enter});
                if (interval[1] - leave > 1e-10) outside.push_back({leave, interval[1]});
            }
            remaining = std::move(outside);
        }
        if (remaining.empty()) break;
    }
    for (const auto& interval : remaining) {
        Stroke stroke;
        stroke.append(start + direction * interval[0]);
        stroke.append(start + direction * interval[1]);
        geometry.strokes.push_back(std::move(stroke));
        geometry.strokeStyles.push_back(style);
    }
}

double guideBodyFraction(const MVector& direction, const GuideBodyGeometry& body) {
    std::vector<std::array<double, 2>> intervals;
    for (const auto& volume : body.volumes) {
        double enter = 0.0;
        double leave = 1.0;
        for (const auto& plane : volume) {
            const double slope = direction * plane.normal;
            if (std::abs(slope) < 1e-12) {
                if (plane.distance < -1e-10) { leave = -1.0; break; }
            } else if (slope > 0) leave = std::min(leave, plane.distance / slope);
            else enter = std::max(enter, plane.distance / slope);
        }
        if (leave - enter > 1e-10) intervals.push_back({enter, leave});
    }
    if (body.volumes.empty()) {
        const double squared = direction * direction;
        for (const auto& stroke : body.strokes) for (unsigned int i = 1; i < stroke.length(); ++i) {
            const MVector first = stroke[i - 1] - MPoint::origin;
            const MVector last = stroke[i] - MPoint::origin;
            const double a = (first * direction) / squared;
            const double b = (last * direction) / squared;
            if ((first - direction * a).length() < 1e-9 &&
                (last - direction * b).length() < 1e-9) {
                intervals.push_back({std::max(0.0, std::min(a, b)), std::min(1.0, std::max(a, b))});
            }
        }
    }
    std::sort(intervals.begin(), intervals.end());
    double end = 0.0;
    for (const auto& interval : intervals) {
        if (interval[0] > end + 1e-10) break;
        end = std::max(end, interval[1]);
    }
    return end;
}

void appendShapeGuide(const ShapeSettings& settings, PartGeometry& geometry,
    const GuideBodyGeometry& body) {
    const short outline = outlinePresetIndex(settings.shape);
    if (!settings.guideLine || !isGuideShape(outline)) return;
    const bool colored = outline == 46 || outline == 50 || outline == 51 || outline == 119;
    const auto styleFor = [&](unsigned int axis, double distance) {
        if (settings.guideLineTemplate) return StrokeStyle::Template;
        return colored && distance > 0 ? kAxisStyles[axis] : StrokeStyle::Normal;
    };
    const auto addAxis = [&](unsigned int axis, double distance) {
        if (std::abs(distance) < 1e-10) return;
        // Wideの腕はPartによる短縮後の本体内に収め、Finの高さには追従しない。
        if (outline == 104 || outline == 106 || outline == 118 || outline == 119) {
            distance *= guideBodyFraction(nativeAxis(axis) * distance, body);
        }
        appendGuideSegment(geometry, MPoint::origin + nativeAxis(axis) * distance,
            styleFor(axis, distance));
    };
    const auto addPair = [&](unsigned int axis, double extent) {
        addAxis(axis, -extent);
        addAxis(axis, extent);
    };
    const auto addArrowTips = [&] {
        if (!settings.part || settings.partShape > 1) return;
        MPoint start = MPoint::origin;
        if (outline == 104) {
            if (body.strokes.empty()) return;
            double minimum = body.strokes.front()[0].x;
            double maximum = minimum;
            for (const auto& stroke : body.strokes) for (const auto& point : stroke) {
                minimum = std::min(minimum, point.x);
                maximum = std::max(maximum, point.x);
            }
            // 帯全体が原点の片側へ移った場合も、接続線を本体とPartの範囲に収める。
            start.x = std::clamp(0.0, minimum, maximum);
        }
        for (const auto& site : optionPartSites(settings)) {
            const double tip = site.attached ? 0.125 * site.sizeScale * partLength(settings) : 0.0;
            const auto endpoint = site.endpoint + site.along * (tip + settings.partOffset);
            appendGuideSegment(geometry, endpoint,
                settings.guideLineTemplate ? StrokeStyle::Template : StrokeStyle::Normal, start);
        }
    };
    if (outline == 6) {
        if (geometry.strokes.empty()) return;
        const Stroke triangle = geometry.strokes.front();
        for (const auto& vertex : triangle) {
            appendGuideSegment(geometry, vertex,
                settings.guideLineTemplate ? StrokeStyle::Template : StrokeStyle::Normal);
        }
        return;
    }
    if (outline == 8 || outline == 110) {
        const auto sites = settings.part && settings.partShape <= 1
            ? optionPartSites(settings) : std::vector<OptionSite>{};
        for (unsigned int axis : {1u, 2u}) for (double sign : {-1.0, 1.0}) {
            const MVector direction = nativeAxis(axis) * sign;
            double extent = 0.5;
            for (const auto& site : sites) {
                if ((site.along - direction).length() > 1e-10) continue;
                const double tip = (site.endpoint - MPoint::origin) * direction +
                    0.125 * site.sizeScale * partLength(settings) + settings.partOffset;
                extent = std::max(extent, tip);
            }
            addAxis(axis, sign * extent);
        }
        return;
    }
    if (outline == 79 || outline == 116 || outline == 117) {
        const double extent = outline == 117
            ? std::max(0.0, 0.5 - settings.wideWidth * 0.5) : 0.5;
        addPair(1, extent);
        addPair(2, extent);
        if (outline == 116) addArrowTips();
        return;
    }
    if (outline == 104 || outline == 106) {
        const double halfWidth = settings.wideWidth * 0.5;
        const double extent = outline == 106 ? std::max(0.5, halfWidth) : 0.5;
        addPair(0, extent);
        addPair(2, outline == 106 ? extent : halfWidth);
        addArrowTips();
        return;
    }
    if (outline == 25) {
        addAxis(0, -0.5);
        addAxis(0, 0.5 * partLength(settings) + settings.partOffset);
        addPair(1, 0.5 * std::abs(partHeight(settings)));
        addPair(2, 0.5 * std::abs(partWidth(settings)));
        return;
    }
    const double extent = outline == 118 || outline == 119
        ? std::max(0.5, settings.wideWidth * 0.5) : 0.5;
    addPair(0, extent);
    addPair(1, outline == 41 || outline == 43 ? 0.25 : extent);
    addPair(2, outline == 41 || outline == 43 ? 0.25 : extent);
}
