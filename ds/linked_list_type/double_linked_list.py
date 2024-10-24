from typing import Optional, Sequence, Any, Tuple
from ds._validators import _validate_index
from ds._validators import _validate_instantiation_from_sequence

__all__ = ["DoubleListNode", "DoubleLinkedList"]


class DoubleListNode:
    """Base node for double linked list"""

    def __init__(
        self,
        value: Any = None,
        next: Optional["DoubleListNode"] = None,
        prev: Optional["DoubleListNode"] = None,
    ) -> None:
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        value = self.value.__str__() if self.value else None
        next = self.next.value.__str__() if self.next else None
        prev = self.prev.value.__str__() if self.prev else None
        return f"{self.__class__.__name__}(value={value}, next={next}, prev={prev})"


class DoubleLinkedList:
    def __new__(cls, _from: Optional[Sequence] = None) -> "DoubleLinkedList":
        _validate_instantiation_from_sequence(
            sequence=_from, data_structure="double linked list"
        )
        return super().__new__(cls)

    def __init__(self, _from: Optional[Sequence] = None) -> None:
        self.head, self.tail, self._len = self._instantiate_object(source=_from)

    @staticmethod
    def _instantiate_object(
        source: Optional[Sequence] = None,
    ) -> Tuple[Optional[DoubleListNode], Optional[DoubleListNode], int]:
        """Private method to instantiate a double linked list."""
        if not source:
            return None, None, 0
        head = DoubleListNode(value=source[0])
        curr = head
        for value in source[1:]:
            new_node = DoubleListNode(value=value, prev=curr)
            curr.next = new_node
            curr = curr.next
        return head, curr, len(source)

    def __len__(self) -> int:
        return self._len

    def __repr__(self) -> str:
        if not self.head:
            return "None"
        return f"{self.__class__.__name__}(head={self.head.value.__repr__()}, tail={self.tail.value.__repr__()}, length={len(self)})"

    def insert(self, index: int, value: Any) -> None:
        """
        Insert a new node at the index-th with the given value.
        Time complexity: O(n) for n equal to the length of the list.
        """
        _validate_index(index=index, lower_bound=0, upper_bound=self._len)
        new_node = DoubleListNode(value=value)
        if index == 0:
            if not self.head:
                self.head = DoubleListNode(value=value)
                self.tail = self.head
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        else:
            current = self.get(index=index - 1)

            new_node.next = current.next
            new_node.prev = current

            current.next.prev = new_node
            current.next = new_node

        self._len += 1
        if index == 0 and self._len == 1:
            self.tail = self.head
        if index == self._len - 1:
            self.tail = new_node

    def prepend(self, value: Any) -> None:
        """
        Add a new node with the given value at the beginning of the double linked list.
        Time complexity: O(1)
        """
        self.insert(index=0, value=value)

    def append(self, value: Any) -> None:
        """
        Add a new node with the given value at the end of the double linked list.
        Time complexity: O(1)
        """
        self.insert(index=self._len, value=value)

    def get(self, index: int) -> DoubleListNode:
        """
        Return the index-th node in the double linked list, if the index is valid.
        Time complexity: O(n), for n equal to the length of the list.
        """
        _validate_index(index=index, lower_bound=0, upper_bound=self._len)
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def remove(self, index: int) -> None:
        """
        Remove the index-th node in the double linked list, if the index is valid.
        Time complexity: O(n), for n equal to the length of the list.
        """
        _validate_index(index=index, lower_bound=0, upper_bound=self._len)
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            current = self.get(index=index - 1)
            current.next = current.next.next
            current.next.prev = current
            if index == self._len:
                self.tail = current
        self._len -= 1

    def is_empty(self) -> bool:
        """
        Return True if the double linked list is empty. False, otherwise.
        Time complexity: O(1)
        """
        return self._len == 0
