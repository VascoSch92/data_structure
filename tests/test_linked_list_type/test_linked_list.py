from ds import LinkedList

VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_initialize_linked_list():
    _ = LinkedList()


def test_initialize_linked_list_from_list():
    _ = LinkedList(_from=VALUES)


def test_initialize_linked_list_from_tuple():
    _ = LinkedList(_from=tuple(VALUES))


def test_get_item() -> None:
    linked_list = LinkedList(VALUES)
    for idx, value in enumerate(VALUES):
        assert linked_list.get(idx).value == value


def test_prepend() -> None:
    linked_list = LinkedList()
    for value in VALUES:
        linked_list.prepend(value)
        assert linked_list.head.value == value


def test_append() -> None:
    linked_list = LinkedList()
    for value in VALUES:
        linked_list.append(value)
        assert linked_list.tail.value == value


def test_remove() -> None:
    linked_list = LinkedList(VALUES)
    linked_list.remove(0)
    assert linked_list.head.value == VALUES[1]
