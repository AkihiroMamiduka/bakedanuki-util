// Cageは接合点と姿勢へ作用させ、PartとFinの局所距離は物理空間で生成する。
MVector cageAttachmentBaseVector(const MVector& vector, const ShapeSettings& settings) {
    return cageBaseBodyPoint(MPoint::origin + vector, settings) - cageBaseBodyPoint(MPoint::origin, settings);
}

MVector cageAttachmentUnit(MVector vector, const MVector& fallback) {
    if (std::hypot(vector.x, vector.y, vector.z) == 0.0) vector = fallback;
    if (std::hypot(vector.x, vector.y, vector.z) == 0.0) vector = MVector(1, 0, 0);
    return baseSpaceNormalized(vector);
}

BaseSpacePartFrame cageAttachmentFrame(const MPoint& basePoint, const MVector& along,
    const MVector& side, const ShapeSettings& settings, bool surfaceNormal = false) {
    auto aim = surfaceNormal ? cageNormal(basePoint, along, settings) : cageVector(basePoint, along, settings);
    aim = cageAttachmentUnit(aim, along);
    auto across = cageVector(basePoint, side, settings);
    across -= aim * (across * aim);
    if (std::hypot(across.x, across.y, across.z) == 0.0) across = side - aim * (side * aim);
    if (std::hypot(across.x, across.y, across.z) == 0.0) {
        const auto helper = std::abs(aim.x) < 0.9 ? MVector(1, 0, 0) : MVector(0, 1, 0);
        across = helper - aim * (helper * aim);
    }
    across = baseSpaceNormalized(across);
    return {aim, across, baseSpaceNormalized(aim ^ across)};
}

// 変形後の三角面または輪郭へ射線を当て、近い交点で接合する。
bool cageAttachmentSurfacePoint(const MPoint& point, const MVector& direction,
    const PartGeometry& body, MPoint& result, bool highest = false) {
    bool found = false;
    double best = highest ? -1e100 : 1e100;
    const auto remember = [&](double distance) {
        if (!std::isfinite(distance)) return;
        const double rank = highest ? distance : std::abs(distance);
        if (found && (highest ? rank <= best : rank >= best)) return;
        found = true;
        best = rank;
        result = point + direction * distance;
    };
    for (const auto& part : body.fillParts) for (unsigned int i = 0; i + 2 < part.triangles.length(); i += 3) {
        const auto& a = part.triangles[i];
        const auto first = part.triangles[i + 1] - a, second = part.triangles[i + 2] - a;
        const auto normal = first ^ second;
        const double denominator = normal * direction, squared = normal * normal;
        if (denominator == 0.0 || squared == 0.0) continue;
        const double distance = normal * (a - point) / denominator;
        const auto hit = point + direction * distance;
        const double u = (((hit - a) ^ second) * normal) / squared;
        const double v = ((first ^ (hit - a)) * normal) / squared;
        if (u >= -1e-9 && v >= -1e-9 && u + v <= 1.0 + 1e-9) remember(distance);
    }
    if (found || highest) return found;
    for (const auto& stroke : body.strokes) for (unsigned int i = 1; i < stroke.length(); ++i) {
        const auto edge = stroke[i] - stroke[i - 1], delta = stroke[i - 1] - point;
        const auto cross = direction ^ edge;
        const double squared = cross * cross;
        if (squared == 0.0) continue;
        const double distance = ((delta ^ edge) * cross) / squared;
        const double fraction = ((delta ^ direction) * cross) / squared;
        if (fraction < -1e-9 || fraction > 1.0 + 1e-9) continue;
        if ((point + direction * distance - stroke[i - 1] - edge * fraction).length() < 1e-8) remember(distance);
    }
    return found;
}

std::vector<OptionClipVolume> cageAttachmentBodyVolumes(const PartGeometry& body,
    bool solid, const MPoint& center) {
    std::vector<OptionClipVolume> volumes;
    for (const auto& part : body.fillParts) for (unsigned int i = 0; i + 2 < part.triangles.length(); i += 3) {
        const auto a = part.triangles[i], b = part.triangles[i + 1], c = part.triangles[i + 2];
        if (!solid) {
            auto volume = optionPlanarVolume({a, b, c});
            if (!volume.empty()) volumes.push_back(std::move(volume));
            continue;
        }
        if (std::abs(((b - a) ^ (c - a)) * (center - a)) < 1e-15) continue;
        const auto inside = MPoint::origin + ((a - MPoint::origin) + (b - MPoint::origin) +
            (c - MPoint::origin) + (center - MPoint::origin)) * 0.25;
        OptionClipVolume volume;
        addOptionClipPlane(volume, (b - a) ^ (c - a), a, inside);
        addOptionClipPlane(volume, (b - a) ^ (center - a), a, inside);
        addOptionClipPlane(volume, (c - b) ^ (center - b), b, inside);
        addOptionClipPlane(volume, (a - c) ^ (center - c), c, inside);
        if (volume.size() == 4) volumes.push_back(std::move(volume));
    }
    return volumes;
}

std::vector<OptionSite> cageAttachmentNativeSites(const ShapeSettings& settings) {
    const short base = crossCircleBaseOutline(outlinePresetIndex(settings.shape));
    if (base < 0) return optionPartSites(settings);
    auto source = settings;
    source.shape = partPreset(base);
    auto result = optionPartSites(source);
    if (settings.partType != 1) return result;
    source.baseSpaceCrossPlane = true;
    auto other = optionPartSites(source);
    for (auto& site : other) {
        site.endpoint = crossCirclePoint(site.endpoint);
        site.along = crossCirclePoint(MPoint::origin + site.along) - MPoint::origin;
        site.side = crossCirclePoint(MPoint::origin + site.side) - MPoint::origin;
    }
    result.insert(result.end(), other.begin(), other.end());
    return result;
}

bool cageAttachmentSolidBody(const ShapeSettings& settings) {
    const short outline = outlinePresetIndex(settings.shape);
    return outline == 19 || outline == 33 || outline == 46 || outline == 47;
}

std::vector<OptionSite> cageArcAttachmentSites(const ShapeSettings& settings) {
    std::vector<OptionSite> result;
    const short outline = outlinePresetIndex(settings.shape);
    const bool axial = isAxialArcOutline(outline);
    const double sweep = std::clamp(settings.circleAngle, 0.0, 2.0 * kPi);
    if (sweep < 1e-12) return result;
    const double first = (kPi - sweep) * 0.5, last = (kPi + sweep) * 0.5;
    auto physical = settings;
    physical.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
    physical.baseSpacePlus = MVector(0.5, 0.5, 0.5);
    const double depth = axialHeadJoinLength(physical);
    const unsigned int count = crossCircleBaseOutline(outline) >= 0 && settings.partType == 1 ? 2 : 1;
    for (unsigned int plane = 0; plane < count; ++plane) {
        const CageArcMetric metric(settings, plane != 0);
        for (unsigned int endIndex = 0; endIndex < (settings.partType == 1 ? 2u : 1u); ++endIndex) {
            const bool atFirst = endIndex == 0;
            const double theta = atFirst ? first : last;
            OptionSite site{metric.point(theta), metric.tangent(theta) * (atFirst ? -1.0 : 1.0),
                axial ? metric.binormal(theta) * (atFirst ? 1.0 : -1.0) : metric.normal(theta), false};
            const auto anchor = site.endpoint + site.along * settings.partOffset;
            const auto originalAlong = site.along, originalSide = site.side;
            const bool symmetricSphere = settings.partShape == 8 &&
                std::abs(partLength(settings) - std::abs(axial ? partHeight(settings) : partWidth(settings))) < 1e-12;
            if (depth > 1e-12 && !metric.degenerate() && !symmetricSphere &&
                (!settings.wide || settings.wideWidth <= 0.1 * std::abs(partWidth(settings)) + 1e-10)) {
                const auto value = [&](double angle) {
                    const auto delta = anchor - metric.point(angle);
                    return delta * delta - depth * depth;
                };
                double before = theta, previous = value(theta);
                for (unsigned int step = 1; step <= 1024; ++step) {
                    const double next = theta + (atFirst ? last - first : first - last) * step / 1024;
                    const double current = value(next);
                    if ((previous < 0.0) != (current < 0.0)) {
                        double low = before, high = next;
                        const bool negative = previous < 0.0;
                        for (unsigned int iteration = 0; iteration < 40; ++iteration) {
                            const double middle = (low + high) * 0.5;
                            if ((value(middle) < 0.0) == negative) low = middle;
                            else high = middle;
                        }
                        const double angle = (low + high) * 0.5;
                        const auto along = cageAttachmentUnit(anchor - metric.point(angle), originalAlong);
                        auto side = originalSide;
                        if (!axial) side = cageAttachmentUnit((originalAlong ^ originalSide) ^ along, originalSide);
                        const auto center = cageBodyPoint(MPoint::origin, settings);
                        const bool outward = axial ? ((along ^ side) * (metric.point(angle) - center) >= -1e-10)
                            : (side * (metric.point(angle) - center) >= -1e-10);
                        if (along * originalAlong >= -1e-10 && outward && std::abs(angle - theta) <= kPi + 1e-10) {
                            site.along = along;
                            site.side = side;
                            site.endpoint = anchor - along * settings.partOffset;
                            break;
                        }
                    }
                    before = next;
                    previous = current;
                }
            }
            result.push_back(site);
        }
    }
    return result;
}

OptionHeads makeCageAttachmentHeads(const ShapeSettings& settings, const PartGeometry& actualBody,
    std::vector<OptionSite>& physicalSites) {
    OptionHeads result;
    auto physical = settings;
    physical.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
    physical.baseSpacePlus = MVector(0.5, 0.5, 0.5);
    physical.axisSwap = physical.baseSpaceCrossPlane = false;
    const bool physicalArcSites = isArcOutline(outlinePresetIndex(settings.shape)) && settings.partType != 2;
    const auto sites = physicalArcSites ? cageArcAttachmentSites(settings) : cageAttachmentNativeSites(settings);
    for (auto site : sites) {
        if (!physicalArcSites) {
            const auto basePoint = cageBaseBodyPoint(site.endpoint, settings);
            const auto baseAlong = cageAttachmentBaseVector(site.along, settings);
            const auto baseSide = cageAttachmentBaseVector(site.side, settings);
            const auto frame = cageAttachmentFrame(basePoint,
                cageAttachmentUnit(baseAlong, singularBaseSpaceVector(site.along, settings)),
                cageAttachmentUnit(baseSide, singularBaseSpaceVector(site.side, settings)), settings,
                site.attached && cageAttachmentSolidBody(settings));
            site.endpoint = cagePoint(basePoint, settings);
            site.along = frame.along;
            site.side = frame.side;
            if (site.attached && !cageAttachmentSolidBody(settings)) {
                site.side = cageAttachmentUnit(cageVector(basePoint, baseSide, settings), frame.side);
                const auto normal = cageNormal(basePoint, baseAlong ^ baseSide, settings);
                site.along = cageAttachmentUnit(site.side ^ normal, frame.along);
                if (site.along * frame.along < 0.0) site.along = -site.along;
            }
        }
        if (site.attached) {
            MPoint surface;
            if (cageAttachmentSurfacePoint(site.endpoint, site.along, actualBody, surface)) site.endpoint = surface;
        }
        physicalSites.push_back(site);
        const std::vector<OptionSite> oneSite{site};
        auto filled = physical;
        filled.fill = true;
        auto head = makeOptionHeads(filled, false, &oneSite);
        result.stops.push_back(head.stops.empty() ? (site.endpoint - MPoint::origin) * site.along : head.stops.front());
        if (site.attached && settings.partShape <= 1) {
            const auto root = [&](MPoint& point) {
                const auto delta = point - site.endpoint;
                if (std::abs(delta * site.along) > 1e-9 || std::abs(delta * (site.along ^ site.side)) > 1e-9) return;
                MPoint surface;
                if (cageAttachmentSurfacePoint(point, site.along, actualBody, surface)) point = surface;
            };
            for (auto& stroke : head.geometry.strokes) for (auto& point : stroke) root(point);
            for (auto& part : head.geometry.fillParts) for (auto& point : part.triangles) root(point);
            head.volumes = cageAttachmentBodyVolumes(head.geometry, false, site.endpoint);
        }
        if (!settings.fill) head.geometry.fillParts.clear();
        if (!result.volumes.empty()) trimOptionGeometry(head.geometry, result.volumes, settings.fill, settings.partShape >= 6);
        if (!head.volumes.empty()) {
            if (settings.partShape >= 6) trimOptionGeometry(result.geometry, head.volumes, settings.fill);
            else trimOptionStrokes(result.geometry, head.volumes);
        }
        result.volumes.insert(result.volumes.end(), head.volumes.begin(), head.volumes.end());
        mergeOptionGeometry(result.geometry, std::move(head.geometry));
    }
    return result;
}

PartGeometry makeCageAttachmentFin(const ShapeSettings& settings, const PartGeometry& baseBody) {
    if (!settings.fin || isArcOutline(outlinePresetIndex(settings.shape)) || partFinHeight(settings) == 0.0) return {};
    auto source = untransformedShapeSettings(settings);
    source.part = source.guideLine = false;
    PartGeometry fin;
    if (isArrowBody(settings)) {
        auto raw = source;
        raw.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
        raw.baseSpacePlus = MVector(0.5, 0.5, 0.5);
        raw.axisSwap = false;
        fin = makeArrowFinGeometry(source, raw);
    } else fin = singularBaseSpaceFin(source);
    const short outline = outlinePresetIndex(source.shape);
    const bool planar = hasLegacyPlanarOrientation(outline);
    auto nativeHeight = colorAttachmentVector(planar ? MVector(1, 0, 0) : MVector(0, 1, 0), source);
    if (outline == 52 || outline == 105 || outline == 57 || outline == 65 || (outline >= 92 && outline <= 95)) {
        nativeHeight = colorAttachmentVector(MVector(0, 0, 1), source);
    }
    const auto height = cageAttachmentUnit(cageAttachmentBaseVector(nativeHeight, settings),
        singularBaseSpaceVector(nativeHeight, settings));
    const auto bounds = boundsForGeometry(baseBody.strokes, baseBody.fillParts);
    const auto mapped = [&](const MPoint& point) {
        MPoint root = point;
        if (!cageAttachmentSurfacePoint(point, height, baseBody, root, true)) {
            auto probe = point;
            for (unsigned int axis = 0; axis < 3; ++axis) if (std::abs(height[axis]) < 0.5) {
                probe[axis] = std::clamp(probe[axis], bounds.min()[axis], bounds.max()[axis]);
            }
            MPoint surface;
            if (cageAttachmentSurfacePoint(probe, height, baseBody, surface, true)) {
                root = point + height * ((surface - probe) * height);
            } else {
                const auto center = cageBaseBodyPoint(MPoint::origin, settings);
                root = point - height * ((point - center) * height);
            }
        }
        const double distance = (point - root) * height;
        const auto direction = cageAttachmentUnit(cageNormal(root, height, settings), height);
        return cagePoint(root, settings) + direction * distance;
    };
    for (auto& stroke : fin.strokes) for (auto& point : stroke) point = mapped(point);
    for (auto& part : fin.fillParts) for (auto& point : part.triangles) point = mapped(point);
    return fin;
}

bool makeCageStraightPartBody(const ShapeSettings& settings, const OptionHeads& heads,
    const std::vector<OptionSite>& partSites, PartGeometry& geometry) {
    const short narrow = optionNarrowOutline(outlinePresetIndex(settings.shape));
    if (narrow != 1 && narrow != 4 && narrow != 5 && narrow != 45 && narrow != 52 && narrow != 53) return false;
    const auto axes = narrow == 5 || narrow == 45 ? std::vector<unsigned int>{0, 1, 2} : straightLineAxes(narrow);
    const auto center = cageBodyPoint(MPoint::origin, settings);
    std::vector<OptionSite> arms;
    OptionHeads stops;
    for (auto axis : axes) for (double sign : {-1.0, 1.0}) {
        const auto point = cageBodyPoint(MPoint::origin + nativeAxis(axis) * (sign * 0.5), settings);
        const auto along = cageAttachmentUnit(point - center,
            singularBaseSpaceVector(nativeAxis(axis) * sign, settings));
        double stop = (point - center) * along;
        for (std::size_t i = 0; i < partSites.size(); ++i) {
            if ((partSites[i].along - along).length() > 1e-8) continue;
            stop = heads.stops[i] - (center - MPoint::origin) * along;
            if (settings.wide && settings.partShape >= 6) {
                stop = (partSites[i].endpoint - center) * along + settings.partOffset;
                if (settings.partShape >= 9) stop -= 0.1 * partLength(settings) * partSites[i].sizeScale;
            }
        }
        if (narrow != 1) stop = std::max(0.0, stop);
        arms.push_back({MPoint::origin + along * stop, along, directionalPartSide(axis), false});
        stops.stops.push_back(stop);
    }
    PartBuilder body(settings.fill);
    if (settings.wide && axes.size() == 3) {
        auto physical = settings;
        physical.shape = partPreset(narrow == 45 ? 119 : 118);
        physical.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
        physical.baseSpacePlus = MVector(0.5, 0.5, 0.5);
        physical.axisSwap = false;
        physical.partShape = 0;
        std::vector<OptionClipVolume> volumes;
        appendOptionWideCross3Axis(body, physical, stops, arms, volumes);
        translateArrowGeometry(body.geometry, center - MPoint::origin);
    } else if (!settings.wide || settings.wideWidth <= 1e-12) {
        if (narrow == 1) body.stroke({center + (arms[0].endpoint - MPoint::origin),
            center + (arms[1].endpoint - MPoint::origin)});
        else for (std::size_t i = 0; i < arms.size(); ++i) body.stroke({center,
            center + (arms[i].endpoint - MPoint::origin)},
            narrow == 45 && i % 2 != 0 ? kAxisStyles[axes[i / 2]] : StrokeStyle::Normal);
    } else {
        const auto basePoint = cageBaseBodyPoint(MPoint::origin, settings);
        const auto first = cageAttachmentBaseVector(nativeAxis(axes.front()), settings);
        const auto other = cageAttachmentBaseVector(nativeAxis(axes.size() == 2 ? axes.back() : 2), settings);
        const auto frame = cageAttachmentFrame(basePoint, first, other, settings);
        const auto normal = cageAttachmentUnit(frame.along ^ frame.side, MVector(0, 1, 0));
        WideEndArrowGeometry bands;
        for (std::size_t i = 0; i < (narrow == 1 ? 1u : arms.size()); ++i) {
            const auto a = narrow == 1 ? center + (arms[0].endpoint - MPoint::origin) : center;
            const auto b = center + (arms[narrow == 1 ? 1 : i].endpoint - MPoint::origin);
            const auto side = cageAttachmentUnit(normal ^ (b - a), frame.side) * (settings.wideWidth * 0.5);
            bands.triangles.push_back({a - side, b - side, b + side});
            bands.triangles.push_back({a - side, b + side, a + side});
        }
        for (auto& triangle : bands.triangles) for (auto& point : triangle) point -= center - MPoint::origin;
        appendPartTriangleUnion(body, bands, {MPoint::origin, frame.along, frame.side});
        translateArrowGeometry(body.geometry, center - MPoint::origin);
    }
    geometry = std::move(body.geometry);
    return true;
}

void appendCageAttachmentGuides(const ShapeSettings& settings, PartGeometry& geometry,
    const std::vector<OptionSite>& physicalSites, const PartGeometry& contactBody,
    const std::vector<OptionClipVolume>& protection) {
    if (!settings.guideLine || !isGuideShape(outlinePresetIndex(settings.shape))) return;
    auto raw = untransformedShapeSettings(settings);
    raw.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
    raw.baseSpacePlus = MVector(0.5, 0.5, 0.5);
    raw.axisSwap = raw.part = raw.fin = false;
    PartGeometry guides;
    const short outline = outlinePresetIndex(settings.shape);
    if (outline == 104 || outline == 106 || outline == 118 || outline == 119) {
        const auto axes = outline == 118 || outline == 119 ? std::vector<unsigned int>{0, 1, 2}
            : straightLineAxes(optionNarrowOutline(outline));
        for (auto axis : axes) for (double sign : {-1.0, 1.0}) {
            appendGuideSegment(guides, MPoint::origin + nativeAxis(axis) * (sign * 0.5),
                settings.guideLineTemplate ? StrokeStyle::Template :
                    outline == 119 && sign > 0 ? kAxisStyles[axis] : StrokeStyle::Normal);
        }
    } else appendShapeGuide(raw, guides, GuideBodyGeometry{});
    PartGeometry physicalGuides;
    const auto center = cageBodyPoint(MPoint::origin, settings);
    const auto mapped = [&](const MPoint& point) {
        auto result = cageBodyPoint(point, settings);
        if (settings.wide && (result - center).length() > 1e-12 &&
            (isPlanarCircleOutline(outline) || outline == 116 || outline == 104 || outline == 106 ||
                outline == 118 || outline == 119)) {
            MPoint hit;
            const auto direction = cageAttachmentUnit(result - center, MVector(1, 0, 0));
            if (cageAttachmentSurfacePoint(result, direction, contactBody, hit)) result = hit;
        }
        return result;
    };
    for (std::size_t index = 0; index < guides.strokes.size(); ++index) {
        const auto& stroke = guides.strokes[index];
        for (unsigned int i = 1; i < stroke.length(); ++i) {
            appendGuideSegment(physicalGuides, mapped(stroke[i]), guides.strokeStyles[index], mapped(stroke[i - 1]));
        }
    }
    if (outline == 104) {
        const auto basePoint = cageBaseBodyPoint(MPoint::origin, settings);
        const auto frame = cageAttachmentFrame(basePoint, cageAttachmentBaseVector(nativeAxis(0), settings),
            cageAttachmentBaseVector(nativeAxis(2), settings), settings);
        const auto style = settings.guideLineTemplate ? StrokeStyle::Template : StrokeStyle::Normal;
        for (double sign : {-1.0, 1.0}) appendGuideSegment(physicalGuides,
            center + frame.side * (sign * settings.wideWidth * 0.5), style, center);
    }
    trimOptionStrokes(physicalGuides, protection);
    for (std::size_t index = 0; index < physicalGuides.strokes.size(); ++index) {
        const auto& stroke = physicalGuides.strokes[index];
        for (unsigned int i = 1; i < stroke.length(); ++i) appendGuideSegment(geometry, stroke[i],
            physicalGuides.strokeStyles[index], stroke[i - 1]);
    }
    if (settings.part && settings.partShape <= 1 &&
        (outline == 8 || outline == 110 || outline == 116 || outline == 104 || outline == 106)) {
        auto physical = settings;
        physical.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
        physical.baseSpacePlus = MVector(0.5, 0.5, 0.5);
        for (const auto& site : physicalSites) appendGuideSegment(geometry, optionPartTip(site, physical),
            settings.guideLineTemplate ? StrokeStyle::Template : StrokeStyle::Normal, center);
    }
}

bool appendCageWrappedAttachments(const ShapeSettings& settings, PartGeometry& geometry,
    std::vector<OptionClipVolume>* templateProtection);

void appendCageAttachments(const ShapeSettings& settings, PartGeometry& geometry,
    const PartGeometry& baseBodyPhysical, const PartGeometry& actualBodyPhysical,
    std::vector<OptionClipVolume>* templateProtection = nullptr) {
    std::vector<OptionClipVolume> protection;
    const bool wrapped = appendCageWrappedAttachments(settings, geometry, &protection);
    const short outline = outlinePresetIndex(settings.shape);
    const bool needsContact = (settings.part && optionPartSupported(outline)) ||
        (settings.guideLine && isGuideShape(outline));
    auto contactBody = needsContact ? actualBodyPhysical : PartGeometry{};
    if (!wrapped && settings.wide && needsContact) {
        if (settings.fill) contactBody = geometry;
        else {
            auto filled = settings;
            filled.fill = true;
            const auto canonical = cageCanonicalBodyGeometry(filled);
            makeCageWideBody(filled, canonical, baseBodyPhysical, actualBodyPhysical, contactBody);
        }
    }
    std::vector<OptionSite> physicalSites;
    if (!wrapped && settings.part && optionPartSupported(outlinePresetIndex(settings.shape))) {
        auto heads = makeCageAttachmentHeads(settings, contactBody, physicalSites);
        protection = heads.volumes;
        const bool straight = makeCageStraightPartBody(settings, heads, physicalSites, geometry);
        if (straight) {
            auto filled = settings;
            filled.fill = true;
            makeCageStraightPartBody(filled, heads, physicalSites, contactBody);
        }
        const auto center = cageBodyPoint(MPoint::origin, settings);
        auto bodyVolumes = cageAttachmentBodyVolumes(cageAttachmentSolidBody(settings) ? actualBodyPhysical : contactBody,
            cageAttachmentSolidBody(settings), center);
        if (cageAttachmentSolidBody(settings)) trimOptionGeometry(heads.geometry, bodyVolumes, settings.fill, settings.partShape >= 6);
        else trimOptionStrokes(heads.geometry, bodyVolumes);
        trimOptionGeometry(geometry, heads.volumes, settings.fill);
        singularBaseSpaceTemplate(heads.geometry, settings.partTemplate);
        mergeOptionGeometry(geometry, std::move(heads.geometry));
        if (straight && !settings.wide && !settings.fill && settings.partShape <= 1) {
            auto physical = settings;
            physical.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
            physical.baseSpacePlus = MVector(0.5, 0.5, 0.5);
            for (std::size_t i = 0; i < physicalSites.size(); ++i) {
                const auto& site = physicalSites[i];
                const auto start = site.endpoint + site.along *
                    (heads.stops[i] - (site.endpoint - MPoint::origin) * site.along);
                appendGuideSegment(geometry, optionPartTip(site, physical), StrokeStyle::Normal, start);
            }
        }
    }
    if (settings.templateLine || settings.templateFill || settings.partTemplate) {
        applyCageBodyTemplate(settings, geometry, baseBodyPhysical, protection);
    }
    if (templateProtection) *templateProtection = protection;
    auto fin = makeCageAttachmentFin(settings, baseBodyPhysical);
    trimOptionGeometry(fin, protection, settings.fill, true);
    if (settings.fill && !fin.fillParts.empty()) {
        const auto before = geometry.fillParts;
        mergeOptionGeometry(geometry, std::move(fin));
        removeFinFillOverlaps(geometry, before);
    } else mergeOptionGeometry(geometry, std::move(fin));
    appendCageAttachmentGuides(settings, geometry, physicalSites, contactBody, protection);
}

AxialWrapData makeCageWrapData(const ShapeSettings& settings, const CageArcMetric& metric,
    bool withPart, const CageArcWideJoin& join) {
    AxialWrapData data;
    const double sweep = std::clamp(settings.circleAngle, 0.0, 2.0 * kPi);
    if (sweep < 1e-12) return data;
    const double first = metric.position((kPi - sweep) * 0.5);
    const double last = metric.position((kPi + sweep) * 0.5);
    const double length = partLength(settings) / metric.periodScale();
    const double width = partWidth(settings), height = partHeight(settings);
    const double depth = settings.partShape <= 1 ? 0.1 * std::cos(kPi / 6.0) * length : 0.1 * length;
    const bool both = withPart && settings.partType == 1;
    double bodyFirst = first, bodyLast = last;
    if (withPart && settings.partShape <= 2 && depth > 0.0 && std::abs(width) > 1e-12) {
        bodyFirst += depth;
        if (both) bodyLast -= depth;
    }
    std::vector<AxialWrapSpoke> ignored;
    if (bodyLast - bodyFirst > 1e-12) addAxialWrapEdge(data.main, ignored,
        bodyFirst, bodyLast, settings.wide ? settings.wideWidth * 0.5 : 0.0,
        settings.wide ? settings.wideWidth * 0.5 : 0.0);
    for (unsigned int index = 0; index < (withPart ? (both ? 2u : 1u) : 0u); ++index) {
        const double anchor = index == 0 ? first : last;
        const double direction = index == 0 ? -1.0 : 1.0;
        std::vector<MPoint> profile;
        if (settings.partShape <= 1) {
            profile = {MPoint(anchor - direction * depth, 0.05 * width, 0),
                MPoint(anchor, 0, 0), MPoint(anchor - direction * depth, -0.05 * width, 0)};
        } else {
            const unsigned int kind = settings.partShape == 2 ? 3 : settings.partShape - 3;
            for (const auto& point : planarEndProfile(kind)) profile.emplace_back(anchor + direction *
                (0.1 * point.x - (kind == 3 ? 0.05 : 0.0)) * length, 0.1 * point.y * width, 0);
        }
        addAxialWrapProfile(data.heads, data.spokes, profile);
        if (settings.partShape == 1) {
            const double base = anchor - direction * depth;
            addAxialWrapProfile(data.crest, data.crestSpokes,
                {MPoint(base, 0, 0), MPoint(base, 0.05 * std::abs(height), 0), MPoint(anchor, 0, 0)});
        }
    }
    data.main.insert(data.main.end(), data.heads.begin(), data.heads.end());
    for (unsigned int i = 0; i <= kCircleSegments; ++i) data.slices.push_back(
        metric.position(2.0 * kPi * i / kCircleSegments));
    std::vector<double> joinAngles;
    appendCageArcWideJoinAngles(joinAngles, metric, join, 0.0, 2.0 * kPi);
    for (double angle : joinAngles) data.slices.push_back(metric.position(angle));
    appendAxialWrapCuts(data.slices, data.main);
    appendAxialWrapCuts(data.slices, data.crest);
    for (const auto& spoke : data.spokes) data.slices.push_back(spoke.position);
    for (const auto& spoke : data.crestSpokes) data.slices.push_back(spoke.position);
    std::sort(data.slices.begin(), data.slices.end());
    data.slices.erase(std::unique(data.slices.begin(), data.slices.end(), [](double a, double b) {
        return std::abs(a - b) < 1e-12;
    }), data.slices.end());
    return data;
}

MPoint cageWrapPoint(const CageArcMetric& metric, double position, double width,
    double height, bool axial, const CageArcWideJoin& join) {
    const double angle = metric.angle(position);
    const auto point = cageArcWideJoinedPoint(metric.point(angle), join);
    const auto normal = metric.normal(angle), binormal = metric.binormal(angle);
    if (!axial && width < 0.0) {
        const auto center = cagePoint(cageBaseBodyPoint(MPoint::origin, metric.settings), metric.settings);
        width = std::max(width, -std::max(0.0, (point - center) * normal));
    }
    return point + (axial ? binormal : normal) * width + (axial ? normal : binormal) * height;
}

void appendCageWrapFaces(PartBuilder& builder, const std::vector<AxialWrapInterval>& intervals,
    const CageArcMetric& metric, bool axial, bool crest, double heightSign, const CageArcWideJoin& join) {
    for (const auto& interval : intervals) {
        if (!interval.active) continue;
        const auto a = cageWrapPoint(metric, interval.first, 0, 0, axial, join);
        const auto b = cageWrapPoint(metric, interval.last, 0, 0, axial, join);
        if (crest) {
            builder.quad(a, b, cageWrapPoint(metric, interval.last, 0, interval.lastHeight * heightSign, axial, join),
                cageWrapPoint(metric, interval.first, 0, interval.firstHeight * heightSign, axial, join));
        } else {
            builder.quad(cageWrapPoint(metric, interval.first, -interval.firstHeight, 0, axial, join),
                cageWrapPoint(metric, interval.last, -interval.lastHeight, 0, axial, join), b, a);
            builder.quad(a, b, cageWrapPoint(metric, interval.last, interval.lastHeight, 0, axial, join),
                cageWrapPoint(metric, interval.first, interval.firstHeight, 0, axial, join));
        }
    }
}

void appendCageWrapBoundary(AxialWrapSegments& segments,
    const std::vector<AxialWrapInterval>& intervals, const std::vector<AxialWrapSpoke>& spokes,
    const CageArcMetric& metric, bool axial, bool crest, bool openArrow, double heightSign,
    const CageArcWideJoin& join) {
    const auto point = [&](double position, double extent) {
        return cageWrapPoint(metric, position, crest ? 0.0 : extent,
            crest ? extent * heightSign : 0.0, axial, join);
    };
    for (const auto& interval : intervals) {
        if (!interval.active) continue;
        if (crest || interval.firstHeight > 1e-12 || interval.lastHeight > 1e-12) {
            addAxialWrapSegment(segments, point(interval.first, interval.firstHeight), point(interval.last, interval.lastHeight));
            if (!crest) addAxialWrapSegment(segments, point(interval.first, -interval.firstHeight), point(interval.last, -interval.lastHeight));
        } else addAxialWrapSegment(segments, point(interval.first, 0), point(interval.last, 0));
        if (openArrow && !crest) addAxialWrapSegment(segments, point(interval.first, 0), point(interval.last, 0));
    }
    if (intervals.empty()) return;
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
        for (const auto& spoke : spokes) if (std::abs(spoke.position - next.first) < 1e-12) spokeHeight = std::max(spokeHeight, spoke.height);
        if (spokeHeight - high > 1e-12) {
            addAxialWrapSegment(segments, point(next.first, high), point(next.first, spokeHeight));
            if (!crest) addAxialWrapSegment(segments, point(next.first, -high), point(next.first, -spokeHeight));
        }
    }
}

bool appendCageWrappedAttachments(const ShapeSettings& settings, PartGeometry& geometry,
    std::vector<OptionClipVolume>* templateProtection) {
    const short outline = outlinePresetIndex(settings.shape);
    if (!settings.part || !isArcOutline(outline) || settings.partShape > 5 || settings.partType == 2) return false;
    const bool axial = isAxialArcOutline(outline);
    const unsigned int count = crossCircleBaseOutline(outline) >= 0 ? 2 : 1;
    const double heightSign = partHeight(settings) < 0.0 ? -1.0 : 1.0;
    const auto join = cageArcWideJoin(settings);
    PartGeometry result;
    for (unsigned int index = 0; index < count; ++index) {
        const CageArcMetric metric(settings, index != 0);
        const bool withPart = index == 0 || settings.partType == 1;
        const auto center = cageBodyPoint(MPoint::origin, settings);
        bool hasPlane = false;
        for (unsigned int sample = 0; sample < 8; ++sample) {
            const auto first = metric.point(2.0 * kPi * sample / 8.0) - center;
            const auto last = metric.point(2.0 * kPi * (sample + 1) / 8.0) - center;
            const auto cross = first ^ last;
            hasPlane = hasPlane || std::hypot(cross.x, cross.y, cross.z) > 0.0;
        }
        const bool curvedPart = withPart && hasPlane && !metric.degenerate();
        const auto data = makeCageWrapData(settings, metric, curvedPart, join);
        const auto main = axialWrapIntervals(data.slices, data.main);
        const auto crest = axialWrapIntervals(data.slices, data.crest);
        PartBuilder builder(settings.fill || join.top || join.bottom);
        appendCageWrapFaces(builder, main, metric, axial, false, heightSign, join);
        appendCageWrapFaces(builder, crest, metric, axial, true, heightSign, join);
        AxialWrapSegments segments;
        const bool openArrow = !settings.wide && !settings.fill && settings.partShape <= 1 && curvedPart;
        appendCageWrapBoundary(segments, main, data.spokes, metric, axial, false, openArrow, heightSign, join);
        appendCageWrapBoundary(segments, crest, data.crestSpokes, metric, axial, true, false, heightSign, join);
        appendAxialWrapStrokes(builder, std::move(segments));
        mergeOptionGeometry(result, std::move(builder.geometry));
        if (templateProtection && curvedPart) {
            PartBuilder heads(true);
            appendCageWrapFaces(heads, axialWrapIntervals(data.slices, data.heads), metric, axial, false, heightSign, join);
            appendCageWrapFaces(heads, crest, metric, axial, true, heightSign, join);
            auto volumes = cageAttachmentBodyVolumes(heads.geometry, false, MPoint::origin);
            templateProtection->insert(templateProtection->end(), volumes.begin(), volumes.end());
        }
        if (withPart && !curvedPart) {
            // 一方の円平面だけが潰れたCrossでも、残る円の巻き付けを維持する。
            const double sweep = std::clamp(settings.circleAngle, 0.0, 2.0 * kPi);
            const double first = (kPi - sweep) * 0.5, last = (kPi + sweep) * 0.5;
            std::vector<OptionSite> sites;
            for (unsigned int end = 0; end < (settings.partType == 1 ? 2u : 1u); ++end) {
                const double theta = end == 0 ? first : last;
                sites.push_back({metric.point(theta), metric.tangent(theta) * (end == 0 ? -1.0 : 1.0),
                    axial ? metric.binormal(theta) * (end == 0 ? 1.0 : -1.0) : metric.normal(theta), false});
            }
            auto physical = settings;
            physical.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
            physical.baseSpacePlus = MVector(0.5, 0.5, 0.5);
            auto heads = makeOptionHeads(physical, false, &sites);
            trimOptionGeometry(result, heads.volumes, settings.fill);
            mergeOptionGeometry(result, std::move(heads.geometry));
            if (templateProtection) templateProtection->insert(templateProtection->end(), heads.volumes.begin(), heads.volumes.end());
        }
    }
    finishCageArcWideJoin(result, join);
    if (!settings.fill) result.fillParts.clear();
    geometry = std::move(result);
    return true;
}
