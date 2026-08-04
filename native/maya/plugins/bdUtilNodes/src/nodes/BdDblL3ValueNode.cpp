#include "bdUtilNodes/nodes/BdDblL3ValueNode.h"

#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>

#include "bdUtilNodes/attributes/DoubleLinear3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"

const MString BdDblL3ValueNode::typeName("bdDblL3_Value");
const MTypeId BdDblL3ValueNode::typeId(0x0007F036);

MObject BdDblL3ValueNode::value;
MObject BdDblL3ValueNode::valueX;
MObject BdDblL3ValueNode::valueY;
MObject BdDblL3ValueNode::valueZ;

void* BdDblL3ValueNode::creator() {
    return new BdDblL3ValueNode();
}

MStatus BdDblL3ValueNode::initialize() {
    MFnNumericAttribute attributeFn;
    MFnUnitAttribute unitAttributeFn;

    MStatus status = bd_util_nodes::createDoubleLinear3Attribute(
        attributeFn,
        unitAttributeFn,
        value,
        valueX,
        valueY,
        valueZ,
        "value",
        "v",
        "valueX",
        "vx",
        "valueY",
        "vy",
        "valueZ",
        "vz",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }

    return addAttribute(value);
}
