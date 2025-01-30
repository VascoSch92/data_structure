import pytest
from ds import UnionFind


def test_initialization():
    uf = UnionFind(5)
    assert uf._parent == [0, 1, 2, 3, 4]
    assert uf._rank == [1, 1, 1, 1, 1]
    assert uf.components == 5


def test_find():
    uf = UnionFind(5)
    assert uf.find(0) == 0
    assert uf.find(4) == 4
    assert uf.components == 5


def test_union():
    uf = UnionFind(5)
    assert uf.components == 5

    uf.union(0, 1)
    assert uf.find(0) == uf.find(1)
    assert uf.components == 4


def test_connected():
    uf = UnionFind(5)
    assert uf.components == 5

    uf.union(0, 1)
    assert uf.components == 4

    uf.union(1, 2)
    assert uf.connected(0, 2) is True
    assert uf.connected(3, 4) is False
    assert uf.components == 3


def test_union_by_rank():
    uf = UnionFind(5)
    assert uf.components == 5

    uf.union(0, 1)
    assert uf.components == 4

    uf.union(2, 3)
    assert uf.components == 3

    uf.union(1, 3)
    assert uf.find(0) == uf.find(3)
    assert uf.components == 2


def test_path_compression():
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(2, 3)
    uf.find(3)
    assert uf._parent[3] == uf.find(0)


@pytest.mark.parametrize(
    "capacity, element, error",
    [(5, 10, ValueError), (5, -10, ValueError), (5, "4", TypeError)],
)
def test_invalid_access(capacity, element, error):
    uf = UnionFind(capacity)
    with pytest.raises(error):
        uf.find(element)
