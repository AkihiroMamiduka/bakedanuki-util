// 潰れた本体では逆写像を使わず、配置点を写してから付属物の寸法を組み立てる。
ShapeSettings singularArcEffectiveSettings(const ShapeSettings& settings);

MVector singularBaseSpaceDirection(const MVector& direction, const ShapeSettings& settings) {
    const auto span = settings.baseSpacePlus - settings.baseSpaceMinus;
    const MVector mapped(direction.x * span.x, direction.y * span.y, direction.z * span.z);
    return baseSpaceNormalized(std::hypot(mapped.x, mapped.y, mapped.z) == 0.0 ? direction : mapped);
}

MVector singularBaseSpaceVector(const MVector& vector, const ShapeSettings& settings) {
    const bool swap = settings.axisSwap && !isColorOutline(outlinePresetIndex(settings.shape));
    const auto point = presetOrientedPoint(MPoint::origin + vector, settings.shape, swap);
    return point - MPoint::origin;
}

std::vector<OptionSite> singularBaseSpaceNativeSites(const ShapeSettings& settings) {
    const short outline = outlinePresetIndex(settings.shape);
    const short base = crossCircleBaseOutline(outline);
    const auto sitesForPlane = [&](bool second) {
        ShapeSettings source = settings;
        if (base >= 0) source.shape = partPreset(base);
        source.baseSpaceCrossPlane = second;
        const auto joinSettings = singularArcEffectiveSettings(source);
        const double halfWidth = crossAxialHalfWidth(joinSettings);
        if (outline == 115 && settings.wideWidth > 1e-12 && halfWidth < 0.5 - 1e-12) {
            source.crossAxialJoinTop = settings.circleAngle >= 2.0 * std::asin(halfWidth * 2.0) - 1e-12;
        }
        const auto span = baseSpaceScale(source);
        if (isArcOutline(outline) && span.y != 0.0 && span.z != 0.0) {
            // 曲線が残る場合は、実際の楕円とPart寸法から接合姿勢を求める。
            for (unsigned int axis = 0; axis < 3; ++axis) {
                if (source.baseSpacePlus[axis] != source.baseSpaceMinus[axis]) continue;
                const double center = source.baseSpacePlus[axis];
                source.baseSpaceMinus[axis] = center - 0.5;
                source.baseSpacePlus[axis] = center + 0.5;
            }
        } else {
            source.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
            source.baseSpacePlus = MVector(0.5, 0.5, 0.5);
        }
        return optionPartSites(source);
    };
    auto sites = sitesForPlane(false);
    if (base >= 0 && settings.partType == 1) {
        auto other = sitesForPlane(true);
        for (auto& site : other) {
            site.endpoint = crossCirclePoint(site.endpoint);
            site.along = crossCirclePoint(MPoint::origin + site.along) - MPoint::origin;
            site.side = crossCirclePoint(MPoint::origin + site.side) - MPoint::origin;
        }
        sites.insert(sites.end(), other.begin(), other.end());
    }
    return sites;
}

std::vector<OptionSite> singularBaseSpaceSites(const ShapeSettings& settings) {
    auto sites = singularBaseSpaceNativeSites(settings);
    const bool swap = settings.axisSwap && !isColorOutline(outlinePresetIndex(settings.shape));
    for (auto& site : sites) {
        site.endpoint = baseSpacePoint(presetOrientedPoint(site.endpoint, settings.shape, swap), settings);
        const auto oldAlong = singularBaseSpaceVector(site.along, settings);
        const auto oldSide = singularBaseSpaceVector(site.side, settings);
        site.along = singularBaseSpaceDirection(oldAlong, settings);
        auto side = singularBaseSpaceDirection(oldSide, settings);
        side -= site.along * (side * site.along);
        if (side.length() == 0.0) {
            side = oldSide - site.along * (oldSide * site.along);
            if (side.length() == 0.0) {
                const auto axis = std::abs(site.along.x) < 0.9 ? MVector(1, 0, 0) : MVector(0, 1, 0);
                side = axis - site.along * (axis * site.along);
            }
        }
        site.side = baseSpaceNormalized(side);
    }
    return sites;
}

void singularBaseSpaceTemplate(PartGeometry& geometry, bool templated) {
    if (!templated) return;
    for (auto& style : geometry.strokeStyles) style = StrokeStyle::Template;
    for (auto& part : geometry.fillParts) part.style = StrokeStyle::Template;
}

// 元の本体断面とFinの自由頂点を分け、張り出す距離だけを実空間で保つ。
double singularFinSurface(const MPoint& point, const MVector& heightDirection,
    const MVector& widthDirection, const PartGeometry& body) {
    if (body.fillParts.empty()) return 0.0;
    double minimum = 1e100;
    double maximum = -1e100;
    for (const auto& part : body.fillParts) for (const auto& vertex : part.triangles) {
        const double width = (vertex - MPoint::origin) * widthDirection;
        minimum = std::min(minimum, width);
        maximum = std::max(maximum, width);
    }
    if (minimum > maximum) return 0.0;
    auto origin = point - heightDirection * ((point - MPoint::origin) * heightDirection);
    const double width = (origin - MPoint::origin) * widthDirection;
    origin += widthDirection * (std::clamp(width, minimum, maximum) - width);
    double surface = -1e100;
    for (const auto& part : body.fillParts) for (unsigned int i = 0; i + 2 < part.triangles.length(); i += 3) {
        const auto& a = part.triangles[i];
        const auto& b = part.triangles[i + 1];
        const auto& c = part.triangles[i + 2];
        const auto first = b - a;
        const auto second = c - a;
        const auto normal = first ^ second;
        const double denominator = normal * heightDirection;
        if (std::abs(denominator) < 1e-14) continue;
        const double distance = (normal * (a - origin)) / denominator;
        const auto hit = origin + heightDirection * distance;
        const double squared = normal * normal;
        const double u = (((hit - a) ^ second) * normal) / squared;
        const double v = ((first ^ (hit - a)) * normal) / squared;
        if (u >= -1e-9 && v >= -1e-9 && u + v <= 1.0 + 1e-9) surface = std::max(surface, distance);
    }
    return surface == -1e100 ? 0.0 : surface;
}

PartGeometry singularBaseSpaceFin(const ShapeSettings& settings) {
    PartGeometry result;
    const short outline = outlinePresetIndex(settings.shape);
    if (!settings.fin || isArcOutline(outline) || partFinHeight(settings) == 0.0) return result;
    ShapeSettings source = settings;
    source.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
    source.baseSpacePlus = MVector(0.5, 0.5, 0.5);
    source.part = source.guideLine = false;
    PartGeometry fin;
    appendShapeFin(source, fin);
    const bool planar = hasLegacyPlanarOrientation(outline);
    const bool line = outline == 1 || outline == 4 || outline == 5 || outline == 45 ||
        outline == 104 || outline == 106 || outline == 118 || outline == 119;
    const auto height = colorAttachmentVector(planar ? MVector(1, 0, 0) : MVector(0, 1, 0), source);
    const auto width = colorAttachmentVector(planar ? MVector(0, 1, 0) : MVector(1, 0, 0), source);
    PartGeometry body;
    if (!line && !planar && outline != 39) {
        ShapeSettings section = source;
        section.shape = partPreset(baseOutlineIndex(outline));
        section.fill = true;
        if (!makeAdjustedPartGeometry(section, body)) body.fillParts = makeFillParts(ShapeTransform(section));
    }
    const auto publicHeight = singularBaseSpaceVector(height, settings);
    const auto physicalHeight = singularBaseSpaceDirection(publicHeight, settings);
    const bool swap = settings.axisSwap && !isColorOutline(outline);
    const auto mapped = [&](const MPoint& point) {
        const double surface = singularFinSurface(point, height, width, body);
        const double distance = (point - MPoint::origin) * height - surface;
        const auto root = point - height * distance;
        return baseSpacePoint(presetOrientedPoint(root, settings.shape, swap), settings) + physicalHeight * distance;
    };
    for (auto& stroke : fin.strokes) for (auto& point : stroke) point = mapped(point);
    for (auto& part : fin.fillParts) for (auto& point : part.triangles) point = mapped(point);
    return fin;
}

MPoint singularArcPoint(const MPoint& point, const ShapeSettings& settings, bool second) {
    const auto oriented = presetOrientedPoint(second ? crossCirclePoint(point) : point,
        settings.shape, settings.axisSwap);
    return baseSpacePoint(oriented, settings);
}

void mapSingularArcGeometry(PartGeometry& geometry, const ShapeSettings& settings, bool second) {
    for (auto& stroke : geometry.strokes) for (auto& point : stroke) point = singularArcPoint(point, settings, second);
    for (auto& part : geometry.fillParts) for (auto& point : part.triangles) point = singularArcPoint(point, settings, second);
}

ShapeSettings singularArcEffectiveSettings(const ShapeSettings& settings) {
    auto result = settings;
    for (unsigned int axis = 0; axis < 3; ++axis) {
        if (result.baseSpacePlus[axis] != result.baseSpaceMinus[axis]) continue;
        const double center = result.baseSpacePlus[axis];
        result.baseSpaceMinus[axis] = center - 0.5;
        result.baseSpacePlus[axis] = center + 0.5;
    }
    return result;
}

OptionHeads singularArcFlatHeads(const ShapeSettings& settings, bool second) {
    auto sites = singularBaseSpaceNativeSites(settings);
    for (auto& site : sites) {
        site.endpoint = singularArcPoint(site.endpoint, settings, second);
        const auto orientation = [&](const MVector& vector) {
            const auto point = second ? crossCirclePoint(MPoint::origin + vector) : MPoint::origin + vector;
            return presetOrientedPoint(point, settings.shape, settings.axisSwap) - MPoint::origin;
        };
        site.along = singularBaseSpaceDirection(orientation(site.along), settings);
        auto side = singularBaseSpaceDirection(orientation(site.side), settings);
        side -= site.along * (side * site.along);
        if (std::hypot(side.x, side.y, side.z) == 0.0) {
            const auto oldSide = orientation(site.side);
            side = oldSide - site.along * (oldSide * site.along);
        }
        if (std::hypot(side.x, side.y, side.z) == 0.0) {
            const auto axis = std::abs(site.along.x) < 0.9 ? nativeAxis(0) : nativeAxis(1);
            side = axis - site.along * (axis * site.along);
        }
        site.side = baseSpaceNormalized(side);
    }
    auto physical = settings;
    physical.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
    physical.baseSpacePlus = MVector(0.5, 0.5, 0.5);
    physical.axisSwap = physical.baseSpaceCrossPlane = false;
    return makeOptionHeads(physical, false, &sites);
}

// 円平面が残る場合は、潰れた法線軸だけを計算用に復元して巻き付けを保つ。
bool appendSingularWrappedArcs(const ShapeSettings& settings, PartGeometry& geometry) {
    const short outline = outlinePresetIndex(settings.shape);
    if (!settings.part || !isArcOutline(outline) || settings.partShape > 5 || settings.partType == 2) return false;
    const short base = crossCircleBaseOutline(outline);
    const unsigned int count = base >= 0 ? 2 : 1;
    std::array<ShapeSettings, 2> sources = {settings, settings};
    bool wrapped = false;
    for (unsigned int index = 0; index < count; ++index) {
        auto& source = sources[index];
        if (base >= 0) source.shape = partPreset(base);
        source.baseSpaceCrossPlane = index == 1;
        source.part = settings.part && (index == 0 || settings.partType == 1);
        const auto joinSettings = singularArcEffectiveSettings(source);
        const double halfWidth = crossAxialHalfWidth(joinSettings);
        if (outline == 115 && settings.wideWidth > 1e-12 && halfWidth < 0.5 - 1e-12) {
            source.crossAxialJoinTop = settings.circleAngle >= 2.0 * std::asin(halfWidth * 2.0) - 1e-12;
            source.crossAxialJoinBottom = settings.circleAngle >= 2.0 * kPi - 1e-12;
        }
        const auto span = baseSpaceScale(source);
        wrapped = wrapped || (source.part && span.y != 0.0 && span.z != 0.0);
    }
    if (!wrapped) return false;
    std::array<PartGeometry, 2> planes;
    std::array<std::vector<OptionClipVolume>, 2> volumes;
    for (unsigned int index = 0; index < count; ++index) {
        const auto& source = sources[index];
        const auto span = baseSpaceScale(source);
        const bool onCurve = source.part && span.y != 0.0 && span.z != 0.0;
        if (onCurve) {
            auto effective = singularArcEffectiveSettings(source);
            if (isAxialArcOutline(outlinePresetIndex(source.shape))) {
                auto data = makeAxialWrapData(effective);
                PartBuilder builder(source.fill);
                const auto main = axialWrapIntervals(data.slices, data.main);
                const auto crest = axialWrapIntervals(data.slices, data.crest);
                appendAxialWrapFaces(builder, main, false, effective);
                appendAxialWrapFaces(builder, crest, true, effective);
                AxialWrapSegments segments;
                appendAxialWrapBoundary(segments, main, data.spokes, false, effective);
                appendAxialWrapBoundary(segments, crest, data.crestSpokes, true, effective);
                appendAxialWrapStrokes(builder, std::move(segments));
                planes[index] = std::move(builder.geometry);
                volumes[index] = axialWrappedPartClipVolumes(effective);
            } else {
                planes[index] = makeRadialWrappedGeometry(effective);
                volumes[index] = radialWrappedPartClipVolumes(effective);
            }
            if (effective.templateLine || effective.templateFill || effective.partTemplate) {
                applyBodyTemplate(effective, planes[index], bodyTemplateReference(effective),
                    optionPartClipVolumes(effective, true));
            }
            // 半空間も頂点と同じアフィン写像へ合わせる。
            for (auto& volume : volumes[index]) for (auto& plane : volume) {
                const auto origin = singularArcPoint(MPoint::origin, effective, index == 1);
                const auto oldNormal = plane.normal;
                const auto vector = inverseBaseSpaceVector(oldNormal, effective);
                plane.normal = singularBaseSpaceVector(index == 1
                    ? crossCirclePoint(MPoint::origin + vector) - MPoint::origin : vector, effective);
                plane.distance += (origin - MPoint::origin) * plane.normal;
            }
            mapSingularArcGeometry(planes[index], effective, index == 1);
        } else {
            auto body = source;
            body.part = false;
            makeOptionShapeGeometry(body, planes[index]);
            if (body.templateLine || body.templateFill) {
                auto classification = body;
                classification.part = source.part;
                applyBodyTemplate(classification, planes[index], bodyTemplateReference(body), {});
            }
            mapSingularArcGeometry(planes[index], body, index == 1);
            if (source.part) {
                auto heads = singularArcFlatHeads(source, index == 1);
                trimOptionGeometry(planes[index], heads.volumes, source.fill);
                singularBaseSpaceTemplate(heads.geometry, source.partTemplate);
                volumes[index] = std::move(heads.volumes);
                mergeOptionGeometry(planes[index], std::move(heads.geometry));
            }
        }
    }
    if (count == 2) {
        trimOptionGeometry(planes[0], volumes[1], settings.fill, true);
        trimOptionGeometry(planes[1], volumes[0], settings.fill);
        mergeOptionGeometry(planes[0], std::move(planes[1]));
    }
    geometry = std::move(planes[0]);
    if (count == 2 && (sources[0].crossAxialJoinTop || sources[0].crossAxialJoinBottom)) {
        const auto center = baseSpacePoint(MPoint::origin, settings);
        const auto reorient = [&](bool restore) {
            const auto point = [&](const MPoint& value) {
                const auto local = restore ? value : value - (center - MPoint::origin);
                const auto oriented = presetOrientedPoint(local, settings.shape, settings.axisSwap);
                return restore ? oriented + (center - MPoint::origin) : oriented;
            };
            for (auto& stroke : geometry.strokes) for (auto& value : stroke) value = point(value);
            for (auto& part : geometry.fillParts) for (auto& value : part.triangles) value = point(value);
        };
        reorient(false);
        const auto joinSettings = singularArcEffectiveSettings(sources[0]);
        const double height = crossAxialJoinHeight(joinSettings) * baseSpaceScale(joinSettings).y;
        if (sources[0].crossAxialJoinTop) joinCrossAxialPlane(geometry, height);
        if (sources[0].crossAxialJoinBottom) joinCrossAxialPlane(geometry, -height);
        reorient(true);
    }
    if (!settings.fill) geometry.fillParts.clear();
    return true;
}

void appendSingularBaseSpaceAttachments(const ShapeSettings& settings, PartGeometry& geometry) {
    if (appendSingularWrappedArcs(settings, geometry)) return;
    ShapeSettings physical = settings;
    physical.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
    physical.baseSpacePlus = MVector(0.5, 0.5, 0.5);
    physical.axisSwap = false;
    const short base = crossCircleBaseOutline(outlinePresetIndex(settings.shape));
    if (base >= 0) physical.shape = partPreset(base);
    const auto sites = singularBaseSpaceSites(settings);
    auto heads = makeOptionHeads(physical, false, &sites);
    trimOptionGeometry(geometry, heads.volumes, settings.fill);
    auto fin = singularBaseSpaceFin(settings);
    trimOptionGeometry(fin, heads.volumes, settings.fill);
    const short outline = outlinePresetIndex(settings.shape);
    const bool straight = outline == 1 || outline == 4 || outline == 5 || outline == 45 ||
        outline == 104 || outline == 106 || outline == 118 || outline == 119;
    const auto center = baseSpacePoint(MPoint::origin, settings);
    const auto oldSites = singularBaseSpaceNativeSites(settings);
    for (std::size_t i = 0; i < sites.size(); ++i) {
        const auto& site = sites[i];
        const double tip = site.attached ? 0.125 * site.sizeScale * partLength(settings) : 0.0;
        const auto endpoint = site.endpoint + site.along * (tip + settings.partOffset);
        if (straight) {
            const bool openArrow = settings.partShape <= 1 && !settings.fill && !settings.wide;
            const double stop = heads.stops[i] - (center - MPoint::origin) * site.along;
            const auto target = openArrow ? endpoint : center + site.along * stop;
            if (outline == 1 || (target - center) * site.along > 0.0) {
                StrokeStyle style = StrokeStyle::Normal;
                if (isColorOutline(outline)) {
                    const auto direction = singularBaseSpaceVector(oldSites[i].along, settings);
                    for (unsigned int axis = 0; axis < 3; ++axis) {
                        if (direction * nativeAxis(axis) > 0.9) style = kAxisStyles[axis];
                    }
                }
                if (settings.templateLine && ((settings.templateLineRate >= 1.0) != settings.templateLineInvert)) {
                    style = StrokeStyle::Template;
                }
                appendGuideSegment(geometry, target, style, center);
            }
        }
        if (settings.guideLine && settings.partShape <= 1 &&
            (outline == 8 || outline == 110 || outline == 116 || outline == 104 || outline == 106)) {
            appendGuideSegment(geometry, endpoint,
                settings.guideLineTemplate ? StrokeStyle::Template : StrokeStyle::Normal, center);
        }
    }
    singularBaseSpaceTemplate(heads.geometry, settings.partTemplate);
    mergeOptionGeometry(geometry, std::move(heads.geometry));
    mergeOptionGeometry(geometry, std::move(fin));
}
