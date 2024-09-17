# Data Structure

---

A collection of data structure for Python

## Overview
- [Linked List Type](#linked-list-type)
  - [Linked List](#linked-list)
- [Stack Type](#stack-type)
  - [Stack](#stack)
  - [MinMaxStack](#minmaxstack)
- [Trie Type](#trie-type)
  - [Trie](#trie)

## Linked List Type

---

### Linked List

| **Method** | **Description**                                                       | **Time Complexity** |    
|------------|-----------------------------------------------------------------------|---------------------|
| `prepend`  | Add a new node with the given value at the begin of the linked list.  | O(1)                | 
| `append`   | Add a new node with the given value at the end of the linked list.    | O(1)                | 
| `insert`   | Insert a new node at the index-th with the given value.               | O(n)                | 
| `get`      | Return the index-th node in the linked list, if the index is valid.   | O(n)                | 
| `remove`   | Remove the index-th node in the linked list, if the index is valid.   | O(n)                |
| `is_empty` | Return `True` if the linked list is empty. `False`, otherwise.        | O(1)                | 

## Stack Type

---

### Stack

| **Method** | **Description**                                          | **Time Complexity** |    
|------------|----------------------------------------------------------|---------------------|
| `pop`      | Delete and return the last element added to the stack.   | O(1)                | 
| `push`     | Push the element `value` at the top of the stack.        | O(1)                | 
| `peek`     | Return the last element added to the stack.              | O(1)                |
| `is_empty` | Return `True` if the stack is empty. `False`, otherwise. | O(1)                | 

### MinMaxStack

| **Method** | **Description**                                          | **Time Complexity** |    
|------------|----------------------------------------------------------|---------------------|
| `pop`      | Delete and return the last element added to the stack.   | O(1)                | 
| `push`     | Push the element `value` at the top of the stack.        | O(1)                | 
| `peek`     | Return the last element added to the stack.              | O(1)                | 
| `min`      | Return the min element presents in the stack.            | O(1)                | 
| `max`      | Return the max element presents in the stack.            | O(1)                | 
| `is_empty` | Return `True` if the stack is empty. `False`, otherwise. | O(1)                | 

## Trie Type

---

### Trie

| **Method**   | **Description**                                           | **Time Complexity** |    
|--------------|-----------------------------------------------------------|---------------------|
| `add`        | Add a word in the trie.                                   | O(n)                | 
| `search`     | Search if a word is in the trie.                          | O(n)                | 
| `startswith` | Search if a word in the trie start with the given prefix. | O(n)                | 
| `remove`     | Remove the given word from the trie.                      | O(n)                | 


