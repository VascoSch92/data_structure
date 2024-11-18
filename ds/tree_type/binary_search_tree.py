from ds import BinaryTree, BinaryTreeNode
from typing import Any, Optional, Sequence

__all__ = ["BinarySearchTree"]


class BinarySearchTree(BinaryTree):
    def _instantiate_object(
        self, source: Optional[Sequence]
    ) -> Optional[BinaryTreeNode]:
        """Private method to instantiate a balanced binary search tree."""
        if not source:
            return None

        source = sorted(source)
        return self._construct_binary_search_tree(
            source=source, left=0, right=len(source) - 1
        )

    def _construct_binary_search_tree(
        self,
        source: Sequence,
        left: int,
        right: int,
        parent: Optional[BinaryTreeNode] = None,
    ) -> Optional[BinaryTreeNode]:
        """Private method to construct a binary search tree from a sequence type object."""
        if left > right:
            return None

        mid = left + (right - left) // 2

        node = BinaryTreeNode(value=source[mid])
        node.left = self._construct_binary_search_tree(
            source=source, left=left, right=mid - 1, parent=node
        )
        node.right = self._construct_binary_search_tree(
            source=source, left=mid + 1, right=right, parent=node
        )
        node.parent = parent
        return node

    def insert(self, value: Any) -> None:
        """
        Insert a node with the given value in the binary search tree.
        Time complexity: O(log(n)), where n is the number of elements of the tree.
        """
        if not self.root:
            self.root = BinaryTreeNode(value=value)
        else:
            self._insert(node=self.root, value=value)

    def _insert(self, node: BinaryTreeNode, value: Any) -> None:
        if value == node.value:
            return None
        if value < node.value:
            if node.left:
                self._insert(node=node.left, value=value)
            else:
                node.left = BinaryTreeNode(value=value, parent=node)
        else:
            if node.right:
                self._insert(node=node.right, value=value)
            else:
                node.right = BinaryTreeNode(value=value, parent=node)

    def delete(self, node: BinaryTreeNode) -> None:
        """
        Delete the given node from the binary search tree.
        Time complexity: O(log(n)), where n is the number of elements of the tree.
        """
        if not self.root and not node:
            return None

        elif not node.left and not node.right:
            return self._delete_leaf(node=node)

        elif not node.left or not node.right:
            return self._delete_node_with_one_child(node=node)

        else:
            return self._delete_node_with_two_children(node=node)

    def _delete_leaf(self, node: BinaryTreeNode) -> None:
        if not node.parent:
            self.root = None
        elif node.parent.left == node:
            node.parent.left = None
        else:
            node.parent.right = None

    def _delete_node_with_one_child(self, node: BinaryTreeNode) -> None:
        child = node.left if node.left else node.right
        child.parent = node.parent

        if not node.parent:
            self.root = child
        elif node.parent.left == node:
            node.parent.left = child
        else:
            node.parent.right = child

    def _delete_node_with_two_children(self, node: BinaryTreeNode) -> None:
        successor = node.right
        while successor.left:
            successor = successor.left
        self.delete(node=successor)

        self._insert_successor(node, successor)

    def _insert_successor(self, node, successor):
        if not node.parent:
            self.root = successor
        elif node.parent.left == node:
            node.parent.left = successor
        else:
            node.parent.right = successor
        successor.parent = node.parent
        successor.left = node.left
        node.left.parent = successor
        successor.right = node.right
        if node.right:
            node.right.parent = successor

    def find(self, target: Any) -> Optional[BinaryTreeNode]:
        """
        Return the node with the given value if found else None.
        Time complexity: O(log(n)), where n is the number of elements of the tree.
        """
        current = self.root
        while current and current.value != target:
            if target < current.value:
                current = current.left
            else:
                current = current.right
        return current
