# coding: utf-8

# self
from .. import logger as u_logger


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def title(title: str):
    text = "=" * 8
    text += f" {title} "
    text = text.ljust(50, "=")
    logger.debug(text)


def separator():
    logger.debug("-" * 50)


def separator_sub():
    logger.debug("-" * 2)
