from typing import Optional, Sequence, Any
from ds import LinkedList
from ds._validators import _validate_instantiation_from_sequence

__all__ = ["Queue"]


class Queue:
    def __new__(cls, _from: Optional[Sequence] = None) -> "Queue":
        _validate_instantiation_from_sequence(sequence=_from, data_structure="queue")
        return super().__new__(cls)

    def __init__(self, _from: Optional[Sequence] = None) -> None:
        self._queue = LinkedList(_from=_from)

    def __len__(self) -> int:
        return self._queue.__len__()

    def __bool__(self) -> bool:
        return self._queue.__len__() > 0

    def __deepcopy__(self) -> "Queue":
        elements = []

        curr = self._queue.head
        while curr:
            elements.append(curr.value)
            curr = curr.next

        return Queue(elements)

    def __repr__(self) -> str:
        curr = self._queue.head
        elements = []
        while curr:
            elements.append(curr.value.__repr__())
            curr = curr.next
        return f"{self.__class__.__name__}({', '.join(elements)})"

    def enqueue(self, value: Any) -> None:
        """
        Push the element `value` at the end of the queue.
        Time complexity: O(1).
        """
        self._queue.append(value=value)

    def dequeue(self) -> Any:
        """
        Delete and return the first element of the queue.
        Time complexity: O(1).
        """
        element = self._queue.get(index=0)
        self._queue.remove(index=0)
        return element.value

    def peek(self) -> Any:
        """
        Return the first element of the queue.
        Time complexity: O(1).
        """
        return self._queue.get(index=0).value

    def is_empty(self) -> bool:
        """
        Return True if the queue is empty. Otherwise, False.
        Time complexity: O(1)
        """
        return self.__len__() == 0
