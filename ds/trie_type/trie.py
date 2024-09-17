from typing import Optional, Sequence


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False


class Trie:
    def __new__(cls, _from: Optional[Sequence[str]] = None) -> "Trie":
        if not isinstance(_from, Sequence) and _from:
            raise TypeError(
                f"Creation of a trie from type {type(_from)} not supported."
            )
        return super().__new__(cls)

    def __init__(self, _from: Optional[Sequence[str]] = None) -> None:
        self.root = self._instantiate_object(source=_from)

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
        Add a word in the trie.
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
        Search if a word is in the trie.
        Time complexity: O(n), where n is the length of the word.
        """
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
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

