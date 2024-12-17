import pytest

from ds import LFUCache


def test_initialization():
    """Test LFUCache initialization."""
    cache = LFUCache(capacity=3)
    assert cache.get_capacity() == 3
    assert cache.get_cache() == {}


def test_invalid_capacity():
    """Test LFUCache raises errors for invalid capacities."""
    with pytest.raises(ValueError):
        LFUCache(capacity=0)  # Invalid: capacity should be > 0
    with pytest.raises(ValueError):
        LFUCache(capacity=-5)  # Invalid: negative capacity


def test_basic_put_and_get():
    """Test basic put and get operations."""
    cache = LFUCache(capacity=2)
    cache.put(1, 1)  # Add key 1 with value 1
    cache.put(2, 2)  # Add key 2 with value 2

    assert cache.get(1) == 1  # Key 1 should return 1
    assert cache.get(2) == 2  # Key 2 should return 2
    assert cache.get(3) is None  # Key 3 does not exist


def test_eviction_least_frequently_used():
    """Test LFU eviction policy."""
    cache = LFUCache(capacity=2)
    cache.put(1, 1)
    cache.put(2, 2)

    assert cache.get(1) == 1  # Access key 1, frequency of key 1 becomes 2
    cache.put(3, 3)  # Evicts key 2 (least frequently used)

    assert cache.get(2) is None  # Key 2 should have been evicted
    assert cache.get(1) == 1  # Key 1 should still be present
    assert cache.get(3) == 3  # Key 3 should be present


def test_lru_with_same_frequency():
    """Test LRU eviction when multiple keys have the same frequency."""
    cache = LFUCache(capacity=2)
    cache.put(1, 1)
    cache.put(2, 2)

    cache.get(1)  # Key 1: frequency = 2
    cache.put(3, 3)  # Evicts key 2 (used less recently than key 1)

    assert cache.get(2) is None  # Key 2 should have been evicted
    assert cache.get(1) == 1  # Key 1 should still be present
    assert cache.get(3) == 3  # Key 3 should be present


def test_update_existing_key():
    """Test that updating an existing key works correctly."""
    cache = LFUCache(capacity=2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)  # Update key 1's value

    assert cache.get(1) == 10  # Value should be updated to 10
    assert cache.get(2) == 2


def test_eviction_edge_case():
    """Test eviction when adding a new key at full capacity."""
    cache = LFUCache(capacity=1)
    cache.put(1, 1)
    assert cache.get(1) == 1

    cache.put(2, 2)  # Evicts key 1, as the cache can only hold 1 key
    assert cache.get(1) is None  # Key 1 should have been evicted
    assert cache.get(2) == 2  # Key 2 should be present


def test_non_hashable_key():
    """Test that non-hashable keys raise an error."""
    cache = LFUCache(capacity=2)
    with pytest.raises(TypeError):
        cache.put([], 1)  # Lists are not hashable keys
    with pytest.raises(TypeError):
        cache.get({})  # Dictionaries are not hashable keys


def test_no_eviction_with_capacity_zero():
    """Test that no keys can be added when capacity is zero."""
    with pytest.raises(ValueError):
        LFUCache(capacity=0)

    cache = LFUCache(capacity=1)
    cache.put(1, 1)
    cache.put(2, 2)  # Evicts key 1
    assert cache.get(1) is None
    assert cache.get(2) == 2
