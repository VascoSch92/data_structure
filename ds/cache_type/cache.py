from ds._validators import _validate_capacity
from typing import Optional, Any
from collections import OrderedDict

__all__ = ["Cache"]


class Cache:
    def __new__(cls, capacity: int = 1024) -> "Cache":
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
        """Return the cache in the order the elements were added."""
        return self._cache

    def get(self, key: str) -> Optional[Any]:
        """
        Get an element from the cache. Return None if key not present in the cache.
        Time complexity: O(1).
        """
        if key in self._cache:
            return self._cache[key]

    def put(self, key: str, value: int) -> None:
        """
        Put an element into the cache if capacity is not exceeded.
        Time complexity: O(1).
        """
        if len(self._cache) < self._capacity:
            self._cache[key] = value
