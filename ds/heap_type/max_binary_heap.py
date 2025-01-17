from typing import Optional, Sequence, List, Any

from ds.heap_type._heap import _Heap

__all__ = ["MaxBinaryHeap"]


class MaxBinaryHeap(_Heap):
    def __init__(self, _from: Optional[Sequence] = None) -> None:
        self._heap = self._instantiate_object(source=_from)

    def __len__(self) -> int:
        """Return the number of elements in the heap."""
        return len(self._heap)

    def __bool__(self) -> bool:
        return self.__len__() > 0

    def __deepcopy__(self) -> "MaxBinaryHeap":
        return MaxBinaryHeap(self._heap.copy())

    def __repr__(self) -> str:
        """String representation of the heap."""
        return f"MaxBinaryHeap({', '.join([element.__repr__() for element in self._heap])})"

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

    def insert(self, value: Any) -> None:
        """
        Insert the element value into the max heap.
        Time complexity: O(log(n)).
        """
        self._heap.append(value)
        self._heapify_up(source=self._heap, index=len(self._heap) - 1)

    def pop(self) -> Any:
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

    def max(self) -> Any:
        """
        Return the largest element without removing it.
        Time complexity: O(1).
        """
        if not self._heap:
            raise IndexError("peek from empty heap")
        return self._heap[0]
