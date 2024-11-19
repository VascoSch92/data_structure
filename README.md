# Data Structure

---

A collection of data structure for Python.

## Overview

| **Data Structure**                        | **Description**                                                                                                    | **Type**                              |    
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| [Linked List](#linked-list)               | Linear data structure where elements, called nodes, are stored in a sequence.                                      | [Linked List Type](#linked-list-type) | 
| [Double Linked List](#double-linked-list) | Linked list where each node has two references: one for the next node and one for the previous node.               | [Linked List Type](#linked-list-type) | 
| [Stack](#stack)                           | Linear data structure that follows the Last In, First Out (LIFO) principle.                                        | [Stack Type](#stack-type)             | 
| [MinMaxStack](#minmaxstack)               | Regular stack where you can access the minimum and maximum of the elements presents in the stack in constant time. | [Stack Type](#stack-type)             | 
| [Queue](#queue)                           | Linear data structure that follows the First In, First Out (FIFO) principle.                                       | [Queue Type](#queue-type)             | 
| [Tree](#tree)                             | Data structure used to represent hierarchical relationships between elements.                                      | [Tree Type](#tree-type)               | 
| [BinaryTree](#binary-tree)                | A binary tree is nothing but a tree where each node has at maximum 2 children.                                     | [Tree Type](#tree-type)               | 
| [BinarySearchTree](#binary-search-tree)   | A binary tree with special properties on the node values                                                           | [Tree Type](#tree-type)               | 
| [Trie](#trie)                             | Tree-like data structure used to store a dynamic set of strings                                                    | [Trie Type](#trie-type)               |
| [MatchTrie](#match-trie)                  | Regular trie, where you can search words with matching.                                                            | [Trie Type](#trie-type)               |
| [HashSet](#hash-set)                      | Data structure that stores a collection of unique elements                                                         | [Hash Table Type](#hash-table-type)   |


## Linked List Type

---

### Linked List

A linked list is a linear data structure where elements, called nodes, are stored in a sequence. 
Each node contains two parts: the data and a reference (or pointer) to the next node in the sequence. 
The first node is called the head, and the last node points to null, indicating the end of the list. 

#### Instantiation

- Empty: `linked_list = LinkedList()`

- From a Sequence type object: `linked_list = LinkedList(SEQUENCE_TYPE_OBJ)`

#### Attributes
- `head`: the head of the linked list (`ListNode` type)
- `tail`: the tail of the linked list (`ListNode` type)

#### Methods

| **Method** | **Description**                                                       | **Time Complexity** |    
|------------|-----------------------------------------------------------------------|---------------------|
| `prepend`  | Add a new node with the given value at the begin of the linked list.  | O(1)                | 
| `append`   | Add a new node with the given value at the end of the linked list.    | O(1)                | 
| `insert`   | Insert a new node at the index-th with the given value.               | O(n)                | 
| `get`      | Return the index-th node in the linked list, if the index is valid.   | O(n)                | 
| `remove`   | Remove the index-th node in the linked list, if the index is valid.   | O(n)                |
| `is_empty` | Return `True` if the linked list is empty. Otherwise, `False`.        | O(1)                |

### Double Linked List

A doubly linked list is a more complex version of a linked list where each node has two references: 
one pointing to the next node and another pointing to the previous node. 
This bidirectional structure allows traversal in both directions (forward and backward). 
Like a regular linked list, the first node is the head, and the last node is the tail.

#### Instantiation

- Empty: `double_linked_list = DoubleLinkedList()`

- From a Sequence type object: `double_linked_list = DoubleLinkedList(SEQUENCE_TYPE_OBJ)`

#### Attributes
- `head`: the head of the linked list (`DoubleListNode` type)
- `tail`: the tail of the linked list (`DoubleListNode` type)

#### Methods

| **Method** | **Description**                                                             | **Time Complexity** |    
|------------|-----------------------------------------------------------------------------|---------------------|
| `prepend`  | Add a new node with the given value at the begin of the double linked list. | O(1)                | 
| `append`   | Add a new node with the given value at the end of the double linked list.   | O(1)                | 
| `insert`   | Insert a new node at the index-th with the given value.                     | O(n)                | 
| `get`      | Return the index-th node in the double linked list, if the index is valid.  | O(n)                | 
| `remove`   | Remove the index-th node in the double linked list, if the index is valid.  | O(n)                |
| `is_empty` | Return `True` if the double linked list is empty. Otherwise, `False`.       | O(1)                | 

## Stack Type

---

### Stack

A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. 
This means that the last element added to the stack is the first one to be removed. 

#### Instantiation

- Empty: `stack = Stack()`

- From a Sequence type object: `stack = Stack(SEQUENCE_TYPE_OBJ)`

#### Methods

| **Method** | **Description**                                          | **Time Complexity** |    
|------------|----------------------------------------------------------|---------------------|
| `pop`      | Delete and return the last element added to the stack.   | O(1)                | 
| `push`     | Push the element `value` at the top of the stack.        | O(1)                | 
| `peek`     | Return the last element added to the stack.              | O(1)                |
| `is_empty` | Return `True` if the stack is empty. Otherwise, `False`. | O(1)                | 

### MinMaxStack

A regular stack where you can access the minimum and maximum of the elements presents in the stack 
in constant time.

#### Instantiation

- Empty: `stack = MinMaxStack()`

- From a Sequence type object: `stack = MinMaxStack(SEQUENCE_TYPE_OBJ)`

#### Methods

| **Method** | **Description**                                          | **Time Complexity** |    
|------------|----------------------------------------------------------|---------------------|
| `pop`      | Delete and return the last element added to the stack.   | O(1)                | 
| `push`     | Push the element `value` at the top of the stack.        | O(1)                | 
| `peek`     | Return the last element added to the stack.              | O(1)                | 
| `min`      | Return the min element presents in the stack.            | O(1)                | 
| `max`      | Return the max element presents in the stack.            | O(1)                | 
| `is_empty` | Return `True` if the stack is empty. Otherwise, `False`. | O(1)                | 


## Queue Type

---

### Queue

A queue is a linear data structure that follows the First In, First Out (FIFO) principle. 
This means the first element added to the queue is the first one to be removed.

#### Instantiation

- Empty: `queue = Queue()`

- From a Sequence type object: `queue = Queue(SEQUENCE_TYPE_OBJ)`

#### Methods

| **Method** | **Description**                                          | **Time Complexity** |    
|------------|----------------------------------------------------------|---------------------|
| `enqueue`  | Push the element `value` at the end of the queue.        | O(1)                | 
| `dequeue`  | Delete and return the first element of the queue.        | O(1)                | 
| `peek`     | Return the first element of the queue.                   | O(1)                | 
| `is_empty` | Return `True` if the queue is empty. Otherwise, `False`. | O(1)                | 


## Tree Type

---

A tree is a data structure used to represent hierarchical relationships between elements. 
It consists of nodes connected by edges, and it follows a specific organization that resembles a tree in nature.

### Binary Tree

A binary tree is nothing but a tree where each node has at maximum 2 children.

#### Instantiation

- Empty: `binary_tree = BinaryTree()`

- From a Sequence type object: `binary_tree = BinaryTree(SEQUENCE_TYPE_OBJ)`

#### Attributes

- `root`: the root of the tree (`BinaryTreeNode` type)


#### Methods

| **Method**              | **Description**                              | **Time Complexity** |    
|-------------------------|----------------------------------------------|---------------------|
| `preorder_traversal`    | Return the preorder traversal of the tree.   | O(n)                | 
| `inorder_traversal`     | Return the inorder traversal of the tree.    | O(n)                | 
| `postorder_traversal`   | Return the postorder traversal of the tree.  | O(n)                | 
| `levels_traversal`      | Return the level order of the tree.          | O(n)                | 


### Binary Search Tree

A Binary Search Tree (BST) is a Binary Tree with the following two properties
for every node:

- All values in the left subtree of the node are smaller than the node's value.

- All values in the right subtree of the node are greater than the node's value.

It allows efficient searching, insertion, and deletion.

#### Instantiation

- Empty: `binary_search_tree = BinarySearchTree()`

- From a Sequence type object: `binary_search_tree = BinaryTree(SEQUENCE_TYPE_OBJ)`

#### Attributes

- `root`: the root of the tree (`BinaryTreeNode` type)

#### Methods

| **Method**         | **Description**                                          | **Time Complexity** |    
|--------------------|----------------------------------------------------------|---------------------|
| `insert`           | Insert a node into the binary search tree.               | O(log(n))           | 
| `delete`           | Delete a node from the binary search tree.               | O(log(n))           | 
| `find`             | Return the node with the given value if found else None. | O(log(n))           |

**Note**: All methods of the class `BinaryTree` are also inherited by the class `BinarySearchTree`.


## Trie Type

---

### Trie

A Trie (pronounced "try") is a tree-like data structure used to store a dynamic set of strings, 
where each node represents a single character of a string. 
It is especially efficient for searching words, making it useful for applications like autocomplete, 
spell checking, and prefix-based searches.

#### Instantiation

- Empty: `trie = Trie()`

- From a Sequence type object of strings: `trie = Trie(SEQUENCE_TYPE_OBJ)`

#### Methods

| **Method**   | **Description**                                           | **Time Complexity** |    
|--------------|-----------------------------------------------------------|---------------------|
| `add`        | Add a word in the trie.                                   | O(n)                | 
| `search`     | Search if a word is in the trie.                          | O(n)                | 
| `startswith` | Search if a word in the trie start with the given prefix. | O(n)                | 
| `remove`     | Remove the given word from the trie.                      | O(n)                | 

### Match Trie

A regular trie, where you can search words with matching.

Base match character is `'.'`, but you can change it with the parameter `match`.

#### Instantiation

- Empty: `trie = MatchTrie()`

- From a Sequence type object of strings: `trie = MatchTrie(SEQUENCE_TYPE_OBJ)`

#### Methods

| **Method**   | **Description**                                                 | **Time Complexity** |    
|--------------|-----------------------------------------------------------------|---------------------|
| `add`        | Add a word in the match trie.                                   | O(n)                | 
| `search`     | Search if a word is in match the trie.                          | O(n)                | 
| `startswith` | Search if a word in the match trie start with the given prefix. | O(n)                | 
| `remove`     | Remove the given word from the trie.                            | O(n)                | 


## Hash Table Type

### Hash Set

A hash set is a data structure, implemented with a hash table, that stores a collection of unique elements, 
offering efficient operations such as insertion, deletion, and lookup.

#### Instantiation

- Empty: `hash_set = HashSet()`

- From a Sequence type object of strings: `hash_set = HashSet(SEQUENCE_TYPE_OBJ)`

#### Methods

| **Method** | **Description**                     | **Time Complexity** |    
|------------|-------------------------------------|---------------------|
| `add`      | Add an item into the HashSet.       | O(1)                | 
| `remove`   | Remove an item from the HashSet.    | O(1)                | 
| `contains` | Check if an item is in the HashSet. | O(1)                | 
| `clear`    | Clear the HashSet.                  | O(n)                | 