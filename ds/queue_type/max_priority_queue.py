import collections
from ds.heap_type.max_binary_heap import MaxBinaryHeap
from ds.queue_type.queue import Queue
from typing import Any, Sequence, Tuple, Dict, Optional, Union, List
from ds._validators import _validate_instantiation_of_sequence_with_priorities

__all__ = ["MaxPriorityQueue"]


class MaxPriorityQueue:
    def __new__(
        cls, _from: Optional[Sequence[Union[Tuple, List]]] = None
    ) -> "MaxPriorityQueue":
        _validate_instantiation_of_sequence_with_priorities(
            sequence=_from, data_structure="MaxPriorityQueue"
        )
        return super().__new__(cls)

    def __init__(self, _from: Optional[Sequence[Union[Tuple, List]]] = None) -> None:
        self._heap, self._queues = self._instantiate_object(source=_from)

    @staticmethod
    def _instantiate_object(
        source: Optional[Sequence[Union[Tuple, List]]],
    ) -> Tuple["MaxBinaryHeap", Dict]:
        heap = MaxBinaryHeap()
        queue = collections.defaultdict(Queue)

        if not source:
            return heap, queue

        for priority, value in source:
            heap.insert(priority)
            queue[priority].enqueue(value)
        return heap, queue

    def __len__(self) -> int:
        return sum([len(queue) for queue in self._queues.values()])

    def __bool__(self) -> bool:
        return self.__len__() != 0

    def __repr__(self) -> str:
        elements = []
        seen_priorities = set()
        heap = self._heap.__deepcopy__()

        while heap:
            priority = heap.pop()
            if priority not in seen_priorities:
                queue = self._queues[priority].__deepcopy__()
                while queue:
                    elements.append(f"({priority}, {queue.dequeue()})")
            seen_priorities.add(priority)

        return f"MaxPriorityQueue({', '.join(elements)})"

    def enqueue(self, priority: Any, value: Any) -> None:
        """
        Add value to the queue with given priority.
        Time Complexity: O(log(n)).
        """
        self._queues[priority].enqueue(value)
        self._heap.insert(priority)

    def dequeue(self) -> Any:
        """
        Remove and return highest-priority value.
        Time Complexity: O(1).
        """
        if self.__len__() == 0:
            raise IndexError("pop from empty max priority queue")
        key = self._heap.pop()
        return self._queues[key].dequeue()

    def peek(self) -> Any:
        """
        Return highest-priority value without removing it.
        Time Complexity: O(1).
        """
        if self.__len__() == 0:
            raise IndexError("peek from empty max priority queue")
        key = self._heap.max()
        return self._queues[key].peek()
