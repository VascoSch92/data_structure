from ds import Stack


def test_initialize_stack():
    _ = Stack()


def test_initialize_stack_from_sequence():
    _ = Stack([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def test_push():
    stack = Stack()
    for j in range(1, 11):
        stack.push(j)
        assert len(stack) == j


def test_pop():
    stack = Stack([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    value = 10
    while stack:
        assert stack.pop() == value
        assert len(stack) == value - 1
        value -= 1


def test_peek():
    stack = Stack([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    value = 10
    while stack:
        assert stack.peek() == value
        assert len(stack) == value
        stack.pop()
        value -= 1
