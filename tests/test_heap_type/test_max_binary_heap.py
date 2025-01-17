import pytest
from ds import MaxBinaryHeap


def test_heap_initialization_empty():
    """Test initializing an empty heap."""
    heap = MaxBinaryHeap()
    assert len(heap) == 0
    assert repr(heap) == "MaxBinaryHeap()"


def test_heap_wrong_initialization():
    """Test initializing an empty heap with wrong arguments."""
    sequence = 123
    with pytest.raises(TypeError):
        MaxBinaryHeap(sequence)


def test_heap_initialization_with_list():
    """Test initializing a heap with a list."""
    heap = MaxBinaryHeap([5, 3, 8, 4, 1])
    assert len(heap) == 5
    assert heap.max() == 8
    assert repr(heap) == "MaxBinaryHeap(8, 4, 5, 3, 1)"


def test_insert():
    """Test inserting elements into the heap."""
    heap = MaxBinaryHeap([5, 3, 8])
    heap.insert(1)
    assert len(heap) == 4
    assert heap.max() == 8
    assert repr(heap) == "MaxBinaryHeap(8, 3, 5, 1)"


def test_pop():
    """Test removing the smallest element from the heap."""
    heap = MaxBinaryHeap([5, 3, 8, 4, 1])
    max_element = heap.pop()
    assert max_element == 8
    assert len(heap) == 4
    assert heap.max() == 5
    assert repr(heap) == "MaxBinaryHeap(5, 4, 1, 3)"


def test_pop_empty_heap():
    """Test popping from an empty heap raises an error."""
    heap = MaxBinaryHeap()
    with pytest.raises(IndexError, match="pop from empty heap"):
        heap.pop()


def test_min_empty_heap():
    """Test accessing the minimum element of an empty heap raises an error."""
    heap = MaxBinaryHeap()
    with pytest.raises(IndexError, match="peek from empty heap"):
        heap.max()


def test_heapify():
    """Test that the heap property is maintained."""
    heap = MaxBinaryHeap([10, 20, 15, 30, 40])
    assert heap.max() == 40
    heap.insert(50)
    assert heap.max() == 50
    heap.pop()
    assert heap.max() == 40
    heap.pop()
    assert heap.max() == 30
    heap.pop()
    assert heap.max() == 20
