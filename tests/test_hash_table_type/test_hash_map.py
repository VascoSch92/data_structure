import pytest
from ds import LinkedList, HashMap


@pytest.fixture
def empty_hashmap():
    """Fixture to create an empty HashMap with default capacity."""
    return HashMap()


@pytest.fixture
def populated_hashmap():
    """Fixture to create a populated HashMap."""
    hashmap = HashMap()
    hashmap.add(("key1", "value1"))
    hashmap.add(("key2", "value2"))
    hashmap.add(("key3", "value3"))
    return hashmap


def test_initialization():
    """Test that the HashMap initializes correctly."""
    hashmap = HashMap(capacity=50)
    assert len(hashmap) == 0
    assert hashmap._capacity == 50
    assert all(
        isinstance(hashmap._buckets[j], LinkedList)
        for j in range(len(hashmap._buckets))
    )
    assert len(hashmap._buckets) == 50


def test_add_and_get(empty_hashmap):
    """Test adding items and retrieving them."""
    empty_hashmap.add(("key1", "value1"))
    assert empty_hashmap.get("key1") == "value1"
    assert len(empty_hashmap) == 1

    empty_hashmap.add(("key2", "value2"))
    assert empty_hashmap.get("key2") == "value2"
    assert len(empty_hashmap) == 2

    # Test updating existing key
    empty_hashmap.add(("key1", "new_value1"))
    assert empty_hashmap.get("key1") == "new_value1"
    assert len(empty_hashmap) == 2  # Length should not increase


def test_get_default(empty_hashmap):
    """Test retrieving a non-existing key with a default fallback."""
    assert empty_hashmap.get("missing_key", "default_value") == "default_value"


def test_remove(populated_hashmap):
    """Test removing items from the HashMap."""
    populated_hashmap.remove("key2")
    assert populated_hashmap.get("key2") is None
    assert len(populated_hashmap) == 2

    populated_hashmap.remove("key1")
    assert populated_hashmap.get("key1") is None
    assert len(populated_hashmap) == 1


def test_keys(populated_hashmap):
    """Test retrieving all keys."""
    keys = list(populated_hashmap.keys())
    assert sorted(keys) == ["key1", "key2", "key3"]


def test_values(populated_hashmap):
    """Test retrieving all values."""
    values = list(populated_hashmap.values())
    assert sorted(values) == ["value1", "value2", "value3"]


def test_items(populated_hashmap):
    """Test retrieving all items."""
    items = list(populated_hashmap.items())
    assert sorted(items) == [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]


def test_clear(populated_hashmap):
    """Test clearing the HashMap."""
    populated_hashmap.clear()
    assert len(populated_hashmap) == 0
    assert list(populated_hashmap.keys()) == []
    assert list(populated_hashmap.values()) == []
    assert list(populated_hashmap.items()) == []
