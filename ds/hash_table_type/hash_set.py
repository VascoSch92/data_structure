from typing import Optional, Sequence, List, Any

from ds import LinkedList
from ds._validators import _validate_instantiation_from_sequence

__all__ = ["HashSet"]


class HashSet:
    def __new__(
        cls, capacity: int = 100, _from: Optional[Sequence] = None
    ) -> "HashSet":
        _validate_instantiation_from_sequence(sequence=_from, data_structure="hash set")
        if not isinstance(capacity, int):
            raise TypeError(
                f"Wrong type provided for capacity. Expected type `int`, got type {type(capacity)}."
            )
        return super().__new__(cls)

    def __init__(self, capacity: int = 100, _from: Optional[Sequence] = None) -> None:
        """Initialize the HashSet with a fixed capacity."""
        self.capacity = capacity
        self._len = 0
        self._buckets = self._instantiate_object(capacity=capacity, source=_from)

    def _instantiate_object(
        self,
        capacity: int,
        source: Optional[Sequence] = None,
    ) -> List[LinkedList]:
        """Private method to instantiate a hash set from a sequence."""
        buckets = [LinkedList() for _ in range(capacity)]

        if not source:
            return buckets

        for key in source:
            index = self._hash(key)
            bucket = buckets[index].head

            # avoid duplicates
            already_added = False
            while bucket:
                if bucket.value == key:
                    already_added = True
                bucket = bucket.next
            if already_added is False:
                buckets[index].append(key)
                self._len += 1
        return buckets

    def __len__(self) -> int:
        return self._len

    def __str__(self) -> str:
        """String representation of the HashSet for debugging."""
        str_repr = "{"
        for bucket in self._buckets:
            curr = bucket.head
            while curr:
                str_repr += curr.value.__str__()
                str_repr += ", "
                curr = curr.next
        str_repr = str_repr[:-2] if str_repr.endswith(", ") else str_repr
        str_repr += "}"
        return str_repr

    def _hash(self, key: Any) -> int:
        """Private method to generate a hash index for the given key."""
        return hash(key) % self.capacity

    def add(self, item: Any) -> None:
        """
        Add an item into the HashSet.
        Time complexity: O(1).
        """
        index = self._hash(item)
        bucket = self._buckets[index].head
        # avoid duplicates
        while bucket:
            if bucket.value == item:
                return
            bucket = bucket.next
        self._buckets[index].append(item)
        self._len += 1

    def remove(self, item: Any) -> None:
        """
        Remove an item from the HashSet.
        Time complexity: O(1).
        """
        index = self._hash(item)
        bucket = self._buckets[index].head

        key_index = 0
        while bucket:
            if bucket.value == item:
                self._buckets[index].remove(key_index)
                self._len -= 1
                return
            key_index += 1

    def contains(self, item: Any) -> bool:
        """
        Check if an item is in the HashSet.
        Time complexity: O(1).
        """
        index = self._hash(item)
        bucket = self._buckets[index].head
        while bucket:
            if bucket.value == item:
                return True
            bucket = bucket.next
        return False

    def clear(self) -> None:
        """
        Clear the HashSet.
        Time complexity: O(n), where n is len(capacity).
        """
        self._buckets = [LinkedList() for _ in range(self.capacity)]
        self._len = 0
