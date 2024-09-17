from ds import ListNode
from typing import Sequence, Optional, Any, Tuple


__all__ = ["Stack"]


class Stack:
    def __new__(cls, _from: Optional[Sequence] = None) -> "Stack":
        if not isinstance(_from, Sequence) and _from:
            raise TypeError(
                f"Creation of a stack from type {type(_from)} not supported."
            )
        return super().__new__(cls)

    def __init__(self, _from: Optional[Sequence] = None) -> None:
        self._stack, self._len = self._instantiate_object(source=_from)

    def __repr__(self) -> str:
        curr = self._stack
        elements = []
        while curr:
            elements.append(curr.value.__repr__())
            curr = curr.next
        return f"Stack({', '.join(elements[::-1])})"

    @staticmethod
    def _instantiate_object(
        source: Optional[Sequence] = None,
    ) -> Tuple[Optional[ListNode], int]:
        """Private method to instantiate a stack."""
        if not source:
            return None, 0
        source = source[::-1]
        stack = ListNode(value=source[0])
        curr = stack
        for value in source[1:]:
            next_element = ListNode(value=value)
            curr.next = next_element
            curr = curr.next
        return stack, len(source)

    def __len__(self) -> int:
        return self._len

    def __bool__(self) -> bool:
        return self._len > 0

    def pop(self) -> Any:
        """
        Delete and return the last element added to the stack.
        Time complexity: O(1).
        """
        if self._len == 0:
            raise ValueError("Empty stack!")
        element = self._stack.value
        self._stack = self._stack.next if self._stack else None
        self._len -= 1
        return element

    def push(self, value: Any) -> None:
        """
        Push the element `value` at the top of the stack.
        Time complexity: O(1).
        """
        new_element = ListNode(value=value, next=self._stack)
        self._stack = new_element
        self._len += 1

    def peek(self) -> Any:
        """
        Return the last element added to the stack.
        Time complexity: O(1).
        """
        if self._len == 0:
            raise ValueError("Empty stack!")
        return self._stack.value

    def is_empty(self) -> bool:
        """
        Return True if the stack is empty. False, otherwise.
        Time complexity: O(1)
        """
        return self._len == 0
