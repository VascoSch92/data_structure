from ds import MatchTrie


def test_initialize_trie():
    _ = MatchTrie()


def test_initialize_trie_from_sequence():
    _ = MatchTrie(["hello", "world"])


def test_add_search_remove():
    trie = MatchTrie()

    trie.add("hello")
    assert trie.search("hello")
    assert trie.search(".ello")
    assert trie.search("h.llo")
    assert trie.search("h...o")
    assert trie.search("hell.")

    trie.remove("hello")
    assert not trie.search("hello")
    assert not trie.search(".ello")
    assert not trie.search("h.llo")
    assert not trie.search("h...o")
    assert not trie.search("hell.")
