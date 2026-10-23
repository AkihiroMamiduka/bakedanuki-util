// 本体と部品を独立した設定から作り、最後に共通座標で接合する。
struct OptionClipPlane {
    MVector normal;
    double distance;
    double value(const MPoint& point) const { return (point - MPoint::origin) * normal - distance; }
};

using OptionClipVolume = std::vector<OptionClipPlane>;

void addOptionClipPlane(OptionClipVolume& volume, MVector normal, const MPoint& point, const MPoint& inside) {
    if (normal.length() < 1e-12) return;
    normal.normalize();
    if ((inside - point) * normal > 0) normal = -normal;
    const double distance = (point - MPoint::origin) * normal;
    for (const auto& plane : volume) {
        if ((plane.normal - normal).length() < 1e-9 && std::abs(plane.distance - distance) < 1e-9) return;
    }
    volume.push_back({normal, distance});
}

OptionClipVolume optionPlanarVolume(const std::vector<MPoint>& points) {
    OptionClipVolume volume;
    if (points.size() < 3) return volume;
    MVector normal;
    MPoint center;
    for (std::size_t i = 0; i < points.size(); ++i) {
        normal += (points[i] - points[0]) ^ (points[(i + 1) % points.size()] - points[0]);
        center += (points[i] - MPoint::origin) / static_cast<double>(points.size());
    }
    if (normal.length() < 1e-12) return volume;
    normal.normalize();
    for (std::size_t i = 0; i < points.size(); ++i) {
        addOptionClipPlane(volume, (points[(i + 1) % points.size()] - points[i]) ^ normal, points[i], center);
    }
    const double distance = (points[0] - MPoint::origin) * normal;
    volume.push_back({normal, distance});
    volume.push_back({-normal, -distance});
    return volume;
}

PartPolygons outsideOptionVolume(std::vector<MPoint> polygon, const OptionClipVolume& volume, bool keepCoincident = false) {
    if (keepCoincident && polygon.size() >= 3) {
        const auto normal = (polygon[1] - polygon[0]) ^ (polygon[2] - polygon[0]);
        for (const auto& plane : volume) {
            if (normal * plane.normal <= 0) continue;
            if (std::all_of(polygon.begin(), polygon.end(), [&](const MPoint& p) { return std::abs(plane.value(p)) < 1e-10; })) return {std::move(polygon)};
        }
    }
    for (const auto& plane : volume) {
        bool outside = true;
        for (const auto& p : polygon) outside = outside && plane.value(p) > 1e-10;
        if (outside) return {std::move(polygon)};
    }
    PartPolygons result;
    for (const auto& plane : volume) {
        if (polygon.empty()) break;
        std::vector<MPoint> inside;
        std::vector<MPoint> outside;
        bool positive = false;
        for (std::size_t i = 0; i < polygon.size(); ++i) {
            const auto a = polygon[i];
            const auto b = polygon[(i + 1) % polygon.size()];
            double da = plane.value(a);
            double db = plane.value(b);
            if (std::abs(da) < 1e-10) da = 0;
            if (std::abs(db) < 1e-10) db = 0;
            positive = positive || da > 0;
            if (da <= 0) inside.push_back(a);
            if (da >= 0) outside.push_back(a);
            if ((da < 0 && db > 0) || (da > 0 && db < 0)) {
                const auto p = a + (b - a) * (da / (da - db));
                inside.push_back(p);
                outside.push_back(p);
            }
        }
        if (positive && outside.size() >= 3) result.push_back(std::move(outside));
        polygon = std::move(inside);
    }
    return result;
}

void trimOptionGeometry(PartGeometry& geometry, const std::vector<OptionClipVolume>& volumes, bool filled, bool keepCoincident = false) {
    if (volumes.empty()) return;
    PartBuilder trimmed(filled);
    for (std::size_t strokeIndex = 0; strokeIndex < geometry.strokes.size(); ++strokeIndex) {
        const auto style = geometry.strokeStyles[strokeIndex];
        const auto& stroke = geometry.strokes[strokeIndex];
        for (unsigned int i = 1; i < stroke.length(); ++i) {
            std::vector<std::array<MPoint, 2>> segments = {{{stroke[i - 1], stroke[i]}}};
            for (const auto& volume : volumes) {
                std::vector<std::array<MPoint, 2>> next;
                for (const auto& segment : segments) {
                    if (keepCoincident && std::any_of(volume.begin(), volume.end(),
                        [&](const OptionClipPlane& plane) {
                            return std::abs(plane.value(segment[0])) < 1e-10 &&
                                std::abs(plane.value(segment[1])) < 1e-10;
                        })) {
                        next.push_back(segment);
                        continue;
                    }
                    double enter = 0, leave = 1;
                    bool intersects = true;
                    for (const auto& plane : volume) {
                        const double a = plane.value(segment[0]);
                        const double b = plane.value(segment[1]);
                        const double delta = b - a;
                        if (std::abs(delta) < 1e-14) {
                            if (a > 1e-10) { intersects = false; break; }
                        } else if (delta > 0) leave = std::min(leave, -a / delta);
                        else enter = std::max(enter, -a / delta);
                        if (leave < enter) { intersects = false; break; }
                    }
                    const auto point = [&](double t) { return segment[0] + (segment[1] - segment[0]) * t; };
                    if (!intersects) next.push_back(segment);
                    else {
                        if (enter > 1e-10) next.push_back({segment[0], point(enter)});
                        if (leave < 1 - 1e-10) next.push_back({point(leave), segment[1]});
                    }
                }
                segments = std::move(next);
            }
            for (const auto& segment : segments) {
                if ((segment[1] - segment[0]).length() > 1e-10) trimmed.stroke({segment[0], segment[1]}, style);
            }
        }
    }
    for (const auto& part : geometry.fillParts) {
        PartBuilder faces(filled);
        for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
            PartPolygons pieces = {{part.triangles[i], part.triangles[i + 1], part.triangles[i + 2]}};
            for (const auto& volume : volumes) {
                PartPolygons next;
                for (const auto& piece : pieces) {
                    for (auto& p : outsideOptionVolume(piece, volume, keepCoincident)) next.push_back(std::move(p));
                }
                pieces = std::move(next);
            }
            for (const auto& piece : pieces) faces.polygon(piece, part.style);
        }
        for (auto& face : faces.geometry.fillParts) {
            face.marker = part.marker;
            face.singleSided = part.singleSided;
            trimmed.geometry.fillParts.push_back(std::move(face));
        }
    }
    geometry = std::move(trimmed.geometry);
}

void mergeOptionGeometry(PartGeometry& target, PartGeometry source) {
    for (std::size_t i = 0; i < source.strokes.size(); ++i) {
        target.strokes.push_back(std::move(source.strokes[i]));
        target.strokeStyles.push_back(source.strokeStyles[i]);
    }
    for (auto& part : source.fillParts) target.fillParts.push_back(std::move(part));
}

OptionClipVolume optionSolidVolume(const PartGeometry& geometry) {
    MPoint inside;
    double count = 0;
    for (const auto& part : geometry.fillParts) for (const auto& p : part.triangles) {
        inside += p - MPoint::origin;
        count += 1;
    }
    if (count == 0) return {};
    inside = MPoint::origin + (inside - MPoint::origin) / count;
    OptionClipVolume volume;
    for (const auto& part : geometry.fillParts) for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
        const auto a = part.triangles[i], b = part.triangles[i + 1], c = part.triangles[i + 2];
        addOptionClipPlane(volume, (b - a) ^ (c - a), a, inside);
    }
    return volume.size() >= 4 ? volume : OptionClipVolume{};
}

void trimOptionStrokes(PartGeometry& geometry, const std::vector<OptionClipVolume>& volumes) {
    auto faces = std::move(geometry.fillParts);
    trimOptionGeometry(geometry, volumes, false);
    geometry.fillParts = std::move(faces);
}

bool optionPartSupported(short outline) {
    return outline == 1 || outline == 4 || outline == 5 || outline == 8 || outline == 19 ||
        outline == 27 || outline == 33 || outline == 45 || outline == 46 || outline == 47 ||
        outline == 52 || outline == 53 || (outline >= 104 && outline <= 111);
}

short optionNarrowOutline(short outline) {
    if (outline == 104) return 1;
    if (outline == 105) return 52;
    if (outline == 106) return 53;
    if (outline == 107) return 4;
    return outline;
}

bool optionWideOutline(short outline) { return outline >= 104 && outline <= 107; }

struct OptionSite {
    MPoint endpoint;
    MVector along;
    MVector side;
    bool attached = false;
    double arrowSize = 1.0;
};

std::vector<OptionSite> optionPartSites(const ShapeSettings& settings) {
    const short outline = outlinePresetIndex(settings.shape);
    if (!settings.part || !optionPartSupported(outline)) return {};
    const bool all = settings.partType == 1;
    std::vector<OptionSite> sites;
    const auto add = [&](MVector along, MVector side, bool attached, double arrowSize = 1.0) {
        sites.push_back({MPoint::origin + along * 0.5, along, side, attached, arrowSize});
    };
    if (outline == 27 || outline == 111) {
        const double sweep = std::clamp(settings.circleAngle, 0.0, 2.0 * kPi);
        if (sweep < 1e-12) return sites;
        if (settings.partType == 2) { add(nativeAxis(1), nativeAxis(2), true); return sites; }
        const double start = 0.5 * (kPi - sweep);
        const double end = 0.5 * (kPi + sweep);
        for (double angle : all ? std::vector<double>{start, end} : std::vector<double>{start}) {
            const bool first = angle == start;
            const auto radial = semicircleRadial(angle);
            const auto tangent = semicircleOutward(angle, first);
            const MVector direction = nativeAxis(2) * tangent.x + nativeAxis(1) * tangent.y;
            const MVector side = nativeAxis(2) * radial.x + nativeAxis(1) * radial.y;
            sites.push_back({MPoint::origin + side * 0.5, direction, side, false});
        }
        return sites;
    }
    if (outline == 8 || outline == 108 || outline == 109 || outline == 110) {
        add(nativeAxis(1), nativeAxis(2), true);
        if (all) {
            add(-nativeAxis(1), -nativeAxis(2), true, 0.5);
            add(nativeAxis(2), -nativeAxis(1), true, 0.5);
            add(-nativeAxis(2), nativeAxis(1), true, 0.5);
        }
        return sites;
    }
    if (outline == 19 || outline == 33 || outline == 46 || outline == 47) {
        add(nativeAxis(0), -nativeAxis(2), true);
        if (all) {
            add(-nativeAxis(0), nativeAxis(2), true);
            add(nativeAxis(1), nativeAxis(2), true);
            add(-nativeAxis(1), -nativeAxis(2), true);
            add(nativeAxis(2), nativeAxis(0), true);
            add(-nativeAxis(2), -nativeAxis(0), true);
        }
        return sites;
    }
    const short base = optionNarrowOutline(outline);
    const auto axes = base == 5 || base == 45 ? std::vector<unsigned int>{0, 1, 2} : straightLineAxes(base);
    for (auto axis : axes) {
        const auto other = axes.size() == 2 ? (axis == axes[0] ? axes[1] : axes[0]) : (axis + 1) % 3;
        add(nativeAxis(axis), nativeAxis(other), false);
        if (!all) break;
        add(-nativeAxis(axis), nativeAxis(other), false);
    }
    return sites;
}

struct OptionHeads {
    PartGeometry geometry;
    std::vector<OptionClipVolume> volumes;
    std::vector<double> stops;
};

OptionHeads makeOptionHeads(const ShapeSettings& settings) {
    OptionHeads result;
    std::vector<std::vector<MPoint>> signatures;
    const short outline = outlinePresetIndex(settings.shape);
    const bool round = outline == 27 || outline == 33 || outline == 46 || outline == 47 || outline == 111;
    for (const auto& site : optionPartSites(settings)) {
        PartBuilder head(settings.fill);
        const auto volumeStart = result.volumes.size();
        MVector up = site.along ^ site.side;
        // 主平面の法線は基準軸に平行。両端とも同じ軸の正側へ立ち上げる。
        if (settings.partShape == 1 && up.x + up.y + up.z < 0) up = -up;
        const auto point = [&](const MPoint& p) {
            return site.endpoint + site.along * (p.x * partLength(settings) + settings.partOffset)
                + site.side * (p.y * partWidth(settings)) + up * (p.z * partWidth(settings));
        };
        double stop = 1e100;
        const auto remember = [&](const MPoint& p) { stop = std::min(stop, (p - MPoint::origin) * site.along); };
        const auto planarPoints = [&](const std::vector<MPoint>& points, bool open) {
            for (const auto& p : points) remember(p);
            auto stroke = points;
            if (!open) stroke.push_back(stroke.front());
            head.stroke(stroke);
            head.polygon(points);
            auto volume = optionPlanarVolume(points);
            if (!volume.empty()) result.volumes.push_back(std::move(volume));
        };
        const auto planar = [&](const std::vector<MPoint>& profile, bool open) {
            std::vector<MPoint> points;
            for (const auto& p : profile) points.push_back(point(p));
            planarPoints(points, open);
        };
        if (settings.partShape <= 1) {
            const double depth = (site.attached ? 0.125 * site.arrowSize : 0.1 * std::cos(kPi / 6.0));
            const double width = site.attached ? (outline == 19 || outline == 8 || (outline >= 108 && outline <= 110) ? 0.072 : 0.075) * site.arrowSize : 0.05;
            const double shoulder = site.attached ? (round ? -0.004903810568 * site.arrowSize : 0.0) : -depth;
            const double tip = site.attached ? depth : 0.0;
            if (site.attached) {
                const double rootWidth = std::clamp(width * partWidth(settings), -0.5, 0.5);
                const double rootY = round ? partSurfaceY(partRoundSection(), rootWidth) : 0.0;
                planarPoints({site.endpoint + site.side * rootWidth + site.along * rootY,
                    point(MPoint(shoulder, width, 0)), point(MPoint(tip, 0, 0)), point(MPoint(shoulder, -width, 0)),
                    site.endpoint - site.side * rootWidth + site.along * rootY}, true);
            } else planar({MPoint(shoulder, width, 0), MPoint(tip, 0, 0), MPoint(shoulder, -width, 0)},
                    !optionWideOutline(outline) && outline != 111);
            if (settings.partShape == 1) {
                if (site.attached) {
                    planar({MPoint(0, 0, 0), MPoint(0, 0, 0.0625 * site.arrowSize), MPoint(tip, 0, 0)}, true);
                } else {
                    planar({MPoint(shoulder, 0, 0), MPoint(shoulder, 0, width), MPoint(tip, 0, 0)}, true);
                }
            }
        } else if (settings.partShape <= 5) {
            const unsigned int kind = settings.partShape == 2 ? 3 : settings.partShape - 3;
            std::vector<MPoint> profile;
            for (const auto& p : planarEndProfile(kind)) profile.emplace_back(0.1 * p.x + (kind == 3 ? (site.attached ? 0.05 : -0.05) : 0), 0.1 * p.y, 0);
            planar(profile, false);
        } else {
            constexpr std::array<short, 5> outlines = {19, 24, 33, 41, 43};
            ShapeSettings component;
            component.shape = partPreset(outlines[settings.partShape - 6]);
            component.fill = settings.fill && partLength(settings) != 0.0 && partWidth(settings) != 0.0;
            std::vector<StrokeStyle> styles;
            const auto strokes = makeStrokes(ShapeTransform(component), styles);
            component.fill = true;
            const auto sourceParts = makeFillParts(ShapeTransform(component));
            head.singleSided = true;
            const auto mapped = [&](const MPoint& p) {
                return point(MPoint(0.1 * p.x + (settings.partShape >= 9 ? (site.attached ? 0.05 : -0.05) : 0), 0.1 * p.y, 0.1 * p.z));
            };
            for (const auto& stroke : strokes) {
                std::vector<MPoint> points;
                for (const auto& p : stroke) { points.push_back(mapped(p)); remember(points.back()); }
                head.stroke(points);
            }
            MPoint inside;
            double count = 0;
            for (const auto& part : sourceParts) for (const auto& p : part.triangles) {
                const auto position = mapped(p);
                remember(position);
                inside += position - MPoint::origin;
                count += 1;
            }
            if (count != 0) inside = MPoint::origin + (inside - MPoint::origin) / count;
            OptionClipVolume volume;
            for (const auto& part : sourceParts) for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
                const auto a = mapped(part.triangles[i]);
                auto b = mapped(part.triangles[i + 1]);
                auto c = mapped(part.triangles[i + 2]);
                if (((b - a) ^ (c - a)) * (a - inside) < 0) std::swap(b, c);
                if (partLength(settings) != 0.0 && partWidth(settings) != 0.0) head.triangle(a, b, c);
                addOptionClipPlane(volume, (b - a) ^ (c - a), a, inside);
            }
            if (volume.size() >= 4) result.volumes.push_back(std::move(volume));
        }
        result.stops.push_back(stop == 1e100 ? 0.5 : stop);
        std::vector<MPoint> signature;
        for (const auto& stroke : head.geometry.strokes) for (const auto& p : stroke) signature.push_back(p);
        bool duplicate = false;
        for (const auto& previous : signatures) {
            if (previous.size() != signature.size()) continue;
            duplicate = std::all_of(signature.begin(), signature.end(), [&](const MPoint& p) {
                return std::any_of(previous.begin(), previous.end(), [&](const MPoint& q) { return (p - q).length() < 1e-9; });
            });
            if (duplicate) break;
        }
        if (duplicate) { result.volumes.resize(volumeStart); continue; }
        signatures.push_back(std::move(signature));
        if (volumeStart != 0) {
            const std::vector<OptionClipVolume> previous(result.volumes.begin(), result.volumes.begin() + volumeStart);
            const std::vector<OptionClipVolume> current(result.volumes.begin() + volumeStart, result.volumes.end());
            if (settings.partShape >= 6) trimOptionGeometry(result.geometry, current, settings.fill);
            else trimOptionStrokes(result.geometry, current);
            trimOptionGeometry(head.geometry, previous, settings.fill, settings.partShape >= 6);
        }
        mergeOptionGeometry(result.geometry, std::move(head.geometry));
    }
    return result;
}

std::vector<OptionClipVolume> optionPartClipVolumes(const ShapeSettings& settings) {
    return makeOptionHeads(settings).volumes;
}

void appendOptionSquare(PartBuilder& builder, short outline) {
    const PartPlane plane{MPoint::origin, nativeAxis(2), nativeAxis(1)};
    const auto style = outline == 110 ? StrokeStyle::Template : StrokeStyle::Normal;
    builder.polygon(plane.points({MPoint(-0.5, -0.5, 0), MPoint(0.5, -0.5, 0), MPoint(0.5, 0.5, 0), MPoint(-0.5, 0.5, 0)}), style);
    for (unsigned int axis = 0; axis < 4; ++axis) {
        const double angle = axis * kPi / 2;
        const MVector along = nativeAxis(1) * std::cos(angle) - nativeAxis(2) * std::sin(angle);
        const MVector side = nativeAxis(2) * std::cos(angle) + nativeAxis(1) * std::sin(angle);
        const auto p = [&](double value) { return MPoint::origin + along * 0.5 + side * value; };
        if (outline == 110) {
            builder.stroke({p(-0.5), p(-0.15)}, StrokeStyle::Template);
            builder.stroke({p(-0.15), p(0.15)});
            builder.stroke({p(0.15), p(0.5)}, StrokeStyle::Template);
        } else builder.stroke({p(-0.5), p(0.5)});
    }
    if (outline == 108 || outline == 109) {
        const auto crossStyle = outline == 109 ? StrokeStyle::Template : StrokeStyle::Normal;
        builder.stroke({MPoint(0, -0.5, 0), MPoint(0, 0.5, 0)}, crossStyle);
        builder.stroke({MPoint(0, 0, -0.5), MPoint(0, 0, 0.5)}, crossStyle);
    }
}

void appendOptionCircle(PartBuilder& builder, const ShapeSettings& settings,
    const OptionHeads& heads, const std::vector<OptionSite>& sites,
    std::vector<OptionClipVolume>& bodyVolumes) {
    const double sweep = std::clamp(settings.circleAngle, 0.0, 2.0 * kPi);
    if (sweep < 1e-12) return;
    const bool wideBase = outlinePresetIndex(settings.shape) == 111;
    const bool wide = wideBase && settings.wideWidth > 1e-12;
    const double start = (kPi - sweep) * 0.5;
    const double end = (kPi + sweep) * 0.5;
    const double outer = wide ? 0.5 + settings.wideWidth * 0.5 : 0.5;
    const double inner = wide ? std::max(0.0, 0.5 - settings.wideWidth * 0.5) : 0;
    const auto angles = semicircleSampleAngles(start, end);
    std::vector<MPoint> outerPoints, innerPoints;
    for (double angle : angles) {
        outerPoints.push_back(kSemicirclePlane.point(MPoint::origin + semicircleRadial(angle) * outer));
        innerPoints.push_back(kSemicirclePlane.point(MPoint::origin + semicircleRadial(angle) * inner));
    }
    PartBuilder arc(true);
    for (std::size_t i = 1; i < angles.size(); ++i) {
        if (wide) arc.quad(outerPoints[i - 1], outerPoints[i], innerPoints[i], innerPoints[i - 1]);
        else arc.triangle(MPoint::origin, outerPoints[i - 1], outerPoints[i]);
    }
    if (!wide) {
        builder.stroke(outerPoints);
        if (builder.filled && !wideBase) builder.geometry.fillParts = std::move(arc.geometry.fillParts);
        for (std::size_t i = 0; i < sites.size(); ++i) {
            if (sites[i].attached) continue;
            const bool openArrow = !settings.fill && settings.partShape <= 1 && !wideBase;
            const double stop = openArrow ? settings.partOffset : heads.stops[i];
            if ((openArrow && std::abs(stop) > 1e-12) || stop > 1e-12) {
                builder.stroke({sites[i].endpoint, sites[i].endpoint + sites[i].along * stop});
            }
        }
        return;
    }
    // 帯の幅を維持し、円弧と移動後の頭部を同じ断面で接続する。
    for (std::size_t i = 0; i < sites.size(); ++i) {
        const auto& site = sites[i];
        if (site.attached) continue;
        const double stop = heads.stops[i];
        const double maxDepth = std::sqrt(std::max(0.0, outer * outer - 0.25));
        const double cut = std::clamp(stop, -maxDepth, 0.0);
        if (cut < -1e-12) {
            const auto at = site.endpoint + site.along * cut;
            const OptionClipVolume clip = {
                {-site.along, -(at - MPoint::origin) * site.along},
                {site.along, (site.endpoint - MPoint::origin) * site.along},
                {-site.side, 0.0},
            };
            trimOptionGeometry(arc.geometry, {clip}, true);
        }
        double minSide = 1e100, maxSide = -1e100;
        for (const auto& part : arc.geometry.fillParts) for (const auto& p : part.triangles) {
            if (std::abs((p - site.endpoint) * site.along - cut) > 1e-8 || (p - MPoint::origin) * site.side < 0) continue;
            const double side = (p - MPoint::origin) * site.side;
            minSide = std::min(minSide, side);
            maxSide = std::max(maxSide, side);
        }
        if (minSide == 1e100) continue;
        const auto arcOuter = MPoint::origin + site.along * cut + site.side * maxSide;
        const auto arcInner = MPoint::origin + site.along * cut + site.side * minSide;
        const auto headOuter = site.endpoint + site.along * stop + site.side * (settings.wideWidth * 0.5);
        const auto headInner = site.endpoint + site.along * stop - site.side * (settings.wideWidth * 0.5);
        arc.quad(arcOuter, arcInner, headInner, headOuter);
    }
    WideEndArrowGeometry band;
    for (const auto& part : arc.geometry.fillParts) for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
        const std::vector<MPoint> face = {part.triangles[i], part.triangles[i + 1], part.triangles[i + 2]};
        auto volume = optionPlanarVolume(face);
        if (!volume.empty()) bodyVolumes.push_back(std::move(volume));
        band.triangles.push_back({face[0], face[1], face[2]});
    }
    appendPartTriangleUnion(builder, band, kSemicirclePlane);
}

bool makeOptionShapeGeometry(const ShapeSettings& settings, PartGeometry& geometry) {
    const short outline = outlinePresetIndex(settings.shape);
    if (!optionPartSupported(outline)) return false;
    PartBuilder builder(settings.fill);
    auto heads = makeOptionHeads(settings);
    const auto sites = optionPartSites(settings);
    std::vector<OptionClipVolume> bodyVolumes;
    const short narrow = optionNarrowOutline(outline);
    const bool straight = narrow == 1 || narrow == 4 || narrow == 5 || narrow == 45 || narrow == 52 || narrow == 53;
    if (straight) {
        const auto axes = narrow == 5 || narrow == 45 ? std::vector<unsigned int>{0, 1, 2} : straightLineAxes(narrow);
        WideEndArrowGeometry bands;
        const PartPlane bandPlane{MPoint::origin, nativeAxis(axes.front()), nativeAxis(axes.size() == 2 ? axes.back() : 1)};
        if (narrow == 1) {
            MPoint first(-0.5, 0, 0);
            MPoint last(0.5, 0, 0);
            for (std::size_t i = 0; i < sites.size(); ++i) {
                const auto endpoint = MPoint::origin + sites[i].along * heads.stops[i];
                if (sites[i].along.x > 0) last = endpoint;
                else first = endpoint;
            }
            if (optionWideOutline(outline) && settings.wideWidth > 1e-12) {
                const auto side = nativeAxis(1) * (settings.wideWidth * 0.5);
                auto volume = optionPlanarVolume(
                    {first - side, last - side, last + side, first + side});
                if (!volume.empty()) bodyVolumes.push_back(std::move(volume));
                bands.triangles.push_back({first - side, last - side, last + side});
                bands.triangles.push_back({first - side, last + side, first + side});
            } else if ((last - first).length() > 1e-12) {
                builder.stroke({first, last});
            }
        } else for (auto axis : axes) for (double sign : {-1.0, 1.0}) {
            const auto direction = nativeAxis(axis) * sign;
            double stop = 0.5;
            for (std::size_t i = 0; i < sites.size(); ++i) {
                if ((sites[i].along - direction).length() < 1e-10) stop = std::max(0.0, heads.stops[i]);
            }
            const auto style = narrow == 45 && sign > 0 ? kAxisStyles[axis] : StrokeStyle::Normal;
            if (optionWideOutline(outline) && settings.wideWidth > 1e-12) {
                const unsigned int other = axes.size() == 2 ? (axis == axes.front() ? axes.back() : axes.front()) : 1;
                const auto side = nativeAxis(other) * (0.5 * settings.wideWidth);
                const auto p = MPoint::origin + direction * stop;
                auto volume = optionPlanarVolume({MPoint::origin - side, p - side, p + side, MPoint::origin + side});
                if (!volume.empty()) bodyVolumes.push_back(std::move(volume));
                bands.triangles.push_back({MPoint::origin - side, p - side, p + side});
                bands.triangles.push_back({MPoint::origin - side, p + side, MPoint::origin + side});
            } else if (stop > 1e-12) builder.stroke({MPoint::origin, MPoint::origin + direction * stop}, style);
        }
        if (optionWideOutline(outline)) appendPartTriangleUnion(builder, bands, bandPlane);
    } else if (outline == 27 || outline == 111) {
        appendOptionCircle(builder, settings, heads, sites, bodyVolumes);
    } else if (outline >= 108 && outline <= 110) appendOptionSquare(builder, outline);
    else builder.body(outline);
    if (settings.part && (outline == 19 || outline == 33 || outline == 46 || outline == 47)) {
        PartBuilder body(true);
        body.body(outline);
        auto volume = optionSolidVolume(body.geometry);
        if (!volume.empty()) trimOptionGeometry(heads.geometry, {std::move(volume)}, settings.fill, settings.partShape >= 6);
    } else if (!bodyVolumes.empty()) trimOptionStrokes(heads.geometry, bodyVolumes);
    // 開いた円弧矢印では元の円弧を先端まで残す。
    const bool openCircleArrow = outline == 27 && !settings.fill && settings.partShape <= 1 && settings.partType != 2;
    if (!openCircleArrow) trimOptionGeometry(builder.geometry, heads.volumes, settings.fill);
    // Squareの中央ガイドは塗り面にも通す。通常の軸線は面を表示しない場合だけ延長する。
    if (settings.partShape <= 1 &&
        ((!settings.fill && straight && !optionWideOutline(outline)) || outline == 108 || outline == 109)) {
        for (std::size_t i = 0; i < sites.size(); ++i) {
            const auto& site = sites[i];
            const double tip = site.attached ? 0.125 * site.arrowSize * partLength(settings) : 0.0;
            const auto end = site.endpoint + site.along * (tip + settings.partOffset);
            const double stop = straight && narrow != 1 ? std::max(0.0, heads.stops[i]) : heads.stops[i];
            const auto start = MPoint::origin + site.along * stop;
            StrokeStyle style = outline == 109 ? StrokeStyle::Template : StrokeStyle::Normal;
            if (narrow == 45) for (unsigned int axis = 0; axis < 3; ++axis) {
                if ((site.along - nativeAxis(axis)).length() < 1e-10) style = kAxisStyles[axis];
            }
            if ((end - start).length() > 1e-10) builder.stroke({start, end}, style);
        }
    }
    mergeOptionGeometry(builder.geometry, std::move(heads.geometry));
    geometry = std::move(builder.geometry);
    return true;
}
