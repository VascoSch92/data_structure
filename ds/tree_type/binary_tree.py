import collections
from typing import Any, Optional, Sequence, List
from ds._validators import _validate_instantiation_from_sequence

__all__ = ["BinaryTreeNode", "BinaryTree"]


class BinaryTreeNode:
    """Base node for a tree."""

    def __init__(
        self,
        value: Any = None,
        left: Optional["BinaryTreeNode"] = None,
        right: Optional["BinaryTreeNode"] = None,
        parent: Optional["BinaryTreeNode"] = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self) -> str:
        value = self.value.__str__() if self.value else None
        left = self.left.value.__str__() if self.left else None
        right = self.right.value.__str__() if self.right else None
        parent = self.parent.value.__str__() if self.parent else None
        return f"{self.__class__.__name__}(value={value}, left={left}, right={right}, parent={parent})"

    def __bool__(self) -> bool:
        return self.value is not None


class BinaryTree:
    def __new__(cls, _from: Optional[Sequence] = None) -> "BinaryTree":
        _validate_instantiation_from_sequence(sequence=_from, data_structure="tree")
        return super().__new__(cls)

    def __init__(self, _from: Optional[Sequence] = None) -> None:
        self.root = self._instantiate_object(source=_from)

    @staticmethod
    def _instantiate_object(source: Optional[Sequence]) -> Optional[BinaryTreeNode]:
        """Private method to instantiate a tree."""
        if not source:
            return None

        root = BinaryTreeNode(value=source[0])
        nodes = [root]

        for idx, value in enumerate(source[1:]):
            if value:
                parent = nodes[idx // 2]
                new_node = BinaryTreeNode(value=value, parent=parent)

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

    def _preorder_traversal(self, node: BinaryTreeNode, values: List) -> List[Any]:
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

    def _inorder_traversal(self, node: BinaryTreeNode, values: List) -> List[Any]:
        """Private method to compute the inorder traversal of a tree."""
        if not node:
            return values
        values = self._inorder_traversal(node=node.left, values=values)
        values.append(node.value)
        values = self._inorder_traversal(node=node.right, values=values)
        return values

    def postorder_traversal(self) -> List[Any]:
        """
        Return the postorder traversal of the tree.
        Time complexity: O(n), where n is the number of elements of the tree.
        """
        return self._postorder_traversal(node=self.root, values=[])

    def _postorder_traversal(self, node: BinaryTreeNode, values: List) -> List[Any]:
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
