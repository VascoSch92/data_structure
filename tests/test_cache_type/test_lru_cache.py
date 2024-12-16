from collections import OrderedDict

import pytest

from ds import LRUCache


def test_cache_initialization():
    """Test cache initialization with default and custom capacities."""
    cache = LRUCache()
    assert cache.get_capacity() == 1024
    assert isinstance(cache.get_cache(), OrderedDict)
    assert len(cache.get_cache()) == 0

    cache_custom = LRUCache(10)
    assert cache_custom.get_capacity() == 10
    assert len(cache_custom.get_cache()) == 0


def test_put_and_get():
    """Test adding and retrieving elements from the cache."""
    cache = LRUCache(3)

    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    assert cache.get("b") == 2
    assert cache.get("c") is None


def test_lru_eviction():
    """Test eviction of least recently used elements."""
    cache = LRUCache(2)

    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)  # This should evict "a"
    assert cache.get("a") is None
    assert cache.get("b") == 2
    assert cache.get("c") == 3


def test_lru_update_order():
    """Test order update when an existing key is accessed."""
    cache = LRUCache(3)

    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    cache.get("a")  # Access "a" to move it to the end
    cache.put("d", 4)  # This should evict "b" now
    assert cache.get("b") is None
    assert cache.get("a") == 1
    assert cache.get("d") == 4


def test_put_updates_value():
    """Test that putting an existing key updates its value."""
    cache = LRUCache(2)

    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("a", 3)  # Update "a"
    assert cache.get("a") == 3
    assert cache.get("b") == 2


def test_capacity_validation_value_error():
    """Test that invalid capacities raise an error."""
    with pytest.raises(ValueError):
        _ = LRUCache(0)


def test_capacity_validation_type_error():
    """Test that invalid capacities raise an error."""
    with pytest.raises(TypeError):
        _ = LRUCache("HelloWorld")


def test_cache_order():
    """Test the ordering of elements in the cache."""
    cache = LRUCache(3)

    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    assert list(cache.get_cache().keys()) == ["a", "b", "c"]

    cache.get("a")  # Access "a" to move it to the end
    assert list(cache.get_cache().keys()) == ["b", "c", "a"]

    cache.put("d", 4)  # Add new element, evict "b"
    assert list(cache.get_cache().keys()) == ["c", "a", "d"]
