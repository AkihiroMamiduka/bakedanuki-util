# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_breakout import OutputsField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField


class MASH_Breakout(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Breakout"

    outputs = OutputsField(multi=True)

    # TODO: outputs.translateX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: outputs.translateY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: outputs.translateZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: outputs.rotateX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: outputs.rotateY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: outputs.rotateZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: outputs.scaleX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: outputs.scaleY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: outputs.scaleZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: outputs.colorX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: outputs.colorY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: outputs.colorZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: outputs.velocityVectorX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: outputs.velocityVectorY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: outputs.velocityVectorZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: outputs.angularVelocityVectorX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: outputs.angularVelocityVectorY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: outputs.angularVelocityVectorZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    inputPoints = TypedField()

    idStart = LongField()
