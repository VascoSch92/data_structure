from ds import Trie


def test_initialize_trie():
    _ = Trie()


def test_initialize_trie_from_sequence():
    _ = Trie(['hello', 'world'])


def test_add_search_remove():
    trie = Trie()

    trie.add('hello')
    assert trie.search('hello')

    trie.remove('hello')
    assert not trie.search('hello')




