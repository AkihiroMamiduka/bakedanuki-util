#pragma once

#include <maya/MFnEnumAttribute.h>
#include <maya/MVector.h>

namespace bdUtilNodes {

inline MObject createSignedAxisAttribute(
    const char* name, const char* shortName, short defaultValue, MStatus& status
) {
    MFnEnumAttribute fn;
    const auto attribute = fn.create(name, shortName, defaultValue, &status);
    if (!status) return attribute;
    const char* fields[] = {"+X", "-X", "+Y", "-Y", "+Z", "-Z"};
    for (short index = 0; index < 6; ++index) {
        status = fn.addField(fields[index], index);
        if (!status) break;
    }
    return attribute;
}

struct SignedShapeAxis {
    unsigned int component;
    double sign;

    MVector vector() const {
        MVector result;
        result[component] = sign;
        return result;
    }
};

constexpr SignedShapeAxis signedShapeAxis(short value) {
    if (value < 0 || value > 5) return {0, 1.0};
    return {static_cast<unsigned int>(value / 2), value % 2 ? -1.0 : 1.0};
}

struct SignedShapeAxes {
    SignedShapeAxis first;
    SignedShapeAxis second;
};

constexpr SignedShapeAxes resolveSignedShapeAxes(short first, short second) {
    const auto firstAxis = signedShapeAxis(first);
    auto secondAxis = signedShapeAxis(second);
    if (firstAxis.component == secondAxis.component) {
        secondAxis = {firstAxis.component == 1 ? 2U : 1U, 1.0};
    }
    return {firstAxis, secondAxis};
}

}  // namespace bdUtilNodes
