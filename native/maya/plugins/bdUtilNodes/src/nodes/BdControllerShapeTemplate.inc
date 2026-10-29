// 基準輪郭の論理区間へ表示種別を割り当て、接合後も同じ位置で切り替える。
enum class BodyTemplateDomainKind { Segment, Circle, Arc };
enum class BodyTemplatePattern { NormalMiddle, TemplateMiddle, TemplateStart };

struct BodyTemplateDomain {
    BodyTemplateDomainKind kind = BodyTemplateDomainKind::Segment;
    BodyTemplatePattern pattern = BodyTemplatePattern::NormalMiddle;
    MPoint first;
    MPoint last;
    MPoint center;
    MVector u = MVector(1, 0, 0);
    MVector v = MVector(0, 0, 1);
    double radius = 0.5;
    double start = -kPi;
    double end = kPi;
};

short bodyTemplateBaseOutline(short outline) {
    switch (outline) {
        case 104: return 1;
        case 106: return 53;
        case 117: return 116;
        case 118: return 5;
        case 119: return 45;
        case 111: return 27;
        case 112: return 120;
        case 114: return 113;
        case 115: return 121;
        default: return outline;
    }
}

MPoint bodyTemplateReferencePoint(const MPoint& point, const ShapeSettings& settings) {
    return presetOrientedPoint(point, settings.shape, false);
}

bool bodyTemplateInsidePart(const MPoint& point, const std::vector<OptionClipVolume>& volumes) {
    return std::any_of(volumes.begin(), volumes.end(), [&](const auto& volume) {
        return !volume.empty() && std::all_of(volume.begin(), volume.end(), [&](const auto& plane) {
            return plane.value(point) <= 1e-9;
        });
    });
}

double bodyTemplateAngle(const BodyTemplateDomain& domain, const MPoint& point) {
    const auto relative = point - domain.center;
    return std::atan2(relative * domain.v, relative * domain.u);
}

double bodyTemplateArcAngle(const BodyTemplateDomain& domain, const MPoint& point) {
    const double angle = bodyTemplateAngle(domain, point);
    if (angle >= domain.start && angle <= domain.end) return angle;
    const auto at = [&](double value) {
        return domain.center + (domain.u * std::cos(value) + domain.v * std::sin(value)) * domain.radius;
    };
    return (point - at(domain.start)).length() <= (point - at(domain.end)).length()
        ? domain.start : domain.end;
}

MPoint bodyTemplateClosestPoint(const BodyTemplateDomain& domain, const MPoint& point) {
    if (domain.kind == BodyTemplateDomainKind::Segment) {
        const auto direction = domain.last - domain.first;
        const double squared = direction * direction;
        const double parameter = squared > 1e-20
            ? std::clamp(((point - domain.first) * direction) / squared, 0.0, 1.0) : 0.0;
        return domain.first + direction * parameter;
    }
    const double angle = domain.kind == BodyTemplateDomainKind::Arc
        ? bodyTemplateArcAngle(domain, point) : bodyTemplateAngle(domain, point);
    return domain.center + (domain.u * std::cos(angle) + domain.v * std::sin(angle)) * domain.radius;
}

bool bodyTemplateParameterIsTemplate(double parameter, double rate, BodyTemplatePattern pattern) {
    if (pattern == BodyTemplatePattern::TemplateStart) return parameter < rate;
    if (pattern == BodyTemplatePattern::TemplateMiddle) {
        return parameter > (1.0 - rate) * 0.5 && parameter < (1.0 + rate) * 0.5;
    }
    return parameter < rate * 0.5 || parameter > 1.0 - rate * 0.5;
}

bool bodyTemplateDomainIsTemplate(const BodyTemplateDomain& domain, const MPoint& point, double rate) {
    if (domain.kind == BodyTemplateDomainKind::Circle) {
        const double local = std::remainder(bodyTemplateAngle(domain, point), kPi * 0.5);
        return std::abs(local) > (1.0 - rate) * kPi * 0.25;
    }
    double parameter = 0.0;
    if (domain.kind == BodyTemplateDomainKind::Arc) {
        parameter = (bodyTemplateArcAngle(domain, point) - domain.start) / (domain.end - domain.start);
    } else {
        const auto direction = domain.last - domain.first;
        parameter = std::clamp(((point - domain.first) * direction) / (direction * direction), 0.0, 1.0);
    }
    return bodyTemplateParameterIsTemplate(parameter, rate, domain.pattern);
}

double bodyTemplateConeParameter(const MPoint& point, double offset) {
    constexpr double slantSquared = 1.25;
    const double position = 0.5 - point.x;
    return std::sqrt(std::max(0.0, position * position - offset * offset / slantSquared));
}

bool bodyTemplateIsTemplate(const std::vector<BodyTemplateDomain>& domains, const MPoint& point, double rate,
    const BodyTemplateDomain* fixed = nullptr, double coneOffset = -1.0) {
    if (rate <= 0.0) return false;
    if (rate >= 1.0) return true;
    if (fixed && coneOffset >= 0.0) {
        return bodyTemplateParameterIsTemplate(bodyTemplateConeParameter(point, coneOffset), rate, fixed->pattern);
    }
    if (fixed) return bodyTemplateDomainIsTemplate(*fixed, point, rate);
    const BodyTemplateDomain* closest = nullptr;
    double distance = 1e100;
    for (const auto& domain : domains) {
        const auto difference = point - bodyTemplateClosestPoint(domain, point);
        const double squared = difference * difference;
        if (squared < distance - 1e-16) {
            distance = squared;
            closest = &domain;
        }
    }
    return closest && bodyTemplateDomainIsTemplate(*closest, point, rate);
}

void appendBodyTemplateCircle(std::vector<BodyTemplateDomain>& domains,
    const MPoint& center, const MVector& u, const MVector& v, double radius = 0.5) {
    BodyTemplateDomain domain;
    domain.kind = BodyTemplateDomainKind::Circle;
    domain.center = center;
    domain.u = u;
    domain.v = v;
    domain.radius = radius;
    domains.push_back(domain);
}

bool bodyTemplateOnCircle(const MPoint& point, const BodyTemplateDomain& domain) {
    if (domain.kind != BodyTemplateDomainKind::Circle) return false;
    const auto relative = point - domain.center;
    return std::abs(relative * (domain.u ^ domain.v)) < 1e-8 &&
        std::abs(relative.length() - domain.radius) < 1e-8;
}

void mergeBodyTemplateSegments(std::vector<BodyTemplateDomain>& domains) {
    bool changed = true;
    while (changed) {
        changed = false;
        for (std::size_t i = 0; i < domains.size(); ++i) {
            if (domains[i].kind != BodyTemplateDomainKind::Segment) continue;
            const auto direction = domains[i].last - domains[i].first;
            const double length = direction.length();
            const auto along = direction / length;
            for (std::size_t j = i + 1; j < domains.size(); ++j) {
                if (domains[j].kind != BodyTemplateDomainKind::Segment) continue;
                const auto first = domains[j].first - domains[i].first;
                const auto last = domains[j].last - domains[i].first;
                if ((first ^ along).length() > 1e-8 || (last ^ along).length() > 1e-8) continue;
                const double low = std::min(first * along, last * along);
                const double high = std::max(first * along, last * along);
                if (low > length + 1e-8 || high < -1e-8) continue;
                const auto origin = domains[i].first;
                domains[i].first = origin + along * std::min(0.0, low);
                domains[i].last = origin + along * std::max(length, high);
                domains.erase(domains.begin() + j);
                changed = true;
                break;
            }
            if (changed) break;
        }
    }
}

std::vector<BodyTemplateDomain> bodyTemplateDomains(
    const ShapeSettings& settings, const BdControllerShapeNode::Geometry& reference
) {
    const short outline = bodyTemplateBaseOutline(outlinePresetIndex(settings.shape));
    std::vector<BodyTemplateDomain> domains;
    if (isArcOutline(outline)) {
        const double sweep = std::clamp(settings.circleAngle, 0.0, 2.0 * kPi);
        if (sweep < 1e-12) return domains;
        BodyTemplateDomain domain;
        domain.kind = BodyTemplateDomainKind::Arc;
        domain.u = MVector(1, 0, 0);
        domain.v = MVector(0, 0, -1);
        domain.start = -sweep * 0.5;
        domain.end = sweep * 0.5;
        const bool cross = crossCircleBaseOutline(outline) >= 0;
        domain.pattern = settings.part && settings.partType == 2
            ? BodyTemplatePattern::NormalMiddle
            : settings.part && settings.partType == 0 && !cross
                ? BodyTemplatePattern::TemplateStart : BodyTemplatePattern::TemplateMiddle;
        domains.push_back(domain);
        if (cross) {
            domain.v = MVector(0, 1, 0);
            domains.push_back(domain);
        }
        return domains;
    }
    // 円はストロークの分割位置ではなく、各本体の基準円から論理区間を決める。
    if (outline == 116 || outline == 0) {
        appendBodyTemplateCircle(domains, MPoint::origin, MVector(1, 0, 0), MVector(0, 0, 1),
            outline == 0 ? 0.5 * 0.275 : 0.5);
        if (outline == 116) return domains;
    } else if (outline == 33 || outline == 46 || outline == 47) {
        appendBodyTemplateCircle(domains, MPoint::origin, MVector(1, 0, 0), MVector(0, 0, 1));
        appendBodyTemplateCircle(domains, MPoint::origin, MVector(1, 0, 0), MVector(0, 1, 0));
        appendBodyTemplateCircle(domains, MPoint::origin, MVector(0, 1, 0), MVector(0, 0, 1));
        return domains;
    } else if (outline == 36 || outline == 43) {
        appendBodyTemplateCircle(domains, MPoint(-0.5, 0, 0), MVector(0, 1, 0), MVector(0, 0, 1));
        if (outline == 36) {
            appendBodyTemplateCircle(domains, MPoint(0.5, 0, 0), MVector(0, 1, 0), MVector(0, 0, 1));
        }
    }
    for (const auto& source : reference.strokes) {
        MPointArray stroke;
        for (const auto& point : source) stroke.append(bodyTemplateReferencePoint(point, settings));
        for (unsigned int i = 1; i < stroke.length(); ++i) {
            if ((stroke[i] - stroke[i - 1]).length() < 1e-10) continue;
            if (std::any_of(domains.begin(), domains.end(), [&](const auto& domain) {
                return bodyTemplateOnCircle(stroke[i - 1], domain) && bodyTemplateOnCircle(stroke[i], domain);
            })) continue;
            BodyTemplateDomain domain;
            domain.first = stroke[i - 1];
            domain.last = stroke[i];
            domains.push_back(domain);
        }
    }
    mergeBodyTemplateSegments(domains);
    const bool line = outline == 1;
    const bool cross = outline == 4 || outline == 5 || outline == 45 || outline == 52 || outline == 53;
    if (line || cross) for (auto& domain : domains) {
        if (domain.kind != BodyTemplateDomainKind::Segment) continue;
        domain.pattern = line && settings.part && settings.partType != 1
            ? BodyTemplatePattern::TemplateStart : BodyTemplatePattern::TemplateMiddle;
        if (line && domain.first.x > domain.last.x) std::swap(domain.first, domain.last);
    }
    return domains;
}

const BodyTemplateDomain* bodyTemplateStrokeDomain(
    const std::vector<BodyTemplateDomain>& domains, const MPointArray& stroke, bool onlyCurves
) {
    if (stroke.length() < (onlyCurves ? 2u : 3u)) return nullptr;
    MVector sum = MVector::zero;
    for (const auto& point : stroke) sum += point - MPoint::origin;
    const auto center = MPoint::origin + sum / stroke.length();
    const BodyTemplateDomain* closest = nullptr;
    double distance = 1e100;
    for (const auto& domain : domains) {
        if (domain.kind == BodyTemplateDomainKind::Segment) continue;
        const auto normal = (domain.u ^ domain.v).normal();
        const double plane = (stroke[0] - domain.center) * normal;
        const auto radial = [&](const MPoint& point) {
            const auto relative = point - domain.center;
            const double u = relative * domain.u, v = relative * domain.v;
            return std::sqrt(u * u + v * v);
        };
        const double radius = radial(stroke[0]);
        if (!std::all_of(stroke.begin(), stroke.end(), [&](const auto& point) {
            return std::abs((point - domain.center) * normal - plane) < 1e-8 &&
                (onlyCurves || std::abs(radial(point) - radius) < 1e-6);
        })) continue;
        const auto difference = center - domain.center;
        const double squared = difference * difference;
        if (squared < distance - 1e-16) {
            distance = squared;
            closest = &domain;
        }
    }
    return closest;
}

struct BodyTemplateGeneratorMapping {
    const BodyTemplateDomain* domain = nullptr;
    double coneOffset = -1.0;
};

const BodyTemplateDomain* bodyTemplateSegmentDomain(
    const std::vector<BodyTemplateDomain>& domains, const MPointArray& stroke
) {
    if (stroke.length() < 2 || (stroke[stroke.length() - 1] - stroke[0]).length() < 1e-10) return nullptr;
    const BodyTemplateDomain* closest = nullptr;
    double distance = 1e100;
    for (const auto& domain : domains) {
        if (domain.kind != BodyTemplateDomainKind::Segment) continue;
        const auto direction = (domain.last - domain.first).normal();
        if (!std::all_of(stroke.begin(), stroke.end(), [&](const auto& point) {
            return ((point - stroke[0]) ^ direction).length() < 1e-8;
        })) continue;
        double squared = 0.0;
        for (const auto& point : stroke) {
            const auto delta = point - bodyTemplateClosestPoint(domain, point);
            squared += delta * delta;
        }
        if (squared < distance - 1e-16) {
            distance = squared;
            closest = &domain;
        }
    }
    return closest;
}

BodyTemplateGeneratorMapping bodyTemplateGeneratorDomain(const ShapeSettings& settings,
    const std::vector<BodyTemplateDomain>& domains, const MPointArray& stroke) {
    const short outline = outlinePresetIndex(settings.shape);
    if ((outline != 36 && outline != 43) || stroke.length() < 2) return {};
    const double span = stroke[stroke.length() - 1].x - stroke[0].x;
    if (std::abs(span) < 1e-10) return {};
    for (unsigned int i = 1; i < stroke.length(); ++i) {
        if ((stroke[i].x - stroke[i - 1].x) * span < -1e-12) return {};
    }
    BodyTemplateGeneratorMapping result;
    double distance = 1e100;
    const auto remember = [&](double squared, const auto& domain, double offset) {
        if (squared < distance - 1e-16) {
            distance = squared;
            result = {&domain, offset};
        }
    };
    for (const auto& domain : domains) {
        if (domain.kind != BodyTemplateDomainKind::Segment || std::abs(domain.last.x - domain.first.x) < 1e-10) continue;
        const auto direction = (domain.last - domain.first).normal();
        if (outline == 36 && !std::all_of(stroke.begin(), stroke.end(), [&](const auto& point) {
            return ((point - stroke[0]) ^ direction).length() < 1e-8;
        })) continue;
        double squared = 0.0;
        for (const auto& point : stroke) {
            const auto delta = point - bodyTemplateClosestPoint(domain, point);
            squared += delta * delta;
        }
        remember(squared, domain, -1.0);
        if (outline != 43 || !settings.wide || settings.wideWidth <= 1e-12) continue;
        const auto base = domain.first.x < domain.last.x ? domain.first : domain.last;
        const double angle = std::atan2(base.z, base.y);
        const double slant = std::sqrt(1.25), ratio = 0.5 / slant;
        const double offset = settings.wideWidth * 0.5;
        // 円錐を展開して作った平行曲線を照合し、近頂点でも別の母線へ移さない。
        for (double sign : {-1.0, 1.0}) {
            squared = 0.0;
            for (const auto& point : stroke) {
                const double position = 0.5 - point.x;
                const double along = position * slant;
                if (along < offset - 1e-8) { squared = 1e100; break; }
                const double side = angle + sign * std::asin(std::clamp(offset / along, 0.0, 1.0)) / ratio;
                const auto expected = MPoint(point.x, 0.5 * position * std::cos(side), 0.5 * position * std::sin(side));
                const auto delta = point - expected;
                squared += delta * delta;
            }
            remember(squared, domain, offset);
        }
    }
    return result;
}

void appendBodyTemplateCut(std::vector<double>& cuts, double first, double last) {
    const double difference = last - first;
    if (std::abs(difference) < 1e-14) return;
    const double parameter = -first / difference;
    if (parameter > 1e-10 && parameter < 1.0 - 1e-10) cuts.push_back(parameter);
}

void appendBodyTemplateConeCuts(std::vector<double>& cuts, const MPoint& first,
    const MPoint& last, double rate, double offset) {
    if (rate <= 0.0 || rate >= 1.0) return;
    for (double parameter : {rate * 0.5, 1.0 - rate * 0.5}) {
        const double position = 0.5 - std::sqrt(parameter * parameter + offset * offset / 1.25);
        appendBodyTemplateCut(cuts, first.x - position, last.x - position);
    }
}

void appendBodyTemplateDomainCuts(std::vector<double>& cuts, const BodyTemplateDomain& domain,
    const MPoint& first, const MPoint& last, double rate) {
    if (rate <= 0.0 || rate >= 1.0) return;
    std::vector<double> boundaries;
    if (domain.kind == BodyTemplateDomainKind::Circle) {
        for (int quarter = -2; quarter <= 2; ++quarter) for (double sign : {-1.0, 1.0}) {
            boundaries.push_back(quarter * kPi * 0.5 + sign * (1.0 - rate) * kPi * 0.25);
        }
    } else {
        if (domain.pattern == BodyTemplatePattern::TemplateStart) boundaries = {rate};
        else if (domain.pattern == BodyTemplatePattern::TemplateMiddle) boundaries = {(1.0 - rate) * 0.5, (1.0 + rate) * 0.5};
        else boundaries = {rate * 0.5, 1.0 - rate * 0.5};
        if (domain.kind == BodyTemplateDomainKind::Arc) {
            for (auto& value : boundaries) value = domain.start + value * (domain.end - domain.start);
            boundaries.push_back(domain.start);
            boundaries.push_back(domain.end);
        }
    }
    for (double boundary : boundaries) {
        if (domain.kind == BodyTemplateDomainKind::Segment) {
            const auto direction = domain.last - domain.first;
            const double squared = direction * direction;
            appendBodyTemplateCut(cuts,
                ((first - domain.first) * direction) / squared - boundary,
                ((last - domain.first) * direction) / squared - boundary);
        } else {
            const auto a = first - domain.center;
            const auto b = last - domain.center;
            const double cosine = std::cos(boundary), sine = std::sin(boundary);
            const double firstSide = (a * domain.v) * cosine - (a * domain.u) * sine;
            const double lastSide = (b * domain.v) * cosine - (b * domain.u) * sine;
            const double difference = lastSide - firstSide;
            if (std::abs(difference) < 1e-14) continue;
            const double parameter = -firstSide / difference;
            if (parameter <= 1e-10 || parameter >= 1.0 - 1e-10) continue;
            const auto relative = a + (b - a) * parameter;
            if ((relative * domain.u) * cosine + (relative * domain.v) * sine >= -1e-10) cuts.push_back(parameter);
        }
    }
}

void applyBodyTemplateLines(const ShapeSettings& settings, BdControllerShapeNode::Geometry& geometry,
    const BdControllerShapeNode::Geometry& reference, const std::vector<OptionClipVolume>& protectedParts) {
    const double rate = std::clamp(settings.templateLineRate, 0.0, 1.0);
    const auto domains = bodyTemplateDomains(settings, reference);
    const bool onlyCurves = !domains.empty() && std::all_of(domains.begin(), domains.end(), [](const auto& domain) {
        return domain.kind != BodyTemplateDomainKind::Segment;
    });
    Strokes strokes;
    std::vector<StrokeStyle> styles;
    for (std::size_t index = 0; index < geometry.strokes.size(); ++index) {
        const auto& source = geometry.strokes[index];
        MPointArray referenceStroke;
        for (const auto& point : source) referenceStroke.append(bodyTemplateReferencePoint(point, settings));
        // 追加した小円も元の円平面へ固定し、交差する別の大円へ区間が移るのを防ぐ。
        const auto* strokeDomain = bodyTemplateStrokeDomain(domains, referenceStroke, onlyCurves);
        const auto generator = strokeDomain ? BodyTemplateGeneratorMapping{}
            : bodyTemplateGeneratorDomain(settings, domains, referenceStroke);
        const auto* segmentDomain = !strokeDomain && !generator.domain
            ? bodyTemplateSegmentDomain(domains, referenceStroke) : nullptr;
        const auto original = geometry.strokeStyles[index];
        const auto normal = original == StrokeStyle::Template ? StrokeStyle::Normal : original;
        const std::size_t begin = strokes.size();
        MPointArray active;
        StrokeStyle activeStyle = normal;
        const auto flush = [&] {
            if (active.length() >= 2) {
                strokes.push_back(std::move(active));
                styles.push_back(activeStyle);
            }
            active = MPointArray();
        };
        const auto append = [&](const MPoint& first, const MPoint& last, StrokeStyle style) {
            if ((last - first).length() < 1e-12) return;
            if (active.length() == 0 || style != activeStyle || (active[active.length() - 1] - first).length() > 1e-9) {
                flush();
                activeStyle = style;
                active.append(first);
            }
            active.append(last);
        };
        for (unsigned int i = 1; i < source.length(); ++i) {
            const auto a = source[i - 1], b = source[i];
            const auto first = referenceStroke[i - 1], last = referenceStroke[i];
            const auto* domain = strokeDomain ? strokeDomain : generator.domain ? generator.domain : segmentDomain;
            double coneOffset = generator.coneOffset;
            // 接合で二点片へ分解された円弧も、平面に平行な弦なら同じ親円へ揃える。
            if (!domain && onlyCurves) {
                MPointArray fragment;
                fragment.append(first);
                fragment.append(last);
                domain = bodyTemplateStrokeDomain(domains, fragment, true);
            } else if (!domain) {
                MPointArray fragment;
                fragment.append(first);
                fragment.append(last);
                const auto mapping = bodyTemplateGeneratorDomain(settings, domains, fragment);
                domain = mapping.domain ? mapping.domain : bodyTemplateSegmentDomain(domains, fragment);
                coneOffset = mapping.coneOffset;
            }
            std::vector<double> cuts = {0.0, 1.0};
            if (coneOffset >= 0.0) appendBodyTemplateConeCuts(cuts, first, last, rate, coneOffset);
            else if (domain) appendBodyTemplateDomainCuts(cuts, *domain, first, last, rate);
            else for (const auto& candidate : domains) appendBodyTemplateDomainCuts(cuts, candidate, first, last, rate);
            for (const auto& volume : protectedParts) for (const auto& plane : volume) {
                appendBodyTemplateCut(cuts, plane.value(a), plane.value(b));
            }
            std::sort(cuts.begin(), cuts.end());
            cuts.erase(std::unique(cuts.begin(), cuts.end(), [](double x, double y) { return std::abs(x - y) < 1e-10; }), cuts.end());
            double start = cuts.front();
            StrokeStyle previous = original;
            for (std::size_t cut = 1; cut < cuts.size(); ++cut) {
                const double middle = (cuts[cut - 1] + cuts[cut]) * 0.5;
                const auto point = a + (b - a) * middle;
                const auto style = bodyTemplateInsidePart(point, protectedParts) ? original
                    : bodyTemplateIsTemplate(domains, first + (last - first) * middle, rate, domain, coneOffset)
                        ? StrokeStyle::Template : normal;
                if (cut > 1 && style != previous) {
                    append(a + (b - a) * start, a + (b - a) * cuts[cut - 1], previous);
                    start = cuts[cut - 1];
                }
                previous = style;
            }
            append(a + (b - a) * start, b, previous);
        }
        flush();
        // 閉輪郭の始終端で同じ表示区間を分断せず、透明な線の端点重複を避ける。
        if (strokes.size() > begin + 1 && styles[begin] == styles.back() &&
            (strokes[begin][0] - strokes.back()[strokes.back().length() - 1]).length() < 1e-9) {
            MPointArray joined = strokes.back();
            for (unsigned int i = 1; i < strokes[begin].length(); ++i) joined.append(strokes[begin][i]);
            strokes[begin] = std::move(joined);
            strokes.pop_back();
            styles.pop_back();
        }
    }
    geometry.strokes = std::move(strokes);
    geometry.strokeStyles = std::move(styles);
}

std::vector<MPoint> bodyTemplateInsidePolygon(std::vector<MPoint> polygon, const OptionClipVolume& volume) {
    for (const auto& plane : volume) {
        if (polygon.empty()) break;
        std::vector<MPoint> inside;
        for (std::size_t i = 0; i < polygon.size(); ++i) {
            const auto a = polygon[i], b = polygon[(i + 1) % polygon.size()];
            double first = plane.value(a), last = plane.value(b);
            if (std::abs(first) < 1e-10) first = 0.0;
            if (std::abs(last) < 1e-10) last = 0.0;
            if (first <= 0.0) inside.push_back(a);
            if ((first < 0.0 && last > 0.0) || (first > 0.0 && last < 0.0)) {
                inside.push_back(a + (b - a) * (first / (first - last)));
            }
        }
        polygon = std::move(inside);
    }
    return polygon;
}

void applyBodyTemplateFill(BdControllerShapeNode::Geometry& geometry,
    const std::vector<OptionClipVolume>& protectedParts) {
    std::vector<BdControllerShapeNode::Geometry::FillPart> result;
    for (const auto& part : geometry.fillParts) {
        if (part.marker) {
            result.push_back(part);
            continue;
        }
        PartBuilder protectedFaces(true), templateFaces(true);
        for (unsigned int i = 0; i + 2 < part.triangles.length(); i += 3) {
            PartPolygons pieces = {{part.triangles[i], part.triangles[i + 1], part.triangles[i + 2]}};
            for (const auto& volume : protectedParts) {
                if (volume.empty()) continue;
                PartPolygons outside;
                for (const auto& piece : pieces) {
                    const auto inside = bodyTemplateInsidePolygon(piece, volume);
                    if (inside.size() >= 3) protectedFaces.polygon(inside, part.style);
                    for (auto& remaining : outsideOptionVolume(piece, volume)) outside.push_back(std::move(remaining));
                }
                pieces = std::move(outside);
            }
            for (const auto& piece : pieces) templateFaces.polygon(piece, StrokeStyle::Template);
        }
        for (auto* faces : {&protectedFaces, &templateFaces}) for (auto& face : faces->geometry.fillParts) {
            face.marker = part.marker;
            face.singleSided = part.singleSided;
            result.push_back(std::move(face));
        }
    }
    geometry.fillParts = std::move(result);
}

void applyBodyTemplate(const ShapeSettings& settings, BdControllerShapeNode::Geometry& geometry,
    const BdControllerShapeNode::Geometry& reference, const std::vector<OptionClipVolume>& protectedParts = {}) {
    if (settings.templateLine) applyBodyTemplateLines(settings, geometry, reference, protectedParts);
    if (settings.templateFill) applyBodyTemplateFill(geometry, protectedParts);
}
