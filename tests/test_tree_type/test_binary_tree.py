import pytest
from ds import BinaryTree, BinaryTreeNode


def test_tree_node_creation():
    node = BinaryTreeNode(value=10)
    assert node.value == 10
    assert node.left is None
    assert node.right is None


def test_tree_node_representation():
    node = BinaryTreeNode(value=20, left=BinaryTreeNode(10), right=BinaryTreeNode(30))
    assert repr(node) == "BinaryTreeNode(value=20, left=10, right=30, parent=None)"


def test_empty_tree_creation():
    tree = BinaryTree()
    assert tree.root is None


def test_tree_creation_from_sequence():
    sequence = [10, 20, 30, 40, 50]
    tree = BinaryTree(sequence)
    assert tree.root.value == 10
    assert tree.root.left.value == 20
    assert tree.root.right.value == 30
    assert tree.root.left.left.value == 40
    assert tree.root.left.right.value == 50


def test_tree_creation_with_invalid_type():
    with pytest.raises(TypeError):
        BinaryTree(123)


def test_preorder_traversal():
    sequence = [10, 20, 30, 40, 50]
    tree = BinaryTree(sequence)
    assert tree.preorder_traversal() == [10, 20, 40, 50, 30]


def test_inorder_traversal():
    sequence = [10, 20, 30, 40, 50]
    tree = BinaryTree(sequence)
    assert tree.inorder_traversal() == [40, 20, 50, 10, 30]


def test_postorder_traversal():
    sequence = [10, 20, 30, 40, 50]
    tree = BinaryTree(sequence)
    assert tree.postorder_traversal() == [40, 50, 20, 30, 10]


def test_levels_traversal():
    sequence = [10, 20, 30, 40, 50]
    tree = BinaryTree(sequence)
    assert tree.levels_traversal() == [[10], [20, 30], [40, 50]]


def test_empty_tree_traversal():
    tree = BinaryTree()
    assert tree.preorder_traversal() == []
    assert tree.inorder_traversal() == []
    assert tree.postorder_traversal() == []
    assert tree.levels_traversal() == []
