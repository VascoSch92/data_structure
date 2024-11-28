import pytest
from ds import MaxHeap


def test_heap_initialization():
    # Test initializing from an empty list
    heap = MaxHeap()
    assert len(heap) == 0
    assert repr(heap) == "MaxHeap()"

    # Test initializing from a list
    elements = [3, 9, 2, 1, 4, 5]
    heap = MaxHeap(elements)
    assert len(heap) == len(elements)
    assert heap.max() == 9  # Largest element should be at the root

    # Test that the heap property is maintained
    assert heap.pop() == 9
    assert heap.pop() == 5
    assert heap.pop() == 4


def test_push():
    # Test pushing elements into an empty heap
    heap = MaxHeap()
    heap.insert(5)
    assert len(heap) == 1
    assert heap.max() == 5

    heap.insert(10)
    assert len(heap) == 2
    assert heap.max() == 10  # Max-heap property: root is the largest

    heap.insert(3)
    assert len(heap) == 3
    assert heap.max() == 10

    # Test maintaining the heap property after multiple pushes
    heap.insert(20)
    assert len(heap) == 4
    assert heap.max() == 20


def test_pop():
    # Test popping from a heap with multiple elements
    elements = [3, 1, 4, 2, 9]
    heap = MaxHeap(elements)
    assert heap.pop() == 9
    assert heap.pop() == 4
    assert heap.pop() == 3
    assert heap.pop() == 2
    assert heap.pop() == 1

    # Test popping from an empty heap
    with pytest.raises(IndexError):
        heap.pop()


def test_peek():
    # Test peeking at the root of the heap
    elements = [3, 7, 2, 1, 4]
    heap = MaxHeap(elements)
    assert heap.max() == 7  # Largest element

    # Peek should not modify the heap
    assert len(heap) == len(elements)

    # Test peeking on an empty heap
    empty_heap = MaxHeap()
    with pytest.raises(IndexError):
        empty_heap.max()


def test_edge_cases():
    # Test initializing with a single element
    heap = MaxHeap([10])
    assert heap.max() == 10
    assert len(heap) == 1
    assert heap.pop() == 10
    assert len(heap) == 0

    # Test pushing into a single-element heap
    heap.insert(20)
    assert heap.max() == 20
    heap.insert(5)
    assert heap.max() == 20

    # Test removing all elements
    heap.pop()
    heap.pop()
    assert len(heap) == 0


def test_heapify_on_large_data():
    # Test heapifying a large dataset
    elements = [i for i in range(1000, 0, -1)]  # Reverse order
    heap = MaxHeap(elements)
    assert heap.max() == 1000  # Largest element
    assert len(heap) == len(elements)

    # Ensure all elements can be popped in decreasing order
    prev = heap.pop()
    while len(heap) > 0:
        current = heap.pop()
        assert prev >= current
        prev = current
