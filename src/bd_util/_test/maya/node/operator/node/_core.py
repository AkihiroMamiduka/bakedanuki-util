# coding: utf-8
"""
Node クラスの名前系プロパティ（namespace / local_name）のテスト・デモ
"""
from ...... import logger as u_logger
from ......maya.node.operator.node._core import Node

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    namespace_with_namespace()
    namespace_without_namespace()
    namespace_multi_level()
    local_name_with_namespace()
    local_name_without_namespace()
    local_name_multi_level()


def namespace_with_namespace():
    logger.debug("===========================================================")
    logger.debug("--- namespace: ネームスペースあり ---")
    node = Node("ns1:myNode")
    logger.debug(
        "{}: {}".format(
            "node.name",
            node.name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.namespace",
            node.namespace,
        )
    )
    # 期待値: "ns1"


def namespace_without_namespace():
    logger.debug("===========================================================")
    logger.debug("--- namespace: ネームスペースなし ---")
    node = Node("myNode")
    logger.debug(
        "{}: {}".format(
            "node.name",
            node.name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.namespace",
            node.namespace,
        )
    )
    # 期待値: ""


def namespace_multi_level():
    logger.debug("===========================================================")
    logger.debug("--- namespace: 多段ネームスペース ---")
    node = Node("ns1:ns2:myNode")
    logger.debug(
        "{}: {}".format(
            "node.name",
            node.name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.namespace",
            node.namespace,
        )
    )
    # 期待値: "ns1:ns2"


def local_name_with_namespace():
    logger.debug("===========================================================")
    logger.debug("--- local_name: ネームスペースあり ---")
    node = Node("ns1:myNode")
    logger.debug(
        "{}: {}".format(
            "node.name",
            node.name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.local_name",
            node.local_name,
        )
    )
    # 期待値: "myNode"


def local_name_without_namespace():
    logger.debug("===========================================================")
    logger.debug("--- local_name: ネームスペースなし ---")
    node = Node("myNode")
    logger.debug(
        "{}: {}".format(
            "node.name",
            node.name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.local_name",
            node.local_name,
        )
    )
    # 期待値: "myNode"


def local_name_multi_level():
    logger.debug("===========================================================")
    logger.debug("--- local_name: 多段ネームスペース ---")
    node = Node("ns1:ns2:myNode")
    logger.debug(
        "{}: {}".format(
            "node.name",
            node.name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.local_name",
            node.local_name,
        )
    )
    # 期待値: "myNode"
