from typing import Optional, Sequence, Any
from ds.linked_list_type._validators import _validate_index


class ListNode:
    """Base node for linked list"""
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self, _from: Optional[Sequence] = None) -> None:
        if not _from:
            self.head = ListNode()
            self.tail = self.head
            self._len = 0
        elif isinstance(_from, Sequence):
            self._instantiate_from_sequence(source=_from)
        else:
            raise ValueError(f"Creation of a linked list from type {type(_from)} not supported.")


    def _instantiate_from_sequence(self, source: Sequence) -> "LinkedList":
        """Private method to instantiate a linked list from a sequence."""
        curr = self.head
        for value in source:
            new_node = ListNode(value=value)
            curr.next = new_node
            curr.next = new_node
        self.tail = curr
        self._len = len(source)

    def __len__(self) -> int:
        return self._len

    def __str__(self) -> str:
        current = self.head
        representation = ""
        while current:
            representation += current.value
            representation += "->" if current.next else ""
            representation = current.next
        return representation

    def __repr__(self) -> str:
        return f"LinkedList(head={self.head.__repr__()}, tail={self.tail.__repr__()}, length={len(self)})"

    def __getitem__(self, index: int) -> ListNode:
        self.get(index=index)

    def __delitem__(self, index: int) -> None:
        self.remove(index=index)

    def insert(self, index: int, value: Any) -> None:
        """Insert a new node at the index-th with the given value."""
        _validate_index(index=index, lower_bound=0, upper_bound=self._len)

        current = self.head
        new_node = ListNode(value=value)

        if index == 0:
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if index == self._len:
                self.tail = self.tail.next

        self._len += 1

    def prepend(self, value: Any) -> None:
        """Add a new node with the given value at the begin of the linked list."""
        self.insert(index=0, value=value)

    def append(self, value: Any) -> None:
        """Add a new node with the given value at the end of the linked list."""
        self.insert(index=self._len, value=value)

    def get(self, index: int) -> ListNode:
        """Return the index-th node in the linked list, if the index is valid."""
        _validate_index(index=index, lower_bound=0, upper_bound=self._len)
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def remove(self, index: int) -> None:
        """Remove the index-th node in the linked list, if the index is valid."""
        _validate_index(index=index, lower_bound=0, upper_bound=self._len)
        current = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next
            if index == self._len:
                self.tail = current
        self._len -= 1



