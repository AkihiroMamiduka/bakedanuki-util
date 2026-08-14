#include "bdUtilNodes/nodes/BdDblLRightTriangleNode.h"

#include <cmath>
#include <tuple>
#include <utility>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"

namespace {

enum class SolveFor : short {
    kHypotenuse = 0,
    kLegA = 1,
    kLegB = 2,
};

struct TriangleResult {
    double output;
    bool isValid;
};

TriangleResult invalidResult() {
    return {0.0, false};
}

TriangleResult solveHypotenuse(double legA, double legB) {
    const double normalizedLegA = std::abs(legA);
    const double normalizedLegB = std::abs(legB);
    if (!std::isfinite(normalizedLegA)
        || !std::isfinite(normalizedLegB)) {
        return invalidResult();
    }

    const double result = std::hypot(normalizedLegA, normalizedLegB);
    if (!std::isfinite(result)) {
        return invalidResult();
    }
    return {result, true};
}

TriangleResult solveLeg(double hypotenuse, double knownLeg) {
    const double normalizedHypotenuse = std::abs(hypotenuse);
    const double normalizedKnownLeg = std::abs(knownLeg);
    if (!std::isfinite(normalizedHypotenuse)
        || !std::isfinite(normalizedKnownLeg)
        || normalizedHypotenuse < normalizedKnownLeg) {
        return invalidResult();
    }
    if (normalizedHypotenuse == 0.0) {
        return {0.0, true};
    }

    const double result = std::sqrt(
                              normalizedHypotenuse - normalizedKnownLeg
                          )
        * std::sqrt(normalizedHypotenuse)
        * std::sqrt(
            1.0 + normalizedKnownLeg / normalizedHypotenuse
        );
    if (!std::isfinite(result)) {
        return invalidResult();
    }
    return {result, true};
}

}  // namespace

const MString BdDblLRightTriangleNode::typeName(
    "bdDblL_RightTriangle"
);
const MTypeId BdDblLRightTriangleNode::typeId(0x001426E8);

MObject BdDblLRightTriangleNode::solveFor;
MObject BdDblLRightTriangleNode::legA;
MObject BdDblLRightTriangleNode::legB;
MObject BdDblLRightTriangleNode::hypotenuse;
MObject BdDblLRightTriangleNode::output;
MObject BdDblLRightTriangleNode::isValid;

void* BdDblLRightTriangleNode::creator() {
    return new BdDblLRightTriangleNode();
}

MStatus BdDblLRightTriangleNode::initialize() {
    MStatus status;
    MFnEnumAttribute enumAttributeFn;
    solveFor = enumAttributeFn.create(
        "solveFor",
        "sf",
        static_cast<short>(SolveFor::kHypotenuse),
        &status
    );
    if (!status) {
        return status;
    }
    for (const auto& field : {
             std::pair<const char*, SolveFor>{
                 "Hypotenuse",
                 SolveFor::kHypotenuse,
             },
             std::pair<const char*, SolveFor>{"LegA", SolveFor::kLegA},
             std::pair<const char*, SolveFor>{"LegB", SolveFor::kLegB},
         }) {
        status = enumAttributeFn.addField(
            field.first,
            static_cast<short>(field.second)
        );
        if (!status) {
            return status;
        }
    }
    status = enumAttributeFn.setReadable(true);
    if (!status) {
        return status;
    }
    status = enumAttributeFn.setWritable(true);
    if (!status) {
        return status;
    }
    status = enumAttributeFn.setStorable(true);
    if (!status) {
        return status;
    }
    status = enumAttributeFn.setKeyable(true);
    if (!status) {
        return status;
    }
    status = addAttribute(solveFor);
    if (!status) {
        return status;
    }

    MFnUnitAttribute unitAttributeFn;
    for (const auto& definition : {
             std::tuple<MObject*, const char*, const char*>{
                 &legA,
                 "legA",
                 "la",
             },
             std::tuple<MObject*, const char*, const char*>{
                 &legB,
                 "legB",
                 "lb",
             },
             std::tuple<MObject*, const char*, const char*>{
                 &hypotenuse,
                 "hypotenuse",
                 "h",
             },
         }) {
        status = bd_util_nodes::createDoubleLinearAttribute(
            unitAttributeFn,
            *std::get<0>(definition),
            std::get<1>(definition),
            std::get<2>(definition),
            0.0
        );
        if (!status) {
            return status;
        }
        status = bd_util_nodes::configureInputUnitAttribute(
            unitAttributeFn
        );
        if (!status) {
            return status;
        }
        status = addAttribute(*std::get<0>(definition));
        if (!status) {
            return status;
        }
    }

    status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        output,
        "output",
        "o",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureOutputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(output);
    if (!status) {
        return status;
    }

    MFnNumericAttribute numericAttributeFn;
    status = bd_util_nodes::createBooleanAttribute(
        numericAttributeFn,
        isValid,
        "isValid",
        "iv",
        true
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureOutputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }
    status = addAttribute(isValid);
    if (!status) {
        return status;
    }

    for (const MObject& inputAttribute : {
             solveFor,
             legA,
             legB,
             hypotenuse,
         }) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
        status = attributeAffects(inputAttribute, isValid);
        if (!status) {
            return status;
        }
    }
    return MS::kSuccess;
}

MStatus BdDblLRightTriangleNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    const MObject requestedAttribute = plug.attribute();
    if (requestedAttribute != output && requestedAttribute != isValid) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    const short solveForValue = dataBlock.inputValue(
        solveFor,
        &status
    ).asShort();
    if (!status) {
        return status;
    }
    const double legAValue = dataBlock.inputValue(legA, &status).asDouble();
    if (!status) {
        return status;
    }
    const double legBValue = dataBlock.inputValue(legB, &status).asDouble();
    if (!status) {
        return status;
    }
    const double hypotenuseValue = dataBlock.inputValue(
        hypotenuse,
        &status
    ).asDouble();
    if (!status) {
        return status;
    }

    TriangleResult result = invalidResult();
    switch (static_cast<SolveFor>(solveForValue)) {
        case SolveFor::kHypotenuse:
            result = solveHypotenuse(legAValue, legBValue);
            break;
        case SolveFor::kLegA:
            result = solveLeg(hypotenuseValue, legBValue);
            break;
        case SolveFor::kLegB:
            result = solveLeg(hypotenuseValue, legAValue);
            break;
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }
    outputValue.setDouble(result.output);
    outputValue.setClean();

    MDataHandle isValidValue = dataBlock.outputValue(isValid, &status);
    if (!status) {
        return status;
    }
    isValidValue.setBool(result.isValid);
    isValidValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblLRightTriangleNode::schedulingType() const {
    return MPxNode::kParallel;
}
