# coding: utf-8
"""
Node クラスの名前系プロパティ（namespace / local_name）のテスト・デモ
"""

# self
from ...... import logger as u_logger
from ..... import str as test_str
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
    test_str.title("namespace_with_namespace")
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
    test_str.title("namespace_without_namespace")
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
    test_str.title("namespace_multi_level")
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
    test_str.title("local_name_with_namespace")
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
    test_str.title("local_name_without_namespace")
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
    test_str.title("local_name_multi_level")
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
