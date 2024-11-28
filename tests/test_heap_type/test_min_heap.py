import pytest
from ds import MinHeap


def test_heap_initialization_empty():
    """Test initializing an empty heap."""
    heap = MinHeap()
    assert len(heap) == 0
    assert repr(heap) == "MinHeap()"


def test_heap_initialization_with_list():
    """Test initializing a heap with a list."""
    heap = MinHeap([5, 3, 8, 4, 1])
    assert len(heap) == 5
    assert heap.min() == 1
    assert repr(heap) == "MinHeap(1, 3, 8, 4, 5)"


def test_insert():
    """Test inserting elements into the heap."""
    heap = MinHeap([5, 3, 8])
    heap.insert(1)
    assert len(heap) == 4
    assert heap.min() == 1
    assert repr(heap) == "MinHeap(1, 3, 8, 5)"


def test_pop():
    """Test removing the smallest element from the heap."""
    heap = MinHeap([5, 3, 8, 4, 1])
    min_element = heap.pop()
    assert min_element == 1
    assert len(heap) == 4
    assert heap.min() == 3
    assert repr(heap) == "MinHeap(3, 4, 8, 5)"


def test_pop_empty_heap():
    """Test popping from an empty heap raises an error."""
    heap = MinHeap()
    with pytest.raises(IndexError, match="pop from empty heap"):
        heap.pop()


def test_min_empty_heap():
    """Test accessing the minimum element of an empty heap raises an error."""
    heap = MinHeap()
    with pytest.raises(IndexError, match="peek from empty heap"):
        heap.min()


def test_heapify():
    """Test that the heap property is maintained."""
    heap = MinHeap([10, 20, 15, 30, 40])
    assert heap.min() == 10
    heap.insert(5)
    assert heap.min() == 5
    heap.pop()
    assert heap.min() == 10
    heap.pop()
    assert heap.min() == 15
    heap.pop()
    assert heap.min() == 20
