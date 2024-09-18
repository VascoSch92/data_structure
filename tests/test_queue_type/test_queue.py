from ds import Queue


def test_initialize_queue():
    _ = Queue()


def test_initialize_queue_from_sequence():
    _ = Queue([1, 2, 3, 4, 5])


def test_enqueue():
    q = Queue()

    for idx in range(5):
        q.enqueue(idx)
        assert len(q) == idx + 1

    assert q.__repr__() == "Queue(0, 1, 2, 3, 4)"


def test_dequeue():
    q = Queue([1, 2, 3, 4, 5])

    value = 1
    while value < 6:
        tmp = q.dequeue()
        assert tmp == value
        assert len(q) == 5 - value
        value += 1
    assert q.__repr__() == "Queue()"


def test_peek():
    q = Queue([1, 2, 3, 4, 5])

    value = 1
    while value < 6:
        tmp = q.peek()
        assert tmp == value
        q.dequeue()
        value += 1
    assert q.__repr__() == "Queue()"


def test_is_empty():
    q1 = Queue()
    q2 = Queue([1, 2, 3, 4, 5])

    assert q1.is_empty()
    assert q2.is_empty() is False
