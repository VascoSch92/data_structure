import collections
from typing import Any, Optional, Sequence, List

__all__ = ["TreeNode", "Tree"]


class TreeNode:
    """Base node for a tree."""

    def __init__(
        self,
        value: Any = None,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        value = self.value.__str__() if self.value else None
        left = self.left.value.__str__() if self.left else None
        right = self.right.value.__str__() if self.right else None
        return f"TreeNode(value={value}, left={left}, right={right})"


class Tree:
    def __new__(cls, _from: Optional[Sequence] = None) -> "Tree":
        if not isinstance(_from, Sequence) and _from:
            raise TypeError(
                f"Creation of a tree from type {type(_from)} not supported."
            )
        return super().__new__(cls)

    def __init__(self, _from: Optional[Sequence] = None) -> None:
        self.root = self._instantiate_object(source=_from)

    @staticmethod
    def _instantiate_object(source: Optional[Sequence]) -> Optional[TreeNode]:
        """Private method to instantiate a tree."""
        if not source:
            return None

        root = TreeNode(value=source[0])
        nodes = [root]

        for idx, value in enumerate(source[1:]):
            if value:
                parent = nodes[idx // 2]
                new_node = TreeNode(value=value)

                if idx % 2 == 0:
                    parent.left = new_node
                else:
                    parent.right = new_node

                nodes.append(new_node)

        return root

    def preorder_traversal(self) -> List[Any]:
        """
        Return the preorder traversal of the tree.
        Time complexity: O(n), where n is the number of elements of the tree.
        """
        return self._preorder_traversal(node=self.root, values=[])

    def _preorder_traversal(self, node: TreeNode, values: List) -> List[Any]:
        """Private method to compute the preorder traversal of a tree."""
        if not node:
            return values
        values.append(node.value)
        self._preorder_traversal(node=node.left, values=values)
        self._preorder_traversal(node=node.right, values=values)
        return values

    def inorder_traversal(self) -> List[Any]:
        """
        Return the inorder traversal of the tree.
        Time complexity: O(n), where n is the number of elements of the tree.
        """
        return self._inorder_traversal(node=self.root, values=[])

    def _inorder_traversal(self, node: TreeNode, values: List) -> List[Any]:
        """Private method to compute the inorder traversal of a tree."""
        if not node:
            return values
        self._preorder_traversal(node=node.left, values=values)
        values.append(node.value)
        self._preorder_traversal(node=node.right, values=values)
        return values

    def postorder_traversal(self) -> List[Any]:
        """
        Return the postorder traversal of the tree.
        Time complexity: O(n), where n is the number of elements of the tree.
        """
        return self._postorder_traversal(node=self.root, values=[])

    def _postorder_traversal(self, node: TreeNode, values: List) -> List[Any]:
        """Private method to compute the postorder traversal of a tree."""
        if not node:
            return values
        self._preorder_traversal(node=node.left, values=values)
        self._preorder_traversal(node=node.right, values=values)
        values.append(node.value)
        return values

    def levels_traversal(self) -> List[List[Any]]:
        """
        Return the level order of the tree.
        Time complexity: O(n), where n is the number of elements of the tree.
        """
        q = collections.deque([self.root])

        levels = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.value)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                levels.append(level)

        return levels
