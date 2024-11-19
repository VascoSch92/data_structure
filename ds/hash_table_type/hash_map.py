from typing import Any, Tuple, Literal, Generator

from ds import LinkedList
from ds._validators import _validate_capacity

__all__ = ["HashMap"]


class HashMap:
    def __new__(cls, capacity: int = 100) -> "HashMap":
        _validate_capacity(capacity=capacity)
        return super().__new__(cls)

    def __init__(self, capacity: int = 100) -> None:
        """Initialize the HashSet with a fixed capacity."""
        self._capacity = capacity
        self._len = 0
        self._buckets = [LinkedList() for _ in range(capacity)]

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
        return hash(key) % self._capacity

    def get(self, key: Any, other: Any = None) -> Any:
        """
        Get the value of the given key or `other` if the given is not found.
        Time complexity: O(1).
        """
        index = self._hash(key)
        bucket = self._buckets[index].head

        while bucket:
            if bucket.value[0] == key:
                return bucket.value[1]
            bucket = bucket.next

        return other

    def add(self, item: Tuple[Any, Any]) -> None:
        """
        Add an item, a couple (key, value), into the HashMap.
        Time complexity: O(1).
        """
        key, value = item
        index = self._hash(key)
        bucket = self._buckets[index].head
        # avoid duplicates
        while bucket:
            if bucket.value[0] == key:
                bucket.value = (key, value)
                return
            bucket = bucket.next
        self._buckets[index].append(item)
        self._len += 1

    def remove(self, key: Any) -> None:
        """
        Remove a key, and the respective value, from the HashMap.
        Time complexity: O(1).
        """
        index = self._hash(key)
        bucket = self._buckets[index].head

        key_index = 0
        while bucket:
            if bucket.value[0] == key:
                self._buckets[index].remove(key_index)
                self._len -= 1
                return
            bucket = bucket.next
            key_index += 1

    def keys(self) -> Generator:
        """
        Retrieve the keys of the Hash Map as generator.
        Time complexity: O(n), where n is the length of the Hash Map.
        """
        return self._retrieve_hash_map_elements(type_="keys")

    def values(self) -> Generator:
        """
        Retrieve the values of the Hash Map as generator.
        Time complexity: O(n), where n is the length of the Hash Map.
        """
        return self._retrieve_hash_map_elements(type_="values")

    def items(self) -> Generator:
        """
        Retrieve the pairs (key, value) of the Hash Map as generator.
        Time complexity: O(n), where n is the length of the Hash Map.
        """
        return self._retrieve_hash_map_elements(type_="items")

    def _retrieve_hash_map_elements(
        self, type_: Literal["keys", "values", "items"]
    ) -> Generator:
        """Private method to retrieve specific elements from the hash table."""
        for bucket in self._buckets:
            curr = bucket.head
            while curr:
                if type_ == "keys":
                    yield curr.value[0]
                elif type_ == "values":
                    yield curr.value[1]
                else:
                    yield curr.value
                curr = curr.next

    def clear(self) -> None:
        """
        Clear the HashMap.
        Time complexity: O(n), where n is len(capacity).
        """
        self._buckets = [LinkedList() for _ in range(self._capacity)]
        self._len = 0
