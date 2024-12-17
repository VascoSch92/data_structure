from ds._validators import _validate_capacity, _validate_hashable_key
from collections import OrderedDict, defaultdict
from typing import Dict, Optional, Any

__all__ = ["LFUCache"]


class LFUCache:
    def __new__(cls, capacity: int = 1024) -> "LFUCache":
        _validate_capacity(capacity=capacity)
        return super().__new__(cls)

    def __init__(self, capacity: int = 1024) -> None:
        """Initialize the Cache with a fixed capacity."""
        self._capacity = capacity
        self._min_frequency = 0  # track minimum frequency
        self._cache = {}  # maps key to its value
        self._counter = {}  # maps key to its frequency
        self._lfu = defaultdict(OrderedDict)  # maps frequency to respective keys

    def get_capacity(self) -> int:
        """Return the capacity of the cache."""
        return self._capacity

    def get_cache(self) -> Dict:
        """Return the cache in the order of usage."""
        return self._cache

    def get(self, key: Any) -> Optional[Any]:
        """
        Get an element from the cache. Return None if key not present in the cache.
        Time complexity: O(1).
        """
        _validate_hashable_key(key=key)

        if key in self._cache:
            self._update_freq(key=key)
            return self._cache[key]

    def _update_freq(self, key: Any) -> None:
        """Private method to update frequency of a key"""
        curr_value, curr_freq = self._cache[key], self._counter[key]

        # Remove the key from its current frequency list
        del self._lfu[curr_freq][key]
        if not self._lfu[curr_freq]:
            del self._lfu[curr_freq]
            if curr_freq == self._min_frequency:
                self._min_frequency += 1

        # Update frequency
        self._counter[key] += 1
        self._lfu[self._counter[key]][key] = curr_value

    def put(self, key: int, value: int) -> None:
        """
        Put an element into the cache, eventually evict least frequently used element.
        Time complexity: O(1).
        """
        _validate_hashable_key(key=key)

        if key in self._cache:  # If key already exists, update value and frequency
            self._cache[key] = value
            self._update_freq(key)
            return

        self._evict_least_frequently_used()

        self._add_new_key(key=key, value=value)

    def _evict_least_frequently_used(self) -> None:
        """Private method to evict the least frequently used key."""
        if len(self._cache) >= self._capacity:
            lfu_key, _ = self._lfu[self._min_frequency].popitem(last=False)

            del self._cache[lfu_key]
            del self._counter[lfu_key]

            if not self._lfu[self._min_frequency]:
                del self._lfu[self._min_frequency]

    def _add_new_key(self, key: Any, value: Any) -> None:
        """Private method to add a new key."""
        self._cache[key] = value
        self._counter[key] = 1
        self._lfu[1][key] = value
        self._min_frequency = 1
