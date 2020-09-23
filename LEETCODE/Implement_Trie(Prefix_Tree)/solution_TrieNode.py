from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for char in word:
            current = current.children[char]
        current.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return current.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for char in prefix:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
