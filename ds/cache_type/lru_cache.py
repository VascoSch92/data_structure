from collections import OrderedDict
from ds._validators import _validate_capacity, _validate_hashable_key
from typing import Any, Optional

__all__ = ["LRUCache"]


class LRUCache:
    def __new__(cls, capacity: int = 1024) -> "LRUCache":
        _validate_capacity(capacity=capacity)
        return super().__new__(cls)

    def __init__(self, capacity: int = 1024) -> None:
        """Initialize the Cache with a fixed capacity."""
        self._capacity = capacity
        self._cache = OrderedDict()  # key - value

    def get_capacity(self) -> int:
        """Return the capacity of the cache."""
        return self._capacity

    def get_cache(self) -> OrderedDict:
        """Return the cache in the order of usage."""
        return self._cache

    def get(self, key: Any) -> Optional[Any]:
        """
        Get an element from the cache. Return None if key not present in the cache.
        Time complexity: O(1).
        """
        _validate_hashable_key(key=key)

        if key in self._cache:
            self._cache.move_to_end(key=key)
            return self._cache[key]

    def put(self, key: Any, value: Any) -> None:
        """
        Put an element into the cache, eventually evict least recent used element.
        Time complexity: O(1).
        """
        _validate_hashable_key(key=key)

        if key in self._cache:
            self._cache.move_to_end(key=key)
            self._cache[key] = value
            return
        self._cache[key] = value

        if len(self._cache) > self._capacity:
            self._cache.popitem(last=False)
