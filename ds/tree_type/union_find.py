from ds._validators import _validate_capacity

__all__ = ["UnionFind"]


class UnionFind:
    def __new__(cls, capacity: int) -> "UnionFind":
        _validate_capacity(capacity=capacity)
        return super().__new__(cls)

    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._parent = list(range(capacity))
        self._rank = [1] * capacity

    def _validate_element(self, value: int) -> None:
        """Private method to validate a given input."""
        if not isinstance(value, int):
            raise TypeError(f"Expected an integer. But got {type(value)}.")
        if not (0 <= value < self._capacity):
            raise ValueError(
                f"Input must be between 0 and {self._capacity}. But got {value}"
            )

    def find(self, x: int) -> int:
        """
        Find the root representative of the given element using path compression.
        Time Complexity: O(1).
        """
        self._validate_element(x)
        if self._parent[x] != x:
            self._parent[x] = self.find(self._parent[x])
        return self._parent[x]

    def union(self, x: int, y: int) -> None:
        """
        Unite the sets containing the given elements using union by rank.
        Time Complexity: O(1).
        """
        self._validate_element(x), self._validate_element(y)

        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            # Attach the smaller tree to the larger tree
            if self._rank[root_x] > self._rank[root_y]:
                self._parent[root_y] = root_x
            elif self._rank[root_x] < self._rank[root_y]:
                self._parent[root_x] = root_y
            else:
                self._parent[root_y] = root_x
                self._rank[root_x] += 1

    def connected(self, x: int, y: int) -> bool:
        """
        Checks if x and y belong to the same set.
        Time Complexity: O(1).
        """
        self._validate_element(x), self._validate_element(y)
        return self.find(x) == self.find(y)
