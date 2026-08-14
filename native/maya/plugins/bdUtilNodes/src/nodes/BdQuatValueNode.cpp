#include "bdUtilNodes/nodes/BdQuatValueNode.h"

#include <maya/MFnNumericAttribute.h>

#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/QuaternionAttribute.h"

const MString BdQuatValueNode::typeName("bdQuat_Value");
const MTypeId BdQuatValueNode::typeId(0x0014270F);

MObject BdQuatValueNode::value;
MObject BdQuatValueNode::valueX;
MObject BdQuatValueNode::valueY;
MObject BdQuatValueNode::valueZ;
MObject BdQuatValueNode::valueW;

void* BdQuatValueNode::creator() {
    return new BdQuatValueNode();
}

MStatus BdQuatValueNode::initialize() {
    MFnNumericAttribute attributeFn;

    MStatus status = bd_util_nodes::createQuaternionAttribute(
        attributeFn,
        value,
        valueX,
        valueY,
        valueZ,
        valueW,
        "value",
        "v",
        "valueX",
        "vx",
        "valueY",
        "vy",
        "valueZ",
        "vz",
        "valueW",
        "vw"
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
