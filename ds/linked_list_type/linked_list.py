from typing import Optional, Sequence, Any, Tuple
from ds._validators import _validate_index, _validate_instantiation_from_sequence
from dataclasses import dataclass

__all__ = ["ListNode", "LinkedList"]


@dataclass
class ListNode:
    """Base node for linked list"""

    value: Any = None
    next: Optional["ListNode"] = None

    def __repr__(self) -> str:
        value = self.value.__str__() if self.value else None
        next = self.next.value.__str__() if self.next else None
        return f"{self.__class__.__name__}(value={value}, next={next})"


class LinkedList:
    def __new__(cls, _from: Optional[Sequence] = None) -> "LinkedList":
        _validate_instantiation_from_sequence(
            sequence=_from,
            data_structure="linked list",
        )
        return super().__new__(cls)

    def __init__(self, _from: Optional[Sequence] = None) -> None:
        self.head, self.tail, self._len = self._instantiate_object(source=_from)

    @staticmethod
    def _instantiate_object(
        source: Optional[Sequence] = None,
    ) -> Tuple[Optional[ListNode], Optional[ListNode], int]:
        """Private method to instantiate a linked list."""
        if not source:
            return None, None, 0
        head = ListNode(value=source[0])
        curr = head
        for value in source[1:]:
            new_node = ListNode(value=value)
            curr.next = new_node
            curr = curr.next
        return head, curr, len(source)

    def __len__(self) -> int:
        return self._len

    def __repr__(self) -> str:
        if not self.head:
            return "None"
        return f"{self.__class__.__name__}(head={self.head.__repr__()}, tail={self.tail.__repr__()}, length={len(self)})"

    def insert(self, index: int, value: Any) -> None:
        """
        Insert a new node at the index-th with the given value.
        Time complexity: O(n) for n equal to the length of the list.
        """
        _validate_index(index=index, lower_bound=0, upper_bound=self._len)
        new_node = ListNode(value=value)
        if index == 0:
            if not self.head:
                self.head = ListNode(value=value)
                self.tail = self.head
            else:
                new_node.next = self.head
                self.head = new_node
        else:
            current = self.get(index=index - 1)
            new_node.next = current.next
            current.next = new_node

        self._len += 1
        if index == 0 and self._len == 1:
            self.tail = self.head
        if index == self._len - 1:
            self.tail = new_node

    def prepend(self, value: Any) -> None:
        """
        Add a new node with the given value at the begin of the linked list.
        Time complexity: O(1)
        """
        self.insert(index=0, value=value)

    def append(self, value: Any) -> None:
        """
        Add a new node with the given value at the end of the linked list.
        Time complexity: O(1)
        """
        self.insert(index=self._len, value=value)

    def get(self, index: int) -> ListNode:
        """
        Return the index-th node in the linked list, if the index is valid.
        Time complexity: O(n), for n equal to the length of the list.
        """
        _validate_index(index=index, lower_bound=0, upper_bound=self._len)
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def remove(self, index: int) -> None:
        """
        Remove the index-th node in the linked list, if the index is valid.
        Time complexity: O(n), for n equal to the length of the list.
        """
        _validate_index(index=index, lower_bound=0, upper_bound=self._len)
        if index == 0:
            self.head = self.head.next
        else:
            current = self.get(index=index - 1)
            current.next = current.next.next
            if index == self._len:
                self.tail = current
        self._len -= 1

    def is_empty(self) -> bool:
        """
        Return True if the linked list is empty. False, otherwise.
        Time complexity: O(1)
        """
        return self._len == 0
