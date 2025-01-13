import pytest
from ds import MaxPriorityQueue


@pytest.fixture
def empty_pq():
    return MaxPriorityQueue()


@pytest.fixture
def sample_pq():
    return MaxPriorityQueue([(1, "low"), (2, "medium"), (3, "high")])


def test_initialization_empty():
    pq = MaxPriorityQueue()
    assert len(pq) == 0
    assert bool(pq) is False


def test_initialization_with_items():
    items = [(1, "low"), (2, "medium"), (3, "high")]
    pq = MaxPriorityQueue(items)
    assert len(pq) == 3
    assert bool(pq) is True


def test_initialization_with_duplicate_priorities():
    items = [(1, "first"), (1, "second"), (2, "medium")]
    pq = MaxPriorityQueue(items)
    assert len(pq) == 3


def test_initialization_invalid_input():
    invalid_inputs = [
        ((1,), TypeError),  # Tuple too short
        ([(1, "a", "b")], ValueError),  # Tuple too long
        ([1, 2, 3], TypeError),  # Not tuples/lists
        ("invalid", TypeError),  # Not a sequence
    ]
    for invalid_input, error in invalid_inputs:
        with pytest.raises(error):
            MaxPriorityQueue(invalid_input)


def test_insert(empty_pq):
    empty_pq.enqueue(1, "low")
    assert len(empty_pq) == 1
    assert empty_pq.peek() == "low"


def test_insert_multiple_same_priority(empty_pq):
    empty_pq.enqueue(1, "first")
    empty_pq.enqueue(1, "second")
    assert len(empty_pq) == 2

    # Items should be returned in FIFO order for same priority
    assert empty_pq.dequeue() == "first"
    assert empty_pq.dequeue() == "second"
    assert len(empty_pq) == 0


def test_pop_empty():
    pq = MaxPriorityQueue()
    with pytest.raises(IndexError, match="pop from empty max priority queue"):
        pq.dequeue()


def test_peek_empty():
    pq = MaxPriorityQueue()
    with pytest.raises(IndexError, match="peek from empty max priority queue"):
        pq.peek()


def test_pop_order(sample_pq):
    # Should return items in priority order (highest first)
    assert sample_pq.dequeue() == "high"
    assert sample_pq.dequeue() == "medium"
    assert sample_pq.dequeue() == "low"
    assert len(sample_pq) == 0


def test_peek(sample_pq):
    # Peek should return the highest priority item without removing it
    assert sample_pq.peek() == "high"
    assert len(sample_pq) == 3
    assert sample_pq.peek() == "high"  # Peek again to verify item wasn't removed


def test_bool_operator():
    pq = MaxPriorityQueue()
    assert not pq  # Empty queue should be False

    pq.enqueue(1, "item")
    assert pq  # Non-empty queue should be True

    pq.dequeue()
    assert not pq  # Empty queue after pop should be False


def test_repr():
    pq = MaxPriorityQueue([(1, "low"), (2, "medium")])
    repr_str = repr(pq)
    assert repr_str == "MaxPriorityQueue((2, medium), (1, low))"


def test_complex_operations():
    pq = MaxPriorityQueue()

    # Insert items with various priorities
    pq.enqueue(3, "high1")
    pq.enqueue(1, "low")
    pq.enqueue(3, "high2")
    pq.enqueue(2, "medium")

    # Check that items come out in correct order
    assert pq.dequeue() == "high1"  # Priority 3
    assert pq.dequeue() == "high2"  # Priority 3
    assert pq.dequeue() == "medium"  # Priority 2
    assert pq.dequeue() == "low"  # Priority 1
