from ds import MinMaxStack


def test_initialize_stack():
    _ = MinMaxStack()


def test_push():
    stack = MinMaxStack()
    for j in range(1, 11):
        stack.push(j)
        assert len(stack) == j
        assert stack.max() == j
        assert stack.min() == 1
