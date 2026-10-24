// 平面Partの輪郭で曲面を切り、面のずれは境界だけで接続する。
struct AxialPlanarJoin {
    OptionClipVolume volume;
    MPoint origin;
    MVector normal;
};

void appendOptionAxialPlanarParts(PartBuilder& builder, const ShapeSettings& settings,
    OptionHeads& heads, const std::vector<OptionSite>& sites, PartGeometry surface) {
    std::vector<AxialPlanarJoin> joins;
    std::vector<OptionClipVolume> volumes;
    for (const auto& site : sites) {
        std::vector<MPoint> profile;
        for (const auto& point : planarEndProfile(settings.partShape - 3)) {
            profile.push_back(site.endpoint + site.along * (point.x * 0.1 * partLength(settings) + settings.partOffset)
                + site.side * (point.y * 0.1 * partWidth(settings)));
        }
        auto volume = optionPlanarVolume(profile);
        if (volume.size() < 5) continue;
        volume.resize(volume.size() - 2);
        // 反対側の円弧を切らないよう、接合する端点側の半空間に限定する。
        volume.push_back({-(site.endpoint - MPoint::origin).normal(), 0.0});
        joins.push_back({volume, profile.front(), (site.along ^ site.side).normal()});
        volumes.push_back(std::move(volume));
    }
    trimOptionGeometry(surface, volumes, true);
    PartBuilder boundary(false);
    appendOptionSurfaceOutline(boundary, surface);
    PartBuilder bridges(true);
    for (const auto& stroke : boundary.geometry.strokes) for (unsigned int i = 1; i < stroke.length(); ++i) {
        const auto a = stroke[i - 1], b = stroke[i];
        for (const auto& join : joins) {
            if (!std::all_of(join.volume.begin(), join.volume.end(), [&](const auto& plane) {
                return plane.value(a) <= 1e-9 && plane.value(b) <= 1e-9;
            })) continue;
            const auto projectedA = a - join.normal * ((a - join.origin) * join.normal);
            const auto projectedB = b - join.normal * ((b - join.origin) * join.normal);
            bridges.quad(a, b, projectedB, projectedA);
            break;
        }
    }
    mergeOptionGeometry(surface, std::move(bridges.geometry));
    ShapeSettings filled = settings;
    filled.fill = true;
    auto planarHeads = makeOptionHeads(filled);
    mergeOptionGeometry(surface, std::move(planarHeads.geometry));
    appendOptionSurfaceOutline(builder, surface);
    // Part面内の線だけを実輪郭で切り、接続面が内部へ着く線も除く。
    for (const auto& join : joins) {
        PartBuilder inPlane(false), other(false);
        for (const auto& stroke : builder.geometry.strokes) for (unsigned int i = 1; i < stroke.length(); ++i) {
            const auto a = stroke[i - 1], b = stroke[i];
            const bool coplanar = std::abs((a - join.origin) * join.normal) < 1e-9 &&
                std::abs((b - join.origin) * join.normal) < 1e-9;
            (coplanar ? inPlane : other).stroke({a, b});
        }
        auto profile = join.volume;
        profile.pop_back();
        trimOptionGeometry(inPlane.geometry, {profile}, false, true);
        mergeOptionGeometry(other.geometry, std::move(inPlane.geometry));
        builder.geometry = std::move(other.geometry);
    }
    if (builder.filled) builder.geometry.fillParts = std::move(surface.fillParts);
    heads.geometry = {};
}
