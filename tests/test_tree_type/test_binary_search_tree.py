from ds import BinarySearchTree


sample_values = [50, 30, 20, 40, 70, 60, 80]


def test_tree_instantiation():
    """Test if Binary Search Tree is instantiated correctly with sorted input."""
    bst = BinarySearchTree([50, 30, 20, 40, 70, 60, 80])
    assert bst.root.value == 50  # Root node
    assert bst.root.left.value == 30
    assert bst.root.right.value == 70


def test_insertion():
    """Test insertion of new elements into the Binary Search Tree."""
    bst = BinarySearchTree([50, 30, 20, 40, 70, 60, 80])
    bst.insert(65)
    assert (
        bst.root.right.left.right.value == 65
    )  # New node should be on the right subtree

    bst.insert(25)
    assert (
        bst.root.left.left.right.value == 25
    )  # New node should be on the left subtree


def test_find_existing_element():
    """Test finding an existing element in the Binary Search Tree."""
    bst = BinarySearchTree([50, 30, 20, 40, 70, 60, 80])
    found_node = bst.find(70)
    assert found_node is not None
    assert found_node.value == 70


def test_find_non_existing_element():
    """Test searching for a non-existing element in the Binary Search Tree."""
    bst = BinarySearchTree([50, 30, 20, 40, 70, 60, 80])
    found_node = bst.find(100)
    assert found_node is None


def test_delete_leaf_node():
    """Test deleting a leaf node (no children) from the Binary Search Tree."""
    bst = BinarySearchTree([50, 30, 20, 40, 70, 60, 80])
    node_to_delete = bst.find(20)
    bst.delete(node_to_delete)

    assert bst.find(20) is None  # Node should no longer exist in the tree
    assert bst.root.left.left is None  # Parent's reference should be removed


def test_delete_node_with_one_child():
    """Test deleting a node with one child from the Binary Search Tree."""
    bst = BinarySearchTree([50, 30, 20, 40, 70, 60, 80])
    bst.insert(25)  # Make sure 20 has a right child 25
    node_to_delete = bst.find(20)
    bst.delete(node_to_delete)

    assert bst.find(20) is None  # Node 20 should be deleted
    assert bst.root.left.left.value == 25  # 25 should take the place of 20


def test_delete_node_with_two_children():
    """Test deleting a node with two children from the Binary Search Tree."""
    bst = BinarySearchTree([50, 30, 20, 40, 70, 60, 80])
    node_to_delete = bst.find(30)
    bst.delete(node_to_delete)

    # After deletion, the successor (40) should take 30's place
    assert bst.root.left.value == 40
    assert bst.find(30) is None


def test_preorder_traversal():
    """Test preorder traversal of the Binary Search Tree."""
    bst = BinarySearchTree([50, 30, 20, 40, 70, 60, 80])
    result = bst.preorder_traversal()
    assert result == [50, 30, 20, 40, 70, 60, 80]


def test_inorder_traversal():
    """Test inorder traversal of the Binary Search Tree."""
    bst = BinarySearchTree([50, 30, 20, 40, 70, 60, 80])
    result = bst.inorder_traversal()
    assert result == sorted(
        sample_values
    )  # In-order traversal should give sorted result


def test_postorder_traversal():
    """Test postorder traversal of the Binary Search Tree."""
    bst = BinarySearchTree([50, 30, 20, 40, 70, 60, 80])
    result = bst.postorder_traversal()
    assert result == [20, 40, 30, 60, 80, 70, 50]


def test_levels_traversal():
    """Test level-order traversal of the Binary Search Tree."""
    bst = BinarySearchTree([50, 30, 20, 40, 70, 60, 80])
    result = bst.levels_traversal()
    expected = [
        [50],
        [30, 70],
        [20, 40, 60, 80],
    ]
    assert result == expected
