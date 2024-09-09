import pytest
from ds import ListNode


def test_initialize():
    _ = ListNode()


@pytest.mark.parametrize(
    "value, next",
    [(1, None), ("str", None), ([], ListNode())],
)
def test_initialized_different_parameters(value, next) -> None:
    _ = ListNode(value=value, next=next)
