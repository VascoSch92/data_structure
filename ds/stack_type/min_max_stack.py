from typing import Sequence, Optional, Any, Tuple
from ds import Stack

__all__ = ["MinMaxStack"]


class MinMaxStack:
    def __new__(cls, _from: Optional[Sequence] = None) -> "MinMaxStack":
        if not isinstance(_from, Sequence) and _from:
            raise TypeError(
                f"Creation of a min/max-stack from type {type(_from)} not supported."
            )
        return super().__new__(cls)

    def __init__(self, _from: Optional[Sequence] = None) -> None:
        self._stack, self._range = (
            self._instantiate_from_sequence(_from) if _from else (Stack(), Stack())
        )
        self._len = len(self._stack) if _from else 0

    @staticmethod
    def _instantiate_from_sequence(source: Sequence) -> Tuple[Stack, Stack]:
        """Private method to instantiate a MinMaxStack from a sequence."""
        source = source[::-1]
        stack, range = Stack(), Stack()
        for idx, value in enumerate(source):
            stack.push(value)
            range.push((min(source[: idx + 1]), max(source[: idx + 1])))

        return stack, range

    def __len__(self) -> int:
        return self._len

    def __bool__(self) -> bool:
        return self._len > 0

    def __repr__(self) -> str:
        return self._stack.__repr__()

    def pop(self) -> Any:
        """
        Delete and return the last element added to the stack.
        Time complexity: O(1).
        """
        if self._len == 0:
            raise ValueError("Empty stack!")
        self._range.pop()
        return self._stack.pop()

    def push(self, value: Any) -> None:
        """
        Push the element `value` at the top of the stack.
        Time complexity: O(1).
        """
        self._stack.push(value=value)

        new_min, new_max = value, value

        if self._len > 0:
            old_min, old_max = self._range.peek()
            new_max = max(new_max, old_max)
            new_min = min(new_min, old_min)

        self._range.push((new_min, new_max))
        self._len += 1

    def peek(self) -> Any:
        """
        Return the last element added to the stack.
        Time complexity: O(1).
        """
        return self._stack.peek()

    def min(self) -> Any:
        """
        Return the min element presents in the stack.
        Time complexity: O(1).
        """
        return self._range.peek()[0]

    def max(self) -> Any:
        """
        Return the max element presents in the stack.
        Time complexity: O(1)
        """
        return self._range.peek()[1]
