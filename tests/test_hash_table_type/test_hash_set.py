import pytest

from ds import HashSet


@pytest.fixture
def hash_set():
    return HashSet(capacity=10)


def test_init_empty_set(hash_set):
    """Test that an empty HashSet is initialized correctly."""
    assert len(hash_set) == 0
    assert str(hash_set) == "{}"


def test_init_with_sequence():
    """Test that the HashSet can be initialized from a sequence."""
    hash_set = HashSet(capacity=10, _from=[1, 2, 3])
    assert len(hash_set) == 3
    assert hash_set.contains(1) is True
    assert hash_set.contains(2) is True
    assert hash_set.contains(3) is True


def test_add_elements(hash_set):
    """Test adding elements to the HashSet."""
    hash_set.add(1)
    hash_set.add(2)
    hash_set.add(3)
    assert len(hash_set) == 3
    assert hash_set.contains(1) is True
    assert hash_set.contains(2) is True
    assert hash_set.contains(3) is True


def test_add_duplicate(hash_set):
    """Test adding a duplicate element."""
    hash_set.add(1)
    hash_set.add(1)  # Adding a duplicate element
    assert len(hash_set) == 1  # Should not increase in size
    assert hash_set.contains(1) is True


def test_remove_existing_element(hash_set):
    """Test removing an existing element."""
    hash_set.add(1)
    hash_set.remove(1)
    assert len(hash_set) == 0
    assert hash_set.contains(1) is False


def test_remove_non_existing_element(hash_set):
    """Test removing a non-existing element."""
    hash_set.add(1)
    hash_set.remove(2)  # Element 2 doesn't exist
    assert len(hash_set) == 1  # Should not change the size
    assert hash_set.contains(1) is True  # 1 should still be present


def test_contains(hash_set):
    """Test the contains method."""
    hash_set.add(1)
    hash_set.add(2)
    assert hash_set.contains(1) is True
    assert hash_set.contains(2) is True
    assert hash_set.contains(3) is False


def test_clear(hash_set):
    """Test the clear method."""
    hash_set.add(1)
    hash_set.add(2)
    hash_set.clear()
    assert len(hash_set) == 0
    assert hash_set.contains(1) is False
    assert hash_set.contains(2) is False


def test_invalid_capacity_type():
    """Test that a TypeError is raised if the capacity is not an integer."""
    with pytest.raises(TypeError):
        HashSet(capacity="100")  # Invalid capacity type


def test_invalid_sequence_type():
    """Test that _validate_instantiation_from_sequence is called correctly."""
    # Here, you could mock _validate_instantiation_from_sequence if necessary
    with pytest.raises(TypeError):
        HashSet(capacity=10, _from=123456789)  # Invalid sequence type


def test_str_representation():
    """Test the string representation of the HashSet."""
    hash_set = HashSet(capacity=10, _from=[1, 2, 3])
    assert str(hash_set) == "{1, 2, 3}"
