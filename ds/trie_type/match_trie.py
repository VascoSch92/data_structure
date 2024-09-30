from typing import Optional, Sequence
from ds.trie_type.trie import TrieNode
from ds._validators import _validate_instantiation_from_sequence

__all__ = ["MatchTrie"]


class MatchTrie:
    def __new__(
        cls, _from: Optional[Sequence[str]] = None, match: str = "."
    ) -> "MatchTrie":
        _validate_instantiation_from_sequence(
            sequence=_from, data_structure="match trie"
        )
        if not isinstance(match, str):
            raise TypeError(
                f"Parameter match must be of type string, but got {type(str)}."
            )
        return super().__new__(cls)

    def __init__(self, _from: Optional[Sequence[str]] = None, match: str = ".") -> None:
        self.root = self._instantiate_object(source=_from)
        self._match = match

    @staticmethod
    def _instantiate_object(source: Optional[Sequence[str]] = None) -> TrieNode:
        root = TrieNode()
        if not source:
            return root

        curr = root
        for word in source:
            for w in word:
                if w not in curr.children:
                    curr.children[w] = TrieNode()
                curr = curr.children[w]
            curr.end = True
        return root

    def add(self, word: str) -> None:
        """
        Add a word in the match trie.
        Time complexity: O(n).
        """
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Search if a word is in the match trie.
        Time complexity: O(n), where n is the length of the word.
        """
        return self._search(word, 0, self.root)

    def _search(self, word: str, start: int, node: TrieNode) -> bool:
        curr = node
        for i in range(start, len(word)):
            c = word[i]
            if c == self._match:
                for child in curr.children.values():
                    if self._search(word, i + 1, child):
                        return True
                return False
            else:
                if c not in curr.children:
                    return False
                curr = curr.children[c]
        return curr.end

    def startswith(self, prefix: str) -> bool:
        """
        Search if a word in the trie start with the given prefix.
        Time complexity: O(n), where n is the length of the prefix.
        """
        curr = self.root
        for w in prefix:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return True

    def remove(self, word: str) -> None:
        """
        Remove the given word from the trie.
        Time complexity: O(n), where n is the length of the word.
        """
        self._remove(node=self.root, word=word, depth=0)

    def _remove(self, node: TrieNode, word: str, depth: int) -> bool:
        """Private method to remove a word."""
        if not node:
            return True

        if depth == len(word):
            if node.end:
                node.end = False
            return len(node.children) == 0

        char = word[depth]
        if char in node.children and self._remove(node.children[char], word, depth + 1):
            del node.children[char]
            return len(node.children) == 0 and not node.end

        return False
