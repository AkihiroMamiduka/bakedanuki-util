# coding: utf-8
from typing import Protocol

from ..float.store import FloatValueStore
from .value import Float3


class Float3ValueStore(Protocol):
    """3つのscalar Storeと、正本への一括読み書きの境界。"""

    @property
    def components(
        self,
    ) -> tuple[FloatValueStore, FloatValueStore, FloatValueStore]:
        """X・Y・Zの正本にアクセスするStoreを返す。"""
        raise NotImplementedError

    @property
    def is_available(self) -> bool:
        """3成分の正本を読み取れるか返す。"""
        raise NotImplementedError

    @property
    def is_writable(self) -> bool:
        """3成分すべてを書き込めるか返す。"""
        raise NotImplementedError

    def read(self) -> Float3:
        """丸めていない公開単位の3成分を返す。"""
        raise NotImplementedError

    def write(self, value: Float3) -> Float3:
        """3成分を一括設定し、確定した実値を返す。"""
        raise NotImplementedError
