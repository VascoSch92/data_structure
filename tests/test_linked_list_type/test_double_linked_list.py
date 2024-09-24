from ds import DoubleLinkedList

VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_initialize_linked_list():
    _ = DoubleLinkedList()


def test_initialize_linked_list_from_list():
    _ = DoubleLinkedList(_from=VALUES)


def test_initialize_linked_list_from_tuple():
    _ = DoubleLinkedList(_from=tuple(VALUES))


def test_get_item() -> None:
    linked_list = DoubleLinkedList(VALUES)
    for idx, value in enumerate(VALUES):
        assert linked_list.get(idx).value == value


def test_prepend() -> None:
    linked_list = DoubleLinkedList()
    for value in VALUES:
        linked_list.prepend(value)
        assert linked_list.head.value == value


def test_remove() -> None:
    linked_list = DoubleLinkedList(VALUES)
    linked_list.remove(0)
    assert linked_list.head.value == VALUES[1]


def test_prev_next() -> None:
    linked_list = DoubleLinkedList(VALUES)
    head = linked_list.head
    prev = None
    for value in VALUES:
        head.value = value
        if head.prev:
            head.prev.value = prev
        else:
            head.prev = prev
        head = head.next
        prev = value
