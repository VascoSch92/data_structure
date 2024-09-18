from typing import Optional, Sequence, Any
from ds import LinkedList

__all__ = ["Queue"]


class Queue:
    def __new__(cls, _from: Optional[Sequence] = None) -> "Queue":
        if not isinstance(_from, Sequence) and _from:
            raise TypeError(
                f"Creation of a queue from type {type(_from)} not supported."
            )
        return super().__new__(cls)

    def __init__(self, _from: Optional[Sequence] = None) -> None:
        self._queue = LinkedList(_from=_from)

    def __len__(self) -> int:
        return self._queue.__len__()

    def __bool__(self) -> bool:
        return self._queue.__len__() > 0

    def __repr__(self) -> str:
        curr = self._queue.head
        elements = []
        while curr:
            elements.append(curr.value.__repr__())
            curr = curr.next
        return f"Queue({', '.join(elements)})"

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
