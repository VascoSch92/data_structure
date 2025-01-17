import collections
from ds.heap_type.min_binary_heap import MinBinaryHeap
from ds.queue_type.queue import Queue
from typing import Any, Sequence, Tuple, Dict, Optional, Union, List
from ds._validators import _validate_instantiation_of_sequence_with_priorities

__all__ = ["MinPriorityQueue"]


class MinPriorityQueue:
    def __new__(
        cls, _from: Optional[Sequence[Union[Tuple, List]]] = None
    ) -> "MinPriorityQueue":
        _validate_instantiation_of_sequence_with_priorities(
            sequence=_from, data_structure="MinPriorityQueue"
        )
        return super().__new__(cls)

    def __init__(self, _from: Optional[Sequence[Union[Tuple, List]]] = None) -> None:
        self._heap, self._queues = self._instantiate_object(source=_from)

    @staticmethod
    def _instantiate_object(
        source: Optional[Sequence[Union[Tuple, List]]],
    ) -> Tuple["MinBinaryHeap", Dict]:
        heap = MinBinaryHeap()
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

        return f"MinPriorityQueue({', '.join(elements)})"

    def enqueue(self, priority, value) -> None:
        """
        Add value to the queue with given priority.
        Time Complexity: O(log(n)).
        """
        self._queues[priority].enqueue(value)
        self._heap.insert(priority)

    def dequeue(self) -> Any:
        """
        Remove and return lowest-priority value.
        Time Complexity: O(1).
        """
        if self.__len__() == 0:
            raise IndexError("pop from empty min priority queue")
        key = self._heap.pop()
        return self._queues[key].dequeue()

    def peek(self) -> Any:
        """
        Return lowest-priority value without removing it.
        Time Complexity: O(1).
        """
        if self.__len__() == 0:
            raise IndexError("peek from empty min priority queue")
        key = self._heap.min()
        return self._queues[key].peek()
