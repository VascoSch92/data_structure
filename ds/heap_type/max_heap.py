from typing import Optional, Sequence, List

from ds._validators import _validate_instantiation_from_sequence

__all__ = ["MaxHeap"]


class MaxHeap:
    def __new__(cls, _from: Optional[Sequence] = None) -> "MaxHeap":
        _validate_instantiation_from_sequence(sequence=_from, data_structure="max heap")
        return super().__new__(cls)

    def __init__(self, _from: Optional[Sequence] = None) -> None:
        self._heap = self._instantiate_object(source=_from)

    def _instantiate_object(self, source: Optional[Sequence] = None) -> List[int]:
        if not source:
            return []

        n = len(source)
        for index in range(n // 2 - 1, -1, -1):
            self._heapify_down(source=source, index=index)
        return list(source)

    def _heapify_down(self, source: Sequence[int], index: int) -> None:
        """Private method to restore the max-heap property by sifting an element down."""
        n = len(source)
        largest, left, right = index, 2 * index + 1, 2 * index + 2

        # Compare with left child
        if left < n and source[left] > source[largest]:
            largest = left

        # Compare with right child
        if right < n and source[right] > source[largest]:
            largest = right

        # If the largest isn't the parent node, swap and recurse
        if largest != index:
            source[index], source[largest] = source[largest], source[index]
            self._heapify_down(source=source, index=largest)

    def _heapify_up(self, source: Sequence[int], index: int) -> None:
        """Private method to restore the max-heap property by sifting an element up."""
        parent = (index - 1) // 2
        while index > 0 and source[index] > source[parent]:
            source[index], source[parent] = source[parent], source[index]
            index = parent
            parent = (index - 1) // 2

    def insert(self, value):
        """
        Insert the element value into the max heap.
        Time complexity: O(log(n)).
        """
        self._heap.append(value)
        self._heapify_up(source=self._heap, index=len(self._heap) - 1)

    def pop(self):
        """
        Remove and return the largest element from the heap.
        Time complexity: O(1).
        """
        if not self._heap:
            raise IndexError("pop from empty heap")

        if len(self._heap) == 1:
            return self._heap.pop()

        # Swap the root with the last element and remove it
        root = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._heapify_down(source=self._heap, index=0)
        return root

    def max(self):
        """
        Return the largest element without removing it.
        Time complexity: O(1).
        """
        if not self._heap:
            raise IndexError("peek from empty heap")
        return self._heap[0]

    def __len__(self):
        """Return the number of elements in the heap."""
        return len(self._heap)

    def __repr__(self):
        """String representation of the heap."""
        return f"MaxHeap({', '.join([element.__repr__() for element in self._heap])})"
