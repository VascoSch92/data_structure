import pytest
from collections import OrderedDict
from ds import Cache


def test_cache_initialization_valid_capacity():
    cache = Cache(capacity=10)
    assert cache.get_capacity() == 10
    assert cache.get_cache() == {}


def test_cache_initialization_invalid_capacity_type():
    with pytest.raises(TypeError, match="Wrong type provided for capacity."):
        _ = Cache(capacity="HelloWorld")


def test_cache_initialization_invalid_capacity_int():
    with pytest.raises(ValueError, match="Capacity must be greater than 0."):
        _ = Cache(capacity=-1)


def test_put_and_get():
    cache = Cache(capacity=3)
    cache.put("key1", 100)
    assert cache.get("key1") == 100

    cache.put("key2", 200)
    assert cache.get("key2") == 200

    assert cache.get_capacity() == 3
    assert cache.get_cache() == {"key1": 100, "key2": 200}


def test_put_over_capacity():
    cache = Cache(capacity=2)
    cache.put("key1", 100)
    cache.put("key2", 200)
    cache.put("key3", 300)  # This should not be added since capacity is 2

    assert cache.get("key1") == 100  # Existing keys remain
    assert cache.get("key2") == 200
    assert cache.get("key3") is None  # New key not added due to capacity limit

    assert cache.get_capacity() == 2
    assert cache.get_cache() == OrderedDict({"key1": 100, "key2": 200})


def test_get_nonexistent_key():
    cache = Cache(capacity=2)
    assert cache.get("nonexistent") is None
