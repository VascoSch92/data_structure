import pytest
from ds import LinkedList


@pytest.mark.parametrize(
    "_from",
    [
        None,
        [1, 2, 3, 4],
        (1, 2, 3, 4)
    ]
)
def test_initialize_linked_list(_from):
    _ = LinkedList(_from=_from)


@pytest.mark.parametrize(
    "_from",
    [
        [1, 2, 3, 4],
        (1, 2, 3, 4)
    ]
)
def test_get_item(_from) -> None:
    linked_list = LinkedList(_from)
    for j in range(len(_from)):
        assert linked_list[j].value == _from[j]
